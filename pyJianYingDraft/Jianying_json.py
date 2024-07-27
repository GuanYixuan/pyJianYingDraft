import os
import json, uuid

from enum import Enum
from typing import Optional, Literal, Union
from typing import Dict, List, Any

from .local_materials import Video_material, Audio_material
from .audio_segment import Audio_segment, Audio_fade, Audio_effect
from .video_segment import Video_segment, Segment_animations, Video_effect

class Script_material:
    """脚本文件中的素材信息部分"""

    audios: List[Audio_material]
    """音频素材列表"""
    videos: List[Video_material]
    """视频素材列表"""

    audio_effects: List[Audio_effect]
    """音频特效列表"""
    audio_fades: List[Audio_fade]
    """音频淡入淡出效果列表"""
    animations: List[Segment_animations]
    """动画素材列表"""
    video_effects: List[Video_effect]
    """视频特效列表"""

    def __init__(self):
        self.audios = []
        self.videos = []
        self.audio_effects = []
        self.audio_fades = []
        self.animations = []
        self.video_effects = []

    def __contains__(self, item: Union[Audio_material, Video_material, Audio_fade, Audio_effect, Segment_animations, Video_effect]) -> bool:
        if isinstance(item, Video_material):
            return item.material_id in [video.material_id for video in self.videos]
        elif isinstance(item, Audio_material):
            return item.material_id in [audio.material_id for audio in self.audios]
        elif isinstance(item, Audio_fade):
            return item.fade_id in [fade.fade_id for fade in self.audio_fades]
        elif isinstance(item, Audio_effect):
            return item.effect_id in [effect.effect_id for effect in self.audio_effects]
        elif isinstance(item, Segment_animations):
            return item.animation_id in [ani.animation_id for ani in self.animations]
        elif isinstance(item, Video_effect):
            return item.global_id in [effect.global_id for effect in self.video_effects]
        else:
            raise TypeError("Invalid argument type '%s'" % type(item))

    def export_json(self) -> Dict[str, List[Any]]:
        return {
            "ai_translates": [],
            "audio_balances": [],
            "audio_effects": [effect.export_json() for effect in self.audio_effects],
            "audio_fades": [fade.export_json() for fade in self.audio_fades],
            "audio_track_indexes": [],
            "audios": [audio.export_json() for audio in self.audios],
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
            "video_effects": [effect.export_json() for effect in self.video_effects],
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
    """视频的总时长, 单位为微秒"""

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

    def add_material(self, material: Union[Video_material, Audio_material]) -> "Script_file":
        if isinstance(material, Video_material):
            self.materials.videos.append(material)
        elif isinstance(material, Audio_material):
            self.materials.audios.append(material)
        else:
            raise TypeError("Invalid argument type '%s'" % type(material))
        return self

    def add_segment(self, segment: Union[Video_segment, Audio_segment]) -> "Script_file":
        if isinstance(segment, Video_segment):
            self.content["tracks"][0]["segments"].append(segment.export_json())
            self.duration = max(self.duration, segment.target_timerange.start + segment.target_timerange.duration)

            if (segment.animations_instance is not None) and (segment.animations_instance not in self.materials):
                self.add_animation(segment.animations_instance)
            for effect in segment.effects:
                if effect not in self.materials:
                    self.materials.video_effects.append(effect)
        elif isinstance(segment, Audio_segment):
            self.content["tracks"][1]["segments"].append(segment.export_json())
            self.duration = max(self.duration, segment.target_timerange.start + segment.target_timerange.duration)

            if (segment.fade is not None) and (segment.fade not in self.materials):
                self.materials.audio_fades.append(segment.fade)
            for effect in segment.effects:
                if effect not in self.materials:
                    self.materials.audio_effects.append(effect)
        else:
            raise TypeError("Invalid argument type '%s'" % type(segment))
        return self

    def add_animation(self, animation: Segment_animations):
        self.materials.animations.append(animation)

    def dumps(self) -> str:
        self.content["fps"] = self.fps
        self.content["duration"] = self.duration
        self.content["canvas_config"] = {"width": self.width, "height": self.height, "ratio": "original"}
        self.content["materials"] = self.materials.export_json()
        return json.dumps(self.content, ensure_ascii=False, indent=4)
