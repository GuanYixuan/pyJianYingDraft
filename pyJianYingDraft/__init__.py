import sys

from .audio_segment import AudioSegment
from .draft_folder import DraftFolder
from .effect_segment import EffectSegment, FilterSegment
from .keyframe import KeyframeProperty
from .local_materials import AudioMaterial, CropSettings, VideoMaterial
from .metadata import AudioSceneEffectType
from .metadata import ToneEffectType
from .metadata import SpeechToSongType
from .metadata import FilterType, FontType, GroupAnimationType, IntroType, MaskType, MixModeType, OutroType
from .metadata import TextIntro, TextLoopAnim, TextOutro, TransitionType
from .metadata import VideoCharacterEffectType, VideoSceneEffectType
from .script_file import ScriptFile
from .template_mode import ExtendMode, ShrinkMode
from .text_segment import TextBackground, TextBorder, TextSegment, TextShadow, TextStyle
from .time_util import SEC, Timerange, tim, trange, trange_seconds
from .track import TrackRef, TrackSpec, TrackType
from .video_segment import ClipSettings, StickerSegment, VideoSegment

ISWIN = sys.platform == "win32"
if ISWIN:
    from .jianying_controller import ExportFramerate, ExportResolution, JianyingController


__all__ = [
    "FontType",
    "MaskType",
    "FilterType",
    "TransitionType",
    "MixModeType",
    "IntroType",
    "OutroType",
    "GroupAnimationType",
    "TextIntro",
    "TextOutro",
    "TextLoopAnim",
    "AudioSceneEffectType",
    "ToneEffectType",
    "SpeechToSongType",
    "VideoSceneEffectType",
    "VideoCharacterEffectType",
    "CropSettings",
    "VideoMaterial",
    "AudioMaterial",
    "KeyframeProperty",
    "Timerange",
    "AudioSegment",
    "VideoSegment",
    "StickerSegment",
    "ClipSettings",
    "EffectSegment",
    "FilterSegment",
    "TextSegment",
    "TextStyle",
    "TextBorder",
    "TextBackground",
    "TextShadow",
    "TrackType",
    "TrackRef",
    "TrackSpec",
    "ShrinkMode",
    "ExtendMode",
    "ScriptFile",
    "DraftFolder",
    "SEC",
    "tim",
    "trange",
    "trange_seconds",
]

if ISWIN:
    __all__.extend([
        "JianyingController",
        "ExportResolution",
        "ExportFramerate",
    ])
