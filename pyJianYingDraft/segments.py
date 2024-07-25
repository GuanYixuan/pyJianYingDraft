import uuid

from enum import Enum
from typing import Optional, Literal, Union
from typing import Dict, List, Any

from .local_materials import Video_material, Audio_material
from .keyframe import Keyframe_property, Keyframe_list

from .metadata.effect_meta import Effect_param_instance
from .metadata.animation_meta import Video_intro_type, Video_outro_type, Video_group_animation_type
from .metadata.audio_effect_meta import Audio_scene_effect_type, Tone_effect_type, Speech_to_song_type

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

class Timerange:
    """记录了起始时间及持续长度的时间范围"""
    start: int
    """起始时间, 单位为微秒"""
    duration: int
    """持续长度, 单位为微秒"""

    def __init__(self, start: int, duration: int):
        self.start = start
        self.duration = duration

    def export_json(self) -> Dict[str, int]:
        return {"start": self.start, "duration": self.duration}

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

    category_id: Literal["in", "out", "group"]
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
            self.category_id = "in"
            self.category_name = "入场"

            self.is_video_animation = True
        elif isinstance(animation_type, Video_outro_type):
            self.animation_type = "out"
            self.category_id = "out"
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

class Base_segment:
    """片段基类"""

    segment_id: str
    """片段全局id, 自动生成"""
    material_id: str
    """使用的素材id"""
    source_timerange: Timerange
    """截取的素材片段的时间范围"""
    target_timerange: Timerange
    """片段在轨道上的时间范围"""
    speed: float
    """播放速度"""
    volume: float
    """音量"""

    common_keyframes: List[Keyframe_list]
    """各属性的关键帧列表"""
    extra_material_refs: List[str]
    """附加的素材id列表, 用于链接动画/特效等"""

    def __init__(self, material_id: str, source_timerange: Timerange, target_timerange: Timerange, speed: float, volume: float):
        self.segment_id = uuid.uuid4().hex
        self.material_id = material_id
        self.source_timerange = source_timerange
        self.target_timerange = target_timerange
        self.speed = speed
        self.volume = volume

        self.common_keyframes = []
        self.extra_material_refs = []

    def export_json(self) -> Dict[str, Any]:
        """返回通用于音频和视频片段的默认属性"""
        return {
            "caption_info": None,
            "cartoon": False,
            "enable_adjust": True,
            "enable_color_correct_adjust": False,
            "enable_color_curves": True,
            "enable_color_match_adjust": False,
            "enable_color_wheels": True,
            "enable_lut": True,
            "enable_smart_color_adjust": False,
            "group_id": "",
            "intensifies_audio": False,
            "is_placeholder": False,
            "is_tone_modify": False,
            "last_nonzero_volume": 1.0,
            "responsive_layout": {"enable": False, "horizontal_pos_layout": 0, "size_layout": 0, "vertical_pos_layout": 0, "target_follow": ""},
            "reverse": False,
            "template_id": "",
            "template_scene": "default",
            "track_attribute": 0,
            "track_render_index": 0,
            "visible": True,
            # 写入自定义字段
            "id": self.segment_id,
            "material_id": self.material_id,
            "source_timerange": self.source_timerange.export_json(),
            "target_timerange": self.target_timerange.export_json(),
            "speed": self.speed,
            "volume": self.volume,

            "common_keyframes": [kf_list.export_json() for kf_list in self.common_keyframes],
            "extra_material_refs": self.extra_material_refs,
            "keyframe_refs": [], # 意义不明
        }

