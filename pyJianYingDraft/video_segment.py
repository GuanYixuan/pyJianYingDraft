"""定义视频片段及其相关类

包含图像调节设置、动画效果、特效、转场等相关类
"""

import uuid
from copy import deepcopy

from typing import Optional, Literal, Union
from typing import Dict, List, Tuple, Any

from .time_util import tim, Timerange
from .segment import VisualSegment, ClipSettings, AudioFade
from .local_materials import VideoMaterial
from .animation import SegmentAnimations, VideoAnimation

from .metadata import EffectMeta, EffectParamInstance
from .metadata import MaskMeta, MaskType, FilterType, TransitionType
from .metadata import IntroType, OutroType, GroupAnimationType
from .metadata import VideoSceneEffectType, VideoCharacterEffectType

class Mask:
    """蒙版对象"""

    mask_meta: MaskMeta
    """蒙版元数据"""
    global_id: str
    """蒙版全局id, 由程序自动生成"""

    center_x: float
    """蒙版中心x坐标, 以半素材宽为单位"""
    center_y: float
    """蒙版中心y坐标, 以半素材高为单位"""
    width: float
    height: float
    aspect_ratio: float

    rotation: float
    invert: bool
    expansion: float
    feather: float
    """羽化程度, 0-1"""
    round_corner: float
    """矩形蒙版的圆角, 0-1"""
    text_config_override: Optional[Dict[str, Any]]
    """文字蒙版文本配置覆盖"""

    def __init__(self, mask_meta: MaskMeta,
                 cx: float, cy: float, w: float, h: float,
                 ratio: float, rot: float, inv: bool, feather: float, round_corner: float,
                 expansion: float = 0.0,
                 text_config_override: Optional[Dict[str, Any]] = None):
        self.mask_meta = mask_meta
        self.global_id = uuid.uuid4().hex

        self.center_x, self.center_y = cx, cy
        self.width, self.height = w, h
        self.aspect_ratio = ratio

        self.rotation = rot
        self.invert = inv
        self.expansion = expansion
        self.feather = feather
        self.round_corner = round_corner
        self.text_config_override = text_config_override

    def export_json(self) -> Dict[str, Any]:
        text_config = {
            "align_type": 15,
            "bold_width": 0.0,
            "char_spacing": 0.0,
            "content": "",
            "font_name": "",
            "font_path": "",
            "font_resource_id": "",
            "font_size": 15.0,
            "has_underline": False,
            "italic_degree": 0,
            "line_gap": 0.0,
            "scale": 1.0
        }
        if self.text_config_override:
            text_config.update(self.text_config_override)
        return {
            "category": "video",
            "category_id": "jichu",
            "category_name": "基础",
            "config": {
                "aspectRatio": self.aspect_ratio,
                "centerX": self.center_x,
                "centerY": self.center_y,
                "expansion": self.expansion,
                "feather": self.feather,
                "height": self.height,
                "invert": self.invert,
                "rotation": self.rotation,
                "roundCorner": self.round_corner,
                "width": self.width
            },
            "id": self.global_id,
            "is_old_version": False,
            "loader_work_space": "",
            "name": self.mask_meta.name,
            "panel": "",
            "platform": "all",
            "position_info": "",
            "resource_id": self.mask_meta.resource_id,
            "resource_type": self.mask_meta.resource_type,
            "source_platform": 0,
            "text_config": text_config,
            "track_segment": "",
            "type": "mask"
            # 不导出path字段
        }

