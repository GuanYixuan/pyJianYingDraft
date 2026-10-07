from __future__ import annotations

from typing import Any, Dict, List, Union, overload

from .audio_segment import AudioEffect, AudioFade
from .local_materials import AudioMaterial, VideoMaterial
from .segment import Speed
from .text_segment import TextBubble
from .video_segment import BackgroundFilling, Chroma, Filter, MixMode, SegmentAnimations, Transition, VideoEffect


class ScriptMaterial:
    """草稿文件中的素材信息部分"""

    audios: List[AudioMaterial]
    """音频素材列表"""
    videos: List[VideoMaterial]
    """视频素材列表"""
    stickers: List[Dict[str, Any]]
    """贴纸素材列表"""
    texts: List[Dict[str, Any]]
    """文本素材列表"""

    audio_effects: List[AudioEffect]
    """音频特效列表"""
    audio_fades: List[AudioFade]
    """音频淡入淡出效果列表"""
    animations: List[SegmentAnimations]
    """动画素材列表"""
    video_effects: List[VideoEffect]
    """视频特效列表"""
    chromas: List[Chroma]
    """色度抠图列表"""

    speeds: List[Speed]
    """变速列表"""
    masks: List[Dict[str, Any]]
    """蒙版列表"""
    common_mask: List[Dict[str, Any]]
    """新版剪映的蒙版列表, 导出到`common_mask`中; 旧版剪映读取`masks`, 新版读取`common_mask`"""
    transitions: List[Transition]
    """转场效果列表"""
    filters: List[Union[Filter, TextBubble]]
    """滤镜/文本花字/文本气泡列表, 导出到`effects`中"""
    mix_modes: List[MixMode]
    """混合模式列表, 导出到`effects`中"""
    canvases: List[BackgroundFilling]
    """背景填充列表"""

    def __init__(self):
        self.audios = []
        self.videos = []
        self.stickers = []
        self.texts = []

        self.audio_effects = []
        self.audio_fades = []
        self.animations = []
        self.video_effects = []
        self.chromas = []

        self.speeds = []
        self.masks = []
        self.common_mask = []
        self.transitions = []
        self.filters = []
        self.mix_modes = []
        self.canvases = []

    @overload
    def __contains__(self, item: Union[VideoMaterial, AudioMaterial]) -> bool: ...

    @overload
    def __contains__(self, item: Union[AudioFade, AudioEffect]) -> bool: ...

    @overload
    def __contains__(self, item: Union[SegmentAnimations, VideoEffect, Chroma, Transition, Filter, MixMode]) -> bool: ...

    def __contains__(self, item) -> bool:
        if isinstance(item, VideoMaterial):
            return item.material_id in [video.material_id for video in self.videos]
        if isinstance(item, AudioMaterial):
            return item.material_id in [audio.material_id for audio in self.audios]
        if isinstance(item, AudioFade):
            return item.fade_id in [fade.fade_id for fade in self.audio_fades]
        if isinstance(item, AudioEffect):
            return item.effect_id in [effect.effect_id for effect in self.audio_effects]
        if isinstance(item, SegmentAnimations):
            return item.animation_id in [ani.animation_id for ani in self.animations]
        if isinstance(item, VideoEffect):
            return item.global_id in [effect.global_id for effect in self.video_effects]
        if isinstance(item, Chroma):
            return item.global_id in [chroma.global_id for chroma in self.chromas]
        if isinstance(item, Transition):
            return item.global_id in [transition.global_id for transition in self.transitions]
        if isinstance(item, Filter):
            return item.global_id in [filter_.global_id for filter_ in self.filters]
        if isinstance(item, MixMode):
            return item.global_id in [mix_mode.global_id for mix_mode in self.mix_modes]
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
            "canvases": [canvas.export_json() for canvas in self.canvases],
            "chromas": [chroma.export_json() for chroma in self.chromas],
            "common_mask": self.common_mask,
            "color_curves": [],
            "digital_humans": [],
            "drafts": [],
            "effects": [_filter.export_json() for _filter in self.filters] +
                       [mix_mode.export_json() for mix_mode in self.mix_modes],
            "flowers": [],
            "green_screens": [],
            "handwrites": [],
            "hsl": [],
            "images": [],
            "log_color_wheels": [],
            "loudnesses": [],
            "manual_deformations": [],
            "masks": self.masks,
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
            "speeds": [spd.export_json() for spd in self.speeds],
            "stickers": self.stickers,
            "tail_leaders": [],
            "text_templates": [],
            "texts": self.texts,
            "time_marks": [],
            "transitions": [transition.export_json() for transition in self.transitions],
            "video_effects": [effect.export_json() for effect in self.video_effects],
            "video_trackings": [],
            "videos": [video.export_json() for video in self.videos],
            "vocal_beautifys": [],
            "vocal_separations": [],
        }
