import warnings
import sys

from .local_materials import CropSettings, VideoMaterial, AudioMaterial
from .keyframe import KeyframeProperty

from .time_util import Timerange
from .audio_segment import AudioSegment
from .video_segment import VideoSegment, StickerSegment, ClipSettings
from .effect_segment import EffectSegment, FilterSegment
from .text_segment import TextSegment, TextStyle, TextBorder, TextBackground, TextShadow

from .metadata import FontType
from .metadata import MaskType
from .metadata import TransitionType, FilterType
from .metadata import IntroType, OutroType, GroupAnimationType
from .metadata import TextIntro, TextOutro, TextLoopAnim
from .metadata import AudioSceneEffectType
from .metadata import VideoSceneEffectType, VideoCharacterEffectType

from .track import TrackType
from .template_mode import ShrinkMode, ExtendMode
from .script_file import ScriptFile
from .draft_folder import DraftFolder

# 仅在Windows系统下导入jianying_controller
ISWIN = (sys.platform == 'win32')
if ISWIN:
    from .jianying_controller import JianyingController, ExportResolution, ExportFramerate

from .time_util import SEC, tim, trange


def _deprecated_class_warning(old_name: str, new_name: str):
    warnings.warn(
        f"{old_name} is deprecated and will be removed in a future version. "
        f"Use {new_name} instead.",
        DeprecationWarning,
        stacklevel=3
    )

# 保持向后兼容
class Script_file:
    """Deprecated: Use ScriptFile instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Script_file", "ScriptFile")
        return ScriptFile(*args, **kwargs)

class Draft_folder:
    """Deprecated: Use DraftFolder instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Draft_folder", "DraftFolder")
        return DraftFolder(*args, **kwargs)

class Shrink_mode:
    """Deprecated: Use ShrinkMode instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Shrink_mode", "ShrinkMode")
        return ShrinkMode(*args, **kwargs)

class Extend_mode:
    """Deprecated: Use ExtendMode instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Extend_mode", "ExtendMode")
        return ExtendMode(*args, **kwargs)

class Clip_settings:
    """Deprecated: Use ClipSettings instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Clip_settings", "ClipSettings")
        return ClipSettings(*args, **kwargs)

class Text_style:
    """Deprecated: Use TextStyle instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Text_style", "TextStyle")
        return TextStyle(*args, **kwargs)

class Text_border:
    """Deprecated: Use TextBorder instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Text_border", "TextBorder")
        return TextBorder(*args, **kwargs)

class Text_background:
    """Deprecated: Use TextBackground instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Text_background", "TextBackground")
        return TextBackground(*args, **kwargs)

class Text_segment:
    """Deprecated: Use TextSegment instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Text_segment", "TextSegment")
        return TextSegment(*args, **kwargs)

class Audio_segment:
    """Deprecated: Use AudioSegment instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Audio_segment", "AudioSegment")
        return AudioSegment(*args, **kwargs)

class Video_segment:
    """Deprecated: Use VideoSegment instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Video_segment", "VideoSegment")
        return VideoSegment(*args, **kwargs)

class Sticker_segment:
    """Deprecated: Use StickerSegment instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Sticker_segment", "StickerSegment")
        return StickerSegment(*args, **kwargs)

class Effect_segment:
    """Deprecated: Use EffectSegment instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Effect_segment", "EffectSegment")
        return EffectSegment(*args, **kwargs)

class Filter_segment:
    """Deprecated: Use FilterSegment instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Filter_segment", "FilterSegment")
        return FilterSegment(*args, **kwargs)

class Video_material:
    """Deprecated: Use VideoMaterial instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Video_material", "VideoMaterial")
        return VideoMaterial(*args, **kwargs)

class Audio_material:
    """Deprecated: Use AudioMaterial instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Audio_material", "AudioMaterial")
        return AudioMaterial(*args, **kwargs)

class Crop_settings:
    """Deprecated: Use CropSettings instead."""
    def __new__(cls, *args, **kwargs):
        _deprecated_class_warning("Crop_settings", "CropSettings")
        return CropSettings(*args, **kwargs)

