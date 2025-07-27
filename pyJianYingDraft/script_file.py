import os
import json
import math
from copy import deepcopy

from typing import Optional, Literal, Union, overload
from typing import Type, Dict, List, Any

from . import util
from . import assets
from . import exceptions
from .template_mode import ImportedTrack, EditableTrack, ImportedMediaTrack, ImportedTextTrack, ShrinkMode, ExtendMode, import_track
from .time_util import Timerange, tim, srt_tstamp
from .local_materials import VideoMaterial, AudioMaterial
from .segment import BaseSegment, Speed, ClipSettings
from .audio_segment import AudioSegment, AudioFade, AudioEffect
from .video_segment import VideoSegment, StickerSegment, SegmentAnimations, VideoEffect, Transition, Filter, BackgroundFilling
from .effect_segment import EffectSegment, FilterSegment
from .text_segment import TextSegment, TextStyle, TextBubble
from .track import TrackType, BaseTrack, Track

from .metadata import VideoSceneEffectType, VideoCharacterEffectType, FilterType

class ScriptMaterial:
    """草稿文件中的素材信息部分"""

    audios: List[AudioMaterial]
    """音频素材列表"""
    videos: List[VideoMaterial]
    """视频素材列表"""
    stickers: List[Dict[str, Any]]
    """贴纸素材列表"""
    texts: List[Dict[str, Any]]
    """文本素材列表"""

    audio_effects: List[AudioEffect]
    """音频特效列表"""
    audio_fades: List[AudioFade]
    """音频淡入淡出效果列表"""
    animations: List[SegmentAnimations]
    """动画素材列表"""
    video_effects: List[VideoEffect]
    """视频特效列表"""

    speeds: List[Speed]
    """变速列表"""
    masks: List[Dict[str, Any]]
    """蒙版列表"""
    transitions: List[Transition]
    """转场效果列表"""
    filters: List[Union[Filter, TextBubble]]
    """滤镜/文本花字/文本气泡列表, 导出到`effects`中"""
    canvases: List[BackgroundFilling]
    """背景填充列表"""

    def __init__(self):
        self.audios = []
        self.videos = []
        self.stickers = []
        self.texts = []

        self.audio_effects = []
        self.audio_fades = []
        self.animations = []
        self.video_effects = []

        self.speeds = []
        self.masks = []
        self.transitions = []
        self.filters = []
        self.canvases = []

    @overload
    def __contains__(self, item: Union[VideoMaterial, AudioMaterial]) -> bool: ...
    @overload
    def __contains__(self, item: Union[AudioFade, AudioEffect]) -> bool: ...
    @overload
    def __contains__(self, item: Union[SegmentAnimations, VideoEffect, Transition, Filter]) -> bool: ...

    def __contains__(self, item) -> bool:
        if isinstance(item, VideoMaterial):
            return item.material_id in [video.material_id for video in self.videos]
        elif isinstance(item, AudioMaterial):
            return item.material_id in [audio.material_id for audio in self.audios]
        elif isinstance(item, AudioFade):
            return item.fade_id in [fade.fade_id for fade in self.audio_fades]
        elif isinstance(item, AudioEffect):
            return item.effect_id in [effect.effect_id for effect in self.audio_effects]
        elif isinstance(item, SegmentAnimations):
            return item.animation_id in [ani.animation_id for ani in self.animations]
        elif isinstance(item, VideoEffect):
            return item.global_id in [effect.global_id for effect in self.video_effects]
        elif isinstance(item, Transition):
            return item.global_id in [transition.global_id for transition in self.transitions]
        elif isinstance(item, Filter):
            return item.global_id in [filter_.global_id for filter_ in self.filters]
        else:
            raise TypeError("Invalid argument type '%s'" % type(item))

    def export_json(self) -> Dict[str, List[Any]]:
        return {
            "ai_translates": [],
            "audio_balances": [],
            "audio_effects": [effect.export_json() for effect in self.audio_effects],
            "audio_fades": [fade.export_json() for fade in self.audio_fades],
            "audio_track_indexes": [],
            "audios": [audio.export_json() for audio in self.audios],
            "beats": [],
            "canvases": [canvas.export_json() for canvas in self.canvases],
            "chromas": [],
            "color_curves": [],
            "digital_humans": [],
            "drafts": [],
            "effects": [_filter.export_json() for _filter in self.filters],
            "flowers": [],
            "green_screens": [],
            "handwrites": [],
            "hsl": [],
            "images": [],
            "log_color_wheels": [],
            "loudnesses": [],
            "manual_deformations": [],
            "masks": self.masks,
            "material_animations": [ani.export_json() for ani in self.animations],
            "material_colors": [],
            "multi_language_refs": [],
            "placeholders": [],
            "plugin_effects": [],
            "primary_color_wheels": [],
            "realtime_denoises": [],
            "shapes": [],
            "smart_crops": [],
            "smart_relights": [],
            "sound_channel_mappings": [],
            "speeds": [spd.export_json() for spd in self.speeds],
            "stickers": self.stickers,
            "tail_leaders": [],
            "text_templates": [],
            "texts": self.texts,
            "time_marks": [],
            "transitions": [transition.export_json() for transition in self.transitions],
            "video_effects": [effect.export_json() for effect in self.video_effects],
            "video_trackings": [],
            "videos": [video.export_json() for video in self.videos],
            "vocal_beautifys": [],
            "vocal_separations": []
        }

