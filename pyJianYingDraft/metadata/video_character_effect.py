"""视频人物特效元数据"""

from .effect_meta import EffectEnum
from .effect_meta import EffectMeta, EffectParam

class VideoCharacterEffectType(EffectEnum):
    """视频人物特效枚举"""

    # 免费特效
    BOOM                 = EffectMeta("BOOM！", False, "6999560597230588429", "1378605", "a7d5d3fbae39950e51bff93b92ad7792", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    X                    = EffectMeta("X", False, "7037006820749087246", "1464226", "ec38784544361583ed45aa333ebdf2c9", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    crash                = EffectMeta("crash！", False, "6999887184018805285", "1378609", "47b6f315a86918e23d94d35c69946fe1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    中刀                 = EffectMeta("中刀", False, "7029514054179754510", "1436386", "ad3377fb7ed70663017b8f4dcecc8441", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    主体冲破屏幕         = EffectMeta("主体冲破屏幕", False, "7390265515056304681", "74731169", "f36c6922e91c3036495591591aba39d9", [])
    九尾狐               = EffectMeta("九尾狐", False, "7011416501160776228", "1404740", "12afdb69b18ec5127874f04d6f3fdefd", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    人影爆闪             = EffectMeta("人影爆闪", False, "7260741462269104697", "19799492", "f307677e792d2970045b653267fca93b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认45%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%"""
    光环_I               = EffectMeta("光环 I", False, "6999584193848021535", "1378551", "ce2098aa7d557cfc63d896fc63ec2846", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    光环_II              = EffectMeta("光环 II", False, "6999882629893853726", "1378552", "adb70b2ea060371bb7d91ec43c031989", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    几何拖尾_I           = EffectMeta("几何拖尾 I", False, "6985081270208303653", "1404702", "dbc19689b9dae201897fce9e894ce5fe", [])
    几何拖尾_II          = EffectMeta("几何拖尾 II", False, "7008079206181507615", "1404705", "9c57ea460222d55e1bbab56600ca3b71", [])
    击中                 = EffectMeta("击中", False, "7008009586581967397", "1404729", "b0a79d87265c9f181f9875a626ad7c66", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    分头行动             = EffectMeta("分头行动", False, "7065570293552517646", "1570064", "50b8be675fac5e23d3bc5d96013c027e", [
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认35%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    分身                 = EffectMeta("分身", False, "7194734735434715704", "9010351", "dca7518f6eb90654d1c2473406db2890", [
                              EffectParam("effects_adjust_distortion", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    动感爱心             = EffectMeta("动感爱心", False, "6998039666024780318", "1238121", "9d3838036dedfd21be7f340273fde034", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    卡通脸               = EffectMeta("卡通脸", False, "7205481536240489019", "10092161", "d01b570f71818e6f6d04bc6c9b1ef766", [])
    变身                 = EffectMeta("变身", False, "6998018272557797924", "1238120", "f78c282c0147f997f1c7624bda919cc3", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    可爱女生             = EffectMeta("可爱女生", False, "6971317732948054542", "1182270", "305aaa38fa724b8fceba4a0be1bd49a8", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    可爱猪               = EffectMeta("可爱猪", False, "6971317650219602446", "1182274", "483efc4867b85d9bf7c39a6b1d878b8d", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    吻痕坏笑             = EffectMeta("吻痕坏笑", False, "7197741530751177274", "9392743", "df256252c27055c7434212ca51caf7d0", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    哈哈哈               = EffectMeta("哈哈哈", False, "6993187958685700638", "1217040", "803508bffb42714235dcdbddb1d30834", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    图腾                 = EffectMeta("图腾", False, "6999820560528052743", "1378608", "006d822d0f49a4e20e539d18ed6cda96", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    圣诞小熊             = EffectMeta("圣诞小熊", False, "7175084803874624061", "7126277", "c66c5f67cc2eeb2827a24fd5558cedfe", [
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认35%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    圣诞帽               = EffectMeta("圣诞帽", False, "7034784053609894430", "1457102", "b3bf8d22530db2a310a8c38abed2fd09", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认30%, 0% ~ 100%"""
    圣诞树               = EffectMeta("圣诞树", False, "7173942106061279781", "6993587", "865c067b3fc9fd7d8fb9d32bfe88cea3", [])
    圣诞胡子             = EffectMeta("圣诞胡子", False, "7034831862597947918", "1457484", "35b6dc4b15d10db2100509cf349f5b5c", [
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.770, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认30%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认77%, 0% ~ 100%"""
    圣诞辣妹             = EffectMeta("圣诞辣妹", False, "7165705324777705992", "7406471", "7c9b779e2382630c01d33528a013b8fb", [
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    圣诞铃铛             = EffectMeta("圣诞铃铛", False, "7175084694940160568", "7126337", "5b59cf441d783d507c2b4b3a0aabf4e9", [
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认35%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    声波                 = EffectMeta("声波", False, "7008055446397260319", "1404731", "f0e9e247eabb12c558de273a8e51c515", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    多屏圣诞树           = EffectMeta("多屏圣诞树", False, "7175084576950194725", "7126387", "1a70506d54ba37021e8dd157358aa76a", [
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认35%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    大头                 = EffectMeta("大头", False, "6986556887818834462", "1201644", "7518e7eb3e186350b688bf712b960c97", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    大眼睛               = EffectMeta("大眼睛", False, "7044080818544710152", "1489516", "b53f3fda1f03d0d1f703fb71a009d790", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    天使环               = EffectMeta("天使环", False, "7019228748775952933", "1400400", "5782ef42472fd9771f9113d98b6e4e58", [])
    太阳神               = EffectMeta("太阳神", False, "7009186849444860453", "1404735", "9c009ca6bf736eba0dd3152bb863fc6d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    好吃                 = EffectMeta("好吃", False, "7075218981442818596", "1626122", "6a55240ce1f00f078b50fd5e34b5afd3", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.200),
                              EffectParam("effects_adjust_horizontal_shift", 0.600, 0.300, 2.600),
                              EffectParam("effects_adjust_size", 0.500, 0.300, 2.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 120%
    effects_adjust_horizontal_shift: 默认60%, 30% ~ 260%
    effects_adjust_size: 默认50%, 30% ~ 200%
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    妖气                 = EffectMeta("妖气", False, "6729410038047183364", "1558942", "8ff658c7bcf3814f91693f906d5eba8b", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    委屈丑丑脸           = EffectMeta("委屈丑丑脸", False, "7130874026733343268", "4192363", "596971eaa17dbe64f62f52fc75c9998a", [])
    害羞                 = EffectMeta("害羞", False, "6979931248890221069", "1187976", "6904d753832ee54a39f46fb23e0c47fc", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%"""
    小恶魔               = EffectMeta("小恶魔", False, "6995534946311868958", "1225626", "7dba67f137a50da13db71188fc6df71f", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%"""
    小鹿角               = EffectMeta("小鹿角", False, "7035938555683672612", "1459882", "a77b46457ff3ea5a5c75c0d127e9cdd2", [])
    尴尬住了             = EffectMeta("尴尬住了", False, "7156141357008949790", "5481035", "cc08bdab9e913aa015d61631abf8fa7d", [])
    局部扭曲             = EffectMeta("局部扭曲", False, "7038521452668129822", "1470210", "da8f3f99ca659d2710b2f9dcecf5fe4c", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    局部马赛克           = EffectMeta("局部马赛克", False, "7034092576726585869", "1454112", "6f37c16b7d7904bc8489e66455f6d78b", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    巴哥犬               = EffectMeta("巴哥犬", False, "6971317662567633421", "1182273", "6764c992938b5c0e62dfc6e46255bde7", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    帅气男生             = EffectMeta("帅气男生", False, "6971317748542476814", "1182269", "71d88fb7f6ae9e19df3f8b491b7355bf", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    幻影_I               = EffectMeta("幻影 I", False, "7212904257043829307", "11357751", "6699feabadc4f59732b8087620fc95a6", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    幽灵                 = EffectMeta("幽灵", False, "7000630410275197470", "1378554", "9f6758469c2a948cadfbeff53bbc5b6d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    弥散流光             = EffectMeta("弥散流光", False, "7034508334157795876", "1455764", "eabd69cd578279cf0dc892e088f60da6", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_noise: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认0%, 0% ~ 100%"""
    彩色负片             = EffectMeta("彩色负片", False, "7035876641083494926", "1459050", "2cd6462bd0bde3023d5f7069cd549b17", [
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    彩色重影             = EffectMeta("彩色重影", False, "6995746173772370469", "1235614", "99b7fa2ef6210832f1d6dccfce4ed759", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    微笑摇摆头           = EffectMeta("微笑摇摆头", False, "7166825483902915109", "6253239", "ff4053845ced3ff3b9fbe9d1429a908b", [
                              EffectParam("effects_adjust_size", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认45%, 0% ~ 100%
    effects_adjust_speed: 默认75%, 0% ~ 100%
    effects_adjust_range: 默认35%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    心动                 = EffectMeta("心动", False, "6986186073814602277", "1204190", "bab33144cacb0cdade5a3d1f18d9c6e7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认75%, 0% ~ 100%"""
    心动信号             = EffectMeta("心动信号", False, "7040012457842053662", "1478394", "a4758810ef78bfca76c45486faeac99d", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    心心眼               = EffectMeta("心心眼", False, "7196943722523660858", "9126233", "aebda718fd41b71cbef713df0b12ac0f", [
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认100%, 0% ~ 100%"""
    恶灵骑士             = EffectMeta("恶灵骑士", False, "7000301210993431053", "1378618", "c0f232fc4435c4bf8a4861efa6bcf671", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    恶魔印记             = EffectMeta("恶魔印记", False, "7000647554337608222", "1378619", "abab6563284c7ef292d1acaaf5a1be3e", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    恶魔尾巴             = EffectMeta("恶魔尾巴", False, "7001021232371995149", "1404725", "7ab5f92c75beb4747dc81731b447f53c", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认100%, 0% ~ 100%"""
    恶魔角               = EffectMeta("恶魔角", False, "7019228817549955597", "1400399", "e3331ccd99a663f0561f82ac87441dcf", [])
    惨                   = EffectMeta("惨", False, "6992836065245532680", "1225625", "f5f8238bef302a2a27cae95c0d2304f1", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%"""
    意识流               = EffectMeta("意识流", False, "7000629338529862151", "1378555", "17dcd65459f769802c3d02fa00af0a48", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认60%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    憔悴                 = EffectMeta("憔悴", False, "6986160256103485989", "1197947", "709a178794856095bfcc215cabc3f91c", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认75%, 0% ~ 100%"""
    懵                   = EffectMeta("懵", False, "6980272649066779143", "1187977", "32325e03b4b27a426af4f3c3916cd718", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%"""
    我不听               = EffectMeta("我不听", False, "7001058741571293709", "1353102", "a56ac41521ef7b1e1ad7e09ec2253082", [
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    我服了               = EffectMeta("我服了", False, "7029509874862002724", "1436336", "6ec666bfc6a45aa53f82f794d75d9976", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%"""
    手印涂抹             = EffectMeta("手印涂抹", False, "7153950763348136478", "5190085", "c617ff4e68e61de777f52149851b782c", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    手绘描边             = EffectMeta("手绘描边", False, "7406177019404227109", "80106342", "07d72dd2e34f4fd41cbdabe05464454d", [])
    打击                 = EffectMeta("打击", False, "6971302911317905956", "1169502", "b310c3ede33e6e0819859dbc67ffab7e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.550, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认55%, 0% ~ 100%"""
    打脸                 = EffectMeta("打脸", False, "6992915114051506725", "1217039", "ade99f5a3c5dc73639e55dbf4157b0eb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    扫描_II              = EffectMeta("扫描 II", False, "7000630959565443614", "1378580", "c6c224fb2fec72f0a0432ccad29546aa", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    拼贴抽帧             = EffectMeta("拼贴抽帧", False, "7142777693707178533", "4574525", "602c047f7cafe02427da4b327fd260cf", [
                              EffectParam("effects_adjust_vertical_chromatic", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.661, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_chromatic: 默认0%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认10%, 0% ~ 100%
    effects_adjust_size: 默认30%, 0% ~ 100%
    effects_adjust_texture: 默认66%, 0% ~ 100%
    effects_adjust_filter: 默认65%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    拼贴风暴             = EffectMeta("拼贴风暴", False, "7037019101402763806", "1464400", "1a39707de66987a9048c2e495b5a1c96", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认75%, 0% ~ 100%"""
    拽酷红眼             = EffectMeta("拽酷红眼", False, "6979861988935471623", "1185226", "3528fdf176336d1ae503e85611d96347", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%"""
    掉小珍珠啦           = EffectMeta("掉小珍珠啦", False, "7132336135748981255", "4080159", "91cb59a743f8089684fcf7c420861e74", [])
    故障描边_I           = EffectMeta("故障描边 I", False, "6998080413587477005", "1238132", "226bca50364904c231246c72b0a9e5c1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    敲打                 = EffectMeta("敲打", False, "6986918523704447501", "1197949", "67737d95f8256e6915b26c3efd41f305", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    新年星黛露           = EffectMeta("新年星黛露", False, "7182406780733887033", "7823781", "6e4e73454d92da43cd9e90cf7c350c7d", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    无信号               = EffectMeta("无信号", False, "7039965830192304671", "1478054", "c6c413df67a97d81b29355a0e1e89f16", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    日系大头贴           = EffectMeta("日系大头贴", False, "7309039877796925978", "32668223", "04f1ebf5bf63743f1bb12f518ede4b5e", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认80%, 0% ~ 100%
    effects_adjust_blur: 默认10%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_distortion: 默认70%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%"""
    星光放射             = EffectMeta("星光放射", False, "6999904379822150158", "1378610", "aa85bd31e3f47e7bd01383b6aacc9508", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    星星拖尾             = EffectMeta("星星拖尾", False, "7007679689388986888", "1404703", "7dabcaa49244e8faeaf61bfa184d53fb", [])
    未来眼镜             = EffectMeta("未来眼镜", False, "6989160247034122789", "1238126", "66983702ac8ca5f68aa9ec32c92c4b3b", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    机械几何             = EffectMeta("机械几何", False, "6997682380454498824", "1238116", "2b469e181b8e5be26a0e09678a9974b0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    机械姬_I             = EffectMeta("机械姬 I", False, "6978809529215488548", "1238098", "11d60d8c8de82453c697bed883e64671", [])
    机械姬_II            = EffectMeta("机械姬 II", False, "6997969810822795813", "1238099", "601bc1f8fd6dfcb9226fa7e54aba9f14", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    机灵怪               = EffectMeta("机灵怪", False, "7158373218724614664", "5510681", "6fa4f54d22b420c8c0a3e59246d1c8b7", [])
    欧美女性             = EffectMeta("欧美女性", False, "6971317800098861576", "1182266", "6d9b6990df1d66bad249c5defd435576", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    欧美男性             = EffectMeta("欧美男性", False, "6971317784085008909", "1182267", "b09c7a6c2134a95aeac139f06217cdde", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    气泡_I               = EffectMeta("气泡 I", False, "6999560743653741087", "1378604", "53133594bcb0ca9cf9cb48b80aa8eec1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    气泡_II              = EffectMeta("气泡 II", False, "6999560859986956813", "1378603", "1b75e11acadf9069723dc387751d68c5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    气波                 = EffectMeta("气波", False, "7008459080452805133", "1404693", "d49684beffa531728f6d0b2f5823a465", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    氛围大头贴           = EffectMeta("氛围大头贴", False, "7309480138486321715", "32919263", "13daa7e7f44f245155737d4a8017d0e2", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认80%, 0% ~ 100%
    effects_adjust_blur: 默认10%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_distortion: 默认70%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%"""
    沉沦                 = EffectMeta("沉沦", False, "7000286535568331294", "1378579", "7f1cef9ddfd657188f2ae2f069c9433b", [
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    流光描边             = EffectMeta("流光描边", False, "7156203771352060424", "6699941", "43de1121773eea81624460ed929b17e8", [
                              EffectParam("effects_adjust_intensity", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认85%, 0% ~ 100%
    effects_adjust_size: 默认15%, 0% ~ 100%
    effects_adjust_range: 默认33%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认25%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    流口水               = EffectMeta("流口水", False, "7072912940101276196", "1610044", "50dec319b04a96990ed59c7a237ed700", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.400, 0.700),
                              EffectParam("effects_adjust_size", 0.800, 0.500, 1.200)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 40% ~ 70%
    effects_adjust_size: 默认80%, 50% ~ 120%"""
    漩涡                 = EffectMeta("漩涡", False, "7007639691797205511", "1404726", "c027fc134ee686578a887120774ae49b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    潮流入侵             = EffectMeta("潮流入侵", False, "7039588403897176583", "1475552", "fff9a2112e2f1befcbe793a348d9b49e", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    潮酷女孩             = EffectMeta("潮酷女孩", False, "6973998028587799076", "1182282", "43567fd71493d00bc90873169a742c7b", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    潮酷男孩             = EffectMeta("潮酷男孩", False, "6971317770835202574", "1182268", "8db29277f098685e305a341ae6256482", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    激光几何             = EffectMeta("激光几何", False, "6998130105188880909", "1238146", "3b57818e4d021368a6a71792ff5efffd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    火焰拖尾             = EffectMeta("火焰拖尾", False, "7008060347789611551", "1404704", "f5e51b968426e15e4e185285a4e8558f", [])
    火焰环绕             = EffectMeta("火焰环绕", False, "7009186695157387784", "1404737", "0336f00d05b706cf8ab9742af8ee16c7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    火焰翅膀_I           = EffectMeta("火焰翅膀 I", False, "7009186539762618910", "1404738", "bab3b65e0ca81daf7fbef82971d57527", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    火焰翅膀_II          = EffectMeta("火焰翅膀 II", False, "7007998245511107108", "1404728", "93fa02d91dd5f7fd2c41314358ba462d", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    灵机一动             = EffectMeta("灵机一动", False, "6982806720867209765", "1187978", "9a0be515180211c4c30a1757d3622ca0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.600, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认60%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    灵魂出走             = EffectMeta("灵魂出走", False, "6994263736991093278", "1220234", "b78e2e42d51b354ad3a2c9af04da43f1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%"""
    爱心光波             = EffectMeta("爱心光波", False, "7058944699737838116", "1552114", "2198438e43c9ff1147958bf750b61b90", [
                              EffectParam("effects_adjust_texture", 0.204, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.753, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认20%, 0% ~ 100%
    effects_adjust_size: 默认75%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    爱心焰火             = EffectMeta("爱心焰火", False, "6999550440639566350", "1378601", "2f8b37a399b2b45ca57717a6244c3c9f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    狼人                 = EffectMeta("狼人", False, "7156899280374993416", "5413619", "f3d6cf02114d17bad33a3003557f5ff5", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%"""
    猩猩脸               = EffectMeta("猩猩脸", False, "7112786295771894285", "3186064", "3afa515823ec425b359bf9102a7cfa28", [])
    猫耳女孩             = EffectMeta("猫耳女孩", False, "6971317673699316261", "1182272", "486df1ec5de1ca0a69210b844b912534", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    电光描边             = EffectMeta("电光描边", False, "7171723380003967496", "6738041", "1a5266ab56ea0645c20f0160aee7743e", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认90%, 0% ~ 100%
    effects_adjust_distortion: 默认70%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    电光放射             = EffectMeta("电光放射", False, "7011414375130993188", "1404739", "092db1dc71adf758d4ab5b19b5b43873", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    电击                 = EffectMeta("电击", False, "6999560974638256671", "1378602", "b1659d113dda06df2115cd948ed09e23", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    电子屏故障           = EffectMeta("电子屏故障", False, "6997976386413531661", "1238119", "05d9292d4d2ef2ea3b84854f4771ff25", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    真的会谢             = EffectMeta("真的会谢", False, "7179493200904589881", "7600931", "bdfc580a5e4155e95c3568dcea50d341", [])
    真香                 = EffectMeta("真香", False, "6995535089975169549", "1225627", "81a9d2b55a363059acb95c637e49d65d", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%"""
    破碎的心             = EffectMeta("破碎的心", False, "7008077860397126158", "1404734", "7ddd6f7b9c206935ac79bfc814467ae4", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    神明少女             = EffectMeta("神明少女", False, "6906817277316829703", "1169466", "20a22b74a6a7a30f2dcab48dbc5276b6", [
                              EffectParam("effects_adjust_soft", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_soft: 默认25%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    科技氛围_I           = EffectMeta("科技氛围 I", False, "6989160173826740767", "1238115", "bdfd8e3165875ca7084b62d7e6204079", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    科技氛围_III         = EffectMeta("科技氛围 III", False, "6983927792010269214", "1238118", "8e1024fd3f6bd41f09d16cf27de0f210", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    秘密                 = EffectMeta("秘密", False, "7023684632591733284", "1418782", "72f525012ca8744325138a89981b3e84", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    箭头环绕             = EffectMeta("箭头环绕", False, "6999943971162034702", "1378553", "c4543904bdf336051dee6e64c8b5ebdd", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    粉色便便             = EffectMeta("粉色便便", False, "6971317685216875044", "1182271", "0c843a5ba39df7e037f4995040f79263", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    背景拖影             = EffectMeta("背景拖影", False, "7012512877038801415", "1379270", "e6c9f05435c8a8912b1321bfa9f39a4a", [
                              EffectParam("effects_adjust_horizontal_shift", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.850, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认85%, 0% ~ 100%"""
    背景氛围II           = EffectMeta("背景氛围II", False, "7007713075486790152", "1404727", "f69d913fb2414b485d7d03770049a5fa", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    脸红                 = EffectMeta("脸红", False, "7025808257306333732", "1424210", "9946c014663314c93786a0a8fc27b347", [
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.802, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    脸绿了               = EffectMeta("脸绿了", False, "7023661644853023263", "1418056", "a4af7d2a30dac7d4be34f96c8d27f556", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.802, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%"""
    脸部故障             = EffectMeta("脸部故障", False, "7260774105073324602", "19351944", "b00871e8d7e141731a2fe3ca29bb857a", [
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    舞者                 = EffectMeta("舞者", False, "6978809631678140935", "1238134", "80d431c5d76932b3f3fb8418267afdb5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    舞者_II              = EffectMeta("舞者 II", False, "7000629698401145352", "1378611", "de4d77dc2f920e92503d9553c0cf1a21", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认60%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    萤火                 = EffectMeta("萤火", False, "6979415063106949639", "1378556", "000701418e2acde7230cfdcc680ef895", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    虚拟人生_I           = EffectMeta("虚拟人生 I", False, "6998017546452472351", "1238100", "54fd9f289f28e1a2f060f4e569c31359", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    虚拟人生_II          = EffectMeta("虚拟人生 II", False, "6998017726589440519", "1238101", "2bc7ecc4b79a372c9fed9a86b850d8a5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    衰                   = EffectMeta("衰", False, "6995855600764588557", "1225628", "80bb667cb6e39b17554321df89c41a86", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%"""
    视线遮挡             = EffectMeta("视线遮挡", False, "7034507846305714696", "1455754", "9d6829ecbc85a6653ca44ccd18c9243f", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认0%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    赛博朋克_I           = EffectMeta("赛博朋克 I", False, "6975112087659876895", "1238114", "3f5f8d770decd3fe853778e00f3ab589", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    赛博朋克_II          = EffectMeta("赛博朋克 II", False, "6997261680803582494", "1238113", "0bbcda72ffc36a7aa6dc7d5ec7cdc0b6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    赛博眼镜             = EffectMeta("赛博眼镜", False, "7055586958050857503", "1536126", "ce551db43d4cd0e9abf3e69a35513113", [])
    轻金属               = EffectMeta("轻金属", False, "7036946127320519182", "1463702", "6f5edc9d13d681afe8ee4f3224014a1e", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认75%, 0% ~ 100%"""
    运动轨迹             = EffectMeta("运动轨迹", False, "7389547512987652658", "74470467", "91ac684d7b70b28e9fd1f3c1f99c97e9", [
                              EffectParam("effects_adjust_number", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认40%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    迷茫                 = EffectMeta("迷茫", False, "6979931594408595975", "1185225", "19618c1e22b607642e7b27dc2602832f", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    闪影                 = EffectMeta("闪影", False, "7090458377901314568", "1825212", "864dcb150b85814ca7615946c7265941", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪烁                 = EffectMeta("闪烁", False, "7008060861528936991", "1404733", "b8648c0ede65749dcc4af04b7d5fa54c", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    闪电炸裂             = EffectMeta("闪电炸裂", False, "6999539022812942884", "1378606", "be8011441a484bf6661aa33604cd06bd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    阳光                 = EffectMeta("阳光", False, "6986176759725036039", "1197948", "7ea97e6b6156a1066459a400f0c26692", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认75%, 0% ~ 100%"""
    阴云密布             = EffectMeta("阴云密布", False, "7025527915320185375", "1427592", "25dc89f2e7cbe9ffb52d1da8f2cade5c", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    阴暗面               = EffectMeta("阴暗面", False, "7000679723906896397", "1378620", "f1efe71ae45c60bc94d1fcb168b8bf4d", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    难吃                 = EffectMeta("难吃", False, "7075326356585714207", "1627088", "22f5c7f78d72ed2767d8673414519e4b", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.200),
                              EffectParam("effects_adjust_horizontal_shift", 0.550, 0.300, 2.600),
                              EffectParam("effects_adjust_size", 0.500, 0.300, 2.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 120%
    effects_adjust_horizontal_shift: 默认55%, 30% ~ 260%
    effects_adjust_size: 默认50%, 30% ~ 200%
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    难过                 = EffectMeta("难过", False, "6979931396827517477", "1187975", "0d1f3c1ea1287cd2de9193f5a6c55d20", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%"""
    雪花眼泪             = EffectMeta("雪花眼泪", False, "7174694873897898553", "7078531", "b078f5583b67f9bfa95e30bf612e3482", [
                              EffectParam("effects_adjust_intensity", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认85%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_sharpen: 默认25%, 0% ~ 100%"""
    霓虹特技             = EffectMeta("霓虹特技", False, "7389546043534217778", "74469969", "a30c2949ccfc35417421caf68261ae0b", [
                              EffectParam("effects_adjust_size", 0.510, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认51%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认0%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%"""
    音符拖尾             = EffectMeta("音符拖尾", False, "7008458769675850248", "1404706", "7c1a10956911f225d514aab1ecfb7aeb", [])
    音符拖尾_II          = EffectMeta("音符拖尾 II", False, "7002176395312894494", "1238188", "c768fa0ad974298284a8adb66678e93a", [])
    飓风                 = EffectMeta("飓风", False, "7008458952451035678", "1404694", "a0bf72f591c6dbba8a211894f618976f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    飞翔的帽子           = EffectMeta("飞翔的帽子", False, "6999892125697446414", "1404708", "ec71eec4c8788ed43133f0a5a775e0c6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    鬼火                 = EffectMeta("鬼火", False, "7008470453366821389", "1404696", "6dcf3bafc5efbf4f3509dae601f57f54", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    黑人女孩             = EffectMeta("黑人女孩", False, "6971317836648026661", "1182265", "bde6e304a5de9614c0f44644fd3d15be", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    黑人男生             = EffectMeta("黑人男生", False, "6971317847318336031", "1182264", "a6e9afde1f86efbb91c49ecd9d6a8fdc", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    鼻血                 = EffectMeta("鼻血", False, "7153900212623249950", "5182539", "fc3d1f3cca541ced7f24b226eff114ee", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""

    # 付费特效
    _3D兔兔              = EffectMeta("3D兔兔", True, "7098954198204551716", "1924176", "78c9a5106ea815c821911a10f7631163", [
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    Love_u               = EffectMeta("Love u", True, "7058892012358996510", "1551894", "2aa9298939a522ca05e5219ab6e91cf6", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认80%, 0% ~ 100%
    effects_adjust_color: 默认30%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%"""
    X瞬移                = EffectMeta("X瞬移", True, "7265629618424517157", "20387617", "366528fe2ee5c5c851a694073cf4b855", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%"""
    分身_III             = EffectMeta("分身 III", True, "7281245666309837349", "23497249", "5b218df611d57e62c26029c0df884b13", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 0.600),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认30%, 0% ~ 60%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    分身ll               = EffectMeta("分身ll", True, "7207269616299545149", "10287363", "a42da906cd114315f798ba59b1692264", [
                              EffectParam("effects_adjust_vertical_shift", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.620, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认30%, 0% ~ 100%
    effects_adjust_size: 默认62%, 0% ~ 100%
    effects_adjust_range: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认55%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认30%, 0% ~ 100%"""
    发光分身             = EffectMeta("发光分身", True, "7233250530292666939", "13661053", "dbff6732319cf9488da4816c188d9f1a", [
                              EffectParam("effects_adjust_color", 0.840, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.102, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认84%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认35%, 0% ~ 100%
    effects_adjust_size: 默认10%, 0% ~ 100%
    effects_adjust_distortion: 默认30%, 0% ~ 100%"""
    变老_美颜            = EffectMeta("变老-美颜", True, "7226689898118386237", "12825757", "bd4037e779bb8ecd6ac12258853974b2", [])
    可爱龙龙             = EffectMeta("可爱龙龙", True, "7327508217590714931", "41751981", "9ac3a781a5aa5b33ddc73be905a2b270", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    吸血鬼               = EffectMeta("吸血鬼", True, "7154356694376518158", "5226581", "c560f8982d276a2824147698951751cd", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    哥特                 = EffectMeta("哥特", True, "7154061273838129672", "5199947", "94bd5a2ec19553d8e91423ab41b1bfee", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%"""
    嘻哈眼镜             = EffectMeta("嘻哈眼镜", True, "6998017895024300557", "1238128", "3a23ea8d16fe9ec18850783595877e4b", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认60%, 0% ~ 100%"""
    天使                 = EffectMeta("天使", True, "7156481333189939720", "5374123", "14336b246c295332eee8b29c5dc807c4", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.900, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认90%, 0% ~ 100%"""
    天使翅膀             = EffectMeta("天使翅膀", True, "6999514637767021070", "1378600", "f7acdf6cab043dbe7401ac89e572f6ff", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    奇行种               = EffectMeta("奇行种", True, "7168749461206733342", "6432361", "ca795d0b1827bcd27231c7c5a10825e3", [])
    局部模糊             = EffectMeta("局部模糊", True, "7036282000780562981", "1461580", "d61e04351e9ead6669cb6db1f4bdce05", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_noise: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认75%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认75%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%"""
    幻彩流光             = EffectMeta("幻彩流光", True, "7303422113812058633", "30319544", "5926b9713b3de1fe23a6b1790ba5d204", [
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.950, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认80%, 0% ~ 100%
    effects_adjust_luminance: 默认20%, 0% ~ 100%
    effects_adjust_intensity: 默认95%, 0% ~ 100%
    effects_adjust_color: 默认20%, 0% ~ 100%"""
    幻影平移             = EffectMeta("幻影平移", True, "7259667629357404730", "19114588", "4f4946b896cb4675e8514fa8d5af517a", [
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    彩虹流体             = EffectMeta("彩虹流体", True, "7273753115604554295", "21883974", "2725088e1378997bea428c8b04e2b15f", [
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认90%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    彩虹边缘             = EffectMeta("彩虹边缘", True, "7306769922535723558", "31771661", "e59040f43c25146de23341ac4b47a8bf", [
                              EffectParam("effects_adjust_intensity", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.150, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认55%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认15%, 0% ~ 100%"""
    影分身               = EffectMeta("影分身", True, "7306822259186864691", "31622417", "8088e845f5e6b8aecd6a9245cf033cfb", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    恶魔之翼             = EffectMeta("恶魔之翼", True, "7008049313305596446", "1404730", "99cdde82bb5587966f1a2bac10d024f2", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    情绪定格             = EffectMeta("情绪定格", True, "7298250619167445531", "28662656", "b60fd80757a580b75be83ea1b8905ef3", [
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.100, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_range: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认10%, 0% ~ 100%"""
    我太可爱了           = EffectMeta("我太可爱了", True, "7132773677086544398", "4104909", "76739264135fb0471d1ac7d9fa8b2027", [])
    我爱了               = EffectMeta("我爱了", True, "7182098630935843385", "9267743", "9ea5207040ca8a6c673eee1c8f4213e9", [])
    我麻了               = EffectMeta("我麻了", True, "7030722591358718494", "1441766", "b3078ea7691c02789dec4360d7ebd5a5", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    手写描边             = EffectMeta("手写描边", True, "7108559446065811998", "2869818", "59694d712050ddb032105f620b50ffe6", [
                              EffectParam("effects_adjust_color", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.210, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认20%, 0% ~ 100%
    effects_adjust_size: 默认21%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认20%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    捕梦                 = EffectMeta("捕梦", True, "7038866261677183524", "1471454", "24df2e977ac4752adaeb8f4495e98aeb", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    撕纸拼贴             = EffectMeta("撕纸拼贴", True, "7406207253583237682", "80787899", "e2b5e11e2f24940b65c91615723613f6", [])
    旋转分身             = EffectMeta("旋转分身", True, "7259667753731101244", "19114658", "f2a47eb17a20c6272e939350cf2268d3", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.300, 0.000, 0.750),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认30%, 0% ~ 75%
    effects_adjust_blur: 默认40%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%"""
    无限穿越             = EffectMeta("无限穿越", True, "7293870099738399269", "27074734", "f6bed6028a99ff60118167854f1f6ed1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认0%, 0% ~ 100%"""
    有事吗               = EffectMeta("有事吗？", True, "7322382230930592266", "39451195", "2cab81a0a4cad0393890f3eaad56a191", [
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认80%, 0% ~ 100%
    effects_adjust_background_animation: 默认60%, 0% ~ 100%"""
    机械环绕_I           = EffectMeta("机械环绕 I", True, "6986465789259813406", "1238184", "bff38e9886478c86635d990f78ca68cd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    机械环绕_II          = EffectMeta("机械环绕 II", True, "6997731822104744478", "1238185", "66eb2b1b98e4ada7cacba9c39d37be74", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    梦境                 = EffectMeta("梦境", True, "7039963252612141598", "1478040", "9f78e88b23ebbef1edc3439c2fc34c52", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    气炸了               = EffectMeta("气炸了", True, "7026548629498237454", "1426832", "979ebc680f1241a86545102632c79dff", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    波点分身             = EffectMeta("波点分身", True, "7086779590768595469", "1826180", "47f63e0ad4dd5f9c3d2045075b6795d4", [
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认60%, 0% ~ 100%
    effects_adjust_intensity: 默认25%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    流体故障             = EffectMeta("流体故障", True, "7287114240089920061", "24949284", "f6cfc884ea840da552785ed2c1a3309b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认70%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认80%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%"""
    涂鸦鬼影             = EffectMeta("涂鸦鬼影", True, "7153917024723276325", "5185037", "9570d183c3973de1498c638834c5136d", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    漩涡溶解             = EffectMeta("漩涡溶解", True, "7201020527501120057", "9583557", "3281d02205f102f70c4b07021be5bc71", [
                              EffectParam("effects_adjust_distortion", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.450, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认45%, 0% ~ 100%
    effects_adjust_speed: 默认45%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认45%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认25%, 0% ~ 100%
    effects_adjust_size: 默认45%, 0% ~ 100%
    effects_adjust_range: 默认45%, 0% ~ 100%"""
    火焰图腾             = EffectMeta("火焰图腾", True, "7009186785662079524", "1404736", "35e9cbe081d47066558a717ce3a774d8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    点赞                 = EffectMeta("点赞", True, "7072663671096218143", "1609620", "9f934cf082ec4d56a6f86e6e1aa2c8f6", [
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认25%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%"""
    热力光谱_I           = EffectMeta("热力光谱 I", True, "7033284501253919268", "1451182", "b578d3e33d8c650dc445c19875f9613f", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    热力光谱_II          = EffectMeta("热力光谱 II", True, "7033338062113346056", "1451606", "b711586fdabf06e7975e4bc2f2d906e6", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    焰火                 = EffectMeta("焰火", True, "7008459945590919716", "1404695", "3dc040bd8a6d3853428cc18030e7872a", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    熬夜冠军             = EffectMeta("熬夜冠军", True, "7330555999801053746", "43238686", "071e4eb6e85a9778b415bcb9303fd867", [
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认80%, 0% ~ 100%"""
    爱心                 = EffectMeta("爱心", True, "7068191600148484638", "1587990", "cda6bba22c1e6038233c0aaf3ec7c0ee", [
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    爱心发射             = EffectMeta("爱心发射", True, "7057403623004705294", "1551876", "665453673ccb652b012a46f63d32109d", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.350, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认35%, 0% ~ 100%"""
    爱心泡泡             = EffectMeta("爱心泡泡", True, "7055592805174874632", "1551930", "62cf1078f3a0e623c349cb4200f3de26", [
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认35%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    爱心眼               = EffectMeta("爱心眼", True, "7104647986176594463", "2491250", "aeee56c74c823b2afda571c023d0f992", [
                              EffectParam("effects_adjust_color", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.050, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认15%, 0% ~ 100%
    effects_adjust_size: 默认20%, 0% ~ 100%
    effects_adjust_range: 默认5%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    爱心美瞳             = EffectMeta("爱心美瞳", True, "7194734371872444965", "8950197", "23b70724f639f5020f4a4f6a53011868", [
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    狱火                 = EffectMeta("狱火", True, "7007676026406834725", "1404692", "29903a65ede13673b23ac1eedc118b5d", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    生气                 = EffectMeta("生气", True, "7068227476035473928", "1588764", "5c652a8c8a664b41ec7c59fa569ee3e8", [
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    电光描边_II          = EffectMeta("电光描边 II", True, "7265989852099777061", "20444547", "3a3aee848d3e7c13822281957ef09093", [
                              EffectParam("effects_adjust_luminance", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.110, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认75%, 0% ~ 100%
    effects_adjust_distortion: 默认65%, 0% ~ 100%
    effects_adjust_size: 默认75%, 0% ~ 100%
    effects_adjust_color: 默认11%, 0% ~ 100%
    effects_adjust_range: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%"""
    电光灼烧             = EffectMeta("电光灼烧", True, "7259649795571061305", "19106834", "3e5d0b31ae925f24539d89b017879815", [
                              EffectParam("effects_adjust_rotate", 0.730, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_rotate: 默认73%, 0% ~ 100%
    effects_adjust_color: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_distortion: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    电光眼               = EffectMeta("电光眼", True, "7106778883143242271", "2724384", "12aed71e7e62dafe99b6ff5ef264a36d", [
                              EffectParam("effects_adjust_color", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认25%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认25%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    电光耳机             = EffectMeta("电光耳机", True, "6998018067154342408", "1238127", "19a87efa0bebe59cdf36eda727a66664", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    眼神光               = EffectMeta("眼神光", True, "7091874262364983815", "1793042", "665fec8aacac1d793e7917a0a0ec3ab3", [
                              EffectParam("effects_adjust_intensity", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认75%, 0% ~ 100%
    effects_adjust_range: 默认85%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    瞬移                 = EffectMeta("瞬移", True, "7322735107280736805", "39618119", "29e526f7936cb5e985f77da6c51498ef", [
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%"""
    碎片分身             = EffectMeta("碎片分身", True, "7207691092655870523", "10339835", "86532426a7e3c08c229dd518c51a893c", [
                              EffectParam("effects_adjust_range", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.950, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认10%, 0% ~ 100%
    effects_adjust_intensity: 默认95%, 0% ~ 100%
    effects_adjust_speed: 默认0%, 0% ~ 100%"""
    碎闪边缘             = EffectMeta("碎闪边缘", True, "7306471467397419547", "31771693", "7c1311ff7b01577587a28252b3cd5d46", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.150, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认15%, 0% ~ 100%"""
    科技氛围_II          = EffectMeta("科技氛围 II", True, "6982572496356643359", "1238117", "d4b1ba4f4bb11a26860cd7f493853661", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    移形回位             = EffectMeta("移形回位", True, "7270801008094089784", "21811668", "4d2d96869fab0fa65766a52360c9fcef", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认30%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    移形幻影_I           = EffectMeta("移形幻影 I", True, "7201010922742092325", "9583559", "c89c34b83924f3fb5c88f2ece2e095b8", [
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    移形幻影_II          = EffectMeta("移形幻影 II", True, "7194734891353772603", "9010339", "c4ce763e7fcd977c98e4b4a8be0b85a1", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    空气流体             = EffectMeta("空气流体", True, "7283548311217246781", "24123133", "9882eb0caf97221ac6bd4161ead3a263", [
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.720, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.660, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认72%, 0% ~ 100%
    effects_adjust_size: 默认66%, 0% ~ 100%"""
    笑哭                 = EffectMeta("笑哭", True, "7072173200418804231", "1606772", "9b86bc9942f7848d7ee7e7e74a077a4b", [
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认25%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%"""
    粒子弥散             = EffectMeta("粒子弥散", True, "7283038170826936892", "23970537", "7a72cd5b5950e933ca7f6df425537c21", [
                              EffectParam("effects_adjust_horizontal_shift", 0.660, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认66%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    美味召唤             = EffectMeta("美味召唤", True, "7073398095186235935", "1612792", "1e09bf5fc9f3bc36e9fdb479c832365b", [
                              EffectParam("effects_adjust_vertical_shift", 0.600, 0.000, 1.200),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认60%, 0% ~ 120%
    effects_adjust_size: 默认50%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    蝴蝶翅膀             = EffectMeta("蝴蝶翅膀", True, "6999567409677865486", "1378607", "69eaf245462b3777f94dfc5aabe18791", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    轮廓扫描             = EffectMeta("轮廓扫描", True, "7260773990178755129", "19351962", "82f3b4a76091dda533a0ca1b0b2265e8", [
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%
    effects_adjust_soft: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    迷幻分身             = EffectMeta("迷幻分身", True, "7280421849974968889", "23303207", "e2bd87ba0c294b5340a8b74cf7c3f954", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.850, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认70%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认90%, 0% ~ 100%
    effects_adjust_size: 默认85%, 0% ~ 100%"""
    金币掉落             = EffectMeta("金币掉落", True, "7021362776404660743", "1543838", "06be5783fa794fc209023a283a47a7d3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    镭射眼_I             = EffectMeta("镭射眼 I", True, "7106778448344912421", "2724386", "ea9d0666a569334a0c6b27c14ade2674", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认90%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    镭射眼_II            = EffectMeta("镭射眼 II", True, "7106778621326397983", "2724385", "3891948240e1594b7ea8025222341a9d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.620, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认62%, 0% ~ 100%"""
    闪光放大             = EffectMeta("闪光放大", True, "7304912977180758537", "33838202", "a64dcdf7a22d382739051486535a4704", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_distortion: 默认70%, 0% ~ 100%"""
    闪电                 = EffectMeta("闪电", True, "7088198349324554766", "1711412", "9c97ab760617a5c3bc75491b3ad8406b", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认10%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    闪电环绕             = EffectMeta("闪电环绕", True, "6998102186068546078", "1238186", "d2459fb754b3d9dbb469d29f6af77423", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    闪电眼               = EffectMeta("闪电眼", True, "7106763566262260231", "2722184", "6b6b4e9eb53581fea08118f62d55c1a9", [
                              EffectParam("effects_adjust_color", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.850, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认25%, 0% ~ 100%
    effects_adjust_luminance: 默认25%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_range: 默认85%, 0% ~ 100%"""
    霓虹爱心             = EffectMeta("霓虹爱心", True, "7194734553288675895", "9221893", "cf3b121f71539f6fc039062473db7c43", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    高光人物             = EffectMeta("高光人物", True, "7406179353362436645", "80107647", "4264ef0b6e1ada149ba0580b36001e2c", [])
    黑色眼泪             = EffectMeta("黑色眼泪", True, "7154231632604434981", "5208347", "0343aabd4b0ef59cc829bd1732be0bbd", [
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
