"""记录剪映自带的视频特效, 此文件主要由程序生成"""

from .effect_meta import Effect_enum
from .effect_meta import Effect_meta, Effect_param

class Video_scene_effect_type(Effect_enum):
    """剪映自带的画面特效类型"""

    _1998       = Effect_meta("1998", False, "6981791065204331044", "1183068", "d53096e8139dd33f7a2be6adcd7ce56b", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    _70s        = Effect_meta("70s", False, "6706773500792689165", "634717", "0fe827460716d30e76cb3f244b9b1010", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    _90s画质    = Effect_meta("90s画质", False, "6760946510910722564", "634889", "d2b4c0ed72e66c6ae61e0ebbc7d008bf", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.630, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.580, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.510, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.63, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.58, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.51, 0.00 ~ 1.00
    """
    DV录制框    = Effect_meta("DV录制框", False, "6878115805498708493", "934600", "4828fe3f6a8bdf99e57febe27006d33b", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.20, 0.00 ~ 1.00
    """
    DV界面      = Effect_meta("DV界面", False, "6974600764027048462", "1164160", "ed29f490b4ccb7f00138f400b05459b5", [])
    I_Lose_You  = Effect_meta("I Lose You", False, "6899746903735407117", "972753", "8486881738dcb661bcd49f490a548d47", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    I_Love_You  = Effect_meta("I Love You", False, "6899746786294895112", "972754", "dfa377da1cc1858ae5d5126488c5cb67", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    JVC         = Effect_meta("JVC", False, "7102302420310430215", "2254788", "6060fe9faac1a35dd89c4362c57bd451", [
                              Effect_param("effects_adjust_color", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.90, 0.00 ~ 1.00
    """
    List边框    = Effect_meta("List边框", False, "6981463637676266020", "1181892", "80a8d14e52a06b47dbb24ddeb7b65f1c", [])
    MV封面      = Effect_meta("MV封面", False, "6925314612204147214", "1033288", "658b5a2a87b51d71f8f968546790257a", [
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    New_Year    = Effect_meta("New Year", False, "7041771617315197453", "1483460", "b3322fbbf99e1d4c9da1fb0b1e97d1a6", [
                              Effect_param("effects_adjust_size", 0.160, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.336, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.339, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.16, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    PS边框      = Effect_meta("PS边框", False, "6860306184595837448", "884226", "a787cee77871e18ae45ccd09fa7f6ac9", [])
    RGB描边     = Effect_meta("RGB描边", False, "6922698007653650957", "1025970", "175536eb523aae867ae4b8cb94f09211", [
                              Effect_param("effects_adjust_speed", 0.670, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    VCR         = Effect_meta("VCR", False, "6876012864679711245", "931458", "6b5dfc171f7c82078c76ffbcb2f6c003", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    X_Signal    = Effect_meta("X-Signal", False, "6709706971638927875", "634719", "218223a1507ca3cac6b93dd8335882a0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    X开幕       = Effect_meta("X开幕", False, "6974024838000153096", "1162978", "59be0a7455162145039e48179ef42c20", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    betamax     = Effect_meta("betamax", False, "7239937281937642041", "14578173", "6cae0f338637ffcf210bbb45015d9538", [
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
    """
    emoji钻石   = Effect_meta("emoji钻石", False, "7078694071245476366", "1647776", "afa5891d090fe132e4cf0a7196895863", [
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.548, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    ins界面     = Effect_meta("ins界面", False, "6761646727142314509", "635133", "1081a3f864316cb7e8ee977d44a90a70", [])
    ins风放大镜 = Effect_meta("ins风放大镜", False, "6992465511455920676", "1380488", "afe7daae94e810f06b339c96deafb5f8", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.00, 0.00 ~ 1.00
    """
    kirakira    = Effect_meta("kirakira", False, "6706773500142555656", "693883", "45e5aac6ec5e94c4639c3671e50fb372", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.33, 0.00 ~ 1.00
    """
    ktv灯光     = Effect_meta("ktv灯光", False, "6771299914891661832", "634197", "0654e68b3db41a82a1abf02e48375e88", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    ktv灯光_II  = Effect_meta("ktv灯光 II", False, "6934938159763427876", "1054906", "53248914c97ddf4722860554d68cac9d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    windows弹窗关闭= Effect_meta("windows弹窗关闭", False, "6976562270071427598", "1169934", "f4d45d9888b6d0d78a147417e4851189", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    windows弹窗打开= Effect_meta("windows弹窗打开", False, "6976538396290191880", "1169728", "6989cff6be738ec6a047871320d3bd9f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    丁达尔光线  = Effect_meta("丁达尔光线", False, "6834008866137575950", "768190", "858aa00b8938e4f0dde79225ef119f60", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    万圣emoji   = Effect_meta("万圣emoji", False, "7021363005052948999", "1405514", "0b226c96ee570ed8c649d97f45879faa", [
                              Effect_param("effects_adjust_speed", 0.336, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    万圣夜      = Effect_meta("万圣夜", False, "6888280327949652493", "951616", "ccd9f93a03f5849a5d5cb96729bb5bec", [
                              Effect_param("effects_adjust_blur", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    三屏        = Effect_meta("三屏", False, "6706773500209664515", "635029", "a753c93aef7a37f2e86870529f2cd06c", [])
    三格漫画    = Effect_meta("三格漫画", False, "6795825532668744206", "635007", "5b738f1286b9929b36bc6a540f11ddd5", [])
    下雨        = Effect_meta("下雨", False, "6734619419890160131", "635039", "40a59ce61692a825c049cd5b15bc6ded", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    不对劲      = Effect_meta("不对劲", False, "6940134524642660895", "1068128", "0be37b64dad56d5f6f89c69165d092fd", [])
    不规则黑框  = Effect_meta("不规则黑框", False, "6865921530488951309", "898673", "2457889e649132e1a427ccd9c258e51e", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    两屏        = Effect_meta("两屏", False, "6706773500796867075", "635025", "69926ac7983e4e234c1b833e8c50896a", [])
    中枪了      = Effect_meta("中枪了", False, "6950894972291781127", "1100950", "ee96dc698c6213303442b30b963978ba", [])
    乌鸦飞过    = Effect_meta("乌鸦飞过", False, "6955028776094798366", "1113160", "a2583447f1ec5767bf063a831b893b9e", [])
    九屏        = Effect_meta("九屏", False, "6719657094741496333", "635011", "8abb86f5699f22f9d2c8d1647458b55a", [])
    九屏跑马灯  = Effect_meta("九屏跑马灯", False, "6726773973683540491", "635031", "0bc85f7544b92909bfef4d20ad17c256", [])
    亮片        = Effect_meta("亮片", False, "6715209448521994755", "634129", "b27dcf2220fd8d3ff7216d9364d07b62", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    人鱼滤镜    = Effect_meta("人鱼滤镜", False, "6766876614862049795", "634199", "f97bd68cfc43174bcb30406a6fc46952", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    仙女变身    = Effect_meta("仙女变身", False, "6746483363567112707", "634173", "b45f02e327c3c242c54f91655798d9c0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    仙女变身_II = Effect_meta("仙女变身 II", False, "6747515070114173447", "634171", "6963f2dab25279d695f581922ce9f87f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    仙女棒      = Effect_meta("仙女棒", False, "7314565034586149403", "35504704", "322d997e0f5a8a9af19acd3c871b98ff", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    仙尘闪闪    = Effect_meta("仙尘闪闪", False, "6963476143370408485", "1133662", "8b9da7f7b3cdd95bd73cc2444433017e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    低像素      = Effect_meta("低像素", False, "6810945511005098509", "703237", "07980fba1cb9edb304a39feaa92f009c", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    低像素_II   = Effect_meta("低像素 II", False, "6811399125544735245", "703239", "01c40b95e4a5b8f850bad330a1864f6a", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    倒计时_II   = Effect_meta("倒计时 II", False, "7051887173276013093", "1521390", "e01f6dadb794566d1ea3364d564f3f59", [
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    像素画      = Effect_meta("像素画", False, "7081557169539125791", "1663132", "0e6597e2bcbc35fe670bd05501ff37ed", [
                              Effect_param("effects_adjust_color", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.755, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.688, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.76, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.69, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.00, 0.00 ~ 1.00
    """
    像素纹理    = Effect_meta("像素纹理", False, "6763903685983474189", "634785", "d132cd0508064d64e92b946adfa5c8be", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    光斑虚化    = Effect_meta("光斑虚化", False, "7297154514262430259", "28151372", "2748cc7e4a94448bddefe35749cce1db", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
    """
    光斑飘落    = Effect_meta("光斑飘落", False, "6899747276718084622", "972749", "5106ce263097acfbe5f8319841bc1e7a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    光晕        = Effect_meta("光晕", False, "6714239617916211716", "634095", "91a3d5329874b35dad2cf9fbf82956af", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    光晕_II     = Effect_meta("光晕 II", False, "6709701759398318604", "634093", "24ade7e79a0d72d1fe5792997640e15f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    全剧终      = Effect_meta("全剧终", False, "6710109932122804750", "634079", "b756f1d59534d07571ab6fac16d8bfda", [])
    六屏        = Effect_meta("六屏", False, "6719657243039502851", "635013", "95d23405c9441a388784c0749ab99471", [])
    关月亮      = Effect_meta("关月亮", False, "6774656266833760780", "634277", "af6c277f693f08679dc142591bc97c52", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.33, 0.00 ~ 1.00
    """
    冰冷实验室  = Effect_meta("冰冷实验室", False, "7019265849047388680", "1398372", "0ba96868fd684b80b4cb82f058f35dc9", [
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.267, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.27, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    冰霜        = Effect_meta("冰霜", False, "6896417042090430989", "966514", "17d279016b1f0961c4e0167f2554b0f5", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    冰霜_II     = Effect_meta("冰霜 II", False, "7047048873897890334", "1499080", "f278e4a04de56a4fbe693e2014f5da9e", [
                              Effect_param("effects_adjust_speed", 0.530, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.53, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    冲击波      = Effect_meta("冲击波", False, "6967180577875169799", "1146394", "ad8e0a154e7a3c78dc23407ec23da9b2", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    冲刺        = Effect_meta("冲刺", False, "6790536507905020430", "635003", "7efa92b9cc009384af9b207474f52b24", [])
    冲刺_II     = Effect_meta("冲刺 II", False, "6781392637216690700", "635001", "5781353d9e23652896b0dd8c43a51162", [])
    冲刺_III    = Effect_meta("冲刺 III", False, "6774324121783243271", "634981", "a2794140abd30a19ba136059f9f89e88", [])
    冲屏闪粉    = Effect_meta("冲屏闪粉", False, "6858138911487562248", "875969", "98753cc737cac50d460ec6f204cdae5b", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    凄凉        = Effect_meta("凄凉", False, "6955021464684728846", "1113134", "0491da81159994e95a68b3087a8709f3", [])
    几何图形    = Effect_meta("几何图形", False, "6871054818241155592", "920550", "0c558210a312c46568635767a3600a08", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    刀光剑影    = Effect_meta("刀光剑影", False, "6740539604509659662", "634741", "8017d7de152a4083d0607b903d716943", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    分屏开幕    = Effect_meta("分屏开幕", False, "7232198317671715385", "13525811", "98ecc4fbd0e619bddad881dc93a94964", [
                              Effect_param("effects_adjust_speed", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
    """
    初雪_I      = Effect_meta("初雪 I", False, "7173558688605540901", "6940749", "8bbb39ead793c59a4baec469890be670", [
                              Effect_param("effects_adjust_speed", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    加载甜蜜    = Effect_meta("加载甜蜜", False, "6924873263994638856", "1031291", "224dafbed2fc8e3711e1cecacf68a95c", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    动感模糊    = Effect_meta("动感模糊", False, "7009120603055591943", "1368758", "167deb8c5b35d5a3097cb107693c62c3", [
                              Effect_param("effects_adjust_horizontal_shift", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_shift: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.85, 0.00 ~ 1.00
    """
    动感荧光    = Effect_meta("动感荧光", False, "6755761739242934798", "635125", "d9f1ac0e1677dcd4475235ea113f03fa", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    动感蓝带    = Effect_meta("动感蓝带", False, "6970598283378954765", "1155430", "28edc10c2a172ca68f6be21037700538", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    单色涂鸦    = Effect_meta("单色涂鸦", False, "7265798651019006521", "20412423", "8a63108339eeb62c0a26122e2f22a850", [
                              Effect_param("effects_adjust_color", 0.300, 0.050, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.570, 0.000, 0.810),
                              Effect_param("effects_adjust_horizontal_shift", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.000, 0.000, 1.000)])
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
    南瓜光斑    = Effect_meta("南瓜光斑", False, "6992844454453318157", "1403930", "3626a4cba39f68ed0bbf43b58c023e07", [
                              Effect_param("effects_adjust_speed", 0.336, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    南瓜笑脸    = Effect_meta("南瓜笑脸", False, "6888208083202347534", "951196", "e28abcdb93864f4d4c1d340e9ce567a5", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    卷动        = Effect_meta("卷动", False, "6719657168292811278", "634735", "613ab501b1260fee424d266c6a214b5e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    原相机      = Effect_meta("原相机", False, "6753416178909057549", "635137", "bc6e1e30a3e6efd3ad60939a09e66323", [])
    友友商店    = Effect_meta("友友商店", False, "6977709836993565220", "1173234", "6fd942a59a1b4010a23b19f74a8fb08a", [])
    反转片_I    = Effect_meta("反转片 I", False, "7153084450593575454", "5114825", "442b39ec01b7ddefd1a2dfe1ce66d00e", [
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    发光        = Effect_meta("发光", False, "6961701455262650916", "1126104", "43648253eed7fb8ea727d167d28cd768", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.40, 0.00 ~ 1.00
    """
    取景框      = Effect_meta("取景框", False, "6712739398984667651", "635089", "1915e124716f1967476f78970f6e90b9", [
                              Effect_param("effects_adjust_noise", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    取景框_II   = Effect_meta("取景框 II", False, "6871187132195541517", "920935", "a8af25fab9ceb2a477fb007d3dfc72b1", [])
    变形了      = Effect_meta("变形了", False, "6940134629282157064", "1068127", "45a40940622ed9173d57e23ff1b3ddee", [])
    变彩色      = Effect_meta("变彩色", False, "6720492336788279815", "634053", "0178a55e4f8c7deec8786d78d875d45e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    变清晰      = Effect_meta("变清晰", False, "6719658716750156291", "634019", "feb43ab124f2c4bc8ee045a773741ed9", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
    """
    变清晰_II   = Effect_meta("变清晰 II", False, "6948352810895282724", "1146596", "da0c95a0f050f7e26e672dfdcbddc226", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    变焦推镜    = Effect_meta("变焦推镜", False, "7296418835429593651", "27896191", "1ef600710b33cc1e4d6f858c47e4b98a", [
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    变秋天      = Effect_meta("变秋天", False, "7012941093520020004", "1381700", "c7aaafd076935ba5a0a42e58365a49cf", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    变黑白      = Effect_meta("变黑白", False, "6730911849706951179", "634055", "d38bd3379c22f994fc3f0819998962c9", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    告白氛围    = Effect_meta("告白氛围", False, "6798021156331852295", "635005", "ed6536056d82bcd5849014db48d9d912", [])
    咔嚓        = Effect_meta("咔嚓", False, "6752780026900386317", "634073", "c742af6913646f7c936642aae51d58d2", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    哈哈弹幕    = Effect_meta("哈哈弹幕", False, "6952852858656002590", "1106302", "777c2c44707c03f6e541c8d954b21f8a", [])
    哈苏胶片    = Effect_meta("哈苏胶片", False, "7078598928056193566", "1646830", "2eead808b8408e1fa4b74b6ad3c74b8d", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.30, 0.00 ~ 1.00
    """
    唱片        = Effect_meta("唱片", False, "6978764021637845541", "1174596", "d4fef5476754cbe563d5004097369290", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    唱片封面    = Effect_meta("唱片封面", False, "6987741974455390734", "1196734", "11ca22f7daac786267a46f99dad47be3", [])
    啊啊啊啊    = Effect_meta("啊啊啊啊", False, "6951661272827957790", "1104164", "cec37f504863cc89308c256482286660", [])
    噪点        = Effect_meta("噪点", False, "6706773498510971404", "634061", "3e5fc04a3ddff85aadb6b52681f00bcd", [
                              Effect_param("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
    """
    四屏        = Effect_meta("四屏", False, "6706773500490682888", "635027", "f0074ead79e0a8dd9a10518667beb0f1", [])
    回弹摇摆    = Effect_meta("回弹摇摆", False, "7146090225855369742", "4720539", "e13659f2365eb5bc295f93342e50139f", [
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
    """
    回忆文件夹  = Effect_meta("回忆文件夹", False, "6998352498062791205", "1227934", "cf7de583f8e09da1476df20d95fc85f2", [])
    回忆胶片    = Effect_meta("回忆胶片", False, "6987725478912070174", "1196624", "3f4f6d7ce71f67e1e61b91d366da4e19", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
    """
    圆形虚线放大镜= Effect_meta("圆形虚线放大镜", False, "7065242222068765198", "1569306", "44370286a32ad2e26535a6af4842aa0b", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.00, 0.00 ~ 1.00
    """
    圣诞光斑    = Effect_meta("圣诞光斑", False, "6769436675958379021", "634209", "dd982dabe21c82f51a9815df29f83f09", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    圣诞星光    = Effect_meta("圣诞星光", False, "6767219683901837832", "634207", "3e41badb29cc40f017f2ece636d26557", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    地狱使者    = Effect_meta("地狱使者", False, "7007684840506003999", "1406882", "2338b8056d16c87a210717ef9bdc28b5", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    基础黑框    = Effect_meta("基础黑框", False, "6712316216905568772", "635127", "534a1c475b222dfc97420bbaf85b7540", [])
    塑料封面    = Effect_meta("塑料封面", False, "6814664313496670728", "703221", "4df02db49968718592fe29998506b8e2", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    塑料封面_II = Effect_meta("塑料封面 II", False, "6814664561082241550", "703219", "204ce6bc753bbc228d489e580c799768", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    塑料封面III = Effect_meta("塑料封面III", False, "6815457699505902087", "703217", "48d99133cab78a4a9b178d8f7fe7be66", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    复古DV      = Effect_meta("复古DV", False, "6865959646092333576", "898868", "19e1584168d4d3570a91185b8149ad03", [
                              Effect_param("effects_adjust_blur", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
    """
    复古DV_II   = Effect_meta("复古DV II", False, "6869650937841979911", "909740", "6979960d3bda8144b3406dee17e7255a", [
                              Effect_param("effects_adjust_blur", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
    """
    复古DV_III  = Effect_meta("复古DV III", False, "6986958810619318792", "1194896", "ff4ee88f3d727ac817750ae84df099cc", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    复古DV_IV   = Effect_meta("复古DV IV", False, "6994703188611830303", "1217306", "d97c48bb4c8048cbeb2ec8ca8e16e43e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.55, 0.00 ~ 1.00
    """
    复古发光    = Effect_meta("复古发光", False, "6993267867214942733", "1212776", "cfea69839054bf3cd30f7a2ac3727ea4", [
                              Effect_param("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.60, 0.00 ~ 1.00
    """
    复古多格    = Effect_meta("复古多格", False, "6875631945510818318", "926324", "19a3d5873d394ff550d6a4367ef18a45", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
    """
    复古弹窗_I  = Effect_meta("复古弹窗 I", False, "6709708058852856327", "635103", "2c2502e679630278461b6ad9d8482928", [
                              Effect_param("effects_adjust_noise", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
    """
    复古弹窗_II = Effect_meta("复古弹窗 II", False, "6764667280681865731", "635143", "168f6b6dfc18d80bf35853d6b7774030", [])
    复古漫画    = Effect_meta("复古漫画", False, "6847440397027774984", "784724", "1f89b68447a46e9feb69654e4dc97a7f", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    复古甜心    = Effect_meta("复古甜心", False, "6926817888632312333", "1039434", "80dbaf8bbb2d7cecdaff271656a58126", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    复古碎钻    = Effect_meta("复古碎钻", False, "6948700335481295374", "1094804", "56f3d29724754f5fc9d50c7bf6c02e28", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    复古蓝调    = Effect_meta("复古蓝调", False, "7078935944459457061", "1648234", "971c462f47f17dd2827ad4fde77fc015", [
                              Effect_param("effects_adjust_sharpen", 0.630, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.630, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_sharpen: 默认0.63, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.63, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    夏日冰块    = Effect_meta("夏日冰块", False, "7237437172733710909", "14244311", "46b643fafe2c93bfc6607b2fe5fdd429", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.230, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.23, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    夏日泡泡_I  = Effect_meta("夏日泡泡 I", False, "7104624152044114462", "2488948", "9f8219296472225136b6e73bc4c23206", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.336, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
    """
    夕阳        = Effect_meta("夕阳", False, "6820595030743323149", "719376", "766398e7682640dc13bceb3f448847dc", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    夕阳_II     = Effect_meta("夕阳 II", False, "6823659895221391886", "720788", "eea48333e37961c63e8d45077552de5a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    夕阳_III    = Effect_meta("夕阳 III", False, "6836996542310650381", "762382", "6deca5bd30382b52c6a7985cee5c4ca2", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    夜蝶        = Effect_meta("夜蝶", False, "6748376019524129292", "634175", "8a1a97c0b237adfb31c8ae55faa64e74", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    夜视框      = Effect_meta("夜视框", False, "6733023209978860035", "635131", "cef5df7500848aeee3f4ea15c6cdaa5b", [])
    大雪        = Effect_meta("大雪", False, "6767148963503018503", "635063", "950d1e82cf0093f609e864d11f8a005d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    大雪纷飞    = Effect_meta("大雪纷飞", False, "6894517304487318024", "961896", "84aa80de0bf14d5924dab46be29f7b5a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    天使光      = Effect_meta("天使光", False, "6721949326022545928", "634143", "37c4098ac98fc25188a5a727064a7729", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    天使降临    = Effect_meta("天使降临", False, "7020715912596558366", "1402689", "be7a34ae22c8b39d1750a602757e4867", [])
    失焦        = Effect_meta("失焦", False, "6984625607376114190", "1188938", "468cbf025f095d34bc7dd08462c94eae", [
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    夸夸弹幕    = Effect_meta("夸夸弹幕", False, "6956147849356644894", "1115952", "9a0e752e8d60267d088a2ade9fb7299d", [])
    夺冠        = Effect_meta("夺冠", False, "6986857922076611080", "1194360", "fae722df471ae30a898ace2990cbbf3d", [
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    孔明灯      = Effect_meta("孔明灯", False, "6734215575196668428", "635037", "f701053aea29c2163b02f98fd9c755ec", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    孔明灯_II   = Effect_meta("孔明灯 II", False, "7008056576514724365", "1363340", "c1a6557f355c41e09fa4c2723d5f5f3e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    字幕投影    = Effect_meta("字幕投影", False, "6828021842695950856", "747802", "ad0ff707e15d0e2dedcc23ef0c57c29a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    字幕投影_II = Effect_meta("字幕投影 II", False, "6829181074954785294", "747910", "d6388dec46d30dda96d8a273616978eb", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    字幕投影_III= Effect_meta("字幕投影 III", False, "6847378675894063623", "784366", "5c5ede6eb3a35e275167b8845c7ee7d5", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    字幕投影_IV = Effect_meta("字幕投影 IV", False, "6858139153020752397", "875967", "ebd3c54c9dbfe73027fd9d480c175888", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    定格闪烁    = Effect_meta("定格闪烁", False, "6998099471565328926", "1227402", "03704af752f236eec942f78ae1190d41", [
                              Effect_param("effects_adjust_speed", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    小剧场      = Effect_meta("小剧场", False, "6955083477708444174", "1113428", "602daf84aef020a2dcba8cbd52182b66", [])
    小动物      = Effect_meta("小动物", False, "6965381784674505246", "1138384", "93e09d8cd1a85e9faae8da2212be88eb", [])
    小花花      = Effect_meta("小花花", False, "6926823177670627848", "1039448", "6fe0a146c0133191fd663c439f213236", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    少女心      = Effect_meta("少女心", False, "6992842225541452325", "1209684", "41607b261ff3c0999a2c43370dd8c442", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    少女心事    = Effect_meta("少女心事", False, "6924872492381114894", "1031294", "ebba75bb53013a6347814b486c6063eb", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    少女星闪    = Effect_meta("少女星闪", False, "6805098811694780942", "703255", "830c6652734b4d6c12604e6f5832c6a1", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    左右摇晃    = Effect_meta("左右摇晃", False, "7166435460321907207", "8430539", "02b826db1b4f972ec812d76b50a49e05", [
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
    """
    布拉格      = Effect_meta("布拉格", False, "6869626257709994510", "909545", "b9b8d37e73f8a5a1c0abff8d6c7cd1b0", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    幻彩文字    = Effect_meta("幻彩文字", False, "6760975890806477319", "634737", "0d367c9f530e2fe08aef913cf1451443", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
    """
    幻影        = Effect_meta("幻影", False, "6723059630676644364", "634751", "44cb0b2f810fa3119f2c9f1ae396db9d", [
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    幻影_II     = Effect_meta("幻影 II", False, "6898958754792870413", "971332", "14e6364b3a6a1485f2583bdfc32b9f9a", [
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    幻术摇摆    = Effect_meta("幻术摇摆", False, "6926400232615842318", "1038152", "3bb76ef02392a04f5b387dbd46942458", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    幻觉        = Effect_meta("幻觉", False, "6709706311455478285", "634723", "1fa56d867a4651cbefbf6a4f669aeafc", [
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    广角        = Effect_meta("广角", False, "7086792017837036046", "1700284", "646ffb6188a447622926872c4fc453d6", [
                              Effect_param("effects_adjust_intensity", 0.450, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.45, 0.00 ~ 1.00
    """
    庆祝彩带    = Effect_meta("庆祝彩带", False, "6984685757508096520", "1189232", "42197cc2549fafa41c4854c4ee086074", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    开幕        = Effect_meta("开幕", False, "6706773534074491403", "631211", "7afa9c82c3d221742bb42a3b01d4fce7", [])
    开幕__II    = Effect_meta("开幕  II", False, "6708899027976458760", "631213", "9fd3ee125c1319e1a3d2345849bef96b", [])
    强锐化      = Effect_meta("强锐化", False, "6711567084741988876", "634783", "c9ae5be2cd096747898e905fe2b6836b", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.620, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.62, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    录像带      = Effect_meta("录像带", False, "6706773534074475012", "634887", "c880d7f9eb6b4f94bf4e8f790fcf3dc0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.40, 0.00 ~ 1.00
    """
    录像带_II   = Effect_meta("录像带 II", False, "6771299859803673101", "634811", "12b20ba900b09a9cd833ffb15eec5f74", [
                              Effect_param("effects_adjust_noise", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.50, 0.00 ~ 1.00
    """
    录像带_III  = Effect_meta("录像带 III", False, "6804357689859117581", "703251", "de0caa2ec7151990960b56f62fedd3fc", [])
    录制框      = Effect_meta("录制框", False, "6709725898762883595", "634801", "bbed85838ac97f63298e51e2f2b0bb03", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    录制边框    = Effect_meta("录制边框", False, "6720541178044879367", "635121", "5a388c880fe2fec47424d62a1e81c2c1", [])
    录制边框_II = Effect_meta("录制边框 II", False, "6720541079080276484", "635119", "aeb6eaaa2881ed69afb5ece40c7c4eb4", [])
    录制边框_III= Effect_meta("录制边框 III", False, "6894451240382501389", "961624", "bc759f18216aac435a0cf29b69bb5051", [])
    录制边框_IIII= Effect_meta("录制边框 IIII", False, "6723065859260027403", "634063", "93297cd4887ae225ecc81f79e89c156b", [])
    彩信        = Effect_meta("彩信", False, "7023692066152518152", "1418386", "d019bb0c5188a75893b08562c9951a4f", [
                              Effect_param("effects_adjust_vertical_shift", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
    """
    彩噪画质    = Effect_meta("彩噪画质", False, "7135711291473138184", "4253680", "fbdce889885763ee82ffa7138de4d36b", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
    """
    彩带        = Effect_meta("彩带", False, "7012933493663470088", "1381644", "c8b3549975f0ddca9247553c2ce79564", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    彩色描边    = Effect_meta("彩色描边", False, "6966904744564494878", "1143666", "fd18f1469ac653e38814a8f6ea7db6bd", [])
    彩色漫画    = Effect_meta("彩色漫画", False, "6795430958737658382", "634947", "329880da582a412ad4db0451755a2065", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    彩色负片    = Effect_meta("彩色负片", False, "6914995893653475847", "1005840", "a78b49205a5d3b7fbc04a19aebce80ea", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    彩虹光      = Effect_meta("彩虹光", False, "6719758141573042692", "634161", "e39f46b0d21562c05fecfd9404d5a22f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    彩虹光_II   = Effect_meta("彩虹光 II", False, "6738279134692119047", "634159", "03814fa76660bb3db88128e2a5ef000f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    彩虹光晕    = Effect_meta("彩虹光晕", False, "6768721870360416782", "634213", "3f04c39cc212c63ac3caa048f6c34588", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    彩虹射线    = Effect_meta("彩虹射线", False, "6808837459728667144", "703249", "5c817bb9e37fafa3f03966051050040c", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    彩虹幻影    = Effect_meta("彩虹幻影", False, "6756845151630397960", "634281", "a5f61f00265cbcf6fbc430780f5b4c03", [
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    彩虹气泡    = Effect_meta("彩虹气泡", False, "6717434470128947725", "634127", "cf2687ea75161551a44016ef2ee4782d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    彩虹爱心    = Effect_meta("彩虹爱心", False, "6924873147053249031", "1031292", "235be137b3284f3d586e03f021951dac", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    彩钻        = Effect_meta("彩钻", False, "6986188114490298888", "1192480", "ba1ae230f2b24fe3383802194fb18e5d", [
                              Effect_param("effects_adjust_size", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    心河        = Effect_meta("心河", False, "6740821434307711496", "634273", "e01e24abb316c5d1ef6f71946aeb1f16", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    心跳        = Effect_meta("心跳", False, "6723068356821258764", "634753", "fb26e9377ee378736086a4e60bde0cce", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    心跳黑框    = Effect_meta("心跳黑框", False, "6732383404991451656", "634049", "167ba80ce0571ba3d1d17d59f5ef5ea1", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    必杀技      = Effect_meta("必杀技", False, "6797658471840879111", "634979", "ac8846e43b1fec25f2afe182d13feb24", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    必杀技_II   = Effect_meta("必杀技 II", False, "6797346848391565831", "634977", "4e3e9d5edd2dc99af5881e3ca3d9344e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    怀旧边框    = Effect_meta("怀旧边框", False, "7113820806446060040", "3222474", "6d93d853611744ad573e113f8acd3ba6", [
                              Effect_param("effects_adjust_size", 0.636, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("sticker", 0.630, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.64, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - sticker: 默认0.63, 0.00 ~ 1.00
    """
    怀旧边框_II = Effect_meta("怀旧边框 II", False, "7039331384183230989", "1475190", "97076a8938d8f45a233d97fd240951c3", [])
    怦然心动    = Effect_meta("怦然心动", False, "6924872657083044359", "1031293", "d5e216a1700db22637509d2966004b16", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    恐怖故事    = Effect_meta("恐怖故事", False, "6888563496133333511", "952539", "5ffc4c3a4ee71dd9aa5f728da300e0f2", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    恐怖故事_II = Effect_meta("恐怖故事 II", False, "6888562369627165191", "952540", "900c63e3517b6fb24b9ed1b66c29efe0", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    恐怖故事_III= Effect_meta("恐怖故事 III", False, "6888594040959275527", "952742", "472194dc4d5622347368fc59c753d827", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    恐怖综艺    = Effect_meta("恐怖综艺", False, "7023349285592764941", "1416842", "733e0831b3facd0931d6e648e1b381fd", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.802, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    恶灵冲屏    = Effect_meta("恶灵冲屏", False, "7022838857221542414", "1413882", "c440724a491336aba4e24910d5c7f6f1", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    愛          = Effect_meta("愛", False, "6831487239164269064", "756184", "310f9f3c69c75cbb8eb25011d01d5ac4", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    我酸了      = Effect_meta("我酸了", False, "6955083374054609444", "1113430", "393059e1b508041d77792ef44ffc007b", [])
    手帐边框    = Effect_meta("手帐边框", False, "6761336384117543438", "635113", "737114bc5ff9b162c7f6fc403e308d63", [])
    手电筒      = Effect_meta("手电筒", False, "6860757586220683790", "886132", "42bd8193cfc9d60fdf4392ffaf3c5baa", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    手绘拍摄器  = Effect_meta("手绘拍摄器", False, "6997608849750364708", "1225274", "4bf0e18f35a6ce0778455fdce692415d", [])
    手绘边框_II = Effect_meta("手绘边框 II", False, "6723044276625740296", "635101", "28cf85153cd70aa39187c96a74dd82e1", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    扫描光条    = Effect_meta("扫描光条", False, "6798379345783034382", "703271", "6b14aef1e0c5759061bc35cbf33ccd9f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    抖动        = Effect_meta("抖动", False, "6706773500796867084", "634759", "950894d4ae28d859d9b7136a73265ee6", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
    """
    折痕        = Effect_meta("折痕", False, "6810944968396378638", "703227", "3f7adc8176999d58e232b5fa456088d5", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    折痕_II     = Effect_meta("折痕 II", False, "6925250879259939336", "1032270", "4efd4758f897b1d364549a688129e5d5", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    折痕_III    = Effect_meta("折痕 III", False, "6925288456943833608", "1032322", "7d4cb9c576864bc421faa8d9d2f4d67e", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    折痕_IV     = Effect_meta("折痕 IV", False, "6925288650011841031", "1032321", "b04966da3a2bbd9212aec61aaa995c33", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    折痕_V      = Effect_meta("折痕 V", False, "6925292438391099912", "1032418", "1530211bc181cd4003243fa6265574db", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    报纸_今日热门= Effect_meta("报纸:今日热门", False, "6711575336955417095", "635091", "d10a4d42b6b91f3f899a1692bddfca08", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    摇摆        = Effect_meta("摇摆", False, "6709706542674874888", "634743", "bb8e9483313416d32bea215d57855490", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    摇摆_II     = Effect_meta("摇摆 II", False, "6821460674577699342", "717392", "332436443a8cbe9014d6bf7c8531ff60", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    撒星星      = Effect_meta("撒星星", False, "6839514681044898311", "768182", "620d63550356df332ba5c014b310d6d2", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    撒星星_II   = Effect_meta("撒星星 II", False, "6849588023714124295", "788728", "5c5349039a938e2348ae58a7dee34302", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    撕纸涂鸦边框= Effect_meta("撕纸涂鸦边框", False, "6969851947306193416", "1153996", "592359a5945a5723aa7ed8b50e8b5ef4", [])
    播放器      = Effect_meta("播放器", False, "6758630566578360845", "635141", "187409b4bd22026b48df1bacdf2f3cfa", [
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    播放器_II   = Effect_meta("播放器 II", False, "6792819149945967111", "635139", "38b3630f57f017191fb1d1bbbf9185f1", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    擦拭开幕    = Effect_meta("擦拭开幕", False, "6841459176510591496", "773560", "6725bf6b227fc208a7bd343661637320", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    放大镜      = Effect_meta("放大镜", False, "7051836120224502308", "1520514", "5f89a973e9cea025690bdb37a293a959", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
    """
    放映机      = Effect_meta("放映机", False, "7067049946049942030", "1576250", "a8bffa5b39a0ff0c1cdc278216e5041d", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.801, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.339, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.34, 0.00 ~ 1.00
    """
    放映机卡顿  = Effect_meta("放映机卡顿", False, "6706773499031081483", "634775", "53f4a563209223baecaaec2cfff02afe", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    放映机抖动  = Effect_meta("放映机抖动", False, "6771320983065203213", "634787", "3d7d53f809b52f7370380f358ef6081c", [
                              Effect_param("effects_adjust_range", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.25, 0.00 ~ 1.00
    """
    放映滚动    = Effect_meta("放映滚动", False, "6970890075907297806", "1155966", "d29c13ced2fda5dca2a486dc9d5b1c6f", [])
    故障        = Effect_meta("故障", False, "6707050322696606222", "634797", "ec4f1908b716eec1e47b48b9c1ac836f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    故障_II     = Effect_meta("故障 II", False, "6738265357825348103", "634795", "d4435f333055899ab5140a4cc69aced6", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    故障读条    = Effect_meta("故障读条", False, "6912013942097187336", "999316", "1ae904081a2d916d6d893e538304494c", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.620, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.62, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    文字闪动    = Effect_meta("文字闪动", False, "6886710931150082573", "949372", "417b001671b78236d47f16351c7fff85", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    斑斓        = Effect_meta("斑斓", False, "7072258619646939679", "1607458", "7030b50aec89e949ea9ce706cfb1512c", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.040, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.04, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    斜向模糊    = Effect_meta("斜向模糊", False, "6871185301071467015", "920936", "7865be92e2a2b811cea9639d08dab0c0", [
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.25, 0.00 ~ 1.00
    """
    方形取景器  = Effect_meta("方形取景器", False, "6706773499031097868", "635099", "23af10c231cf1b88104e206ca5b6d9ad", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.660, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    方形开幕    = Effect_meta("方形开幕", False, "6729055410835165708", "634043", "c216a88587da0864bfe1f477f2fd1880", [])
    旋转方块    = Effect_meta("旋转方块", False, "7041504567648850445", "1482636", "d41b7b274f570518ad7aedb88e7b687e", [
                              Effect_param("effects_adjust_size", 0.714, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.71, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.25, 0.00 ~ 1.00
    """
    日式DV      = Effect_meta("日式DV", False, "6965747262165094942", "1146392", "2ba4db88748088d60090705ab0d921fd", [])
    日文字幕    = Effect_meta("日文字幕", False, "6858954575701873160", "881783", "1943875bfc98f928d2d60ac63c1a7271", [
                              Effect_param("sticker", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    日落灯      = Effect_meta("日落灯", False, "6920147678248571406", "1020046", "0a5d6dc144c4a488cc223c14ef092d05", [
                              Effect_param("sticker", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.560, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.610, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.640, 0.000, 1.000)])
    """参数:
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.56, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.61, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.64, 0.00 ~ 1.00
    """
    时光碎片    = Effect_meta("时光碎片", False, "6971332934288544286", "1157058", "97a217ce3f6f5c8a4729912f1b77ec23", [])
    时间停止    = Effect_meta("时间停止", False, "6948722700286169631", "1095262", "dce8f128927e797533d59dc0b1fb6c7d", [])
    星光        = Effect_meta("星光", False, "6717433583289504268", "634117", "18ca299d377f85452542449185ccdcd9", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星光_II     = Effect_meta("星光 II", False, "6715209934738297358", "634113", "c0629f8eb980bc1cc9853fd15fcb49cd", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星光绽放    = Effect_meta("星光绽放", False, "6760243564598268420", "634195", "af1fc6a5b22f4357b4f86ad314510851", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星光闪耀    = Effect_meta("星光闪耀", False, "6967255188730024455", "1146750", "3650ba757a4c5be9accd956d8dd47df1", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星光闪闪    = Effect_meta("星光闪闪", False, "6871055398107877902", "920549", "6fe220ca67a2f626ffd888b28172bc29", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星夜        = Effect_meta("星夜", False, "7008149210159649294", "1364164", "1c75b4cf948ba65efeb1af5a25b41a7e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星星冲屏    = Effect_meta("星星冲屏", False, "6769007480652435982", "634193", "52685a9660f7ddc2e9223f437485f4b2", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    星星坠落    = Effect_meta("星星坠落", False, "6783598688624185867", "634269", "9dbbc7ce4806c9b7cfbb722cd4c7a9d4", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星星投影    = Effect_meta("星星投影", False, "6826530141586330120", "741906", "cfbf1b6be6d23e3575caf3a026f54082", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星星灯      = Effect_meta("星星灯", False, "6903072502369489422", "977478", "9a20a02448ef8d95a81c3b16ca881742", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星星闪烁    = Effect_meta("星星闪烁", False, "6778285088485413384", "634215", "f75821b85d4f8e7be6eb42ca17f2e343", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星星闪烁_II = Effect_meta("星星闪烁 II", False, "6834010357728547335", "755806", "469b87318cdd87cefbb54223cd4633fd", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星星闪烁_III= Effect_meta("星星闪烁 III", False, "6871167583991632391", "920916", "ccdcf8be8c2d54b0c029ece6f85e4d51", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星月童话    = Effect_meta("星月童话", False, "6967255330958873124", "1146749", "310fe4000e5635f13ec28570736b60e3", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星河        = Effect_meta("星河", False, "6734498838410695175", "634265", "5d1c03757b50feee9ef6bb4ac4d4d99c", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星河_II     = Effect_meta("星河 II", False, "7010648091049071135", "1372810", "2273947aec8664bd5c7a0f410c8bebfb", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    星火        = Effect_meta("星火", False, "6715209198109463054", "634103", "c2811a4bdeb4394ae95f3aa9875dc4dc", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星火_II     = Effect_meta("星火 II", False, "6907053209173365256", "986477", "43a04949ebd13d27d7b38f5083882322", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星火炸开    = Effect_meta("星火炸开", False, "6808838081420988942", "703243", "bf25e21e5b4a025e984e2eed0a00345d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星移        = Effect_meta("星移", False, "6778284619499311623", "634267", "f1c6583c2a7227b6ccf002863fdfdf65", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星空        = Effect_meta("星空", False, "6734587005872640519", "635035", "dc11bf828dc298c85256509f24f0451d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星辰        = Effect_meta("星辰", False, "6761722814157296141", "634271", "572ed0caff4d1d4ee69b8ab9914ae69a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    星辰_I      = Effect_meta("星辰 I", False, "6946113717100614158", "1087622", "3c8c6e57ebbcca08e0202a2ce489a109", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    星辰_II     = Effect_meta("星辰 II", False, "6946453051368542727", "1089758", "4776e97efe2b615622586f9eba683b81", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
    """
    星辰_III    = Effect_meta("星辰 III", False, "6948700154874565156", "1094800", "7e62c362c751a7d4bc806e5036e1ce45", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
    """
    星雨        = Effect_meta("星雨", False, "6766488666261950989", "634187", "ec147993b7ce136beccd018d179fae2c", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    春日樱花    = Effect_meta("春日樱花", False, "6927185086685123086", "1041304", "0e308be06e990da9322e807a8a4b3783", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    春日边框    = Effect_meta("春日边框", False, "6942800783737885198", "1076064", "a8f4b178a0c820ab601f742ce4eb286a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    晴天光线    = Effect_meta("晴天光线", False, "6740540037563159047", "635071", "1d65a16823fdd3130901b3687f0107d0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    暗夜        = Effect_meta("暗夜", False, "6886698114258833934", "949350", "17b5b34a9580eca1b093e3b9b730b5ad", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    暗夜归来    = Effect_meta("暗夜归来", False, "7020715691355410951", "1402690", "7e0d21432508fde619dad195088275b8", [])
    暗夜彩虹    = Effect_meta("暗夜彩虹", False, "6823658782090859022", "720808", "123ffb581708c8e5df875d30fdf26b66", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    暗夜彩虹_II = Effect_meta("暗夜彩虹 II", False, "6824046488419570184", "741832", "8411467f9cf5520fdb9cc14151bef011", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    暗夜彩虹III = Effect_meta("暗夜彩虹III", False, "6824047157369115150", "741860", "3b1f50d0c90f48a42cdb0071beedb4a9", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    暗夜精灵    = Effect_meta("暗夜精灵", False, "6888573576870367751", "952536", "fd84a50ad750ae84e3b2ce62cd22a6e5", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    暗夜蝙蝠    = Effect_meta("暗夜蝙蝠", False, "7021786820153184775", "1407954", "bbe314aced3bb2ab605a2c7c6b0adf93", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    暗角        = Effect_meta("暗角", False, "6723086142658318860", "634057", "ef7abad9671e2f3da7993b7673ece5fc", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    暗黑剪影    = Effect_meta("暗黑剪影", False, "6886718600233619982", "949388", "e31ade9f9b38b5721fb601ad187bb163", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    暗黑噪点    = Effect_meta("暗黑噪点", False, "7022896066559218183", "1414024", "fae125ebf95a6bb9d8a4233ea9b3dced", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.801, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.801, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
    """
    暗黑蝙蝠    = Effect_meta("暗黑蝙蝠", False, "6749064512390828548", "634179", "934fcfaf5b153a5a0fc91951b9d7d61b", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    曝光        = Effect_meta("曝光", False, "6992043513365926408", "1207064", "e961c201b279f5ef164f119aa7ab2a78", [
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.60, 0.00 ~ 1.00
    """
    曝光降低    = Effect_meta("曝光降低", False, "6765766949382132232", "634659", "be1c0676764ee83d32b63afc46272c28", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    月亮投影    = Effect_meta("月亮投影", False, "6826529572536717837", "741892", "c71386afba5abc8a66cd05a5c21fab2c", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    月亮闪闪    = Effect_meta("月亮闪闪", False, "6876339287038628359", "931823", "11d24cd11738137f080ab6b050337f8f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    月光闪闪    = Effect_meta("月光闪闪", False, "6906802979861434887", "986344", "72e1573314be95270038e193db1def8d", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
    """
    望远镜      = Effect_meta("望远镜", False, "6834012604759806472", "761578", "63e50736865f6248f87b6280c5b0d88b", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    未来主义    = Effect_meta("未来主义", False, "6982870068069667365", "1185624", "5c8d55dd2769674a7c05099020ca1000", [])
    杂志        = Effect_meta("杂志", False, "6810945952451400200", "703235", "c2d0a5d79d37501fb8d49502783145e6", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    树影        = Effect_meta("树影", False, "6815830852035940872", "703215", "e94e1952adee72678c426490036dae61", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    树影_II     = Effect_meta("树影 II", False, "6820591707617235464", "719372", "068b6e28050ccaa8d0832419a0a185c4", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    格纹纸质    = Effect_meta("格纹纸质", False, "6815834305084789262", "703223", "722c3de2c3639bbcaa23b0e8ff7b9486", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    格纹纸质_II = Effect_meta("格纹纸质 II", False, "6815834434726531597", "703225", "af3ab7ecf7d9e53618301ea7652027e7", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    梦境        = Effect_meta("梦境", False, "6841460732639318542", "773088", "37faa88347805d59c7d7db2e2267e0c9", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    梦境_II     = Effect_meta("梦境 II", False, "6849235870130639368", "788039", "715227fc796386820c16198a57fd5249", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    梦境_III    = Effect_meta("梦境 III", False, "6843319622385537544", "774964", "ae67e41be59533a1fa5de82ad641563a", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    梦境_IV     = Effect_meta("梦境 IV", False, "6841460608248844813", "773086", "23336e6ee5aef71cc59e7b072fede43b", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_soft: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    梦幻雪花    = Effect_meta("梦幻雪花", False, "6894208129534267912", "961480", "0d95d3c97bfac92fd5abc0f5c04431a5", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    梦蝶        = Effect_meta("梦蝶", False, "6998050316528652831", "1406766", "9ec25a811ae581e20a53276af7a3b131", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    梦魇        = Effect_meta("梦魇", False, "7024080087163081229", "1419974", "b678d12a5275aa28637557b455299c5c", [
                              Effect_param("effects_adjust_speed", 0.336, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    梵高背景    = Effect_meta("梵高背景", False, "6967354298275467807", "1147066", "52e5b1690a75d4e6ca88c7f18f47b7e7", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    模糊        = Effect_meta("模糊", False, "6739752823140913675", "634025", "abb0b0e8472b73a42e796086c708d216", [
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    模糊开幕    = Effect_meta("模糊开幕", False, "6758752103092457991", "634071", "c0827630f211d83cc2a8258ce59d8c78", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
    """
    模糊星光    = Effect_meta("模糊星光", False, "6771299961171612174", "634255", "f40e2044c0482290ab34e4db7dfdabcb", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
    """
    模糊星光_II = Effect_meta("模糊星光 II", False, "6806254134619017741", "703247", "5f0825e579151faded0b25cdac27324f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    模糊闭幕    = Effect_meta("模糊闭幕", False, "6821460725517521416", "717394", "b42ba749d552dbb865daa4c0a8e8ae6d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
    """
    横向闭幕    = Effect_meta("横向闭幕", False, "6876339694825640455", "931822", "b7abe840af4f942b11e0ccda971d4df7", [])
    横纹故障    = Effect_meta("横纹故障", False, "6806254428358709767", "703269", "fbc084265465ab0db5ba8e2b3624c4d0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    横纹故障_II = Effect_meta("横纹故障 II", False, "6815093228216259079", "703267", "a9061d0f59a826dc552e96ecc38c94c4", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    樱花朵朵    = Effect_meta("樱花朵朵", False, "6940448547137393159", "1069014", "3c1cb50f953aea57451da040eeade612", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    橘色负片    = Effect_meta("橘色负片", False, "6914995976608420365", "1005839", "95ddc63de88b65e1782c88c300c7e90e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    欧根纱      = Effect_meta("欧根纱", False, "7273334324106105403", "21803568", "8d6a52eab248332cc91493e8856160ad", [
                              Effect_param("effects_adjust_size", 0.300, 0.000, 0.600),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.280, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.125, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.30, 0.00 ~ 0.60
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.28, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.12, 0.00 ~ 1.00
    """
    毛刺        = Effect_meta("毛刺", False, "6709706457543086605", "634711", "08b418c92900f56a493cd0efb570f0e1", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    毛玻璃      = Effect_meta("毛玻璃", False, "7031846864198570532", "1445528", "31be9d7ef329624b8b106a6a48998361", [])
    水墨晕染    = Effect_meta("水墨晕染", False, "6746486938137530884", "634101", "561b55373df7ee5e9e6f10d5cb235190", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    水彩晕染    = Effect_meta("水彩晕染", False, "6733378866686988803", "634099", "85757609b1d1f799ebf542aec9662fce", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    水波纹      = Effect_meta("水波纹", False, "6940173521905521159", "1068390", "61ab10b10def92e31b0400ac87e43088", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
    """
    水波纹投影  = Effect_meta("水波纹投影", False, "6847018706887774727", "783644", "4b0042213e23e9050cfb066f2365564b", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    水滴模糊    = Effect_meta("水滴模糊", False, "6911935918433636871", "998722", "99d7b39f93c993e17cca03313041aa8d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    水滴滚动    = Effect_meta("水滴滚动", False, "6863328348920091144", "892170", "25bf851759c3c6ebdf2036ee357866d3", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    油画纹理    = Effect_meta("油画纹理", False, "6808442362314887693", "645833", "e3fc6aa919c13ff59280907da88d2bf3", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    泡泡        = Effect_meta("泡泡", False, "6806254230614053383", "703241", "060b8178d3ac554eaa0d22e04989e70c", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    泡泡变焦    = Effect_meta("泡泡变焦", False, "7133105682881974821", "4118383", "84c9bae7a15dc1118072ee3ab1ddf3c2", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
    """
    波纹扭曲    = Effect_meta("波纹扭曲", False, "7368745372081984035", "63865672", "c0db14b731d4f04c95332348a0488089", [
                              Effect_param("effects_adjust_sharpen", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_sharpen: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.55, 0.00 ~ 1.00
    """
    波纹色差    = Effect_meta("波纹色差", False, "6709347834690277892", "634285", "57d2f602616ff3f9ce589e2b3150e364", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    流动烟雾    = Effect_meta("流动烟雾", False, "7257495407712801317", "18648774", "ab6aa4d420ef1cf322d25b24a054a7c6", [
                              Effect_param("effects_adjust_size", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.90, 0.00 ~ 1.00
    """
    流星雨      = Effect_meta("流星雨", False, "6974750495415996936", "1164794", "fa635717b7c3eeefed138087de04c267", [])
    浓雾        = Effect_meta("浓雾", False, "6751566830206194190", "635047", "b69f839d17cd1fa3ca2b67df18b95519", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    浪漫氛围    = Effect_meta("浪漫氛围", False, "6790533020215415304", "634253", "af18c87e794b96c831549e8406c8f8c5", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    浪漫氛围_II = Effect_meta("浪漫氛围 II", False, "6814667933684339207", "705081", "7021b0ea7b01f0dc0be39b091c3431a2", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    涂鸦切割边框= Effect_meta("涂鸦切割边框", False, "6969850948969566756", "1153998", "e477d2fe74226d0905247b351722848c", [])
    淡彩边框    = Effect_meta("淡彩边框", False, "6753512270598246925", "635117", "3da6d9d4146803479ed0b4ab840219a2", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    清新绿格子  = Effect_meta("清新绿格子", False, "6966132680211567135", "1141780", "add7f1470b3da2f309c52f337722fe1b", [])
    渐显开幕    = Effect_meta("渐显开幕", False, "6722343568188379661", "634041", "a299b022ab4d7a1830ac72dce3d21d95", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    渐渐放大    = Effect_meta("渐渐放大", False, "6730912024596845063", "634067", "56b46f1ebc45c47730d3f7c2569200fc", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.660, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    渐隐闭幕    = Effect_meta("渐隐闭幕", False, "6723050814006366734", "634039", "05c17ac3298c0521cd91a720850a27de", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    温柔细闪    = Effect_meta("温柔细闪", False, "6995497812221760030", "1220300", "90a28bc4dcde319ec961b8f07a81c817", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    游戏界面    = Effect_meta("游戏界面", False, "6983877697524994567", "1187140", "79fc508b1d127dc744a0b6bf9d63c8ea", [])
    满屏问号    = Effect_meta("满屏问号", False, "6950902993294201358", "1101078", "168794f69f32cdb6011ebca4b5bf3382", [])
    漏光噪点    = Effect_meta("漏光噪点", False, "6810944598874001934", "703229", "2e08fe198f1c351fb6d19ded110a5a84", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    火光        = Effect_meta("火光", False, "6748623656181568011", "634167", "8ae6b74e205a7ba0e3fcd3f01e93b72d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    火光刷过    = Effect_meta("火光刷过", False, "6803160938603090440", "705085", "94e472584aebf6d8fe65675b50184165", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    火光包围    = Effect_meta("火光包围", False, "6803162714148442632", "705033", "3d4fa21f005a3526c2f3189f29c03d0a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    火光翻滚    = Effect_meta("火光翻滚", False, "6809889314860700173", "703263", "b613ef50916282ef8dca4babe5d1006d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    火光蔓延    = Effect_meta("火光蔓延", False, "6803162375148016135", "703265", "eca67ce53f0d86e643af3dc6de2b8a0a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    灵魂出窍    = Effect_meta("灵魂出窍", False, "6706773500784284172", "634709", "7cd3e52c6ee775c334f44bec43b54325", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    炫彩        = Effect_meta("炫彩", False, "6732693992225378828", "634091", "c58f672e5d95a2ee49b3659006871671", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    炫彩_II     = Effect_meta("炫彩 II", False, "6933131104274616840", "1145374", "bd0e205c7b587098dbea50d4404ab314", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    烟花        = Effect_meta("烟花", False, "6782461740274684424", "635073", "4e7301f2c6232050b71d95e750d67861", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    烟花_II     = Effect_meta("烟花 II", False, "7010666068997837342", "1373018", "4037759ec478f5a033d160f1bab07f90", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    烟花_III    = Effect_meta("烟花 III", False, "7052201781241057805", "1522424", "5d6d7516368c1dcdfb2bb274c2600416", [
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.336, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
    """
    烟雾        = Effect_meta("烟雾", False, "6733145063997575694", "634145", "f7e8f3aee8e513dc63a56c43f58b0287", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    烟雾炸开    = Effect_meta("烟雾炸开", False, "6804317747351130638", "703261", "c4687b9722a4e7299039fd06f7956742", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    爆炸        = Effect_meta("爆炸", False, "6740540228194275844", "635067", "7b4df7ff18f6e6ccb1b49bf58611499e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心Kira    = Effect_meta("爱心Kira", False, "6896058666357625351", "965696", "74a62663b998596eb7f11485d8518b17", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    爱心bling   = Effect_meta("爱心bling", False, "6709706255105004045", "634133", "182cd7556ffdc70c9a8fdb98947f9d8c", [
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    爱心光斑    = Effect_meta("爱心光斑", False, "6709706178340852236", "634135", "58c897c26fa3df544d100541167c02b8", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心光斑_II = Effect_meta("爱心光斑 II", False, "6791647108974776839", "634261", "85619b11f963ebd32b545b069cd75221", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心光波    = Effect_meta("爱心光波", False, "6746014633942848007", "634191", "6d42bba28607f45ca90a7359b7c6ab74", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    爱心啵啵    = Effect_meta("爱心啵啵", False, "6924869659476890125", "1031295", "dce0f289716b6e4c4c7256a4ab364188", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心射线    = Effect_meta("爱心射线", False, "6805099653730669070", "703257", "d75a8189380e55c63785b24d8050f9c6", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    爱心投影    = Effect_meta("爱心投影", False, "6828020234876621325", "741958", "7515290b9cb341d5816bc502bafaabab", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心方块    = Effect_meta("爱心方块", False, "7041103714647544334", "1480898", "076a41421bbc4a6419fcccdc3c1ce80c", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.634, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.63, 0.00 ~ 1.00
    """
    爱心暗角    = Effect_meta("爱心暗角", False, "6925342127807271431", "1033842", "1991e877ef3ba32d48bcbe62a2e326cb", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    爱心气泡    = Effect_meta("爱心气泡", False, "6792405144655893005", "634235", "3b6d673988e3e82046b3159f59a5c12a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心泡泡    = Effect_meta("爱心泡泡", False, "6886709503136371207", "949386", "bc428e7342600fc4cf0daa1515f3aac6", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心爆炸    = Effect_meta("爱心爆炸", False, "6855563744123032071", "824444", "39dfc6d5b4e0a4fa623d5d5e959c4095", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    爱心缤纷    = Effect_meta("爱心缤纷", False, "6790534436153725448", "634259", "5cd7d926814e4c5b6baca975bf3f8a80", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心缤纷_II = Effect_meta("爱心缤纷 II", False, "6792092999468716558", "634257", "d7391e2297dbeea1409bd53de6f2064e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    爱心跳动    = Effect_meta("爱心跳动", False, "6790547496394297863", "634275", "68b31593ac0e5c661e1d610ce540d64b", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    爱心跳动_II = Effect_meta("爱心跳动 II", False, "6858138763290219021", "875970", "e246526e1234846c538b718d4be7dbf2", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    爱心闪烁    = Effect_meta("爱心闪烁", False, "6792109800135070222", "634231", "e8eb70ffb513761efe8662314e411974", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    牛皮纸关闭  = Effect_meta("牛皮纸关闭", False, "6966139059194303013", "1140082", "f2fb4e0bf0ea133b39eb068152acce74", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    牛皮纸打开  = Effect_meta("牛皮纸打开", False, "6966136913010889223", "1140078", "bc67263387f709f884b84337e67fe6d6", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    牛皮纸边框_I= Effect_meta("牛皮纸边框 I", False, "6966139444382405134", "1140086", "db111daab71339846516a5c01402752e", [])
    牛皮纸边框_II= Effect_meta("牛皮纸边框 II", False, "6966139579912950286", "1140085", "e91bd852184f4ac248f6291a4c8d1826", [])
    玫瑰花瓣    = Effect_meta("玫瑰花瓣", False, "6734619627051028996", "635051", "abd9d7c89fa42048f1ad1fe68b867ba0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    玻璃破碎    = Effect_meta("玻璃破碎", False, "6912015453892121102", "999326", "cb76d83cf3c3b3674b2207c33bcaf67d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    甜心投影    = Effect_meta("甜心投影", False, "7058961500060258847", "1552216", "24068e8b49b64d8802e7d62ca05acc07", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.435, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.44, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
    """
    生日快乐    = Effect_meta("生日快乐", False, "6899747371593241096", "972748", "7e2e3e9671c48ebdd4abf0f8efa0b3eb", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    电光包围    = Effect_meta("电光包围", False, "6809889225144537613", "703259", "41db536d57ca3c1d547f13b658c2386d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    电光漩涡    = Effect_meta("电光漩涡", False, "6797341815377760782", "634975", "363d8c0772a4e49a3f51f233748dd86b", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    电子屏      = Effect_meta("电子屏", False, "6847692508449739278", "785074", "7e3720dced915006968402e0f245f955", [
                              Effect_param("effects_adjust_noise", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    电影刮花    = Effect_meta("电影刮花", False, "6722366799003783692", "634789", "10c7d224fcc46291509c22a902efeb6e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    电影感      = Effect_meta("电影感", False, "6719333680713568771", "634029", "1beeb560b0796fc181f265df1e83fa66", [])
    电影感画幅  = Effect_meta("电影感画幅", False, "6746135410218373646", "634083", "f37cf7f307b394d1d496d5264c7b2a86", [
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    电脑桌面    = Effect_meta("电脑桌面", False, "7026619341839798820", "1482288", "1625f25739fdc13d63b9867589929cae", [
                              Effect_param("effects_adjust_color", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    电视关机    = Effect_meta("电视关机", False, "6719656840646365707", "634805", "c2ef989d8286f4b2e5a747bca129602a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    电视开机    = Effect_meta("电视开机", False, "6719661856434164237", "634807", "b7f303766220a86078204b79a4db2566", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    电视彩虹屏  = Effect_meta("电视彩虹屏", False, "6852503085672043021", "815546", "d6ef86b7e37c1996e336d6541f5c4d7a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    电视纹理    = Effect_meta("电视纹理", False, "6763933311933878791", "634803", "12829eb28e30b3c046bcb9ce3fdd8641", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
    """
    画展边框    = Effect_meta("画展边框", False, "6839527903424680456", "768176", "594fd22d6effa8153b7a619746b1dd0f", [])
    白噪点边框  = Effect_meta("白噪点边框", False, "6970599572976439839", "1155426", "ffe0f3ffa043687873060dabb41e45ac", [])
    白胶边框    = Effect_meta("白胶边框", False, "6865979592264389127", "898956", "77fb2991364f2882ef4b61317f7a10dc", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    白色描边    = Effect_meta("白色描边", False, "6953169122649707045", "1107244", "647776c50dafcbfab55f1dcb36d28792", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    白色渐显    = Effect_meta("白色渐显", False, "6723790385069429262", "634037", "94b1df840d30218f14e8a5e509df5c8e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    白色爱心    = Effect_meta("白色爱心", False, "6868556923503907342", "904792", "6fbffdaff4f4a6f3894af0a29f5fe8cc", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    白色线框    = Effect_meta("白色线框", False, "6753512551536923149", "635109", "66d6c8dffd954669fbb74410f28ac6c0", [])
    白色边框    = Effect_meta("白色边框", False, "6974602583411266079", "1164159", "799ac5c78fddad12e395047e180f4328", [])
    百叶窗      = Effect_meta("百叶窗", False, "6823654892872143367", "719380", "bde8d2cb9d033a45c92615f9b18b47a1", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    百叶窗_II   = Effect_meta("百叶窗 II", False, "6823656768334205454", "719404", "380df1dbfbfb93a560b389d5683043e7", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    监控        = Effect_meta("监控", False, "6773542922030682632", "634941", "82748b8ee1cc9a6619aa3571c5e59183", [
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
    """
    盗梦空间    = Effect_meta("盗梦空间", False, "7024053604596060680", "1419276", "ab8caff5408905d424c23bef34af0853", [
                              Effect_param("effects_adjust_size", 0.336, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.667, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.801, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
    """
    盛世美颜    = Effect_meta("盛世美颜", False, "6860757421283873293", "886130", "16d39197cd79d2753ce8c58f409c78a2", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    相机网格    = Effect_meta("相机网格", False, "6725730715138265612", "634051", "7569da277fd0c96d1a8ab45a024baa96", [])
    相纸        = Effect_meta("相纸", False, "6713856991086776835", "635093", "14d50603fdd87a40a787e71172901a56", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.70, 0.00 ~ 1.00
    """
    瞬间模糊    = Effect_meta("瞬间模糊", False, "6903409009210954253", "979300", "811854906cb966498a38302cf5474be2", [
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    破冰        = Effect_meta("破冰", False, "7047049192832766477", "1499079", "35814c493387bfc7af1eadf958e28d71", [
                              Effect_param("effects_adjust_speed", 0.336, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    磨砂纹理    = Effect_meta("磨砂纹理", False, "6732693826135134734", "634027", "4ea2d570ea1d66a407d6973006c199a0", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    祝福环绕    = Effect_meta("祝福环绕", False, "7324617866056045106", "40453164", "f04f5974c31731224645e5d0374e3e04", [
                              Effect_param("effects_adjust_color", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("sticker", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - sticker: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.40, 0.00 ~ 1.00
    """
    秋日暖黄    = Effect_meta("秋日暖黄", False, "7005090271696261640", "1352364", "962a7be1764e7dcdb8ab54198a6bde14", [])
    空灵        = Effect_meta("空灵", False, "7021096050899292680", "1404120", "c0bbb93750bb7fe5b9b2900ff853adb6", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    窗格        = Effect_meta("窗格", False, "6719656757175521800", "634781", "6c832fb174c39c2c7f8af853987e89e4", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    窗格光      = Effect_meta("窗格光", False, "6823659309428118030", "719378", "6bd27e2b68879bb788d7ef0265648795", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    简约边框    = Effect_meta("简约边框", False, "7039329234170417701", "1475188", "a130a890772cc684fc987dcf2ec22124", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    箭头放大镜  = Effect_meta("箭头放大镜", False, "7067461440960991752", "1579942", "e0540ac533119123deb057f99419b6dc", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.00, 0.00 ~ 1.00
    """
    粉红老电视  = Effect_meta("粉红老电视", False, "6839596824936845838", "770876", "10efcbd56eb7d9dd9cea22bb55bf443c", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    粉红芭比边框= Effect_meta("粉红芭比边框", False, "6986591867999621668", "1193772", "3500630cec44ef4028af9ea40b325c99", [])
    粉色闪粉    = Effect_meta("粉色闪粉", False, "6858953149974057486", "881784", "e0294c868dacfeb1f83c406d4e21e121", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    粉黄渐变    = Effect_meta("粉黄渐变", False, "7008413208721494559", "1365502", "36f666ce547c61a8bbe9fc634cb79b69", [])
    粒子模糊    = Effect_meta("粒子模糊", False, "6730841158806671886", "634031", "d411df8e887895dbae6904e8c25d6c51", [
                              Effect_param("effects_adjust_noise", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    精灵闪粉    = Effect_meta("精灵闪粉", False, "6967274435963261476", "1146790", "4a4d26ee6fcb0a71ee15666b8864498f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    精细锐化    = Effect_meta("精细锐化", False, "7250368600911909413", "16609879", "df34b01300ddefbfd8b04bee900ae432", [
                              Effect_param("effects_adjust_blur", 0.120, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.080, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.12, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.08, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    糖果纸      = Effect_meta("糖果纸", False, "6782100631638249998", "634217", "37ae35224ded86cd0e5d5bc2d58e3cc8", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    紫色波纹    = Effect_meta("紫色波纹", False, "6987321998036701704", "1195758", "4e80d6d461e093799fa7ce721d7dbd89", [])
    紫色负片    = Effect_meta("紫色负片", False, "6915313694884762125", "1007834", "a21c94f366e16f2aa8bd9e491ec226c5", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    紫雾        = Effect_meta("紫雾", False, "6886335679681270279", "948716", "bf106ce53d50ff0a7ebabe323a69b097", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    繁星点点    = Effect_meta("繁星点点", False, "6839577027939406344", "768166", "5342526311c51bc957c5abc25b2f5280", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    纵向开幕    = Effect_meta("纵向开幕", False, "6876338988437737997", "931824", "d75e138469226782f6d918983725d700", [])
    纵向模糊    = Effect_meta("纵向模糊", False, "6716684911840858628", "634137", "39d1ffded922746f7e09b925798a2f1a", [
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    纸膜边框_I  = Effect_meta("纸膜边框 I", False, "6981464043542286879", "1181888", "d76f129d3e1a3c4a0350a6537c382c13", [])
    纸膜边框_II = Effect_meta("纸膜边框 II", False, "6981464169736311327", "1181886", "b95690afb9846aeacdfccd0cb05cef27", [])
    纸质撕边    = Effect_meta("纸质撕边", False, "6843686214025875981", "784032", "fd5588f68a681b8eba1449a5d0240097", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    纸质边框    = Effect_meta("纸质边框", False, "6844765419853582856", "780656", "554d4d330b4d17f0b404e598a66f05c9", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    纸质边框_II = Effect_meta("纸质边框 II", False, "6844832937272152589", "780658", "b3fbce0bfe68298555ab18ed39fc817a", [])
    细闪        = Effect_meta("细闪", False, "6847773569435308558", "785536", "9f35060cd9e36abab8c5ebb80d8efbf6", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    细闪_II     = Effect_meta("细闪 II", False, "6893002658420888078", "959412", "186c623a413a10ddbf28bfa0215a55f4", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    细闪_III    = Effect_meta("细闪 III", False, "6963598424113418783", "1134290", "432b12f72fe1b0f081dc292bc415dbb0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    美式        = Effect_meta("美式", False, "6849214832856535560", "787752", "d3c405c7369854dd009dd63f6a4b2b46", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    美式_II     = Effect_meta("美式 II", False, "6843320153900323335", "774972", "cd7423d39d5a115fc4d5d7f5db43658c", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    美式_III    = Effect_meta("美式 III", False, "6843319785522991623", "774968", "d936f602060a9b010a261e85166b5a14", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    美式_IV     = Effect_meta("美式 IV", False, "6850006476472193543", "812078", "0bddd63da76f2f117140ff240c57daee", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.620, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.62, 0.00 ~ 1.00
    """
    美式_V      = Effect_meta("美式 V", False, "6849225862588404237", "787968", "26f287cc23166dc878589197c5800842", [
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    美漫        = Effect_meta("美漫", False, "6981339244547543560", "1181360", "d17c9fedb83124be5b0f758d90eea0be", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    羽毛        = Effect_meta("羽毛", False, "6709706658815152643", "634295", "135a9b19d3a4d08dfdd5bb1c9eabbfec", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    老照片      = Effect_meta("老照片", False, "6815764475375784462", "703231", "140119b43a843a5732e5b4064a58576e", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    老照片_II   = Effect_meta("老照片 II", False, "6815767788490068494", "703233", "25921facf51181e20ad0947556517792", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    老照片_III  = Effect_meta("老照片 III", False, "6813924503148564999", "719374", "e199463a70a8b3840f248dbc9fac6769", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    老电影      = Effect_meta("老电影", False, "6706773498506777095", "635095", "3ffab78abca09b413e5b7178511f903d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    老电影_II   = Effect_meta("老电影 II", False, "6865921078858879496", "898674", "62b508cb16fd1c0da7a2989da5bd49fd", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    老电视卡顿  = Effect_meta("老电视卡顿", False, "6706773499052036615", "634771", "da767092b3d91fa36fae380e90f11cdd", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    聚光灯      = Effect_meta("聚光灯", False, "6750075966053159427", "634081", "49c61bf16894adb9926b79d18993c3bd", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    聚焦        = Effect_meta("聚焦", False, "6710056993287049742", "635083", "97b20e018b0bdd4ff12025b5358a6e81", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    胡言乱语    = Effect_meta("胡言乱语", False, "6951364520048595492", "1102990", "2b069d3c512bb55aa56b9837d6244eee", [])
    胶片        = Effect_meta("胶片", False, "6708624565657932292", "635097", "c85a5c6d8841e2e6dd65813cbe60505c", [
                              Effect_param("effects_adjust_noise", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    胶片_II     = Effect_meta("胶片 II", False, "6710090540643258891", "635087", "9c4e00c766b4fd4f603bed3a720397b9", [
                              Effect_param("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_chromatic: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.55, 0.00 ~ 1.00
    """
    胶片_III    = Effect_meta("胶片 III", False, "6841053178406900231", "773562", "2413a56c73f8432072f1cf4429648193", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    胶片_IV     = Effect_meta("胶片 IV", False, "6896439221179912718", "966552", "9f76eb0fd12192188a8ace928de37416", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    胶片抖动    = Effect_meta("胶片抖动", False, "7075213848558440990", "1625760", "86c6710992682fa9d51b9bfea52d2b47", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
    """
    胶片显影    = Effect_meta("胶片显影", False, "6830336944111620616", "744244", "a09195689037df58fd23db7f28d3a2b6", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_soft: 默认1.00, 0.00 ~ 1.00
    """
    胶片框      = Effect_meta("胶片框", False, "6974600629268255262", "1164161", "393b58c3e98a33f92ea16ac611919909", [])
    胶片框_II   = Effect_meta("胶片框 II", False, "6974600475999998477", "1164162", "fd84488800ef5683555188564886ab76", [])
    胶片框_III  = Effect_meta("胶片框 III", False, "6987714956401578510", "1196596", "d0169ca7d23e5196df0e4604bcfbe2c1", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    胶片漏光    = Effect_meta("胶片漏光", False, "6815093106841489934", "705083", "179080155bccbfd7ddf7e37137eb2747", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    胶片漏光_II = Effect_meta("胶片漏光 II", False, "6814743838964322829", "718872", "0a0b12f5a4e442871708fcbf14fdec5d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    胶片连拍    = Effect_meta("胶片连拍", False, "6994787976613990925", "1218011", "cb017def5c29fc1af5de0041469d4ff4", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    自然        = Effect_meta("自然", False, "6843319885339038216", "774970", "b692892ba55b4cbd18c97704102b9938", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    自然_II     = Effect_meta("自然 II", False, "6841460795394494990", "773090", "7196a6d5e3b895f781a453e70abb971a", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    自然_III    = Effect_meta("自然 III", False, "6843680748856152584", "775998", "6d80537f452debf98b09f2df79080e37", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    自然_IV     = Effect_meta("自然 IV", False, "6843680812584407559", "776000", "29800968f49ad39520d47e999024becb", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    自然_V      = Effect_meta("自然 V", False, "6843319715499086343", "774966", "6ff4d109673eb689778b2be2f5af1c3e", [
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    色差        = Effect_meta("色差", False, "6706773498561303044", "634059", "737c54ea0dcf628cc78714a77eef52a3", [
                              Effect_param("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    色差开幕    = Effect_meta("色差开幕", False, "6868546720783929870", "904723", "fc98a601f63bacc514067ecfa2849137", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
    """
    色差放大    = Effect_meta("色差放大", False, "6883360769992299016", "945036", "894bef97217ae4bab59ae710228bdf40", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
    """
    色差放射    = Effect_meta("色差放射", False, "6716422405511713287", "634777", "85706adda9a242bbb6dc2c3da2542ba1", [
                              Effect_param("effects_adjust_blur", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.55, 0.00 ~ 1.00
    """
    色差故障    = Effect_meta("色差故障", False, "6706773498922013191", "634773", "6ee1a1ab0be0849602a3c983a025c47a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    色差故障_II = Effect_meta("色差故障 II", False, "6706773498561319428", "634769", "638565d68ac2845eb2c552497efec3d8", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    色差星闪    = Effect_meta("色差星闪", False, "6904921853635072520", "982304", "c13d9ca825a2adb976c429456af2ead0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    色差默片    = Effect_meta("色差默片", False, "6719362972239532548", "634793", "82cc4ec1b530fc13e1af9be9e4b63c4f", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
    """
    节日彩带    = Effect_meta("节日彩带", False, "6907438556793278983", "987446", "47ca5466c833a9287af563c9890f8159", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    花火        = Effect_meta("花火", False, "6767147410671014407", "634223", "4e7b79927a6067a2080ce6b61da8faf9", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    花火_II     = Effect_meta("花火 II", False, "6907051960180937229", "986478", "8a3f34e4c9650409a8aa6059f8610e14", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    花瓣飘落    = Effect_meta("花瓣飘落", False, "6796905369932141064", "635059", "a772c059e7fb8304292e7ebb870e8eb3", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    花瓣飞扬    = Effect_meta("花瓣飞扬", False, "6796903619762328072", "635057", "24c3c52fe9d54c8677ee514c0530528c", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    荡漾_II     = Effect_meta("荡漾 II", False, "7140929198763282980", "4493526", "7a08a3c5aa067e55cd0f638cd3161a1b", [
                              Effect_param("effects_adjust_range", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.350, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.35, 0.00 ~ 1.00
    """
    荡秋千      = Effect_meta("荡秋千", False, "7388040405465436722", "73935190", "bee293df8d3c2a62e722c60eca82aab3", [])
    荧光扫描    = Effect_meta("荧光扫描", False, "7041474808986472967", "1482382", "4c6263913593bbf1fc06f01e8c3fcf8b", [
                              Effect_param("effects_adjust_color", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    荧光爱心    = Effect_meta("荧光爱心", False, "6792095053360665096", "634227", "b9b9be20aed7761f81c6757a4428a034", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    荧光线描    = Effect_meta("荧光线描", False, "6795826477590909454", "634945", "d393537113a37c7cff64101d0e042a87", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    荧光绿      = Effect_meta("荧光绿", False, "6858138988834722312", "875968", "7cbaffedca388899dec7c7219592074c", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    荧光蝙蝠    = Effect_meta("荧光蝙蝠", False, "6886339116561076749", "948715", "ad61d53ca404616d198bc766e6c64df8", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    荧幕噪点    = Effect_meta("荧幕噪点", False, "6706773534066086413", "634779", "f090492c306fe35f917eed1216f14f8c", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    荧幕噪点_II = Effect_meta("荧幕噪点 II", False, "6803161742789579277", "703253", "53ff3188476c74715a73aa34f08a1edf", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    萤光        = Effect_meta("萤光", False, "6715209844216828420", "634107", "59a3ea0709d076e3043555a7d5d40945", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    萤光飞舞    = Effect_meta("萤光飞舞", False, "6877098783209951751", "932242", "d34177a4c2caf9581e67b0206cf6a919", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    萤火        = Effect_meta("萤火", False, "7006265184050221576", "1357502", "d473ca7fa127312a7651ec1523a6e880", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    落叶        = Effect_meta("落叶", False, "6740863535674298888", "635043", "5e8db93a52a15e7254dc7e1c115c145c", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    落樱        = Effect_meta("落樱", False, "6924859706661933576", "1031296", "7372d9708980266944aec9650ccde843", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蒸汽波      = Effect_meta("蒸汽波", False, "6719658860539286020", "634147", "08d620dca82aea6bf5d71d48ba4a6b3d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    蒸汽波投影  = Effect_meta("蒸汽波投影", False, "6830351103272423949", "747926", "83c74d3a0dd8f6d11d3cc3063f1eadfa", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蒸汽波路灯  = Effect_meta("蒸汽波路灯", False, "6829184472349413895", "755808", "564a4710d8ece86ade31f9eee89deb01", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蒸汽腾腾    = Effect_meta("蒸汽腾腾", False, "6894200076227318286", "961482", "f852e42917f0ea29be56bbb12891c920", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蓝光扫描    = Effect_meta("蓝光扫描", False, "7254126209540297274", "17710554", "5f9918f9606b3dfbb8e8c8b7b90ca0e3", [
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
    """
    蓝线模糊    = Effect_meta("蓝线模糊", False, "6920136330563293704", "1019968", "770dd5360aa3cfc96d97738f62627957", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    蓝色负片    = Effect_meta("蓝色负片", False, "6914996050382033421", "1005838", "c40c9ca0a5c2ea1a22c54a3dc943b3de", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    蓝色闪电边框= Effect_meta("蓝色闪电边框", False, "6989911842575356446", "1201878", "f69acdd1cea097f4db0bf01ed015559b", [])
    虚化        = Effect_meta("虚化", False, "6756397840785740295", "634065", "5b22f93757ce6807874cc5e1530db8b3", [
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    蝙蝠Kira    = Effect_meta("蝙蝠Kira", False, "6888977985697747463", "953420", "408ee7831b71cbae827138898d26c934", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
    """
    蝴蝶        = Effect_meta("蝴蝶", False, "6706773499836404228", "634157", "559a055318e1a9940281c8eb31954ee9", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蝴蝶_II     = Effect_meta("蝴蝶 II", False, "6747586717672280584", "634155", "014a7aa25087ad6a6bfa14ca6146bedd", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蝴蝶光斑    = Effect_meta("蝴蝶光斑", False, "6748307256959308299", "634183", "45377639fc1c0b29cc889f71f6ca2fd0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蝶舞        = Effect_meta("蝶舞", False, "6747946665312784910", "634177", "b6c530af2bd744d77df4d5b70e3497f8", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    表面模糊    = Effect_meta("表面模糊", False, "7244073793562350140", "15249743", "8629e4a00fdb51b73c98842bc7a6f0c5", [
                              Effect_param("effects_adjust_blur", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.70, 0.00 ~ 1.00
    """
    裂开了      = Effect_meta("裂开了", False, "6944914067702157861", "1082654", "48084a37dbea8252814a0d96520dcaee", [])
    视频分割    = Effect_meta("视频分割", False, "6729023693739004419", "634747", "a9338d60042f719860346409954ed387", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
    """
    视频界面    = Effect_meta("视频界面", False, "6752799091941446147", "635135", "ecbdf02c28278b4436c1dfaf3b733650", [])
    诡异分割    = Effect_meta("诡异分割", False, "7021800634621891109", "1408118", "2755d9f7c9b46356a832ef58ef405df7", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.630, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.63, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.70, 0.00 ~ 1.00
    """
    负片闪烁    = Effect_meta("负片闪烁", False, "6863353894152442375", "892686", "ed476f61f551e99709b62ce8ed922323", [
                              Effect_param("effects_adjust_speed", 0.560, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.56, 0.00 ~ 1.00
    """
    赞赞赞      = Effect_meta("赞赞赞", False, "7057055647472292359", "1543072", "a927f8d9d6b8fcefd4671cb53455d8d5", [])
    蹦迪光      = Effect_meta("蹦迪光", False, "6716419849544798723", "634733", "5b3449fa5476bfd93851d0b4cce7b8c9", [
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    蹦迪彩光    = Effect_meta("蹦迪彩光", False, "6716450942285255182", "634731", "355d46c4bff8c9b6286f3324fb6e27b7", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    车窗        = Effect_meta("车窗", False, "7012926200767058463", "1381596", "e16d42dbe728d95e6cdc2585a817a3e2", [])
    车窗影      = Effect_meta("车窗影", False, "6834006887415943694", "761222", "d37540d91f173eaeef40a3ac6a2de42e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    轻微抖动    = Effect_meta("轻微抖动", False, "7258208250896585274", "18798726", "b5235343ec32572db40123246a22fefa", [
                              Effect_param("effects_adjust_range", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    轻微放大    = Effect_meta("轻微放大", False, "6791743223522923021", "634077", "c09004507723569a3e762494d4ffda7d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    边缘glitch  = Effect_meta("边缘glitch", False, "6777238992816443912", "634749", "516eb9ef0e22a58d17984712a9301b23", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    边缘加色    = Effect_meta("边缘加色", False, "6781315516909752844", "634757", "1d5ac14cba4e6e8559cacd2c37d62c43", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    边缘加色_II = Effect_meta("边缘加色 II", False, "6790180635555140109", "634755", "ff84c6f908752eda1298021c2e382e0f", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    边缘加色_III= Effect_meta("边缘加色 III", False, "6901190770473046535", "974844", "91c834c21a94810977500c0f0f0d406b", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    边缘发光    = Effect_meta("边缘发光", False, "6769065553207235086", "634069", "656e16d4aff7d609ff25c2ff8abc156c", [
                              Effect_param("effects_adjust_luminance", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.25, 0.00 ~ 1.00
    """
    边缘荧光    = Effect_meta("边缘荧光", False, "6903064458008990215", "977454", "270610eeb2c6810b2cd43743033bebee", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    运动一夏    = Effect_meta("运动一夏", False, "6984393713208267301", "1188619", "c78c14c0ce8641f5de8ba5a03f8dce29", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    迪斯科      = Effect_meta("迪斯科", False, "6756113382840996360", "634739", "975bfbd37de349a6c2390576a61d243e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    迷幻烟雾    = Effect_meta("迷幻烟雾", False, "6719661667447214605", "634089", "d03e2cc41acde9dd8e3eab333c43ba2c", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    迷离        = Effect_meta("迷离", False, "6706773549362713095", "634721", "7c2f3180ded615ee30e6d1a5bafc5392", [
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    迷雾        = Effect_meta("迷雾", False, "6887505634791526926", "950488", "057c2404619359f8ceec96e20eee0f2f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    逆光对焦    = Effect_meta("逆光对焦", False, "6992032047959118344", "1218244", "ccba5bb5c3656e951ce7e6ec272dc606", [
                              Effect_param("effects_adjust_soft", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_soft: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.33, 0.00 ~ 1.00
    """
    选中框      = Effect_meta("选中框", False, "6712358020417851917", "635081", "f65a653528911a459a3011c647b68cf4", [])
    邮票边框    = Effect_meta("邮票边框", False, "7012988323387937293", "1382084", "f14c0b2288f110621f814c237c5471a6", [
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
    """
    金属背景    = Effect_meta("金属背景", False, "7044853948456374814", "1493772", "44ec1abb4102d0886e6cb4e60a80ae72", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.505, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.710, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.51, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.71, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    金片        = Effect_meta("金片", False, "6771299796058640908", "634229", "5ff7544cd83c2ec196b1acc8f47bf51c", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金片_II     = Effect_meta("金片 II", False, "6924589854269379079", "1030626", "3100003d53722ae2d1e8ca0bde4a1043", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金片炸开    = Effect_meta("金片炸开", False, "6899747182816006669", "972750", "075cfd56ba9a170c62a6ad8150d4845d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉        = Effect_meta("金粉", False, "6709706378702754312", "631215", "0443a82ca7b709b643abaf8da7051cca", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉_II     = Effect_meta("金粉 II", False, "6774672940651778573", "634289", "75dc8419d6ebcca570bb85b0daeb883f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉_III    = Effect_meta("金粉 III", False, "6984393847467938335", "1188618", "752d69c565983fbed6bb13c3d8542ca7", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉撒落    = Effect_meta("金粉撒落", False, "6907439016547717646", "987445", "c84cfe1f31a1a79e5a9b362bc744d3d3", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉旋转    = Effect_meta("金粉旋转", False, "7033654301050278431", "1452336", "14fd0f24372acd5be33505ee5759ca11", [
                              Effect_param("effects_adjust_speed", 0.336, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉聚拢    = Effect_meta("金粉聚拢", False, "6806254339821146637", "703245", "a4d9c4c3bde58e6aa6db39fcef692108", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    金粉闪闪    = Effect_meta("金粉闪闪", False, "7034048554318434830", "1453820", "a552dfa820b5aba27e4f09e3d83b8643", [
                              Effect_param("effects_adjust_speed", 0.336, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    钻光        = Effect_meta("钻光", False, "6723824479216079368", "634097", "c9c730b13ac00e7b8b16af1d882fe31c", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    钻石碎片    = Effect_meta("钻石碎片", False, "7077487066476450340", "1639618", "7c201b5477a02796bddb330377b7fce7", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
    """
    镜像        = Effect_meta("镜像", False, "6956148985400660517", "1115964", "0e68989382af0ece7e1e864cc2107c67", [])
    镜头变焦    = Effect_meta("镜头变焦", False, "6868546663607177736", "904724", "59273e718263fae7a1001c65fe44ad3a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.30, 0.00 ~ 1.00
    """
    长虹玻璃    = Effect_meta("长虹玻璃", False, "6992081595976913416", "1235644", "2f5917be32e664eef67419212e54cad0", [
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    闪亮登场    = Effect_meta("闪亮登场", False, "6760547949349966350", "634185", "a1c096efd5f98b438ab0f762bea9c41a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    闪亮登场_II = Effect_meta("闪亮登场 II", False, "6891946116212855303", "958186", "0a249f3cd35bef5ca846a49680248812", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    闪光灯_Ⅰ   = Effect_meta("闪光灯 Ⅰ", False, "6844432942563856904", "777760", "c602afac7537de506bb822c37e9f2191", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    闪光震动    = Effect_meta("闪光震动", False, "7260437169389441597", "19279654", "17416edf590446330a683c9eb4f5c9e3", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.580, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.58, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    闪动        = Effect_meta("闪动", False, "6717639344577843725", "634725", "0bc9ee34335ba4f9d75e4a2b21f4d6e5", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    闪动光斑    = Effect_meta("闪动光斑", False, "6753169731617821191", "634181", "d7c42c303074967c0cad7c7a6adfe896", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    闪屏        = Effect_meta("闪屏", False, "6758298031608566280", "634729", "51b2af1e78502e00abb3d47b21a55796", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    闪电        = Effect_meta("闪电", False, "6734215409513271820", "635069", "6191fcf13bfd15e4288a81a174ba0ed8", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    闪白        = Effect_meta("闪白", False, "6706773500792672781", "634761", "f0804cb2cb4e88a036ecf87dcf031cf0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    闪耀星光    = Effect_meta("闪耀星光", False, "6784346950385799694", "634219", "93c0a1e7829ec10d8502466ea74846dd", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    闪闪        = Effect_meta("闪闪", False, "6869625970437919246", "909546", "293daf09b25bb116a038576ff690e698", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    闪闪发光_II = Effect_meta("闪闪发光 II", False, "7013264306959553060", "1382870", "9a723996777d5f56d3802b53c8cc46bb", [
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
    """
    闪黑        = Effect_meta("闪黑", False, "6863327462470717960", "892171", "383b8ace93434f0c5d17689933140422", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    闪黑II      = Effect_meta("闪黑II", False, "7221377929467400765", "12078089", "3c25ccac35121fe42e647b119e37a21f", [
                              Effect_param("effects_adjust_speed", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.40, 0.00 ~ 1.00
    """
    闭幕        = Effect_meta("闭幕", False, "6725685146323784205", "634035", "6a59cb9db4036a187d4b1ca3a2cab8f3", [])
    闭幕_II     = Effect_meta("闭幕 II", False, "6729065630013592067", "634033", "47ad4fe486fe97a4529998d53e5e93b3", [])
    随机色块    = Effect_meta("随机色块", False, "7026674824537707038", "1427664", "a7e3cf890d40734c1b44172eff546c41", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
    """
    随机色块_II = Effect_meta("随机色块 II", False, "7030742849134006792", "1441868", "0d5b2c847554024c4bd5dbaf06d842fb", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
    """
    随机裁剪    = Effect_meta("随机裁剪", False, "6991794787464516127", "1206444", "348f8137cc25a994e2a676a5639d3bd9", [
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    隐形人      = Effect_meta("隐形人", False, "7020318315310486046", "1400804", "2cf16035b605ce73f4b44bcd650adfb3", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.350, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
    """
    隔行扫描    = Effect_meta("隔行扫描", False, "6976152376457564708", "1168118", "e8349feb07866b44bbce9c9effa6f51a", [
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    雨滴晕开    = Effect_meta("雨滴晕开", False, "6792488562869670414", "635041", "2bded973503eaa2ce5644ef44354d90d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    雪窗        = Effect_meta("雪窗", False, "7168743948528128548", "6431703", "823ecc00612b35e63837f9ce6f4f4af5", [
                              Effect_param("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    雪花        = Effect_meta("雪花", False, "7030728702258319909", "1441796", "aa711f9666bdc3e51ff72de0d7c073a8", [
                              Effect_param("effects_adjust_speed", 0.336, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    雪花冲屏    = Effect_meta("雪花冲屏", False, "6769435378806952455", "634203", "2c07239e54041e85518b111b1ad8eb86", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    雪花开幕    = Effect_meta("雪花开幕", False, "6730429759425090059", "634045", "8c3a0db33fda83398b66a5a8ab64cc41", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    雪花故障    = Effect_meta("雪花故障", False, "6847689727261282824", "785064", "f24f4cebfa22bc28d74c9b30aa17f1a0", [
                              Effect_param("effects_adjust_range", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.55, 0.00 ~ 1.00
    """
    雪花细闪    = Effect_meta("雪花细闪", False, "6770604155561054734", "634201", "3eab18374e64043e209c3deac2bbe56d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    零点解锁    = Effect_meta("零点解锁", False, "6907054642123772430", "986480", "f189f93d81e1638035e229389355cc4e", [
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    雾气        = Effect_meta("雾气", False, "6734619830449607171", "635049", "add061ec46e4f013ed3482a6dc87c9b9", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    雾气_II     = Effect_meta("雾气 II", False, "6740539818666627588", "635045", "6e963a8a2e1fd100e7ac3d2f21100a8a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    雾气光线    = Effect_meta("雾气光线", False, "6715209712129806851", "635065", "607f77fe518da5a26e7457ea932f5ad7", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    震动        = Effect_meta("震动", False, "6761645818723176968", "634075", "d11532bfbfbd6f9af59026c2c42f2570", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    霓虹投影    = Effect_meta("霓虹投影", False, "7058961173743407630", "1552220", "46a3a7dbb114d888726b1cf9a22189c2", [
                              Effect_param("effects_adjust_soft", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_soft: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
    """
    霓虹摇摆    = Effect_meta("霓虹摇摆", False, "6925387220073320974", "1034626", "f7ce2e949d495d22dab8f6a2b032a9b9", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
    """
    霓虹灯      = Effect_meta("霓虹灯", False, "6829182808485794311", "742028", "35a6f9b3c544b0f97ccbf3fea89e6010", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    预警        = Effect_meta("预警", False, "6955083255825568264", "1113432", "3dfcefd286a1684818c543e17b7d5bc6", [])
    颤抖        = Effect_meta("颤抖", False, "6863326875649839623", "892172", "7cb6c1646c43d86a394245e194e3f451", [
                              Effect_param("effects_adjust_range", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    飘落花瓣    = Effect_meta("飘落花瓣", False, "6719658795661791747", "634153", "c39b069df62f67308de64f86b920dbbd", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    飘落闪粉    = Effect_meta("飘落闪粉", False, "6720029963602366979", "634165", "517bbcd8e398072ce95c0d9763c4c914", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    飘落闪粉_II = Effect_meta("飘落闪粉 II", False, "6720029866504229390", "634163", "6bd90b0f33d3722d759b0fc2d5ddc9bd", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    飘雪        = Effect_meta("飘雪", False, "6732360625214722572", "635061", "8e2909d8fe6a77833f62fccf73630aa7", [])
    飘雪_II     = Effect_meta("飘雪 II", False, "6763531573594690061", "635055", "e4c07894c4f11edbbc580486b50f4b8e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    飞速计算    = Effect_meta("飞速计算", False, "6951364383477862948", "1102992", "b08f9e05c86b2e980444d336d9db7427", [])
    马赛克      = Effect_meta("马赛克", False, "6770564289074827784", "639477", "c9f3bf5b93d53bdc514be0d9c480fcf0", [
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    高光瞬间    = Effect_meta("高光瞬间", False, "6955021144156017188", "1113136", "7e50ea3473876ee7bbc0f9105cc6c65e", [])
    魅力光束    = Effect_meta("魅力光束", False, "6814668066882851335", "705071", "8c305048985cc4cd8236d08b716c2d16", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    魔法        = Effect_meta("魔法", False, "7000199435372204580", "1232490", "98296a4bc028cef2bb3b06ffbb490faf", [
                              Effect_param("effects_adjust_speed", 0.336, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.802, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    魔法变身    = Effect_meta("魔法变身", False, "6964608751231832613", "1136674", "4ec729c610f93a85cd08b9a9474aaecf", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    魔法边框    = Effect_meta("魔法边框", False, "7020407234798555655", "1401520", "f995faa8d65405b92637e54d90d4d9a9", [])
    魔法边框_II = Effect_meta("魔法边框 II", False, "7021795690149843463", "1408090", "6f23fdea097c9e547d934e0c134cd0c9", [])
    鱼眼        = Effect_meta("鱼眼", False, "6867722963865571854", "901430", "d577e4744d29d971675ec9c71d94ca94", [
                              Effect_param("effects_adjust_distortion", 0.770, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.77, 0.00 ~ 1.00
    """
    黄蓝星芒    = Effect_meta("黄蓝星芒", False, "7000312634574639653", "1232996", "290f59cb09438e3b8681f055a9b4a967", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    黑白VHS     = Effect_meta("黑白VHS", False, "7021795095900852772", "1408072", "1a53630780dee01e236cff7233d35d01", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.530, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.430, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.53, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.43, 0.00 ~ 1.00
    """
    黑白三格    = Effect_meta("黑白三格", False, "6719657002571665934", "635017", "e4022fb9e226f41f58c33d255c647eed", [])
    黑白漫画    = Effect_meta("黑白漫画", False, "6795826673993388551", "634953", "f5e6a157bc591221429ad4d0af4764b3", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    黑白漫画_II = Effect_meta("黑白漫画 II", False, "6904876576735760904", "981864", "93e7188b36f51f6aa660cf2cf44569b7", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    黑白线描    = Effect_meta("黑白线描", False, "6795430643154031111", "634951", "68c0d3c64a515b7cdc99b2cf0b6914fe", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    黑线故障    = Effect_meta("黑线故障", False, "6970572741116170788", "1155300", "fc0dca637063d415f92ab45869d9f8d5", [])
    黑羽毛      = Effect_meta("黑羽毛", False, "6716441529084285454", "634151", "9be9c2290cd7574af6d47f1779e4519a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    黑羽毛_II   = Effect_meta("黑羽毛 II", False, "6751257389422350860", "634149", "8e20f4ef27e5d50c3839eabcde5c292d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    黑胶边框    = Effect_meta("黑胶边框", False, "6865958778265670151", "898866", "30c353317f11b9a5dcdf5b64708955ad", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    黑色噪点    = Effect_meta("黑色噪点", False, "6888561214125773326", "952514", "e7baebcf969437d4d5cdb607578bbf89", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    黑色老电视  = Effect_meta("黑色老电视", False, "6738276072246219277", "635123", "87b8b83900d283b06e02ead6f09111e5", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Bling飘落   = Effect_meta("Bling飘落", True, "7306819369571455515", "31620429", "5425c855f5395166464034278b51afc2", [
                              Effect_param("effects_adjust_speed", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.450, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.45, 0.00 ~ 1.00
    """
    C300        = Effect_meta("C300", True, "7226241938649780793", "12744891", "3bc3db89a7d77cbeb49d42a9566b575f", [
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.55, 0.00 ~ 1.00
    """
    IXUS        = Effect_meta("IXUS", True, "7213660933942415930", "11068675", "bd4fb5e91257e0bcf302f23a093f57cc", [
                              Effect_param("effects_adjust_intensity", 0.440, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("sticker", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.44, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.15, 0.00 ~ 1.00
    """
    Ins描边     = Effect_meta("Ins描边", True, "7265936765175730744", "20434943", "402b239494189ae949538500b9fd6e50", [
                              Effect_param("effects_adjust_color", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.460, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.300, 0.000, 1.000)])
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
    S形运镜     = Effect_meta("S形运镜", True, "7291263159023702584", "26271784", "1a137ba40b56a10809190892c3850f95", [
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    W830        = Effect_meta("W830", True, "7226197862529372731", "12732403", "70556dee7b46e17512e9525613951aca", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.80, 0.00 ~ 1.00
    """
    一刀两断    = Effect_meta("一刀两断", True, "7290460914174661177", "26002592", "6e66b782a69fa0c2712deeaf50d4aadf", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
    """
    丁达尔旋焦  = Effect_meta("丁达尔旋焦", True, "7361697260960223759", "59474165", "815fe4564516ccb104dd6a12682e6ac2", [
                              Effect_param("effects_adjust_texture", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
    """
    丝印涂鸦    = Effect_meta("丝印涂鸦", True, "7270068054040515131", "21210786", "0e342cccb5b95dafc6e99f0f51603b04", [
                              Effect_param("effects_adjust_color", 0.200, 0.050, 1.000),
                              Effect_param("effects_adjust_intensity", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.570, 0.000, 0.810),
                              Effect_param("effects_adjust_speed", 0.430, 0.000, 0.700),
                              Effect_param("effects_adjust_texture", 0.120, 0.000, 0.500)])
    """参数:
        - effects_adjust_color: 默认0.20, 0.05 ~ 1.00
        - effects_adjust_intensity: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.57, 0.00 ~ 0.81
        - effects_adjust_speed: 默认0.43, 0.00 ~ 0.70
        - effects_adjust_texture: 默认0.12, 0.00 ~ 0.50
    """
    丝滑运镜    = Effect_meta("丝滑运镜", True, "7382145257607008809", "71888371", "9333197e30c47f6aab8eb7b6bba7bd38", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.667, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    两屏分割    = Effect_meta("两屏分割", True, "7069602912057430558", "1594946", "2eba26aa15c0e44d2c258ce63a38d243", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.10, 0.00 ~ 1.00
    """
    中轴旋转    = Effect_meta("中轴旋转", True, "7224407224460775994", "12495253", "16c94e8b38c2d306c11b0d4cfb63dec9", [
                              Effect_param("effects_adjust_speed", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    云朵绵绵    = Effect_meta("云朵绵绵", True, "7287143540033851964", "24962948", "66f0d5b98e5c703d596c6d5053b36a73", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("sticker", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    五星好评    = Effect_meta("五星好评", True, "7176947440350663223", "7318779", "68b302b2bea8da7aea6db5fef3da518e", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    交叉震闪    = Effect_meta("交叉震闪", True, "7291135461697786423", "26216294", "c008c7e122d99b87378292db514ed6cb", [
                              Effect_param("effects_adjust_color", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
    """
    低保真      = Effect_meta("低保真", True, "7300933146923504178", "29478846", "afb3e21fb90b170bc431dd088513b2ed", [
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.20, 0.00 ~ 1.00
    """
    侧移模糊    = Effect_meta("侧移模糊", True, "7291553469180154423", "26353150", "2fb8c434b5867861aca8abfd58c72920", [
                              Effect_param("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    倒带        = Effect_meta("倒带", True, "7358381380687893027", "57670397", "7eb38d3b30ae8e18748fcd3ed726aab2", [
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
    """
    倒计时      = Effect_meta("倒计时", True, "7042501782014005773", "1485906", "06c20494725c2b5873c5aac7fcea3205", [])
    假日闪闪_Ⅱ = Effect_meta("假日闪闪 Ⅱ", True, "7173558602580365838", "6940703", "ee3bcd824b78992d1a9ee05289f724bb", [
                              Effect_param("effects_adjust_size", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.650, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.65, 0.00 ~ 1.00
    """
    像素屏闪    = Effect_meta("像素屏闪", True, "7242581780866273850", "14975389", "a0b46f005c19589d83743e33b8f7f05c", [
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    像素扫描    = Effect_meta("像素扫描", True, "7345080472545792521", "50297398", "a37ca96c39e545f397ec3ff4c6c9a5b1", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    像素拉伸_II = Effect_meta("像素拉伸 II", True, "7355396055397044790", "56071748", "867a13e17bbab1fff0bc2344a41c4559", [
                              Effect_param("effects_adjust_rotate", 0.600, 0.200, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_rotate: 默认0.60, 0.20 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    像素排序    = Effect_meta("像素排序", True, "7223659432419267132", "12385973", "24e9de1fa2c77ec26045f7113fdc79f9", [
                              Effect_param("effects_adjust_number", 0.940, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.94, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.00, 0.00 ~ 1.00
    """
    像素故障    = Effect_meta("像素故障", True, "7239557281942082107", "14523597", "964299673ae36eb232abec3452f50624", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    像素爱心    = Effect_meta("像素爱心", True, "7058961362550002212", "1552218", "cbf62902df7101761116f28616cbbabc", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    像素震闪    = Effect_meta("像素震闪", True, "7349147660290363944", "52648474", "5eed2819a04cfccafd198a00309ad2a0", [
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    光线扫描    = Effect_meta("光线扫描", True, "7047492648587760142", "1500914", "815e6f766c2f5ba2e6b6eea27844b2d1", [
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.380, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.38, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.15, 0.00 ~ 1.00
    """
    光线拖影    = Effect_meta("光线拖影", True, "7254547939194835515", "17852396", "1cee833d647541e86d24bb2f7b7635ea", [
                              Effect_param("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.340, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.34, 0.00 ~ 1.00
    """
    光谱扫描    = Effect_meta("光谱扫描", True, "7257452387160298021", "18636946", "871e765d3b6486d36166bfb55dfc4b54", [
                              Effect_param("effects_adjust_background_animation", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.614, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.642, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.61, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.64, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.33, 0.00 ~ 1.00
    """
    兔兔碎闪    = Effect_meta("兔兔碎闪", True, "7184326422612152887", "8343041", "375943efb400de1f186e9701e1f4b8e6", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    全息扫描    = Effect_meta("全息扫描", True, "7246746366108504636", "15772481", "7de6cab0dbc13aaaa9ccc25e1259c3da", [
                              Effect_param("effects_adjust_luminance", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.260, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.570, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.26, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.57, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.60, 0.00 ~ 1.00
    """
    分屏漏光    = Effect_meta("分屏漏光", True, "7276332732051886649", "22335555", "b19b89d0f4daf5988d2f390e5364077e", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("sticker", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - sticker: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    动态侦测    = Effect_meta("动态侦测", True, "7348407437877056009", "52247519", "930511ab136c4558e75177f724587990", [
                              Effect_param("effects_adjust_speed", 55.000, 0.000, 100.000),
                              Effect_param("effects_adjust_number", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.980, 0.000, 1.000),
                              Effect_param("sticker", 0.240, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.100, 0.000, 1.000)])
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
    动态格      = Effect_meta("动态格", True, "7065593660921877028", "1570398", "eb35001e4b8d3d9e2c7b797578d1e97c", [
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    动感光束    = Effect_meta("动感光束", True, "7162091309375689223", "5779099", "89af4a6484b09943dd5ce0313b6f3300", [
                              Effect_param("effects_adjust_intensity", 0.581, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.398, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.58, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.40, 0.00 ~ 1.00
    """
    动感变焦    = Effect_meta("动感变焦", True, "7338707315987583488", "47239575", "a36edfb925cbfa69a86a5bdd53f7237f", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    动感扫光    = Effect_meta("动感扫光", True, "7345724656642429452", "50636467", "8df52caeaddcd571a2b6bb325b7209ae", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
    """
    动感推镜    = Effect_meta("动感推镜", True, "7330964667252085248", "43472640", "f482dc307814b8b0697bbf9aa678b5e8", [
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    动感竖线    = Effect_meta("动感竖线", True, "7339899789795922468", "47905484", "798630fbe18ab78b9a751a48341aed8b", [
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.210, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000)])
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
    动感运镜    = Effect_meta("动感运镜", True, "7340866533943415308", "48296868", "e258bc9e064d90c2b65ec5fed2320885", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    十字模糊    = Effect_meta("十字模糊", True, "7156060838334304775", "5508159", "0737102012e5a9451b6dcb842fa3cbf6", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
    """
    十字爆闪    = Effect_meta("十字爆闪", True, "7291868496558821915", "26443872", "04a1a4ff3dec382e6c2b00586ceb301a", [
                              Effect_param("effects_adjust_intensity", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
    """
    单向移动    = Effect_meta("单向移动", True, "7221408305871065661", "12087461", "1efa77e2563de9f51ecf4c8639a995bc", [
                              Effect_param("effects_adjust_speed", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.490, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.49, 0.00 ~ 1.00
    """
    单彩渐变    = Effect_meta("单彩渐变", True, "7296751848508101158", "28007443", "bb064dadbd40eda875b9a632d07c4e3f", [
                              Effect_param("effects_adjust_speed", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
    """
    单色填充    = Effect_meta("单色填充", True, "7128329164314120717", "3956309", "7647e2c7607c75922abb4cd232e83dff", [
                              Effect_param("effects_adjust_range", 0.760, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.360, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.76, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.36, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    卡机        = Effect_meta("卡机", True, "7046676785693463071", "1498082", "ea84ea931c93434b86263b92aabbadd4", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    卡通渲染    = Effect_meta("卡通渲染", True, "7358012370125328937", "57459941", "a0b8524e28d2e4cb243ae5c6a0448fb1", [
                              Effect_param("effects_adjust_size", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.30, 0.00 ~ 1.00
    """
    发光HDR     = Effect_meta("发光HDR", True, "7265989852099777061", "20444395", "ae36dc26cae2cd9b4f66a25dc4323c29", [
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.15, 0.00 ~ 1.00
    """
    取景器      = Effect_meta("取景器", True, "7145432172021682725", "4694121", "76868b9a58758e29212eb76abe18eef2", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.336, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.802, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    变色狙击    = Effect_meta("变色狙击", True, "7146096867544142367", "5418579", "f4876e6aa0a710888c0dded6dd35879c", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    变色闪光    = Effect_meta("变色闪光", True, "7257436414965453368", "18628864", "3f06e59c32f2e12dd4b63686844a0121", [
                              Effect_param("effects_adjust_range", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.850, 0.000, 1.000)])
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
    变速推镜    = Effect_meta("变速推镜", True, "7338347637009027618", "47074578", "81bb946b8dfe47610a322d7f2d2496d9", [
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 2.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 2.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 2.000),
                              Effect_param("effects_adjust_range", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 2.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 2.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 2.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    变速推镜II  = Effect_meta("变速推镜II", True, "7349154305045172736", "53195413", "5b71a4a5390f261a4e400c0dd2e31d0f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    可爱涂鸦    = Effect_meta("可爱涂鸦", True, "7267137261697765943", "20662139", "3b8f6203dfedcd2ff5d17ff6ac6bef78", [
                              Effect_param("sticker", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.180, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000)])
    """参数:
        - sticker: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.18, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
    """
    吓到失魂    = Effect_meta("吓到失魂", True, "7149057547792552456", "4884447", "2ce39d4b185862a94ebaf6d9ca871b96", [
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.707, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.71, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.10, 0.00 ~ 1.00
    """
    噪片映射    = Effect_meta("噪片映射", True, "7130233403898597902", "4002845", "e974f7b6381909e805e37d72c955ab1f", [
                              Effect_param("effects_adjust_noise", 0.343, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    圆形分屏    = Effect_meta("圆形分屏", True, "7298664552793641522", "28683046", "3674e65bf11eb5b60c9ebcb4f7591dbd", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.10, 0.00 ~ 1.00
    """
    圣诞日记    = Effect_meta("圣诞日记", True, "7308639868085604901", "32448752", "360c82d08c822cecb16e79b201768177", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.780, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.78, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    复古彩虹    = Effect_meta("复古彩虹", True, "7269735872445026877", "21148898", "75886bbc57543881343141e58e0c3871", [
                              Effect_param("effects_adjust_size", 0.720, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 0.800),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.72, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 0.80
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.90, 0.00 ~ 1.00
    """
    复古拼贴    = Effect_meta("复古拼贴", True, "7264510800415429177", "20159886", "8628c4e9455115f3c9fac5411de3241e", [
                              Effect_param("effects_adjust_speed", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.440, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.44, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    复古紫调    = Effect_meta("复古紫调", True, "7273707462107075130", "21870120", "eb8220e91369535e0cd5a471fd98b2a2", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.340, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.380, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.260, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.560, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.38, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.26, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.56, 0.00 ~ 1.00
    """
    复古红调    = Effect_meta("复古红调", True, "7170897764744696356", "7308411", "2a96e0c8e739c577b3f3860bad1d0c0a", [
                              Effect_param("effects_adjust_size", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.70, 0.00 ~ 1.00
    """
    复古连拍    = Effect_meta("复古连拍", True, "7078198448045953572", "1644374", "154f59ff4dd71886d96aa36391656a64", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.160, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.16, 0.00 ~ 1.00
    """
    复古闪闪    = Effect_meta("复古闪闪", True, "7039549945338139150", "1475376", "bd1494bd893e3e113ef7ca922f2db8a5", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    复古频闪    = Effect_meta("复古频闪", True, "7343141676828856844", "49278125", "83e65027b467568dbc6dd666658e07d8", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.850, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    失焦CCD     = Effect_meta("失焦CCD", True, "7189438884340568633", "8556597", "e08db3117c2c608d3c1ea94129ff6b27", [
                              Effect_param("effects_adjust_blur", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    失焦光斑    = Effect_meta("失焦光斑", True, "7280121081208246845", "23238701", "01947e259c3fa9990faa6c58345af775", [
                              Effect_param("effects_adjust_size", 0.120, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.850, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.340, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.12, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
    """
    定格祝福    = Effect_meta("定格祝福", True, "7321603111791890982", "39287043", "6ec72c24a543383a74db927a3022e5c1", [
                              Effect_param("effects_adjust_color", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
    """
    实况开幕    = Effect_meta("实况开幕", True, "7367289783153857024", "63011918", "58a0d76b10a23a76f1d7834f097e888a", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
    """
    对焦DV      = Effect_meta("对焦DV", True, "7195792007309038117", "9034919", "e9646eb7d4a371f41bd5e3c151f65589", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.20, 0.00 ~ 1.00
    """
    局部推镜    = Effect_meta("局部推镜", True, "7301528497577529906", "29684830", "a607e28c273a94691df816231b0d5f3c", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    局部色彩    = Effect_meta("局部色彩", True, "7041515097927193125", "1482682", "5a629b9f88febe47a6c99a5113c02d06", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    居中闪切    = Effect_meta("居中闪切", True, "7273800436128158264", "21899077", "98283327a415b5719ca3bec1c713b707", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.00, 0.00 ~ 1.00
    """
    屏幕律动    = Effect_meta("屏幕律动", True, "7119437097697546782", "3529421", "0736478f60e481067bdeadeb1c620e00", [
                              Effect_param("effects_adjust_speed", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
    """
    幻动光斑    = Effect_meta("幻动光斑", True, "7337641482376974883", "46674042", "5ee226902be5ac3294d53fb015b428d8", [
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
    """
    幻彩故障    = Effect_meta("幻彩故障", True, "6912383907191067149", "1005744", "76f90178a99f63e7c95869f597c568cd", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    幻影_I      = Effect_meta("幻影 I", True, "7212904257043829307", "10969387", "6699feabadc4f59732b8087620fc95a6", [
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    弹动摇镜    = Effect_meta("弹动摇镜", True, "7332839146907505215", "44400476", "79ba3b0f0b1687e56a7514a0301e6af0", [
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
    """
    弹动旋入    = Effect_meta("弹动旋入", True, "7377307494097359371", "69256604", "cc9bb0039ebba34a0951ff9c9b8118c4", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    弹性闪动    = Effect_meta("弹性闪动", True, "7161280260435087885", "5718993", "a852817db39ecb51dd2217523a53a032", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    彩光摇晃    = Effect_meta("彩光摇晃", True, "7359557508014281268", "58342723", "b5ec6622597ef93c0ec5c983c2da730b", [
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    彩光频闪    = Effect_meta("彩光频闪", True, "7221126479793361465", "12061167", "41afdc49bdf68220c2a01997091e5cf5", [
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.850, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.260, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.26, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    彩色像素    = Effect_meta("彩色像素", True, "7254126716489044538", "17710540", "065447c724fdfd29412be566af129e90", [
                              Effect_param("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.270, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.27, 0.00 ~ 1.00
    """
    彩色流光_I  = Effect_meta("彩色流光 I", True, "7246400747665887802", "15698169", "77ec3549e15d944b01992551e3e0c35e", [
                              Effect_param("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.590, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.59, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.00, 0.00 ~ 1.00
    """
    彩色流光_II = Effect_meta("彩色流光 II", True, "7251502652549239354", "16940779", "eb006a9670d27e811c07bd7b689bbd99", [
                              Effect_param("effects_adjust_size", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.030, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.03, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    彩色流光_III= Effect_meta("彩色流光 III", True, "7246410407399658043", "15699849", "c605c345e8bfc8d98d054f577d31dc55", [
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.60, 0.00 ~ 1.00
    """
    彩色火焰    = Effect_meta("彩色火焰", True, "6966855040380178981", "1142428", "2a83206eb7f6f9d65af177a29ea223e2", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    彩色珠滴    = Effect_meta("彩色珠滴", True, "7223201236621726264", "12323189", "68bfe7d647af605724dbff1911ad05f6", [
                              Effect_param("effects_adjust_number", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.260, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.26, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    彩色电光    = Effect_meta("彩色电光", True, "7275262942348579389", "22296923", "4486aefcbd511057cafcdcbc13e4f057", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.680, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.68, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    彩色碎彩    = Effect_meta("彩色碎彩", True, "7181402247824151099", "7743725", "4638f92e49b284396403035e0d9f543f", [
                              Effect_param("effects_adjust_speed", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    彩色碎片    = Effect_meta("彩色碎片", True, "7101592529811804679", "2148348", "48d0dd4f0d70a5d8c6b4846792068335", [
                              Effect_param("sticker", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    彩色碎片_II = Effect_meta("彩色碎片 II", True, "7104546559747953166", "2483800", "0a021da140d56312adf53a90ea3780e5", [
                              Effect_param("effects_adjust_speed", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
    """
    彩色闪烁    = Effect_meta("彩色闪烁", True, "7222939637260489274", "12297327", "759bf05e399d90bb465edf21d29dabfc", [
                              Effect_param("effects_adjust_color", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    彩虹光影    = Effect_meta("彩虹光影", True, "7377004728208593447", "69089511", "122551eb93dd49877b59586f7d66d42f", [
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.660, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    彩虹棱镜    = Effect_meta("彩虹棱镜", True, "7195867446429880889", "9053951", "c96f1eba3950dc1bbe134a216ef4a6bb", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.30, 0.00 ~ 1.00
    """
    彩虹泛光    = Effect_meta("彩虹泛光", True, "7195112049876144698", "10021925", "75a2d417b48815ffec602d06baa28e02", [
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
    """
    彩虹闪屏    = Effect_meta("彩虹闪屏", True, "7343557569589285413", "49499805", "aaeae77e0c74db18769bd2cbab83360a", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    彩边频闪    = Effect_meta("彩边频闪", True, "7352815372510171688", "54679766", "9ddcc579cbfbb6350934ea279f7f9f50", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    微震闪黑    = Effect_meta("微震闪黑", True, "7377721589900513818", "69480931", "28471a0d035b66c5b99d954cbcbf496a", [
                              Effect_param("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
    """
    心跳_II     = Effect_meta("心跳 II", True, "7140620970934407693", "4478025", "e940e6b4377d03450c4a53ab618b99f0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.360, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.36, 0.00 ~ 1.00
    """
    快速变焦    = Effect_meta("快速变焦", True, "7281494629483024952", "23539651", "9af1277c92286811b1890ebe1d682237", [
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.285, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.28, 0.00 ~ 1.00
    """
    快闪运镜    = Effect_meta("快闪运镜", True, "7366140711969755674", "62251172", "4e85edcb46572136ce3343e9cdc197d2", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
    """
    恐怖涂鸦    = Effect_meta("恐怖涂鸦", True, "7117142803863310855", "5418578", "b37405a2ca50f0059744dae5b66ff997", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.220, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.22, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.90, 0.00 ~ 1.00
    """
    慢门拖影    = Effect_meta("慢门拖影", True, "7317916065353175579", "37514660", "0bc4e48d7665268ab0f911979fbec195", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.140, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.14, 0.00 ~ 1.00
    """
    手写边框    = Effect_meta("手写边框", True, "7111253709614486029", "3099452", "1562db9ef86c866cdd951885f1fa26f4", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.260, 0.000, 1.000),
                              Effect_param("sticker", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.26, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
    """
    扭动变焦    = Effect_meta("扭动变焦", True, "7338354272280515106", "47079994", "83df4a1fadf009b94e737565720debef", [
                              Effect_param("effects_adjust_size", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.30, 0.00 ~ 1.00
    """
    扭曲变焦    = Effect_meta("扭曲变焦", True, "7299392770534281765", "28941014", "643635cac6435ea88dd6c4a9ae91303f", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.00, 0.00 ~ 1.00
    """
    扭曲模糊    = Effect_meta("扭曲模糊", True, "7210652297754317367", "10694297", "a48e3fb197688fb20a959a961ab54383", [
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.455, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
    """
    抖动模糊    = Effect_meta("抖动模糊", True, "7202812661405323813", "9780487", "416a2f55681bf6951f25fd3c7336025b", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    抽帧拖影    = Effect_meta("抽帧拖影", True, "7353197719587918362", "54890386", "40f732cd394565be3c7764923c5104be", [
                              Effect_param("effects_adjust_blur", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
    """
    拉伸旋镜    = Effect_meta("拉伸旋镜", True, "7359100199437865506", "58077796", "8dd1ef0645dddee8170190583a1ff51a", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.670, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.67, 0.00 ~ 1.00
    """
    拉扯震动    = Effect_meta("拉扯震动", True, "7240010949938123320", "14603013", "3fb05905a15df5a9b23f36a940016e4e", [
                              Effect_param("effects_adjust_distortion", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.00, 0.00 ~ 1.00
    """
    拉镜开幕    = Effect_meta("拉镜开幕", True, "7340923698955686451", "48340294", "5e3de3ba75f157a19687d84df4545bb0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
    """
    拍照定格    = Effect_meta("拍照定格", True, "7358795504966177292", "57913226", "49d70fec464c90afff087cb5854997dd", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
    """
    拖影灯光    = Effect_meta("拖影灯光", True, "7328017754584257075", "42028150", "3e1f119bd6387d1495fe234cf746e5f8", [
                              Effect_param("effects_adjust_number", 0.698, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.336, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    拟截图放大镜= Effect_meta("拟截图放大镜", True, "7028458557058060831", "1478160", "4c962a1294de796686ec24a81a63fe7e", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.00, 0.00 ~ 1.00
    """
    推拉跟随    = Effect_meta("推拉跟随", True, "7380236931893826089", "70944695", "a6fb9367f095b33fa0047a43c2161e74", [
                              Effect_param("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    推拉运镜    = Effect_meta("推拉运镜", True, "7382100760630137381", "71865342", "4b123b8db48a337b91327c2871ca81e0", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.656, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.849, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.85, 0.00 ~ 1.00
    """
    摇晃叠影    = Effect_meta("摇晃叠影", True, "7307264899422360073", "31866711", "2f82ba674fd1d78a14ccb5d384ee3704", [
                              Effect_param("effects_adjust_speed", 0.350, 0.100, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.35, 0.10 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    摇晃推镜    = Effect_meta("摇晃推镜", True, "7311585733976789554", "33958767", "2b806738c3a5e3126a2013cebc2c4913", [
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    摇晃运镜    = Effect_meta("摇晃运镜", True, "7241063267357954619", "14730265", "bbc5f812f50b8ea1aadb3fd6ac2dd6f0", [
                              Effect_param("effects_adjust_speed", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.80, 0.00 ~ 1.00
    """
    撕纸特写    = Effect_meta("撕纸特写", True, "7235886675845452349", "14014573", "c322a330e87f550e0e56c7cef60e6465", [
                              Effect_param("effects_adjust_speed", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    播放界面    = Effect_meta("播放界面", True, "7078880636584333838", "1647944", "ce6641cd0add17ae5b20286b8a8ff72f", [
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.20, 0.00 ~ 1.00
    """
    故障定格    = Effect_meta("故障定格", True, "7223652101287580216", "12383111", "18c3c5143edfcf076876fc70566fd521", [
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    故障开幕    = Effect_meta("故障开幕", True, "7338335435959046656", "47063402", "43a746efc920f57c2b2196446992f4cf", [
                              Effect_param("effects_adjust_sharpen", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_sharpen: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    故障震闪    = Effect_meta("故障震闪", True, "7315262223213924873", "35954280", "510623ce6e6c3d77151024fe04eb30dd", [
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.714, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.71, 0.00 ~ 1.00
    """
    散光弹动    = Effect_meta("散光弹动", True, "7347985147662176807", "52013378", "1d1f9cc33d051f8c2942cbc86de9f6dd", [
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
    """
    散光闪烁    = Effect_meta("散光闪烁", True, "7338348256226710016", "47894032", "6353300f8b3c913e3a1d60321fd2cc21", [
                              Effect_param("effects_adjust_intensity", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    数字矩阵    = Effect_meta("数字矩阵", True, "7254547645903934010", "17852330", "53625d829446e44920b2397cf4336180", [
                              Effect_param("effects_adjust_blur", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.33, 0.00 ~ 1.00
    """
    斜线震动    = Effect_meta("斜线震动", True, "7244511673409606201", "15332069", "154a4e843d36fe8660f15624a330d2a1", [
                              Effect_param("effects_adjust_size", 0.409, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.704, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.339, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.41, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    新年仙女棒  = Effect_meta("新年仙女棒", True, "7321990419351343653", "39297699", "878e6aaf1e19c6de170d4544c22c38b2", [
                              Effect_param("effects_adjust_size", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.480, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.780, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.48, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.78, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
    """
    方形模糊    = Effect_meta("方形模糊", True, "7384032238951731739", "72505526", "0883434b90fbeaf428ac86a0f87cb4fe", [
                              Effect_param("effects_adjust_blur", 0.877, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.450, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.88, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.45, 0.00 ~ 1.00
    """
    旋焦        = Effect_meta("旋焦", True, "7224445669698703909", "12505491", "c83771425ffddd97d3389480f0f68927", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    旋焦推镜    = Effect_meta("旋焦推镜", True, "7351324357425107519", "53786746", "bfffafcc16a30af7d6faaf7816bd09cf", [
                              Effect_param("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    旋转变焦    = Effect_meta("旋转变焦", True, "7311544501057622555", "33928843", "46f6856d1b6c40a7d6b7c6da0ae24439", [
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.15, 0.00 ~ 1.00
    """
    旋转回弹    = Effect_meta("旋转回弹", True, "7343557174058029568", "49499445", "fcc043da345af8e07d700f1d13d32dd8", [
                              Effect_param("effects_adjust_speed", 0.660, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
    """
    旋转圆球    = Effect_meta("旋转圆球", True, "7382147305350107700", "71888863", "bc332eeb63f21a5f48f90221ed709196", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    旋转抖动    = Effect_meta("旋转抖动", True, "7324315025558999602", "40324156", "a2df1870a268dac31ac369382c42cf43", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
    """
    旋转抖动_II = Effect_meta("旋转抖动 II", True, "7347956961318539826", "51995951", "a080eeb37e5c98ff3a510c395463727a", [
                              Effect_param("effects_adjust_speed", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
    """
    星星变焦    = Effect_meta("星星变焦", True, "7169474672671592991", "6661731", "daedab920b87b778c4f7c672928dbf96", [
                              Effect_param("effects_adjust_size", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.70, 0.00 ~ 1.00
    """
    曝光变焦    = Effect_meta("曝光变焦", True, "7259639809491079737", "19104048", "b66ceb2594aee2fd5a1ace6a67e4db0f", [
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    曝光扩散    = Effect_meta("曝光扩散", True, "7340136879615906344", "47990686", "f01002b2853ba8736b02ee943e132421", [
                              Effect_param("effects_adjust_luminance", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    曲线模糊    = Effect_meta("曲线模糊", True, "7340622176065688098", "48215352", "b140dc7906477e7462636a93f5c9fe3c", [
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.366, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.425, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.37, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.42, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    极速旋转    = Effect_meta("极速旋转", True, "7343542497651462708", "49487569", "c6f8519f592a44f74424411e304bd46b", [
                              Effect_param("effects_adjust_speed", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
    """
    柔和辉光    = Effect_meta("柔和辉光", True, "7249209626829263421", "16279737", "805d415643265f3625c1fb9d55822e32", [
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    梦幻辉光    = Effect_meta("梦幻辉光", True, "7355386179308491300", "56065875", "4f0997824f81dc66309050646ce45bae", [
                              Effect_param("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.300, 0.000, 2.000),
                              Effect_param("effects_adjust_blur", 0.200, 0.000, 1.500)])
    """参数:
        - effects_adjust_luminance: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.30, 0.00 ~ 2.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.50
    """
    模拟拍照    = Effect_meta("模拟拍照", True, "7349154734537708084", "53350183", "2cb9807eebb8a358bc01e02e4a1d48b9", [
                              Effect_param("effects_adjust_blur", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    横向闪光    = Effect_meta("横向闪光", True, "7242555690965799483", "14965785", "0e48afbc4e9aa05505644493cbb7156a", [
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    横条开幕    = Effect_meta("横条开幕", True, "7381442168759521792", "71626094", "5fa33938a1ad4a956bbac1b3e9805969", [
                              Effect_param("effects_adjust_speed", 0.667, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    樱花飘落    = Effect_meta("樱花飘落", True, "7207718227382637113", "10348463", "e70695e42c80f681ed4e173b4735ac0b", [
                              Effect_param("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    欧根纱II    = Effect_meta("欧根纱II", True, "7366882927801537024", "62749085", "aebc534e02b822de7d014b33d5ac103c", [
                              Effect_param("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.40, 0.00 ~ 1.00
    """
    气球花花    = Effect_meta("气球花花", True, "7231385092193522235", "13400477", "bd2685c4dba13e0e4e44cd4f0a9ff834", [
                              Effect_param("effects_adjust_speed", 0.700, 0.000, 1.000),
                              Effect_param("sticker", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    氛围边框    = Effect_meta("氛围边框", True, "7308944810646180379", "32599175", "657d08f76bf5e462d0acb066315d7e32", [
                              Effect_param("effects_adjust_texture", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.800),
                              Effect_param("effects_adjust_luminance", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.80
        - effects_adjust_luminance: 默认0.10, 0.00 ~ 1.00
    """
    水光影      = Effect_meta("水光影", True, "7122736441053942285", "3687389", "0e8f5cf28c600c62140c2f3666dbe18b", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.15, 0.00 ~ 1.00
    """
    水波倒影    = Effect_meta("水波倒影", True, "7313842878847914547", "35129784", "d151e3575ce8eca803787e849b2ee7f4", [
                              Effect_param("effects_adjust_vertical_shift", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
    """
    水波模糊    = Effect_meta("水波模糊", True, "7047088638932292127", "1499278", "99199baa75373b4a0faa08aa1c27a37a", [
                              Effect_param("effects_adjust_horizontal_chromatic", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_chromatic: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    水波泛起    = Effect_meta("水波泛起", True, "7250433374882370103", "16641371", "eda468a5537c139c6355e5abd75004de", [
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.440, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.460, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.44, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.46, 0.00 ~ 1.00
    """
    水波流动    = Effect_meta("水波流动", True, "7140273505630687780", "4458607", "7dd5dbc55d5db8553d233fee727c40ac", [
                              Effect_param("effects_adjust_distortion", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
    """
    水滴扩散    = Effect_meta("水滴扩散", True, "7221508316852130362", "12112703", "b4690abcdd92f98e3291fdcb74444f5b", [
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
    """
    油画模糊    = Effect_meta("油画模糊", True, "7232232188278739493", "13537551", "f727569dc65078e90f66c9e63d3f9712", [
                              Effect_param("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.403, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.40, 0.00 ~ 1.00
    """
    法式暖调    = Effect_meta("法式暖调", True, "7090546987170271780", "1747384", "f47d4affff8b734ed6c3b9042e81f7a4", [
                              Effect_param("effects_adjust_size", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    法式涂鸦    = Effect_meta("法式涂鸦", True, "7253039682877919803", "17395354", "2519d69e2fe1fbe64a653b570e786a0c", [
                              Effect_param("effects_adjust_color", 0.610, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.661, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.720, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.61, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.72, 0.00 ~ 1.00
    """
    泛光扫描    = Effect_meta("泛光扫描", True, "7134989289498087967", "4217252", "5c2fe2a8c4212ee879c16bea71b31e96", [
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, 0.00 ~ 1.00
    """
    泛光爆闪    = Effect_meta("泛光爆闪", True, "7254484266996732476", "17821188", "7eeab42db5ca9a73186fe4f445b7613c", [
                              Effect_param("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    泛光闪动    = Effect_meta("泛光闪动", True, "7236298986993226301", "14080033", "982d5dfb68207b458e4061c6a8742482", [
                              Effect_param("effects_adjust_blur", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    泡泡光斑    = Effect_meta("泡泡光斑", True, "7320155012036825610", "38547267", "a8ef5cdbe91838c8092a05a4ee2abf28", [
                              Effect_param("effects_adjust_size", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.300, 0.000, 1.000)])
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
    泡泡冲屏    = Effect_meta("泡泡冲屏", True, "7373963046693114387", "67466796", "51ea34188c370cae7e764a47be73d6a3", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 0.800)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 0.80
    """
    波动清晰    = Effect_meta("波动清晰", True, "7340620060362281512", "48213992", "d4009f4188b7c8293760896d5a606f0f", [
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
    """
    波浪        = Effect_meta("波浪", True, "7159183282632921631", "5574521", "2d803403ccfbeb2328a811014a55081f", [
                              Effect_param("effects_adjust_speed", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.780, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.78, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    波浪丝印    = Effect_meta("波浪丝印", True, "7146406661249307150", "4880117", "cf32c231aa6b092d39cbcd7c346db5a3", [
                              Effect_param("effects_adjust_texture", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    波纹闪动    = Effect_meta("波纹闪动", True, "7332415663106953769", "44222768", "7efba1463deb33955572e53ec6bd71be", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
    """
    流体冲屏    = Effect_meta("流体冲屏", True, "7221730308251456037", "12130415", "958711bf2dc7393f39862e7952f6b5c5", [
                              Effect_param("effects_adjust_speed", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    流体荡开    = Effect_meta("流体荡开", True, "7322018576125137417", "39315461", "fa0a0cd4b5446445108d6b4d44466739", [
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    海报描边    = Effect_meta("海报描边", True, "7133104392231719431", "4118241", "9b6e240d941ae5e77e573cd584265e77", [
                              Effect_param("effects_adjust_noise", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
    """
    海鸥DC      = Effect_meta("海鸥DC", True, "7051853636548170271", "1520896", "b9dc0143d875fbff52cb26f363f45d14", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    液态分离    = Effect_meta("液态分离", True, "7241096748184113701", "14742833", "c24d9c1a2bf816e305645ee216b75e30", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    漂浮爱心    = Effect_meta("漂浮爱心", True, "7306769922535723558", "31585739", "2a84ea537b525994b2803d6a538960e1", [
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    潮流涂鸦    = Effect_meta("潮流涂鸦", True, "7350240257914180135", "53198933", "9d284a90662cd32eeb4e8228a379c441", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    瀑布开幕    = Effect_meta("瀑布开幕", True, "7351689682138174006", "54008092", "ecd11cf24ab2644cc93ae00f4ad1a7d3", [
                              Effect_param("effects_adjust_speed", 0.570, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.260, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.57, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.26, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
    """
    灵魂出窍_II = Effect_meta("灵魂出窍 II", True, "7299377358283215398", "28934274", "4e2c3e0ff21146736ddfeea23e6affaa", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.85, 0.00 ~ 1.00
    """
    灿灿金币    = Effect_meta("灿灿金币", True, "7304546673215148595", "30737307", "921df9ceada99345eff8e577b1e10722", [
                              Effect_param("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.80, 0.00 ~ 1.00
    """
    灿金彩带    = Effect_meta("灿金彩带", True, "7308706488686481947", "33271125", "22171c77551d5769904778e3bd386859", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.25, 0.00 ~ 1.00
    """
    炫光变焦    = Effect_meta("炫光变焦", True, "7002109122350944781", "1237470", "8b94fb6f9bacb3eab0d44fc8bad3ddd1", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.753, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    炫光扫描    = Effect_meta("炫光扫描", True, "7367314177741820435", "63023070", "79582fc0a97afe1fcd4fb0199d07bc7d", [
                              Effect_param("effects_adjust_speed", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.660, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.66, 0.00 ~ 1.00
    """
    烟花2024    = Effect_meta("烟花2024", True, "7308706250731033097", "36744068", "511dd4d1de63c4839c5912c69711e8cf", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.770, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.625, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.77, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.62, 0.00 ~ 1.00
    """
    热恋        = Effect_meta("热恋", True, "7195020880018149944", "9062069", "d4a9c95961f95536f3fc44096bf62cbd", [
                              Effect_param("effects_adjust_size", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.060, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.06, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    爆闪锐化    = Effect_meta("爆闪锐化", True, "7222907722486780472", "12284805", "389b3c8872b9a18e5fe570975e3aa2ae", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.70, 0.00 ~ 1.00
    """
    爱心扫光    = Effect_meta("爱心扫光", True, "7322345920962499123", "39420273", "e1629600c228ebd43732cb589c245168", [
                              Effect_param("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
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
    爱心气球    = Effect_meta("爱心气球", True, "7268210584707928634", "20875808", "ec80143a43c12596d99f8c31043c6a8b", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    爱心软糖    = Effect_meta("爱心软糖", True, "7331625316885991970", "43774786", "0bab0476804fd6ac903bda686f49f3cb", [
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.90, 0.00 ~ 1.00
    """
    爱心边框    = Effect_meta("爱心边框", True, "7065927898833621511", "1572505", "2f62bf787eb44535dbd128d60f46a29c", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.00, 0.00 ~ 1.00
    """
    珠光Kira    = Effect_meta("珠光Kira", True, "7267917946733728314", "20820466", "235af2aa5680584b232598629e70b990", [
                              Effect_param("effects_adjust_number", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    珠光碎闪    = Effect_meta("珠光碎闪", True, "7265695554640810533", "20405527", "325258e144f2c6417f123d48886356de", [
                              Effect_param("effects_adjust_filter", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.15, 0.00 ~ 1.00
    """
    电光描边    = Effect_meta("电光描边", True, "7106762731960668703", "2721906", "15153b69c032c89f4087d12ef7a613ca", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
    """
    电光波动    = Effect_meta("电光波动", True, "7301674026173207066", "29755128", "9d7a93ea28f697fbc109cd26377d025d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 2.000),
                              Effect_param("effects_adjust_color", 0.030, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 2.00
        - effects_adjust_color: 默认0.03, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    电光爆闪    = Effect_meta("电光爆闪", True, "7306471467397419547", "31478585", "dfc0eec30caaa1a9f992332a85e89a7b", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    电光爆闪_II = Effect_meta("电光爆闪 II", True, "7349150013441708559", "52650215", "8129e3f83ad6973ba9e6613dbf7afb88", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
    """
    电光爱心    = Effect_meta("电光爱心", True, "7106779118867321357", "2724410", "04883bbcc4ce20a240d5f90dc34db76f", [
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.419, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.473, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.590, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.42, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.47, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.59, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认1.00, 0.00 ~ 1.00
    """
    电音故障    = Effect_meta("电音故障", True, "7246745900473651773", "15772327", "fdec63c54f10bf1b8b557a3709196eff", [
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.580, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.58, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    画质清晰    = Effect_meta("画质清晰", True, "7348707427165934107", "52400085", "4a35ff3b8a83d2cec2d56e5651f9e04a", [
                              Effect_param("effects_adjust_luminance", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.800, 0.000, 2.000),
                              Effect_param("effects_adjust_blur", 0.300, 0.000, 1.500),
                              Effect_param("effects_adjust_range", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.80, 0.00 ~ 2.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.50
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.33, 0.00 ~ 1.00
    """
    白鸽        = Effect_meta("白鸽", True, "7382490757770252827", "71992424", "3e6056fb9e3a1829a666c6680f7eab83", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    相片定格    = Effect_meta("相片定格", True, "7265526511220822586", "20350863", "a58e3178d3a498edac53074a3c3a7542", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.850, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    矩阵频闪    = Effect_meta("矩阵频闪", True, "7306346511367934491", "31403673", "51763569c67e833ffcb37bd41a365c75", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.880, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.88, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    碎闪描边    = Effect_meta("碎闪描边", True, "7130585329609740814", "4007289", "680eaa2d8db4fd3a5d33cf5399e61518", [
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
    """
    磁带DV      = Effect_meta("磁带DV", True, "7101987162526061070", "2211756", "b6b5848678e71593cf7e5112874b9939", [
                              Effect_param("effects_adjust_sharpen", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_sharpen: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    磨砂水晶    = Effect_meta("磨砂水晶", True, "7090380952605561381", "1729610", "f0d404000523379787cffd6e1db715c2", [
                              Effect_param("effects_adjust_vertical_shift", 0.000, -1.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.000, -1.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.00, -1.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, -1.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    神龙纳福    = Effect_meta("神龙纳福", True, "7326853354615738889", "41485429", "de1999f4a3c33b823bd0ab1b24142adb", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    秋日暖阳    = Effect_meta("秋日暖阳", True, "7156868464894808583", "5408805", "62cdcc8cc7c26ea48447578ee57b5f35", [
                              Effect_param("effects_adjust_blur", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    移轴模糊    = Effect_meta("移轴模糊", True, "7246784641384845861", "15780929", "ceae265f1f63d74a4816f647710885a3", [
                              Effect_param("effects_adjust_range", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.00, 0.00 ~ 1.00
    """
    竖向开幕    = Effect_meta("竖向开幕", True, "7384009190836015654", "72501890", "26c9cc8d460d2639fe4fbb0bbd012d41", [
                              Effect_param("effects_adjust_blur", 0.877, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.88, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.60, 0.00 ~ 1.00
    """
    竖向闪光    = Effect_meta("竖向闪光", True, "7212938795702817338", "10976911", "7529d488cc18a6fb4a7e58c4ef3af378", [
                              Effect_param("effects_adjust_number", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.690, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.69, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    竖线屏闪    = Effect_meta("竖线屏闪", True, "7304258446658900489", "30666842", "4444e09ba223f94827fb9d423f445a71", [
                              Effect_param("effects_adjust_luminance", 1.700, 0.000, 2.300),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 2.500),
                              Effect_param("effects_adjust_range", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 2.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认1.70, 0.00 ~ 2.30
        - effects_adjust_blur: 默认1.00, 0.00 ~ 2.50
        - effects_adjust_range: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 2.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    竖闪模糊    = Effect_meta("竖闪模糊", True, "7291135061494075960", "26216108", "795af3daacce29e8d7732e5b2223e01a", [
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
    """
    粉雪        = Effect_meta("粉雪", True, "7298283919944716827", "28549704", "273f611315ca2f66e370a3a77de6185c", [
                              Effect_param("effects_adjust_background_animation", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.950, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.95, 0.00 ~ 1.00
    """
    粒子放射    = Effect_meta("粒子放射", True, "7217716815407878693", "11587497", "df109cf35978de6bcc3803f559b14b07", [
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    精致辉光    = Effect_meta("精致辉光", True, "7368344527494451712", "63611181", "ad7fae5b6c5335be75113171ab5a6b6d", [
                              Effect_param("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.850, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.40, 0.00 ~ 1.00
    """
    紫光夜      = Effect_meta("紫光夜", True, "7311995150962528778", "34184103", "1a4c76312950f09d8fd14e68de775bd8", [
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    繁花棱镜II  = Effect_meta("繁花棱镜II", True, "7269749564658160184", "21150170", "f0d388c9f42348261ed7b6871cfaa86e", [
                              Effect_param("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.30, 0.00 ~ 1.00
    """
    红蓝魔      = Effect_meta("红蓝魔", True, "7122384870294163975", "3675609", "0c7634532abc28facafe3afe024a4fbc", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    红边模糊    = Effect_meta("红边模糊", True, "7130591331700707876", "4007601", "1afa6bef0ff1ddd4e54c13a2d6a7c59a", [
                              Effect_param("effects_adjust_blur", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.90, 0.00 ~ 1.00
    """
    纵向跳动    = Effect_meta("纵向跳动", True, "7190200556692967995", "8626971", "95f1d0f51d2eb529ac7b97c8cddbfaf1", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认1.00, 0.00 ~ 1.00
    """
    纸质抽帧    = Effect_meta("纸质抽帧", True, "7046650052286091812", "1534320", "1d4d7f2a92315acd523dbfe21176cfbf", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    线光变速    = Effect_meta("线光变速", True, "7367628113062138377", "63209940", "87a99c8ae0f9e333abaef48b79a96c90", [
                              Effect_param("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    线条涂鸦    = Effect_meta("线条涂鸦", True, "7266446552258843173", "20547949", "33b11d3bd867449b2fcc21c349b33639", [
                              Effect_param("effects_adjust_texture", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 0.800),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 0.80
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    缤纷        = Effect_meta("缤纷", True, "7072268839303516709", "1607634", "4294dd203d48821ed92525b79f704231", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    网点丝印    = Effect_meta("网点丝印", True, "7146404902971904548", "4879935", "01312233fbabf72f4f66ac30f84c020c", [
                              Effect_param("effects_adjust_texture", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    群蝶飞舞    = Effect_meta("群蝶飞舞", True, "7347658324956942883", "51832286", "88f861bb14eac5dae7fe7e5df123d718", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
    """
    羽毛飘落    = Effect_meta("羽毛飘落", True, "7379513630837969445", "70529088", "46f1c56f6fcd3a2abd80ff7d701f6eb0", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.260, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.108, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.26, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.11, 0.00 ~ 1.00
    """
    翻转变焦    = Effect_meta("翻转变焦", True, "7299377095107416585", "28934164", "6c5f82fb84dc77d361ae83657259bc19", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
    """
    翻转开幕    = Effect_meta("翻转开幕", True, "7235902836188385852", "14020695", "a4d3d6cc942a659f39cc5bbcb90b516e", [
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.10, 0.00 ~ 1.00
    """
    老式DV      = Effect_meta("老式DV", True, "7026261220961292807", "1426168", "9b7fc1e4ed44a38366a37377d7003192", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.630, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.63, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.30, 0.00 ~ 1.00
    """
    胶片V       = Effect_meta("胶片V", True, "7151967279817691662", "5050659", "e8dabb72421c2773120bfc6d4d3785f0", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    胶片冷绿    = Effect_meta("胶片冷绿", True, "7146524414312452645", "4837281", "52a78b591b893502154b101c757877db", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    胶片暖棕    = Effect_meta("胶片暖棕", True, "7145385234320593439", "4837280", "bcb9ebf14085e77e8b0e1cd1cf0a87f8", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
    """
    胶片滚动    = Effect_meta("胶片滚动", True, "7080354236956938782", "1655466", "a05a7b82f4d36066ef3d6630bb1be809", [
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    胶片闪切    = Effect_meta("胶片闪切", True, "7384745950608101924", "72761923", "347713d7f8a7b69b1885ee9d38cd8de6", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    脉搏跳动    = Effect_meta("脉搏跳动", True, "7052226294972420621", "1522814", "c65fc5a267dde559e80e16c8fcc9cd6c", [
                              Effect_param("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
    """
    色差震闪    = Effect_meta("色差震闪", True, "7355109046694711871", "55932216", "b4d72c47be1ca1238cddf0790a8a0c55", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    色散冲击    = Effect_meta("色散冲击", True, "7374053937369846307", "67503542", "ed2771a77992c0f8d0958bbaadbba53e", [
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
    """
    色散故障    = Effect_meta("色散故障", True, "7242574690638631479", "14972687", "5989d49ac22b81107c9741367ae6651d", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    花屏故障    = Effect_meta("花屏故障", True, "7361718823575097919", "59487955", "93a206e311d0b8128da7ee0ee776c917", [
                              Effect_param("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.143, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_chromatic: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.14, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    花瓣环绕    = Effect_meta("花瓣环绕", True, "7345688874577826342", "50608291", "d954d5148a1d1ec24016499b38b85d1d", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.33, 0.00 ~ 1.00
    """
    菱形光斑    = Effect_meta("菱形光斑", True, "7316813562783994395", "40449614", "8baa04aecc7a8e40d9c71cb3c7a91f33", [
                              Effect_param("effects_adjust_filter", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.230, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.23, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.75, 0.00 ~ 1.00
    """
    菱形变焦    = Effect_meta("菱形变焦", True, "7147943538120987166", "4841353", "fda851ab65ee2b7bd6bb568a0e8bc544", [
                              Effect_param("effects_adjust_size", 0.521, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.720, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.52, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.72, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
    """
    落叶_II     = Effect_meta("落叶 II", True, "7153556255263429151", "5418631", "a7658052127fea9d33b12696e2d71ca4", [
                              Effect_param("effects_adjust_size", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    蓝光爆闪    = Effect_meta("蓝光爆闪", True, "7288655540341707324", "25450329", "363de1da61a76d9d902e62a7bed611e6", [
                              Effect_param("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.650, 0.010, 1.000),
                              Effect_param("effects_adjust_range", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.65, 0.01 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.80, 0.00 ~ 1.00
    """
    蓝色丝印    = Effect_meta("蓝色丝印", True, "7131985730791805448", "4097661", "0fceb871b844d51454db5d59da3636ef", [
                              Effect_param("effects_adjust_texture", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    虹光旋入    = Effect_meta("虹光旋入", True, "7377352335028130367", "69273433", "bf6fb74a7290e9a8d31dc36453736b66", [
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.660, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.66, 0.00 ~ 1.00
    """
    视频播放    = Effect_meta("视频播放", True, "7144915597308989988", "4668537", "7a18d00c453615e8415306a7f1f37396", [
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    负片分屏    = Effect_meta("负片分屏", True, "7278974994623763003", "22907949", "5a980a6a4a707fc1ad13caff77e3926a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.33, 0.00 ~ 1.00
    """
    负片涂鸦    = Effect_meta("负片涂鸦", True, "7157966185571553822", "5477607", "c622911e77150d8ec0e9c4ecde458c02", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    负片涂鸦_II = Effect_meta("负片涂鸦 II", True, "7231111030028374584", "13379581", "02590242d94571bb62a8635b4fd5a3f7", [
                              Effect_param("effects_adjust_texture", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.320, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.32, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
    """
    负片涂鸦_III= Effect_meta("负片涂鸦 III", True, "7267517097775731261", "20745376", "96a028c1ac17f22a452c1e012d47f3ed", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.00, 0.00 ~ 1.00
    """
    负片游移    = Effect_meta("负片游移", True, "7091488033555354120", "1787254", "bc811feeac5b5e4608cbb80c99a07d46", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.000, -1.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.000, -1.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.00, -1.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, -1.00 ~ 1.00
    """
    负片频闪    = Effect_meta("负片频闪", True, "7153575555554611720", "5155369", "c737112d913d14f6cc8871dbc51c8013", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.85, 0.00 ~ 1.00
    """
    超大光斑    = Effect_meta("超大光斑", True, "7171321435200164383", "6691829", "8f525928d0c73912e59702928d728ef2", [
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.20, 0.00 ~ 1.00
    """
    超强锐化    = Effect_meta("超强锐化", True, "7129336892121682468", "3950243", "f5d68fac1d5f2d24144d143772c4d41b", [
                              Effect_param("effects_adjust_sharpen", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_sharpen: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    跟随运镜    = Effect_meta("跟随运镜", True, "7299426452896748042", "28956878", "4c501e2a054c24f4268b4daa44460f90", [
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.15, 0.00 ~ 1.00
    """
    跟随运镜_II = Effect_meta("跟随运镜 II", True, "7340954638184616467", "48362872", "d34cbcf01362bf60945dafa56ec5704b", [
                              Effect_param("effects_adjust_range", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.400, 0.100, 1.000),
                              Effect_param("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.40, 0.10 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.80, 0.00 ~ 1.00
    """
    车窗_II     = Effect_meta("车窗 II", True, "7109280482025542157", "4795296", "bb46f32dec1993f4c7457360fd61af7c", [
                              Effect_param("effects_adjust_range", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("sticker", 0.350, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - sticker: 默认0.35, 0.00 ~ 1.00
    """
    辉光开幕    = Effect_meta("辉光开幕", True, "7338322046822126114", "47051728", "a37854eb4a70d1f149c417ce3269a8f5", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.270, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.27, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
    """
    边缘扫光    = Effect_meta("边缘扫光", True, "7322363012092793353", "39434745", "8b7a9733b393b42cf018ce2efdebca2a", [
                              Effect_param("effects_adjust_soft", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_soft: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    迷幻故障    = Effect_meta("迷幻故障", True, "7265960462330630714", "20440246", "5ddfb1bd3479179af2c0ec0026b57e3e", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    迷幻荡漾    = Effect_meta("迷幻荡漾", True, "7223208176206746173", "12324741", "1ab6e40160a674cd19de3ade157a3d0b", [
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    迷幻震动    = Effect_meta("迷幻震动", True, "7238863029775897148", "14438877", "e28a153a03d2dcf1a12384712196bc07", [
                              Effect_param("effects_adjust_distortion", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
    """
    重复变焦    = Effect_meta("重复变焦", True, "7161285099667853831", "5719311", "ae41555c055c73d2089f1d681f2bcc20", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    重复震闪    = Effect_meta("重复震闪", True, "7250369682207674938", "16610415", "63a7958ffc3e6a73d3b9556f7ca04381", [
                              Effect_param("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    金色碎片    = Effect_meta("金色碎片", True, "7106040163402256927", "2622164", "a24eabdabec50f5d52f7e6fb099c899c", [
                              Effect_param("effects_adjust_speed", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.30, 0.00 ~ 1.00
    """
    金边闪烁    = Effect_meta("金边闪烁", True, "7304832158466576947", "30855689", "46b93ae5afcb00ecface4fd485014d9c", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    银杏飘落    = Effect_meta("银杏飘落", True, "7296789290724364850", "28024643", "c1b8196608a6ef6b142389f499647275", [
                              Effect_param("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.000, 0.100, 1.000),
                              Effect_param("effects_adjust_size", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.00, 0.10 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.10, 0.00 ~ 1.00
    """
    闪光弹跳    = Effect_meta("闪光弹跳", True, "7210315941396091447", "10660327", "982ccb302cc81c13762eb31a25c54de5", [
                              Effect_param("effects_adjust_speed", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
    """
    闪光灯_II   = Effect_meta("闪光灯 II", True, "7143919857539486238", "4795220", "1b9f1a3ee39a65820ae21d72793c89a9", [
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    闪光灯IV    = Effect_meta("闪光灯IV", True, "7276317197658493498", "22328905", "db710dc6b5ea5b2f46595480d06d0d7d", [
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    闪电扭曲    = Effect_meta("闪电扭曲", True, "7329871968298078759", "42913127", "244819f79dffa729f9c9caeeb15a7698", [
                              Effect_param("effects_adjust_luminance", 0.666, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    闪白_II     = Effect_meta("闪白 II", True, "7281219213828559397", "23489443", "631162213ead8ced21aa7936bae06390", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 2.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 2.00
    """
    随机闪切    = Effect_meta("随机闪切", True, "7267909305519575608", "20816436", "6a5fa04981e50a2c7bd67a4e03e4d3e6", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.20, 0.00 ~ 1.00
    """
    随机马赛克  = Effect_meta("随机马赛克", True, "7299769859900969510", "29099986", "190ec4ff873df478cd8842c1c9a9f967", [
                              Effect_param("effects_adjust_size", 0.280, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.220, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.28, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.22, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
    """
    隔行DV      = Effect_meta("隔行DV", True, "7215598241558041125", "11331317", "3429986a54fc1d15cc29f7340103540d", [
                              Effect_param("effects_adjust_blur", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.20, 0.00 ~ 1.00
    """
    雨季_I      = Effect_meta("雨季 I", True, "7149065282768605732", "6731496", "fe78f4e40b597e3170f46831622f8e06", [
                              Effect_param("effects_adjust_blur", 0.160, 0.000, 0.800),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.336, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.16, 0.00 ~ 0.80
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
    """
    雪花光斑    = Effect_meta("雪花光斑", True, "7296707597707514406", "27986887", "b6b5e079f2c4079d72185fb43cfc7521", [
                              Effect_param("effects_adjust_background_animation", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.100, 0.000, 1.000),
                              Effect_param("sticker", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.10, 0.00 ~ 1.00
        - sticker: 默认0.60, 0.00 ~ 1.00
    """
    雪雾        = Effect_meta("雪雾", True, "7303380658934518323", "30305488", "bc0e8be4f1a2d7171824311ce9e57c44", [
                              Effect_param("sticker", 0.280, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.300, 0.000, 1.000)])
    """参数:
        - sticker: 默认0.28, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.30, 0.00 ~ 1.00
    """
    雾镜_II     = Effect_meta("雾镜 II", True, "7147920433604465159", "6731657", "627544f24ff53bde600ab918cb51a17d", [
                              Effect_param("effects_adjust_blur", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    震动光束    = Effect_meta("震动光束", True, "7246758527992074811", "15775885", "5c4feafe4eb534961c0df1cadb899e83", [
                              Effect_param("effects_adjust_intensity", 0.420, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.160, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.490, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.42, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.16, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.49, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.75, 0.00 ~ 1.00
    """
    震动发光    = Effect_meta("震动发光", True, "7249264623226982968", "16303237", "ce596725c52c5cfa0e8205c1cbc00585", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
    """
    震动屏闪    = Effect_meta("震动屏闪", True, "7171697545154925069", "6733311", "c83c072fdbd9921701f12498c0c00cfc", [
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
    """
    震动扫光    = Effect_meta("震动扫光", True, "7374053409546048052", "67503342", "3b86c556d5a92c8937b1120823bc34b2", [
                              Effect_param("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.40, 0.00 ~ 1.00
    """
    震动推镜    = Effect_meta("震动推镜", True, "7345004981029704233", "50238678", "47b846ada207d95dce6bc0501102db85", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.220, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.22, 0.00 ~ 1.00
    """
    震闪渐黑    = Effect_meta("震闪渐黑", True, "7304249285577544201", "30662744", "dfddc3aedd22941d50e768623fbd60ba", [
                              Effect_param("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.100, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.10 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
    """
    霓虹光线    = Effect_meta("霓虹光线", True, "7254125922222084663", "17710570", "c2274095125803b495db0623740fcb22", [
                              Effect_param("effects_adjust_luminance", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, 0.00 ~ 1.00
    """
    霓虹闪切    = Effect_meta("霓虹闪切", True, "7345353688774349348", "50455778", "32ab9ae1b2f18168bb5d78bfdfda9176", [
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.825, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.82, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认1.00, 0.00 ~ 1.00
    """
    马赛克闪切  = Effect_meta("马赛克闪切", True, "7308712918902641203", "32503798", "6b0566a1868f7a088935c8835052db63", [
                              Effect_param("effects_adjust_size", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.130, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.13, 0.00 ~ 1.00
    """
    高速彩光    = Effect_meta("高速彩光", True, "7343527966145516042", "49475327", "e92f5749fec01ea61ad9d6747d808f82", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    鱼眼_II     = Effect_meta("鱼眼 II", True, "7023664868083372580", "1418072", "3961e7c38420d89d64c5d267a3068254", [
                              Effect_param("effects_adjust_speed", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.80, 0.00 ~ 1.00
    """
    鱼眼_III    = Effect_meta("鱼眼 III", True, "7051881765975101983", "1521356", "b2620a812f8a4e48121a0e18cf36233e", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.30, 0.00 ~ 1.00
    """
    鱼眼_IV     = Effect_meta("鱼眼 IV", True, "7091597643553444359", "1790048", "5977716750083a4ded0565086be43e07", [
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.55, 0.00 ~ 1.00
    """
    黑白胶片    = Effect_meta("黑白胶片", True, "7085992144627831326", "1691558", "708a2e34f1ecf5774e910d8da7099304", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """

class Video_character_effect_type(Effect_enum):
    """剪映自带的人物特效类型"""

    BOOM        = Effect_meta("BOOM！", False, "6999560597230588429", "1378605", "a7d5d3fbae39950e51bff93b92ad7792", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    X           = Effect_meta("X", False, "7037006820749087246", "1464226", "ec38784544361583ed45aa333ebdf2c9", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    crash       = Effect_meta("crash！", False, "6999887184018805285", "1378609", "47b6f315a86918e23d94d35c69946fe1", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    中刀        = Effect_meta("中刀", False, "7029514054179754510", "1436386", "ad3377fb7ed70663017b8f4dcecc8441", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    主体冲破屏幕= Effect_meta("主体冲破屏幕", False, "7390265515056304681", "74731169", "f36c6922e91c3036495591591aba39d9", [])
    九尾狐      = Effect_meta("九尾狐", False, "7011416501160776228", "1404740", "12afdb69b18ec5127874f04d6f3fdefd", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    人影爆闪    = Effect_meta("人影爆闪", False, "7260741462269104697", "19799492", "f307677e792d2970045b653267fca93b", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
    """
    光环_I      = Effect_meta("光环 I", False, "6999584193848021535", "1378551", "ce2098aa7d557cfc63d896fc63ec2846", [
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    光环_II     = Effect_meta("光环 II", False, "6999882629893853726", "1378552", "adb70b2ea060371bb7d91ec43c031989", [
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    几何拖尾_I  = Effect_meta("几何拖尾 I", False, "6985081270208303653", "1404702", "dbc19689b9dae201897fce9e894ce5fe", [])
    几何拖尾_II = Effect_meta("几何拖尾 II", False, "7008079206181507615", "1404705", "9c57ea460222d55e1bbab56600ca3b71", [])
    击中        = Effect_meta("击中", False, "7008009586581967397", "1404729", "b0a79d87265c9f181f9875a626ad7c66", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    分头行动    = Effect_meta("分头行动", False, "7065570293552517646", "1570064", "50b8be675fac5e23d3bc5d96013c027e", [
                              Effect_param("effects_adjust_size", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    分身        = Effect_meta("分身", False, "7194734735434715704", "9010351", "dca7518f6eb90654d1c2473406db2890", [
                              Effect_param("effects_adjust_distortion", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    动感爱心    = Effect_meta("动感爱心", False, "6998039666024780318", "1238121", "9d3838036dedfd21be7f340273fde034", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    卡通脸      = Effect_meta("卡通脸", False, "7205481536240489019", "10092161", "d01b570f71818e6f6d04bc6c9b1ef766", [])
    变身        = Effect_meta("变身", False, "6998018272557797924", "1238120", "f78c282c0147f997f1c7624bda919cc3", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    可爱女生    = Effect_meta("可爱女生", False, "6971317732948054542", "1182270", "305aaa38fa724b8fceba4a0be1bd49a8", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    可爱猪      = Effect_meta("可爱猪", False, "6971317650219602446", "1182274", "483efc4867b85d9bf7c39a6b1d878b8d", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    吻痕坏笑    = Effect_meta("吻痕坏笑", False, "7197741530751177274", "9392743", "df256252c27055c7434212ca51caf7d0", [
                              Effect_param("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    哈哈哈      = Effect_meta("哈哈哈", False, "6993187958685700638", "1217040", "803508bffb42714235dcdbddb1d30834", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    图腾        = Effect_meta("图腾", False, "6999820560528052743", "1378608", "006d822d0f49a4e20e539d18ed6cda96", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    圣诞小熊    = Effect_meta("圣诞小熊", False, "7175084803874624061", "7126277", "c66c5f67cc2eeb2827a24fd5558cedfe", [
                              Effect_param("effects_adjust_size", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    圣诞帽      = Effect_meta("圣诞帽", False, "7034784053609894430", "1457102", "b3bf8d22530db2a310a8c38abed2fd09", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.30, 0.00 ~ 1.00
    """
    圣诞树      = Effect_meta("圣诞树", False, "7173942106061279781", "6993587", "865c067b3fc9fd7d8fb9d32bfe88cea3", [])
    圣诞胡子    = Effect_meta("圣诞胡子", False, "7034831862597947918", "1457484", "35b6dc4b15d10db2100509cf349f5b5c", [
                              Effect_param("effects_adjust_size", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.770, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.77, 0.00 ~ 1.00
    """
    圣诞辣妹    = Effect_meta("圣诞辣妹", False, "7165705324777705992", "7406471", "7c9b779e2382630c01d33528a013b8fb", [
                              Effect_param("effects_adjust_texture", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    圣诞铃铛    = Effect_meta("圣诞铃铛", False, "7175084694940160568", "7126337", "5b59cf441d783d507c2b4b3a0aabf4e9", [
                              Effect_param("effects_adjust_size", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    声波        = Effect_meta("声波", False, "7008055446397260319", "1404731", "f0e9e247eabb12c558de273a8e51c515", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    多屏圣诞树  = Effect_meta("多屏圣诞树", False, "7175084576950194725", "7126387", "1a70506d54ba37021e8dd157358aa76a", [
                              Effect_param("effects_adjust_size", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    大头        = Effect_meta("大头", False, "6986556887818834462", "1201644", "7518e7eb3e186350b688bf712b960c97", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    大眼睛      = Effect_meta("大眼睛", False, "7044080818544710152", "1489516", "b53f3fda1f03d0d1f703fb71a009d790", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    天使环      = Effect_meta("天使环", False, "7019228748775952933", "1400400", "5782ef42472fd9771f9113d98b6e4e58", [])
    太阳神      = Effect_meta("太阳神", False, "7009186849444860453", "1404735", "9c009ca6bf736eba0dd3152bb863fc6d", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    好吃        = Effect_meta("好吃", False, "7075218981442818596", "1626122", "6a55240ce1f00f078b50fd5e34b5afd3", [
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.200),
                              Effect_param("effects_adjust_horizontal_shift", 0.600, 0.300, 2.600),
                              Effect_param("effects_adjust_size", 0.500, 0.300, 2.000),
                              Effect_param("sticker", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.20
        - effects_adjust_horizontal_shift: 默认0.60, 0.30 ~ 2.60
        - effects_adjust_size: 默认0.50, 0.30 ~ 2.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    妖气        = Effect_meta("妖气", False, "6729410038047183364", "1558942", "8ff658c7bcf3814f91693f906d5eba8b", [
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    委屈丑丑脸  = Effect_meta("委屈丑丑脸", False, "7130874026733343268", "4192363", "596971eaa17dbe64f62f52fc75c9998a", [])
    害羞        = Effect_meta("害羞", False, "6979931248890221069", "1187976", "6904d753832ee54a39f46fb23e0c47fc", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("sticker", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
    """
    小恶魔      = Effect_meta("小恶魔", False, "6995534946311868958", "1225626", "7dba67f137a50da13db71188fc6df71f", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
    """
    小鹿角      = Effect_meta("小鹿角", False, "7035938555683672612", "1459882", "a77b46457ff3ea5a5c75c0d127e9cdd2", [])
    尴尬住了    = Effect_meta("尴尬住了", False, "7156141357008949790", "5481035", "cc08bdab9e913aa015d61631abf8fa7d", [])
    局部扭曲    = Effect_meta("局部扭曲", False, "7038521452668129822", "1470210", "da8f3f99ca659d2710b2f9dcecf5fe4c", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    局部马赛克  = Effect_meta("局部马赛克", False, "7034092576726585869", "1454112", "a2669cddba1a547ee9330215fe32e86b", [
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    巴哥犬      = Effect_meta("巴哥犬", False, "6971317662567633421", "1182273", "6764c992938b5c0e62dfc6e46255bde7", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    帅气男生    = Effect_meta("帅气男生", False, "6971317748542476814", "1182269", "71d88fb7f6ae9e19df3f8b491b7355bf", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    幻影_I      = Effect_meta("幻影 I", False, "7212904257043829307", "11357751", "6699feabadc4f59732b8087620fc95a6", [
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    幽灵        = Effect_meta("幽灵", False, "7000630410275197470", "1378554", "6cc1df4c330fce3c92fefc89fbe4b7f6", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    弥散流光    = Effect_meta("弥散流光", False, "7034508334157795876", "1455764", "eabd69cd578279cf0dc892e088f60da6", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.00, 0.00 ~ 1.00
    """
    彩色负片    = Effect_meta("彩色负片", False, "7035876641083494926", "1459050", "2cd6462bd0bde3023d5f7069cd549b17", [
                              Effect_param("effects_adjust_size", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    彩色重影    = Effect_meta("彩色重影", False, "6995746173772370469", "1235614", "99b7fa2ef6210832f1d6dccfce4ed759", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    微笑摇摆头  = Effect_meta("微笑摇摆头", False, "7166825483902915109", "6253239", "ff4053845ced3ff3b9fbe9d1429a908b", [
                              Effect_param("effects_adjust_size", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    心动        = Effect_meta("心动", False, "6986186073814602277", "1204190", "bab33144cacb0cdade5a3d1f18d9c6e7", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.75, 0.00 ~ 1.00
    """
    心动信号    = Effect_meta("心动信号", False, "7040012457842053662", "1478394", "a4758810ef78bfca76c45486faeac99d", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    心心眼      = Effect_meta("心心眼", False, "7196943722523660858", "9126233", "aebda718fd41b71cbef713df0b12ac0f", [
                              Effect_param("effects_adjust_distortion", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
    """
    恶灵骑士    = Effect_meta("恶灵骑士", False, "7000301210993431053", "1378618", "c0f232fc4435c4bf8a4861efa6bcf671", [
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    恶魔印记    = Effect_meta("恶魔印记", False, "7000647554337608222", "1378619", "abab6563284c7ef292d1acaaf5a1be3e", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    恶魔尾巴    = Effect_meta("恶魔尾巴", False, "7001021232371995149", "1404725", "7ab5f92c75beb4747dc81731b447f53c", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认1.00, 0.00 ~ 1.00
    """
    恶魔角      = Effect_meta("恶魔角", False, "7019228817549955597", "1400399", "e3331ccd99a663f0561f82ac87441dcf", [])
    惨          = Effect_meta("惨", False, "6992836065245532680", "1225625", "f5f8238bef302a2a27cae95c0d2304f1", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
    """
    意识流      = Effect_meta("意识流", False, "7000629338529862151", "1378555", "17dcd65459f769802c3d02fa00af0a48", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    憔悴        = Effect_meta("憔悴", False, "6986160256103485989", "1197947", "709a178794856095bfcc215cabc3f91c", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.75, 0.00 ~ 1.00
    """
    懵          = Effect_meta("懵", False, "6980272649066779143", "1187977", "32325e03b4b27a426af4f3c3916cd718", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("sticker", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
    """
    我不听      = Effect_meta("我不听", False, "7001058741571293709", "1353102", "a56ac41521ef7b1e1ad7e09ec2253082", [
                              Effect_param("effects_adjust_number", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    我服了      = Effect_meta("我服了", False, "7029509874862002724", "1436336", "6ec666bfc6a45aa53f82f794d75d9976", [
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
    """
    打击        = Effect_meta("打击", False, "6971302911317905956", "1169502", "b310c3ede33e6e0819859dbc67ffab7e", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.55, 0.00 ~ 1.00
    """
    打脸        = Effect_meta("打脸", False, "6992915114051506725", "1217039", "ade99f5a3c5dc73639e55dbf4157b0eb", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    扫描_II     = Effect_meta("扫描 II", False, "7000630959565443614", "1378580", "c6c224fb2fec72f0a0432ccad29546aa", [
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    拼贴抽帧    = Effect_meta("拼贴抽帧", False, "7142777693707178533", "4574525", "602c047f7cafe02427da4b327fd260cf", [
                              Effect_param("effects_adjust_vertical_chromatic", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.661, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_chromatic: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    拼贴风暴    = Effect_meta("拼贴风暴", False, "7037019101402763806", "1464400", "1a39707de66987a9048c2e495b5a1c96", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.75, 0.00 ~ 1.00
    """
    拽酷红眼    = Effect_meta("拽酷红眼", False, "6979861988935471623", "1185226", "3528fdf176336d1ae503e85611d96347", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
    """
    掉小珍珠啦  = Effect_meta("掉小珍珠啦", False, "7132336135748981255", "4080159", "006d2be0ee7d9109b202e609d29b37e3", [])
    故障描边_I  = Effect_meta("故障描边 I", False, "6998080413587477005", "1238132", "226bca50364904c231246c72b0a9e5c1", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    敲打        = Effect_meta("敲打", False, "6986918523704447501", "1197949", "67737d95f8256e6915b26c3efd41f305", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    新年星黛露  = Effect_meta("新年星黛露", False, "7182406780733887033", "7823781", "6e4e73454d92da43cd9e90cf7c350c7d", [
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
    """
    无信号      = Effect_meta("无信号", False, "7039965830192304671", "1478054", "c6c413df67a97d81b29355a0e1e89f16", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    星光放射    = Effect_meta("星光放射", False, "6999904379822150158", "1378610", "aa85bd31e3f47e7bd01383b6aacc9508", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    星星拖尾    = Effect_meta("星星拖尾", False, "7007679689388986888", "1404703", "7dabcaa49244e8faeaf61bfa184d53fb", [])
    未来眼镜    = Effect_meta("未来眼镜", False, "6989160247034122789", "1238126", "66983702ac8ca5f68aa9ec32c92c4b3b", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    机械几何    = Effect_meta("机械几何", False, "6997682380454498824", "1238116", "2b469e181b8e5be26a0e09678a9974b0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    机械姬_I    = Effect_meta("机械姬 I", False, "6978809529215488548", "1238098", "11d60d8c8de82453c697bed883e64671", [])
    机械姬_II   = Effect_meta("机械姬 II", False, "6997969810822795813", "1238099", "601bc1f8fd6dfcb9226fa7e54aba9f14", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    机灵怪      = Effect_meta("机灵怪", False, "7158373218724614664", "5510681", "6fa4f54d22b420c8c0a3e59246d1c8b7", [])
    欧美女性    = Effect_meta("欧美女性", False, "6971317800098861576", "1182266", "6d9b6990df1d66bad249c5defd435576", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    欧美男性    = Effect_meta("欧美男性", False, "6971317784085008909", "1182267", "b09c7a6c2134a95aeac139f06217cdde", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    气泡_I      = Effect_meta("气泡 I", False, "6999560743653741087", "1378604", "53133594bcb0ca9cf9cb48b80aa8eec1", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    气泡_II     = Effect_meta("气泡 II", False, "6999560859986956813", "1378603", "1b75e11acadf9069723dc387751d68c5", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    气波        = Effect_meta("气波", False, "7008459080452805133", "1404693", "d49684beffa531728f6d0b2f5823a465", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    沉沦        = Effect_meta("沉沦", False, "7000286535568331294", "1378579", "7f1cef9ddfd657188f2ae2f069c9433b", [
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    流光描边    = Effect_meta("流光描边", False, "7156203771352060424", "6699941", "43de1121773eea81624460ed929b17e8", [
                              Effect_param("effects_adjust_intensity", 0.850, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    流口水      = Effect_meta("流口水", False, "7072912940101276196", "1610044", "50dec319b04a96990ed59c7a237ed700", [
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.500, 0.400, 0.700),
                              Effect_param("effects_adjust_size", 0.800, 0.500, 1.200)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.40 ~ 0.70
        - effects_adjust_size: 默认0.80, 0.50 ~ 1.20
    """
    漩涡        = Effect_meta("漩涡", False, "7007639691797205511", "1404726", "c027fc134ee686578a887120774ae49b", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    潮流入侵    = Effect_meta("潮流入侵", False, "7039588403897176583", "1475552", "1cf49471f39f839690bdb9516e99c37c", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    潮酷女孩    = Effect_meta("潮酷女孩", False, "6973998028587799076", "1182282", "43567fd71493d00bc90873169a742c7b", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    潮酷男孩    = Effect_meta("潮酷男孩", False, "6971317770835202574", "1182268", "8db29277f098685e305a341ae6256482", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    激光几何    = Effect_meta("激光几何", False, "6998130105188880909", "1238146", "3b57818e4d021368a6a71792ff5efffd", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    火焰拖尾    = Effect_meta("火焰拖尾", False, "7008060347789611551", "1404704", "f5e51b968426e15e4e185285a4e8558f", [])
    火焰环绕    = Effect_meta("火焰环绕", False, "7009186695157387784", "1404737", "0336f00d05b706cf8ab9742af8ee16c7", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    火焰翅膀_I  = Effect_meta("火焰翅膀 I", False, "7009186539762618910", "1404738", "bab3b65e0ca81daf7fbef82971d57527", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    火焰翅膀_II = Effect_meta("火焰翅膀 II", False, "7007998245511107108", "1404728", "93fa02d91dd5f7fd2c41314358ba462d", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    灵机一动    = Effect_meta("灵机一动", False, "6982806720867209765", "1187978", "9a0be515180211c4c30a1757d3622ca0", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.600, 0.000, 1.000),
                              Effect_param("sticker", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.60, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    灵魂出走    = Effect_meta("灵魂出走", False, "6994263736991093278", "1220234", "84ab61fed5e4137e73112badf715f370", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("sticker", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
    """
    爱心光波    = Effect_meta("爱心光波", False, "7058944699737838116", "1552114", "2198438e43c9ff1147958bf750b61b90", [
                              Effect_param("effects_adjust_texture", 0.204, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.753, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    爱心焰火    = Effect_meta("爱心焰火", False, "6999550440639566350", "1378601", "2f8b37a399b2b45ca57717a6244c3c9f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    猩猩脸      = Effect_meta("猩猩脸", False, "7112786295771894285", "3186064", "3afa515823ec425b359bf9102a7cfa28", [])
    猫耳女孩    = Effect_meta("猫耳女孩", False, "6971317673699316261", "1182272", "486df1ec5de1ca0a69210b844b912534", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    电光描边    = Effect_meta("电光描边", False, "7171723380003967496", "6738041", "1a5266ab56ea0645c20f0160aee7743e", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    电光放射    = Effect_meta("电光放射", False, "7011414375130993188", "1404739", "092db1dc71adf758d4ab5b19b5b43873", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    电击        = Effect_meta("电击", False, "6999560974638256671", "1378602", "b1659d113dda06df2115cd948ed09e23", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    电子屏故障  = Effect_meta("电子屏故障", False, "6997976386413531661", "1238119", "05d9292d4d2ef2ea3b84854f4771ff25", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    真的会谢    = Effect_meta("真的会谢", False, "7179493200904589881", "7600931", "bdfc580a5e4155e95c3568dcea50d341", [])
    真香        = Effect_meta("真香", False, "6995535089975169549", "1225627", "81a9d2b55a363059acb95c637e49d65d", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
    """
    破碎的心    = Effect_meta("破碎的心", False, "7008077860397126158", "1404734", "7ddd6f7b9c206935ac79bfc814467ae4", [
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    神明少女    = Effect_meta("神明少女", False, "6906817277316829703", "1169466", "ec3e07e2c9d85b1f3fd258d26fb256c4", [
                              Effect_param("effects_adjust_soft", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_soft: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    科技氛围_I  = Effect_meta("科技氛围 I", False, "6989160173826740767", "1238115", "bdfd8e3165875ca7084b62d7e6204079", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    科技氛围_III= Effect_meta("科技氛围 III", False, "6983927792010269214", "1238118", "8e1024fd3f6bd41f09d16cf27de0f210", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    秘密        = Effect_meta("秘密", False, "7023684632591733284", "1418782", "72f525012ca8744325138a89981b3e84", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    箭头环绕    = Effect_meta("箭头环绕", False, "6999943971162034702", "1378553", "c4543904bdf336051dee6e64c8b5ebdd", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    粉色便便    = Effect_meta("粉色便便", False, "6971317685216875044", "1182271", "0c843a5ba39df7e037f4995040f79263", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    背景拖影    = Effect_meta("背景拖影", False, "7012512877038801415", "1379270", "e6c9f05435c8a8912b1321bfa9f39a4a", [
                              Effect_param("effects_adjust_horizontal_shift", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_shift: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.85, 0.00 ~ 1.00
    """
    背景氛围II  = Effect_meta("背景氛围II", False, "7007713075486790152", "1404727", "f69d913fb2414b485d7d03770049a5fa", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    脸红        = Effect_meta("脸红", False, "7025808257306333732", "1424210", "9946c014663314c93786a0a8fc27b347", [
                              Effect_param("sticker", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.802, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    脸绿了      = Effect_meta("脸绿了", False, "7023661644853023263", "1418056", "a4af7d2a30dac7d4be34f96c8d27f556", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.802, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
    """
    脸部故障    = Effect_meta("脸部故障", False, "7260774105073324602", "19351944", "b00871e8d7e141731a2fe3ca29bb857a", [
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    舞者        = Effect_meta("舞者", False, "6978809631678140935", "1238134", "80d431c5d76932b3f3fb8418267afdb5", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    舞者_II     = Effect_meta("舞者 II", False, "7000629698401145352", "1378611", "de4d77dc2f920e92503d9553c0cf1a21", [
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    萤火        = Effect_meta("萤火", False, "6979415063106949639", "1378556", "000701418e2acde7230cfdcc680ef895", [
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    虚拟人生_I  = Effect_meta("虚拟人生 I", False, "6998017546452472351", "1238100", "54fd9f289f28e1a2f060f4e569c31359", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    虚拟人生_II = Effect_meta("虚拟人生 II", False, "6998017726589440519", "1238101", "2bc7ecc4b79a372c9fed9a86b850d8a5", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    衰          = Effect_meta("衰", False, "6995855600764588557", "1225628", "80bb667cb6e39b17554321df89c41a86", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
    """
    视线遮挡    = Effect_meta("视线遮挡", False, "7034507846305714696", "1455754", "9d6829ecbc85a6653ca44ccd18c9243f", [
                              Effect_param("effects_adjust_speed", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    赛博朋克_I  = Effect_meta("赛博朋克 I", False, "6975112087659876895", "1238114", "3f5f8d770decd3fe853778e00f3ab589", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    赛博朋克_II = Effect_meta("赛博朋克 II", False, "6997261680803582494", "1238113", "0bbcda72ffc36a7aa6dc7d5ec7cdc0b6", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    赛博眼镜    = Effect_meta("赛博眼镜", False, "7055586958050857503", "1536126", "ce551db43d4cd0e9abf3e69a35513113", [])
    轻金属      = Effect_meta("轻金属", False, "7036946127320519182", "1463702", "6f5edc9d13d681afe8ee4f3224014a1e", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.75, 0.00 ~ 1.00
    """
    运动轨迹    = Effect_meta("运动轨迹", False, "7389547512987652658", "74470467", "91ac684d7b70b28e9fd1f3c1f99c97e9", [
                              Effect_param("effects_adjust_number", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    迷茫        = Effect_meta("迷茫", False, "6979931594408595975", "1185225", "9e8012a17d162ab2263190ffd4152b72", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    闪影        = Effect_meta("闪影", False, "7090458377901314568", "1825212", "864dcb150b85814ca7615946c7265941", [
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    闪烁        = Effect_meta("闪烁", False, "7008060861528936991", "1404733", "b8648c0ede65749dcc4af04b7d5fa54c", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    闪电炸裂    = Effect_meta("闪电炸裂", False, "6999539022812942884", "1378606", "be8011441a484bf6661aa33604cd06bd", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    阳光        = Effect_meta("阳光", False, "6986176759725036039", "1197948", "7ea97e6b6156a1066459a400f0c26692", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.75, 0.00 ~ 1.00
    """
    阴云密布    = Effect_meta("阴云密布", False, "7025527915320185375", "1427592", "25dc89f2e7cbe9ffb52d1da8f2cade5c", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    阴暗面      = Effect_meta("阴暗面", False, "7000679723906896397", "1378620", "f1efe71ae45c60bc94d1fcb168b8bf4d", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    难吃        = Effect_meta("难吃", False, "7075326356585714207", "1627088", "22f5c7f78d72ed2767d8673414519e4b", [
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.200),
                              Effect_param("effects_adjust_horizontal_shift", 0.550, 0.300, 2.600),
                              Effect_param("effects_adjust_size", 0.500, 0.300, 2.000),
                              Effect_param("sticker", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.20
        - effects_adjust_horizontal_shift: 默认0.55, 0.30 ~ 2.60
        - effects_adjust_size: 默认0.50, 0.30 ~ 2.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    难过        = Effect_meta("难过", False, "6979931396827517477", "1187975", "0d1f3c1ea1287cd2de9193f5a6c55d20", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("sticker", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
    """
    雪花眼泪    = Effect_meta("雪花眼泪", False, "7174694873897898553", "7078531", "b078f5583b67f9bfa95e30bf612e3482", [
                              Effect_param("effects_adjust_intensity", 0.850, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_sharpen", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.25, 0.00 ~ 1.00
    """
    霓虹特技    = Effect_meta("霓虹特技", False, "7389546043534217778", "74469969", "a30c2949ccfc35417421caf68261ae0b", [
                              Effect_param("effects_adjust_size", 0.510, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.51, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    音符拖尾    = Effect_meta("音符拖尾", False, "7008458769675850248", "1404706", "7c1a10956911f225d514aab1ecfb7aeb", [])
    音符拖尾_II = Effect_meta("音符拖尾 II", False, "7002176395312894494", "1238188", "c768fa0ad974298284a8adb66678e93a", [])
    飓风        = Effect_meta("飓风", False, "7008458952451035678", "1404694", "a0bf72f591c6dbba8a211894f618976f", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    飞翔的帽子  = Effect_meta("飞翔的帽子", False, "6999892125697446414", "1404708", "ec71eec4c8788ed43133f0a5a775e0c6", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    鬼火        = Effect_meta("鬼火", False, "7008470453366821389", "1404696", "6dcf3bafc5efbf4f3509dae601f57f54", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    黑人女孩    = Effect_meta("黑人女孩", False, "6971317836648026661", "1182265", "bde6e304a5de9614c0f44644fd3d15be", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    黑人男生    = Effect_meta("黑人男生", False, "6971317847318336031", "1182264", "a6e9afde1f86efbb91c49ecd9d6a8fdc", [
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    _3D兔兔     = Effect_meta("3D兔兔", True, "7098954198204551716", "1924176", "78c9a5106ea815c821911a10f7631163", [
                              Effect_param("sticker", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    Love_u      = Effect_meta("Love u", True, "7058892012358996510", "1551894", "2aa9298939a522ca05e5219ab6e91cf6", [
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
    """
    X瞬移       = Effect_meta("X瞬移", True, "7265629618424517157", "20387617", "366528fe2ee5c5c851a694073cf4b855", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
    """
    分身_III    = Effect_meta("分身 III", True, "7281245666309837349", "23497249", "5b218df611d57e62c26029c0df884b13", [
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 0.600),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.30, 0.00 ~ 0.60
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    分身ll      = Effect_meta("分身ll", True, "7207269616299545149", "10287363", "a42da906cd114315f798ba59b1692264", [
                              Effect_param("effects_adjust_vertical_shift", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.620, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.62, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.30, 0.00 ~ 1.00
    """
    发光分身    = Effect_meta("发光分身", True, "7233250530292666939", "13661053", "dbff6732319cf9488da4816c188d9f1a", [
                              Effect_param("effects_adjust_color", 0.840, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.102, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.84, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
    """
    变老美颜    = Effect_meta("变老-美颜", True, "7226689898118386237", "12825757", "bd4037e779bb8ecd6ac12258853974b2", [])
    可爱龙龙    = Effect_meta("可爱龙龙", True, "7327508217590714931", "41751981", "9ac3a781a5aa5b33ddc73be905a2b270", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_texture", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    嘻哈眼镜    = Effect_meta("嘻哈眼镜", True, "6998017895024300557", "1238128", "3a23ea8d16fe9ec18850783595877e4b", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.60, 0.00 ~ 1.00
    """
    天使        = Effect_meta("天使", True, "6997362211219837448", "1238102", "8ef8376678b551b005ea62bfe99b6d3a", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    天使翅膀    = Effect_meta("天使翅膀", True, "6999514637767021070", "1378600", "f7acdf6cab043dbe7401ac89e572f6ff", [
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    奇行种      = Effect_meta("奇行种", True, "7168749461206733342", "6432361", "ca795d0b1827bcd27231c7c5a10825e3", [])
    局部模糊    = Effect_meta("局部模糊", True, "7036282000780562981", "1461580", "d61e04351e9ead6669cb6db1f4bdce05", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_noise", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
    """
    幻彩流光    = Effect_meta("幻彩流光", True, "7303422113812058633", "30319544", "5926b9713b3de1fe23a6b1790ba5d204", [
                              Effect_param("effects_adjust_texture", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.950, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.95, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.20, 0.00 ~ 1.00
    """
    幻影平移    = Effect_meta("幻影平移", True, "7259667629357404730", "19114588", "4f4946b896cb4675e8514fa8d5af517a", [
                              Effect_param("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
    """
    彩虹流体    = Effect_meta("彩虹流体", True, "7273753115604554295", "21883974", "2725088e1378997bea428c8b04e2b15f", [
                              Effect_param("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    彩虹边缘    = Effect_meta("彩虹边缘", True, "7306769922535723558", "31771661", "e59040f43c25146de23341ac4b47a8bf", [
                              Effect_param("effects_adjust_intensity", 0.550, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.15, 0.00 ~ 1.00
    """
    影分身      = Effect_meta("影分身", True, "7306822259186864691", "31622417", "8088e845f5e6b8aecd6a9245cf033cfb", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    恶魔之翼    = Effect_meta("恶魔之翼", True, "7008049313305596446", "1404730", "99cdde82bb5587966f1a2bac10d024f2", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    情绪定格    = Effect_meta("情绪定格", True, "7298250619167445531", "28662656", "b60fd80757a580b75be83ea1b8905ef3", [
                              Effect_param("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.10, 0.00 ~ 1.00
    """
    我太可爱了  = Effect_meta("我太可爱了", True, "7132773677086544398", "4104909", "76739264135fb0471d1ac7d9fa8b2027", [])
    我爱了      = Effect_meta("我爱了", True, "7182098630935843385", "9267743", "9ea5207040ca8a6c673eee1c8f4213e9", [])
    我麻了      = Effect_meta("我麻了", True, "7030722591358718494", "1441766", "b3078ea7691c02789dec4360d7ebd5a5", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    手写描边    = Effect_meta("手写描边", True, "7108559446065811998", "2869818", "59694d712050ddb032105f620b50ffe6", [
                              Effect_param("effects_adjust_color", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.210, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.21, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    捕梦        = Effect_meta("捕梦", True, "7038866261677183524", "1471454", "24df2e977ac4752adaeb8f4495e98aeb", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    旋转分身    = Effect_meta("旋转分身", True, "7259667753731101244", "19114658", "f2a47eb17a20c6272e939350cf2268d3", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.300, 0.000, 0.750),
                              Effect_param("effects_adjust_blur", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.30, 0.00 ~ 0.75
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
    """
    无限穿越    = Effect_meta("无限穿越", True, "7293870099738399269", "27074734", "f6bed6028a99ff60118167854f1f6ed1", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.00, 0.00 ~ 1.00
    """
    有事吗      = Effect_meta("有事吗？", True, "7322382230930592266", "39451195", "2cab81a0a4cad0393890f3eaad56a191", [
                              Effect_param("effects_adjust_texture", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.60, 0.00 ~ 1.00
    """
    机械环绕_I  = Effect_meta("机械环绕 I", True, "6986465789259813406", "1238184", "bff38e9886478c86635d990f78ca68cd", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    机械环绕_II = Effect_meta("机械环绕 II", True, "6997731822104744478", "1238185", "66eb2b1b98e4ada7cacba9c39d37be74", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    梦境        = Effect_meta("梦境", True, "7039963252612141598", "1478040", "9f78e88b23ebbef1edc3439c2fc34c52", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    气炸了      = Effect_meta("气炸了", True, "7026548629498237454", "1426832", "979ebc680f1241a86545102632c79dff", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    波点分身    = Effect_meta("波点分身", True, "7086779590768595469", "1826180", "47f63e0ad4dd5f9c3d2045075b6795d4", [
                              Effect_param("effects_adjust_color", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    流体故障    = Effect_meta("流体故障", True, "7287114240089920061", "24949284", "f6cfc884ea840da552785ed2c1a3309b", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
    """
    漩涡溶解    = Effect_meta("漩涡溶解", True, "7201020527501120057", "9583557", "3281d02205f102f70c4b07021be5bc71", [
                              Effect_param("effects_adjust_distortion", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.450, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.450, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.45, 0.00 ~ 1.00
    """
    火焰图腾    = Effect_meta("火焰图腾", True, "7009186785662079524", "1404736", "35e9cbe081d47066558a717ce3a774d8", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    点赞        = Effect_meta("点赞", True, "7072663671096218143", "1609620", "9f934cf082ec4d56a6f86e6e1aa2c8f6", [
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
    """
    热力光谱_I  = Effect_meta("热力光谱 I", True, "7033284501253919268", "1451182", "b578d3e33d8c650dc445c19875f9613f", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.801, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    热力光谱_II = Effect_meta("热力光谱 II", True, "7033338062113346056", "1451606", "b711586fdabf06e7975e4bc2f2d906e6", [
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.801, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    焰火        = Effect_meta("焰火", True, "7008459945590919716", "1404695", "3dc040bd8a6d3853428cc18030e7872a", [
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    熬夜冠军    = Effect_meta("熬夜冠军", True, "7330555999801053746", "43238686", "071e4eb6e85a9778b415bcb9303fd867", [
                              Effect_param("effects_adjust_texture", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.80, 0.00 ~ 1.00
    """
    爱心        = Effect_meta("爱心", True, "7068191600148484638", "1587990", "cda6bba22c1e6038233c0aaf3ec7c0ee", [
                              Effect_param("effects_adjust_number", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    爱心发射    = Effect_meta("爱心发射", True, "7057403623004705294", "1551876", "665453673ccb652b012a46f63d32109d", [
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.350, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.35, 0.00 ~ 1.00
    """
    爱心泡泡    = Effect_meta("爱心泡泡", True, "7055592805174874632", "1551930", "62cf1078f3a0e623c349cb4200f3de26", [
                              Effect_param("effects_adjust_size", 0.350, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    爱心眼      = Effect_meta("爱心眼", True, "7104647986176594463", "2491250", "aeee56c74c823b2afda571c023d0f992", [
                              Effect_param("effects_adjust_color", 0.150, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.050, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.05, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    爱心美瞳    = Effect_meta("爱心美瞳", True, "7194734371872444965", "8950197", "23b70724f639f5020f4a4f6a53011868", [
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    狱火        = Effect_meta("狱火", True, "7007676026406834725", "1404692", "29903a65ede13673b23ac1eedc118b5d", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    生气        = Effect_meta("生气", True, "7068227476035473928", "1588764", "5c652a8c8a664b41ec7c59fa569ee3e8", [
                              Effect_param("effects_adjust_number", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    电光描边_II = Effect_meta("电光描边 II", True, "7265989852099777061", "20444547", "0177b9dd16527e7c082ad4ddfe59f0bc", [
                              Effect_param("effects_adjust_luminance", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.650, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.110, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.11, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
    """
    电光灼烧    = Effect_meta("电光灼烧", True, "7259649795571061305", "19106834", "3e5d0b31ae925f24539d89b017879815", [
                              Effect_param("effects_adjust_rotate", 0.730, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_rotate: 默认0.73, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    电光眼      = Effect_meta("电光眼", True, "7106778883143242271", "2724384", "12aed71e7e62dafe99b6ff5ef264a36d", [
                              Effect_param("effects_adjust_color", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    电光耳机    = Effect_meta("电光耳机", True, "6998018067154342408", "1238127", "19a87efa0bebe59cdf36eda727a66664", [
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    眼神光      = Effect_meta("眼神光", True, "7091874262364983815", "1793042", "665fec8aacac1d793e7917a0a0ec3ab3", [
                              Effect_param("effects_adjust_intensity", 0.750, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.850, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    瞬移        = Effect_meta("瞬移", True, "7322735107280736805", "39618119", "29e526f7936cb5e985f77da6c51498ef", [
                              Effect_param("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
    """
    碎片分身    = Effect_meta("碎片分身", True, "7207691092655870523", "10339835", "86532426a7e3c08c229dd518c51a893c", [
                              Effect_param("effects_adjust_range", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.950, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.95, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.00, 0.00 ~ 1.00
    """
    碎闪边缘    = Effect_meta("碎闪边缘", True, "7306471467397419547", "31771693", "7c1311ff7b01577587a28252b3cd5d46", [
                              Effect_param("effects_adjust_range", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.200, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.15, 0.00 ~ 1.00
    """
    科技氛围_II = Effect_meta("科技氛围 II", True, "6982572496356643359", "1238117", "d4b1ba4f4bb11a26860cd7f493853661", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    移形回位    = Effect_meta("移形回位", True, "7270801008094089784", "21811668", "4d2d96869fab0fa65766a52360c9fcef", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.300, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    移形幻影_I  = Effect_meta("移形幻影 I", True, "7201010922742092325", "9583559", "c89c34b83924f3fb5c88f2ece2e095b8", [
                              Effect_param("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    移形幻影_II = Effect_meta("移形幻影 II", True, "7194734891353772603", "9010339", "c4ce763e7fcd977c98e4b4a8be0b85a1", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    空气流体    = Effect_meta("空气流体", True, "7283548311217246781", "24123133", "9882eb0caf97221ac6bd4161ead3a263", [
                              Effect_param("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.400, 0.000, 1.000),
                              Effect_param("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.720, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.660, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.72, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.66, 0.00 ~ 1.00
    """
    笑哭        = Effect_meta("笑哭", True, "7072173200418804231", "1606772", "9b86bc9942f7848d7ee7e7e74a077a4b", [
                              Effect_param("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
    """
    粒子弥散    = Effect_meta("粒子弥散", True, "7283038170826936892", "23970537", "7a72cd5b5950e933ca7f6df425537c21", [
                              Effect_param("effects_adjust_horizontal_shift", 0.660, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_shift: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    美味召唤    = Effect_meta("美味召唤", True, "7073398095186235935", "1612792", "1e09bf5fc9f3bc36e9fdb479c832365b", [
                              Effect_param("effects_adjust_vertical_shift", 0.600, 0.000, 1.200),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("sticker", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.60, 0.00 ~ 1.20
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    蝴蝶翅膀    = Effect_meta("蝴蝶翅膀", True, "6999567409677865486", "1378607", "69eaf245462b3777f94dfc5aabe18791", [
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    轮廓扫描    = Effect_meta("轮廓扫描", True, "7260773990178755129", "19351962", "7abf09f3d054331c74f328ed951db5cb", [
                              Effect_param("effects_adjust_color", 0.600, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_soft", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    迷幻分身    = Effect_meta("迷幻分身", True, "7280421849974968889", "23303207", "e2bd87ba0c294b5340a8b74cf7c3f954", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_number", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_blur", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_rotate", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.85, 0.00 ~ 1.00
    """
    金币掉落    = Effect_meta("金币掉落", True, "7021362776404660743", "1543838", "06be5783fa794fc209023a283a47a7d3", [
                              Effect_param("effects_adjust_speed", 0.333, 0.000, 1.000),
                              Effect_param("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    镭射眼_I    = Effect_meta("镭射眼 I", True, "7106778448344912421", "2724386", "ea9d0666a569334a0c6b27c14ade2674", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.900, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    镭射眼_II   = Effect_meta("镭射眼 II", True, "7106778621326397983", "2724385", "3891948240e1594b7ea8025222341a9d", [
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 0.620, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.62, 0.00 ~ 1.00
    """
    闪电        = Effect_meta("闪电", True, "7088198349324554766", "1711412", "9c97ab760617a5c3bc75491b3ad8406b", [
                              Effect_param("effects_adjust_color", 0.000, 0.000, 1.000),
                              Effect_param("effects_adjust_speed", 0.100, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    闪电环绕    = Effect_meta("闪电环绕", True, "6998102186068546078", "1238186", "d2459fb754b3d9dbb469d29f6af77423", [
                              Effect_param("effects_adjust_speed", 0.330, 0.000, 1.000),
                              Effect_param("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_size", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    闪电眼      = Effect_meta("闪电眼", True, "7106763566262260231", "2722184", "6b6b4e9eb53581fea08118f62d55c1a9", [
                              Effect_param("effects_adjust_color", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_luminance", 0.250, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 1.000, 0.000, 1.000),
                              Effect_param("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              Effect_param("effects_adjust_range", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.85, 0.00 ~ 1.00
    """
    霓虹爱心    = Effect_meta("霓虹爱心", True, "7194734553288675895", "8981839", "9d6f972481069644431af54815c8a75b", [
                              Effect_param("effects_adjust_speed", 0.500, 0.000, 1.000),
                              Effect_param("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
