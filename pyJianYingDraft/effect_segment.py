"""定义特效/滤镜片段类"""

from typing import Union, Optional, List

from .time_util import Timerange
from .segment import BaseSegment
from .video_segment import VideoEffect, Filter

from .metadata import VideoSceneEffectType, VideoCharacterEffectType, FilterType

class EffectSegment(BaseSegment):
    """放置在独立特效轨道上的特效片段"""

    effect_inst: VideoEffect
    """相应的特效素材

    在放入轨道时自动添加到素材列表中
    """

    def __init__(self, effect_type: Union[VideoSceneEffectType, VideoCharacterEffectType],
                 target_timerange: Timerange, params: Optional[List[Optional[float]]] = None):
        self.effect_inst = VideoEffect(effect_type, params, apply_target_type=2)  # 作用域为全局
        super().__init__(self.effect_inst.global_id, target_timerange)

class FilterSegment(BaseSegment):
    """放置在独立滤镜轨道上的滤镜片段"""

    material: Filter
    """相应的滤镜素材

    在放入轨道时自动添加到素材列表中
    """

    def __init__(self, meta: FilterType, target_timerange: Timerange, intensity: float):
        self.material = Filter(meta.value, intensity)
        super().__init__(self.material.global_id, target_timerange)