class Video_segment(Base_segment):
    """安放在轨道上的一个视频/图片片段"""

    clip_settings: Clip_settings
    """图像调节设置, 其效果可被关键帧覆盖"""

    uniform_scale: bool
    """是否锁定XY轴缩放比例"""
    animations_instance: Optional[Segment_animations]
    """动画实例, 可能为空"""

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
        self.animations_instance = None

    def attach_animation(self, animation: Segment_animations) -> None:
        """将给定的动画链接到此片段, 你仍然需要调用`Script_file.add_animation`来将动画添加到素材列表中"""
        assert self.animations_instance is None
        self.animations_instance = animation
        self.extra_material_refs.append(animation.animation_id)

    def add_animation(self, animation_type: Union[Video_intro_type, Video_outro_type, Video_group_animation_type]) -> None:
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

    def add_keyframe(self, _property: Keyframe_property, time_offset: int, value: float) -> None:
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
                return
        kf_list = Keyframe_list(_property)
        kf_list.add_keyframe(time_offset, value)
        self.common_keyframes.append(kf_list)

    def export_json(self) -> Dict[str, Any]:
        json_dict = super().export_json()
        json_dict.update({
            "clip": self.clip_settings.export_json(),
            "hdr_settings": {"intensity": 1.0, "mode": 1, "nits": 1000},
            "uniform_scale": {"on": self.uniform_scale, "value": 1.0},
        })
        return json_dict

class Audio_fade:
    """音频淡入淡出效果"""

    fade_id: str
    """淡入淡出效果的全局id, 自动生成"""

    in_duration: int
    """淡入时长, 单位为微秒"""
    out_duration: int
    """淡出时长, 单位为微秒"""

    def __init__(self, in_duration: int, out_duration: int):
        """根据给定的淡入/淡出时长构造一个淡入淡出效果"""

        self.fade_id = uuid.uuid4().hex
        self.in_duration = in_duration
        self.out_duration = out_duration

    def export_json(self) -> Dict[str, Any]:
        return {
            "id": self.fade_id,
            "fade_in_duration": self.in_duration,
            "fade_out_duration": self.out_duration,
            "fade_type": 0,
            "type": "audio_fade"
        }

class Audio_effect:
    """音频特效对象"""

    name: str
    """特效名称"""
    effect_id: str
    """特效全局id, 由剪映本身提供"""
    resource_id: str
    """资源id, 由剪映本身提供"""

    category_id: Literal["sound_effect", "tone", "speech_to_song"]
    category_name: Literal["场景音", "音色", "声音成曲"]

    audio_adjust_params: List[Effect_param_instance]

    def __init__(self, effect_meta: Union[Audio_scene_effect_type, Tone_effect_type, Speech_to_song_type],
                 params: Optional[List[Optional[float]]] = None):
        """根据给定的音效元数据及参数列表构造一个音频特效对象, params的范围是0~100"""

        self.name = effect_meta.value.name
        self.effect_id = uuid.uuid4().hex
        self.resource_id = effect_meta.value.resource_id
        self.audio_adjust_params = []

        if isinstance(effect_meta, Audio_scene_effect_type):
            self.category_id = "sound_effect"
            self.category_name = "场景音"
        elif isinstance(effect_meta, Tone_effect_type):
            self.category_id = "tone"
            self.category_name = "音色"
        elif isinstance(effect_meta, Speech_to_song_type):
            self.category_id = "speech_to_song"
            self.category_name = "声音成曲"
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
            self.audio_adjust_params.append(Effect_param_instance(param, i, val))

    def export_json(self) -> Dict[str, Any]:
        return {
            "audio_adjust_params": [param.export_json() for param in self.audio_adjust_params],
            "category_id": self.category_id,
            "category_name": self.category_name,
            "id": self.effect_id,
            "is_ugc": False,
            "name": self.name,
            "production_path": "",
            "resource_id": self.resource_id,
            "speaker_id": "",
            "sub_type": 1,
            "time_range": {"duration": 0, "start": 0}, # 似乎并未用到
            "type": "audio_effect"
            # 不导出path和constant_material_id
        }

