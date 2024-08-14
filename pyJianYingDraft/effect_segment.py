"""定义特效/滤镜片段类"""

import uuid

from typing import Union, Optional
from typing import List, Dict, Any

from .time_util import Timerange
from .segment import Base_segment
from .video_segment import Video_effect, Filter

from .metadata import Effect_meta
from .metadata import Video_scene_effect_type, Video_character_effect_type, Filter_type

class Effect_segment(Base_segment):
    """放置在独立特效轨道上的特效片段"""

    effect_inst: Video_effect
    """相应的特效素材

    在放入轨道时自动添加到素材列表中
    """

    def __init__(self, effect_type: Union[Video_scene_effect_type, Video_character_effect_type],
                 target_timerange: Timerange, params: Optional[List[Optional[float]]] = None):
        self.effect_inst = Video_effect(effect_type, params, apply_target_type=2) # 作用域为全局
        super().__init__(self.effect_inst.global_id, target_timerange)

    def export_json(self) -> Dict[str, Any]:
        ret = super().export_json()
        ret["render_index"] = 11000
        return ret

class Filter_segment(Base_segment):
    """放置在独立滤镜轨道上的滤镜片段"""

    material: Filter
    """相应的滤镜素材

    在放入轨道时自动添加到素材列表中
    """

    def __init__(self, meta: Filter_type, target_timerange: Timerange, intensity: Optional[float] = None):
        if intensity is None: intensity = 1.0

        self.material = Filter(meta.value, intensity)
        super().__init__(self.material.global_id, target_timerange)

    def export_json(self) -> Dict[str, Any]:
        ret = super().export_json()
        ret["render_index"] = 10000
        return ret
