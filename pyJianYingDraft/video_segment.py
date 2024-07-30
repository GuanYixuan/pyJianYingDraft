"""定义视频片段及其相关类

包含图像调节设置、动画效果、特效、转场等相关类
"""

import uuid

from typing import Optional, Literal, Union
from typing import Dict, List, Any

from .segment import Base_segment, Timerange
from .local_materials import Video_material
from .keyframe import Keyframe_property, Keyframe_list

from .metadata.effect_meta import Effect_param_instance
from .metadata.animation_meta import Video_intro_type, Video_outro_type, Video_group_animation_type
from .metadata.video_effect_meta import Video_scene_effect_type, Video_character_effect_type
from .metadata.transition_meta import Transition_type

class Clip_settings:
    """素材片段的图像调节设置"""

    alpha: float
    """图像透明度, 0-1"""
    flip_horizontal: bool
    """是否水平翻转"""
    flip_vertical: bool
    """是否垂直翻转"""
    rotation: float
    """旋转角度, 可正可负"""
    scale_x: float
    """水平缩放比例"""
    scale_y: float
    """垂直缩放比例"""
    transform_x: float
    """水平位移, 单位为像素?"""
    transform_y: float
    """垂直位移, 单位为像素?"""

    def __init__(self, *, alpha: float = 1.0,
                 flip_horizontal: bool = False, flip_vertical: bool = False,
                 rotation: float = 0.0,
                 scale_x: float = 1.0, scale_y: float = 1.0,
                 transform_x: float = 0.0, transform_y: float = 0.0):
        """初始化图像调节设置, 默认参数表示不作任何图像变换"""
        self.alpha = alpha
        self.flip_horizontal, self.flip_vertical = flip_horizontal, flip_vertical
        self.rotation = rotation
        self.scale_x, self.scale_y = scale_x, scale_y
        self.transform_x, self.transform_y = transform_x, transform_y

    def export_json(self) -> Dict[str, Any]:
        clip_settings_json = {
            "alpha": self.alpha,
            "flip": {"horizontal": self.flip_horizontal, "vertical": self.flip_vertical},
            "rotation": self.rotation,
            "scale": {"x": self.scale_x, "y": self.scale_y},
            "transform": {"x": self.transform_x, "y": self.transform_y}
        }
        return clip_settings_json

class Animation:
    """一个动画效果"""

    name: str
    """动画名称, 默认取为动画效果的名称"""
    effect_id: str
    """另一种动画id, 由剪映本身提供"""
    animation_type: Literal["in", "out", "group"]
    resource_id: str
    """资源id, 由剪映本身提供"""

    start: int
    """动画相对此片段开头的偏移, 单位为微秒"""
    duration: int
    """动画持续时间, 单位为微秒, 各动画有其默认值"""

    category_id: Literal["ruchang", "chuchang", "group"]
    category_name: Literal["入场", "出场", "组合"]
    """动画类型, 入场/出场/组合"""

    is_video_animation: bool

    def __init__(self, animation_type: Union[Video_intro_type, Video_outro_type, Video_group_animation_type],
                 start: int, duration: int):
        type_meta = animation_type.value
        self.name = type_meta.title
        self.effect_id = type_meta.effect_id
        self.resource_id = type_meta.resource_id

        if isinstance(animation_type, Video_intro_type):
            self.animation_type = "in"
            self.category_id = "ruchang"
            self.category_name = "入场"

            self.is_video_animation = True
        elif isinstance(animation_type, Video_outro_type):
            self.animation_type = "out"
            self.category_id = "chuchang"
            self.category_name = "出场"

            self.is_video_animation = True
        elif isinstance(animation_type, Video_group_animation_type):
            self.animation_type = "group"
            self.category_id = "group"
            self.category_name = "组合"

            self.is_video_animation = True

        self.start = start
        self.duration = duration

    def export_json(self) -> Dict[str, Any]:
        return {
            "anim_adjust_params": None,
            "platform": "all",
            "panel": "video" if self.is_video_animation else "",
            "material_type": "video" if self.is_video_animation else "sticker",

            "name": self.name,
            "id": self.effect_id,
            "type": self.animation_type,
            "resource_id": self.resource_id,
            "category_id": self.category_id,
            "category_name": self.category_name,

            "start": self.start,
            "duration": self.duration,
            # 不导出path和request_id字段
        }

