"""草稿文件夹管理器"""

import os
import shutil

from typing import List, Optional

from . import assets
from .draft_content_loader import FallbackLoader
from .script_file import ScriptFile

DRAFT_FILE_NAME = "draft_info.json"
"""草稿主文件名

剪映 6.0 及以上版本读取此文件, 已在 11.4.0 上实测确认. 旧文件名`draft_content.json`
仅被"草稿包导入"流程识别(该流程会将其重命名), 直接放入草稿文件夹会被判定为"草稿内容已损坏".
"""

LEGACY_DRAFT_FILE_NAME = "draft_content.json"
"""旧版(剪映 5.9 及以下)的草稿主文件名, 仅用于读取兼容"""

class DraftFolder:
    """管理一个文件夹及其内的一系列草稿"""

    folder_path: str
    """根路径"""
    fallback_loader: Optional[FallbackLoader]
    """明文 JSON 读取失败后的后备读取器"""

    def __init__(
        self,
        folder_path: str,
        fallback_loader: Optional[FallbackLoader] = None,
    ):
        """初始化草稿文件夹管理器

        Args:
            folder_path (`str`): 包含若干草稿的文件夹, 一般取剪映保存草稿的位置即可
            fallback_loader (`Callable`, optional): 当草稿主文件无法按明文 JSON 读取时使用的后备读取器.
                剪映 6.0 及以上版本保存的草稿是密文, 读取它们需要提供本参数.
                其输入为文件原始字节串, 返回值仅支持 JSON 字符串或字典.

        Raises:
            `FileNotFoundError`: 路径不存在
        """
        self.folder_path = folder_path
        self.fallback_loader = fallback_loader

        if not os.path.exists(self.folder_path):
            raise FileNotFoundError(f"根文件夹 {self.folder_path} 不存在")

    def list_drafts(self) -> List[str]:
        """列出文件夹中所有草稿的名称

        注意: 本函数只是如实地列出子文件夹的名称, 并不检查它们是否符合草稿的格式
        """
        return [f for f in os.listdir(self.folder_path) if os.path.isdir(os.path.join(self.folder_path, f))]

    def has_draft(self, draft_name: str) -> bool:
        """检查文件夹中是否存在指定名称的草稿

        注意: 本函数只检查文件夹是否存在, 并不检查草稿是否符合剪映的格式

        Args:
            draft_name (`str`): 草稿名称, 即相应文件夹名称
        """
        return draft_name in self.list_drafts()

    def remove(self, draft_name: str) -> None:
        """删除指定名称的草稿

        Args:
            draft_name (`str`): 草稿名称, 即相应文件夹名称

        Raises:
            `FileNotFoundError`: 对应的草稿不存在
        """
        draft_path = os.path.join(self.folder_path, draft_name)
        if not os.path.exists(draft_path):
            raise FileNotFoundError(f"草稿文件夹 {draft_name} 不存在")

        shutil.rmtree(draft_path)

    def create_draft(self, draft_name: str, width: int, height: int, fps: int = 30, *,
                     maintrack_adsorb: bool = True,
                     allow_replace: bool = False) -> ScriptFile:
        """创建一个新草稿并开始编辑, 编辑完成后使用`ScriptFile.save()`保存即可

        Args:
            draft_name (`str`): 草稿名称, 即相应文件夹名称
            width (`int`): 视频宽度, 单位为像素
            height (`int`): 视频高度, 单位为像素
            fps (`int`, optional): 视频帧率. 默认为30.
            maintrack_adsorb (`bool`, optional): 是否启用主轨道吸附（主轨磁吸）. 默认启用.
            allow_replace (`bool`, optional): 是否允许覆盖与`draft_name`重名的草稿. 默认为否.

        Raises:
            `FileExistsError`: 已存在与`draft_name`重名的草稿, 但不允许覆盖.
        """
        draft_path = os.path.join(self.folder_path, draft_name)
        if os.path.exists(draft_path):
            if not allow_replace:
                raise FileExistsError(f"草稿文件夹 {draft_name} 已存在且不允许覆盖")
            shutil.rmtree(draft_path)

        # 创建草稿文件夹
        os.makedirs(draft_path)
        shutil.copy(assets.get_asset_path("DRAFT_META_TEMPLATE"), os.path.join(draft_path, "draft_meta_info.json"))

        # 创建草稿文件
        script_file = ScriptFile(width, height, fps, maintrack_adsorb)
        script_file.save_path = os.path.join(draft_path, DRAFT_FILE_NAME)

        return script_file

    @staticmethod
    def _draft_file_path(draft_path: str) -> str:
        """草稿主文件的路径, 优先新版文件名, 回退旧版以兼容 5.9 及以下产出的草稿

        Args:
            draft_path (`str`): 草稿文件夹路径
        """
        new_path = os.path.join(draft_path, DRAFT_FILE_NAME)
        if os.path.exists(new_path):
            return new_path

        legacy_path = os.path.join(draft_path, LEGACY_DRAFT_FILE_NAME)
        if os.path.exists(legacy_path):
            return legacy_path

        # 两者均不存在时指向新版文件名, 使报错信息落在当前应有的路径上
        return new_path

    def inspect_material(self, draft_name: str) -> None:
        """输出指定名称草稿中的贴纸素材元数据

        Args:
            draft_name (`str`): 草稿名称, 即相应文件夹名称

        Raises:
            `FileNotFoundError`: 对应的草稿不存在
        """
        draft_path = os.path.join(self.folder_path, draft_name)
        if not os.path.exists(draft_path):
            raise FileNotFoundError(f"草稿文件夹 {draft_name} 不存在")

        script_file = self.load_template(draft_name)
        script_file.inspect_material()

    def load_template(self, draft_name: str) -> ScriptFile:
        """在文件夹中打开一个草稿作为模板, 并在其上进行编辑

        Args:
            draft_name (`str`): 草稿名称, 即相应文件夹名称

        Returns:
            `ScriptFile`: 以模板模式打开的草稿对象

        Raises:
            `FileNotFoundError`: 对应的草稿不存在
            `DraftContentLoadFailed`: 草稿内容不是合法明文 JSON，且未提供可用的`fallback_loader`，
                或`fallback_loader`返回了非法结果
        """
        draft_path = os.path.join(self.folder_path, draft_name)
        if not os.path.exists(draft_path):
            raise FileNotFoundError(f"草稿文件夹 {draft_name} 不存在")

        return ScriptFile._load_template(
            self._draft_file_path(draft_path),
            fallback_loader=self.fallback_loader,
        )

    def duplicate_as_template(self, template_name: str, new_draft_name: str, allow_replace: bool = False) -> ScriptFile:
        """复制一份给定的草稿, 并在复制出的新草稿上进行编辑

        Args:
            template_name (`str`): 原草稿名称
            new_draft_name (`str`): 新草稿名称
            allow_replace (`bool`, optional): 是否允许覆盖与`new_draft_name`重名的草稿. 默认为否.

        Returns:
            `ScriptFile`: 以模板模式打开的**复制后的**草稿对象

        Raises:
            `FileNotFoundError`: 原始草稿不存在
            `FileExistsError`: 已存在与`new_draft_name`重名的草稿, 但不允许覆盖.
            `DraftContentLoadFailed`: 复制出的草稿内容不是合法明文 JSON，且未提供可用的`fallback_loader`，
                或`fallback_loader`返回了非法结果
        """
        template_path = os.path.join(self.folder_path, template_name)
        new_draft_path = os.path.join(self.folder_path, new_draft_name)
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"模板草稿 {template_name} 不存在")
        if os.path.exists(new_draft_path) and not allow_replace:
            raise FileExistsError(f"新草稿 {new_draft_name} 已存在且不允许覆盖")

        # 复制草稿文件夹
        shutil.copytree(template_path, new_draft_path, dirs_exist_ok=allow_replace)

        # 打开草稿
        return self.load_template(new_draft_name)
