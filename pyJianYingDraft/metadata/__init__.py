"""记录各种特效/音效/滤镜等的元数据"""

from .effect_meta import EffectMeta, EffectParamInstance

from .font_meta import FontType
from .mask_meta import MaskType, MaskMeta
from .filter_meta import FilterType
from .transition_meta import TransitionType
from .animation_meta import IntroType, OutroType, GroupAnimationType
from .animation_meta import TextIntro, TextOutro, TextLoopAnim
from .audio_effect_meta import AudioSceneEffectType, ToneEffectType, SpeechToSongType
from .video_effect_meta import VideoSceneEffectType, VideoCharacterEffectType

__all__ = [
    "EffectMeta",
    "EffectParamInstance",
    "MaskType",
    "MaskMeta",
    "FilterType",
    "FontType",
    "TransitionType",
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
    "VideoCharacterEffectType"
]
