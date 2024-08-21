import uuid

from enum import Enum
from typing import TypeVar, Generic
from typing import Dict, List, Any, Literal

from .segment import Base_segment
from .video_segment import Video_segment
from .audio_segment import Audio_segment
from .text_segment import Text_segment
from .effect_segment import Effect_segment, Filter_segment

class Track_type(Enum):
    """轨道类型枚举

    变量名对应type属性, 值表示可接受的片段类型
    """

    video = Video_segment
    audio = Audio_segment
    effect = Effect_segment
    filter = Filter_segment
    text = Text_segment

Seg_type = TypeVar("Seg_type", bound=Base_segment)
class Track(Generic[Seg_type]):
    """轨道"""

    track_type: Track_type
    """轨道类型"""
    name: str
    """轨道名称"""
    track_id: str
    """轨道全局ID, 由程序自动生成"""

    segments: List[Seg_type]

    def __init__(self, track_type: Track_type, name: str):
        self.track_type = track_type
        self.name = name
        self.track_id = uuid.uuid4().hex

        self.segments = []

    def add_segment(self, segment: Seg_type) -> "Track[Seg_type]":
        """向轨道中添加一个片段, 添加的片段必须匹配轨道类型且不与现有片段重叠

        Args:
            segment (Seg_type): 要添加的片段

        Raises:
            `TypeError`: 新片段类型与轨道类型不匹配
            `ValueError`: 新片段与现有片段重叠
        """
        if not isinstance(segment, self.track_type.value):
            raise TypeError("New segment (%s) is not of the same type as the track (%s)" % (type(segment), self.track_type.value))

        # 检查片段是否重叠
        for seg in self.segments:
            if seg.overlaps(segment):
                raise ValueError("New segment overlaps with existing segment [start: {}, duration: {}]" \
                                .format(seg.target_timerange.start, seg.target_timerange.duration))

        self.segments.append(segment)
        return self

    def export_json(self) -> Dict[str, Any]:
        return {
            "attribute": 0,
            "flag": 0,
            "id": self.track_id,
            "is_default_name": len(self.name) == 0,
            "name": self.name,
            "segments": [seg.export_json() for seg in self.segments],
            "type": self.track_type.name
        }