class ScriptFile:
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

    materials: ScriptMaterial
    """草稿文件中的素材信息部分"""
    tracks: Dict[str, Track]
    """轨道信息"""

    imported_materials: Dict[str, List[Dict[str, Any]]]
    """导入的素材信息"""
    imported_tracks: List[ImportedTrack]
    """导入的轨道信息"""

    def __init__(self, width: int, height: int, fps: int = 30):
        """**创建剪映草稿推荐使用`DraftFolder.create_draft()`而非此方法**

        Args:
            width (int): 视频宽度, 单位为像素
            height (int): 视频高度, 单位为像素
            fps (int, optional): 视频帧率. 默认为30.
        """
        self.save_path = None

        self.width = width
        self.height = height
        self.fps = fps
        self.duration = 0

        self.materials = ScriptMaterial()
        self.tracks = {}

        self.imported_materials = {}
        self.imported_tracks = []

        with open(assets.get_asset_path('DRAFT_CONTENT_TEMPLATE'), "r", encoding="utf-8") as f:
            self.content = json.load(f)

    @staticmethod
    def load_template(json_path: str) -> "ScriptFile":
        """从JSON文件加载草稿模板

        Args:
            json_path (str): JSON文件路径

        Raises:
            `FileNotFoundError`: JSON文件不存在
        """
        obj = ScriptFile(**util.provide_ctor_defaults(ScriptFile))
        obj.save_path = json_path
        if not os.path.exists(json_path):
            raise FileNotFoundError("JSON文件 '%s' 不存在" % json_path)
        with open(json_path, "r", encoding="utf-8") as f:
            obj.content = json.load(f)

        util.assign_attr_with_json(obj, ["fps", "duration"], obj.content)
        util.assign_attr_with_json(obj, ["width", "height"], obj.content["canvas_config"])

        obj.imported_materials = deepcopy(obj.content["materials"])
        obj.imported_tracks = [import_track(track_data) for track_data in obj.content["tracks"]]

        return obj

    def add_material(self, material: Union[VideoMaterial, AudioMaterial]) -> "ScriptFile":
        """向草稿文件中添加一个素材"""
        if material in self.materials:  # 素材已存在
            return self
        if isinstance(material, VideoMaterial):
            self.materials.videos.append(material)
        elif isinstance(material, AudioMaterial):
            self.materials.audios.append(material)
        else:
            raise TypeError("错误的素材类型: '%s'" % type(material))
        return self

    def add_track(self, track_type: TrackType, track_name: Optional[str] = None, *,
                  mute: bool = False,
                  relative_index: int = 0, absolute_index: Optional[int] = None) -> "ScriptFile":
        """向草稿文件中添加一个指定类型、指定名称的轨道, 可以自定义轨道层级

        注意: 主视频轨道(最底层的视频轨道)上的视频片段必须从0s开始, 否则会被剪映强制对齐至0s.

        为避免混淆, 仅在创建第一个同类型轨道时允许不指定名称

        Args:
            track_type (TrackType): 轨道类型
            track_name (str, optional): 轨道名称. 仅在创建第一个同类型轨道时允许不指定.
            mute (bool, optional): 轨道是否静音. 默认不静音.
            relative_index (int, optional): 相对(同类型轨道的)图层位置, 越高越接近前景. 默认为0.
            absolute_index (int, optional): 绝对图层位置, 越高越接近前景. 此参数将直接覆盖相应片段的`render_index`属性, 供有经验的用户使用.
                此参数不能与`relative_index`同时使用.

        Raises:
            `NameError`: 已存在同类型轨道且未指定名称, 或已存在同名轨道
        """

        if track_name is None:
            if track_type in [track.track_type for track in self.tracks.values()]:
                raise NameError("'%s' 类型的轨道已存在, 请为新轨道指定名称以避免混淆" % track_type)
            track_name = track_type.name
        if track_name in [track.name for track in self.tracks.values()]:
            raise NameError("名为 '%s' 的轨道已存在" % track_name)

        render_index = track_type.value.render_index + relative_index
        if absolute_index is not None:
            render_index = absolute_index

        self.tracks[track_name] = Track(track_type, track_name, render_index, mute)
        return self

    def _get_track(self, segment_type: Type[BaseSegment], track_name: Optional[str]) -> Track:
        # 指定轨道名称
        if track_name is not None:
            if track_name not in self.tracks:
                raise NameError("不存在名为 '%s' 的轨道" % track_name)
            return self.tracks[track_name]
        # 寻找唯一的同类型的轨道
        count = sum([1 for track in self.tracks.values() if track.accept_segment_type == segment_type])
        if count == 0: raise NameError("不存在接受 '%s' 的轨道" % segment_type)
        if count > 1: raise NameError("存在多个接受 '%s' 的轨道, 请指定轨道名称" % segment_type)

        return next(track for track in self.tracks.values() if track.accept_segment_type == segment_type)

    def add_segment(self, segment: Union[VideoSegment, StickerSegment, AudioSegment, TextSegment],
                    track_name: Optional[str] = None) -> "ScriptFile":
        """向指定轨道中添加一个片段

        Args:
            segment (`VideoSegment`, `StickerSegment`, `AudioSegment`, or `TextSegment`): 要添加的片段
            track_name (`str`, optional): 添加到的轨道名称. 当此类型的轨道仅有一条时可省略.

        Raises:
            `NameError`: 未找到指定名称的轨道, 或必须提供`track_name`参数时未提供
            `TypeError`: 片段类型不匹配轨道类型
            `SegmentOverlap`: 新片段与已有片段重叠
        """
        target = self._get_track(type(segment), track_name)

        # 加入轨道并更新时长
        target.add_segment(segment)
        self.duration = max(self.duration, segment.end)

        # 自动添加相关素材
        if isinstance(segment, VideoSegment):
            # 出入场等动画
            if (segment.animations_instance is not None) and (segment.animations_instance not in self.materials):
                self.materials.animations.append(segment.animations_instance)
            # 特效
            for effect in segment.effects:
                if effect not in self.materials:
                    self.materials.video_effects.append(effect)
            # 滤镜
            for filter_ in segment.filters:
                if filter_ not in self.materials:
                    self.materials.filters.append(filter_)
            # 蒙版
            if segment.mask is not None:
                self.materials.masks.append(segment.mask.export_json())
            # 转场
            if (segment.transition is not None) and (segment.transition not in self.materials):
                self.materials.transitions.append(segment.transition)
            # 背景填充
            if segment.background_filling is not None:
                self.materials.canvases.append(segment.background_filling)

            self.materials.speeds.append(segment.speed)
        elif isinstance(segment, StickerSegment):
            self.materials.stickers.append(segment.export_material())
        elif isinstance(segment, AudioSegment):
            # 淡入淡出
            if (segment.fade is not None) and (segment.fade not in self.materials):
                self.materials.audio_fades.append(segment.fade)
            # 特效
            for effect in segment.effects:
                if effect not in self.materials:
                    self.materials.audio_effects.append(effect)
            self.materials.speeds.append(segment.speed)
        elif isinstance(segment, TextSegment):
            # 出入场等动画
            if (segment.animations_instance is not None) and (segment.animations_instance not in self.materials):
                self.materials.animations.append(segment.animations_instance)
            # 气泡效果
            if segment.bubble is not None:
                self.materials.filters.append(segment.bubble)
            # 花字效果
            if segment.effect is not None:
                self.materials.filters.append(segment.effect)
            # 字体样式
            self.materials.texts.append(segment.export_material())

        # 添加片段素材
        if isinstance(segment, (VideoSegment, AudioSegment)):
            self.add_material(segment.material_instance)

        return self

    def add_effect(self, effect: Union[VideoSceneEffectType, VideoCharacterEffectType],
                   t_range: Timerange, track_name: Optional[str] = None, *,
                   params: Optional[List[Optional[float]]] = None) -> "ScriptFile":
        """向指定的特效轨道中添加一个特效片段

        Args:
            effect (`VideoSceneEffectType` or `VideoCharacterEffectType`): 特效类型
            t_range (`Timerange`): 特效片段的时间范围
            track_name (`str`, optional): 添加到的轨道名称. 当特效轨道仅有一条时可省略.
            params (`List[Optional[float]]`, optional): 特效参数列表, 参数列表中未提供或为None的项使用默认值.
                参数取值范围(0~100)与剪映中一致. 某个特效类型有何参数以及具体参数顺序以枚举类成员的annotation为准.

        Raises:
            `NameError`: 未找到指定名称的轨道, 或必须提供`track_name`参数时未提供
            `TypeError`: 指定的轨道不是特效轨道
            `ValueError`: 新片段与已有片段重叠、提供的参数数量超过了该特效类型的参数数量, 或参数值超出范围.
        """
        target = self._get_track(EffectSegment, track_name)

        # 加入轨道并更新时长
        segment = EffectSegment(effect, t_range, params)
        target.add_segment(segment)
        self.duration = max(self.duration, t_range.start + t_range.duration)

        # 自动添加相关素材
        if segment.effect_inst not in self.materials:
            self.materials.video_effects.append(segment.effect_inst)
        return self

    def add_filter(self, filter_meta: FilterType, t_range: Timerange,
                   track_name: Optional[str] = None, intensity: float = 100.0) -> "ScriptFile":
        """向指定的滤镜轨道中添加一个滤镜片段

        Args:
            filter_meta (`FilterType`): 滤镜类型
            t_range (`Timerange`): 滤镜片段的时间范围
            track_name (`str`, optional): 添加到的轨道名称. 当滤镜轨道仅有一条时可省略.
            intensity (`float`, optional): 滤镜强度(0-100). 仅当所选滤镜能够调节强度时有效. 默认为100.

        Raises:
            `NameError`: 未找到指定名称的轨道, 或必须提供`track_name`参数时未提供
            `TypeError`: 指定的轨道不是滤镜轨道
            `ValueError`: 新片段与已有片段重叠
        """
        target = self._get_track(FilterSegment, track_name)

        # 加入轨道并更新时长
        segment = FilterSegment(filter_meta, t_range, intensity / 100.0)  # 转换为0-1范围
        target.add_segment(segment)
        self.duration = max(self.duration, t_range.end)

        # 自动添加相关素材
        self.materials.filters.append(segment.material)
        return self

    def import_srt(self, srt_path: str, track_name: str, *,
                   time_offset: Union[str, float] = 0.0,
                   style_reference: Optional[TextSegment] = None,
                   text_style: TextStyle = TextStyle(size=5, align=1, auto_wrapping=True),
                   clip_settings: Optional[ClipSettings] = ClipSettings(transform_y=-0.8)) -> "ScriptFile":
        """从SRT文件中导入字幕, 支持传入一个`TextSegment`作为样式参考

        注意: 默认不会使用参考片段的`clip_settings`属性, 若需要请显式为此函数传入`clip_settings=None`

        Args:
            srt_path (`str`): SRT文件路径
            track_name (`str`): 导入到的文本轨道名称, 若不存在则自动创建
            style_reference (`TextSegment`, optional): 作为样式参考的文本片段, 若提供则使用其样式.
            time_offset (`Union[str, float]`, optional): 字幕整体时间偏移, 单位为微秒, 默认为0.
            text_style (`TextStyle`, optional): 字幕样式, 默认模仿剪映导入字幕时的样式, 会被`style_reference`覆盖.
            clip_settings (`ClipSettings`, optional): 图像调节设置, 默认模仿剪映导入字幕时的设置, 会覆盖`style_reference`的设置除非指定为`None`.

        Raises:
            `NameError`: 已存在同名轨道
            `TypeError`: 轨道类型不匹配
        """
        if style_reference is None and clip_settings is None:
            raise ValueError("未提供样式参考时请提供`clip_settings`参数")

        time_offset = tim(time_offset)
        if track_name not in self.tracks:
            self.add_track(TrackType.text, track_name, relative_index=999)  # 在所有文本轨道的最上层

        with open(srt_path, "r", encoding="utf-8-sig") as srt_file:
            lines = srt_file.readlines()

        def __add_text_segment(text: str, t_range: Timerange) -> None:
            if style_reference:
                seg = TextSegment.create_from_template(text, t_range, style_reference)
                if clip_settings is not None:
                    seg.clip_settings = deepcopy(clip_settings)
            else:
                seg = TextSegment(text, t_range, style=text_style, clip_settings=clip_settings)
            self.add_segment(seg, track_name)

        index = 0
        text: str = ""
        text_trange: Timerange
        read_state: Literal["index", "timestamp", "content"] = "index"
        while index < len(lines):
            line = lines[index].strip()
            if read_state == "index":
                if len(line) == 0:
                    index += 1
                    continue
                if not line.isdigit():
                    raise ValueError("Expected a number at line %d, got '%s'" % (index+1, line))
                index += 1
                read_state = "timestamp"
            elif read_state == "timestamp":
                # 读取时间戳
                start_str, end_str = line.split(" --> ")
                start, end = srt_tstamp(start_str), srt_tstamp(end_str)
                text_trange = Timerange(start + time_offset, end - start)

                index += 1
                read_state = "content"
            elif read_state == "content":
                # 内容结束, 生成片段
                if len(line) == 0:
                    __add_text_segment(text.strip(), text_trange)

                    text = ""
                    read_state = "index"
                else:
                    text += line + "\n"
                index += 1

        # 添加最后一个片段
        if len(text) > 0:
            __add_text_segment(text.strip(), text_trange)

        return self

    def get_imported_track(self, track_type: Literal[TrackType.video, TrackType.audio, TrackType.text],
                           name: Optional[str] = None, index: Optional[int] = None) -> EditableTrack:
        """获取指定类型的导入轨道, 以便在其上进行替换

        推荐使用轨道名称进行筛选（若已知轨道名称）

        Args:
            track_type (`TrackType.video`, `TrackType.audio` or `TrackType.text`): 轨道类型, 目前只支持音视频和文本轨道
            name (`str`, optional): 轨道名称, 不指定则不根据名称筛选.
            index (`int`, optional): 轨道在**同类型的导入轨道**中的下标, 以0为最下层轨道. 不指定则不根据下标筛选.

        Raises:
            `TrackNotFound`: 未找到满足条件的轨道
            `AmbiguousTrack`: 找到多个满足条件的轨道
        """
        tracks_of_same_type: List[EditableTrack] = []
        for track in self.imported_tracks:
            if track.track_type == track_type:
                assert isinstance(track, EditableTrack)
                tracks_of_same_type.append(track)

        ret: List[EditableTrack] = []
        for ind, track in enumerate(tracks_of_same_type):
            if (name is not None) and (track.name != name): continue
            if (index is not None) and (ind != index): continue
            ret.append(track)

        if len(ret) == 0:
            raise exceptions.TrackNotFound(
                "没有找到满足条件的轨道: track_type=%s, name=%s, index=%s" % (track_type, name, index))
        if len(ret) > 1:
            raise exceptions.AmbiguousTrack(
                "找到多个满足条件的轨道: track_type=%s, name=%s, index=%s" % (track_type, name, index))

        return ret[0]

    def import_track(self, source_file: "ScriptFile", track: EditableTrack, *,
                     offset: Union[str, int] = 0,
                     new_name: Optional[str] = None, relative_index: Optional[int] = None) -> "ScriptFile":
        """将一个`EditableTrack`导入到当前`ScriptFile`中, 如从模板草稿中导入特定的文本或视频轨道到当前正在编辑的草稿文件中

        注意: 本方法会保留各片段及其素材的id, 因而不支持向同一草稿多次导入同一轨道

        Args:
            source_file (`ScriptFile`): 源文件，包含要导入的轨道
            track (`EditableTrack`): 要导入的轨道, 可通过`get_imported_track`方法获取.
            offset (`str | int`, optional): 轨道的时间偏移量(微秒), 可以是整数微秒值或时间字符串(如"1s"). 默认不添加偏移.
            new_name (`str`, optional): 新轨道名称, 默认使用源轨道名称.
            relative_index (`int`, optional): 相对索引，用于调整导入轨道的渲染层级. 默认保持原有层级.
        """
        # 直接拷贝原始轨道结构, 按需修改渲染层级
        imported_track = deepcopy(track)
        if relative_index is not None:
            imported_track.render_index = track.track_type.value.render_index + relative_index
        if new_name is not None:
            imported_track.name = new_name

        # 应用偏移量
        offset_us = tim(offset)
        if offset_us != 0:
            for seg in imported_track.segments:
                seg.target_timerange.start = max(0, seg.target_timerange.start + offset_us)
        self.imported_tracks.append(imported_track)

        # 收集所有需要复制的素材ID
        material_ids = set()
        segments: List[Dict[str, Any]] = track.raw_data.get("segments", [])
        for segment in segments:
            # 主素材ID
            material_id = segment.get("material_id")
            if material_id:
                material_ids.add(material_id)

            # extra_material_refs中的素材ID
            extra_refs: List[str] = segment.get("extra_material_refs", [])
            material_ids.update(extra_refs)

        # 复制素材
        for material_type, material_list in source_file.imported_materials.items():
            for material in material_list:
                if material.get("id") in material_ids:
                    if material_type not in self.imported_materials:
                        self.imported_materials[material_type] = []
                    self.imported_materials[material_type].append(deepcopy(material))
                    material_ids.remove(material.get("id"))

        assert len(material_ids) == 0, "未找到以下素材: %s" % material_ids

        # 更新总时长
        self.duration = max(self.duration, track.end_time)

        return self

    def replace_material_by_name(self, material_name: str, material: Union[VideoMaterial, AudioMaterial],
                                 replace_crop: bool = False) -> "ScriptFile":
        """替换指定名称的素材, 并影响所有引用它的片段

        这种方法不会改变相应片段的时长和引用范围(`source_timerange`), 尤其适合于图片素材

        Args:
            material_name (`str`): 要替换的素材名称
            material (`VideoMaterial` or `AudioMaterial`): 新素材, 目前只支持视频和音频
            replace_crop (`bool`, optional): 是否替换原素材的裁剪设置, 默认为否. 仅对视频素材有效.

        Raises:
            `MaterialNotFound`: 根据指定名称未找到与新素材同类的素材
            `AmbiguousMaterial`: 根据指定名称找到多个与新素材同类的素材
        """
        video_mode = isinstance(material, VideoMaterial)
        # 查找素材
        target_json_obj: Optional[Dict[str, Any]] = None
        target_material_list = self.imported_materials["videos" if video_mode else "audios"]
        name_key = "material_name" if video_mode else "name"
        for mat in target_material_list:
            if mat[name_key] == material_name:
                if target_json_obj is not None:
                    raise exceptions.AmbiguousMaterial(
                        "找到多个名为 '%s', 类型为 '%s' 的素材" % (material_name, type(material)))
                target_json_obj = mat
        if target_json_obj is None:
            raise exceptions.MaterialNotFound("没有找到名为 '%s', 类型为 '%s' 的素材" % (material_name, type(material)))

        # 更新素材信息
        target_json_obj.update({name_key: material.material_name, "path": material.path, "duration": material.duration})
        if video_mode:
            target_json_obj.update({"width": material.width, "height": material.height, "material_type": material.material_type})
            if replace_crop:
                target_json_obj.update({"crop": material.crop_settings.export_json()})

        return self

    def replace_material_by_seg(self, track: EditableTrack, segment_index: int, material: Union[VideoMaterial, AudioMaterial],
                                source_timerange: Optional[Timerange] = None, *,
                                handle_shrink: ShrinkMode = ShrinkMode.cut_tail,
                                handle_extend: Union[ExtendMode, List[ExtendMode]] = ExtendMode.cut_material_tail) -> "ScriptFile":
        """替换指定音视频轨道上指定片段的素材, 暂不支持变速片段的素材替换

        Args:
            track (`EditableTrack`): 要替换素材的轨道, 由`get_imported_track`获取
            segment_index (`int`): 要替换素材的片段下标, 从0开始
            material (`VideoMaterial` or `AudioMaterial`): 新素材, 必须与原素材类型一致
            source_timerange (`Timerange`, optional): 从原素材中截取的时间范围, 默认为全时段, 若是图片素材则默认与原片段等长.
            handle_shrink (`Shrink_mode`, optional): 新素材比原素材短时的处理方式, 默认为裁剪尾部, 使片段长度与素材一致.
            handle_extend (`Extend_mode` or `List[Extend_mode]`, optional): 新素材比原素材长时的处理方式, 将按顺序逐个尝试直至成功或抛出异常.
                默认为截断素材尾部, 使片段维持原长不变

        Raises:
            `IndexError`: `segment_index`越界
            `TypeError`: 轨道或素材类型不正确
            `ExtensionFailed`: 新素材比原素材长时处理失败
        """
        if not isinstance(track, ImportedMediaTrack):
            raise TypeError("指定的轨道(类型为 %s)不支持素材替换" % track.track_type)
        if not 0 <= segment_index < len(track):
            raise IndexError("片段下标 %d 超出 [0, %d) 的范围" % (segment_index, len(track)))
        if not track.check_material_type(material):
            raise TypeError("指定的素材类型 %s 不匹配轨道类型 %s", (type(material), track.track_type))
        seg = track.segments[segment_index]

        if isinstance(handle_extend, ExtendMode):
            handle_extend = [handle_extend]
        if source_timerange is None:
            if isinstance(material, VideoMaterial) and (material.material_type == "photo"):
                source_timerange = Timerange(0, seg.duration)
            else:
                source_timerange = Timerange(0, material.duration)

        # 处理时间变化
        track.process_timerange(segment_index, source_timerange, handle_shrink, handle_extend)

        # 最后替换素材链接
        track.segments[segment_index].material_id = material.material_id
        self.add_material(material)

        # TODO: 更新总长
        return self

    def replace_text(self, track: EditableTrack, segment_index: int, text: Union[str, List[str]],
                     recalc_style: bool = True) -> "ScriptFile":
        """替换指定文本轨道上指定片段的文字内容, 支持普通文本片段或文本模板片段

        Args:
            track (`EditableTrack`): 要替换文字的文本轨道, 由`get_imported_track`获取
            segment_index (`int`): 要替换文字的片段下标, 从0开始
            text (`str` or `List[str]`): 新的文字内容, 对于文本模板而言应传入一个字符串列表.
            recalc_style (`bool`): 是否重新计算字体样式分布, 即调整各字体样式应用范围以尽量维持原有占比不变, 默认开启.

        Raises:
            `IndexError`: `segment_index`越界
            `TypeError`: 轨道类型不正确
            `ValueError`: 文本模板片段的文本数量不匹配
        """
        if not isinstance(track, ImportedTextTrack):
            raise TypeError("指定的轨道(类型为 %s)不支持文本内容替换" % track.track_type)
        if not 0 <= segment_index < len(track):
            raise IndexError("片段下标 %d 超出 [0, %d) 的范围" % (segment_index, len(track)))

        def __recalc_style_range(old_len: int, new_len: int, styles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
            """调整字体样式分布"""
            new_styles: List[Dict[str, Any]] = []
            for style in styles:
                start = math.ceil(style["range"][0] / old_len * new_len)
                end = math.ceil(style["range"][1] / old_len * new_len)
                style["range"] = [start, end]
                if start != end:
                    new_styles.append(style)
            return new_styles

        replaced: bool = False
        material_id: str = track.segments[segment_index].material_id
        # 尝试在文本素材中替换
        for mat in self.imported_materials["texts"]:
            if mat["id"] != material_id:
                continue

            if isinstance(text, list):
                if len(text) != 1:
                    raise ValueError(f"正常文本片段只能有一个文字内容, 但替换内容是 {text}")
                text = text[0]

            content = json.loads(mat["content"])
            if recalc_style:
                content["styles"] = __recalc_style_range(len(content["text"]), len(text), content["styles"])
            content["text"] = text
            mat["content"] = json.dumps(content, ensure_ascii=False)
            replaced = True
            break
        if replaced:
            return self

        # 尝试在文本模板中替换
        for template in self.imported_materials["text_templates"]:
            if template["id"] != material_id:
                continue

            resources = template["text_info_resources"]
            if isinstance(text, str):
                text = [text]
            if len(text) > len(resources):
                raise ValueError(f"文字模板'{template['name']}'只有{len(resources)}段文本, 但提供了{len(text)}段替换内容")

            for sub_material_id, new_text in zip(map(lambda x: x["text_material_id"], resources), text):
                for mat in self.imported_materials["texts"]:
                    if mat["id"] != sub_material_id:
                        continue

                    try:
                        content = json.loads(mat["content"])
                        if recalc_style:
                            content["styles"] = __recalc_style_range(len(content["text"]), len(new_text), content["styles"])
                        content["text"] = new_text
                        mat["content"] = json.dumps(content, ensure_ascii=False)
                    except json.JSONDecodeError:
                        mat["content"] = new_text
                    except TypeError:
                        mat["content"] = new_text

                    break
            replaced = True
            break

        assert replaced, f"未找到指定片段的素材 {material_id}"

        return self

    def inspect_material(self) -> None:
        """输出草稿中导入的贴纸、文本气泡以及花字素材的元数据"""
        print("贴纸素材:")
        for sticker in self.imported_materials["stickers"]:
            print("\tResource id: %s '%s'" % (sticker["resource_id"], sticker.get("name", "")))

        print("文字气泡效果:")
        for effect in self.imported_materials["effects"]:
            if effect["type"] == "text_shape":
                print("\tEffect id: %s ,Resource id: %s '%s'" %
                      (effect["effect_id"], effect["resource_id"], effect.get("name", "")))

        print("花字效果:")
        for effect in self.imported_materials["effects"]:
            if effect["type"] == "text_effect":
                print("\tResource id: %s '%s'" % (effect["resource_id"], effect.get("name", "")))

    def dumps(self) -> str:
        """将草稿文件内容导出为JSON字符串"""
        self.content["fps"] = self.fps
        self.content["duration"] = self.duration
        self.content["canvas_config"] = {"width": self.width, "height": self.height, "ratio": "original"}
        self.content["materials"] = self.materials.export_json()

        # 合并导入的素材
        for material_type, material_list in self.imported_materials.items():
            if material_type not in self.content["materials"]:
                self.content["materials"][material_type] = material_list
            else:
                self.content["materials"][material_type].extend(material_list)

        # 对轨道排序并导出
        track_list: List[BaseTrack] = list(self.imported_tracks + list(self.tracks.values()))  # 新加入的轨道在列表末尾（上层）
        track_list.sort(key=lambda track: track.render_index)
        self.content["tracks"] = [track.export_json() for track in track_list]

        return json.dumps(self.content, ensure_ascii=False, indent=4)

    def dump(self, file_path: str) -> None:
        """将草稿文件内容写入文件"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(self.dumps())

    def save(self) -> None:
        """保存草稿文件至打开时的路径

        Raises:
            `ValueError`: 没有设置保存路径
        """
        if self.save_path is None:
            raise ValueError("没有设置保存路径, 可能不在模板模式下")
        self.dump(self.save_path)