class VideoEffect:
    """视频特效素材"""

    name: str
    """特效名称"""
    global_id: str
    """特效全局id, 由程序自动生成"""
    effect_id: str
    """某种特效id, 由剪映本身提供"""
    resource_id: str
    """资源id, 由剪映本身提供"""

    effect_type: Literal["video_effect", "face_effect"]
    apply_target_type: Literal[0, 2]
    """应用目标类型, 0: 片段, 2: 全局"""

    adjust_params: List[EffectParamInstance]

    def __init__(self, effect_meta: Union[VideoSceneEffectType, VideoCharacterEffectType],
                 params: Optional[List[Optional[float]]] = None, *,
                 apply_target_type: Literal[0, 2] = 0):
        """根据给定的特效元数据及参数列表构造一个视频特效对象, params的范围是0~100"""

        self.name = effect_meta.value.name
        self.global_id = uuid.uuid4().hex
        self.effect_id = effect_meta.value.effect_id
        self.resource_id = effect_meta.value.resource_id
        self.adjust_params = []

        if isinstance(effect_meta, VideoSceneEffectType):
            self.effect_type = "video_effect"
        elif isinstance(effect_meta, VideoCharacterEffectType):
            self.effect_type = "face_effect"
        else:
            raise TypeError("Invalid effect meta type %s" % type(effect_meta))
        self.apply_target_type = apply_target_type

        self.adjust_params = effect_meta.value.parse_params(params)

    def export_json(self) -> Dict[str, Any]:
        return {
            "adjust_params": [param.export_json() for param in self.adjust_params],
            "apply_target_type": self.apply_target_type,
            "apply_time_range": None,
            "category_id": "",  # 一律设为空
            "category_name": "",  # 一律设为空
            "common_keyframes": [],
            "disable_effect_faces": [],
            "effect_id": self.effect_id,
            "formula_id": "",
            "id": self.global_id,
            "name": self.name,
            "platform": "all",
            "render_index": 11000,
            "resource_id": self.resource_id,
            "source_platform": 0,
            "time_range": None,
            "track_render_index": 0,
            "type": self.effect_type,
            "value": 1.0,
            "version": ""
            # 不导出path、request_id和algorithm_artifact_path字段
        }

class Filter:
    """滤镜素材"""

    global_id: str
    """滤镜全局id, 由程序自动生成"""

    effect_meta: EffectMeta
    """滤镜的元数据"""
    intensity: float
    """滤镜强度(滤镜的唯一参数)"""

    apply_target_type: Literal[0, 2]
    """应用目标类型, 0: 片段, 2: 全局"""

    def __init__(self, meta: EffectMeta, intensity: float, *,
                 apply_target_type: Literal[0, 2] = 0):
        """根据给定的滤镜元数据及强度构造滤镜素材对象"""

        self.global_id = uuid.uuid4().hex
        self.effect_meta = meta
        self.intensity = intensity
        self.apply_target_type = apply_target_type

    def export_json(self) -> Dict[str, Any]:
        return {
            "adjust_params": [],
            "apply_target_type": self.apply_target_type,
            "bloom_params": None,
            "category_id": "",  # 一律设为空
            "category_name": "",  # 一律设为空
            "color_match_info": {
                "source_feature_path": "",
                "target_feature_path": "",
                "target_image_path": ""
            },
            "effect_id": self.effect_meta.effect_id,
            "enable_skin_tone_correction": False,
            "exclusion_group": [],
            "face_adjust_params": [],
            "formula_id": "",
            "id": self.global_id,
            "intensity_key": "",
            "multi_language_current": "",
            "name": self.effect_meta.name,
            "panel_id": "",
            "platform": "all",
            "resource_id": self.effect_meta.resource_id,
            "source_platform": 1,
            "sub_type": "none",
            "time_range": None,
            "type": "filter",
            "value": self.intensity,
            "version": ""
            # 不导出path和request_id
        }

class Transition:
    """转场对象"""

    name: str
    """转场名称"""
    global_id: str
    """转场全局id, 由程序自动生成"""
    effect_id: str
    """转场效果id, 由剪映本身提供"""
    resource_id: str
    """资源id, 由剪映本身提供"""

    duration: int
    """转场持续时间, 单位为微秒"""
    is_overlap: bool
    """是否与上一个片段重叠(?)"""

    def __init__(self, effect_meta: TransitionType, duration: Optional[int] = None):
        """根据给定的转场元数据及持续时间构造一个转场对象"""
        self.name = effect_meta.value.name
        self.global_id = uuid.uuid4().hex
        self.effect_id = effect_meta.value.effect_id
        self.resource_id = effect_meta.value.resource_id

        self.duration = duration if duration is not None else effect_meta.value.default_duration
        self.is_overlap = effect_meta.value.is_overlap

    def export_json(self) -> Dict[str, Any]:
        return {
            "category_id": "",  # 一律设为空
            "category_name": "",  # 一律设为空
            "duration": self.duration,
            "effect_id": self.effect_id,
            "id": self.global_id,
            "is_overlap": self.is_overlap,
            "name": self.name,
            "platform": "all",
            "resource_id": self.resource_id,
            "type": "transition"
            # 不导出path和request_id字段
        }

