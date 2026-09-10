import json
import os
import shutil
import uuid
from copy import deepcopy
from typing import Any, Dict, List, Optional, Set

from . import assets
from . import util
from ._script_file_segments import _ScriptFileSegmentOps
from ._script_file_template import _ScriptFileTemplateOps
from ._script_file_tracks import _ScriptFileTrackOps
from .draft_content_loader import FallbackLoader, load_draft_content
from .script_material import ScriptMaterial
from .template_mode import ImportedTrack, import_track
from .track import BaseTrack, Track

MATERIALS_DIR_NAME = "materials"
"""草稿文件夹内存放内联素材的子目录名"""


class ScriptFile(_ScriptFileTrackOps, _ScriptFileSegmentOps, _ScriptFileTemplateOps):
    """剪映草稿文件, 大部分接口定义在此"""

    save_path: Optional[str]
    """草稿文件保存路径, 仅在模板模式下有效"""
    content: Dict[str, Any]
    """草稿文件内容"""

    width: int
    """视频的宽度, 单位为像素"""
    height: int
    """视频的高度, 单位为像素"""
    fps: int
    """视频的帧率"""
    duration: int
    """视频的总时长, 单位为微秒"""

    maintrack_adsorb: bool
    """是否启用主轨道吸附（主轨磁吸）"""

    materials: ScriptMaterial
    """草稿文件中的素材信息部分"""
    tracks: Dict[str, Track]
    """轨道信息"""

    imported_materials: Dict[str, List[Dict[str, Any]]]
    """导入的素材原始信息, 读取时推荐走带自动补空的`_get_imported_material_list`方法"""
    imported_tracks: List[ImportedTrack]
    """导入的轨道信息"""
    _track_ref_owner_id: str
    """用于校验 TrackRef 归属的内部标识"""

    def __init__(self, width: int, height: int, fps: int, maintrack_adsorb: bool):
        """**创建剪映草稿推荐使用`DraftFolder.create_draft()`而非此方法**

        Args:
            width (int): 视频宽度, 单位为像素
            height (int): 视频高度, 单位为像素
            fps (int): 视频帧率
            maintrack_adsorb (bool): 是否启用主轨道吸附（主轨磁吸）

        Raises:
            无
        """
        self.save_path = None

        self.width = width
        self.height = height
        self.fps = fps
        self.duration = 0
        self.maintrack_adsorb = maintrack_adsorb

        self.materials = ScriptMaterial()
        self.tracks = {}

        self.imported_materials = {}
        self.imported_tracks = []
        self._track_ref_owner_id = uuid.uuid4().hex

        with open(assets.get_asset_path("DRAFT_CONTENT_TEMPLATE"), "r", encoding="utf-8") as f:
            self.content = json.load(f)

    @classmethod
    def _load_template(
        cls,
        json_path: str,
        fallback_loader: Optional[FallbackLoader] = None,
    ) -> "ScriptFile":
        obj = cls(**util.provide_ctor_defaults(cls))
        obj.save_path = json_path
        obj.content = load_draft_content(json_path, fallback_loader=fallback_loader)
        obj.content.setdefault("fps", 30.0)
        obj.content.setdefault("config", {})
        obj.content["config"].setdefault("maintrack_adsorb", True)
        obj.content.setdefault("tracks", [])
        obj.content.setdefault("materials", {})

        for track in obj.content["tracks"]:
            track.setdefault("segments", [])

        util.assign_attr_with_json(obj, ["fps", "duration"], obj.content)
        util.assign_attr_with_json(obj, ["maintrack_adsorb"], obj.content["config"])
        util.assign_attr_with_json(obj, ["width", "height"], obj.content["canvas_config"])

        obj.imported_materials = deepcopy(obj.content["materials"])
        obj.imported_tracks = [
            import_track(track_data, track_order)
            for track_order, track_data in enumerate(obj.content["tracks"])
        ]

        return obj

    def dumps(self) -> str:
        """将草稿文件内容导出为JSON字符串"""
        self.content["fps"] = self.fps
        self.content["duration"] = self.duration
        self.content["config"]["maintrack_adsorb"] = self.maintrack_adsorb
        self.content["canvas_config"] = {"width": self.width, "height": self.height, "ratio": "original"}
        self.content["materials"] = self.materials.export_json()

        for material_type, material_list in self.imported_materials.items():
            if material_type not in self.content["materials"]:
                self.content["materials"][material_type] = material_list
            else:
                self.content["materials"][material_type].extend(material_list)

        track_list: List[BaseTrack] = []
        track_list.extend(self.imported_tracks)
        track_list.extend(self.tracks.values())
        track_list.sort(key=lambda track: track.track_order)
        track_exports = [track.export_json() for track in track_list]
        for export_index, track_json in enumerate(track_exports):
            for segment_json in track_json["segments"]:
                segment_json["render_index"] = export_index
                segment_json["track_render_index"] = 0

        self.content["tracks"] = track_exports

        return json.dumps(self.content, ensure_ascii=False, indent=4)

    def dump(self, file_path: str) -> None:
        """将草稿文件内容写入文件"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(self.dumps())

    @staticmethod
    def _unique_material_name(name: str, used_names: Set[str]) -> str:
        """避开`used_names`中已占用的文件名, 必要时追加序号"""
        if name not in used_names:
            return name

        stem, suffix = os.path.splitext(name)
        index = 1
        while f"{stem}_{index}{suffix}" in used_names:
            index += 1
        return f"{stem}_{index}{suffix}"

    def _inline_materials(self, target_dir: str) -> None:
        """将本地音视频素材复制到`target_dir`并改写素材路径

        剪映默认无权访问 macOS 的桌面/文档/下载目录, 引用这些位置的素材会在打开草稿时
        提示"暂无访问权限"(草稿本身仍能正常解析). 把素材放进草稿文件夹内可绕开该限制,
        也使草稿连同素材可以整体拷贝到另一台机器.

        仅处理本对象创建的本地素材; 模板模式下导入的素材路径由剪映自行管理, 不作改动.

        Args:
            target_dir (`str`): 素材复制到的目标文件夹
        """
        materials = [*self.materials.videos, *self.materials.audios]
        if not materials:
            return

        os.makedirs(target_dir, exist_ok=True)
        copied: Dict[str, str] = {}  # 素材源路径 -> 复制后的路径
        used_names: Set[str] = set()

        for material in materials:
            source = os.path.abspath(material.path) if material.path else ""
            if not source or not os.path.exists(source):
                continue  # 素材缺失交由剪映的"链接媒体"流程处理, 此处不中断保存

            # 同一素材被多个片段引用时只复制一次
            if source in copied:
                material.path = copied[source]
                continue

            name = self._unique_material_name(os.path.basename(source), used_names)
            used_names.add(name)
            target = os.path.join(target_dir, name)
            if source != os.path.abspath(target):
                shutil.copy2(source, target)

            copied[source] = target
            material.path = target

    def save(self, *, inline_materials: bool = False) -> None:
        """保存草稿文件至打开时的路径

        Args:
            inline_materials (`bool`, optional): 是否将本地素材复制进草稿文件夹的
                `materials`子目录并改写素材路径. 默认为否.

        Raises:
            `ValueError`: 没有设置保存路径
        """
        if self.save_path is None:
            raise ValueError("没有设置保存路径, 可能不在模板模式下")

        if inline_materials:
            self._inline_materials(os.path.join(os.path.dirname(self.save_path), MATERIALS_DIR_NAME))

        self.dump(self.save_path)
