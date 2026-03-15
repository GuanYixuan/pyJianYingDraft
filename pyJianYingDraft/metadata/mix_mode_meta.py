"""混合模式元数据"""

from .effect_meta import EffectEnum, EffectMeta

class MixModeType(EffectEnum):
    """混合模式类型"""

    正片叠底 = EffectMeta("正片叠底", False, "6758325895519277582", "871333", "8001e07eefc5d8b69572b977ca14bef9", [])
    颜色减淡 = EffectMeta("颜色减淡", False, "6758325800031752712", "871334", "f979dd10def50fad3ffb77c7f0df3db7", [])
    颜色加深 = EffectMeta("颜色加深", False, "6758325724848853518", "871335", "b76087cda4833f553cf09e82fb81c463", [])
    线性加深 = EffectMeta("线性加深", False, "6758325619253056013", "871336", "655f3590dd07ece41209fb312348ffe9", [])
    柔光 = EffectMeta("柔光", False, "6758325439212556814", "871337", "042aa15b71b1e17bca0bd928eec6fba7", [])
    强光 = EffectMeta("强光", False, "6758325264670790152", "871338", "840ca85a1a33e6fc3ea78bbdb2db8f60", [])
    滤色 = EffectMeta("滤色", False, "6758325170760323597", "871339", "d9c1d4ca7ab91df4f48d12b339f2da88", [])
    叠加 = EffectMeta("叠加", False, "6758324989931295240", "871340", "e6a48579910dfe831ba53a6acc6737f9", [])
    变亮 = EffectMeta("变亮", False, "6758324919789949453", "871341", "b0e90c43dc266a317b05b0cd3ca5bfba", [])
    变暗 = EffectMeta("变暗", False, "6758324839670354445", "871342", "420c92a2b480dc8e402d9269a5f83515", [])