# 枚举类的向后兼容 - 使用代理类
class _DeprecatedEnum:
    """带deprecation警告的枚举代理类"""
    def __init__(self, original_enum, old_name, new_name):
        self._enum = original_enum
        self._old_name = old_name
        self._new_name = new_name

    def __getattr__(self, name):
        # 当访问枚举成员时显示警告
        _deprecated_class_warning(self._old_name, self._new_name)
        return getattr(self._enum, name)

    def __getitem__(self, name):
        # 当通过索引访问时显示警告
        _deprecated_class_warning(self._old_name, self._new_name)
        return self._enum[name]

    def __repr__(self):
        return f"<Deprecated {self._old_name} (use {self._new_name} instead)>"

Track_type = _DeprecatedEnum(TrackType, "Track_type", "TrackType")
Font_type = _DeprecatedEnum(FontType, "Font_type", "FontType")
Mask_type = _DeprecatedEnum(MaskType, "Mask_type", "MaskType")
Filter_type = _DeprecatedEnum(FilterType, "Filter_type", "FilterType")
Transition_type = _DeprecatedEnum(TransitionType, "Transition_type", "TransitionType")
Intro_type = _DeprecatedEnum(IntroType, "Intro_type", "IntroType")
Outro_type = _DeprecatedEnum(OutroType, "Outro_type", "OutroType")
Group_animation_type = _DeprecatedEnum(GroupAnimationType, "Group_animation_type", "GroupAnimationType")
Text_intro = _DeprecatedEnum(TextIntro, "Text_intro", "TextIntro")
Text_outro = _DeprecatedEnum(TextOutro, "Text_outro", "TextOutro")
Text_loop_anim = _DeprecatedEnum(TextLoopAnim, "Text_loop_anim", "TextLoopAnim")
Audio_scene_effect_type = _DeprecatedEnum(AudioSceneEffectType, "Audio_scene_effect_type", "AudioSceneEffectType")
Video_scene_effect_type = _DeprecatedEnum(VideoSceneEffectType, "Video_scene_effect_type", "VideoSceneEffectType")
Video_character_effect_type = _DeprecatedEnum(VideoCharacterEffectType, "Video_character_effect_type", "VideoCharacterEffectType")
Keyframe_property = _DeprecatedEnum(KeyframeProperty, "Keyframe_property", "KeyframeProperty")

# 仅在Windows系统下定义jianying_controller相关的向后兼容类
if ISWIN:
    class Jianying_controller:
        """Deprecated: Use JianyingController instead."""
        def __new__(cls, *args, **kwargs):
            _deprecated_class_warning("Jianying_controller", "JianyingController")
            return JianyingController(*args, **kwargs)

    Export_resolution = _DeprecatedEnum(ExportResolution, "Export_resolution", "ExportResolution")
    Export_framerate = _DeprecatedEnum(ExportFramerate, "Export_framerate", "ExportFramerate")

# 基础__all__列表（所有平台通用）
__all__ = [
    "FontType",
    "MaskType",
    "FilterType",
    "TransitionType",
    "IntroType",
    "OutroType",
    "GroupAnimationType",
    "TextIntro",
    "TextOutro",
    "TextLoopAnim",
    "AudioSceneEffectType",
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
    "ShrinkMode",
    "ExtendMode",
    "ScriptFile",
    "DraftFolder",
    "SEC",
    "tim",
    "trange",

    # 向后兼容的snake_case类
    "Script_file",
    "Draft_folder",
    "Shrink_mode",
    "Extend_mode",
    "Track_type",
    "Font_type",
    "Mask_type",
    "Filter_type",
    "Transition_type",
    "Intro_type",
    "Outro_type",
    "Group_animation_type",
    "Text_intro",
    "Text_outro",
    "Text_loop_anim",
    "Audio_scene_effect_type",
    "Video_scene_effect_type",
    "Video_character_effect_type",
    "Clip_settings",
    "Text_style",
    "Text_border",
    "Text_background",
    "Text_segment",
    "Audio_segment",
    "Video_segment",
    "Sticker_segment",
    "Effect_segment",
    "Filter_segment",
    "Video_material",
    "Audio_material",
    "Crop_settings",
    "Keyframe_property",
]

# 仅在Windows系统下添加jianying_controller相关的导出
if ISWIN:
    __all__.extend([
        "JianyingController",
        "ExportResolution",
        "ExportFramerate",
        "Jianying_controller",
        "Export_resolution",
        "Export_framerate",
    ])
