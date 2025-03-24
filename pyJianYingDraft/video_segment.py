"""定义视频片段及其相关类

包含图像调节设置、动画效果、特效、转场等相关类
"""

import uuid
from copy import deepcopy

from typing import Optional, Literal, Union
from typing import Dict, List, Tuple, Any

from .time_util import tim, Timerange
from .segment import Visual_segment, Clip_settings
from .local_materials import Video_material
from .animation import Segment_animations, Video_animation

from .metadata import Effect_meta, Effect_param_instance
from .metadata import Mask_meta, Mask_type, Filter_type, Transition_type
from .metadata import Intro_type, Outro_type, Group_animation_type
from .metadata import Video_scene_effect_type, Video_character_effect_type

class Mask:
    """蒙版对象"""

    mask_meta: Mask_meta
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
    feather: float
    """羽化程度, 0-1"""
    round_corner: float
    """矩形蒙版的圆角, 0-1"""

    def __init__(self, mask_meta: Mask_meta,
                 cx: float, cy: float, w: float, h: float,
                 ratio: float, rot: float, inv: bool, feather: float, round_corner: float):
        self.mask_meta = mask_meta
        self.global_id = uuid.uuid4().hex

        self.center_x, self.center_y = cx, cy
        self.width, self.height = w, h
        self.aspect_ratio = ratio

        self.rotation = rot
        self.invert = inv
        self.feather = feather
        self.round_corner = round_corner

    def export_json(self) -> Dict[str, Any]:
        return {
            "config": {
                "aspectRatio": self.aspect_ratio,
                "centerX": self.center_x,
                "centerY": self.center_y,
                "feather": self.feather,
                "height": self.height,
                "invert": self.invert,
                "rotation": self.rotation,
                "roundCorner": self.round_corner,
                "width": self.width
            },
            "id": self.global_id,
            "name": self.mask_meta.name,
            "platform": "all",
            "position_info": "",
            "resource_type": self.mask_meta.resource_type,
            "resource_id": self.mask_meta.resource_id,
            "type": "mask"
            # 不导出path字段
        }

