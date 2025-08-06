"""记录各种特效/音效/滤镜等的元数据

音频相关元数据更新时间：2024
其余元数据更新时间：2025-08
"""

from .effect_meta import EffectMeta, EffectParamInstance
from .effect_meta import AnimationMeta

# 视频特效
from .video_scene_effect import VideoSceneEffectType
from .video_character_effect import VideoCharacterEffectType

# 视频动画
from .video_intro import IntroType
from .video_outro import OutroType
from .video_group_animation import GroupAnimationType

# 音频特效
from .audio_scene_effect import AudioSceneEffectType
from .tone_effect import ToneEffectType
from .speech_to_song import SpeechToSongType

# 文本动画
from .text_intro import TextIntro
from .text_outro import TextOutro
from .text_loop import TextLoopAnim

# 其它
from .font_meta import FontType
from .mask_meta import MaskType, MaskMeta
from .filter_meta import FilterType
from .transition_meta import TransitionType

__all__ = [
    "AnimationMeta",
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
