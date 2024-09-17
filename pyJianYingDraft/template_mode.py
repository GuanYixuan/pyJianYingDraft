"""与模板模式相关的类及函数等"""

from copy import deepcopy

from . import util
from .track import Base_track, Track_type
from .time_util import Timerange

from typing import List, Dict, Any

class Imported_segment:
    """导入的视频/音频片段"""

    raw_data: Dict[str, Any]
    """原始数据"""

    name: str
    """片段名称"""
    material_id: str
    """使用的素材id"""
    source_timerange: Timerange
    """片段取用的素材时间范围"""
    target_timerange: Timerange
    """片段在轨道上的时间范围"""

    __DATA_ATTRS = ["name", "material_id", "source_timerange", "target_timerange"]
    def __init__(self, json_data: Dict[str, Any]):
        self.raw_data = deepcopy(json_data)

        util.assign_attr_with_json(self, self.__DATA_ATTRS, json_data)

    def export_json(self) -> Dict[str, Any]:
        json_data = deepcopy(self.raw_data)
        json_data.update(util.export_attr_to_json(self, self.__DATA_ATTRS))
        return json_data

class Static_track(Base_track):
    """模板模式下导入的不可修改的轨道"""

    raw_data: Dict[str, Any]
    """原始轨道数据"""

    def __init__(self, json_data: Dict[str, Any]):
        self.track_type = Track_type.from_name(json_data["type"])
        self.name = json_data["name"]
        self.track_id = json_data["id"]
        self.render_index = max([int(seg["render_index"]) for seg in json_data["segments"]])

        self.raw_data = deepcopy(json_data)

    def export_json(self) -> Dict[str, Any]:
        return self.raw_data

class Imported_track(Base_track):
    """模板模式下导入且可修改的轨道"""

    raw_data: Dict[str, Any]
    """原始轨道数据"""
    segments: List[Imported_segment]
    """该轨道包含的片段列表"""

    def __init__(self, json_data: Dict[str, Any]):
        self.track_type = Track_type.from_name(json_data["type"])
        self.name = json_data["name"]
        self.track_id = json_data["id"]
        self.render_index = max([int(seg["render_index"]) for seg in json_data["segments"]])

        self.raw_data = deepcopy(json_data)
        self.segments = [Imported_segment(seg) for seg in json_data["segments"]]

    def __len__(self):
        return len(self.segments)

    def export_json(self) -> Dict[str, Any]:
        self.raw_data.update({"segments": [seg.export_json() for seg in self.segments]})
        return self.raw_data