class Segment_animations:
    """附加于某素材上的一系列动画（一般是入场、出场）"""

    animation_id: str
    """动画系列全局id, 自动生成"""
    animation_type: str
    """animation_type字段, 似乎总是'sticker_animation'"""

    animations: List[Animation]
    """动画列表"""

    def __init__(self, animation_type: str = "sticker_animation"):
        self.animation_id = uuid.uuid4().hex
        self.animation_type = animation_type
        self.animations = []

    def add_animation(self, animation: Animation) -> None:
        # 不允许添加超过一个同类型的动画（如两个入场动画）
        if animation.animation_type in [ani.animation_type for ani in self.animations]:
            raise ValueError(f"Duplicate animation type '{animation.animation_type}'")
        # 不允许组合动画与出入场动画同时出现
        if any(ani.animation_type == "group" for ani in self.animations):
            raise ValueError("Group animation contradicts with any other animation")
        if animation.animation_type == "group" and len(self.animations) > 0:
            raise ValueError("Cannot add group animation when there are animations exist")

        self.animations.append(animation)

    def export_json(self) -> Dict[str, Any]:
        return {
            "id": self.animation_id,
            "type": self.animation_type,
            "multi_language_current": "none",
            "animations": [animation.export_json() for animation in self.animations]
        }

