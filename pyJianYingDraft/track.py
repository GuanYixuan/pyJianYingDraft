import uuid

from enum import Enum
from typing import TypeVar, Generic, Type
from typing import Dict, List, Any, Union, Optional
from dataclasses import dataclass

from .segment import Base_segment
from .video_segment import Video_segment
from .audio_segment import Audio_segment
from .text_segment import Text_segment
from .effect_segment import Effect_segment, Filter_segment

@dataclass
class Track_meta:
    """与轨道类型关联的轨道元数据"""

    segment_type: Union[Type[Video_segment], Type[Audio_segment], Type[Effect_segment], Type[Filter_segment], Type[Text_segment]]
    """与轨道关联的片段类型"""
    render_index: int
    """默认渲染顺序, 值越大越接近前景"""

class Track_type(Enum):
    """轨道类型枚举

    变量名对应type属性, 值表示相应的轨道元数据
    """

    video = Track_meta(Video_segment, 0)
    audio = Track_meta(Audio_segment, 0)
    effect = Track_meta(Effect_segment, 10000)
    filter = Track_meta(Filter_segment, 11000)
    text = Track_meta(Text_segment, 14000)

Seg_type = TypeVar("Seg_type", bound=Base_segment)
class Track(Generic[Seg_type]):
    """轨道"""

    track_type: Track_type
    """轨道类型"""
    name: str
    """轨道名称"""
    track_id: str
    """轨道全局ID, 由程序自动生成"""
    render_index: int
    """渲染顺序, 值越大越接近前景"""

    segments: List[Seg_type]

    def __init__(self, track_type: Track_type, name: str, render_index: int):
        self.track_type = track_type
        self.name = name
        self.track_id = uuid.uuid4().hex
        self.render_index = render_index

        self.segments = []

    @property
    def accept_segment_type(self) -> Type[Seg_type]:
        """返回该轨道允许的片段类型"""
        return self.track_type.value.segment_type # type: ignore

    def add_segment(self, segment: Seg_type) -> "Track[Seg_type]":
        """向轨道中添加一个片段, 添加的片段必须匹配轨道类型且不与现有片段重叠

        Args:
            segment (Seg_type): 要添加的片段

        Raises:
            `TypeError`: 新片段类型与轨道类型不匹配
            `ValueError`: 新片段与现有片段重叠
        """
        if not isinstance(segment, self.accept_segment_type):
            raise TypeError("New segment (%s) is not of the same type as the track (%s)" % (type(segment), self.accept_segment_type))

        # 检查片段是否重叠
        for seg in self.segments:
            if seg.overlaps(segment):
                raise ValueError("New segment overlaps with existing segment [start: {}, duration: {}]" \
                                .format(seg.target_timerange.start, seg.target_timerange.duration))

        self.segments.append(segment)
        return self

    def export_json(self) -> Dict[str, Any]:
        # 为每个片段写入render_index
        segment_exports = [seg.export_json() for seg in self.segments]
        for seg in segment_exports:
            seg["render_index"] = self.render_index

        return {
            "attribute": 0,
            "flag": 0,
            "id": self.track_id,
            "is_default_name": len(self.name) == 0,
            "name": self.name,
            "segments": segment_exports,
            "type": self.track_type.name
        }