class Video_effect:
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

    adjust_params: List[Effect_param_instance]

    def __init__(self, effect_meta: Union[Video_scene_effect_type, Video_character_effect_type],
                 params: Optional[List[Optional[float]]] = None, *,
                 apply_target_type: Literal[0, 2] = 0):
        """根据给定的特效元数据及参数列表构造一个视频特效对象, params的范围是0~100"""

        self.name = effect_meta.value.name
        self.global_id = uuid.uuid4().hex
        self.effect_id = effect_meta.value.effect_id
        self.resource_id = effect_meta.value.resource_id
        self.adjust_params = []

        if isinstance(effect_meta, Video_scene_effect_type):
            self.effect_type = "video_effect"
        elif isinstance(effect_meta, Video_character_effect_type):
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

    effect_meta: Effect_meta
    """滤镜的元数据"""
    intensity: float
    """滤镜强度(滤镜的唯一参数)"""

    apply_target_type: Literal[0, 2]
    """应用目标类型, 0: 片段, 2: 全局"""

    def __init__(self, meta: Effect_meta, intensity: float, *,
                 apply_target_type: Literal[0, 2] = 0):
        """根据给定的滤镜元数据及强度构造滤镜素材对象"""

        self.global_id = uuid.uuid4().hex
        self.effect_meta = meta
        self.intensity = intensity
        self.apply_target_type = apply_target_type

    def export_json(self) -> Dict[str, Any]:
        return {
            "adjust_params": [],
            "algorithm_artifact_path": "",
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

    def __init__(self, effect_meta: Transition_type, duration: Optional[int] = None):
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

class Video_segment(Visual_segment):
    """安放在轨道上的一个视频/图片片段"""

    material_instance: Video_material
    """素材实例"""
    material_size: Tuple[int, int]
    """素材尺寸"""

    effects: List[Video_effect]
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

    # TODO: material参数接受path进行便捷构造
    def __init__(self, material: Video_material, target_timerange: Timerange, *,
                 source_timerange: Optional[Timerange] = None, speed: Optional[float] = None, volume: float = 1.0,
                 clip_settings: Optional[Clip_settings] = None):
        """利用给定的视频/图片素材构建一个轨道片段, 并指定其时间信息及图像调节设置

        Args:
            material (`Video_material`): 素材实例
            target_timerange (`Timerange`): 片段在轨道上的目标时间范围
            source_timerange (`Timerange`, optional): 截取的素材片段的时间范围, 默认从开头根据`speed`截取与`target_timerange`等长的一部分
            speed (`float`, optional): 播放速度, 默认为1.0. 此项与`source_timerange`同时指定时, 将覆盖`target_timerange`中的时长
            volume (`float`, optional): 音量, 默认为1.0
            clip_settings (`Clip_settings`, optional): 图像调节设置, 默认不作任何变换

        Raises:
            `ValueError`: 指定的或计算出的`source_timerange`超出了素材的时长范围
        """
        if source_timerange is not None and speed is not None:
            target_timerange = Timerange(target_timerange.start, round(source_timerange.duration / speed))
        elif source_timerange is not None and speed is None:
            speed = source_timerange.duration / target_timerange.duration
        else:  # source_timerange is None
            speed = speed if speed is not None else 1.0
            source_timerange = Timerange(0, round(target_timerange.duration * speed))

        if source_timerange.end > material.duration:
            raise ValueError(f"截取的素材时间范围 {source_timerange} 超出了素材时长({material.duration})")

        super().__init__(material.material_id, source_timerange, target_timerange, speed, volume, clip_settings=clip_settings)

        self.material_instance = deepcopy(material)
        self.material_size = (material.width, material.height)
        self.effects = []
        self.filters = []
        self.transition = None
        self.mask = None

    def add_animation(self, animation_type: Union[Intro_type, Outro_type, Group_animation_type],
                      duration: Optional[Union[int, str]] = None) -> "Video_segment":
        """将给定的入场/出场/组合动画添加到此片段的动画列表中

        Args:
            animation_type (`Intro_type`, `Outro_type`, or `Group_animation_type`): 动画类型
            duration (`int` or `str`, optional): 动画持续时间, 单位为微秒. 若传入字符串则会调用`tim()`函数进行解析.
                若不指定则使用动画类型定义的默认值. 理论上只适用于入场和出场动画.
        """
        if duration is not None:
            duration = tim(duration)
        if isinstance(animation_type, Intro_type):
            start = 0
            duration = duration or animation_type.value.duration
        elif isinstance(animation_type, Outro_type):
            duration = duration or animation_type.value.duration
            start = self.target_timerange.duration - duration
        elif isinstance(animation_type, Group_animation_type):
            start = 0
            duration = duration or self.target_timerange.duration
        else:
            raise TypeError("Invalid animation type %s" % type(animation_type))

        if self.animations_instance is None:
            self.animations_instance = Segment_animations()
            self.extra_material_refs.append(self.animations_instance.animation_id)

        self.animations_instance.add_animation(Video_animation(animation_type, start, duration))

        return self

    def add_effect(self, effect_type: Union[Video_scene_effect_type, Video_character_effect_type],
                   params: Optional[List[Optional[float]]] = None) -> "Video_segment":
        """为视频片段添加一个作用于整个片段的特效

        Args:
            effect_type (`Video_scene_effect_type` or `Video_character_effect_type`): 特效类型
            params (`List[Optional[float]]`, optional): 特效参数列表, 参数列表中未提供或为None的项使用默认值.
                参数取值范围(0~100)与剪映中一致. 某个特效类型有何参数以及具体参数顺序以枚举类成员的annotation为准.

        Raises:
            `ValueError`: 提供的参数数量超过了该特效类型的参数数量, 或参数值超出范围.
        """
        if params is not None and len(params) > len(effect_type.value.params):
            raise ValueError("为音频效果 %s 传入了过多的参数" % effect_type.value.name)

        effect_inst = Video_effect(effect_type, params)
        self.effects.append(effect_inst)
        self.extra_material_refs.append(effect_inst.global_id)

        return self

    def add_filter(self, filter_type: Filter_type, intensity: float = 100.0) -> "Video_segment":
        """为视频片段添加一个滤镜

        Args:
            filter_type (`Filter_type`): 滤镜类型
            intensity (`float`, optional): 滤镜强度(0-100), 仅当所选滤镜能够调节强度时有效. 默认为100.
        """
        filter_inst = Filter(filter_type.value, intensity / 100.0)  # 转化为0~1范围
        self.filters.append(filter_inst)
        self.extra_material_refs.append(filter_inst.global_id)

        return self

    def add_mask(self, mask_type: Mask_type, *, center_x: float = 0.0, center_y: float = 0.0, size: float = 0.5,
                 rotation: float = 0.0, feather: float = 0.0, invert: bool = False,
                 rect_width: Optional[float] = None, round_corner: Optional[float] = None) -> "Video_segment":
        """为视频片段添加蒙版

        Args:
            mask_type (`Mask_type`): 蒙版类型
            center_x (`float`, optional): 蒙版中心点X坐标(以素材的像素为单位), 默认设置在素材中心
            center_y (`float`, optional): 蒙版中心点Y坐标(以素材的像素为单位), 默认设置在素材中心
            size (`float`, optional): 蒙版的"主要尺寸"(镜面的可视部分高度/圆形直径/爱心高度等), 以占素材高度的比例表示, 默认为0.5
            rotation (`float`, optional): 蒙版顺时针旋转的**角度**, 默认不旋转
            feather (`float`, optional): 蒙版的羽化参数, 取值范围0~100, 默认无羽化
            invert (`bool`, optional): 是否反转蒙版, 默认不反转
            rect_width (`float`, optional): 矩形蒙版的宽度, 仅在蒙版类型为矩形时允许设置, 以占素材宽度的比例表示, 默认与`size`相同
            round_corner (`float`, optional): 矩形蒙版的圆角参数, 仅在蒙版类型为矩形时允许设置, 取值范围0~100, 默认为0

        Raises:
            `ValueError`: 试图添加多个蒙版或不正确地设置了`rect_width`及`round_corner`
        """

        if self.mask is not None:
            raise ValueError("当前片段已有蒙版, 不能再添加新的蒙版")
        if (rect_width is not None or round_corner is not None) and mask_type != Mask_type.矩形:
            raise ValueError("`rect_width` 以及 `round_corner` 仅在蒙版类型为矩形时允许设置")
        if rect_width is None and mask_type == Mask_type.矩形:
            rect_width = size
        if round_corner is None:
            round_corner = 0

        width = rect_width or size * self.material_size[1] * mask_type.value.default_aspect_ratio / self.material_size[0]
        self.mask = Mask(mask_type.value, center_x / (self.material_size[0] / 2), center_y / (self.material_size[1] / 2),
                         w=width, h=size, ratio=mask_type.value.default_aspect_ratio,
                         rot=rotation, inv=invert, feather=feather/100, round_corner=round_corner/100)
        self.extra_material_refs.append(self.mask.global_id)
        return self

    def add_transition(self, transition_type: Transition_type, *, duration: Optional[Union[int, str]] = None) -> "Video_segment":
        """为视频片段添加转场, 注意转场应当添加在**前面的**片段上

        Args:
            transition_type (`Transition_type`): 转场类型
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

    def export_json(self) -> Dict[str, Any]:
        json_dict = super().export_json()
        json_dict.update({
            "hdr_settings": {"intensity": 1.0, "mode": 1, "nits": 1000},
        })
        return json_dict

class Sticker_segment(Visual_segment):
    """安放在轨道上的一个贴纸片段"""

    resource_id: str
    """贴纸资源id"""

    def __init__(self, resource_id: str, target_timerange: Timerange, *, clip_settings: Optional[Clip_settings] = None):
        """根据贴纸resource_id构建一个贴纸片段, 并指定其时间信息及图像调节设置

        片段创建完成后, 可通过`Script_file.add_segment`方法将其添加到轨道中

        Args:
            resource_id (`str`): 贴纸resource_id, 可通过`Script_file.inspect_material`从模板中获取
            target_timerange (`Timerange`): 片段在轨道上的目标时间范围
            clip_settings (`Clip_settings`, optional): 图像调节设置, 默认不作任何变换
        """
        super().__init__(uuid.uuid4().hex, None, target_timerange, 1.0, 1.0, clip_settings=clip_settings)
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
