"""定义时间范围及片段基类

部分与时间相关的辅助函数也暂时在此定义
"""

import uuid

from abc import ABC
from typing import Dict, List, Any

from .time_util import Timerange
from .keyframe import Keyframe_list

class Base_segment(ABC):
    """片段基类"""

    segment_id: str
    """片段全局id, 由程序自动生成"""
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

    def overlaps(self, other: "Base_segment") -> bool:
        """判断是否与另一个片段有重叠"""
        return not (self.target_timerange.start + self.target_timerange.duration <= other.target_timerange.start or
                    self.target_timerange.start >= other.target_timerange.start + other.target_timerange.duration)

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
