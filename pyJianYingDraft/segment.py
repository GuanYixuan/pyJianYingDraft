"""定义时间范围及片段基类

部分与时间相关的辅助函数也暂时在此定义
"""

import uuid

from typing import Union
from typing import Dict, List, Any

from .keyframe import Keyframe_list

def tim(inp: Union[str, float]) -> int:
    """将输入的字符串或秒数转换为微秒

    支持类似 "1h52m3s" 或 "0.15s" 这样的格式
    """
    if isinstance(inp, (int, float)):
        return int(round(inp * 1000000))

    inp = inp.strip().lower()
    last_index: int = 0
    total_time: float = 0
    for unit, factor in zip(["h", "m", "s"], [3600*1e6, 60*1e6, 1e6]):
        unit_index = inp.find(unit)
        if unit_index == -1: continue

        total_time += float(inp[last_index:unit_index]) * factor
        last_index = unit_index + 1

    return int(round(total_time))

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

def trange(start: Union[str, int], duration: Union[str, int]) -> Timerange:
        """Timerange的简便构造函数, 接受字符串或整数作为参数

        支持类似 "1h52m3s" 或 "0.15s" 这样的格式
        """
        return Timerange(tim(start), tim(duration))


class Base_segment:
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
