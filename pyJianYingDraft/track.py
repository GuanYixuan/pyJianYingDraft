"""轨道类及其元数据"""

import uuid

from enum import Enum
from typing import TypeVar, Generic, Type
from typing import Dict, List, Any, Union
from dataclasses import dataclass
from abc import ABC, abstractmethod

from .exceptions import SegmentOverlap
from .segment import Base_segment
from .video_segment import Video_segment, Sticker_segment
from .audio_segment import Audio_segment
from .text_segment import Text_segment
from .effect_segment import Effect_segment, Filter_segment

@dataclass
class Track_meta:
    """与轨道类型关联的轨道元数据"""

    segment_type: Union[Type[Video_segment], Type[Audio_segment],
                        Type[Effect_segment], Type[Filter_segment],
                        Type[Text_segment], Type[Sticker_segment], None]
    """与轨道关联的片段类型"""
    render_index: int
    """默认渲染顺序, 值越大越接近前景"""
    allow_modify: bool
    """当被导入时, 是否允许修改"""

class Track_type(Enum):
    """轨道类型枚举

    变量名对应type属性, 值表示相应的轨道元数据
    """

    video = Track_meta(Video_segment, 0, True)
    audio = Track_meta(Audio_segment, 0, True)
    effect = Track_meta(Effect_segment, 10000, False)
    filter = Track_meta(Filter_segment, 11000, False)
    sticker = Track_meta(Sticker_segment, 14000, False)
    text = Track_meta(Text_segment, 15000, True)  # 原本是14000, 避免与sticker冲突改为15000

    adjust = Track_meta(None, 0, False)
    """仅供导入时使用, 不要尝试新建此类型的轨道"""

    @staticmethod
    def from_name(name: str) -> "Track_type":
        """根据名称获取轨道类型枚举"""
        for t in Track_type:
            if t.name == name:
                return t
        raise ValueError("Invalid track type: %s" % name)


class Base_track(ABC):
    """轨道基类"""

    track_type: Track_type
    """轨道类型"""
    name: str
    """轨道名称"""
    track_id: str
    """轨道全局ID"""
    render_index: int
    """渲染顺序, 值越大越接近前景"""

    @abstractmethod
    def export_json(self) -> Dict[str, Any]: ...

Seg_type = TypeVar("Seg_type", bound=Base_segment)
class Track(Base_track, Generic[Seg_type]):
    """非模板模式下的轨道"""

    mute: bool
    """是否静音"""

    segments: List[Seg_type]
    """该轨道包含的片段列表"""

    def __init__(self, track_type: Track_type, name: str, render_index: int, mute: bool):
        self.track_type = track_type
        self.name = name
        self.track_id = uuid.uuid4().hex
        self.render_index = render_index

        self.mute = mute
        self.segments = []

    @property
    def end_time(self) -> int:
        """轨道结束时间, 微秒"""
        if len(self.segments) == 0:
            return 0
        return self.segments[-1].target_timerange.end

    @property
    def accept_segment_type(self) -> Type[Seg_type]:
        """返回该轨道允许的片段类型"""
        return self.track_type.value.segment_type  # type: ignore

    def add_segment(self, segment: Seg_type) -> "Track[Seg_type]":
        """向轨道中添加一个片段, 添加的片段必须匹配轨道类型且不与现有片段重叠

        Args:
            segment (Seg_type): 要添加的片段

        Raises:
            `TypeError`: 新片段类型与轨道类型不匹配
            `SegmentOverlap`: 新片段与现有片段重叠
        """
        if not isinstance(segment, self.accept_segment_type):
            raise TypeError("New segment (%s) is not of the same type as the track (%s)" % (type(segment), self.accept_segment_type))

        # 检查片段是否重叠
        for seg in self.segments:
            if seg.overlaps(segment):
                raise SegmentOverlap("New segment overlaps with existing segment [start: {}, end: {}]"
                                     .format(segment.target_timerange.start, segment.target_timerange.end))

        self.segments.append(segment)
        return self

    def export_json(self) -> Dict[str, Any]:
        # 为每个片段写入render_index
        segment_exports = [seg.export_json() for seg in self.segments]
        for seg in segment_exports:
            seg["render_index"] = self.render_index

        return {
            "attribute": int(self.mute),
            "flag": 0,
            "id": self.track_id,
            "is_default_name": len(self.name) == 0,
            "name": self.name,
            "segments": segment_exports,
            "type": self.track_type.name
        }
