from .effect_meta import EffectEnum
from .effect_meta import EffectMeta

class SpeechToSongType(EffectEnum):
    """剪映自带的音频“声音成曲”效果类型, 此类效果目前不能自动被剪映所识别"""

    Lofi        = EffectMeta("Lofi", False, "7252917861948068410", "17345060", "8dd8889045e6c065177df791ddb3dfb8", [])
    民谣        = EffectMeta("民谣", False, "7251868698170888759", "17046923", "8dd8889045e6c065177df791ddb3dfb8", [])
    嘻哈        = EffectMeta("嘻哈", True, "7252918249036190245", "17344948", "8dd8889045e6c065177df791ddb3dfb8", [])
    爵士        = EffectMeta("爵士", True, "7264413578860433978", "20120940", "8dd8889045e6c065177df791ddb3dfb8", [])
    节奏蓝调    = EffectMeta("节奏蓝调", True, "7252918101958726200", "17345046", "8dd8889045e6c065177df791ddb3dfb8", [])
    雷鬼        = EffectMeta("雷鬼", True, "7264413386962637368", "20120864", "8dd8889045e6c065177df791ddb3dfb8", [])