class BackgroundFilling:
    """背景填充对象"""

    global_id: str
    """背景填充全局id, 由程序自动生成"""
    fill_type: Literal["canvas_blur", "canvas_color"]
    """背景填充类型"""
    blur: float
    """模糊程度, 0-1"""
    color: str
    """背景颜色, 格式为'#RRGGBBAA'"""

    def __init__(self, fill_type: Literal["canvas_blur", "canvas_color"], blur: float, color: str):
        self.global_id = uuid.uuid4().hex
        self.fill_type = fill_type
        self.blur = blur
        self.color = color

    def export_json(self) -> Dict[str, Any]:
        return {
            "id": self.global_id,
            "type": self.fill_type,
            "blur": self.blur,
            "color": self.color,
            "source_platform": 0,
        }

class VideoSegment(VisualSegment):
    """安放在轨道上的一个视频/图片片段"""

    material_instance: VideoMaterial
    """素材实例"""
    material_size: Tuple[int, int]
    """素材尺寸"""

    fade: Optional[AudioFade]
    """音频淡入淡出效果, 可能为空

    在放入轨道时自动添加到素材列表中
    """

    effects: List[VideoEffect]
    """特效列表

    在放入轨道时自动添加到素材列表中
    """
    filters: List[Filter]
    """滤镜列表

    在放入轨道时自动添加到素材列表中
    """
    mask: Optional[Mask]
    """蒙版实例, 可能为空

    在放入轨道时自动添加到素材列表中
    """
    transition: Optional[Transition]
    """转场实例, 可能为空

    在放入轨道时自动添加到素材列表中
    """
    background_filling: Optional[BackgroundFilling]
    """背景填充实例, 可能为空

    在放入轨道时自动添加到素材列表中
    """

    def __init__(self, material: Union[VideoMaterial, str], target_timerange: Optional[Timerange] = None, *,
                 source_timerange: Optional[Timerange] = None, speed: Optional[float] = None, volume: float = 1.0,
                 change_pitch: bool = False, clip_settings: Optional[ClipSettings] = None):
        """利用给定的视频/图片素材构建一个轨道片段, 并指定其时间信息及图像调节设置

        Args:
            material (`VideoMaterial` or `str`): 素材实例或素材路径, 若为路径则自动构造素材实例(此时不能指定`cropSettings`参数)
            target_timerange (`Timerange`): 片段在轨道上的目标时间范围, 默认使用素材完整时长
            source_timerange (`Timerange`, optional): 截取的素材片段的时间范围, 默认从开头根据`speed`截取与`target_timerange`等长的一部分
            speed (`float`, optional): 播放速度, 默认为1.0. 此项与`source_timerange`同时指定时, 将覆盖`target_timerange`中的时长
            volume (`float`, optional): 音量, 默认为1.0
            change_pitch (`bool`, optional): 是否跟随变速改变音调, 默认为否
            clip_settings (`ClipSettings`, optional): 图像调节设置, 默认不作任何变换

        Raises:
            `ValueError`: 指定的或计算出的`source_timerange`超出了素材的时长范围
        """
        if isinstance(material, str):
            material = VideoMaterial(material)

        if source_timerange is not None and speed is not None:
            start = target_timerange.start if target_timerange else 0
            target_timerange = Timerange(start, round(source_timerange.duration / speed))
        elif source_timerange is not None and speed is None:
            if target_timerange is None:
                speed = 1.0
                target_timerange = Timerange(0, source_timerange.duration)
            else:
                speed = source_timerange.duration / target_timerange.duration
        else:
            speed = speed if speed is not None else 1.0
            if target_timerange is None:   # target_timerange and source_timerange is None
                source_timerange = Timerange(0, material.duration)
                target_timerange = Timerange(0, round(source_timerange.duration / speed))
            else:  # source_timerange is None
                source_timerange = Timerange(0, round(target_timerange.duration * speed))

        if source_timerange.end > material.duration:
            raise ValueError(f"截取的素材时间范围 {source_timerange} 超出了素材时长({material.duration})")

        super().__init__(material.material_id, source_timerange, target_timerange, speed,
                         volume, change_pitch, clip_settings=clip_settings)

        self.material_instance = deepcopy(material)
        self.material_size = (material.width, material.height)
        self.effects = []
        self.filters = []
        self.transition = None
        self.mask = None
        self.background_filling = None
        self.fade = None

    def add_animation(self, animation_type: Union[IntroType, OutroType, GroupAnimationType],
                      duration: Optional[Union[int, str]] = None) -> "VideoSegment":
        """将给定的入场/出场/组合动画添加到此片段的动画列表中

        Args:
            animation_type (`IntroType`, `OutroType`, or `GroupAnimationType`): 动画类型
            duration (`int` or `str`, optional): 动画持续时间, 单位为微秒. 若传入字符串则会调用`tim()`函数进行解析.
                若不指定则使用动画类型定义的默认值. 理论上只适用于入场和出场动画.
        """
        if duration is not None:
            duration = tim(duration)
        if isinstance(animation_type, IntroType):
            start = 0
            duration = duration or animation_type.value.duration
        elif isinstance(animation_type, OutroType):
            duration = duration or animation_type.value.duration
            start = self.target_timerange.duration - duration
        elif isinstance(animation_type, GroupAnimationType):
            start = 0
            duration = duration or self.target_timerange.duration
        else:
            raise TypeError("Invalid animation type %s" % type(animation_type))

        if self.animations_instance is None:
            self.animations_instance = SegmentAnimations()
            self.extra_material_refs.append(self.animations_instance.animation_id)

        self.animations_instance.add_animation(VideoAnimation(animation_type, start, duration))

        return self

    def add_effect(self, effect_type: Union[VideoSceneEffectType, VideoCharacterEffectType],
                   params: Optional[List[Optional[float]]] = None) -> "VideoSegment":
        """为视频片段添加一个作用于整个片段的特效

        Args:
            effect_type (`VideoSceneEffectType` or `VideoCharacterEffectType`): 特效类型
            params (`List[Optional[float]]`, optional): 特效参数列表, 参数列表中未提供或为None的项使用默认值.
                参数取值范围(0~100)与剪映中一致. 某个特效类型有何参数以及具体参数顺序以枚举类成员的annotation为准.

        Raises:
            `ValueError`: 提供的参数数量超过了该特效类型的参数数量, 或参数值超出范围.
        """
        if params is not None and len(params) > len(effect_type.value.params):
            raise ValueError("为音频效果 %s 传入了过多的参数" % effect_type.value.name)

        effect_inst = VideoEffect(effect_type, params)
        self.effects.append(effect_inst)
        self.extra_material_refs.append(effect_inst.global_id)

        return self

    def add_fade(self, in_duration: Union[str, int], out_duration: Union[str, int]) -> "VideoSegment":
        """为视频片段添加音频淡入淡出效果, 仅对有音轨的视频片段有效

        Args:
            in_duration (`int` or `str`): 音频淡入时长, 单位为微秒, 若为字符串则会调用`tim()`函数进行解析
            out_duration (`int` or `str`): 音频淡出时长, 单位为微秒, 若为字符串则会调用`tim()`函数进行解析

        Raises:
            `ValueError`: 当前片段已存在淡入淡出效果
        """
        if self.fade is not None:
            raise ValueError("当前片段已存在淡入淡出效果")

        if isinstance(in_duration, str): in_duration = tim(in_duration)
        if isinstance(out_duration, str): out_duration = tim(out_duration)

        self.fade = AudioFade(in_duration, out_duration)
        self.extra_material_refs.append(self.fade.fade_id)

        return self

    def add_filter(self, filter_type: FilterType, intensity: float = 100.0) -> "VideoSegment":
        """为视频片段添加一个滤镜

        Args:
            filter_type (`FilterType`): 滤镜类型
            intensity (`float`, optional): 滤镜强度(0-100), 仅当所选滤镜能够调节强度时有效. 默认为100.
        """
        filter_inst = Filter(filter_type.value, intensity / 100.0)  # 转化为0~1范围
        self.filters.append(filter_inst)
        self.extra_material_refs.append(filter_inst.global_id)

        return self

    def add_mask(self, mask_type: MaskType, *, center_x: float = 0.0, center_y: float = 0.0, size: float = 0.5,
                 rotation: float = 0.0, feather: float = 0.0, invert: bool = False, expansion: float = 0.0,
                 text_content: Optional[str] = None, text_font_name: str = "系统",
                 text_font_path: str = "", text_font_size: float = 40.0, text_scale: float = 74.45620779038588,
                 text_align_type: int = 1, text_bold_width: float = 1.0, text_char_spacing: float = 0.0,
                 text_italic_degree: int = 0, text_line_gap: float = 0.0, text_has_underline: bool = False,
                 text_font_resource_id: str = "",
                 rect_width: Optional[float] = None, round_corner: Optional[float] = None) -> "VideoSegment":
        """为视频片段添加蒙版

        Args:
            mask_type (`MaskType`): 蒙版类型
            center_x (`float`, optional): 蒙版中心点X坐标(以素材的像素为单位), 默认设置在素材中心
            center_y (`float`, optional): 蒙版中心点Y坐标(以素材的像素为单位), 默认设置在素材中心
            size (`float`, optional): 蒙版的"主要尺寸"(镜面的可视部分高度/圆形直径/爱心高度等), 以占素材高度的比例表示, 默认为0.5
            rotation (`float`, optional): 蒙版顺时针旋转的**角度**, 默认不旋转
            feather (`float`, optional): 蒙版的羽化参数, 取值范围0~100, 默认无羽化
            invert (`bool`, optional): 是否反转蒙版, 默认不反转
            expansion (`float`, optional): 蒙版扩展参数, 取值范围0~100, 默认不扩展
            text_content (`str`, optional): 文字蒙版内容, 仅在蒙版类型为文字时生效, 默认为"默认文本"
            text_font_name (`str`, optional): 文字蒙版字体名称, 仅在蒙版类型为文字时生效
            text_font_path (`str`, optional): 文字蒙版字体路径(可为空), 仅在蒙版类型为文字时生效
            text_font_size (`float`, optional): 文字蒙版字体大小, 仅在蒙版类型为文字时生效
            text_scale (`float`, optional): 文字蒙版缩放, 仅在蒙版类型为文字时生效
            text_align_type (`int`, optional): 文字蒙版对齐方式, 仅在蒙版类型为文字时生效
            text_bold_width (`float`, optional): 文字蒙版加粗宽度, 仅在蒙版类型为文字时生效
            text_char_spacing (`float`, optional): 文字蒙版字间距, 仅在蒙版类型为文字时生效
            text_italic_degree (`int`, optional): 文字蒙版倾斜度, 仅在蒙版类型为文字时生效
            text_line_gap (`float`, optional): 文字蒙版行间距, 仅在蒙版类型为文字时生效
            text_has_underline (`bool`, optional): 文字蒙版下划线, 仅在蒙版类型为文字时生效
            text_font_resource_id (`str`, optional): 文字蒙版字体资源ID, 仅在蒙版类型为文字时生效
            rect_width (`float`, optional): 矩形蒙版的宽度, 仅在蒙版类型为矩形时允许设置, 以占素材宽度的比例表示, 默认与`size`相同
            round_corner (`float`, optional): 矩形蒙版的圆角参数, 仅在蒙版类型为矩形时允许设置, 取值范围0~100, 默认为0

        Raises:
            `ValueError`: 试图添加多个蒙版或不正确地设置了`rect_width`及`round_corner`
        """

        if self.mask is not None:
            raise ValueError("当前片段已有蒙版, 不能再添加新的蒙版")
        if (rect_width is not None or round_corner is not None) and mask_type != MaskType.矩形:
            raise ValueError("`rect_width` 以及 `round_corner` 仅在蒙版类型为矩形时允许设置")
        if rect_width is None and mask_type == MaskType.矩形:
            rect_width = size
        if round_corner is None:
            round_corner = 0
        text_config_override = None
        if mask_type == MaskType.文字:
            if text_content is None:
                text_content = "默认文本"
            text_config_override = {
                "align_type": text_align_type,
                "bold_width": text_bold_width,
                "char_spacing": text_char_spacing,
                "content": text_content,
                "font_name": text_font_name,
                "font_path": text_font_path,
                "font_resource_id": text_font_resource_id,
                "font_size": text_font_size,
                "has_underline": text_has_underline,
                "italic_degree": text_italic_degree,
                "line_gap": text_line_gap,
                "scale": text_scale
            }

        width = rect_width or size * self.material_size[1] * mask_type.value.default_aspect_ratio / self.material_size[0]
        self.mask = Mask(mask_type.value, center_x / (self.material_size[0] / 2), center_y / (self.material_size[1] / 2),
                         w=width, h=size, ratio=mask_type.value.default_aspect_ratio,
                         rot=rotation, inv=invert, feather=feather/100, round_corner=round_corner/100,
                         expansion=expansion/100,
                         text_config_override=text_config_override)
        self.extra_material_refs.append(self.mask.global_id)
        return self

    def add_transition(self, transition_type: TransitionType, *, duration: Optional[Union[int, str]] = None) -> "VideoSegment":
        """为视频片段添加转场, 注意转场应当添加在**前面的**片段上

        Args:
            transition_type (`TransitionType`): 转场类型
            duration (`int` or `str`, optional): 转场持续时间, 单位为微秒. 若传入字符串则会调用`tim()`函数进行解析. 若不指定则使用转场类型定义的默认值.

        Raises:
            `ValueError`: 试图添加多个转场.
        """
        if self.transition is not None:
            raise ValueError("当前片段已有转场, 不能再添加新的转场")
        if isinstance(duration, str): duration = tim(duration)

        self.transition = Transition(transition_type, duration)
        self.extra_material_refs.append(self.transition.global_id)
        return self

    def add_background_filling(self, fill_type: Literal["blur", "color"], blur: float = 0.0625, color: str = "#00000000") -> "VideoSegment":
        """为视频片段添加背景填充

        注意: 背景填充仅对底层视频轨道上的片段生效

        Args:
            fill_type (`blur` or `color`): 填充类型, `blur`表示模糊, `color`表示颜色.
            blur (`float`, optional): 模糊程度, 0.0-1.0. 仅在`fill_type`为`blur`时有效. 剪映中的四档模糊数值分别为0.0625, 0.375, 0.75和1.0, 默认为0.0625.
            color (`str`, optional): 填充颜色, 格式为'#RRGGBBAA'. 仅在`fill_type`为`color`时有效.

        Raises:
            `ValueError`: 当前片段已有背景填充效果或`fill_type`无效.
        """
        if self.background_filling is not None:
            raise ValueError("当前片段已有背景填充效果")

        if fill_type == "blur":
            self.background_filling = BackgroundFilling("canvas_blur", blur, color)
        elif fill_type == "color":
            self.background_filling = BackgroundFilling("canvas_color", blur, color)
        else:
            raise ValueError(f"无效的背景填充类型 {fill_type}")

        self.extra_material_refs.append(self.background_filling.global_id)
        return self

    def export_json(self) -> Dict[str, Any]:
        json_dict = super().export_json()
        json_dict.update({
            "hdr_settings": {"intensity": 1.0, "mode": 1, "nits": 1000},
        })
        json_dict["enable_adjust_mask"] = True
        json_dict["enable_video_mask"] = True
        return json_dict

class StickerSegment(VisualSegment):
    """安放在轨道上的一个贴纸片段"""

    resource_id: str
    """贴纸资源id"""

    def __init__(self, resource_id: str, target_timerange: Timerange, *, clip_settings: Optional[ClipSettings] = None):
        """根据贴纸resource_id构建一个贴纸片段, 并指定其时间信息及图像调节设置

        片段创建完成后, 可通过`ScriptFile.add_segment`方法将其添加到轨道中

        Args:
            resource_id (`str`): 贴纸resource_id, 可通过`ScriptFile.inspect_material`从模板中获取
            target_timerange (`Timerange`): 片段在轨道上的目标时间范围
            clip_settings (`ClipSettings`, optional): 图像调节设置, 默认不作任何变换
        """
        super().__init__(uuid.uuid4().hex, None, target_timerange, 1.0, 1.0, False, clip_settings=clip_settings)
        self.resource_id = resource_id

    def export_material(self) -> Dict[str, Any]:
        """创建极简的贴纸素材对象, 以此不再单独定义贴纸素材类"""
        return {
            "id": self.material_id,
            "resource_id": self.resource_id,
            "sticker_id": self.resource_id,
            "source_platform": 1,
            "type": "sticker",
        }
