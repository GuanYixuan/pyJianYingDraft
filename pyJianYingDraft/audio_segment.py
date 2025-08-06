"""定义音频片段及其相关类

包含淡入淡出效果、音频特效等相关类
"""

import uuid
from copy import deepcopy

from typing import Optional, Literal, Union
from typing import Dict, List, Any

from .time_util import tim, Timerange
from .segment import MediaSegment
from .local_materials import AudioMaterial
from .keyframe import KeyframeProperty, KeyframeList

from .metadata import EffectParamInstance
from .metadata import AudioSceneEffectType, ToneEffectType, SpeechToSongType

class AudioFade:
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

class AudioEffect:
    """音频特效对象"""

    name: str
    """特效名称"""
    effect_id: str
    """特效全局id, 由程序自动生成"""
    resource_id: str
    """资源id, 由剪映本身提供"""

    category_id: Literal["sound_effect", "tone", "speech_to_song"]
    category_name: Literal["场景音", "音色", "声音成曲"]
    category_index: Literal[1, 2, 3]

    audio_adjust_params: List[EffectParamInstance]

    def __init__(self, effect_meta: Union[AudioSceneEffectType, ToneEffectType, SpeechToSongType],
                 params: Optional[List[Optional[float]]] = None):
        """根据给定的音效元数据及参数列表构造一个音频特效对象, params的范围是0~100"""

        self.name = effect_meta.value.name
        self.effect_id = uuid.uuid4().hex
        self.resource_id = effect_meta.value.resource_id
        self.audio_adjust_params = []

        if isinstance(effect_meta, AudioSceneEffectType):
            self.category_id = "sound_effect"
            self.category_name = "场景音"
            self.category_index = 1
        elif isinstance(effect_meta, ToneEffectType):
            self.category_id = "tone"
            self.category_name = "音色"
            self.category_index = 2
        elif isinstance(effect_meta, SpeechToSongType):
            self.category_id = "speech_to_song"
            self.category_name = "声音成曲"
            self.category_index = 3
        else:
            raise TypeError("不支持的元数据类型 %s" % type(effect_meta))

        self.audio_adjust_params = effect_meta.value.parse_params(params)

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
            "sub_type": self.category_index,
            "time_range": {"duration": 0, "start": 0},  # 似乎并未用到
            "type": "audio_effect"
            # 不导出path和constant_material_id
        }

class AudioSegment(MediaSegment):
    """安放在轨道上的一个音频片段"""

    material_instance: AudioMaterial
    """音频素材实例"""

    fade: Optional[AudioFade]
    """音频淡入淡出效果, 可能为空

    在放入轨道时自动添加到素材列表中
    """

    effects: List[AudioEffect]
    """音频特效列表

    在放入轨道时自动添加到素材列表中
    """

    def __init__(self, material: Union[AudioMaterial, str], target_timerange: Timerange, *,
                 source_timerange: Optional[Timerange] = None, speed: Optional[float] = None, volume: float = 1.0,
                 change_pitch: bool = False):
        """利用给定的音频素材构建一个轨道片段, 并指定其时间信息及播放速度/音量

        Args:
            material (`AudioMaterial` or `str`): 素材实例或素材路径, 若为路径则自动构造素材实例
            target_timerange (`Timerange`): 片段在轨道上的目标时间范围
            source_timerange (`Timerange`, optional): 截取的素材片段的时间范围, 默认从开头根据`speed`截取与`target_timerange`等长的一部分
            speed (`float`, optional): 播放速度, 默认为1.0. 此项与`source_timerange`同时指定时, 将覆盖`target_timerange`中的时长
            volume (`float`, optional): 音量, 默认为1.0
            change_pitch (`bool`, optional): 是否跟随变速改变音调, 默认为否

        Raises:
            `ValueError`: 指定的或计算出的`source_timerange`超出了素材的时长范围
        """
        if isinstance(material, str):
            material = AudioMaterial(material)

        if source_timerange is not None and speed is not None:
            target_timerange = Timerange(target_timerange.start, round(source_timerange.duration / speed))
        elif source_timerange is not None and speed is None:
            speed = source_timerange.duration / target_timerange.duration
        else:  # source_timerange is None
            speed = speed if speed is not None else 1.0
            source_timerange = Timerange(0, round(target_timerange.duration * speed))

        if source_timerange.end > material.duration:
            raise ValueError(f"截取的素材时间范围 {source_timerange} 超出了素材时长({material.duration})")

        super().__init__(material.material_id, source_timerange, target_timerange, speed, volume, change_pitch)

        self.material_instance = deepcopy(material)
        self.fade = None
        self.effects = []

    def add_effect(self, effect_type: Union[AudioSceneEffectType, ToneEffectType, SpeechToSongType],
                   params: Optional[List[Optional[float]]] = None) -> "AudioSegment":
        """为音频片段添加一个作用于整个片段的音频效果, 目前"声音成曲"效果不能自动被剪映所识别

        Args:
            effect_type (`AudioSceneEffectType` | `ToneEffectType` | `SpeechToSongType`): 音效类型, 一类音效只能添加一个.
            params (`List[Optional[float]]`, optional): 音效参数列表, 参数列表中未提供或为None的项使用默认值.
                参数取值范围(0~100)与剪映中一致. 某个特效类型有何参数以及具体参数顺序以枚举类成员的annotation为准.

        Raises:
            `ValueError`: 试图添加一个已经存在的音效类型、提供的参数数量超过了该音效类型的参数数量, 或参数值超出范围.
        """
        if params is not None and len(params) > len(effect_type.value.params):
            raise ValueError("为音频效果 %s 传入了过多的参数" % effect_type.value.name)

        effect_inst = AudioEffect(effect_type, params)
        if effect_inst.category_id in [eff.category_id for eff in self.effects]:
            raise ValueError("当前音频片段已经有此类型 (%s) 的音效了" % effect_inst.category_name)
        self.effects.append(effect_inst)
        self.extra_material_refs.append(effect_inst.effect_id)

        return self

    def add_fade(self, in_duration: Union[str, int], out_duration: Union[str, int]) -> "AudioSegment":
        """为音频片段添加淡入淡出效果

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

    def add_keyframe(self, time_offset: int, volume: float) -> "AudioSegment":
        """为音频片段创建一个*控制音量*的关键帧, 并自动加入到关键帧列表中

        Args:
            time_offset (`int`): 关键帧的时间偏移量, 单位为微秒
            volume (`float`): 音量在`time_offset`处的值
        """
        _property = KeyframeProperty.volume
        for kf_list in self.common_keyframes:
            if kf_list.keyframe_property == _property:
                kf_list.add_keyframe(time_offset, volume)
                return self
        kf_list = KeyframeList(_property)
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
