from .effect_meta import EffectEnum
from .effect_meta import EffectMeta, EffectParam

class VideoSceneEffectType(EffectEnum):
    """剪映自带的画面特效类型"""

    _1998       = EffectMeta("1998", False, "6981791065204331044", "1183068", "d53096e8139dd33f7a2be6adcd7ce56b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    _70s        = EffectMeta("70s", False, "6706773500792689165", "634717", "0fe827460716d30e76cb3f244b9b1010", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    _90s画质    = EffectMeta("90s画质", False, "6760946510910722564", "634889", "d2b4c0ed72e66c6ae61e0ebbc7d008bf", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.630, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.580, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.510, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.63, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.58, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.51, 0.00 ~ 1.00
    """
    DV录制框    = EffectMeta("DV录制框", False, "6878115805498708493", "934600", "4828fe3f6a8bdf99e57febe27006d33b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.20, 0.00 ~ 1.00
    """
    DV界面      = EffectMeta("DV界面", False, "6974600764027048462", "1164160", "ed29f490b4ccb7f00138f400b05459b5", [])
    I_Lose_You  = EffectMeta("I Lose You", False, "6899746903735407117", "972753", "8486881738dcb661bcd49f490a548d47", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    I_Love_You  = EffectMeta("I Love You", False, "6899746786294895112", "972754", "dfa377da1cc1858ae5d5126488c5cb67", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    JVC         = EffectMeta("JVC", False, "7102302420310430215", "2254788", "6060fe9faac1a35dd89c4362c57bd451", [
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.90, 0.00 ~ 1.00
    """
    List边框    = EffectMeta("List边框", False, "6981463637676266020", "1181892", "80a8d14e52a06b47dbb24ddeb7b65f1c", [])
    MV封面      = EffectMeta("MV封面", False, "6925314612204147214", "1033288", "658b5a2a87b51d71f8f968546790257a", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    New_Year    = EffectMeta("New Year", False, "7041771617315197453", "1483460", "b3322fbbf99e1d4c9da1fb0b1e97d1a6", [
                              EffectParam("effects_adjust_size", 0.160, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.339, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.16, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    PS边框      = EffectMeta("PS边框", False, "6860306184595837448", "884226", "a787cee77871e18ae45ccd09fa7f6ac9", [])
    RGB描边     = EffectMeta("RGB描边", False, "6922698007653650957", "1025970", "175536eb523aae867ae4b8cb94f09211", [
                              EffectParam("effects_adjust_speed", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    VCR         = EffectMeta("VCR", False, "6876012864679711245", "931458", "6b5dfc171f7c82078c76ffbcb2f6c003", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    X_Signal    = EffectMeta("X-Signal", False, "6709706971638927875", "634719", "218223a1507ca3cac6b93dd8335882a0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    X开幕       = EffectMeta("X开幕", False, "6974024838000153096", "1162978", "59be0a7455162145039e48179ef42c20", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    betamax     = EffectMeta("betamax", False, "7239937281937642041", "14578173", "6cae0f338637ffcf210bbb45015d9538", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
    """
    emoji钻石   = EffectMeta("emoji钻石", False, "7078694071245476366", "1647776", "afa5891d090fe132e4cf0a7196895863", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.548, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    ins界面     = EffectMeta("ins界面", False, "6761646727142314509", "635133", "1081a3f864316cb7e8ee977d44a90a70", [])
    ins风放大镜 = EffectMeta("ins风放大镜", False, "6992465511455920676", "1380488", "afe7daae94e810f06b339c96deafb5f8", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.00, 0.00 ~ 1.00
    """
    kirakira    = EffectMeta("kirakira", False, "6706773500142555656", "693883", "45e5aac6ec5e94c4639c3671e50fb372", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.33, 0.00 ~ 1.00
    """
    ktv灯光     = EffectMeta("ktv灯光", False, "6771299914891661832", "634197", "0654e68b3db41a82a1abf02e48375e88", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    ktv灯光_II  = EffectMeta("ktv灯光 II", False, "6934938159763427876", "1054906", "53248914c97ddf4722860554d68cac9d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    windows弹窗关闭= EffectMeta("windows弹窗关闭", False, "6976562270071427598", "1169934", "f4d45d9888b6d0d78a147417e4851189", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    windows弹窗打开= EffectMeta("windows弹窗打开", False, "6976538396290191880", "1169728", "6989cff6be738ec6a047871320d3bd9f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    丁达尔光线  = EffectMeta("丁达尔光线", False, "6834008866137575950", "768190", "858aa00b8938e4f0dde79225ef119f60", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    万圣emoji   = EffectMeta("万圣emoji", False, "7021363005052948999", "1405514", "0b226c96ee570ed8c649d97f45879faa", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    万圣夜      = EffectMeta("万圣夜", False, "6888280327949652493", "951616", "ccd9f93a03f5849a5d5cb96729bb5bec", [
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    三屏        = EffectMeta("三屏", False, "6706773500209664515", "635029", "a753c93aef7a37f2e86870529f2cd06c", [])
    三格漫画    = EffectMeta("三格漫画", False, "6795825532668744206", "635007", "5b738f1286b9929b36bc6a540f11ddd5", [])
    下雨        = EffectMeta("下雨", False, "6734619419890160131", "635039", "40a59ce61692a825c049cd5b15bc6ded", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    不对劲      = EffectMeta("不对劲", False, "6940134524642660895", "1068128", "0be37b64dad56d5f6f89c69165d092fd", [])
    不规则黑框  = EffectMeta("不规则黑框", False, "6865921530488951309", "898673", "2457889e649132e1a427ccd9c258e51e", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    两屏        = EffectMeta("两屏", False, "6706773500796867075", "635025", "69926ac7983e4e234c1b833e8c50896a", [])
    中枪了      = EffectMeta("中枪了", False, "6950894972291781127", "1100950", "ee96dc698c6213303442b30b963978ba", [])
    乌鸦飞过    = EffectMeta("乌鸦飞过", False, "6955028776094798366", "1113160", "a2583447f1ec5767bf063a831b893b9e", [])
    九屏        = EffectMeta("九屏", False, "6719657094741496333", "635011", "8abb86f5699f22f9d2c8d1647458b55a", [])
    九屏跑马灯  = EffectMeta("九屏跑马灯", False, "6726773973683540491", "635031", "0bc85f7544b92909bfef4d20ad17c256", [])
    亮片        = EffectMeta("亮片", False, "6715209448521994755", "634129", "b27dcf2220fd8d3ff7216d9364d07b62", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    人鱼滤镜    = EffectMeta("人鱼滤镜", False, "6766876614862049795", "634199", "f97bd68cfc43174bcb30406a6fc46952", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    仙女变身    = EffectMeta("仙女变身", False, "6746483363567112707", "634173", "b45f02e327c3c242c54f91655798d9c0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    仙女变身_II = EffectMeta("仙女变身 II", False, "6747515070114173447", "634171", "6963f2dab25279d695f581922ce9f87f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    仙女棒      = EffectMeta("仙女棒", False, "7314565034586149403", "35504704", "322d997e0f5a8a9af19acd3c871b98ff", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    仙尘闪闪    = EffectMeta("仙尘闪闪", False, "6963476143370408485", "1133662", "8b9da7f7b3cdd95bd73cc2444433017e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    低像素      = EffectMeta("低像素", False, "6810945511005098509", "703237", "07980fba1cb9edb304a39feaa92f009c", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    低像素_II   = EffectMeta("低像素 II", False, "6811399125544735245", "703239", "01c40b95e4a5b8f850bad330a1864f6a", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    倒计时_II   = EffectMeta("倒计时 II", False, "7051887173276013093", "1521390", "e01f6dadb794566d1ea3364d564f3f59", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    像素画      = EffectMeta("像素画", False, "7081557169539125791", "1663132", "0e6597e2bcbc35fe670bd05501ff37ed", [
                              EffectParam("effects_adjust_color", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.755, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.688, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.76, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.69, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.00, 0.00 ~ 1.00
    """
    像素纹理    = EffectMeta("像素纹理", False, "6763903685983474189", "634785", "d132cd0508064d64e92b946adfa5c8be", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    光斑虚化    = EffectMeta("光斑虚化", False, "7297154514262430259", "28151372", "2748cc7e4a94448bddefe35749cce1db", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
    """
    光斑飘落    = EffectMeta("光斑飘落", False, "6899747276718084622", "972749", "5106ce263097acfbe5f8319841bc1e7a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    光晕        = EffectMeta("光晕", False, "6714239617916211716", "634095", "91a3d5329874b35dad2cf9fbf82956af", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    光晕_II     = EffectMeta("光晕 II", False, "6709701759398318604", "634093", "24ade7e79a0d72d1fe5792997640e15f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    全剧终      = EffectMeta("全剧终", False, "6710109932122804750", "634079", "b756f1d59534d07571ab6fac16d8bfda", [])
    六屏        = EffectMeta("六屏", False, "6719657243039502851", "635013", "95d23405c9441a388784c0749ab99471", [])
    关月亮      = EffectMeta("关月亮", False, "6774656266833760780", "634277", "af6c277f693f08679dc142591bc97c52", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.33, 0.00 ~ 1.00
    """
    冰冷实验室  = EffectMeta("冰冷实验室", False, "7019265849047388680", "1398372", "0ba96868fd684b80b4cb82f058f35dc9", [
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.267, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.27, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    冰霜        = EffectMeta("冰霜", False, "6896417042090430989", "966514", "17d279016b1f0961c4e0167f2554b0f5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    冰霜_II     = EffectMeta("冰霜 II", False, "7047048873897890334", "1499080", "f278e4a04de56a4fbe693e2014f5da9e", [
                              EffectParam("effects_adjust_speed", 0.530, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.53, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    冲击波      = EffectMeta("冲击波", False, "6967180577875169799", "1146394", "ad8e0a154e7a3c78dc23407ec23da9b2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    冲刺        = EffectMeta("冲刺", False, "6790536507905020430", "635003", "7efa92b9cc009384af9b207474f52b24", [])
    冲刺_II     = EffectMeta("冲刺 II", False, "6781392637216690700", "635001", "5781353d9e23652896b0dd8c43a51162", [])
    冲刺_III    = EffectMeta("冲刺 III", False, "6774324121783243271", "634981", "a2794140abd30a19ba136059f9f89e88", [])
    冲屏闪粉    = EffectMeta("冲屏闪粉", False, "6858138911487562248", "875969", "98753cc737cac50d460ec6f204cdae5b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    凄凉        = EffectMeta("凄凉", False, "6955021464684728846", "1113134", "0491da81159994e95a68b3087a8709f3", [])
    几何图形    = EffectMeta("几何图形", False, "6871054818241155592", "920550", "0c558210a312c46568635767a3600a08", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    刀光剑影    = EffectMeta("刀光剑影", False, "6740539604509659662", "634741", "8017d7de152a4083d0607b903d716943", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    分屏开幕    = EffectMeta("分屏开幕", False, "7232198317671715385", "13525811", "98ecc4fbd0e619bddad881dc93a94964", [
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
    """
    初雪_I      = EffectMeta("初雪 I", False, "7173558688605540901", "6940749", "8bbb39ead793c59a4baec469890be670", [
                              EffectParam("effects_adjust_speed", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    加载甜蜜    = EffectMeta("加载甜蜜", False, "6924873263994638856", "1031291", "224dafbed2fc8e3711e1cecacf68a95c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    动感模糊    = EffectMeta("动感模糊", False, "7009120603055591943", "1368758", "167deb8c5b35d5a3097cb107693c62c3", [
                              EffectParam("effects_adjust_horizontal_shift", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_shift: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.85, 0.00 ~ 1.00
    """
    动感荧光    = EffectMeta("动感荧光", False, "6755761739242934798", "635125", "d9f1ac0e1677dcd4475235ea113f03fa", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    动感蓝带    = EffectMeta("动感蓝带", False, "6970598283378954765", "1155430", "28edc10c2a172ca68f6be21037700538", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    单色涂鸦    = EffectMeta("单色涂鸦", False, "7265798651019006521", "20412423", "8a63108339eeb62c0a26122e2f22a850", [
                              EffectParam("effects_adjust_color", 0.300, 0.050, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.570, 0.000, 0.810),
                              EffectParam("effects_adjust_horizontal_shift", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.30, 0.05 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.57, 0.00 ~ 0.81
        - effects_adjust_horizontal_shift: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
    """
    南瓜光斑    = EffectMeta("南瓜光斑", False, "6992844454453318157", "1403930", "3626a4cba39f68ed0bbf43b58c023e07", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    南瓜笑脸    = EffectMeta("南瓜笑脸", False, "6888208083202347534", "951196", "e28abcdb93864f4d4c1d340e9ce567a5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    卷动        = EffectMeta("卷动", False, "6719657168292811278", "634735", "613ab501b1260fee424d266c6a214b5e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    原相机      = EffectMeta("原相机", False, "6753416178909057549", "635137", "bc6e1e30a3e6efd3ad60939a09e66323", [])
    友友商店    = EffectMeta("友友商店", False, "6977709836993565220", "1173234", "6fd942a59a1b4010a23b19f74a8fb08a", [])
    反转片_I    = EffectMeta("反转片 I", False, "7153084450593575454", "5114825", "442b39ec01b7ddefd1a2dfe1ce66d00e", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    发光        = EffectMeta("发光", False, "6961701455262650916", "1126104", "43648253eed7fb8ea727d167d28cd768", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.40, 0.00 ~ 1.00
    """
    取景框      = EffectMeta("取景框", False, "6712739398984667651", "635089", "1915e124716f1967476f78970f6e90b9", [
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    取景框_II   = EffectMeta("取景框 II", False, "6871187132195541517", "920935", "a8af25fab9ceb2a477fb007d3dfc72b1", [])
    变形了      = EffectMeta("变形了", False, "6940134629282157064", "1068127", "45a40940622ed9173d57e23ff1b3ddee", [])
    变彩色      = EffectMeta("变彩色", False, "6720492336788279815", "634053", "0178a55e4f8c7deec8786d78d875d45e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    变清晰      = EffectMeta("变清晰", False, "6719658716750156291", "634019", "feb43ab124f2c4bc8ee045a773741ed9", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
    """
    变清晰_II   = EffectMeta("变清晰 II", False, "6948352810895282724", "1146596", "da0c95a0f050f7e26e672dfdcbddc226", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    变焦推镜    = EffectMeta("变焦推镜", False, "7296418835429593651", "27896191", "1ef600710b33cc1e4d6f858c47e4b98a", [
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    变秋天      = EffectMeta("变秋天", False, "7012941093520020004", "1381700", "c7aaafd076935ba5a0a42e58365a49cf", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    变黑白      = EffectMeta("变黑白", False, "6730911849706951179", "634055", "d38bd3379c22f994fc3f0819998962c9", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    告白氛围    = EffectMeta("告白氛围", False, "6798021156331852295", "635005", "ed6536056d82bcd5849014db48d9d912", [])
    咔嚓        = EffectMeta("咔嚓", False, "6752780026900386317", "634073", "c742af6913646f7c936642aae51d58d2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    哈哈弹幕    = EffectMeta("哈哈弹幕", False, "6952852858656002590", "1106302", "777c2c44707c03f6e541c8d954b21f8a", [])
    哈苏胶片    = EffectMeta("哈苏胶片", False, "7078598928056193566", "1646830", "2eead808b8408e1fa4b74b6ad3c74b8d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.30, 0.00 ~ 1.00
    """
    唱片        = EffectMeta("唱片", False, "6978764021637845541", "1174596", "d4fef5476754cbe563d5004097369290", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    唱片封面    = EffectMeta("唱片封面", False, "6987741974455390734", "1196734", "11ca22f7daac786267a46f99dad47be3", [])
    啊啊啊啊    = EffectMeta("啊啊啊啊", False, "6951661272827957790", "1104164", "cec37f504863cc89308c256482286660", [])
    噪点        = EffectMeta("噪点", False, "6706773498510971404", "634061", "3e5fc04a3ddff85aadb6b52681f00bcd", [
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
    """
    四屏        = EffectMeta("四屏", False, "6706773500490682888", "635027", "f0074ead79e0a8dd9a10518667beb0f1", [])
    回弹摇摆    = EffectMeta("回弹摇摆", False, "7146090225855369742", "4720539", "e13659f2365eb5bc295f93342e50139f", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
    """
    回忆文件夹  = EffectMeta("回忆文件夹", False, "6998352498062791205", "1227934", "cf7de583f8e09da1476df20d95fc85f2", [])
    回忆胶片    = EffectMeta("回忆胶片", False, "6987725478912070174", "1196624", "3f4f6d7ce71f67e1e61b91d366da4e19", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
    """
    圆形虚线放大镜= EffectMeta("圆形虚线放大镜", False, "7065242222068765198", "1569306", "44370286a32ad2e26535a6af4842aa0b", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.00, 0.00 ~ 1.00
    """
    圣诞光斑    = EffectMeta("圣诞光斑", False, "6769436675958379021", "634209", "dd982dabe21c82f51a9815df29f83f09", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    圣诞星光    = EffectMeta("圣诞星光", False, "6767219683901837832", "634207", "3e41badb29cc40f017f2ece636d26557", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    地狱使者    = EffectMeta("地狱使者", False, "7007684840506003999", "1406882", "2338b8056d16c87a210717ef9bdc28b5", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    基础黑框    = EffectMeta("基础黑框", False, "6712316216905568772", "635127", "534a1c475b222dfc97420bbaf85b7540", [])
    塑料封面    = EffectMeta("塑料封面", False, "6814664313496670728", "703221", "4df02db49968718592fe29998506b8e2", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    塑料封面_II = EffectMeta("塑料封面 II", False, "6814664561082241550", "703219", "204ce6bc753bbc228d489e580c799768", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    塑料封面III = EffectMeta("塑料封面III", False, "6815457699505902087", "703217", "48d99133cab78a4a9b178d8f7fe7be66", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    复古DV      = EffectMeta("复古DV", False, "6865959646092333576", "898868", "19e1584168d4d3570a91185b8149ad03", [
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
    """
    复古DV_II   = EffectMeta("复古DV II", False, "6869650937841979911", "909740", "6979960d3bda8144b3406dee17e7255a", [
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
    """
    复古DV_III  = EffectMeta("复古DV III", False, "6986958810619318792", "1194896", "ff4ee88f3d727ac817750ae84df099cc", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    复古DV_IV   = EffectMeta("复古DV IV", False, "6994703188611830303", "1217306", "d97c48bb4c8048cbeb2ec8ca8e16e43e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.55, 0.00 ~ 1.00
    """
    复古发光    = EffectMeta("复古发光", False, "6993267867214942733", "1212776", "cfea69839054bf3cd30f7a2ac3727ea4", [
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.60, 0.00 ~ 1.00
    """
    复古多格    = EffectMeta("复古多格", False, "6875631945510818318", "926324", "19a3d5873d394ff550d6a4367ef18a45", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
    """
    复古弹窗_I  = EffectMeta("复古弹窗 I", False, "6709708058852856327", "635103", "2c2502e679630278461b6ad9d8482928", [
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
    """
    复古弹窗_II = EffectMeta("复古弹窗 II", False, "6764667280681865731", "635143", "168f6b6dfc18d80bf35853d6b7774030", [])
    复古漫画    = EffectMeta("复古漫画", False, "6847440397027774984", "784724", "1f89b68447a46e9feb69654e4dc97a7f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    复古甜心    = EffectMeta("复古甜心", False, "6926817888632312333", "1039434", "80dbaf8bbb2d7cecdaff271656a58126", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    复古碎钻    = EffectMeta("复古碎钻", False, "6948700335481295374", "1094804", "56f3d29724754f5fc9d50c7bf6c02e28", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    复古蓝调    = EffectMeta("复古蓝调", False, "7078935944459457061", "1648234", "971c462f47f17dd2827ad4fde77fc015", [
                              EffectParam("effects_adjust_sharpen", 0.630, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.630, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_sharpen: 默认0.63, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.63, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    夏日冰块    = EffectMeta("夏日冰块", False, "7237437172733710909", "14244311", "46b643fafe2c93bfc6607b2fe5fdd429", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.230, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.23, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    夏日泡泡_I  = EffectMeta("夏日泡泡 I", False, "7104624152044114462", "2488948", "9f8219296472225136b6e73bc4c23206", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
    """
    夕阳        = EffectMeta("夕阳", False, "6820595030743323149", "719376", "766398e7682640dc13bceb3f448847dc", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    夕阳_II     = EffectMeta("夕阳 II", False, "6823659895221391886", "720788", "eea48333e37961c63e8d45077552de5a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    夕阳_III    = EffectMeta("夕阳 III", False, "6836996542310650381", "762382", "6deca5bd30382b52c6a7985cee5c4ca2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    夜蝶        = EffectMeta("夜蝶", False, "6748376019524129292", "634175", "8a1a97c0b237adfb31c8ae55faa64e74", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    夜视框      = EffectMeta("夜视框", False, "6733023209978860035", "635131", "cef5df7500848aeee3f4ea15c6cdaa5b", [])
    大雪        = EffectMeta("大雪", False, "6767148963503018503", "635063", "950d1e82cf0093f609e864d11f8a005d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    大雪纷飞    = EffectMeta("大雪纷飞", False, "6894517304487318024", "961896", "84aa80de0bf14d5924dab46be29f7b5a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    天使光      = EffectMeta("天使光", False, "6721949326022545928", "634143", "37c4098ac98fc25188a5a727064a7729", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    天使降临    = EffectMeta("天使降临", False, "7020715912596558366", "1402689", "be7a34ae22c8b39d1750a602757e4867", [])
    失焦        = EffectMeta("失焦", False, "6984625607376114190", "1188938", "468cbf025f095d34bc7dd08462c94eae", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    夸夸弹幕    = EffectMeta("夸夸弹幕", False, "6956147849356644894", "1115952", "9a0e752e8d60267d088a2ade9fb7299d", [])
    夺冠        = EffectMeta("夺冠", False, "6986857922076611080", "1194360", "fae722df471ae30a898ace2990cbbf3d", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    孔明灯      = EffectMeta("孔明灯", False, "6734215575196668428", "635037", "f701053aea29c2163b02f98fd9c755ec", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    孔明灯_II   = EffectMeta("孔明灯 II", False, "7008056576514724365", "1363340", "c1a6557f355c41e09fa4c2723d5f5f3e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    字幕投影    = EffectMeta("字幕投影", False, "6828021842695950856", "747802", "ad0ff707e15d0e2dedcc23ef0c57c29a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    字幕投影_II = EffectMeta("字幕投影 II", False, "6829181074954785294", "747910", "d6388dec46d30dda96d8a273616978eb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    字幕投影_III= EffectMeta("字幕投影 III", False, "6847378675894063623", "784366", "5c5ede6eb3a35e275167b8845c7ee7d5", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    字幕投影_IV = EffectMeta("字幕投影 IV", False, "6858139153020752397", "875967", "ebd3c54c9dbfe73027fd9d480c175888", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    定格闪烁    = EffectMeta("定格闪烁", False, "6998099471565328926", "1227402", "03704af752f236eec942f78ae1190d41", [
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    小剧场      = EffectMeta("小剧场", False, "6955083477708444174", "1113428", "602daf84aef020a2dcba8cbd52182b66", [])
    小动物      = EffectMeta("小动物", False, "6965381784674505246", "1138384", "93e09d8cd1a85e9faae8da2212be88eb", [])
    小花花      = EffectMeta("小花花", False, "6926823177670627848", "1039448", "6fe0a146c0133191fd663c439f213236", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    少女心      = EffectMeta("少女心", False, "6992842225541452325", "1209684", "41607b261ff3c0999a2c43370dd8c442", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    少女心事    = EffectMeta("少女心事", False, "6924872492381114894", "1031294", "ebba75bb53013a6347814b486c6063eb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    少女星闪    = EffectMeta("少女星闪", False, "6805098811694780942", "703255", "830c6652734b4d6c12604e6f5832c6a1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    左右摇晃    = EffectMeta("左右摇晃", False, "7166435460321907207", "8430539", "02b826db1b4f972ec812d76b50a49e05", [
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
    """
    布拉格      = EffectMeta("布拉格", False, "6869626257709994510", "909545", "b9b8d37e73f8a5a1c0abff8d6c7cd1b0", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    幻彩文字    = EffectMeta("幻彩文字", False, "6760975890806477319", "634737", "0d367c9f530e2fe08aef913cf1451443", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
    """
    幻影        = EffectMeta("幻影", False, "6723059630676644364", "634751", "44cb0b2f810fa3119f2c9f1ae396db9d", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    幻影_II     = EffectMeta("幻影 II", False, "6898958754792870413", "971332", "14e6364b3a6a1485f2583bdfc32b9f9a", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    幻术摇摆    = EffectMeta("幻术摇摆", False, "6926400232615842318", "1038152", "3bb76ef02392a04f5b387dbd46942458", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    幻觉        = EffectMeta("幻觉", False, "6709706311455478285", "634723", "1fa56d867a4651cbefbf6a4f669aeafc", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    广角        = EffectMeta("广角", False, "7086792017837036046", "1700284", "646ffb6188a447622926872c4fc453d6", [
                              EffectParam("effects_adjust_intensity", 0.450, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.45, 0.00 ~ 1.00
    """
    庆祝彩带    = EffectMeta("庆祝彩带", False, "6984685757508096520", "1189232", "42197cc2549fafa41c4854c4ee086074", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    开幕        = EffectMeta("开幕", False, "6706773534074491403", "631211", "7afa9c82c3d221742bb42a3b01d4fce7", [])
    开幕__II    = EffectMeta("开幕  II", False, "6708899027976458760", "631213", "9fd3ee125c1319e1a3d2345849bef96b", [])
    强锐化      = EffectMeta("强锐化", False, "6711567084741988876", "634783", "c9ae5be2cd096747898e905fe2b6836b", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.620, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.62, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    录像带      = EffectMeta("录像带", False, "6706773534074475012", "634887", "c880d7f9eb6b4f94bf4e8f790fcf3dc0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.40, 0.00 ~ 1.00
    """
    录像带_II   = EffectMeta("录像带 II", False, "6771299859803673101", "634811", "12b20ba900b09a9cd833ffb15eec5f74", [
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.50, 0.00 ~ 1.00
    """
    录像带_III  = EffectMeta("录像带 III", False, "6804357689859117581", "703251", "de0caa2ec7151990960b56f62fedd3fc", [])
    录制框      = EffectMeta("录制框", False, "6709725898762883595", "634801", "bbed85838ac97f63298e51e2f2b0bb03", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    录制边框    = EffectMeta("录制边框", False, "6720541178044879367", "635121", "5a388c880fe2fec47424d62a1e81c2c1", [])
    录制边框_II = EffectMeta("录制边框 II", False, "6720541079080276484", "635119", "aeb6eaaa2881ed69afb5ece40c7c4eb4", [])
    录制边框_III= EffectMeta("录制边框 III", False, "6894451240382501389", "961624", "bc759f18216aac435a0cf29b69bb5051", [])
    录制边框_IIII= EffectMeta("录制边框 IIII", False, "6723065859260027403", "634063", "93297cd4887ae225ecc81f79e89c156b", [])
    彩信        = EffectMeta("彩信", False, "7023692066152518152", "1418386", "d019bb0c5188a75893b08562c9951a4f", [
                              EffectParam("effects_adjust_vertical_shift", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
    """
    彩噪画质    = EffectMeta("彩噪画质", False, "7135711291473138184", "4253680", "fbdce889885763ee82ffa7138de4d36b", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
    """
    彩带        = EffectMeta("彩带", False, "7012933493663470088", "1381644", "c8b3549975f0ddca9247553c2ce79564", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    彩色描边    = EffectMeta("彩色描边", False, "6966904744564494878", "1143666", "fd18f1469ac653e38814a8f6ea7db6bd", [])
    彩色漫画    = EffectMeta("彩色漫画", False, "6795430958737658382", "634947", "329880da582a412ad4db0451755a2065", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    彩色负片    = EffectMeta("彩色负片", False, "6914995893653475847", "1005840", "a78b49205a5d3b7fbc04a19aebce80ea", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    彩虹光      = EffectMeta("彩虹光", False, "6719758141573042692", "634161", "e39f46b0d21562c05fecfd9404d5a22f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    彩虹光_II   = EffectMeta("彩虹光 II", False, "6738279134692119047", "634159", "03814fa76660bb3db88128e2a5ef000f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    彩虹光晕    = EffectMeta("彩虹光晕", False, "6768721870360416782", "634213", "3f04c39cc212c63ac3caa048f6c34588", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    彩虹射线    = EffectMeta("彩虹射线", False, "6808837459728667144", "703249", "5c817bb9e37fafa3f03966051050040c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    彩虹幻影    = EffectMeta("彩虹幻影", False, "6756845151630397960", "634281", "a5f61f00265cbcf6fbc430780f5b4c03", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    彩虹气泡    = EffectMeta("彩虹气泡", False, "6717434470128947725", "634127", "cf2687ea75161551a44016ef2ee4782d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    彩虹爱心    = EffectMeta("彩虹爱心", False, "6924873147053249031", "1031292", "235be137b3284f3d586e03f021951dac", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    彩钻        = EffectMeta("彩钻", False, "6986188114490298888", "1192480", "ba1ae230f2b24fe3383802194fb18e5d", [
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    心河        = EffectMeta("心河", False, "6740821434307711496", "634273", "e01e24abb316c5d1ef6f71946aeb1f16", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    心跳        = EffectMeta("心跳", False, "6723068356821258764", "634753", "fb26e9377ee378736086a4e60bde0cce", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    心跳黑框    = EffectMeta("心跳黑框", False, "6732383404991451656", "634049", "167ba80ce0571ba3d1d17d59f5ef5ea1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    必杀技      = EffectMeta("必杀技", False, "6797658471840879111", "634979", "ac8846e43b1fec25f2afe182d13feb24", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    必杀技_II   = EffectMeta("必杀技 II", False, "6797346848391565831", "634977", "4e3e9d5edd2dc99af5881e3ca3d9344e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    怀旧边框    = EffectMeta("怀旧边框", False, "7113820806446060040", "3222474", "6d93d853611744ad573e113f8acd3ba6", [
                              EffectParam("effects_adjust_size", 0.636, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("sticker", 0.630, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.64, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - sticker: 默认0.63, 0.00 ~ 1.00
    """
    怀旧边框_II = EffectMeta("怀旧边框 II", False, "7039331384183230989", "1475190", "97076a8938d8f45a233d97fd240951c3", [])
    怦然心动    = EffectMeta("怦然心动", False, "6924872657083044359", "1031293", "d5e216a1700db22637509d2966004b16", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    恐怖故事    = EffectMeta("恐怖故事", False, "6888563496133333511", "952539", "5ffc4c3a4ee71dd9aa5f728da300e0f2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    恐怖故事_II = EffectMeta("恐怖故事 II", False, "6888562369627165191", "952540", "900c63e3517b6fb24b9ed1b66c29efe0", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    恐怖故事_III= EffectMeta("恐怖故事 III", False, "6888594040959275527", "952742", "472194dc4d5622347368fc59c753d827", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    恐怖综艺    = EffectMeta("恐怖综艺", False, "7023349285592764941", "1416842", "733e0831b3facd0931d6e648e1b381fd", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.802, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    恶灵冲屏    = EffectMeta("恶灵冲屏", False, "7022838857221542414", "1413882", "c440724a491336aba4e24910d5c7f6f1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    愛          = EffectMeta("愛", False, "6831487239164269064", "756184", "310f9f3c69c75cbb8eb25011d01d5ac4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    我酸了      = EffectMeta("我酸了", False, "6955083374054609444", "1113430", "393059e1b508041d77792ef44ffc007b", [])
    手帐边框    = EffectMeta("手帐边框", False, "6761336384117543438", "635113", "737114bc5ff9b162c7f6fc403e308d63", [])
    手电筒      = EffectMeta("手电筒", False, "6860757586220683790", "886132", "42bd8193cfc9d60fdf4392ffaf3c5baa", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    手绘拍摄器  = EffectMeta("手绘拍摄器", False, "6997608849750364708", "1225274", "4bf0e18f35a6ce0778455fdce692415d", [])
    手绘边框_II = EffectMeta("手绘边框 II", False, "6723044276625740296", "635101", "28cf85153cd70aa39187c96a74dd82e1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    扫描光条    = EffectMeta("扫描光条", False, "6798379345783034382", "703271", "6b14aef1e0c5759061bc35cbf33ccd9f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    抖动        = EffectMeta("抖动", False, "6706773500796867084", "634759", "950894d4ae28d859d9b7136a73265ee6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
    """
    折痕        = EffectMeta("折痕", False, "6810944968396378638", "703227", "3f7adc8176999d58e232b5fa456088d5", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    折痕_II     = EffectMeta("折痕 II", False, "6925250879259939336", "1032270", "4efd4758f897b1d364549a688129e5d5", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    折痕_III    = EffectMeta("折痕 III", False, "6925288456943833608", "1032322", "7d4cb9c576864bc421faa8d9d2f4d67e", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    折痕_IV     = EffectMeta("折痕 IV", False, "6925288650011841031", "1032321", "b04966da3a2bbd9212aec61aaa995c33", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    折痕_V      = EffectMeta("折痕 V", False, "6925292438391099912", "1032418", "1530211bc181cd4003243fa6265574db", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    报纸_今日热门= EffectMeta("报纸:今日热门", False, "6711575336955417095", "635091", "d10a4d42b6b91f3f899a1692bddfca08", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    摇摆        = EffectMeta("摇摆", False, "6709706542674874888", "634743", "bb8e9483313416d32bea215d57855490", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    摇摆_II     = EffectMeta("摇摆 II", False, "6821460674577699342", "717392", "332436443a8cbe9014d6bf7c8531ff60", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    撒星星      = EffectMeta("撒星星", False, "6839514681044898311", "768182", "620d63550356df332ba5c014b310d6d2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    撒星星_II   = EffectMeta("撒星星 II", False, "6849588023714124295", "788728", "5c5349039a938e2348ae58a7dee34302", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    撕纸涂鸦边框= EffectMeta("撕纸涂鸦边框", False, "6969851947306193416", "1153996", "592359a5945a5723aa7ed8b50e8b5ef4", [])
    播放器      = EffectMeta("播放器", False, "6758630566578360845", "635141", "187409b4bd22026b48df1bacdf2f3cfa", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    播放器_II   = EffectMeta("播放器 II", False, "6792819149945967111", "635139", "38b3630f57f017191fb1d1bbbf9185f1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    擦拭开幕    = EffectMeta("擦拭开幕", False, "6841459176510591496", "773560", "6725bf6b227fc208a7bd343661637320", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    放大镜      = EffectMeta("放大镜", False, "7051836120224502308", "1520514", "5f89a973e9cea025690bdb37a293a959", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
    """
    放映机      = EffectMeta("放映机", False, "7067049946049942030", "1576250", "a8bffa5b39a0ff0c1cdc278216e5041d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.339, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.34, 0.00 ~ 1.00
    """
    放映机卡顿  = EffectMeta("放映机卡顿", False, "6706773499031081483", "634775", "53f4a563209223baecaaec2cfff02afe", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    放映机抖动  = EffectMeta("放映机抖动", False, "6771320983065203213", "634787", "3d7d53f809b52f7370380f358ef6081c", [
                              EffectParam("effects_adjust_range", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.25, 0.00 ~ 1.00
    """
    放映滚动    = EffectMeta("放映滚动", False, "6970890075907297806", "1155966", "d29c13ced2fda5dca2a486dc9d5b1c6f", [])
    故障        = EffectMeta("故障", False, "6707050322696606222", "634797", "ec4f1908b716eec1e47b48b9c1ac836f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    故障_II     = EffectMeta("故障 II", False, "6738265357825348103", "634795", "d4435f333055899ab5140a4cc69aced6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    故障读条    = EffectMeta("故障读条", False, "6912013942097187336", "999316", "1ae904081a2d916d6d893e538304494c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.620, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.62, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    文字闪动    = EffectMeta("文字闪动", False, "6886710931150082573", "949372", "417b001671b78236d47f16351c7fff85", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    斑斓        = EffectMeta("斑斓", False, "7072258619646939679", "1607458", "7030b50aec89e949ea9ce706cfb1512c", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.040, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.04, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    斜向模糊    = EffectMeta("斜向模糊", False, "6871185301071467015", "920936", "7865be92e2a2b811cea9639d08dab0c0", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.25, 0.00 ~ 1.00
    """
    方形取景器  = EffectMeta("方形取景器", False, "6706773499031097868", "635099", "23af10c231cf1b88104e206ca5b6d9ad", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.660, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    方形开幕    = EffectMeta("方形开幕", False, "6729055410835165708", "634043", "c216a88587da0864bfe1f477f2fd1880", [])
    旋转方块    = EffectMeta("旋转方块", False, "7041504567648850445", "1482636", "d41b7b274f570518ad7aedb88e7b687e", [
                              EffectParam("effects_adjust_size", 0.714, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.71, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.25, 0.00 ~ 1.00
    """
    日式DV      = EffectMeta("日式DV", False, "6965747262165094942", "1146392", "2ba4db88748088d60090705ab0d921fd", [])
    日文字幕    = EffectMeta("日文字幕", False, "6858954575701873160", "881783", "1943875bfc98f928d2d60ac63c1a7271", [
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    日落灯      = EffectMeta("日落灯", False, "6920147678248571406", "1020046", "0a5d6dc144c4a488cc223c14ef092d05", [
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.560, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.610, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.640, 0.000, 1.000)])
    """参数:
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.56, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.61, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.64, 0.00 ~ 1.00
    """
    时光碎片    = EffectMeta("时光碎片", False, "6971332934288544286", "1157058", "97a217ce3f6f5c8a4729912f1b77ec23", [])
    时间停止    = EffectMeta("时间停止", False, "6948722700286169631", "1095262", "dce8f128927e797533d59dc0b1fb6c7d", [])
    星光        = EffectMeta("星光", False, "6717433583289504268", "634117", "18ca299d377f85452542449185ccdcd9", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星光_II     = EffectMeta("星光 II", False, "6715209934738297358", "634113", "c0629f8eb980bc1cc9853fd15fcb49cd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星光绽放    = EffectMeta("星光绽放", False, "6760243564598268420", "634195", "af1fc6a5b22f4357b4f86ad314510851", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星光闪耀    = EffectMeta("星光闪耀", False, "6967255188730024455", "1146750", "3650ba757a4c5be9accd956d8dd47df1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星光闪闪    = EffectMeta("星光闪闪", False, "6871055398107877902", "920549", "6fe220ca67a2f626ffd888b28172bc29", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星夜        = EffectMeta("星夜", False, "7008149210159649294", "1364164", "1c75b4cf948ba65efeb1af5a25b41a7e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星星冲屏    = EffectMeta("星星冲屏", False, "6769007480652435982", "634193", "52685a9660f7ddc2e9223f437485f4b2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    星星坠落    = EffectMeta("星星坠落", False, "6783598688624185867", "634269", "9dbbc7ce4806c9b7cfbb722cd4c7a9d4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星星投影    = EffectMeta("星星投影", False, "6826530141586330120", "741906", "cfbf1b6be6d23e3575caf3a026f54082", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星星灯      = EffectMeta("星星灯", False, "6903072502369489422", "977478", "9a20a02448ef8d95a81c3b16ca881742", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星星闪烁    = EffectMeta("星星闪烁", False, "6778285088485413384", "634215", "f75821b85d4f8e7be6eb42ca17f2e343", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星星闪烁_II = EffectMeta("星星闪烁 II", False, "6834010357728547335", "755806", "469b87318cdd87cefbb54223cd4633fd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星星闪烁_III= EffectMeta("星星闪烁 III", False, "6871167583991632391", "920916", "ccdcf8be8c2d54b0c029ece6f85e4d51", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星月童话    = EffectMeta("星月童话", False, "6967255330958873124", "1146749", "310fe4000e5635f13ec28570736b60e3", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星河        = EffectMeta("星河", False, "6734498838410695175", "634265", "5d1c03757b50feee9ef6bb4ac4d4d99c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星河_II     = EffectMeta("星河 II", False, "7010648091049071135", "1372810", "2273947aec8664bd5c7a0f410c8bebfb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    星火        = EffectMeta("星火", False, "6715209198109463054", "634103", "c2811a4bdeb4394ae95f3aa9875dc4dc", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星火_II     = EffectMeta("星火 II", False, "6907053209173365256", "986477", "43a04949ebd13d27d7b38f5083882322", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星火炸开    = EffectMeta("星火炸开", False, "6808838081420988942", "703243", "bf25e21e5b4a025e984e2eed0a00345d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星移        = EffectMeta("星移", False, "6778284619499311623", "634267", "f1c6583c2a7227b6ccf002863fdfdf65", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星空        = EffectMeta("星空", False, "6734587005872640519", "635035", "dc11bf828dc298c85256509f24f0451d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星辰        = EffectMeta("星辰", False, "6761722814157296141", "634271", "572ed0caff4d1d4ee69b8ab9914ae69a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星辰_I      = EffectMeta("星辰 I", False, "6946113717100614158", "1087622", "3c8c6e57ebbcca08e0202a2ce489a109", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    星辰_II     = EffectMeta("星辰 II", False, "6946453051368542727", "1089758", "4776e97efe2b615622586f9eba683b81", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
    """
    星辰_III    = EffectMeta("星辰 III", False, "6948700154874565156", "1094800", "7e62c362c751a7d4bc806e5036e1ce45", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
    """
    星雨        = EffectMeta("星雨", False, "6766488666261950989", "634187", "ec147993b7ce136beccd018d179fae2c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    春日樱花    = EffectMeta("春日樱花", False, "6927185086685123086", "1041304", "0e308be06e990da9322e807a8a4b3783", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    春日边框    = EffectMeta("春日边框", False, "6942800783737885198", "1076064", "a8f4b178a0c820ab601f742ce4eb286a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    晴天光线    = EffectMeta("晴天光线", False, "6740540037563159047", "635071", "1d65a16823fdd3130901b3687f0107d0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    暗夜        = EffectMeta("暗夜", False, "6886698114258833934", "949350", "17b5b34a9580eca1b093e3b9b730b5ad", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    暗夜归来    = EffectMeta("暗夜归来", False, "7020715691355410951", "1402690", "7e0d21432508fde619dad195088275b8", [])
    暗夜彩虹    = EffectMeta("暗夜彩虹", False, "6823658782090859022", "720808", "123ffb581708c8e5df875d30fdf26b66", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    暗夜彩虹_II = EffectMeta("暗夜彩虹 II", False, "6824046488419570184", "741832", "8411467f9cf5520fdb9cc14151bef011", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    暗夜彩虹III = EffectMeta("暗夜彩虹III", False, "6824047157369115150", "741860", "3b1f50d0c90f48a42cdb0071beedb4a9", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    暗夜精灵    = EffectMeta("暗夜精灵", False, "6888573576870367751", "952536", "fd84a50ad750ae84e3b2ce62cd22a6e5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    暗夜蝙蝠    = EffectMeta("暗夜蝙蝠", False, "7021786820153184775", "1407954", "bbe314aced3bb2ab605a2c7c6b0adf93", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    暗角        = EffectMeta("暗角", False, "6723086142658318860", "634057", "ef7abad9671e2f3da7993b7673ece5fc", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    暗黑剪影    = EffectMeta("暗黑剪影", False, "6886718600233619982", "949388", "e31ade9f9b38b5721fb601ad187bb163", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    暗黑噪点    = EffectMeta("暗黑噪点", False, "7022896066559218183", "1414024", "fae125ebf95a6bb9d8a4233ea9b3dced", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.801, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
    """
    暗黑蝙蝠    = EffectMeta("暗黑蝙蝠", False, "6749064512390828548", "634179", "934fcfaf5b153a5a0fc91951b9d7d61b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    曝光        = EffectMeta("曝光", False, "6992043513365926408", "1207064", "e961c201b279f5ef164f119aa7ab2a78", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.60, 0.00 ~ 1.00
    """
    曝光降低    = EffectMeta("曝光降低", False, "6765766949382132232", "634659", "be1c0676764ee83d32b63afc46272c28", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    月亮投影    = EffectMeta("月亮投影", False, "6826529572536717837", "741892", "c71386afba5abc8a66cd05a5c21fab2c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    月亮闪闪    = EffectMeta("月亮闪闪", False, "6876339287038628359", "931823", "11d24cd11738137f080ab6b050337f8f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    月光闪闪    = EffectMeta("月光闪闪", False, "6906802979861434887", "986344", "72e1573314be95270038e193db1def8d", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
    """
    望远镜      = EffectMeta("望远镜", False, "6834012604759806472", "761578", "63e50736865f6248f87b6280c5b0d88b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    未来主义    = EffectMeta("未来主义", False, "6982870068069667365", "1185624", "5c8d55dd2769674a7c05099020ca1000", [])
    杂志        = EffectMeta("杂志", False, "6810945952451400200", "703235", "c2d0a5d79d37501fb8d49502783145e6", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    树影        = EffectMeta("树影", False, "6815830852035940872", "703215", "e94e1952adee72678c426490036dae61", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    树影_II     = EffectMeta("树影 II", False, "6820591707617235464", "719372", "068b6e28050ccaa8d0832419a0a185c4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    格纹纸质    = EffectMeta("格纹纸质", False, "6815834305084789262", "703223", "722c3de2c3639bbcaa23b0e8ff7b9486", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    格纹纸质_II = EffectMeta("格纹纸质 II", False, "6815834434726531597", "703225", "af3ab7ecf7d9e53618301ea7652027e7", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    梦境        = EffectMeta("梦境", False, "6841460732639318542", "773088", "37faa88347805d59c7d7db2e2267e0c9", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    梦境_II     = EffectMeta("梦境 II", False, "6849235870130639368", "788039", "715227fc796386820c16198a57fd5249", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    梦境_III    = EffectMeta("梦境 III", False, "6843319622385537544", "774964", "ae67e41be59533a1fa5de82ad641563a", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    梦境_IV     = EffectMeta("梦境 IV", False, "6841460608248844813", "773086", "23336e6ee5aef71cc59e7b072fede43b", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_soft: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    梦幻雪花    = EffectMeta("梦幻雪花", False, "6894208129534267912", "961480", "0d95d3c97bfac92fd5abc0f5c04431a5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    梦蝶        = EffectMeta("梦蝶", False, "6998050316528652831", "1406766", "9ec25a811ae581e20a53276af7a3b131", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    梦魇        = EffectMeta("梦魇", False, "7024080087163081229", "1419974", "b678d12a5275aa28637557b455299c5c", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    梵高背景    = EffectMeta("梵高背景", False, "6967354298275467807", "1147066", "52e5b1690a75d4e6ca88c7f18f47b7e7", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    模糊        = EffectMeta("模糊", False, "6739752823140913675", "634025", "abb0b0e8472b73a42e796086c708d216", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    模糊开幕    = EffectMeta("模糊开幕", False, "6758752103092457991", "634071", "c0827630f211d83cc2a8258ce59d8c78", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
    """
    模糊星光    = EffectMeta("模糊星光", False, "6771299961171612174", "634255", "f40e2044c0482290ab34e4db7dfdabcb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
    """
    模糊星光_II = EffectMeta("模糊星光 II", False, "6806254134619017741", "703247", "5f0825e579151faded0b25cdac27324f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    模糊闭幕    = EffectMeta("模糊闭幕", False, "6821460725517521416", "717394", "b42ba749d552dbb865daa4c0a8e8ae6d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
    """
    横向闭幕    = EffectMeta("横向闭幕", False, "6876339694825640455", "931822", "b7abe840af4f942b11e0ccda971d4df7", [])
    横纹故障    = EffectMeta("横纹故障", False, "6806254428358709767", "703269", "fbc084265465ab0db5ba8e2b3624c4d0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    横纹故障_II = EffectMeta("横纹故障 II", False, "6815093228216259079", "703267", "a9061d0f59a826dc552e96ecc38c94c4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    樱花朵朵    = EffectMeta("樱花朵朵", False, "6940448547137393159", "1069014", "3c1cb50f953aea57451da040eeade612", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    橘色负片    = EffectMeta("橘色负片", False, "6914995976608420365", "1005839", "95ddc63de88b65e1782c88c300c7e90e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    欧根纱      = EffectMeta("欧根纱", False, "7273334324106105403", "21803568", "8d6a52eab248332cc91493e8856160ad", [
                              EffectParam("effects_adjust_size", 0.300, 0.000, 0.600),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.280, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.125, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.30, 0.00 ~ 0.60
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.28, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.12, 0.00 ~ 1.00
    """
    毛刺        = EffectMeta("毛刺", False, "6709706457543086605", "634711", "08b418c92900f56a493cd0efb570f0e1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    毛玻璃      = EffectMeta("毛玻璃", False, "7031846864198570532", "1445528", "31be9d7ef329624b8b106a6a48998361", [])
    水墨晕染    = EffectMeta("水墨晕染", False, "6746486938137530884", "634101", "561b55373df7ee5e9e6f10d5cb235190", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    水彩晕染    = EffectMeta("水彩晕染", False, "6733378866686988803", "634099", "85757609b1d1f799ebf542aec9662fce", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    水波纹      = EffectMeta("水波纹", False, "6940173521905521159", "1068390", "61ab10b10def92e31b0400ac87e43088", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
    """
    水波纹投影  = EffectMeta("水波纹投影", False, "6847018706887774727", "783644", "4b0042213e23e9050cfb066f2365564b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    水滴模糊    = EffectMeta("水滴模糊", False, "6911935918433636871", "998722", "99d7b39f93c993e17cca03313041aa8d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    水滴滚动    = EffectMeta("水滴滚动", False, "6863328348920091144", "892170", "25bf851759c3c6ebdf2036ee357866d3", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    油画纹理    = EffectMeta("油画纹理", False, "6808442362314887693", "645833", "e3fc6aa919c13ff59280907da88d2bf3", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    泡泡        = EffectMeta("泡泡", False, "6806254230614053383", "703241", "060b8178d3ac554eaa0d22e04989e70c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    泡泡变焦    = EffectMeta("泡泡变焦", False, "7133105682881974821", "4118383", "84c9bae7a15dc1118072ee3ab1ddf3c2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
    """
    波纹扭曲    = EffectMeta("波纹扭曲", False, "7368745372081984035", "63865672", "c0db14b731d4f04c95332348a0488089", [
                              EffectParam("effects_adjust_sharpen", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_sharpen: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.55, 0.00 ~ 1.00
    """
    波纹色差    = EffectMeta("波纹色差", False, "6709347834690277892", "634285", "57d2f602616ff3f9ce589e2b3150e364", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    流动烟雾    = EffectMeta("流动烟雾", False, "7257495407712801317", "18648774", "ab6aa4d420ef1cf322d25b24a054a7c6", [
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.90, 0.00 ~ 1.00
    """
    流星雨      = EffectMeta("流星雨", False, "6974750495415996936", "1164794", "fa635717b7c3eeefed138087de04c267", [])
    浓雾        = EffectMeta("浓雾", False, "6751566830206194190", "635047", "b69f839d17cd1fa3ca2b67df18b95519", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    浪漫氛围    = EffectMeta("浪漫氛围", False, "6790533020215415304", "634253", "af18c87e794b96c831549e8406c8f8c5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    浪漫氛围_II = EffectMeta("浪漫氛围 II", False, "6814667933684339207", "705081", "7021b0ea7b01f0dc0be39b091c3431a2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    涂鸦切割边框= EffectMeta("涂鸦切割边框", False, "6969850948969566756", "1153998", "e477d2fe74226d0905247b351722848c", [])
    淡彩边框    = EffectMeta("淡彩边框", False, "6753512270598246925", "635117", "3da6d9d4146803479ed0b4ab840219a2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    清新绿格子  = EffectMeta("清新绿格子", False, "6966132680211567135", "1141780", "add7f1470b3da2f309c52f337722fe1b", [])
    渐显开幕    = EffectMeta("渐显开幕", False, "6722343568188379661", "634041", "a299b022ab4d7a1830ac72dce3d21d95", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    渐渐放大    = EffectMeta("渐渐放大", False, "6730912024596845063", "634067", "56b46f1ebc45c47730d3f7c2569200fc", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.660, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    渐隐闭幕    = EffectMeta("渐隐闭幕", False, "6723050814006366734", "634039", "05c17ac3298c0521cd91a720850a27de", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    温柔细闪    = EffectMeta("温柔细闪", False, "6995497812221760030", "1220300", "90a28bc4dcde319ec961b8f07a81c817", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    游戏界面    = EffectMeta("游戏界面", False, "6983877697524994567", "1187140", "79fc508b1d127dc744a0b6bf9d63c8ea", [])
    满屏问号    = EffectMeta("满屏问号", False, "6950902993294201358", "1101078", "168794f69f32cdb6011ebca4b5bf3382", [])
    漏光噪点    = EffectMeta("漏光噪点", False, "6810944598874001934", "703229", "2e08fe198f1c351fb6d19ded110a5a84", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    火光        = EffectMeta("火光", False, "6748623656181568011", "634167", "8ae6b74e205a7ba0e3fcd3f01e93b72d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    火光刷过    = EffectMeta("火光刷过", False, "6803160938603090440", "705085", "94e472584aebf6d8fe65675b50184165", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    火光包围    = EffectMeta("火光包围", False, "6803162714148442632", "705033", "3d4fa21f005a3526c2f3189f29c03d0a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    火光翻滚    = EffectMeta("火光翻滚", False, "6809889314860700173", "703263", "b613ef50916282ef8dca4babe5d1006d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    火光蔓延    = EffectMeta("火光蔓延", False, "6803162375148016135", "703265", "eca67ce53f0d86e643af3dc6de2b8a0a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    灵魂出窍    = EffectMeta("灵魂出窍", False, "6706773500784284172", "634709", "7cd3e52c6ee775c334f44bec43b54325", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    炫彩        = EffectMeta("炫彩", False, "6732693992225378828", "634091", "c58f672e5d95a2ee49b3659006871671", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    炫彩_II     = EffectMeta("炫彩 II", False, "6933131104274616840", "1145374", "bd0e205c7b587098dbea50d4404ab314", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    烟花        = EffectMeta("烟花", False, "6782461740274684424", "635073", "4e7301f2c6232050b71d95e750d67861", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    烟花_II     = EffectMeta("烟花 II", False, "7010666068997837342", "1373018", "4037759ec478f5a033d160f1bab07f90", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    烟花_III    = EffectMeta("烟花 III", False, "7052201781241057805", "1522424", "5d6d7516368c1dcdfb2bb274c2600416", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
    """
    烟雾        = EffectMeta("烟雾", False, "6733145063997575694", "634145", "f7e8f3aee8e513dc63a56c43f58b0287", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    烟雾炸开    = EffectMeta("烟雾炸开", False, "6804317747351130638", "703261", "c4687b9722a4e7299039fd06f7956742", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    爆炸        = EffectMeta("爆炸", False, "6740540228194275844", "635067", "7b4df7ff18f6e6ccb1b49bf58611499e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心Kira    = EffectMeta("爱心Kira", False, "6896058666357625351", "965696", "74a62663b998596eb7f11485d8518b17", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    爱心bling   = EffectMeta("爱心bling", False, "6709706255105004045", "634133", "182cd7556ffdc70c9a8fdb98947f9d8c", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    爱心光斑    = EffectMeta("爱心光斑", False, "6709706178340852236", "634135", "58c897c26fa3df544d100541167c02b8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心光斑_II = EffectMeta("爱心光斑 II", False, "6791647108974776839", "634261", "85619b11f963ebd32b545b069cd75221", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心光波    = EffectMeta("爱心光波", False, "6746014633942848007", "634191", "6d42bba28607f45ca90a7359b7c6ab74", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    爱心啵啵    = EffectMeta("爱心啵啵", False, "6924869659476890125", "1031295", "dce0f289716b6e4c4c7256a4ab364188", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心射线    = EffectMeta("爱心射线", False, "6805099653730669070", "703257", "d75a8189380e55c63785b24d8050f9c6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    爱心投影    = EffectMeta("爱心投影", False, "6828020234876621325", "741958", "7515290b9cb341d5816bc502bafaabab", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心方块    = EffectMeta("爱心方块", False, "7041103714647544334", "1480898", "076a41421bbc4a6419fcccdc3c1ce80c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.634, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.63, 0.00 ~ 1.00
    """
    爱心暗角    = EffectMeta("爱心暗角", False, "6925342127807271431", "1033842", "1991e877ef3ba32d48bcbe62a2e326cb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    爱心气泡    = EffectMeta("爱心气泡", False, "6792405144655893005", "634235", "3b6d673988e3e82046b3159f59a5c12a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心泡泡    = EffectMeta("爱心泡泡", False, "6886709503136371207", "949386", "bc428e7342600fc4cf0daa1515f3aac6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心爆炸    = EffectMeta("爱心爆炸", False, "6855563744123032071", "824444", "39dfc6d5b4e0a4fa623d5d5e959c4095", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    爱心缤纷    = EffectMeta("爱心缤纷", False, "6790534436153725448", "634259", "5cd7d926814e4c5b6baca975bf3f8a80", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心缤纷_II = EffectMeta("爱心缤纷 II", False, "6792092999468716558", "634257", "d7391e2297dbeea1409bd53de6f2064e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心跳动    = EffectMeta("爱心跳动", False, "6790547496394297863", "634275", "68b31593ac0e5c661e1d610ce540d64b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    爱心跳动_II = EffectMeta("爱心跳动 II", False, "6858138763290219021", "875970", "e246526e1234846c538b718d4be7dbf2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    爱心闪烁    = EffectMeta("爱心闪烁", False, "6792109800135070222", "634231", "e8eb70ffb513761efe8662314e411974", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    牛皮纸关闭  = EffectMeta("牛皮纸关闭", False, "6966139059194303013", "1140082", "f2fb4e0bf0ea133b39eb068152acce74", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    牛皮纸打开  = EffectMeta("牛皮纸打开", False, "6966136913010889223", "1140078", "bc67263387f709f884b84337e67fe6d6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    牛皮纸边框_I= EffectMeta("牛皮纸边框 I", False, "6966139444382405134", "1140086", "db111daab71339846516a5c01402752e", [])
    牛皮纸边框_II= EffectMeta("牛皮纸边框 II", False, "6966139579912950286", "1140085", "e91bd852184f4ac248f6291a4c8d1826", [])
    玫瑰花瓣    = EffectMeta("玫瑰花瓣", False, "6734619627051028996", "635051", "abd9d7c89fa42048f1ad1fe68b867ba0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    玻璃破碎    = EffectMeta("玻璃破碎", False, "6912015453892121102", "999326", "cb76d83cf3c3b3674b2207c33bcaf67d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    甜心投影    = EffectMeta("甜心投影", False, "7058961500060258847", "1552216", "24068e8b49b64d8802e7d62ca05acc07", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.435, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.44, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
    """
    生日快乐    = EffectMeta("生日快乐", False, "6899747371593241096", "972748", "7e2e3e9671c48ebdd4abf0f8efa0b3eb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    电光包围    = EffectMeta("电光包围", False, "6809889225144537613", "703259", "41db536d57ca3c1d547f13b658c2386d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    电光漩涡    = EffectMeta("电光漩涡", False, "6797341815377760782", "634975", "363d8c0772a4e49a3f51f233748dd86b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    电子屏      = EffectMeta("电子屏", False, "6847692508449739278", "785074", "7e3720dced915006968402e0f245f955", [
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    电影刮花    = EffectMeta("电影刮花", False, "6722366799003783692", "634789", "10c7d224fcc46291509c22a902efeb6e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    电影感      = EffectMeta("电影感", False, "6719333680713568771", "634029", "1beeb560b0796fc181f265df1e83fa66", [])
    电影感画幅  = EffectMeta("电影感画幅", False, "6746135410218373646", "634083", "f37cf7f307b394d1d496d5264c7b2a86", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    电脑桌面    = EffectMeta("电脑桌面", False, "7026619341839798820", "1482288", "1625f25739fdc13d63b9867589929cae", [
                              EffectParam("effects_adjust_color", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    电视关机    = EffectMeta("电视关机", False, "6719656840646365707", "634805", "c2ef989d8286f4b2e5a747bca129602a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    电视开机    = EffectMeta("电视开机", False, "6719661856434164237", "634807", "b7f303766220a86078204b79a4db2566", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    电视彩虹屏  = EffectMeta("电视彩虹屏", False, "6852503085672043021", "815546", "d6ef86b7e37c1996e336d6541f5c4d7a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    电视纹理    = EffectMeta("电视纹理", False, "6763933311933878791", "634803", "12829eb28e30b3c046bcb9ce3fdd8641", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
    """
    画展边框    = EffectMeta("画展边框", False, "6839527903424680456", "768176", "594fd22d6effa8153b7a619746b1dd0f", [])
    白噪点边框  = EffectMeta("白噪点边框", False, "6970599572976439839", "1155426", "ffe0f3ffa043687873060dabb41e45ac", [])
    白胶边框    = EffectMeta("白胶边框", False, "6865979592264389127", "898956", "77fb2991364f2882ef4b61317f7a10dc", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    白色描边    = EffectMeta("白色描边", False, "6953169122649707045", "1107244", "647776c50dafcbfab55f1dcb36d28792", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    白色渐显    = EffectMeta("白色渐显", False, "6723790385069429262", "634037", "94b1df840d30218f14e8a5e509df5c8e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    白色爱心    = EffectMeta("白色爱心", False, "6868556923503907342", "904792", "6fbffdaff4f4a6f3894af0a29f5fe8cc", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    白色线框    = EffectMeta("白色线框", False, "6753512551536923149", "635109", "66d6c8dffd954669fbb74410f28ac6c0", [])
    白色边框    = EffectMeta("白色边框", False, "6974602583411266079", "1164159", "799ac5c78fddad12e395047e180f4328", [])
    百叶窗      = EffectMeta("百叶窗", False, "6823654892872143367", "719380", "bde8d2cb9d033a45c92615f9b18b47a1", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    百叶窗_II   = EffectMeta("百叶窗 II", False, "6823656768334205454", "719404", "380df1dbfbfb93a560b389d5683043e7", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    监控        = EffectMeta("监控", False, "6773542922030682632", "634941", "82748b8ee1cc9a6619aa3571c5e59183", [
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
    """
    盗梦空间    = EffectMeta("盗梦空间", False, "7024053604596060680", "1419276", "ab8caff5408905d424c23bef34af0853", [
                              EffectParam("effects_adjust_size", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
    """
    盛世美颜    = EffectMeta("盛世美颜", False, "6860757421283873293", "886130", "16d39197cd79d2753ce8c58f409c78a2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    相机网格    = EffectMeta("相机网格", False, "6725730715138265612", "634051", "7569da277fd0c96d1a8ab45a024baa96", [])
    相纸        = EffectMeta("相纸", False, "6713856991086776835", "635093", "14d50603fdd87a40a787e71172901a56", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.70, 0.00 ~ 1.00
    """
    瞬间模糊    = EffectMeta("瞬间模糊", False, "6903409009210954253", "979300", "811854906cb966498a38302cf5474be2", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    破冰        = EffectMeta("破冰", False, "7047049192832766477", "1499079", "35814c493387bfc7af1eadf958e28d71", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    磨砂纹理    = EffectMeta("磨砂纹理", False, "6732693826135134734", "634027", "4ea2d570ea1d66a407d6973006c199a0", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    祝福环绕    = EffectMeta("祝福环绕", False, "7324617866056045106", "40453164", "f04f5974c31731224645e5d0374e3e04", [
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("sticker", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - sticker: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.40, 0.00 ~ 1.00
    """
    秋日暖黄    = EffectMeta("秋日暖黄", False, "7005090271696261640", "1352364", "962a7be1764e7dcdb8ab54198a6bde14", [])
    空灵        = EffectMeta("空灵", False, "7021096050899292680", "1404120", "c0bbb93750bb7fe5b9b2900ff853adb6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    窗格        = EffectMeta("窗格", False, "6719656757175521800", "634781", "6c832fb174c39c2c7f8af853987e89e4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    窗格光      = EffectMeta("窗格光", False, "6823659309428118030", "719378", "6bd27e2b68879bb788d7ef0265648795", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    简约边框    = EffectMeta("简约边框", False, "7039329234170417701", "1475188", "a130a890772cc684fc987dcf2ec22124", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    箭头放大镜  = EffectMeta("箭头放大镜", False, "7067461440960991752", "1579942", "e0540ac533119123deb057f99419b6dc", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.00, 0.00 ~ 1.00
    """
    粉红老电视  = EffectMeta("粉红老电视", False, "6839596824936845838", "770876", "10efcbd56eb7d9dd9cea22bb55bf443c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    粉红芭比边框= EffectMeta("粉红芭比边框", False, "6986591867999621668", "1193772", "3500630cec44ef4028af9ea40b325c99", [])
    粉色闪粉    = EffectMeta("粉色闪粉", False, "6858953149974057486", "881784", "e0294c868dacfeb1f83c406d4e21e121", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    粉黄渐变    = EffectMeta("粉黄渐变", False, "7008413208721494559", "1365502", "36f666ce547c61a8bbe9fc634cb79b69", [])
    粒子模糊    = EffectMeta("粒子模糊", False, "6730841158806671886", "634031", "d411df8e887895dbae6904e8c25d6c51", [
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    精灵闪粉    = EffectMeta("精灵闪粉", False, "6967274435963261476", "1146790", "4a4d26ee6fcb0a71ee15666b8864498f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    精细锐化    = EffectMeta("精细锐化", False, "7250368600911909413", "16609879", "df34b01300ddefbfd8b04bee900ae432", [
                              EffectParam("effects_adjust_blur", 0.120, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.080, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.12, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.08, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    糖果纸      = EffectMeta("糖果纸", False, "6782100631638249998", "634217", "37ae35224ded86cd0e5d5bc2d58e3cc8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    紫色波纹    = EffectMeta("紫色波纹", False, "6987321998036701704", "1195758", "4e80d6d461e093799fa7ce721d7dbd89", [])
    紫色负片    = EffectMeta("紫色负片", False, "6915313694884762125", "1007834", "a21c94f366e16f2aa8bd9e491ec226c5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    紫雾        = EffectMeta("紫雾", False, "6886335679681270279", "948716", "bf106ce53d50ff0a7ebabe323a69b097", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    繁星点点    = EffectMeta("繁星点点", False, "6839577027939406344", "768166", "5342526311c51bc957c5abc25b2f5280", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    纵向开幕    = EffectMeta("纵向开幕", False, "6876338988437737997", "931824", "d75e138469226782f6d918983725d700", [])
    纵向模糊    = EffectMeta("纵向模糊", False, "6716684911840858628", "634137", "39d1ffded922746f7e09b925798a2f1a", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    纸膜边框_I  = EffectMeta("纸膜边框 I", False, "6981464043542286879", "1181888", "d76f129d3e1a3c4a0350a6537c382c13", [])
    纸膜边框_II = EffectMeta("纸膜边框 II", False, "6981464169736311327", "1181886", "b95690afb9846aeacdfccd0cb05cef27", [])
    纸质撕边    = EffectMeta("纸质撕边", False, "6843686214025875981", "784032", "fd5588f68a681b8eba1449a5d0240097", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    纸质边框    = EffectMeta("纸质边框", False, "6844765419853582856", "780656", "554d4d330b4d17f0b404e598a66f05c9", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    纸质边框_II = EffectMeta("纸质边框 II", False, "6844832937272152589", "780658", "b3fbce0bfe68298555ab18ed39fc817a", [])
    细闪        = EffectMeta("细闪", False, "6847773569435308558", "785536", "9f35060cd9e36abab8c5ebb80d8efbf6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    细闪_II     = EffectMeta("细闪 II", False, "6893002658420888078", "959412", "186c623a413a10ddbf28bfa0215a55f4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    细闪_III    = EffectMeta("细闪 III", False, "6963598424113418783", "1134290", "432b12f72fe1b0f081dc292bc415dbb0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    美式        = EffectMeta("美式", False, "6849214832856535560", "787752", "d3c405c7369854dd009dd63f6a4b2b46", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    美式_II     = EffectMeta("美式 II", False, "6843320153900323335", "774972", "cd7423d39d5a115fc4d5d7f5db43658c", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    美式_III    = EffectMeta("美式 III", False, "6843319785522991623", "774968", "d936f602060a9b010a261e85166b5a14", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    美式_IV     = EffectMeta("美式 IV", False, "6850006476472193543", "812078", "0bddd63da76f2f117140ff240c57daee", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.620, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.62, 0.00 ~ 1.00
    """
    美式_V      = EffectMeta("美式 V", False, "6849225862588404237", "787968", "26f287cc23166dc878589197c5800842", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    美漫        = EffectMeta("美漫", False, "6981339244547543560", "1181360", "d17c9fedb83124be5b0f758d90eea0be", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    羽毛        = EffectMeta("羽毛", False, "6709706658815152643", "634295", "135a9b19d3a4d08dfdd5bb1c9eabbfec", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    老照片      = EffectMeta("老照片", False, "6815764475375784462", "703231", "140119b43a843a5732e5b4064a58576e", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    老照片_II   = EffectMeta("老照片 II", False, "6815767788490068494", "703233", "25921facf51181e20ad0947556517792", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    老照片_III  = EffectMeta("老照片 III", False, "6813924503148564999", "719374", "e199463a70a8b3840f248dbc9fac6769", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    老电影      = EffectMeta("老电影", False, "6706773498506777095", "635095", "3ffab78abca09b413e5b7178511f903d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    老电影_II   = EffectMeta("老电影 II", False, "6865921078858879496", "898674", "62b508cb16fd1c0da7a2989da5bd49fd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    老电视卡顿  = EffectMeta("老电视卡顿", False, "6706773499052036615", "634771", "da767092b3d91fa36fae380e90f11cdd", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    聚光灯      = EffectMeta("聚光灯", False, "6750075966053159427", "634081", "49c61bf16894adb9926b79d18993c3bd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    聚焦        = EffectMeta("聚焦", False, "6710056993287049742", "635083", "97b20e018b0bdd4ff12025b5358a6e81", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    胡言乱语    = EffectMeta("胡言乱语", False, "6951364520048595492", "1102990", "2b069d3c512bb55aa56b9837d6244eee", [])
    胶片        = EffectMeta("胶片", False, "6708624565657932292", "635097", "c85a5c6d8841e2e6dd65813cbe60505c", [
                              EffectParam("effects_adjust_noise", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    胶片_II     = EffectMeta("胶片 II", False, "6710090540643258891", "635087", "9c4e00c766b4fd4f603bed3a720397b9", [
                              EffectParam("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_chromatic: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.55, 0.00 ~ 1.00
    """
    胶片_III    = EffectMeta("胶片 III", False, "6841053178406900231", "773562", "2413a56c73f8432072f1cf4429648193", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    胶片_IV     = EffectMeta("胶片 IV", False, "6896439221179912718", "966552", "9f76eb0fd12192188a8ace928de37416", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    胶片抖动    = EffectMeta("胶片抖动", False, "7075213848558440990", "1625760", "86c6710992682fa9d51b9bfea52d2b47", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
    """
    胶片显影    = EffectMeta("胶片显影", False, "6830336944111620616", "744244", "a09195689037df58fd23db7f28d3a2b6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_soft: 默认1.00, 0.00 ~ 1.00
    """
    胶片框      = EffectMeta("胶片框", False, "6974600629268255262", "1164161", "393b58c3e98a33f92ea16ac611919909", [])
    胶片框_II   = EffectMeta("胶片框 II", False, "6974600475999998477", "1164162", "fd84488800ef5683555188564886ab76", [])
    胶片框_III  = EffectMeta("胶片框 III", False, "6987714956401578510", "1196596", "d0169ca7d23e5196df0e4604bcfbe2c1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    胶片漏光    = EffectMeta("胶片漏光", False, "6815093106841489934", "705083", "179080155bccbfd7ddf7e37137eb2747", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    胶片漏光_II = EffectMeta("胶片漏光 II", False, "6814743838964322829", "718872", "0a0b12f5a4e442871708fcbf14fdec5d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    胶片连拍    = EffectMeta("胶片连拍", False, "6994787976613990925", "1218011", "cb017def5c29fc1af5de0041469d4ff4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    自然        = EffectMeta("自然", False, "6843319885339038216", "774970", "b692892ba55b4cbd18c97704102b9938", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    自然_II     = EffectMeta("自然 II", False, "6841460795394494990", "773090", "7196a6d5e3b895f781a453e70abb971a", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    自然_III    = EffectMeta("自然 III", False, "6843680748856152584", "775998", "6d80537f452debf98b09f2df79080e37", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    自然_IV     = EffectMeta("自然 IV", False, "6843680812584407559", "776000", "29800968f49ad39520d47e999024becb", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    自然_V      = EffectMeta("自然 V", False, "6843319715499086343", "774966", "6ff4d109673eb689778b2be2f5af1c3e", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    色差        = EffectMeta("色差", False, "6706773498561303044", "634059", "737c54ea0dcf628cc78714a77eef52a3", [
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    色差开幕    = EffectMeta("色差开幕", False, "6868546720783929870", "904723", "fc98a601f63bacc514067ecfa2849137", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
    """
    色差放大    = EffectMeta("色差放大", False, "6883360769992299016", "945036", "894bef97217ae4bab59ae710228bdf40", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
    """
    色差放射    = EffectMeta("色差放射", False, "6716422405511713287", "634777", "85706adda9a242bbb6dc2c3da2542ba1", [
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.55, 0.00 ~ 1.00
    """
    色差故障    = EffectMeta("色差故障", False, "6706773498922013191", "634773", "6ee1a1ab0be0849602a3c983a025c47a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    色差故障_II = EffectMeta("色差故障 II", False, "6706773498561319428", "634769", "638565d68ac2845eb2c552497efec3d8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    色差星闪    = EffectMeta("色差星闪", False, "6904921853635072520", "982304", "c13d9ca825a2adb976c429456af2ead0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    色差默片    = EffectMeta("色差默片", False, "6719362972239532548", "634793", "82cc4ec1b530fc13e1af9be9e4b63c4f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
    """
    节日彩带    = EffectMeta("节日彩带", False, "6907438556793278983", "987446", "47ca5466c833a9287af563c9890f8159", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    花火        = EffectMeta("花火", False, "6767147410671014407", "634223", "4e7b79927a6067a2080ce6b61da8faf9", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    花火_II     = EffectMeta("花火 II", False, "6907051960180937229", "986478", "8a3f34e4c9650409a8aa6059f8610e14", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    花瓣飘落    = EffectMeta("花瓣飘落", False, "6796905369932141064", "635059", "a772c059e7fb8304292e7ebb870e8eb3", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    花瓣飞扬    = EffectMeta("花瓣飞扬", False, "6796903619762328072", "635057", "24c3c52fe9d54c8677ee514c0530528c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    荡漾_II     = EffectMeta("荡漾 II", False, "7140929198763282980", "4493526", "7a08a3c5aa067e55cd0f638cd3161a1b", [
                              EffectParam("effects_adjust_range", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.350, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.35, 0.00 ~ 1.00
    """
    荡秋千      = EffectMeta("荡秋千", False, "7388040405465436722", "73935190", "bee293df8d3c2a62e722c60eca82aab3", [])
    荧光扫描    = EffectMeta("荧光扫描", False, "7041474808986472967", "1482382", "4c6263913593bbf1fc06f01e8c3fcf8b", [
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    荧光爱心    = EffectMeta("荧光爱心", False, "6792095053360665096", "634227", "b9b9be20aed7761f81c6757a4428a034", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    荧光线描    = EffectMeta("荧光线描", False, "6795826477590909454", "634945", "d393537113a37c7cff64101d0e042a87", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    荧光绿      = EffectMeta("荧光绿", False, "6858138988834722312", "875968", "7cbaffedca388899dec7c7219592074c", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    荧光蝙蝠    = EffectMeta("荧光蝙蝠", False, "6886339116561076749", "948715", "ad61d53ca404616d198bc766e6c64df8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    荧幕噪点    = EffectMeta("荧幕噪点", False, "6706773534066086413", "634779", "f090492c306fe35f917eed1216f14f8c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    荧幕噪点_II = EffectMeta("荧幕噪点 II", False, "6803161742789579277", "703253", "53ff3188476c74715a73aa34f08a1edf", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    萤光        = EffectMeta("萤光", False, "6715209844216828420", "634107", "59a3ea0709d076e3043555a7d5d40945", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    萤光飞舞    = EffectMeta("萤光飞舞", False, "6877098783209951751", "932242", "d34177a4c2caf9581e67b0206cf6a919", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    萤火        = EffectMeta("萤火", False, "7006265184050221576", "1357502", "d473ca7fa127312a7651ec1523a6e880", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    落叶        = EffectMeta("落叶", False, "6740863535674298888", "635043", "5e8db93a52a15e7254dc7e1c115c145c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    落樱        = EffectMeta("落樱", False, "6924859706661933576", "1031296", "7372d9708980266944aec9650ccde843", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蒸汽波      = EffectMeta("蒸汽波", False, "6719658860539286020", "634147", "08d620dca82aea6bf5d71d48ba4a6b3d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    蒸汽波投影  = EffectMeta("蒸汽波投影", False, "6830351103272423949", "747926", "83c74d3a0dd8f6d11d3cc3063f1eadfa", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蒸汽波路灯  = EffectMeta("蒸汽波路灯", False, "6829184472349413895", "755808", "564a4710d8ece86ade31f9eee89deb01", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蒸汽腾腾    = EffectMeta("蒸汽腾腾", False, "6894200076227318286", "961482", "f852e42917f0ea29be56bbb12891c920", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蓝光扫描    = EffectMeta("蓝光扫描", False, "7254126209540297274", "17710554", "5f9918f9606b3dfbb8e8c8b7b90ca0e3", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
    """
    蓝线模糊    = EffectMeta("蓝线模糊", False, "6920136330563293704", "1019968", "770dd5360aa3cfc96d97738f62627957", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    蓝色负片    = EffectMeta("蓝色负片", False, "6914996050382033421", "1005838", "c40c9ca0a5c2ea1a22c54a3dc943b3de", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    蓝色闪电边框= EffectMeta("蓝色闪电边框", False, "6989911842575356446", "1201878", "f69acdd1cea097f4db0bf01ed015559b", [])
    虚化        = EffectMeta("虚化", False, "6756397840785740295", "634065", "5b22f93757ce6807874cc5e1530db8b3", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    蝙蝠Kira    = EffectMeta("蝙蝠Kira", False, "6888977985697747463", "953420", "408ee7831b71cbae827138898d26c934", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
    """
    蝴蝶        = EffectMeta("蝴蝶", False, "6706773499836404228", "634157", "559a055318e1a9940281c8eb31954ee9", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蝴蝶_II     = EffectMeta("蝴蝶 II", False, "6747586717672280584", "634155", "014a7aa25087ad6a6bfa14ca6146bedd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蝴蝶光斑    = EffectMeta("蝴蝶光斑", False, "6748307256959308299", "634183", "45377639fc1c0b29cc889f71f6ca2fd0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蝶舞        = EffectMeta("蝶舞", False, "6747946665312784910", "634177", "b6c530af2bd744d77df4d5b70e3497f8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    表面模糊    = EffectMeta("表面模糊", False, "7244073793562350140", "15249743", "8629e4a00fdb51b73c98842bc7a6f0c5", [
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.70, 0.00 ~ 1.00
    """
    裂开了      = EffectMeta("裂开了", False, "6944914067702157861", "1082654", "48084a37dbea8252814a0d96520dcaee", [])
    视频分割    = EffectMeta("视频分割", False, "6729023693739004419", "634747", "a9338d60042f719860346409954ed387", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
    """
    视频界面    = EffectMeta("视频界面", False, "6752799091941446147", "635135", "ecbdf02c28278b4436c1dfaf3b733650", [])
    诡异分割    = EffectMeta("诡异分割", False, "7021800634621891109", "1408118", "2755d9f7c9b46356a832ef58ef405df7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.630, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.63, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.70, 0.00 ~ 1.00
    """
    负片闪烁    = EffectMeta("负片闪烁", False, "6863353894152442375", "892686", "ed476f61f551e99709b62ce8ed922323", [
                              EffectParam("effects_adjust_speed", 0.560, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.56, 0.00 ~ 1.00
    """
    赞赞赞      = EffectMeta("赞赞赞", False, "7057055647472292359", "1543072", "a927f8d9d6b8fcefd4671cb53455d8d5", [])
    蹦迪光      = EffectMeta("蹦迪光", False, "6716419849544798723", "634733", "5b3449fa5476bfd93851d0b4cce7b8c9", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    蹦迪彩光    = EffectMeta("蹦迪彩光", False, "6716450942285255182", "634731", "355d46c4bff8c9b6286f3324fb6e27b7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    车窗        = EffectMeta("车窗", False, "7012926200767058463", "1381596", "e16d42dbe728d95e6cdc2585a817a3e2", [])
    车窗影      = EffectMeta("车窗影", False, "6834006887415943694", "761222", "d37540d91f173eaeef40a3ac6a2de42e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    轻微抖动    = EffectMeta("轻微抖动", False, "7258208250896585274", "18798726", "b5235343ec32572db40123246a22fefa", [
                              EffectParam("effects_adjust_range", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    轻微放大    = EffectMeta("轻微放大", False, "6791743223522923021", "634077", "c09004507723569a3e762494d4ffda7d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    边缘glitch  = EffectMeta("边缘glitch", False, "6777238992816443912", "634749", "516eb9ef0e22a58d17984712a9301b23", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    边缘加色    = EffectMeta("边缘加色", False, "6781315516909752844", "634757", "1d5ac14cba4e6e8559cacd2c37d62c43", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    边缘加色_II = EffectMeta("边缘加色 II", False, "6790180635555140109", "634755", "ff84c6f908752eda1298021c2e382e0f", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    边缘加色_III= EffectMeta("边缘加色 III", False, "6901190770473046535", "974844", "91c834c21a94810977500c0f0f0d406b", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    边缘发光    = EffectMeta("边缘发光", False, "6769065553207235086", "634069", "656e16d4aff7d609ff25c2ff8abc156c", [
                              EffectParam("effects_adjust_luminance", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.25, 0.00 ~ 1.00
    """
    边缘荧光    = EffectMeta("边缘荧光", False, "6903064458008990215", "977454", "270610eeb2c6810b2cd43743033bebee", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    运动一夏    = EffectMeta("运动一夏", False, "6984393713208267301", "1188619", "c78c14c0ce8641f5de8ba5a03f8dce29", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    迪斯科      = EffectMeta("迪斯科", False, "6756113382840996360", "634739", "975bfbd37de349a6c2390576a61d243e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    迷幻烟雾    = EffectMeta("迷幻烟雾", False, "6719661667447214605", "634089", "d03e2cc41acde9dd8e3eab333c43ba2c", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    迷离        = EffectMeta("迷离", False, "6706773549362713095", "634721", "7c2f3180ded615ee30e6d1a5bafc5392", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    迷雾        = EffectMeta("迷雾", False, "6887505634791526926", "950488", "057c2404619359f8ceec96e20eee0f2f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    逆光对焦    = EffectMeta("逆光对焦", False, "6992032047959118344", "1218244", "ccba5bb5c3656e951ce7e6ec272dc606", [
                              EffectParam("effects_adjust_soft", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_soft: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.33, 0.00 ~ 1.00
    """
    选中框      = EffectMeta("选中框", False, "6712358020417851917", "635081", "f65a653528911a459a3011c647b68cf4", [])
    邮票边框    = EffectMeta("邮票边框", False, "7012988323387937293", "1382084", "f14c0b2288f110621f814c237c5471a6", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
    """
    金属背景    = EffectMeta("金属背景", False, "7044853948456374814", "1493772", "44ec1abb4102d0886e6cb4e60a80ae72", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.505, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.710, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.51, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.71, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    金片        = EffectMeta("金片", False, "6771299796058640908", "634229", "5ff7544cd83c2ec196b1acc8f47bf51c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金片_II     = EffectMeta("金片 II", False, "6924589854269379079", "1030626", "3100003d53722ae2d1e8ca0bde4a1043", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金片炸开    = EffectMeta("金片炸开", False, "6899747182816006669", "972750", "075cfd56ba9a170c62a6ad8150d4845d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉        = EffectMeta("金粉", False, "6709706378702754312", "631215", "0443a82ca7b709b643abaf8da7051cca", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉_II     = EffectMeta("金粉 II", False, "6774672940651778573", "634289", "75dc8419d6ebcca570bb85b0daeb883f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉_III    = EffectMeta("金粉 III", False, "6984393847467938335", "1188618", "752d69c565983fbed6bb13c3d8542ca7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉撒落    = EffectMeta("金粉撒落", False, "6907439016547717646", "987445", "c84cfe1f31a1a79e5a9b362bc744d3d3", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉旋转    = EffectMeta("金粉旋转", False, "7033654301050278431", "1452336", "14fd0f24372acd5be33505ee5759ca11", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉聚拢    = EffectMeta("金粉聚拢", False, "6806254339821146637", "703245", "a4d9c4c3bde58e6aa6db39fcef692108", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉闪闪    = EffectMeta("金粉闪闪", False, "7034048554318434830", "1453820", "a552dfa820b5aba27e4f09e3d83b8643", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    钻光        = EffectMeta("钻光", False, "6723824479216079368", "634097", "c9c730b13ac00e7b8b16af1d882fe31c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    钻石碎片    = EffectMeta("钻石碎片", False, "7077487066476450340", "1639618", "7c201b5477a02796bddb330377b7fce7", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
    """
    镜像        = EffectMeta("镜像", False, "6956148985400660517", "1115964", "0e68989382af0ece7e1e864cc2107c67", [])
    镜头变焦    = EffectMeta("镜头变焦", False, "6868546663607177736", "904724", "59273e718263fae7a1001c65fe44ad3a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.30, 0.00 ~ 1.00
    """
    长虹玻璃    = EffectMeta("长虹玻璃", False, "6992081595976913416", "1235644", "2f5917be32e664eef67419212e54cad0", [
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    闪亮登场    = EffectMeta("闪亮登场", False, "6760547949349966350", "634185", "a1c096efd5f98b438ab0f762bea9c41a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    闪亮登场_II = EffectMeta("闪亮登场 II", False, "6891946116212855303", "958186", "0a249f3cd35bef5ca846a49680248812", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    闪光灯_Ⅰ   = EffectMeta("闪光灯 Ⅰ", False, "6844432942563856904", "777760", "c602afac7537de506bb822c37e9f2191", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    闪光震动    = EffectMeta("闪光震动", False, "7260437169389441597", "19279654", "17416edf590446330a683c9eb4f5c9e3", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.580, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.58, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    闪动        = EffectMeta("闪动", False, "6717639344577843725", "634725", "0bc9ee34335ba4f9d75e4a2b21f4d6e5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    闪动光斑    = EffectMeta("闪动光斑", False, "6753169731617821191", "634181", "d7c42c303074967c0cad7c7a6adfe896", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    闪屏        = EffectMeta("闪屏", False, "6758298031608566280", "634729", "51b2af1e78502e00abb3d47b21a55796", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    闪电        = EffectMeta("闪电", False, "6734215409513271820", "635069", "6191fcf13bfd15e4288a81a174ba0ed8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    闪白        = EffectMeta("闪白", False, "6706773500792672781", "634761", "f0804cb2cb4e88a036ecf87dcf031cf0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    闪耀星光    = EffectMeta("闪耀星光", False, "6784346950385799694", "634219", "93c0a1e7829ec10d8502466ea74846dd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    闪闪        = EffectMeta("闪闪", False, "6869625970437919246", "909546", "293daf09b25bb116a038576ff690e698", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    闪闪发光_II = EffectMeta("闪闪发光 II", False, "7013264306959553060", "1382870", "9a723996777d5f56d3802b53c8cc46bb", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
    """
    闪黑        = EffectMeta("闪黑", False, "6863327462470717960", "892171", "383b8ace93434f0c5d17689933140422", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    闪黑II      = EffectMeta("闪黑II", False, "7221377929467400765", "12078089", "3c25ccac35121fe42e647b119e37a21f", [
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.40, 0.00 ~ 1.00
    """
    闭幕        = EffectMeta("闭幕", False, "6725685146323784205", "634035", "6a59cb9db4036a187d4b1ca3a2cab8f3", [])
    闭幕_II     = EffectMeta("闭幕 II", False, "6729065630013592067", "634033", "47ad4fe486fe97a4529998d53e5e93b3", [])
    随机色块    = EffectMeta("随机色块", False, "7026674824537707038", "1427664", "a7e3cf890d40734c1b44172eff546c41", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
    """
    随机色块_II = EffectMeta("随机色块 II", False, "7030742849134006792", "1441868", "0d5b2c847554024c4bd5dbaf06d842fb", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
    """
    随机裁剪    = EffectMeta("随机裁剪", False, "6991794787464516127", "1206444", "348f8137cc25a994e2a676a5639d3bd9", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    隐形人      = EffectMeta("隐形人", False, "7020318315310486046", "1400804", "2cf16035b605ce73f4b44bcd650adfb3", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
    """
    隔行扫描    = EffectMeta("隔行扫描", False, "6976152376457564708", "1168118", "e8349feb07866b44bbce9c9effa6f51a", [
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    雨滴晕开    = EffectMeta("雨滴晕开", False, "6792488562869670414", "635041", "2bded973503eaa2ce5644ef44354d90d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    雪窗        = EffectMeta("雪窗", False, "7168743948528128548", "6431703", "823ecc00612b35e63837f9ce6f4f4af5", [
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    雪花        = EffectMeta("雪花", False, "7030728702258319909", "1441796", "aa711f9666bdc3e51ff72de0d7c073a8", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    雪花冲屏    = EffectMeta("雪花冲屏", False, "6769435378806952455", "634203", "2c07239e54041e85518b111b1ad8eb86", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    雪花开幕    = EffectMeta("雪花开幕", False, "6730429759425090059", "634045", "8c3a0db33fda83398b66a5a8ab64cc41", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    雪花故障    = EffectMeta("雪花故障", False, "6847689727261282824", "785064", "f24f4cebfa22bc28d74c9b30aa17f1a0", [
                              EffectParam("effects_adjust_range", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.55, 0.00 ~ 1.00
    """
    雪花细闪    = EffectMeta("雪花细闪", False, "6770604155561054734", "634201", "3eab18374e64043e209c3deac2bbe56d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    零点解锁    = EffectMeta("零点解锁", False, "6907054642123772430", "986480", "f189f93d81e1638035e229389355cc4e", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    雾气        = EffectMeta("雾气", False, "6734619830449607171", "635049", "add061ec46e4f013ed3482a6dc87c9b9", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    雾气_II     = EffectMeta("雾气 II", False, "6740539818666627588", "635045", "6e963a8a2e1fd100e7ac3d2f21100a8a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    雾气光线    = EffectMeta("雾气光线", False, "6715209712129806851", "635065", "607f77fe518da5a26e7457ea932f5ad7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    震动        = EffectMeta("震动", False, "6761645818723176968", "634075", "d11532bfbfbd6f9af59026c2c42f2570", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    霓虹投影    = EffectMeta("霓虹投影", False, "7058961173743407630", "1552220", "46a3a7dbb114d888726b1cf9a22189c2", [
                              EffectParam("effects_adjust_soft", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_soft: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
    """
    霓虹摇摆    = EffectMeta("霓虹摇摆", False, "6925387220073320974", "1034626", "f7ce2e949d495d22dab8f6a2b032a9b9", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
    """
    霓虹灯      = EffectMeta("霓虹灯", False, "6829182808485794311", "742028", "35a6f9b3c544b0f97ccbf3fea89e6010", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    预警        = EffectMeta("预警", False, "6955083255825568264", "1113432", "3dfcefd286a1684818c543e17b7d5bc6", [])
    颤抖        = EffectMeta("颤抖", False, "6863326875649839623", "892172", "7cb6c1646c43d86a394245e194e3f451", [
                              EffectParam("effects_adjust_range", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    飘落花瓣    = EffectMeta("飘落花瓣", False, "6719658795661791747", "634153", "c39b069df62f67308de64f86b920dbbd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    飘落闪粉    = EffectMeta("飘落闪粉", False, "6720029963602366979", "634165", "517bbcd8e398072ce95c0d9763c4c914", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    飘落闪粉_II = EffectMeta("飘落闪粉 II", False, "6720029866504229390", "634163", "6bd90b0f33d3722d759b0fc2d5ddc9bd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    飘雪        = EffectMeta("飘雪", False, "6732360625214722572", "635061", "8e2909d8fe6a77833f62fccf73630aa7", [])
    飘雪_II     = EffectMeta("飘雪 II", False, "6763531573594690061", "635055", "e4c07894c4f11edbbc580486b50f4b8e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    飞速计算    = EffectMeta("飞速计算", False, "6951364383477862948", "1102992", "b08f9e05c86b2e980444d336d9db7427", [])
    马赛克      = EffectMeta("马赛克", False, "6770564289074827784", "639477", "c9f3bf5b93d53bdc514be0d9c480fcf0", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    高光瞬间    = EffectMeta("高光瞬间", False, "6955021144156017188", "1113136", "7e50ea3473876ee7bbc0f9105cc6c65e", [])
    魅力光束    = EffectMeta("魅力光束", False, "6814668066882851335", "705071", "8c305048985cc4cd8236d08b716c2d16", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    魔法        = EffectMeta("魔法", False, "7000199435372204580", "1232490", "98296a4bc028cef2bb3b06ffbb490faf", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.802, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    魔法变身    = EffectMeta("魔法变身", False, "6964608751231832613", "1136674", "4ec729c610f93a85cd08b9a9474aaecf", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    魔法边框    = EffectMeta("魔法边框", False, "7020407234798555655", "1401520", "f995faa8d65405b92637e54d90d4d9a9", [])
    魔法边框_II = EffectMeta("魔法边框 II", False, "7021795690149843463", "1408090", "6f23fdea097c9e547d934e0c134cd0c9", [])
    鱼眼        = EffectMeta("鱼眼", False, "6867722963865571854", "901430", "d577e4744d29d971675ec9c71d94ca94", [
                              EffectParam("effects_adjust_distortion", 0.770, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.77, 0.00 ~ 1.00
    """
    黄蓝星芒    = EffectMeta("黄蓝星芒", False, "7000312634574639653", "1232996", "290f59cb09438e3b8681f055a9b4a967", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    黑白VHS     = EffectMeta("黑白VHS", False, "7021795095900852772", "1408072", "1a53630780dee01e236cff7233d35d01", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.530, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.430, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.53, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.43, 0.00 ~ 1.00
    """
    黑白三格    = EffectMeta("黑白三格", False, "6719657002571665934", "635017", "e4022fb9e226f41f58c33d255c647eed", [])
    黑白漫画    = EffectMeta("黑白漫画", False, "6795826673993388551", "634953", "f5e6a157bc591221429ad4d0af4764b3", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    黑白漫画_II = EffectMeta("黑白漫画 II", False, "6904876576735760904", "981864", "93e7188b36f51f6aa660cf2cf44569b7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    黑白线描    = EffectMeta("黑白线描", False, "6795430643154031111", "634951", "68c0d3c64a515b7cdc99b2cf0b6914fe", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    黑线故障    = EffectMeta("黑线故障", False, "6970572741116170788", "1155300", "fc0dca637063d415f92ab45869d9f8d5", [])
    黑羽毛      = EffectMeta("黑羽毛", False, "6716441529084285454", "634151", "9be9c2290cd7574af6d47f1779e4519a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    黑羽毛_II   = EffectMeta("黑羽毛 II", False, "6751257389422350860", "634149", "8e20f4ef27e5d50c3839eabcde5c292d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    黑胶边框    = EffectMeta("黑胶边框", False, "6865958778265670151", "898866", "30c353317f11b9a5dcdf5b64708955ad", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    黑色噪点    = EffectMeta("黑色噪点", False, "6888561214125773326", "952514", "e7baebcf969437d4d5cdb607578bbf89", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    黑色老电视  = EffectMeta("黑色老电视", False, "6738276072246219277", "635123", "87b8b83900d283b06e02ead6f09111e5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Bling飘落   = EffectMeta("Bling飘落", True, "7306819369571455515", "31620429", "5425c855f5395166464034278b51afc2", [
                              EffectParam("effects_adjust_speed", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.450, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.45, 0.00 ~ 1.00
    """
    C300        = EffectMeta("C300", True, "7226241938649780793", "12744891", "3bc3db89a7d77cbeb49d42a9566b575f", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.55, 0.00 ~ 1.00
    """
    IXUS        = EffectMeta("IXUS", True, "7213660933942415930", "11068675", "bd4fb5e91257e0bcf302f23a093f57cc", [
                              EffectParam("effects_adjust_intensity", 0.440, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.44, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.15, 0.00 ~ 1.00
    """
    Ins描边     = EffectMeta("Ins描边", True, "7265936765175730744", "20434943", "402b239494189ae949538500b9fd6e50", [
                              EffectParam("effects_adjust_color", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.460, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.46, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.30, 0.00 ~ 1.00
    """
    S形运镜     = EffectMeta("S形运镜", True, "7291263159023702584", "26271784", "1a137ba40b56a10809190892c3850f95", [
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    W830        = EffectMeta("W830", True, "7226197862529372731", "12732403", "70556dee7b46e17512e9525613951aca", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.80, 0.00 ~ 1.00
    """
    一刀两断    = EffectMeta("一刀两断", True, "7290460914174661177", "26002592", "6e66b782a69fa0c2712deeaf50d4aadf", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
    """
    丁达尔旋焦  = EffectMeta("丁达尔旋焦", True, "7361697260960223759", "59474165", "815fe4564516ccb104dd6a12682e6ac2", [
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
    """
    丝印涂鸦    = EffectMeta("丝印涂鸦", True, "7270068054040515131", "21210786", "0e342cccb5b95dafc6e99f0f51603b04", [
                              EffectParam("effects_adjust_color", 0.200, 0.050, 1.000),
                              EffectParam("effects_adjust_intensity", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.570, 0.000, 0.810),
                              EffectParam("effects_adjust_speed", 0.430, 0.000, 0.700),
                              EffectParam("effects_adjust_texture", 0.120, 0.000, 0.500)])
    """参数:
        - effects_adjust_color: 默认0.20, 0.05 ~ 1.00
        - effects_adjust_intensity: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.57, 0.00 ~ 0.81
        - effects_adjust_speed: 默认0.43, 0.00 ~ 0.70
        - effects_adjust_texture: 默认0.12, 0.00 ~ 0.50
    """
    丝滑运镜    = EffectMeta("丝滑运镜", True, "7382145257607008809", "71888371", "9333197e30c47f6aab8eb7b6bba7bd38", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    两屏分割    = EffectMeta("两屏分割", True, "7069602912057430558", "1594946", "2eba26aa15c0e44d2c258ce63a38d243", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.10, 0.00 ~ 1.00
    """
    中轴旋转    = EffectMeta("中轴旋转", True, "7224407224460775994", "12495253", "16c94e8b38c2d306c11b0d4cfb63dec9", [
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    云朵绵绵    = EffectMeta("云朵绵绵", True, "7287143540033851964", "24962948", "66f0d5b98e5c703d596c6d5053b36a73", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    五星好评    = EffectMeta("五星好评", True, "7176947440350663223", "7318779", "68b302b2bea8da7aea6db5fef3da518e", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    交叉震闪    = EffectMeta("交叉震闪", True, "7291135461697786423", "26216294", "c008c7e122d99b87378292db514ed6cb", [
                              EffectParam("effects_adjust_color", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
    """
    低保真      = EffectMeta("低保真", True, "7300933146923504178", "29478846", "afb3e21fb90b170bc431dd088513b2ed", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.20, 0.00 ~ 1.00
    """
    侧移模糊    = EffectMeta("侧移模糊", True, "7291553469180154423", "26353150", "2fb8c434b5867861aca8abfd58c72920", [
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    倒带        = EffectMeta("倒带", True, "7358381380687893027", "57670397", "7eb38d3b30ae8e18748fcd3ed726aab2", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
    """
    倒计时      = EffectMeta("倒计时", True, "7042501782014005773", "1485906", "06c20494725c2b5873c5aac7fcea3205", [])
    假日闪闪_Ⅱ = EffectMeta("假日闪闪 Ⅱ", True, "7173558602580365838", "6940703", "ee3bcd824b78992d1a9ee05289f724bb", [
                              EffectParam("effects_adjust_size", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.650, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.65, 0.00 ~ 1.00
    """
    像素屏闪    = EffectMeta("像素屏闪", True, "7242581780866273850", "14975389", "a0b46f005c19589d83743e33b8f7f05c", [
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    像素扫描    = EffectMeta("像素扫描", True, "7345080472545792521", "50297398", "a37ca96c39e545f397ec3ff4c6c9a5b1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    像素拉伸_II = EffectMeta("像素拉伸 II", True, "7355396055397044790", "56071748", "867a13e17bbab1fff0bc2344a41c4559", [
                              EffectParam("effects_adjust_rotate", 0.600, 0.200, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_rotate: 默认0.60, 0.20 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    像素排序    = EffectMeta("像素排序", True, "7223659432419267132", "12385973", "24e9de1fa2c77ec26045f7113fdc79f9", [
                              EffectParam("effects_adjust_number", 0.940, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.94, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.00, 0.00 ~ 1.00
    """
    像素故障    = EffectMeta("像素故障", True, "7239557281942082107", "14523597", "964299673ae36eb232abec3452f50624", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    像素爱心    = EffectMeta("像素爱心", True, "7058961362550002212", "1552218", "cbf62902df7101761116f28616cbbabc", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    像素震闪    = EffectMeta("像素震闪", True, "7349147660290363944", "52648474", "5eed2819a04cfccafd198a00309ad2a0", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    光线扫描    = EffectMeta("光线扫描", True, "7047492648587760142", "1500914", "815e6f766c2f5ba2e6b6eea27844b2d1", [
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.380, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.38, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.15, 0.00 ~ 1.00
    """
    光线拖影    = EffectMeta("光线拖影", True, "7254547939194835515", "17852396", "1cee833d647541e86d24bb2f7b7635ea", [
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.340, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.34, 0.00 ~ 1.00
    """
    光谱扫描    = EffectMeta("光谱扫描", True, "7257452387160298021", "18636946", "871e765d3b6486d36166bfb55dfc4b54", [
                              EffectParam("effects_adjust_background_animation", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.614, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.642, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.61, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.64, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.33, 0.00 ~ 1.00
    """
    兔兔碎闪    = EffectMeta("兔兔碎闪", True, "7184326422612152887", "8343041", "375943efb400de1f186e9701e1f4b8e6", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    全息扫描    = EffectMeta("全息扫描", True, "7246746366108504636", "15772481", "7de6cab0dbc13aaaa9ccc25e1259c3da", [
                              EffectParam("effects_adjust_luminance", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.260, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.570, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.26, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.57, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.60, 0.00 ~ 1.00
    """
    分屏漏光    = EffectMeta("分屏漏光", True, "7276332732051886649", "22335555", "b19b89d0f4daf5988d2f390e5364077e", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("sticker", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - sticker: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    动态侦测    = EffectMeta("动态侦测", True, "7348407437877056009", "52247519", "930511ab136c4558e75177f724587990", [
                              EffectParam("effects_adjust_speed", 55.000, 0.000, 100.000),
                              EffectParam("effects_adjust_number", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.980, 0.000, 1.000),
                              EffectParam("sticker", 0.240, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认55.00, 0.00 ~ 100.00
        - effects_adjust_number: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.98, 0.00 ~ 1.00
        - sticker: 默认0.24, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.10, 0.00 ~ 1.00
    """
    动态格      = EffectMeta("动态格", True, "7065593660921877028", "1570398", "eb35001e4b8d3d9e2c7b797578d1e97c", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    动感光束    = EffectMeta("动感光束", True, "7162091309375689223", "5779099", "89af4a6484b09943dd5ce0313b6f3300", [
                              EffectParam("effects_adjust_intensity", 0.581, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.398, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.58, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.40, 0.00 ~ 1.00
    """
    动感变焦    = EffectMeta("动感变焦", True, "7338707315987583488", "47239575", "a36edfb925cbfa69a86a5bdd53f7237f", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    动感扫光    = EffectMeta("动感扫光", True, "7345724656642429452", "50636467", "8df52caeaddcd571a2b6bb325b7209ae", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
    """
    动感推镜    = EffectMeta("动感推镜", True, "7330964667252085248", "43472640", "f482dc307814b8b0697bbf9aa678b5e8", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    动感竖线    = EffectMeta("动感竖线", True, "7339899789795922468", "47905484", "798630fbe18ab78b9a751a48341aed8b", [
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.210, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.21, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    动感运镜    = EffectMeta("动感运镜", True, "7340866533943415308", "48296868", "e258bc9e064d90c2b65ec5fed2320885", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    十字模糊    = EffectMeta("十字模糊", True, "7156060838334304775", "5508159", "0737102012e5a9451b6dcb842fa3cbf6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
    """
    十字爆闪    = EffectMeta("十字爆闪", True, "7291868496558821915", "26443872", "04a1a4ff3dec382e6c2b00586ceb301a", [
                              EffectParam("effects_adjust_intensity", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
    """
    单向移动    = EffectMeta("单向移动", True, "7221408305871065661", "12087461", "1efa77e2563de9f51ecf4c8639a995bc", [
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.490, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.49, 0.00 ~ 1.00
    """
    单彩渐变    = EffectMeta("单彩渐变", True, "7296751848508101158", "28007443", "bb064dadbd40eda875b9a632d07c4e3f", [
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
    """
    单色填充    = EffectMeta("单色填充", True, "7128329164314120717", "3956309", "7647e2c7607c75922abb4cd232e83dff", [
                              EffectParam("effects_adjust_range", 0.760, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.360, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.76, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.36, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    卡机        = EffectMeta("卡机", True, "7046676785693463071", "1498082", "ea84ea931c93434b86263b92aabbadd4", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    卡通渲染    = EffectMeta("卡通渲染", True, "7358012370125328937", "57459941", "a0b8524e28d2e4cb243ae5c6a0448fb1", [
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.30, 0.00 ~ 1.00
    """
    发光HDR     = EffectMeta("发光HDR", True, "7265989852099777061", "20444395", "ae36dc26cae2cd9b4f66a25dc4323c29", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.15, 0.00 ~ 1.00
    """
    取景器      = EffectMeta("取景器", True, "7145432172021682725", "4694121", "76868b9a58758e29212eb76abe18eef2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.802, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    变色狙击    = EffectMeta("变色狙击", True, "7146096867544142367", "5418579", "f4876e6aa0a710888c0dded6dd35879c", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    变色闪光    = EffectMeta("变色闪光", True, "7257436414965453368", "18628864", "3f06e59c32f2e12dd4b63686844a0121", [
                              EffectParam("effects_adjust_range", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.85, 0.00 ~ 1.00
    """
    变速推镜    = EffectMeta("变速推镜", True, "7338347637009027618", "47074578", "81bb946b8dfe47610a322d7f2d2496d9", [
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 2.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 2.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 2.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 2.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 2.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 2.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    变速推镜II  = EffectMeta("变速推镜II", True, "7349154305045172736", "53195413", "5b71a4a5390f261a4e400c0dd2e31d0f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    可爱涂鸦    = EffectMeta("可爱涂鸦", True, "7267137261697765943", "20662139", "3b8f6203dfedcd2ff5d17ff6ac6bef78", [
                              EffectParam("sticker", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.180, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000)])
    """参数:
        - sticker: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.18, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
    """
    吓到失魂    = EffectMeta("吓到失魂", True, "7149057547792552456", "4884447", "2ce39d4b185862a94ebaf6d9ca871b96", [
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.707, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.71, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.10, 0.00 ~ 1.00
    """
    噪片映射    = EffectMeta("噪片映射", True, "7130233403898597902", "4002845", "e974f7b6381909e805e37d72c955ab1f", [
                              EffectParam("effects_adjust_noise", 0.343, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    圆形分屏    = EffectMeta("圆形分屏", True, "7298664552793641522", "28683046", "3674e65bf11eb5b60c9ebcb4f7591dbd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.10, 0.00 ~ 1.00
    """
    圣诞日记    = EffectMeta("圣诞日记", True, "7308639868085604901", "32448752", "360c82d08c822cecb16e79b201768177", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.780, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.78, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    复古彩虹    = EffectMeta("复古彩虹", True, "7269735872445026877", "21148898", "75886bbc57543881343141e58e0c3871", [
                              EffectParam("effects_adjust_size", 0.720, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 0.800),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.72, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 0.80
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.90, 0.00 ~ 1.00
    """
    复古拼贴    = EffectMeta("复古拼贴", True, "7264510800415429177", "20159886", "8628c4e9455115f3c9fac5411de3241e", [
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.440, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.44, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    复古紫调    = EffectMeta("复古紫调", True, "7273707462107075130", "21870120", "eb8220e91369535e0cd5a471fd98b2a2", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.340, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.380, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.260, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.560, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.38, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.26, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.56, 0.00 ~ 1.00
    """
    复古红调    = EffectMeta("复古红调", True, "7170897764744696356", "7308411", "2a96e0c8e739c577b3f3860bad1d0c0a", [
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.70, 0.00 ~ 1.00
    """
    复古连拍    = EffectMeta("复古连拍", True, "7078198448045953572", "1644374", "154f59ff4dd71886d96aa36391656a64", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.160, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.16, 0.00 ~ 1.00
    """
    复古闪闪    = EffectMeta("复古闪闪", True, "7039549945338139150", "1475376", "bd1494bd893e3e113ef7ca922f2db8a5", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    复古频闪    = EffectMeta("复古频闪", True, "7343141676828856844", "49278125", "83e65027b467568dbc6dd666658e07d8", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    失焦CCD     = EffectMeta("失焦CCD", True, "7189438884340568633", "8556597", "e08db3117c2c608d3c1ea94129ff6b27", [
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    失焦光斑    = EffectMeta("失焦光斑", True, "7280121081208246845", "23238701", "01947e259c3fa9990faa6c58345af775", [
                              EffectParam("effects_adjust_size", 0.120, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.340, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.12, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
    """
    定格祝福    = EffectMeta("定格祝福", True, "7321603111791890982", "39287043", "6ec72c24a543383a74db927a3022e5c1", [
                              EffectParam("effects_adjust_color", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
    """
    实况开幕    = EffectMeta("实况开幕", True, "7367289783153857024", "63011918", "58a0d76b10a23a76f1d7834f097e888a", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
    """
    对焦DV      = EffectMeta("对焦DV", True, "7195792007309038117", "9034919", "e9646eb7d4a371f41bd5e3c151f65589", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.20, 0.00 ~ 1.00
    """
    局部推镜    = EffectMeta("局部推镜", True, "7301528497577529906", "29684830", "a607e28c273a94691df816231b0d5f3c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    局部色彩    = EffectMeta("局部色彩", True, "7041515097927193125", "1482682", "5a629b9f88febe47a6c99a5113c02d06", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    居中闪切    = EffectMeta("居中闪切", True, "7273800436128158264", "21899077", "98283327a415b5719ca3bec1c713b707", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.00, 0.00 ~ 1.00
    """
    屏幕律动    = EffectMeta("屏幕律动", True, "7119437097697546782", "3529421", "0736478f60e481067bdeadeb1c620e00", [
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
    """
    幻动光斑    = EffectMeta("幻动光斑", True, "7337641482376974883", "46674042", "5ee226902be5ac3294d53fb015b428d8", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
    """
    幻彩故障    = EffectMeta("幻彩故障", True, "6912383907191067149", "1005744", "76f90178a99f63e7c95869f597c568cd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    幻影_I      = EffectMeta("幻影 I", True, "7212904257043829307", "10969387", "6699feabadc4f59732b8087620fc95a6", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    弹动摇镜    = EffectMeta("弹动摇镜", True, "7332839146907505215", "44400476", "79ba3b0f0b1687e56a7514a0301e6af0", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
    """
    弹动旋入    = EffectMeta("弹动旋入", True, "7377307494097359371", "69256604", "cc9bb0039ebba34a0951ff9c9b8118c4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    弹性闪动    = EffectMeta("弹性闪动", True, "7161280260435087885", "5718993", "a852817db39ecb51dd2217523a53a032", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    彩光摇晃    = EffectMeta("彩光摇晃", True, "7359557508014281268", "58342723", "b5ec6622597ef93c0ec5c983c2da730b", [
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    彩光频闪    = EffectMeta("彩光频闪", True, "7221126479793361465", "12061167", "41afdc49bdf68220c2a01997091e5cf5", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.260, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.26, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    彩色像素    = EffectMeta("彩色像素", True, "7254126716489044538", "17710540", "065447c724fdfd29412be566af129e90", [
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.270, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.27, 0.00 ~ 1.00
    """
    彩色流光_I  = EffectMeta("彩色流光 I", True, "7246400747665887802", "15698169", "77ec3549e15d944b01992551e3e0c35e", [
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.590, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.59, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.00, 0.00 ~ 1.00
    """
    彩色流光_II = EffectMeta("彩色流光 II", True, "7251502652549239354", "16940779", "eb006a9670d27e811c07bd7b689bbd99", [
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.030, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.03, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    彩色流光_III= EffectMeta("彩色流光 III", True, "7246410407399658043", "15699849", "c605c345e8bfc8d98d054f577d31dc55", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.60, 0.00 ~ 1.00
    """
    彩色火焰    = EffectMeta("彩色火焰", True, "6966855040380178981", "1142428", "2a83206eb7f6f9d65af177a29ea223e2", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    彩色珠滴    = EffectMeta("彩色珠滴", True, "7223201236621726264", "12323189", "68bfe7d647af605724dbff1911ad05f6", [
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.260, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.26, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    彩色电光    = EffectMeta("彩色电光", True, "7275262942348579389", "22296923", "4486aefcbd511057cafcdcbc13e4f057", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.680, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.68, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    彩色碎彩    = EffectMeta("彩色碎彩", True, "7181402247824151099", "7743725", "4638f92e49b284396403035e0d9f543f", [
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    彩色碎片    = EffectMeta("彩色碎片", True, "7101592529811804679", "2148348", "48d0dd4f0d70a5d8c6b4846792068335", [
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    彩色碎片_II = EffectMeta("彩色碎片 II", True, "7104546559747953166", "2483800", "0a021da140d56312adf53a90ea3780e5", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
    """
    彩色闪烁    = EffectMeta("彩色闪烁", True, "7222939637260489274", "12297327", "759bf05e399d90bb465edf21d29dabfc", [
                              EffectParam("effects_adjust_color", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    彩虹光影    = EffectMeta("彩虹光影", True, "7377004728208593447", "69089511", "122551eb93dd49877b59586f7d66d42f", [
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.660, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    彩虹棱镜    = EffectMeta("彩虹棱镜", True, "7195867446429880889", "9053951", "c96f1eba3950dc1bbe134a216ef4a6bb", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.30, 0.00 ~ 1.00
    """
    彩虹泛光    = EffectMeta("彩虹泛光", True, "7195112049876144698", "10021925", "75a2d417b48815ffec602d06baa28e02", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
    """
    彩虹闪屏    = EffectMeta("彩虹闪屏", True, "7343557569589285413", "49499805", "aaeae77e0c74db18769bd2cbab83360a", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    彩边频闪    = EffectMeta("彩边频闪", True, "7352815372510171688", "54679766", "9ddcc579cbfbb6350934ea279f7f9f50", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    微震闪黑    = EffectMeta("微震闪黑", True, "7377721589900513818", "69480931", "28471a0d035b66c5b99d954cbcbf496a", [
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
    """
    心跳_II     = EffectMeta("心跳 II", True, "7140620970934407693", "4478025", "e940e6b4377d03450c4a53ab618b99f0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.360, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.36, 0.00 ~ 1.00
    """
    快速变焦    = EffectMeta("快速变焦", True, "7281494629483024952", "23539651", "9af1277c92286811b1890ebe1d682237", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.285, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.28, 0.00 ~ 1.00
    """
    快闪运镜    = EffectMeta("快闪运镜", True, "7366140711969755674", "62251172", "4e85edcb46572136ce3343e9cdc197d2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
    """
    恐怖涂鸦    = EffectMeta("恐怖涂鸦", True, "7117142803863310855", "5418578", "b37405a2ca50f0059744dae5b66ff997", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.220, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.22, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.90, 0.00 ~ 1.00
    """
    慢门拖影    = EffectMeta("慢门拖影", True, "7317916065353175579", "37514660", "0bc4e48d7665268ab0f911979fbec195", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.140, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.14, 0.00 ~ 1.00
    """
    手写边框    = EffectMeta("手写边框", True, "7111253709614486029", "3099452", "1562db9ef86c866cdd951885f1fa26f4", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.260, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.26, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
    """
    扭动变焦    = EffectMeta("扭动变焦", True, "7338354272280515106", "47079994", "83df4a1fadf009b94e737565720debef", [
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.30, 0.00 ~ 1.00
    """
    扭曲变焦    = EffectMeta("扭曲变焦", True, "7299392770534281765", "28941014", "643635cac6435ea88dd6c4a9ae91303f", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.00, 0.00 ~ 1.00
    """
    扭曲模糊    = EffectMeta("扭曲模糊", True, "7210652297754317367", "10694297", "a48e3fb197688fb20a959a961ab54383", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.455, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
    """
    抖动模糊    = EffectMeta("抖动模糊", True, "7202812661405323813", "9780487", "416a2f55681bf6951f25fd3c7336025b", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    抽帧拖影    = EffectMeta("抽帧拖影", True, "7353197719587918362", "54890386", "40f732cd394565be3c7764923c5104be", [
                              EffectParam("effects_adjust_blur", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
    """
    拉伸旋镜    = EffectMeta("拉伸旋镜", True, "7359100199437865506", "58077796", "8dd1ef0645dddee8170190583a1ff51a", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.670, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.67, 0.00 ~ 1.00
    """
    拉扯震动    = EffectMeta("拉扯震动", True, "7240010949938123320", "14603013", "3fb05905a15df5a9b23f36a940016e4e", [
                              EffectParam("effects_adjust_distortion", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.00, 0.00 ~ 1.00
    """
    拉镜开幕    = EffectMeta("拉镜开幕", True, "7340923698955686451", "48340294", "5e3de3ba75f157a19687d84df4545bb0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
    """
    拍照定格    = EffectMeta("拍照定格", True, "7358795504966177292", "57913226", "49d70fec464c90afff087cb5854997dd", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
    """
    拖影灯光    = EffectMeta("拖影灯光", True, "7328017754584257075", "42028150", "3e1f119bd6387d1495fe234cf746e5f8", [
                              EffectParam("effects_adjust_number", 0.698, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    拟截图放大镜= EffectMeta("拟截图放大镜", True, "7028458557058060831", "1478160", "4c962a1294de796686ec24a81a63fe7e", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.00, 0.00 ~ 1.00
    """
    推拉跟随    = EffectMeta("推拉跟随", True, "7380236931893826089", "70944695", "a6fb9367f095b33fa0047a43c2161e74", [
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    推拉运镜    = EffectMeta("推拉运镜", True, "7382100760630137381", "71865342", "4b123b8db48a337b91327c2871ca81e0", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.656, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.849, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.85, 0.00 ~ 1.00
    """
    摇晃叠影    = EffectMeta("摇晃叠影", True, "7307264899422360073", "31866711", "2f82ba674fd1d78a14ccb5d384ee3704", [
                              EffectParam("effects_adjust_speed", 0.350, 0.100, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.35, 0.10 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    摇晃推镜    = EffectMeta("摇晃推镜", True, "7311585733976789554", "33958767", "2b806738c3a5e3126a2013cebc2c4913", [
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    摇晃运镜    = EffectMeta("摇晃运镜", True, "7241063267357954619", "14730265", "bbc5f812f50b8ea1aadb3fd6ac2dd6f0", [
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.80, 0.00 ~ 1.00
    """
    撕纸特写    = EffectMeta("撕纸特写", True, "7235886675845452349", "14014573", "c322a330e87f550e0e56c7cef60e6465", [
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    播放界面    = EffectMeta("播放界面", True, "7078880636584333838", "1647944", "ce6641cd0add17ae5b20286b8a8ff72f", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.20, 0.00 ~ 1.00
    """
    故障定格    = EffectMeta("故障定格", True, "7223652101287580216", "12383111", "18c3c5143edfcf076876fc70566fd521", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    故障开幕    = EffectMeta("故障开幕", True, "7338335435959046656", "47063402", "43a746efc920f57c2b2196446992f4cf", [
                              EffectParam("effects_adjust_sharpen", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_sharpen: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    故障震闪    = EffectMeta("故障震闪", True, "7315262223213924873", "35954280", "510623ce6e6c3d77151024fe04eb30dd", [
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.714, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.71, 0.00 ~ 1.00
    """
    散光弹动    = EffectMeta("散光弹动", True, "7347985147662176807", "52013378", "1d1f9cc33d051f8c2942cbc86de9f6dd", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
    """
    散光闪烁    = EffectMeta("散光闪烁", True, "7338348256226710016", "47894032", "6353300f8b3c913e3a1d60321fd2cc21", [
                              EffectParam("effects_adjust_intensity", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    数字矩阵    = EffectMeta("数字矩阵", True, "7254547645903934010", "17852330", "53625d829446e44920b2397cf4336180", [
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.33, 0.00 ~ 1.00
    """
    斜线震动    = EffectMeta("斜线震动", True, "7244511673409606201", "15332069", "154a4e843d36fe8660f15624a330d2a1", [
                              EffectParam("effects_adjust_size", 0.409, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.704, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.339, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.41, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    新年仙女棒  = EffectMeta("新年仙女棒", True, "7321990419351343653", "39297699", "878e6aaf1e19c6de170d4544c22c38b2", [
                              EffectParam("effects_adjust_size", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.480, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.780, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.48, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.78, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
    """
    方形模糊    = EffectMeta("方形模糊", True, "7384032238951731739", "72505526", "0883434b90fbeaf428ac86a0f87cb4fe", [
                              EffectParam("effects_adjust_blur", 0.877, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.450, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.88, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.45, 0.00 ~ 1.00
    """
    旋焦        = EffectMeta("旋焦", True, "7224445669698703909", "12505491", "c83771425ffddd97d3389480f0f68927", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    旋焦推镜    = EffectMeta("旋焦推镜", True, "7351324357425107519", "53786746", "bfffafcc16a30af7d6faaf7816bd09cf", [
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    旋转变焦    = EffectMeta("旋转变焦", True, "7311544501057622555", "33928843", "46f6856d1b6c40a7d6b7c6da0ae24439", [
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.15, 0.00 ~ 1.00
    """
    旋转回弹    = EffectMeta("旋转回弹", True, "7343557174058029568", "49499445", "fcc043da345af8e07d700f1d13d32dd8", [
                              EffectParam("effects_adjust_speed", 0.660, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
    """
    旋转圆球    = EffectMeta("旋转圆球", True, "7382147305350107700", "71888863", "bc332eeb63f21a5f48f90221ed709196", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    旋转抖动    = EffectMeta("旋转抖动", True, "7324315025558999602", "40324156", "a2df1870a268dac31ac369382c42cf43", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
    """
    旋转抖动_II = EffectMeta("旋转抖动 II", True, "7347956961318539826", "51995951", "a080eeb37e5c98ff3a510c395463727a", [
                              EffectParam("effects_adjust_speed", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
    """
    星星变焦    = EffectMeta("星星变焦", True, "7169474672671592991", "6661731", "daedab920b87b778c4f7c672928dbf96", [
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.70, 0.00 ~ 1.00
    """
    曝光变焦    = EffectMeta("曝光变焦", True, "7259639809491079737", "19104048", "b66ceb2594aee2fd5a1ace6a67e4db0f", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    曝光扩散    = EffectMeta("曝光扩散", True, "7340136879615906344", "47990686", "f01002b2853ba8736b02ee943e132421", [
                              EffectParam("effects_adjust_luminance", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    曲线模糊    = EffectMeta("曲线模糊", True, "7340622176065688098", "48215352", "b140dc7906477e7462636a93f5c9fe3c", [
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.366, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.425, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.37, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.42, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    极速旋转    = EffectMeta("极速旋转", True, "7343542497651462708", "49487569", "c6f8519f592a44f74424411e304bd46b", [
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
    """
    柔和辉光    = EffectMeta("柔和辉光", True, "7249209626829263421", "16279737", "805d415643265f3625c1fb9d55822e32", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    梦幻辉光    = EffectMeta("梦幻辉光", True, "7355386179308491300", "56065875", "4f0997824f81dc66309050646ce45bae", [
                              EffectParam("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.300, 0.000, 2.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.500)])
    """参数:
        - effects_adjust_luminance: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.30, 0.00 ~ 2.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.50
    """
    模拟拍照    = EffectMeta("模拟拍照", True, "7349154734537708084", "53350183", "2cb9807eebb8a358bc01e02e4a1d48b9", [
                              EffectParam("effects_adjust_blur", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    横向闪光    = EffectMeta("横向闪光", True, "7242555690965799483", "14965785", "0e48afbc4e9aa05505644493cbb7156a", [
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    横条开幕    = EffectMeta("横条开幕", True, "7381442168759521792", "71626094", "5fa33938a1ad4a956bbac1b3e9805969", [
                              EffectParam("effects_adjust_speed", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    樱花飘落    = EffectMeta("樱花飘落", True, "7207718227382637113", "10348463", "e70695e42c80f681ed4e173b4735ac0b", [
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    欧根纱II    = EffectMeta("欧根纱II", True, "7366882927801537024", "62749085", "aebc534e02b822de7d014b33d5ac103c", [
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.40, 0.00 ~ 1.00
    """
    气球花花    = EffectMeta("气球花花", True, "7231385092193522235", "13400477", "bd2685c4dba13e0e4e44cd4f0a9ff834", [
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    氛围边框    = EffectMeta("氛围边框", True, "7308944810646180379", "32599175", "657d08f76bf5e462d0acb066315d7e32", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.800),
                              EffectParam("effects_adjust_luminance", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.80
        - effects_adjust_luminance: 默认0.10, 0.00 ~ 1.00
    """
    水光影      = EffectMeta("水光影", True, "7122736441053942285", "3687389", "0e8f5cf28c600c62140c2f3666dbe18b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.15, 0.00 ~ 1.00
    """
    水波倒影    = EffectMeta("水波倒影", True, "7313842878847914547", "35129784", "d151e3575ce8eca803787e849b2ee7f4", [
                              EffectParam("effects_adjust_vertical_shift", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
    """
    水波模糊    = EffectMeta("水波模糊", True, "7047088638932292127", "1499278", "99199baa75373b4a0faa08aa1c27a37a", [
                              EffectParam("effects_adjust_horizontal_chromatic", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_chromatic: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    水波泛起    = EffectMeta("水波泛起", True, "7250433374882370103", "16641371", "eda468a5537c139c6355e5abd75004de", [
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.440, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.460, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.44, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.46, 0.00 ~ 1.00
    """
    水波流动    = EffectMeta("水波流动", True, "7140273505630687780", "4458607", "7dd5dbc55d5db8553d233fee727c40ac", [
                              EffectParam("effects_adjust_distortion", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
    """
    水滴扩散    = EffectMeta("水滴扩散", True, "7221508316852130362", "12112703", "b4690abcdd92f98e3291fdcb74444f5b", [
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
    """
    油画模糊    = EffectMeta("油画模糊", True, "7232232188278739493", "13537551", "f727569dc65078e90f66c9e63d3f9712", [
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.403, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.40, 0.00 ~ 1.00
    """
    法式暖调    = EffectMeta("法式暖调", True, "7090546987170271780", "1747384", "f47d4affff8b734ed6c3b9042e81f7a4", [
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    法式涂鸦    = EffectMeta("法式涂鸦", True, "7253039682877919803", "17395354", "2519d69e2fe1fbe64a653b570e786a0c", [
                              EffectParam("effects_adjust_color", 0.610, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.661, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.720, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.61, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.72, 0.00 ~ 1.00
    """
    泛光扫描    = EffectMeta("泛光扫描", True, "7134989289498087967", "4217252", "5c2fe2a8c4212ee879c16bea71b31e96", [
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, 0.00 ~ 1.00
    """
    泛光爆闪    = EffectMeta("泛光爆闪", True, "7254484266996732476", "17821188", "7eeab42db5ca9a73186fe4f445b7613c", [
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    泛光闪动    = EffectMeta("泛光闪动", True, "7236298986993226301", "14080033", "982d5dfb68207b458e4061c6a8742482", [
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    泡泡光斑    = EffectMeta("泡泡光斑", True, "7320155012036825610", "38547267", "a8ef5cdbe91838c8092a05a4ee2abf28", [
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.30, 0.00 ~ 1.00
    """
    泡泡冲屏    = EffectMeta("泡泡冲屏", True, "7373963046693114387", "67466796", "51ea34188c370cae7e764a47be73d6a3", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 0.800)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 0.80
    """
    波动清晰    = EffectMeta("波动清晰", True, "7340620060362281512", "48213992", "d4009f4188b7c8293760896d5a606f0f", [
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
    """
    波浪        = EffectMeta("波浪", True, "7159183282632921631", "5574521", "2d803403ccfbeb2328a811014a55081f", [
                              EffectParam("effects_adjust_speed", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.780, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.78, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    波浪丝印    = EffectMeta("波浪丝印", True, "7146406661249307150", "4880117", "cf32c231aa6b092d39cbcd7c346db5a3", [
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    波纹闪动    = EffectMeta("波纹闪动", True, "7332415663106953769", "44222768", "7efba1463deb33955572e53ec6bd71be", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
    """
    流体冲屏    = EffectMeta("流体冲屏", True, "7221730308251456037", "12130415", "958711bf2dc7393f39862e7952f6b5c5", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    流体荡开    = EffectMeta("流体荡开", True, "7322018576125137417", "39315461", "fa0a0cd4b5446445108d6b4d44466739", [
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    海报描边    = EffectMeta("海报描边", True, "7133104392231719431", "4118241", "9b6e240d941ae5e77e573cd584265e77", [
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
    """
    海鸥DC      = EffectMeta("海鸥DC", True, "7051853636548170271", "1520896", "b9dc0143d875fbff52cb26f363f45d14", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    液态分离    = EffectMeta("液态分离", True, "7241096748184113701", "14742833", "c24d9c1a2bf816e305645ee216b75e30", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    漂浮爱心    = EffectMeta("漂浮爱心", True, "7306769922535723558", "31585739", "2a84ea537b525994b2803d6a538960e1", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    潮流涂鸦    = EffectMeta("潮流涂鸦", True, "7350240257914180135", "53198933", "9d284a90662cd32eeb4e8228a379c441", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    瀑布开幕    = EffectMeta("瀑布开幕", True, "7351689682138174006", "54008092", "ecd11cf24ab2644cc93ae00f4ad1a7d3", [
                              EffectParam("effects_adjust_speed", 0.570, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.260, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.57, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.26, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
    """
    灵魂出窍_II = EffectMeta("灵魂出窍 II", True, "7299377358283215398", "28934274", "4e2c3e0ff21146736ddfeea23e6affaa", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.85, 0.00 ~ 1.00
    """
    灿灿金币    = EffectMeta("灿灿金币", True, "7304546673215148595", "30737307", "921df9ceada99345eff8e577b1e10722", [
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.80, 0.00 ~ 1.00
    """
    灿金彩带    = EffectMeta("灿金彩带", True, "7308706488686481947", "33271125", "22171c77551d5769904778e3bd386859", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.25, 0.00 ~ 1.00
    """
    炫光变焦    = EffectMeta("炫光变焦", True, "7002109122350944781", "1237470", "8b94fb6f9bacb3eab0d44fc8bad3ddd1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.753, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    炫光扫描    = EffectMeta("炫光扫描", True, "7367314177741820435", "63023070", "79582fc0a97afe1fcd4fb0199d07bc7d", [
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.660, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.66, 0.00 ~ 1.00
    """
    烟花2024    = EffectMeta("烟花2024", True, "7308706250731033097", "36744068", "511dd4d1de63c4839c5912c69711e8cf", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.770, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.625, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.77, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.62, 0.00 ~ 1.00
    """
    热恋        = EffectMeta("热恋", True, "7195020880018149944", "9062069", "d4a9c95961f95536f3fc44096bf62cbd", [
                              EffectParam("effects_adjust_size", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.060, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.06, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    爆闪锐化    = EffectMeta("爆闪锐化", True, "7222907722486780472", "12284805", "389b3c8872b9a18e5fe570975e3aa2ae", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.70, 0.00 ~ 1.00
    """
    爱心扫光    = EffectMeta("爱心扫光", True, "7322345920962499123", "39420273", "e1629600c228ebd43732cb589c245168", [
                              EffectParam("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
    """
    爱心气球    = EffectMeta("爱心气球", True, "7268210584707928634", "20875808", "ec80143a43c12596d99f8c31043c6a8b", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    爱心软糖    = EffectMeta("爱心软糖", True, "7331625316885991970", "43774786", "0bab0476804fd6ac903bda686f49f3cb", [
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.90, 0.00 ~ 1.00
    """
    爱心边框    = EffectMeta("爱心边框", True, "7065927898833621511", "1572505", "2f62bf787eb44535dbd128d60f46a29c", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.00, 0.00 ~ 1.00
    """
    珠光Kira    = EffectMeta("珠光Kira", True, "7267917946733728314", "20820466", "235af2aa5680584b232598629e70b990", [
                              EffectParam("effects_adjust_number", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    珠光碎闪    = EffectMeta("珠光碎闪", True, "7265695554640810533", "20405527", "325258e144f2c6417f123d48886356de", [
                              EffectParam("effects_adjust_filter", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.15, 0.00 ~ 1.00
    """
    电光描边    = EffectMeta("电光描边", True, "7106762731960668703", "2721906", "15153b69c032c89f4087d12ef7a613ca", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
    """
    电光波动    = EffectMeta("电光波动", True, "7301674026173207066", "29755128", "9d7a93ea28f697fbc109cd26377d025d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 2.000),
                              EffectParam("effects_adjust_color", 0.030, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 2.00
        - effects_adjust_color: 默认0.03, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    电光爆闪    = EffectMeta("电光爆闪", True, "7306471467397419547", "31478585", "dfc0eec30caaa1a9f992332a85e89a7b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    电光爆闪_II = EffectMeta("电光爆闪 II", True, "7349150013441708559", "52650215", "8129e3f83ad6973ba9e6613dbf7afb88", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
    """
    电光爱心    = EffectMeta("电光爱心", True, "7106779118867321357", "2724410", "04883bbcc4ce20a240d5f90dc34db76f", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.419, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.473, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.590, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.42, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.47, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.59, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认1.00, 0.00 ~ 1.00
    """
    电音故障    = EffectMeta("电音故障", True, "7246745900473651773", "15772327", "fdec63c54f10bf1b8b557a3709196eff", [
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.580, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.58, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    画质清晰    = EffectMeta("画质清晰", True, "7348707427165934107", "52400085", "4a35ff3b8a83d2cec2d56e5651f9e04a", [
                              EffectParam("effects_adjust_luminance", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.800, 0.000, 2.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.500),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.80, 0.00 ~ 2.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.50
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.33, 0.00 ~ 1.00
    """
    白鸽        = EffectMeta("白鸽", True, "7382490757770252827", "71992424", "3e6056fb9e3a1829a666c6680f7eab83", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    相片定格    = EffectMeta("相片定格", True, "7265526511220822586", "20350863", "a58e3178d3a498edac53074a3c3a7542", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    矩阵频闪    = EffectMeta("矩阵频闪", True, "7306346511367934491", "31403673", "51763569c67e833ffcb37bd41a365c75", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.880, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.88, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    碎闪描边    = EffectMeta("碎闪描边", True, "7130585329609740814", "4007289", "680eaa2d8db4fd3a5d33cf5399e61518", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
    """
    磁带DV      = EffectMeta("磁带DV", True, "7101987162526061070", "2211756", "b6b5848678e71593cf7e5112874b9939", [
                              EffectParam("effects_adjust_sharpen", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_sharpen: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    磨砂水晶    = EffectMeta("磨砂水晶", True, "7090380952605561381", "1729610", "f0d404000523379787cffd6e1db715c2", [
                              EffectParam("effects_adjust_vertical_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.00, -1.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, -1.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    神龙纳福    = EffectMeta("神龙纳福", True, "7326853354615738889", "41485429", "de1999f4a3c33b823bd0ab1b24142adb", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    秋日暖阳    = EffectMeta("秋日暖阳", True, "7156868464894808583", "5408805", "62cdcc8cc7c26ea48447578ee57b5f35", [
                              EffectParam("effects_adjust_blur", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    移轴模糊    = EffectMeta("移轴模糊", True, "7246784641384845861", "15780929", "ceae265f1f63d74a4816f647710885a3", [
                              EffectParam("effects_adjust_range", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.00, 0.00 ~ 1.00
    """
    竖向开幕    = EffectMeta("竖向开幕", True, "7384009190836015654", "72501890", "26c9cc8d460d2639fe4fbb0bbd012d41", [
                              EffectParam("effects_adjust_blur", 0.877, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.88, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.60, 0.00 ~ 1.00
    """
    竖向闪光    = EffectMeta("竖向闪光", True, "7212938795702817338", "10976911", "7529d488cc18a6fb4a7e58c4ef3af378", [
                              EffectParam("effects_adjust_number", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.690, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.69, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    竖线屏闪    = EffectMeta("竖线屏闪", True, "7304258446658900489", "30666842", "4444e09ba223f94827fb9d423f445a71", [
                              EffectParam("effects_adjust_luminance", 1.700, 0.000, 2.300),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 2.500),
                              EffectParam("effects_adjust_range", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 2.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认1.70, 0.00 ~ 2.30
        - effects_adjust_blur: 默认1.00, 0.00 ~ 2.50
        - effects_adjust_range: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 2.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    竖闪模糊    = EffectMeta("竖闪模糊", True, "7291135061494075960", "26216108", "795af3daacce29e8d7732e5b2223e01a", [
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
    """
    粉雪        = EffectMeta("粉雪", True, "7298283919944716827", "28549704", "273f611315ca2f66e370a3a77de6185c", [
                              EffectParam("effects_adjust_background_animation", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.950, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.95, 0.00 ~ 1.00
    """
    粒子放射    = EffectMeta("粒子放射", True, "7217716815407878693", "11587497", "df109cf35978de6bcc3803f559b14b07", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    精致辉光    = EffectMeta("精致辉光", True, "7368344527494451712", "63611181", "ad7fae5b6c5335be75113171ab5a6b6d", [
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.40, 0.00 ~ 1.00
    """
    紫光夜      = EffectMeta("紫光夜", True, "7311995150962528778", "34184103", "1a4c76312950f09d8fd14e68de775bd8", [
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    繁花棱镜II  = EffectMeta("繁花棱镜II", True, "7269749564658160184", "21150170", "f0d388c9f42348261ed7b6871cfaa86e", [
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.30, 0.00 ~ 1.00
    """
    红蓝魔      = EffectMeta("红蓝魔", True, "7122384870294163975", "3675609", "0c7634532abc28facafe3afe024a4fbc", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    红边模糊    = EffectMeta("红边模糊", True, "7130591331700707876", "4007601", "1afa6bef0ff1ddd4e54c13a2d6a7c59a", [
                              EffectParam("effects_adjust_blur", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.90, 0.00 ~ 1.00
    """
    纵向跳动    = EffectMeta("纵向跳动", True, "7190200556692967995", "8626971", "95f1d0f51d2eb529ac7b97c8cddbfaf1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认1.00, 0.00 ~ 1.00
    """
    纸质抽帧    = EffectMeta("纸质抽帧", True, "7046650052286091812", "1534320", "1d4d7f2a92315acd523dbfe21176cfbf", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    线光变速    = EffectMeta("线光变速", True, "7367628113062138377", "63209940", "87a99c8ae0f9e333abaef48b79a96c90", [
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    线条涂鸦    = EffectMeta("线条涂鸦", True, "7266446552258843173", "20547949", "33b11d3bd867449b2fcc21c349b33639", [
                              EffectParam("effects_adjust_texture", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 0.800),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 0.80
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    缤纷        = EffectMeta("缤纷", True, "7072268839303516709", "1607634", "4294dd203d48821ed92525b79f704231", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    网点丝印    = EffectMeta("网点丝印", True, "7146404902971904548", "4879935", "01312233fbabf72f4f66ac30f84c020c", [
                              EffectParam("effects_adjust_texture", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    群蝶飞舞    = EffectMeta("群蝶飞舞", True, "7347658324956942883", "51832286", "88f861bb14eac5dae7fe7e5df123d718", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
    """
    羽毛飘落    = EffectMeta("羽毛飘落", True, "7379513630837969445", "70529088", "46f1c56f6fcd3a2abd80ff7d701f6eb0", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.260, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.108, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.26, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.11, 0.00 ~ 1.00
    """
    翻转变焦    = EffectMeta("翻转变焦", True, "7299377095107416585", "28934164", "6c5f82fb84dc77d361ae83657259bc19", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
    """
    翻转开幕    = EffectMeta("翻转开幕", True, "7235902836188385852", "14020695", "a4d3d6cc942a659f39cc5bbcb90b516e", [
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.10, 0.00 ~ 1.00
    """
    老式DV      = EffectMeta("老式DV", True, "7026261220961292807", "1426168", "9b7fc1e4ed44a38366a37377d7003192", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.630, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.63, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.30, 0.00 ~ 1.00
    """
    胶片V       = EffectMeta("胶片V", True, "7151967279817691662", "5050659", "e8dabb72421c2773120bfc6d4d3785f0", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    胶片冷绿    = EffectMeta("胶片冷绿", True, "7146524414312452645", "4837281", "52a78b591b893502154b101c757877db", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    胶片暖棕    = EffectMeta("胶片暖棕", True, "7145385234320593439", "4837280", "bcb9ebf14085e77e8b0e1cd1cf0a87f8", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
    """
    胶片滚动    = EffectMeta("胶片滚动", True, "7080354236956938782", "1655466", "a05a7b82f4d36066ef3d6630bb1be809", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    胶片闪切    = EffectMeta("胶片闪切", True, "7384745950608101924", "72761923", "347713d7f8a7b69b1885ee9d38cd8de6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    脉搏跳动    = EffectMeta("脉搏跳动", True, "7052226294972420621", "1522814", "c65fc5a267dde559e80e16c8fcc9cd6c", [
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
    """
    色差震闪    = EffectMeta("色差震闪", True, "7355109046694711871", "55932216", "b4d72c47be1ca1238cddf0790a8a0c55", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    色散冲击    = EffectMeta("色散冲击", True, "7374053937369846307", "67503542", "ed2771a77992c0f8d0958bbaadbba53e", [
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
    """
    色散故障    = EffectMeta("色散故障", True, "7242574690638631479", "14972687", "5989d49ac22b81107c9741367ae6651d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    花屏故障    = EffectMeta("花屏故障", True, "7361718823575097919", "59487955", "93a206e311d0b8128da7ee0ee776c917", [
                              EffectParam("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.143, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_chromatic: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.14, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    花瓣环绕    = EffectMeta("花瓣环绕", True, "7345688874577826342", "50608291", "d954d5148a1d1ec24016499b38b85d1d", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.33, 0.00 ~ 1.00
    """
    菱形光斑    = EffectMeta("菱形光斑", True, "7316813562783994395", "40449614", "8baa04aecc7a8e40d9c71cb3c7a91f33", [
                              EffectParam("effects_adjust_filter", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.230, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.23, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.75, 0.00 ~ 1.00
    """
    菱形变焦    = EffectMeta("菱形变焦", True, "7147943538120987166", "4841353", "fda851ab65ee2b7bd6bb568a0e8bc544", [
                              EffectParam("effects_adjust_size", 0.521, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.720, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.52, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.72, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
    """
    落叶_II     = EffectMeta("落叶 II", True, "7153556255263429151", "5418631", "a7658052127fea9d33b12696e2d71ca4", [
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    蓝光爆闪    = EffectMeta("蓝光爆闪", True, "7288655540341707324", "25450329", "363de1da61a76d9d902e62a7bed611e6", [
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.650, 0.010, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.65, 0.01 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.80, 0.00 ~ 1.00
    """
    蓝色丝印    = EffectMeta("蓝色丝印", True, "7131985730791805448", "4097661", "0fceb871b844d51454db5d59da3636ef", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    虹光旋入    = EffectMeta("虹光旋入", True, "7377352335028130367", "69273433", "bf6fb74a7290e9a8d31dc36453736b66", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.660, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.66, 0.00 ~ 1.00
    """
    视频播放    = EffectMeta("视频播放", True, "7144915597308989988", "4668537", "7a18d00c453615e8415306a7f1f37396", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    负片分屏    = EffectMeta("负片分屏", True, "7278974994623763003", "22907949", "5a980a6a4a707fc1ad13caff77e3926a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.33, 0.00 ~ 1.00
    """
    负片涂鸦    = EffectMeta("负片涂鸦", True, "7157966185571553822", "5477607", "c622911e77150d8ec0e9c4ecde458c02", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    负片涂鸦_II = EffectMeta("负片涂鸦 II", True, "7231111030028374584", "13379581", "02590242d94571bb62a8635b4fd5a3f7", [
                              EffectParam("effects_adjust_texture", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.320, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.32, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
    """
    负片涂鸦_III= EffectMeta("负片涂鸦 III", True, "7267517097775731261", "20745376", "96a028c1ac17f22a452c1e012d47f3ed", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.00, 0.00 ~ 1.00
    """
    负片游移    = EffectMeta("负片游移", True, "7091488033555354120", "1787254", "bc811feeac5b5e4608cbb80c99a07d46", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, -1.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.00, -1.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, -1.00 ~ 1.00
    """
    负片频闪    = EffectMeta("负片频闪", True, "7153575555554611720", "5155369", "c737112d913d14f6cc8871dbc51c8013", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.85, 0.00 ~ 1.00
    """
    超大光斑    = EffectMeta("超大光斑", True, "7171321435200164383", "6691829", "8f525928d0c73912e59702928d728ef2", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
    """
    超强锐化    = EffectMeta("超强锐化", True, "7129336892121682468", "3950243", "f5d68fac1d5f2d24144d143772c4d41b", [
                              EffectParam("effects_adjust_sharpen", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_sharpen: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    跟随运镜    = EffectMeta("跟随运镜", True, "7299426452896748042", "28956878", "4c501e2a054c24f4268b4daa44460f90", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.15, 0.00 ~ 1.00
    """
    跟随运镜_II = EffectMeta("跟随运镜 II", True, "7340954638184616467", "48362872", "d34cbcf01362bf60945dafa56ec5704b", [
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.400, 0.100, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.40, 0.10 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.80, 0.00 ~ 1.00
    """
    车窗_II     = EffectMeta("车窗 II", True, "7109280482025542157", "4795296", "bb46f32dec1993f4c7457360fd61af7c", [
                              EffectParam("effects_adjust_range", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("sticker", 0.350, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - sticker: 默认0.35, 0.00 ~ 1.00
    """
    辉光开幕    = EffectMeta("辉光开幕", True, "7338322046822126114", "47051728", "a37854eb4a70d1f149c417ce3269a8f5", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.270, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.27, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
    """
    边缘扫光    = EffectMeta("边缘扫光", True, "7322363012092793353", "39434745", "8b7a9733b393b42cf018ce2efdebca2a", [
                              EffectParam("effects_adjust_soft", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_soft: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    迷幻故障    = EffectMeta("迷幻故障", True, "7265960462330630714", "20440246", "5ddfb1bd3479179af2c0ec0026b57e3e", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    迷幻荡漾    = EffectMeta("迷幻荡漾", True, "7223208176206746173", "12324741", "1ab6e40160a674cd19de3ade157a3d0b", [
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    迷幻震动    = EffectMeta("迷幻震动", True, "7238863029775897148", "14438877", "e28a153a03d2dcf1a12384712196bc07", [
                              EffectParam("effects_adjust_distortion", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
    """
    重复变焦    = EffectMeta("重复变焦", True, "7161285099667853831", "5719311", "ae41555c055c73d2089f1d681f2bcc20", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    重复震闪    = EffectMeta("重复震闪", True, "7250369682207674938", "16610415", "63a7958ffc3e6a73d3b9556f7ca04381", [
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    金色碎片    = EffectMeta("金色碎片", True, "7106040163402256927", "2622164", "a24eabdabec50f5d52f7e6fb099c899c", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.30, 0.00 ~ 1.00
    """
    金边闪烁    = EffectMeta("金边闪烁", True, "7304832158466576947", "30855689", "46b93ae5afcb00ecface4fd485014d9c", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    银杏飘落    = EffectMeta("银杏飘落", True, "7296789290724364850", "28024643", "c1b8196608a6ef6b142389f499647275", [
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.000, 0.100, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.00, 0.10 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.10, 0.00 ~ 1.00
    """
    闪光弹跳    = EffectMeta("闪光弹跳", True, "7210315941396091447", "10660327", "982ccb302cc81c13762eb31a25c54de5", [
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
    """
    闪光灯_II   = EffectMeta("闪光灯 II", True, "7143919857539486238", "4795220", "1b9f1a3ee39a65820ae21d72793c89a9", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    闪光灯IV    = EffectMeta("闪光灯IV", True, "7276317197658493498", "22328905", "db710dc6b5ea5b2f46595480d06d0d7d", [
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    闪电扭曲    = EffectMeta("闪电扭曲", True, "7329871968298078759", "42913127", "244819f79dffa729f9c9caeeb15a7698", [
                              EffectParam("effects_adjust_luminance", 0.666, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    闪白_II     = EffectMeta("闪白 II", True, "7281219213828559397", "23489443", "631162213ead8ced21aa7936bae06390", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 2.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 2.00
    """
    随机闪切    = EffectMeta("随机闪切", True, "7267909305519575608", "20816436", "6a5fa04981e50a2c7bd67a4e03e4d3e6", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.20, 0.00 ~ 1.00
    """
    随机马赛克  = EffectMeta("随机马赛克", True, "7299769859900969510", "29099986", "190ec4ff873df478cd8842c1c9a9f967", [
                              EffectParam("effects_adjust_size", 0.280, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.220, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.28, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.22, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
    """
    隔行DV      = EffectMeta("隔行DV", True, "7215598241558041125", "11331317", "3429986a54fc1d15cc29f7340103540d", [
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.20, 0.00 ~ 1.00
    """
    雨季_I      = EffectMeta("雨季 I", True, "7149065282768605732", "6731496", "fe78f4e40b597e3170f46831622f8e06", [
                              EffectParam("effects_adjust_blur", 0.160, 0.000, 0.800),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.16, 0.00 ~ 0.80
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
    """
    雪花光斑    = EffectMeta("雪花光斑", True, "7296707597707514406", "27986887", "b6b5e079f2c4079d72185fb43cfc7521", [
                              EffectParam("effects_adjust_background_animation", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.100, 0.000, 1.000),
                              EffectParam("sticker", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.10, 0.00 ~ 1.00
        - sticker: 默认0.60, 0.00 ~ 1.00
    """
    雪雾        = EffectMeta("雪雾", True, "7303380658934518323", "30305488", "bc0e8be4f1a2d7171824311ce9e57c44", [
                              EffectParam("sticker", 0.280, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.300, 0.000, 1.000)])
    """参数:
        - sticker: 默认0.28, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.30, 0.00 ~ 1.00
    """
    雾镜_II     = EffectMeta("雾镜 II", True, "7147920433604465159", "6731657", "627544f24ff53bde600ab918cb51a17d", [
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    震动光束    = EffectMeta("震动光束", True, "7246758527992074811", "15775885", "5c4feafe4eb534961c0df1cadb899e83", [
                              EffectParam("effects_adjust_intensity", 0.420, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.160, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.490, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.42, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.16, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.49, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.75, 0.00 ~ 1.00
    """
    震动发光    = EffectMeta("震动发光", True, "7249264623226982968", "16303237", "ce596725c52c5cfa0e8205c1cbc00585", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    震动屏闪    = EffectMeta("震动屏闪", True, "7171697545154925069", "6733311", "c83c072fdbd9921701f12498c0c00cfc", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
    """
    震动扫光    = EffectMeta("震动扫光", True, "7374053409546048052", "67503342", "3b86c556d5a92c8937b1120823bc34b2", [
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.40, 0.00 ~ 1.00
    """
    震动推镜    = EffectMeta("震动推镜", True, "7345004981029704233", "50238678", "47b846ada207d95dce6bc0501102db85", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.220, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.22, 0.00 ~ 1.00
    """
    震闪渐黑    = EffectMeta("震闪渐黑", True, "7304249285577544201", "30662744", "dfddc3aedd22941d50e768623fbd60ba", [
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.100, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.10 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
    """
    霓虹光线    = EffectMeta("霓虹光线", True, "7254125922222084663", "17710570", "c2274095125803b495db0623740fcb22", [
                              EffectParam("effects_adjust_luminance", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, 0.00 ~ 1.00
    """
    霓虹闪切    = EffectMeta("霓虹闪切", True, "7345353688774349348", "50455778", "32ab9ae1b2f18168bb5d78bfdfda9176", [
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.825, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.82, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认1.00, 0.00 ~ 1.00
    """
    马赛克闪切  = EffectMeta("马赛克闪切", True, "7308712918902641203", "32503798", "6b0566a1868f7a088935c8835052db63", [
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.130, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.13, 0.00 ~ 1.00
    """
    高速彩光    = EffectMeta("高速彩光", True, "7343527966145516042", "49475327", "e92f5749fec01ea61ad9d6747d808f82", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    鱼眼_II     = EffectMeta("鱼眼 II", True, "7023664868083372580", "1418072", "3961e7c38420d89d64c5d267a3068254", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.80, 0.00 ~ 1.00
    """
    鱼眼_III    = EffectMeta("鱼眼 III", True, "7051881765975101983", "1521356", "b2620a812f8a4e48121a0e18cf36233e", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.30, 0.00 ~ 1.00
    """
    鱼眼_IV     = EffectMeta("鱼眼 IV", True, "7091597643553444359", "1790048", "5977716750083a4ded0565086be43e07", [
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.55, 0.00 ~ 1.00
    """
    黑白胶片    = EffectMeta("黑白胶片", True, "7085992144627831326", "1691558", "708a2e34f1ecf5774e910d8da7099304", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
