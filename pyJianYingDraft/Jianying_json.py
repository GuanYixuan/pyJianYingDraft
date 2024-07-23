import os
import json, uuid

from enum import Enum
from typing import Optional, Literal, Union
from typing import Dict, List, Any

from .local_materials import Video_material
from .segments import Segment_animations, Video_segment

class Script_material:
    """脚本文件中的素材信息部分"""

    videos: List[Video_material]
    """视频素材列表"""

    animations: List[Segment_animations]
    """动画素材列表"""

    def __init__(self):
        self.videos = []
        self.animations = []

    def __contains__(self, item: Union[Video_material, Segment_animations]) -> bool:
        if isinstance(item, Video_material):
            return item.material_id in [video.material_id for video in self.videos]
        elif isinstance(item, Segment_animations):
            return item.animation_id in [ani.animation_id for ani in self.animations]
        else:
            raise TypeError("Invalid argument type '%s'" % type(item))

    def export_json(self) -> Dict[str, List[Any]]:
        return {
            "ai_translates": [],
            "audio_balances": [],
            "audio_effects": [],
            "audio_fades": [],
            "audio_track_indexes": [],
            "audios": [],
            "beats": [],
            "canvases": [],
            "chromas": [],
            "color_curves": [],
            "digital_humans": [],
            "drafts": [],
            "effects": [],
            "flowers": [],
            "green_screens": [],
            "handwrites": [],
            "hsl": [],
            "images": [],
            "log_color_wheels": [],
            "loudnesses": [],
            "manual_deformations": [],
            "masks": [],
            "material_animations": [ani.export_json() for ani in self.animations],
            "material_colors": [],
            "multi_language_refs": [],
            "placeholders": [],
            "plugin_effects": [],
            "primary_color_wheels": [],
            "realtime_denoises": [],
            "shapes": [],
            "smart_crops": [],
            "smart_relights": [],
            "sound_channel_mappings": [],
            "speeds": [],
            "stickers": [],
            "tail_leaders": [],
            "text_templates": [],
            "texts": [],
            "time_marks": [],
            "transitions": [],
            "video_effects": [],
            "video_trackings": [],
            "videos": [video.export_json() for video in self.videos],
            "vocal_beautifys": [],
            "vocal_separations": []
        }

class Script_file:

    content: Dict[str, Any]
    """脚本文件内容"""

    width: int
    """视频的宽度, 单位为像素"""
    height: int
    """视频的高度, 单位为像素"""
    fps: int
    """视频的帧率"""
    duration: int

    materials: Script_material
    """脚本文件中的素材信息部分"""

    TEMPLATE_FILE = "draft_content_template.json"

    def __init__(self, width: int, height: int, fps: int = 30):
        self.width = width
        self.height = height
        self.fps = fps
        self.duration = 0

        self.materials = Script_material()

        with open(os.path.join(os.path.dirname(__file__), self.TEMPLATE_FILE), "r", encoding="utf-8") as f:
            self.content = json.load(f)

    def add_material(self, material: Video_material):
        self.materials.videos.append(material)

    def add_segment(self, segment: Video_segment):
        self.content["tracks"][0]["segments"].append(segment.export_json())
        self.duration = max(self.duration, segment.target_timerange.start + segment.target_timerange.duration)

        if (segment.animations_instance is not None) and (segment.animations_instance not in self.materials):
            self.add_animation(segment.animations_instance)

    def add_animation(self, animation: Segment_animations):
        self.materials.animations.append(animation)

    def dumps(self) -> str:
        self.content["fps"] = self.fps
        self.content["duration"] = self.duration
        self.content["canvas_config"] = {"width": self.width, "height": self.height, "ratio": "original"}
        self.content["materials"] = self.materials.export_json()
        return json.dumps(self.content, ensure_ascii=False, indent=4)
