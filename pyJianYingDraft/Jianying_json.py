import os
import json, uuid

from typing import Optional, Union, overload
from typing import Dict, List, Any

from .local_materials import Video_material, Audio_material
from .audio_segment import Audio_segment, Audio_fade, Audio_effect
from .video_segment import Video_segment, Segment_animations, Video_effect, Transition
from .track import Track_type, Track

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

    transitions: List[Transition]
    """转场效果列表"""

    def __init__(self):
        self.audios = []
        self.videos = []
        self.audio_effects = []
        self.audio_fades = []
        self.animations = []
        self.video_effects = []
        self.transitions = []

    @overload
    def __contains__(self, item: Union[Video_material, Audio_material]) -> bool:...
    @overload
    def __contains__(self, item: Union[Audio_fade, Audio_effect]) -> bool:...
    @overload
    def __contains__(self, item: Union[Segment_animations, Video_effect, Transition]) -> bool:...

    def __contains__(self, item) -> bool:
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
        elif isinstance(item, Transition):
            return item.global_id in [transition.global_id for transition in self.transitions]
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
            "transitions": [transition.export_json() for transition in self.transitions],
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
    tracks: Dict[str, Track]
    """轨道信息"""

    TEMPLATE_FILE = "draft_content_template.json"

    def __init__(self, width: int, height: int, fps: int = 30):
        self.width = width
        self.height = height
        self.fps = fps
        self.duration = 0

        self.materials = Script_material()
        self.tracks = {}

        with open(os.path.join(os.path.dirname(__file__), self.TEMPLATE_FILE), "r", encoding="utf-8") as f:
            self.content = json.load(f)

    def add_material(self, material: Union[Video_material, Audio_material]) -> "Script_file":
        """向脚本文件中添加一个素材"""
        if isinstance(material, Video_material):
            self.materials.videos.append(material)
        elif isinstance(material, Audio_material):
            self.materials.audios.append(material)
        else:
            raise TypeError("Invalid argument type '%s'" % type(material))
        return self

    def add_track(self, track_type: Track_type, track_name: Optional[str] = None) -> "Script_file":
        """向脚本文件中添加一个指定类型、指定名称的轨道

        注意: 轨道的创建顺序决定了其在轨道列表中的位置, 越晚创建的轨道越接近前景

        为避免混淆, 仅在创建第一个同类型轨道时允许不指定名称

        Args:
            track_type (Track_type): 轨道类型
            track_name (str, optional): 轨道名称. 仅在创建第一个同类型轨道时允许不指定.

        Raises:
            `NameError`: 已存在同类型轨道且未指定名称, 或已存在同名轨道
        """

        if track_name is None:
            if track_type in [track.track_type for track in self.tracks.values()]:
                raise NameError("Track of type '%s' already exists, please specify a name" % track_type)
            track_name = track_type.name
        if track_name in [track.name for track in self.tracks.values()]:
            raise NameError("Track with name '%s' already exists" % track_name)

        self.tracks[track_name] = Track(track_type, track_name)
        return self

    def add_segment(self, segment: Union[Video_segment, Audio_segment], track_name: Optional[str] = None) -> "Script_file":
        """向指定轨道中添加一个片段

        Args:
            segment (Union[Video_segment, Audio_segment]): 要添加的片段
            track_name (str, optional): 添加到的轨道名称. 当此类型的轨道仅有一条时可省略.

        Raises:
            `NameError`: 未找到指定名称的轨道, 或必须提供`track_name`参数时未提供
            `TypeError`: 片段类型不匹配轨道类型
            `ValueError`: 新片段与已有片段重叠
        """
        target: Track
        if track_name is not None: # 指定轨道名称
            if track_name not in self.tracks: raise NameError("Track with name '%s' not found" % track_name)
            target = self.tracks[track_name]
        else: # 寻找唯一的同类型的轨道
            count = sum([1 for track in self.tracks.values() if isinstance(segment, track.track_type.value)])
            if count == 0: raise NameError("No track of type '%s' found" % type(segment))
            if count > 1: raise NameError("Multiple tracks of type '%s' found, please specify a track name" % type(segment))

            target = next(track for track in self.tracks.values() if isinstance(segment, track.track_type.value))

        # 加入轨道并更新时长
        target.add_segment(segment)
        self.duration = max(self.duration, segment.target_timerange.start + segment.target_timerange.duration)

        # 自动添加相关素材
        if isinstance(segment, Video_segment):
            # 出入场动画
            if (segment.animations_instance is not None) and (segment.animations_instance not in self.materials):
                self.materials.animations.append(segment.animations_instance)
            # 特效
            for effect in segment.effects:
                if effect not in self.materials:
                    self.materials.video_effects.append(effect)
            # 转场
            if (segment.transition is not None) and (segment.transition not in self.materials):
                self.materials.transitions.append(segment.transition)
        elif isinstance(segment, Audio_segment):
            if (segment.fade is not None) and (segment.fade not in self.materials):
                self.materials.audio_fades.append(segment.fade)
            for effect in segment.effects:
                if effect not in self.materials:
                    self.materials.audio_effects.append(effect)

        return self

    def dumps(self) -> str:
        self.content["fps"] = self.fps
        self.content["duration"] = self.duration
        self.content["canvas_config"] = {"width": self.width, "height": self.height, "ratio": "original"}
        self.content["materials"] = self.materials.export_json()
        self.content["tracks"] = [track.export_json() for track in self.tracks.values()]
        return json.dumps(self.content, ensure_ascii=False, indent=4)