class Video_effect:
    """视频特效对象"""

    name: str
    """特效名称"""
    global_id: str
    """特效全局id, 由程序自动生成"""
    effect_id: str
    """某种特效id, 由剪映本身提供"""
    resource_id: str
    """资源id, 由剪映本身提供"""

    effect_type: Literal["video_effect", "face_effect"]

    adjust_params: List[Effect_param_instance]

    def __init__(self, effect_meta: Union[Video_scene_effect_type, Video_character_effect_type],
                 params: Optional[List[Optional[float]]] = None):
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

        if params is None: params = []
        for i, param in enumerate(effect_meta.value.params):
            val = param.default_value
            if i < len(params):
                input_v = params[i]
                if input_v is not None:
                    if input_v < 0 or input_v > 100:
                        raise ValueError("Invalid parameter value %f within %s" % (input_v, str(param)))
                    val = param.min_value + (param.max_value - param.min_value) * input_v / 100.0 # 从0~100映射到实际值
            self.adjust_params.append(Effect_param_instance(param, i, val))

    def export_json(self) -> Dict[str, Any]:
        return {
            "adjust_params": [param.export_json() for param in self.adjust_params],
            "apply_target_type": 0,
            "apply_time_range": None,
            "category_id": "", # 一律设为空
            "category_name": "", # 一律设为空
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

    def __init__(self, effect_meta: Transition_type, *, duration: Optional[int] = None):
        """根据给定的转场元数据及持续时间构造一个转场对象"""
        self.name = effect_meta.value.name
        self.global_id = uuid.uuid4().hex
        self.effect_id = effect_meta.value.effect_id
        self.resource_id = effect_meta.value.resource_id

        self.duration = duration if duration is not None else effect_meta.value.default_duration
        self.is_overlap = effect_meta.value.is_overlap

    def export_json(self) -> Dict[str, Any]:
        return {
            "category_id": "", # 一律设为空
            "category_name": "", # 一律设为空
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

class Video_segment(Base_segment):
    """安放在轨道上的一个视频/图片片段"""

    clip_settings: Clip_settings
    """图像调节设置, 其效果可被关键帧覆盖"""

    uniform_scale: bool
    """是否锁定XY轴缩放比例"""

    effects: List[Video_effect]
    """特效列表

    在放入轨道时自动添加到素材列表中
    """
    animations_instance: Optional[Segment_animations]
    """动画实例, 可能为空

    在放入轨道时自动添加到素材列表中
    """

    def __init__(self, material: Video_material, target_timerange: Timerange, *,
                 source_timerange: Optional[Timerange] = None, speed: Optional[float] = None, volume: float = 1.0,
                 clip_settings: Optional[Clip_settings] = None):
        """利用给定的视频/图片素材构建一个轨道片段, 并指定其时间信息及图像调节设置

        片段创建完成后, 可通过`Script_file.add_segment`方法将其添加到轨道中

        Args:
            material (`Video_material`): 素材实例, 注意你仍然需要为其调用`Script_file.add_material`来将其添加到素材列表中
            target_timerange (`Timerange`): 片段在轨道上的目标时间范围
            source_timerange (`Timerange`, optional): 截取的素材片段的时间范围, 默认从开头根据`speed`截取与`target_timerange`等长的一部分
            speed (`float`, optional): 播放速度, 默认为1.0. 此项与`source_timerange`同时指定时, 将覆盖`target_timerange`中的时长
            volume (`float`, optional): 音量, 默认为1.0
            clip_settings (`Clip_settings`, optional): 图像调节设置, 默认不作任何变换
        """
        if source_timerange is not None and speed is not None:
            target_timerange = Timerange(target_timerange.start, round(source_timerange.duration / speed))
        elif source_timerange is not None and speed is None:
            speed = source_timerange.duration / target_timerange.duration
        else: # source_timerange is None
            speed = speed if speed is not None else 1.0
            source_timerange = Timerange(0, round(target_timerange.duration * speed))

        super().__init__(material.material_id, source_timerange, target_timerange, speed, volume)

        self.clip_settings = clip_settings if clip_settings is not None else Clip_settings()
        self.uniform_scale = True
        self.effects = []
        self.animations_instance = None

    def add_animation(self, animation_type: Union[Video_intro_type, Video_outro_type, Video_group_animation_type]) -> "Video_segment":
        """将给定的入场/出场/组合动画添加到此片段的动画列表中, 动画的起止时间自动确定"""
        if isinstance(animation_type, Video_intro_type):
            start = 0
            duration = animation_type.value.duration
        elif isinstance(animation_type, Video_outro_type):
            start = self.target_timerange.duration - animation_type.value.duration
            duration = animation_type.value.duration
        elif isinstance(animation_type, Video_group_animation_type):
            start = 0
            duration = self.target_timerange.duration
        else:
            raise TypeError("Invalid animation type %s" % type(animation_type))

        if self.animations_instance is None:
            self.animations_instance = Segment_animations()
            self.extra_material_refs.append(self.animations_instance.animation_id)

        self.animations_instance.add_animation(Animation(animation_type, start, duration))

        return self

    def add_effect(self, effect_type: Union[Video_scene_effect_type, Video_character_effect_type], params: Optional[List[Optional[float]]] = None) -> "Video_segment":
        """为视频片段添加一个作用于整个片段的特效"""
        if params is not None and len(params) > len(effect_type.value.params):
            raise ValueError("Too many parameters for effect %s" % effect_type.value.name)

        effect_inst = Video_effect(effect_type, params)
        self.effects.append(effect_inst)
        self.extra_material_refs.append(effect_inst.global_id)

        return self

    def add_keyframe(self, _property: Keyframe_property, time_offset: int, value: float) -> "Video_segment":
        """为给定属性创建一个关键帧, 并自动加入到关键帧列表中

        Args:
            _property (`Keyframe_property`): 要控制的属性
            time_offset (`int`): 关键帧的时间偏移量, 单位为微秒
            value (`float`): 属性在`time_offset`处的值

        Raises:
            `ValueError`: 试图同时设置`uniform_scale`以及`scale_x`或`scale_y`其中一者

        """
        if (_property == Keyframe_property.scale_x or _property == Keyframe_property.scale_y) and self.uniform_scale:
            self.uniform_scale = False
        elif _property == Keyframe_property.uniform_scale:
            if not self.uniform_scale: raise ValueError("Cannot set uniform_scale when scale_x or scale_y already exist")
            _property = Keyframe_property.scale_x

        for kf_list in self.common_keyframes:
            if kf_list.keyframe_property == _property:
                kf_list.add_keyframe(time_offset, value)
                return self
        kf_list = Keyframe_list(_property)
        kf_list.add_keyframe(time_offset, value)
        self.common_keyframes.append(kf_list)
        return self

    def export_json(self) -> Dict[str, Any]:
        json_dict = super().export_json()
        json_dict.update({
            "clip": self.clip_settings.export_json(),
            "hdr_settings": {"intensity": 1.0, "mode": 1, "nits": 1000},
            "uniform_scale": {"on": self.uniform_scale, "value": 1.0},
        })
        return json_dict
