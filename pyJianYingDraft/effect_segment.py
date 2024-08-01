"""定义特效/滤镜片段类"""

import uuid

from typing import Union, Optional
from typing import Dict, Any

from .time_util import Timerange
from .segment import Base_segment

from .metadata import Effect_meta
from .metadata import Video_scene_effect_type, Video_character_effect_type, Filter_type

class Filter_segment(Base_segment):
    """放置在独立滤镜轨道上的滤镜片段"""

    effect_meta: Effect_meta
    """滤镜的元数据"""
    intensity: float
    """滤镜强度(滤镜的唯一参数)"""

    def __init__(self, meta: Filter_type, target_timerange: Timerange, intensity: Optional[float] = None):
        super().__init__(uuid.uuid4().hex, target_timerange)
        self.effect_meta = meta.value

        if intensity is not None:
            if len(self.effect_meta.params) == 0:
                raise ValueError("Intensity cannot be set for this filter")
            self.intensity = intensity
        else:
            self.intensity = 1.0

    def export_material(self) -> Dict[str, Any]:
        """导出此特效/滤镜片段所需的素材, 以此不再单独定义Effect_material类"""
        return {
            "adjust_params": [],
            "algorithm_artifact_path": "",
            "apply_target_type": 0,
            "bloom_params": None,
            "category_id": "", # 一律设为空
            "category_name": "", # 一律设为空
            "color_match_info": {
                "source_feature_path": "",
                "target_feature_path": "",
                "target_image_path": ""
            },
            "effect_id": self.effect_meta.effect_id,
            "enable_skin_tone_correction": False,
            "exclusion_group": [],
            "face_adjust_params": [],
            "formula_id": "",
            "id": self.material_id,
            "intensity_key": "",
            "multi_language_current": "",
            "name": self.effect_meta.name,
            "panel_id": "",
            "platform": "all",
            "resource_id": self.effect_meta.resource_id,
            "source_platform": 1,
            "sub_type": "none",
            "time_range": None,
            "type": "filter",
            "value": self.intensity,
            "version": ""
            # 不导出path和request_id
        }

    def export_json(self) -> Dict[str, Any]:
        ret = super().export_json()
        ret["render_index"] = 10000
        return ret