class Audio_segment(Base_segment):
    """安放在轨道上的一个音频片段"""

    fade: Optional[Audio_fade]
    """音频淡入淡出效果, 可能为空

    在放入轨道时自动添加到素材列表中
    """

    effects: List[Audio_effect]
    """音频特效列表

    在放入轨道时自动添加到素材列表中
    """

    def __init__(self, material: Audio_material, target_timerange: Timerange, *,
                 source_timerange: Optional[Timerange] = None, speed: Optional[float] = None, volume: float = 1.0):
        """利用给定的音频素材构建一个轨道片段, 并指定其时间信息及播放速度/音量

        片段创建完成后, 可通过`Script_file.add_segment`方法将其添加到轨道中

        Args:
            material (`Audio_material`): 素材实例, 注意你仍然需要为其调用`Script_file.add_material`来将其添加到素材列表中
            target_timerange (`Timerange`): 片段在轨道上的目标时间范围
            source_timerange (`Timerange`, optional): 截取的素材片段的时间范围, 默认从开头根据`speed`截取与`target_timerange`等长的一部分
            speed (`float`, optional): 播放速度, 默认为1.0. 此项与`source_timerange`同时指定时, 将覆盖`target_timerange`中的时长
            volume (`float`, optional): 音量, 默认为1.0
        """
        if source_timerange is not None and speed is not None:
            target_timerange = Timerange(target_timerange.start, round(source_timerange.duration / speed))
        elif source_timerange is not None and speed is None:
            speed = source_timerange.duration / target_timerange.duration
        else: # source_timerange is None
            speed = speed if speed is not None else 1.0
            source_timerange = Timerange(0, round(target_timerange.duration * speed))

        super().__init__(material.material_id, source_timerange, target_timerange, speed, volume)

        self.fade = None
        self.effects = []

    def add_effect(self, effect_type: Union[Audio_scene_effect_type, Tone_effect_type, Speech_to_song_type],
                   params: Optional[List[Optional[float]]] = None) -> "Audio_segment":
        """为音频片段添加一个作用于整个片段的音频效果, 目前“声音成曲”效果不能自动被剪映所识别

        Args:
            effect_type (`Audio_scene_effect_type` | `Tone_effect_type` | `Speech_to_song_type`): 音效类型, 一类音效只能添加一个.
            params (`List[Optional[float]]`, optional): 音效参数列表, 参数列表中未提供或为None的项使用默认值.
                参数列表的顺序及参数取值范围(0~100)均与剪映中一致. 音效类型可查阅枚举类的具体定义.

        Raises:
            `ValueError`: 试图添加一个已经存在的音效类型, 或提供的参数数量超过了该音效类型的参数数量.
        """
        if params is not None and len(params) > len(effect_type.value.params):
            raise ValueError("Too many parameters for effect %s" % effect_type.value.name)

        effect_inst = Audio_effect(effect_type, params)
        if effect_inst.category_id in [eff.category_id for eff in self.effects]:
            raise ValueError("Audio segment already has an effect of this category (%s)" % effect_inst.category_name)
        self.effects.append(effect_inst)
        self.extra_material_refs.append(effect_inst.effect_id)

        return self

    def add_fade(self, in_duration: int, out_duration: int) -> "Audio_segment":
        """为音频片段添加淡入淡出效果

        Args:
            in_duration (`int`): 音频淡入时长, 单位为微秒
            out_duration (`int`): 音频淡出时长, 单位为微秒

        Raises:
            `ValueError`: 当前片段已存在淡入淡出效果
        """
        if self.fade is not None:
            raise ValueError("Audio segment already has a fade")
        self.fade = Audio_fade(in_duration, out_duration)
        self.extra_material_refs.append(self.fade.fade_id)

        return self

    def add_keyframe(self, time_offset: int, volume: float) -> "Audio_segment":
        """为音频片段创建一个*控制音量*的关键帧, 并自动加入到关键帧列表中

        Args:
            time_offset (`int`): 关键帧的时间偏移量, 单位为微秒
            volume (`float`): 音量在`time_offset`处的值
        """
        _property = Keyframe_property.volume
        for kf_list in self.common_keyframes:
            if kf_list.keyframe_property == _property:
                kf_list.add_keyframe(time_offset, volume)
                return self
        kf_list = Keyframe_list(_property)
        kf_list.add_keyframe(time_offset, volume)
        self.common_keyframes.append(kf_list)
        return self

    def export_json(self) -> Dict[str, Any]:
        json_dict = super().export_json()
        json_dict.update({
            "clip": None,
            "hdr_settings": None
        })
        return json_dict
