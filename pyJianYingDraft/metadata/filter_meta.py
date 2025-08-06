"""滤镜效果元数据"""

from .effect_meta import EffectEnum
from .effect_meta import EffectMeta, EffectParam

class FilterType(EffectEnum):
    """滤镜效果类型"""

    # 免费特效
    _1980                = EffectMeta("1980", False, "7127828208690433311", "7127828208690433311", "d3595847ee8348c69c6037b8003a76e9", [])
    ABG                  = EffectMeta("ABG", False, "7127679308897832206", "7127679308897832206", "d07b36b0b8e1893ce49df327ba926804", [])
    Ditto                = EffectMeta("Ditto", False, "7195816046077496635", "7195816046077496635", "09d18408ca0dee53716c3a4f41dd35e1", [])
    KE1                  = EffectMeta("KE1", False, "7127819154018536741", "7127819154018536741", "5ece7eff894e25a356b9111e78478c56", [])
    KV5D                 = EffectMeta("KV5D", False, "7127578859217620254", "7127578859217620254", "57940599e2c8d85a7f73824c7360bfca", [])
    Lofi_II              = EffectMeta("Lofi II", False, "7232216810031025468", "7232216810031025468", "7d5f9e106b93bf758725da54daa1843f", [])
    VHS_III              = EffectMeta("VHS III", False, "7127669764905782542", "7127669764905782542", "c8d7adad4773fccc2128d8eafa569572", [])
    三洋VPC              = EffectMeta("三洋VPC", False, "7127669338089311495", "7127669338089311495", "73c77a4b9c5085af6175a523d24bc7c6", [])
    书意                 = EffectMeta("书意", False, "7368493100127292723", "7368493100127292723", "3e20d8ccc31ca6a495b3f8e2ff116744", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    亢奋                 = EffectMeta("亢奋", False, "7166472327801097476", "7166472327801097476", "93c16f48d5d45cb663270a82a06f72b8", [])
    亮夏                 = EffectMeta("亮夏", False, "7505804389395877120", "7505804389395877120", "839755ea45f49179790ae2d9a00810b3", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    亮肤                 = EffectMeta("亮肤", False, "7127655008715230495", "7127655008715230495", "2aaa463c5deee34e73384d549edc7c15", [])
    仲夏绿光             = EffectMeta("仲夏绿光", False, "7127675970252754189", "7127675970252754189", "970f4b2c797e2890787f7420d8c0613b", [])
    似锦                 = EffectMeta("似锦", False, "7188014191834418493", "7188014191834418493", "869cb94d6bbec5c6b771092ec1ef8cfe", [])
    低保真               = EffectMeta("低保真", False, "7304170509661506843", "7304170509661506843", "db39172ffff69e973886c2e8598dbc75", [])
    侘寂灰               = EffectMeta("侘寂灰", False, "7127609569416711455", "7127609569416711455", "17547e013b45f87dc7e4e1f7059d7e62", [])
    元气新年             = EffectMeta("元气新年", False, "7457859598221987110", "7457859598221987110", "659b4fa52fb892852dbab15dfc4717e2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    克洛伊               = EffectMeta("克洛伊", False, "7366640728493002018", "7366640728493002018", "2740205bf2c6b79d64d84548a6ed5e21", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    入夏                 = EffectMeta("入夏", False, "7101096733958065421", "7101096733958065421", "b5aa7c782bad8122e80cfd9f7c4dc72c", [])
    冬日烧烤             = EffectMeta("冬日烧烤", False, "7449704838763466035", "7449704838763466035", "bcd542f8af28c382cdacb39b588c4bbe", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    冬漫                 = EffectMeta("冬漫", False, "7302324323270872346", "7302324323270872346", "a883a2e3b66f3e9c7bcaa1672e51ee9a", [])
    冬离                 = EffectMeta("冬离", False, "7300786822068571418", "7300786822068571418", "b5389102a96557d6c03047e814756936", [])
    冰火                 = EffectMeta("冰火", False, "7303812389177265447", "7303812389177265447", "61065880d8580b8b1a206de0b0773571", [])
    冰肌                 = EffectMeta("冰肌", False, "7199089344756370743", "7199089344756370743", "18c6b91685b82ef1cd3d7b7261f997ea", [])
    冷气机               = EffectMeta("冷气机", False, "7263359186883366155", "7263359186883366155", "740c1bfa9cb365344bd8a51bf7ef037b", [])
    冷白                 = EffectMeta("冷白", False, "7127614731187178783", "7127614731187178783", "a47ab1d817480c87ff6de4c9ba10b204", [])
    冷蓝                 = EffectMeta("冷蓝", False, "7127618237117877518", "7127618237117877518", "accf4492064dabe05dce1c28457b6f89", [])
    净白肤               = EffectMeta("净白肤", False, "7411580367452376361", "7411580367452376361", "e03e1f71900c5bc97f5c80059161429a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    凛冬                 = EffectMeta("凛冬", False, "7449996162343390473", "7449996162343390473", "f4cf3b6ee689d7dca67dc9e2d3cc2303", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    凝黛                 = EffectMeta("凝黛", False, "7298279202350976282", "7298279202350976282", "7bad3476dce5691d9e8f90f50122ed33", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    初恋                 = EffectMeta("初恋", False, "7195812984306814267", "7195812984306814267", "9fdc53e8dab072725d9bb088b8930869", [])
    千玺IXU              = EffectMeta("千玺IXU", False, "7127824119294364959", "7127824119294364959", "12af151fa57d3226ee3781a070ae54a6", [])
    千里江山             = EffectMeta("千里江山", False, "7208495854938901793", "7208495854938901793", "e084a0e8da69837502a97b63bf85b0a8", [])
    千金妝               = EffectMeta("千金妝", False, "7370585884078443802", "7370585884078443802", "e814069ba1dea090eeb44b397eeac252", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    卡露尔               = EffectMeta("卡露尔", False, "7301224597033192716", "7301224597033192716", "c95b8177a1b57996fcdb4b04d789ac28", [])
    即刻春光             = EffectMeta("即刻春光", False, "7127675868641594654", "7127675868641594654", "ba343f6bb3720ba81a8662d669b6b743", [])
    原木                 = EffectMeta("原木", False, "7127675195812351239", "7127675195812351239", "a2cb1c6dd47c2ce4aeb0dd7303353438", [])
    去黄增质             = EffectMeta("去黄增质", False, "7438854064458239258", "7438854064458239258", "008490b1e0c2a608966ab708b176584a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    去黄提亮             = EffectMeta("去黄提亮", False, "7438853477616340250", "7438853477616340250", "db9162c29361fbc85838182ec6a8fd51", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    古早韩系             = EffectMeta("古早韩系", False, "7462953965160893723", "7462953965160893723", "e59a2644bdd93eba36bfc8b8eb96c9ca", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    古早韩风             = EffectMeta("古早韩风", False, "7473168869222370571", "7473168869222370571", "2a0b58004ab4c613cf6da21d79143e53", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    古罗马               = EffectMeta("古罗马", False, "7242212640498568503", "7242212640498568503", "3d438e293e65d63e71af3db73b03bc4e", [])
    古风影视             = EffectMeta("古风影视", False, "7404104823563472137", "7404104823563472137", "42a7457ab2132e7da56676b0112f0a80", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    告白                 = EffectMeta("告白", False, "7437136821512949007", "7437136821512949007", "377e1a6c5d32f0ef99839ddd35f8d3aa", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    喜市                 = EffectMeta("喜市", False, "7185440129442417931", "7185440129442417931", "5210a45933f4265e5f262d3018a78d64", [])
    喜庆胶片             = EffectMeta("喜庆胶片", False, "7451265649273261363", "7451265649273261363", "b507e0b53989990c855e33bbfd18d9f6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    四喜                 = EffectMeta("四喜", False, "7312102522733268251", "7312102522733268251", "7ae54f18e5dc446f9269686b7d14f404", [])
    圣诞灯光             = EffectMeta("圣诞灯光", False, "7429295645669756195", "7429295645669756195", "d66aa7fafbb00c5b7ebb913cce97583f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    圣诞灯光II           = EffectMeta("圣诞灯光II", False, "7429295455953046818", "7429295455953046818", "fc1cb16d78ae2d3c57e50d2651e44054", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    圣诞灯光III          = EffectMeta("圣诞灯光III", False, "7429296137275755810", "7429296137275755810", "804cb9914032bb0bd58ad449e28302e7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    复古工业             = EffectMeta("复古工业", False, "7127608212483820837", "7127608212483820837", "cf8d236e185f6b174544151be3baba93", [])
    夏日小美好           = EffectMeta("夏日小美好", False, "7494125821032975642", "7494125821032975642", "985ce1e590cac79022c0b162c10080cf", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夏日泡泡             = EffectMeta("夏日泡泡", False, "7208548640279760140", "7208548640279760140", "19043b812fb18f38fab47b5bcf6080e0", [])
    夏日清凉             = EffectMeta("夏日清凉", False, "7505632228659973416", "7505632228659973416", "90897cbdc876de7beba905db2d6b3c40", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夏日辣妹             = EffectMeta("夏日辣妹", False, "7502729392179776779", "7502729392179776779", "b617fc9280cb849b8893d052ab937741", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夏日风吟             = EffectMeta("夏日风吟", False, "7127684611802418445", "7127684611802418445", "3120cfc3dd0f1fe2090749012d60a20b", [])
    夏荷青瓷             = EffectMeta("夏荷青瓷", False, "7244817652424641830", "7244817652424641830", "dac62447c29293f5f9ef519632fdb436", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    大唐盛世             = EffectMeta("大唐盛世", False, "7493423027670109449", "7493423027670109449", "0dfa10fafe76d2947b7cf1e3e50a5003", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    奈良                 = EffectMeta("奈良", False, "7351684015906147621", "7351684015906147621", "2a7ada2a5ac7a8742b37c3bc794b07b0", [])
    奥本海默             = EffectMeta("奥本海默", False, "7271142654505766183", "7271142654505766183", "2a1f03001d0db5f28f73bee7bc00ccf7", [])
    奶杏                 = EffectMeta("奶杏", False, "7297134192100379938", "7297134192100379938", "89ae84878534d61d0b7d62ba395fc8b7", [])
    奶油                 = EffectMeta("奶油", False, "7127618513048571173", "7127618513048571173", "dd39d5622353128e5f7c1de20020359a", [])
    奶油肤               = EffectMeta("奶油肤", False, "7463296170950020403", "7463296170950020403", "55291539636f958d2bca4ea9958efbad", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    奶绿                 = EffectMeta("奶绿", False, "7127684319300029733", "7127684319300029733", "8924565ec41520d2a8a88d846069768f", [])
    姜饼红               = EffectMeta("姜饼红", False, "7127624030135389471", "7127624030135389471", "22925be3f36caa278eb5df6a0278c636", [])
    威尼之都             = EffectMeta("威尼之都", False, "7406553962922429735", "7406553962922429735", "18606fd2c90ef2689278dc26e2cec94b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    安愉                 = EffectMeta("安愉", False, "7190242827543022880", "7190242827543022880", "ed7e951505cbf70dee0f4d144d239828", [])
    宫崎漫夏             = EffectMeta("宫崎漫夏", False, "7500223670678228262", "7500223670678228262", "2bb28eb6cdb9fd43ae41937e3a47cdb1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    富士CC_II            = EffectMeta("富士CC II", False, "7268561903721401641", "7268561903721401641", "cb92e0b13cd9b9a3aca8bb00b1a9c328", [])
    寻荷                 = EffectMeta("寻荷", False, "7295362817874480425", "7295362817874480425", "0230f2fb3e9ea72df20f8819542b4410", [])
    小镇                 = EffectMeta("小镇", False, "7127654151688965384", "7127654151688965384", "fc386676ee752b20918fb61c42c28a7b", [])
    山系                 = EffectMeta("山系", False, "7127662738884545806", "7127662738884545806", "d9d5332152b0f951229402d7d840263e", [])
    巧克力               = EffectMeta("巧克力", False, "7363220647767592243", "7363220647767592243", "6e513d9dcb9357219e35097b945a3881", [])
    布兰卡               = EffectMeta("布兰卡", False, "7242208887883992381", "7242208887883992381", "1774e2dd335a10a5f3174062c08403a2", [])
    布朗                 = EffectMeta("布朗", False, "7273777590102527290", "7273777590102527290", "b6bee72111d56fd16679adcf9543a05a", [])
    希望                 = EffectMeta("希望", False, "7271141541521968396", "7271141541521968396", "fdb975090cbdc5a5fb2e56ae982514a2", [])
    幽蓝                 = EffectMeta("幽蓝", False, "7330441280016715062", "7330441280016715062", "9db4cff7dd63bf1a17ced3728ca02e5e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    彩果                 = EffectMeta("彩果", False, "7175101541198679353", "7175101541198679353", "b5d50eae497be9aab963a96993a80df1", [])
    彩檐                 = EffectMeta("彩檐", False, "7226234868059917628", "7226234868059917628", "6c4502f0bd36c8d702db0c2b2f9ad18a", [])
    影叙                 = EffectMeta("影叙", False, "7349953761059638555", "7349953761059638555", "72e02210098c120bbcddca245656aaca", [])
    微澜                 = EffectMeta("微澜", False, "7338406163848940840", "7338406163848940840", "7e302ecfc744cbb1d38d71533214b257", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    德古拉               = EffectMeta("德古拉", False, "7127678346472819982", "7127678346472819982", "f8bfba1ebdb6c5054eec4eb1e9433e72", [])
    快照I                = EffectMeta("快照I", False, "7143537677655100709", "7143537677655100709", "526ce6c2fd2228cda17fc5f64a7267cf", [])
    忽风                 = EffectMeta("忽风", False, "7330123964305378586", "7330123964305378586", "c455bc6760bd9829f2d467866527a1b1", [])
    情感电影             = EffectMeta("情感电影", False, "7505461557237730598", "7505461557237730598", "f587d5a01d40ac69f26b9cc59a969822", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    情绪电影             = EffectMeta("情绪电影", False, "7420000959759224118", "7420000959759224118", "fd27b358349ee85c7a7241316534fef6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    扫街                 = EffectMeta("扫街", False, "7376146305736822028", "7376146305736822028", "fd2b6e08a9c7a29d5052c48fe10ecdfb", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    探店博主III          = EffectMeta("探店博主III", False, "7411911267859860746", "7411911267859860746", "400bd4f181603f72b4ca0174e0e62781", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    摩卡灰               = EffectMeta("摩卡灰", False, "7437011056653847808", "7437011056653847808", "e45427030aa2609974234c68b336511b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    敦刻尔克             = EffectMeta("敦刻尔克", False, "7127568601921408293", "7127568601921408293", "6b4a7017eecf10aa48e3f93586e04a6a", [])
    料理                 = EffectMeta("料理", False, "7127656350833806622", "7127656350833806622", "31ebabffaf3ed8653e0db318dfbeaa9d", [])
    新年电影             = EffectMeta("新年电影", False, "7445550576210873663", "7445550576210873663", "56bd30429814522169ee00614a7c3a05", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    新闪                 = EffectMeta("新闪", False, "7342395072199019803", "7342395072199019803", "9c3858dfbdd548bef8a012d55f795b47", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    日出                 = EffectMeta("日出", False, "7325383700240256296", "7325383700240256296", "628b7f7c8a7fea3f89edaff21f4c9d25", [])
    日系奶油             = EffectMeta("日系奶油", False, "7127664177870671135", "7127664177870671135", "8e779b2183d399fb192decf3616f8c27", [])
    日落橘               = EffectMeta("日落橘", False, "7127669630667066655", "7127669630667066655", "1ff996d1537f8a485f193314861c6b5b", [])
    日落飞车             = EffectMeta("日落飞车", False, "7505662247407013135", "7505662247407013135", "f077d7a11fa93abd6f0bd8786fe17fc0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    旧乐园               = EffectMeta("旧乐园", False, "7239977329668263227", "7239977329668263227", "604ff64bec0ae328aa1d1c19fb89bfa2", [])
    旧时代I              = EffectMeta("旧时代I", False, "7232218563270954300", "7232218563270954300", "9532fcb213a6eb45c2441d8d0466f9ef", [])
    明晰                 = EffectMeta("明晰", False, "7367715162964446516", "7367715162964446516", "c622c908228fb2796e141f973b9746e9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    星云                 = EffectMeta("星云", False, "7127672042069036319", "7127672042069036319", "b73b7e9c33f8e387cbb579a5c11f01b9", [])
    春日暖阳             = EffectMeta("春日暖阳", False, "7459274314634775827", "7459274314634775827", "56c9eb74589523ba37467165a9f73f76", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春日绿妍             = EffectMeta("春日绿妍", False, "7463345622440037658", "7463345622440037658", "0fa37f0c990e27a8029d65d07f84be23", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    昭和夏               = EffectMeta("昭和夏", False, "7505660075252485376", "7505660075252485376", "08e5c5e7bfba6a18dd67cd1c8eefeb1e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴好春日             = EffectMeta("晴好春日", False, "7468552996008299791", "7468552996008299791", "6ee5038f6fe86df6b95594bcdbe5075a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴沐                 = EffectMeta("晴沐", False, "7342503492311076137", "7342503492311076137", "1280aaabcbcdb3e0f2d5e39947d330d8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴研                 = EffectMeta("晴研", False, "7472763263684578572", "7472763263684578572", "696738f25d65091f3a1d77bda171d91c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暖食                 = EffectMeta("暖食", False, "7127653100269210916", "7127653100269210916", "47b7c1b9f560b85b528c24f7cbbb6cd4", [])
    暗夜                 = EffectMeta("暗夜", False, "7127823728070659358", "7127823728070659358", "788c476ccf299db46035bd930d90c342", [])
    暗调氛围             = EffectMeta("暗调氛围", False, "7463118934061993242", "7463118934061993242", "b5be681b2126319c4f831d4e0f8cfe31", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗雅                 = EffectMeta("暗雅", False, "7127656352410848548", "7127656352410848548", "c5207d449099512b7efd9419c75378f7", [])
    暮光                 = EffectMeta("暮光", False, "7242211155131862332", "7242211155131862332", "b5e36cb0438d74eac97fb6c7ec66260f", [])
    暮色                 = EffectMeta("暮色", False, "7127594686541237535", "7127594686541237535", "adbf6d3bbbd6a6d4525300d78323a7d2", [])
    月升之国             = EffectMeta("月升之国", False, "7127819487419567373", "7127819487419567373", "46638e887295beddd23c84206af26a1b", [])
    月夜                 = EffectMeta("月夜", False, "7143532202112912670", "7143532202112912670", "67cfe630584f194d007e3001052f5094", [])
    未央                 = EffectMeta("未央", False, "7340282260312182050", "7340282260312182050", "901d60cca1c56063279941926ed877be", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    朱栗                 = EffectMeta("朱栗", False, "7299055174880988479", "7299055174880988479", "d2fb23b72e1ed1ad368ab20c87ae5271", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    松果棕               = EffectMeta("松果棕", False, "7127669342325443854", "7127669342325443854", "d68bcfc1e312f0e3e52f164a59cff686", [])
    林间                 = EffectMeta("林间", False, "7127663793827564808", "7127663793827564808", "c1ff0cd2a3eea239334b9604d31b4947", [])
    柠檬青               = EffectMeta("柠檬青", False, "7127676358766923016", "7127676358766923016", "0437481ce079dd3f1160351c1038d628", [])
    梨花白               = EffectMeta("梨花白", False, "7345493751416016166", "7345493751416016166", "fa20a675c5b9caa46f42809746ed3ff5", [])
    梵时                 = EffectMeta("梵时", False, "7341767383259942155", "7341767383259942155", "a8908ae23533d029ea98fd6c5d052143", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    棕咖                 = EffectMeta("棕咖", False, "7273779209934245179", "7273779209934245179", "d661b0ee2e5417c12e824af664490161", [])
    棕宥                 = EffectMeta("棕宥", False, "7332348414933421366", "7332348414933421366", "d3dfad8c9cbc044369c528461bd79f57", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    棠梨                 = EffectMeta("棠梨", False, "7329819965920398604", "7329819965920398604", "09c9a4e110dd011c2155a544ecfe4b89", [])
    椰林                 = EffectMeta("椰林", False, "7252674515287788856", "7252674515287788856", "d0e4bf788a131db36ccf98e09f6cf056", [])
    椿和                 = EffectMeta("椿和", False, "7341032461234654475", "7341032461234654475", "46b1e432d7075fe6dc2b31d98809dac5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    椿来                 = EffectMeta("椿来", False, "7347729407181704498", "7347729407181704498", "13780c3447b3326ab87365015d0d0cb9", [])
    樱粉                 = EffectMeta("樱粉", False, "7127632545272925470", "7127632545272925470", "a5411e69fdf93e03f1d0c29ee6822173", [])
    比佛利               = EffectMeta("比佛利", False, "7127657040348040479", "7127657040348040479", "0b705ff4b8eb7fe5090848b588139e75", [])
    气泡水               = EffectMeta("气泡水", False, "7127619120761212168", "7127619120761212168", "4a0b28181b76b9ba2dd4ccdf66aa905a", [])
    江浙沪               = EffectMeta("江浙沪", False, "7127838224344435981", "7127838224344435981", "9287d59bc7ff0bce6f4893b0383c4bfe", [])
    治愈萌宠             = EffectMeta("治愈萌宠", False, "7454497262480231718", "7454497262480231718", "41f5c01699c2940a8ca8654cdaaf1bcc", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    泥金                 = EffectMeta("泥金", False, "7208495760520842529", "7208495760520842529", "62be11e3055851b4816ae3a55a7c1106", [])
    活力夏               = EffectMeta("活力夏", False, "7493764749054709001", "7493764749054709001", "8ad383deeb6804200d47aa85695d45fd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    流光金属             = EffectMeta("流光金属", False, "7127675565779307789", "7127675565779307789", "0c75bf2670f41bb66be90753649cd4a2", [])
    浅岛                 = EffectMeta("浅岛", False, "7281163331245821239", "7281163331245821239", "dc6d03248744c082a2929bb29184f820", [])
    浪漫烟火             = EffectMeta("浪漫烟火", False, "7446098658942078258", "7446098658942078258", "c69ce4d373a9ad5c212495d951935035", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    浮生                 = EffectMeta("浮生", False, "7340687187194678569", "7340687187194678569", "f438386d5155971f6ecd2600126fcbb4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    海浪梦境             = EffectMeta("海浪梦境", False, "7401018435674688787", "7401018435674688787", "ea9788764c806bf56c5442c70d6f1705", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    海街日记             = EffectMeta("海街日记", False, "7127615915004366116", "7127615915004366116", "8ac09d35b39a8b6f289ef5f4330a3d62", [])
    海雾                 = EffectMeta("海雾", False, "7189595107610447163", "7189595107610447163", "3099b6872219761db76f4c7cc86ea0e5", [])
    海鸥DC               = EffectMeta("海鸥DC", False, "7127830050786823437", "7127830050786823437", "8cd726548b6275553ce2668cca28f32e", [])
    深沉                 = EffectMeta("深沉", False, "7414897963752770828", "7414897963752770828", "2b7f9e970de54af1adab089a0006dfae", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    深秋                 = EffectMeta("深秋", False, "7295596083101633842", "7295596083101633842", "7f3622e3b0947e47bb12a835bf80c686", [])
    深褐                 = EffectMeta("深褐", False, "7127615347703811336", "7127615347703811336", "e7e999ed75f9f3a0626cf946b08c4f35", [])
    清冷                 = EffectMeta("清冷", False, "7405602958748028186", "7405602958748028186", "a70b959036e5b054ae6974045896cef3", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清冷冬日             = EffectMeta("清冷冬日", False, "7449939213430082867", "7449939213430082867", "41a819a8662d671d7bb79cf28719e0de", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新                 = EffectMeta("清新", False, "7469310117079420211", "7469310117079420211", "245032b4f8f96e0c760a1b2895a82f38", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新夏颜             = EffectMeta("清新夏颜", False, "7503936728286252323", "7503936728286252323", "b7a00d6e17947ce127f43aa7361478b5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新漫和             = EffectMeta("清新漫和", False, "7480517561486953779", "7480517561486953779", "5c4f109e0688d3d80d827172811a0a2a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清明上河             = EffectMeta("清明上河", False, "7208495962887621899", "7208495962887621899", "9fa5e1e67f3217c48cb8e64c26469fc1", [])
    清晰明亮             = EffectMeta("清晰明亮", False, "7433813603758722342", "7433813603758722342", "79084bba6b177ef0e597583b46ad5d16", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰烟花             = EffectMeta("清晰烟花", False, "7448652759869525287", "7448652759869525287", "e1590847287bd196ebdc5866e395fa78", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清澈                 = EffectMeta("清澈", False, "7359419156619332902", "7359419156619332902", "a40f003f9ea1ff5570314e7fa1e0a289", [])
    清透自然             = EffectMeta("清透自然", False, "7482047649831570726", "7482047649831570726", "798b1b2fdced376700d7069fed060793", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    温述                 = EffectMeta("温述", False, "7351580023742090535", "7351580023742090535", "207610064067f787d8339e8661a19d72", [])
    港历                 = EffectMeta("港历", False, "7346017304909581587", "7346017304909581587", "a60377ccb7d2eba39c9c9a54178f2869", [])
    港风                 = EffectMeta("港风", False, "7127830945243090184", "7127830945243090184", "44c277e7933012ecceaa669d4bc64452", [])
    演唱会               = EffectMeta("演唱会", False, "7396701250764426546", "7396701250764426546", "9753e98d86b99c2a0a99fb4dbfbfa981", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    漫夏                 = EffectMeta("漫夏", False, "7366616947703991571", "7366616947703991571", "3b090944724c8cc1a8d7a5d73be3358f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    漫彩                 = EffectMeta("漫彩", False, "7177269429972045089", "7177269429972045089", "71885c8e558e4b6fece843e3d4464e62", [])
    漫春                 = EffectMeta("漫春", False, "7332866997128105228", "7332866997128105228", "0affb5f75ea91249ecdeb3fa5e255255", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    漫步                 = EffectMeta("漫步", False, "7263357613050563852", "7263357613050563852", "de874f8a3993f93bb067593f0dfcfa5a", [])
    漫谷                 = EffectMeta("漫谷", False, "7312002825054211378", "7312002825054211378", "c201f700471bac64dddec7f4844ee3a7", [])
    烈焰红               = EffectMeta("烈焰红", False, "7409669784155000090", "7409669784155000090", "46c99536d5481e0e1e4dbe445ff1144c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    烘培                 = EffectMeta("烘培", False, "7127675183246200072", "7127675183246200072", "55cb15f600fff6aa4bda19f490aa7548", [])
    烟岚                 = EffectMeta("烟岚", False, "7341204799590763788", "7341204799590763788", "33937d0f480f994e09bc32adfe352cbd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    烟火增色             = EffectMeta("烟火增色", False, "7446098755905965338", "7446098755905965338", "8f844a1d9916774ba105fc26dee5212d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    烟花增强             = EffectMeta("烟花增强", False, "7444905127871270181", "7444905127871270181", "aed1cca59d133d454f96f5ce0e6888ed", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    烟霞                 = EffectMeta("烟霞", False, "7143533042978524424", "7143533042978524424", "e33d66d89891ebab00dabb91a4b4caee", [])
    热烈                 = EffectMeta("热烈", False, "7471880541189492007", "7471880541189492007", "bb9e824b308077331a1f0f2da36ae7da", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    煦日                 = EffectMeta("煦日", False, "7297144048903556388", "7297144048903556388", "0ccb49dc9361df2d3262786b6c43d8ee", [])
    熔金                 = EffectMeta("熔金", False, "7143575737881120037", "7143575737881120037", "870a7dad3d5f5aae975be2b353d2ed06", [])
    燃力                 = EffectMeta("燃力", False, "7248571956860079395", "7248571956860079395", "f8deda9b7cb4ff2f4e6382795c7265a7", [])
    牛皮纸               = EffectMeta("牛皮纸", False, "7127822013074263310", "7127822013074263310", "351a03b45cb0cd2e13911113e7b06ca5", [])
    珠光蓝               = EffectMeta("珠光蓝", False, "7127657509501914399", "7127657509501914399", "2b91f0f9a4a9cac90b3cd1be50637f58", [])
    珠落                 = EffectMeta("珠落", False, "7213575938615872823", "7213575938615872823", "9ced1b064be8feb4c3c3b2989b61e286", [])
    病娇                 = EffectMeta("病娇", False, "7291179909718740259", "7291179909718740259", "5e1e1d48442e9e2fa3bab8e724bce4ad", [])
    盐岚                 = EffectMeta("盐岚", False, "7359223280714239268", "7359223280714239268", "e517e2dd0dc2601874ce0ca63c9cc75d", [])
    矿野                 = EffectMeta("矿野", False, "7281162649314889015", "7281162649314889015", "7e645e33c8e3d019669e9cb5d03d6886", [])
    砂红                 = EffectMeta("砂红", False, "7300758676732677427", "7300758676732677427", "2f33ad8925eb2079b23900241fcf83a4", [])
    砾绀                 = EffectMeta("砾绀", False, "7340915058542759219", "7340915058542759219", "d0f6bbafe6d5b1d6d5100e99c79b9e9e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    空灵                 = EffectMeta("空灵", False, "7353555308448419098", "7353555308448419098", "341afbfb8058ac32a1994b2dc39be59c", [])
    空谷                 = EffectMeta("空谷", False, "7143532176313699620", "7143532176313699620", "03d4f2901ecb0ea047b731273f2ee3d0", [])
    竹绢                 = EffectMeta("竹绢", False, "7208496463293320480", "7208496463293320480", "807ef3820365dbe8c27047bab51ab65d", [])
    米棕                 = EffectMeta("米棕", False, "7221477781043973413", "7221477781043973413", "e687f0134f6ee01f8f50198bd52ebd00", [])
    粉瓷                 = EffectMeta("粉瓷", False, "7127667757998411044", "7127667757998411044", "76eac8836f1ddd762af8c6317b1c8c73", [])
    粉肤                 = EffectMeta("粉肤", False, "7296493947625557286", "7296493947625557286", "1b4893feb8dac4eb014b6e3f52449786", [])
    粹光                 = EffectMeta("粹光", False, "7373693828328475941", "7373693828328475941", "a3b69c7718dab46fedcd6ceabcb7425b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    素肌                 = EffectMeta("素肌", False, "7127671162758270245", "7127671162758270245", "cfb819eefe90e08965021dfea52d402b", [])
    红绿                 = EffectMeta("红绿", False, "7127622617699290399", "7127622617699290399", "e20b3185492170b68d6c7944270e3f76", [])
    绝对红               = EffectMeta("绝对红", False, "7127667361456426248", "7127667361456426248", "cc6084f69428c5a741ea4280ddbfe3c8", [])
    绿妍                 = EffectMeta("绿妍", False, "7127675252410223909", "7127675252410223909", "46a6f490249d7eabe3a9e8cd8e92cf2d", [])
    美味                 = EffectMeta("美味", False, "7414142998075690279", "7414142998075690279", "08e7404edc27b9b8c0a9ce51ccbb75dc", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    老友记               = EffectMeta("老友记", False, "7127669912050420999", "7127669912050420999", "e45f9a4c50717a3585006591b41e3440", [])
    胡桃木               = EffectMeta("胡桃木", False, "7127830961621847310", "7127830961621847310", "5eb7457d0d18cfdf0dcd99725acf2dd9", [])
    自然                 = EffectMeta("自然", False, "7127821314198342943", "7127821314198342943", "f4a371ed60b7448b146cd1b1c697a9e8", [])
    自然清晰             = EffectMeta("自然清晰", False, "7412691247992671497", "7412691247992671497", "b53afa88ca3762e229cdcf982c705d49", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    自由                 = EffectMeta("自由", False, "7271143155544739108", "7271143155544739108", "a202f96129bf04064a37cd92f5fda5b9", [])
    臻金                 = EffectMeta("臻金", False, "7306726303594564904", "7306726303594564904", "6cae1766e18f62be45ddcf4d169da037", [])
    花园                 = EffectMeta("花园", False, "7226990672190950713", "7226990672190950713", "b235531243327c4b03bdd5495f95d9c6", [])
    花椿                 = EffectMeta("花椿", False, "7127539889553427719", "7127539889553427719", "6502db5f541da3fdfbedf9161a79e53c", [])
    花火                 = EffectMeta("花火", False, "7175071186185964812", "7175071186185964812", "cd3a2d3f97bb4874bc9b16f36fec2329", [])
    花火夜焰             = EffectMeta("花火夜焰", False, "7460022261144177957", "7460022261144177957", "b78a09cb97225b3fde2575cea820da3e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    花花世界             = EffectMeta("花花世界", False, "7505429510930730275", "7505429510930730275", "e5c8c6ee154d78c75d8236197ae79a9e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    落日                 = EffectMeta("落日", False, "7166494058305670432", "7166494058305670432", "a3909c6739bcfffce11c1ed328afdb39", [])
    落日海岛             = EffectMeta("落日海岛", False, "7369501986401570099", "7369501986401570099", "0cefc26f8aa950c8934766ad229255bc", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    落日飞车             = EffectMeta("落日飞车", False, "7350133636890463498", "7350133636890463498", "c92ce87d49816b7c930d5c1a5f537536", [])
    落牧                 = EffectMeta("落牧", False, "7375415880118783295", "7375415880118783295", "14f918c1d7bd5d19324268c8e7874cd4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    蒸汽波               = EffectMeta("蒸汽波", False, "7127671519450320159", "7127671519450320159", "620ed46028278726516be363bdf070de", [])
    薄荷                 = EffectMeta("薄荷", False, "7343782317820857641", "7343782317820857641", "eed11d695897d0068dc658d09a18f444", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    褪色                 = EffectMeta("褪色", False, "7127668404764380447", "7127668404764380447", "13ed65a66841ee746146665f0aa18c6d", [])
    西野                 = EffectMeta("西野", False, "7331590962696834313", "7331590962696834313", "c5368d1617ac7b8af8b616782b388557", [])
    西餐                 = EffectMeta("西餐", False, "7127668806398315806", "7127668806398315806", "c447f798e1aaf5a776b40432571e9ee8", [])
    谧歌                 = EffectMeta("谧歌", False, "7301212776532380966", "7301212776532380966", "229eed4ae519e0c29efe23a2f07ba644", [])
    贝松绿               = EffectMeta("贝松绿", False, "7127668616991952158", "7127668616991952158", "5820a95014d61c7b5a45d23ba045d0e1", [])
    质感暗调             = EffectMeta("质感暗调", False, "7127653798155209997", "7127653798155209997", "80cc0198c081d823bfbfa08fd5e0c3c6", [])
    质感电影             = EffectMeta("质感电影", False, "7395858604311596299", "7395858604311596299", "163feab5aa04b300109d4317cf5c7712", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    赛博朋克             = EffectMeta("赛博朋克", False, "7127657979838516494", "7127657979838516494", "fe6d8ddb41fd8ea4f184ff5d9ca0b77e", [])
    赤陀                 = EffectMeta("赤陀", False, "7226251886360300837", "7226251886360300837", "f44a2fd63bcdb30bd1cdfd1120ced1e1", [])
    赫本                 = EffectMeta("赫本", False, "7127663117508660517", "7127663117508660517", "589b59735865a200db3ac561640ed299", [])
    赫石                 = EffectMeta("赫石", False, "7302823953406446899", "7302823953406446899", "4be5b26f8b932f7fe7a3f8033d5549b2", [])
    轻食                 = EffectMeta("轻食", False, "7127621137705618724", "7127621137705618724", "27fbb36cf04af9886d4d9e6abcd3691b", [])
    达芬妮               = EffectMeta("达芬妮", False, "7300602459356040484", "7300602459356040484", "e9556101678a74dc573133da00401854", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    迈阿密               = EffectMeta("迈阿密", False, "7127684611450178823", "7127684611450178823", "f9f32708f0029a5b043736e64133324f", [])
    酷白                 = EffectMeta("酷白", False, "7127676762514885919", "7127676762514885919", "e62e07d9ed430226e6afaa96dba3844a", [])
    野餐                 = EffectMeta("野餐", False, "7246617998516063527", "7246617998516063527", "a16b2e6c9faaafff19e3c3276e4eca65", [])
    金属                 = EffectMeta("金属", False, "7127654151688949000", "7127654151688949000", "7aaae4aad5195f4df6929d9cb2f77fc9", [])
    闪光灯               = EffectMeta("闪光灯", False, "7364705637931994405", "7364705637931994405", "5b6fd1621826d837d88c71de0ced5f76", [])
    闪胶回忆             = EffectMeta("闪胶回忆", False, "7452726092126833959", "7452726092126833959", "4a1de85787a2fa27ddbe569a73e787e4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    闻香识人             = EffectMeta("闻香识人", False, "7127823728267775263", "7127823728267775263", "56693fef51ca05d7631f1bf3ae47c3cc", [])
    阿尔菲               = EffectMeta("阿尔菲", False, "7299130097632627979", "7299130097632627979", "5225172497e1cd5bd3a8e1162a9c25d0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    雪鹿                 = EffectMeta("雪鹿", False, "7302796570947243264", "7302796570947243264", "10ff7e7bc0accc06c5ce3b9c09114b18", [])
    雾瓷                 = EffectMeta("雾瓷", False, "7169239634076060960", "7169239634076060960", "03e7a58f2d18954a4ced7fec8371cd5e", [])
    青春古早             = EffectMeta("青春古早", False, "7505676110412254527", "7505676110412254527", "80742c0b85468f8cb13333db96449c36", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    青橙                 = EffectMeta("青橙", False, "7127615575865478430", "7127615575865478430", "58b4c939e727d94fb074ca0a1c0400ad", [])
    青橙电影             = EffectMeta("青橙电影", False, "7401896022214970650", "7401896022214970650", "6ccecf9c82c21938ed4bd2751db52b9c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    青红夜               = EffectMeta("青红夜", False, "7281575818621455628", "7281575818621455628", "7b439160a4134076dc70571813ec9cbb", [])
    音乐节               = EffectMeta("音乐节", False, "7405834787132280079", "7405834787132280079", "b61e21d4516390ecde868b5d670126d6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    风铃                 = EffectMeta("风铃", False, "7211001257996127547", "7211001257996127547", "48d79f8501ade6fd7a33055b83947eb8", [])
    香松                 = EffectMeta("香松", False, "7175094003493309757", "7175094003493309757", "528e10e4419475bf6acf24488b660dbd", [])
    高清4K电影           = EffectMeta("高清4K电影", False, "7452548610971012379", "7452548610971012379", "f23af43c6ec3724a0cb415677dae00c0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清冬日             = EffectMeta("高清冬日", False, "7450317804554685708", "7450317804554685708", "85b6ad6c821ee2361ce32cae5c70acf9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清明亮             = EffectMeta("高清明亮", False, "7434564801990266162", "7434564801990266162", "6a7ba37411cc37d75d9ae20d29b65dee", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清润白             = EffectMeta("高清润白", False, "7404503340576410906", "7404503340576410906", "d454e2c98a89324036eef9c15ebb3590", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清烟火             = EffectMeta("高清烟火", False, "7446098482013768970", "7446098482013768970", "8eeca9ea5018c168413ec0e080655bb5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清福气             = EffectMeta("高清福气", False, "7460008665286855973", "7460008665286855973", "935da93388e6d7542176aa5e614c14f2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高饱和               = EffectMeta("高饱和", False, "7127653121966230814", "7127653121966230814", "a0533d46f3bc544f36e00965b2644067", [])
    鬼魅                 = EffectMeta("鬼魅", False, "7291201164027252024", "7291201164027252024", "20fd9ce9674e1e0137955e2d74ce252a", [])
    鲜亮食光             = EffectMeta("鲜亮食光", False, "7441227246326582537", "7441227246326582537", "7c0143c47f7ffa237d2c84b0e42c9a7a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    鲜美年味             = EffectMeta("鲜美年味", False, "7460115630973340940", "7460115630973340940", "862e1a16a282b2ddc8112a317e53d3d7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    黑胶唱片             = EffectMeta("黑胶唱片", False, "7221805176410180921", "7221805176410180921", "97fc59d95cbb611d888bf10da5a1c015", [])
    黑莓                 = EffectMeta("黑莓", False, "7175100298610871610", "7175100298610871610", "aefe136056b95d5f06b4cbb440961168", [])
    黑豹                 = EffectMeta("黑豹", False, "7202475126485503236", "7202475126485503236", "9f33e8c52e07d1af8ff00781f7645124", [])
    默片                 = EffectMeta("默片", False, "7127655037026848031", "7127655037026848031", "81be2b9491c4c805cb4f70a595ab46a6", [])

    # 付费特效
    _160C                = EffectMeta("160C", True, "7190249807682800954", "7190249807682800954", "7505f10b71bc6e346a1696544121ac9e", [])
    _2077                = EffectMeta("2077", True, "7131347316111314189", "7131347316111314189", "168cd951f6f51c1fb1cd9ea1658f4012", [])
    _400H                = EffectMeta("400H", True, "7190236487152127269", "7190236487152127269", "20817f9b1ed37a720c02abea87714655", [])
    _4K画质              = EffectMeta("4K画质", True, "7477802799862992138", "7477802799862992138", "857c116e0fde4f429fe4ee0084283843", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    _4K画质电影          = EffectMeta("4K画质电影", True, "7478641636092775743", "7478641636092775743", "46b9cdb1c33433a6eaa8e0ba5ac29322", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    _4K高品质            = EffectMeta("4K高品质", True, "7480203423095213362", "7480203423095213362", "68d93b6b15e95f4c6f39fd659873ef07", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    _800Z                = EffectMeta("800Z", True, "7190237757552348471", "7190237757552348471", "53acbe492462a72db57c3f5ed7de9345", [])
    _8K画质              = EffectMeta("8K画质", True, "7478895015901613375", "7478895015901613375", "d5a81c57ca772c8456e3f9d53ebaf67e", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    _90s                 = EffectMeta("90s", True, "7131366613823114503", "7131366613823114503", "ff76a6962c69106eede587fab606fc27", [])
    City_Walk            = EffectMeta("City Walk", True, "7263360572404550931", "7263360572404550931", "9a183540a03b391b3a17b67970ddc93a", [])
    EOS3                 = EffectMeta("EOS3", True, "7200697197002886404", "7200697197002886404", "1ea3335f32de0ff87c643bd0df2075e4", [])
    FXN                  = EffectMeta("FXN", True, "7332480052392774975", "7332480052392774975", "01cd75f7c9b5fb3b05bbcb54e53400d4", [])
    GR正片               = EffectMeta("GR正片", True, "7168098796860148995", "7168098796860148995", "1f28a387f3f22baff4b1410530d2750f", [])
    GR绿                 = EffectMeta("GR绿", True, "7168121440141708576", "7168121440141708576", "5ad1db915106f04413a025928b28cdf5", [])
    GR蓝                 = EffectMeta("GR蓝", True, "7168097661160131879", "7168097661160131879", "c7f40f1f2b5c655d6ca5f45f8d86b52d", [])
    IG白                 = EffectMeta("IG白", True, "7221479156318489893", "7221479156318489893", "02a7a3a08ed9756bb1ae7b924213c33d", [])
    INS亮肤              = EffectMeta("INS亮肤", True, "7438279481191599411", "7438279481191599411", "15a084174af323240d88f2911613bb7a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    INS晴肤              = EffectMeta("INS晴肤", True, "7438279661588581669", "7438279661588581669", "77a245b9cc31d17d4fffc621d1a16d83", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    INS暗                = EffectMeta("INS暗", True, "7223645151820877093", "7223645151820877093", "29c393013eddca0fdd0ee0087100915e", [])
    INS暗调              = EffectMeta("INS暗调", True, "7473409650746985779", "7473409650746985779", "d15a78d524285235d2aedf03a27a6037", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    INS柔肤              = EffectMeta("INS柔肤", True, "7438646040036789542", "7438646040036789542", "096d6ca77da11bdfa15f055c82ccc187", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    KONICA               = EffectMeta("KONICA", True, "7200712753324035339", "7200712753324035339", "c05506c48792c883d3ecff9e25e0c677", [])
    KU4                  = EffectMeta("KU4", True, "7127669605199318280", "7127669605199318280", "b382bdfe54fed4ae7986f5205de60713", [])
    PENTAX               = EffectMeta("PENTAX", True, "7200999937960627459", "7200999937960627459", "87b401a86d70ae0fd4a5c3b23486c7b5", [])
    Pocket3              = EffectMeta("Pocket3", True, "7493462285889899803", "7493462285889899803", "52373abce98c4509bd1bbc5db694cbd2", [])
    Y3K                  = EffectMeta("Y3K", True, "7398034408139230490", "7398034408139230490", "a9dbbc5d01811225842ea0332fa330c1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    doll感透白           = EffectMeta("doll感透白", True, "7493542918276320539", "7493542918276320539", "64e3b6888a7afe415aedec81dfce032d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    iPhone6s             = EffectMeta("iPhone6s", True, "7393943544089627930", "7393943544089627930", "a83a14437d060aa093acf5f2441d6dc1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    万圣                 = EffectMeta("万圣", True, "7426749131344841995", "7426749131344841995", "9d8d5689c13ca9e44441527c505fb693", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    下雨天               = EffectMeta("下雨天", True, "7503602197586791743", "7503602197586791743", "4b7923d0d2db9788bf52de6e1558692f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    不要抬头             = EffectMeta("不要抬头", True, "7202480720843984131", "7202480720843984131", "3b3dc994ea819d31555abae026b1cc91", [])
    丝滑皮肤             = EffectMeta("丝滑皮肤", True, "7495673180904885516", "7495673180904885516", "7e44f3f603e1f39f46ee4bb552f2e7ac", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    中性                 = EffectMeta("中性", True, "7127621445806525704", "7127621445806525704", "8168144d29c35cf186eccb03ec9f3d93", [])
    中性II               = EffectMeta("中性II", True, "7312646907908607244", "7312646907908607244", "ad71ff12ac0afd02cb6c583d0ee69d8a", [])
    丹枫                 = EffectMeta("丹枫", True, "7297138825359281423", "7297138825359281423", "a97673c2524eba984b75396530501fa8", [])
    乐游                 = EffectMeta("乐游", True, "7193982146363673856", "7193982146363673856", "2a215f5fe9ff6c1a8effea9135bbe3bb", [])
    云暖                 = EffectMeta("云暖", True, "7314883649999015231", "7314883649999015231", "7819364ae09bf6c6771fce646cde6ec9", [])
    亚裔II               = EffectMeta("亚裔II", True, "7393338906369903910", "7393338906369903910", "95a3122514319889de739d782e1ad02b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    京都                 = EffectMeta("京都", True, "7127679758581697822", "7127679758581697822", "63e749e3d425d0912123b4d7e53fc446", [])
    亭竹                 = EffectMeta("亭竹", True, "7302325291634920755", "7302325291634920755", "4bddb2bc6d4ca571e5f45a3dbe3f84dc", [])
    亮丽                 = EffectMeta("亮丽", True, "7413406043608272154", "7413406043608272154", "46ac28247c5fd004e08d5d970152eb49", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    人生之事             = EffectMeta("人生之事", True, "7148844086869396743", "7148844086869396743", "352419343c715ea1be613980e91f5aa8", [])
    仲夏                 = EffectMeta("仲夏", True, "7127575884780817672", "7127575884780817672", "70d9d3e21083edc6d3b52dc2bbc8d054", [])
    仲夏夜               = EffectMeta("仲夏夜", True, "7281166048273943867", "7281166048273943867", "0773453b9c513222ed0b2a629b141b38", [])
    仿撕拉片             = EffectMeta("仿撕拉片", True, "7503844955467648283", "7503844955467648283", "184bb2a8f80b693ada67bd80ac38ab1e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    伊豆                 = EffectMeta("伊豆", True, "7195781682492984636", "7195781682492984636", "2330a4a65c6f4ab15ef39c10ab063ff7", [])
    伤感故事电影         = EffectMeta("伤感故事电影", True, "7516859499404119296", "7516859499404119296", "21b43b02064aef8b87590b2b3ebb67e1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    伤感电影             = EffectMeta("伤感电影", True, "7498948996816194843", "7498948996816194843", "c5ddafa9ebd09886302cc442398ab521", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    余晖                 = EffectMeta("余晖", True, "7278616064018107707", "7278616064018107707", "19e8ac930af976579c60df1ad6f4c4fe", [])
    佳能G12              = EffectMeta("佳能G12", True, "7485292050917657906", "7485292050917657906", "23ecefd04019e949de483cf913e08771", [])
    佳能G7X_II           = EffectMeta("佳能G7X II", True, "7291597100389862707", "7291597100389862707", "e9aef9a32a0ed9ebf39c9f23340fd408", [])
    佳能G7X_III          = EffectMeta("佳能G7X III", True, "7291595038688136474", "7291595038688136474", "3c89208f4754d78ad97df171a1cc1ffc", [])
    俏皮萌宠             = EffectMeta("俏皮萌宠", True, "7394713676789353737", "7394713676789353737", "bba8efffe5600316da5ac027b95fa231", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    俱乐部               = EffectMeta("俱乐部", True, "7239235794744003851", "7239235794744003851", "1f6a4516fb91c8e68217123191dc38ea", [])
    倾森                 = EffectMeta("倾森", True, "7332714336315526409", "7332714336315526409", "2b0731e9eacb5098ad43bd99ae6f23d7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    假日海滩             = EffectMeta("假日海滩", True, "7405115979107274020", "7405115979107274020", "4ac4228650cb812a80173b56c310aa15", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    假日电影感           = EffectMeta("假日电影感", True, "7517179906292190501", "7517179906292190501", "9c39d9434ea88b9e0614fbd4dd78d240", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    健身II               = EffectMeta("健身II", True, "7500860668199914790", "7500860668199914790", "e1f58996a63c9575f90a33d24e4bfccd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    傍晚                 = EffectMeta("傍晚", True, "7226990270053649725", "7226990270053649725", "a1aa29d3a6ea4ca73cb38dac5f5f5d6a", [])
    元宵祈福             = EffectMeta("元宵祈福", True, "7467923122545544499", "7467923122545544499", "4567a0899a90932be92a68098082eb1d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    元气粉肌             = EffectMeta("元气粉肌", True, "7472748943953169727", "7472748943953169727", "05b894b6fded9f70314c8223cfda6d64", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    光流                 = EffectMeta("光流", True, "7233732009070300473", "7233732009070300473", "351346b807ca9bfa063e517f10d96f95", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    冬日物语             = EffectMeta("冬日物语", True, "7444960658178821414", "7444960658178821414", "e04c7e0b73dda7a63c5fd938ac9946cb", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    冬日电影II           = EffectMeta("冬日电影II", True, "7446453265190948132", "7446453265190948132", "61852bede7a3b918009bbf7e2f0b0481", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    冬禧                 = EffectMeta("冬禧", True, "7190250133672578316", "7190250133672578316", "6423fd745c7ba83613feea71977763fb", [])
    冰夏                 = EffectMeta("冰夏", True, "7258221827485486393", "7258221827485486393", "d6a3a5ee2c52a32842ba9c269e4c7fde", [])
    冰清蓝               = EffectMeta("冰清蓝", True, "7494313060480388389", "7494313060480388389", "b7e789f7e334a6b4f75dc3037f50fdee", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    冰瀑                 = EffectMeta("冰瀑", True, "7196927862056701240", "7196927862056701240", "9691bde0838975e3573faad0791d3cdf", [])
    冰茶                 = EffectMeta("冰茶", True, "7131399016771800357", "7131399016771800357", "ab44066c23ab6639ca6ff5eb2b850582", [])
    冰雪白               = EffectMeta("冰雪白", True, "7462637393783360809", "7462637393783360809", "7dd656b0f9320d3130691567c6ee1645", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    冷叙                 = EffectMeta("冷叙", True, "7159132840179895590", "7159132840179895590", "c60635dea7f7a6df2ba9b1e08fee006e", [])
    冷墨                 = EffectMeta("冷墨", True, "7300751893813366053", "7300751893813366053", "e6d9891ef7f02898055a16f11a8750bc", [])
    冷月夜               = EffectMeta("冷月夜", True, "7281165355353951543", "7281165355353951543", "0a9aaba6174a6b1a46d78365bd7fa0c4", [])
    冷白圣诞             = EffectMeta("冷白圣诞", True, "7446290191557397814", "7446290191557397814", "c81c0f2ea8bf243a05d972a0659c8af5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    冷萃                 = EffectMeta("冷萃", True, "7177729481300364548", "7177729481300364548", "a7500c67b168c4ff886e0329b3662399", [])
    冷调CCD              = EffectMeta("冷调CCD", True, "7434467628422270220", "7434467628422270220", "4b508c7a838560659d4acca26a7ffea0", [])
    净白                 = EffectMeta("净白", True, "7127667352782572807", "7127667352782572807", "c13995808d8fbfdf9ed2b9f2873dfea7", [])
    凉夏                 = EffectMeta("凉夏", True, "7377370212749839667", "7377370212749839667", "2857a91d80b1821a71a5d640bb2d33f3", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    加州落日             = EffectMeta("加州落日", True, "7498004563954322726", "7498004563954322726", "9274335a725277627eb10c958358f367", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    劲闯                 = EffectMeta("劲闯", True, "7248568097660013864", "7248568097660013864", "9822ae48045e256dfb2ca2369c368d47", [])
    千禧潮酷             = EffectMeta("千禧潮酷", True, "7513608221735554330", "7513608221735554330", "61e92e952bc3a99617ffabe355fed07e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    半衫                 = EffectMeta("半衫", True, "7145391402661334280", "7145391402661334280", "a4d67ea33ac459b1e0c2ab4677ebb3b1", [])
    原生自然             = EffectMeta("原生自然", True, "7473037215426153728", "7473037215426153728", "7db0af0929986a1d6a72425f03c97ec7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    原野                 = EffectMeta("原野", True, "7271281225115897140", "7271281225115897140", "fd213d120b3cb62c0128c73f24cba6a9", [])
    去灰                 = EffectMeta("去灰", True, "7127559231062002951", "7127559231062002951", "21c377ab968576732daa1643051b735c", [])
    去灰II               = EffectMeta("去灰II", True, "7226991425160858937", "7226991425160858937", "e58c1b8d3539cb1e89c37dc56b934369", [])
    去灰明晰             = EffectMeta("去灰明晰", True, "7436399689764834623", "7436399689764834623", "bf4984955b7c9d8682b34784abe07948", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    去灰高清             = EffectMeta("去灰高清", True, "7436400247540141348", "7436400247540141348", "8fa6afa7dcdaed7d26d2829aece5dca0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    去雾                 = EffectMeta("去雾", True, "7473437502787816740", "7473437502787816740", "cc9d8a8be29f7ea8f8807d5d5ca3a61d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    反差富士             = EffectMeta("反差富士", True, "7403222365217295667", "7403222365217295667", "60bcb4eb31327c764963919972a31628", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    发光CCD              = EffectMeta("发光CCD", True, "7434468515576319295", "7434468515576319295", "56442b377a1b22860018e387ca1d9ea2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    发光肤               = EffectMeta("发光肤", True, "7477960070073027850", "7477960070073027850", "16027cb1b7cd27ac1ac02baad1d2e553", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    叠阳                 = EffectMeta("叠阳", True, "7148961858320354573", "7148961858320354573", "852e9a57b27c6d6f4e71b65be8f43927", [])
    古早像素             = EffectMeta("古早像素", True, "7470614335644077375", "7470614335644077375", "c874f99264828b3f179288d81745cf42", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    古早回忆             = EffectMeta("古早回忆", True, "7449798505385790746", "7449798505385790746", "26a8a7b5705761b5c26d49532a0e74ec", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    古早复古             = EffectMeta("古早复古", True, "7457910812439596339", "7457910812439596339", "b2884dc7ce5cc92bab1179ca2e31db35", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    古早记忆             = EffectMeta("古早记忆", True, "7366562482812456255", "7366562482812456255", "3a6086410283e0166d65d7935faa3809", [])
    古早韩式             = EffectMeta("古早韩式", True, "7469697255663078694", "7469697255663078694", "5a5e95024f4ced3da0fd167a4931cd1b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    古都                 = EffectMeta("古都", True, "7127615616525126949", "7127615616525126949", "ce6f674fe7eebb2be94a3784496d2d4f", [])
    吉宵                 = EffectMeta("吉宵", True, "7190241639070174503", "7190241639070174503", "14910132a5caef71f9fa0a1076098026", [])
    味蕾                 = EffectMeta("味蕾", True, "7281166220794055997", "7281166220794055997", "04205b3010d2adedb961380ceb679a6b", [])
    和歌山               = EffectMeta("和歌山", True, "7210651068324285754", "7210651068324285754", "50e01f465c3dc235b925e5a43ed901eb", [])
    哈苏I                = EffectMeta("哈苏I", True, "7291596720956329266", "7291596720956329266", "df3882769e455938b11f5596ac569e49", [])
    哈苏II               = EffectMeta("哈苏II", True, "7291560741885480250", "7291560741885480250", "498b45335903ffa59cef94ac0376fd38", [])
    哈苏蓝               = EffectMeta("哈苏蓝", True, "7361792059109313811", "7361792059109313811", "45392b51287027d5fa5249495c6a9007", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    哥谭                 = EffectMeta("哥谭", True, "7337928347118275890", "7337928347118275890", "25575caefd72dfcac744d7aa717d4c1f", [])
    唤晴II               = EffectMeta("唤晴II", True, "7485986828164599067", "7485986828164599067", "a7fc072d2ec64e29e9568d580edd6e7c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    国民旧照             = EffectMeta("国民旧照", True, "7511971221785922826", "7511971221785922826", "b188101c8e03b870871faac571033dd9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    国风影视             = EffectMeta("国风影视", True, "7507263202682572044", "7507263202682572044", "780c9df564ba881242a3a3fd205c584c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    国风电影             = EffectMeta("国风电影", True, "7409572381775138067", "7409572381775138067", "8600273a392d0e967d9671cd20ec0899", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    圣善夜               = EffectMeta("圣善夜", True, "7175100386007584060", "7175100386007584060", "d67a3e3c70791b034ccbd201de89908d", [])
    圣诞回忆录           = EffectMeta("圣诞回忆录", True, "7447162094572686592", "7447162094572686592", "58f5e01abfb26b8db86ef923ffc35f9b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    圣诞愿景             = EffectMeta("圣诞愿景", True, "7428162298436537627", "7428162298436537627", "beff3bd9341b5517c97c23eafe24983a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    圣诞拍立得           = EffectMeta("圣诞拍立得", True, "7438160882837835018", "7438160882837835018", "29632de266432a7808e62d5e4d499637", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    圣诞闪胶             = EffectMeta("圣诞闪胶", True, "7446329652706168100", "7446329652706168100", "b8284b725f840f880ae21208fc87fa75", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    圣诞闪胶II           = EffectMeta("圣诞闪胶II", True, "7446329592119332108", "7446329592119332108", "d2f78c92985d2e02e1ae6819abf6b30f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    城市赏月II           = EffectMeta("城市赏月II", True, "7405206230550973731", "7405206230550973731", "86ea7d3bdd6f5605d8d0d7e2e5a92200", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    增色II               = EffectMeta("增色II", True, "7411476796526300452", "7411476796526300452", "8794bb983e61ab36704bbc7b6c964237", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    增质CCD              = EffectMeta("增质CCD", True, "7500847387959708978", "7500847387959708978", "41f83b3a2e4e741112b4b98e83735eb4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    墨林                 = EffectMeta("墨林", True, "7271284653816843554", "7271284653816843554", "a311fa20eacf38b912c183627e008ff5", [])
    复古电影感           = EffectMeta("复古电影感", True, "7479800436778732863", "7479800436778732863", "ac5a841a4e7a08b12c69e43da470768f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    复古蓝调             = EffectMeta("复古蓝调", True, "7449048492665834779", "7449048492665834779", "d00d1242160522fdbdb8b5d694549728", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夏天岛               = EffectMeta("夏天岛", True, "7258222828581915959", "7258222828581915959", "84743746b64ea59c89eb7d404c0be696", [])
    夏威夷               = EffectMeta("夏威夷", True, "7159140854601469223", "7159140854601469223", "616966578de6ebccae6b5eaa5b914d82", [])
    夏日度假             = EffectMeta("夏日度假", True, "7497479023556070693", "7497479023556070693", "3243469a2db642375b9c7edb372eb835", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夏日物语             = EffectMeta("夏日物语", True, "7503950769758948620", "7503950769758948620", "f0c9d57e7fabbe8116ea7b6e2b4438c0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夏日粉               = EffectMeta("夏日粉", True, "7261469707138518283", "7261469707138518283", "b667443ab8554ad725bd72bb9cabab2b", [])
    夏日紫霞             = EffectMeta("夏日紫霞", True, "7508030199255026970", "7508030199255026970", "e2511ed7c2027e8df0205c3dc96116cf", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夏日繁花             = EffectMeta("夏日繁花", True, "7509774929961684278", "7509774929961684278", "95f365426843cbefe175bf9b6699fee7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    多巴胺               = EffectMeta("多巴胺", True, "7237441824611224889", "7237441824611224889", "83ec0f2e61d762e17830bd55ca08e8d3", [])
    夜拍闪曝             = EffectMeta("夜拍闪曝", True, "7494135245709610275", "7494135245709610275", "775c6fd432cc8c187c473b1ea109b0d4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夜拍高光             = EffectMeta("夜拍高光", True, "7462637606052941095", "7462637606052941095", "f7ba4b96c56acc96fa7c86f1e13f1c43", [])
    夜景人像增强         = EffectMeta("夜景人像增强", True, "7493208490832317705", "7493208490832317705", "c2574ae2684de016ee740b78b2c6064d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夜景去雾             = EffectMeta("夜景去雾", True, "7525110001959030042", "7525110001959030042", "c5744f7e50df98655bcdc4101a19b768", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夜景增色             = EffectMeta("夜景增色", True, "7341302999068757259", "7341302999068757259", "f144c6f9e9accae6cb76c2b11b9549b2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夜景增色II           = EffectMeta("夜景增色II", True, "7411477748130139403", "7411477748130139403", "1be937803f18855a2ee12a82c6d8c30a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夜焰                 = EffectMeta("夜焰", True, "7185289606600953092", "7185289606600953092", "fdafbb7b837d162b7ff32cbb0f130da4", [])
    夜雾                 = EffectMeta("夜雾", True, "7168110568673479948", "7168110568673479948", "e6b2ff75ac938639d840ec586264c2f5", [])
    大吉岭               = EffectMeta("大吉岭", True, "7175076362997288230", "7175076362997288230", "d6138cfc775b365ce144308d5a7c46d9", [])
    大海增色             = EffectMeta("大海增色", True, "7500853613342772507", "7500853613342772507", "c2c3d5067e31b748bf7c2686047f8ea9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    大疆电影感           = EffectMeta("大疆电影感", True, "7512706064693988645", "7512706064693988645", "2a70d8e43f4cec20b20d602da4e60676", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    奥林巴斯             = EffectMeta("奥林巴斯", True, "7361792068475325735", "7361792068475325735", "a523adb5976eb5a39d963683f520551f", [])
    奥罗拉               = EffectMeta("奥罗拉", True, "7269236283019463972", "7269236283019463972", "2a04fac3df136d4135b8ea94aa7d604a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    奶呼萌宠             = EffectMeta("奶呼萌宠", True, "7395972887133441307", "7395972887133441307", "7278a8d1ae246098e7f8db233bbec459", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    奶油II               = EffectMeta("奶油II", True, "7474592762331942184", "7474592762331942184", "4a972233f7836fd91773131bdba27488", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    奶油原生             = EffectMeta("奶油原生", True, "7501670015859445055", "7501670015859445055", "ac040ebfb2343dbcf2c0c17227009d4e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    奶油柔肤             = EffectMeta("奶油柔肤", True, "7482412177760996646", "7482412177760996646", "a64d8790c1f50c529d66b382290fbabc", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    奶油白               = EffectMeta("奶油白", True, "7398438142321134898", "7398438142321134898", "48358ee1c48f7293c4148609e736337f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    奶油美食             = EffectMeta("奶油美食", True, "7480210942026927423", "7480210942026927423", "406786a335a27c96d88acdb491582c6b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    奶油风萌宠           = EffectMeta("奶油风萌宠", True, "7510488117430734118", "7510488117430734118", "9088ec10dbd831542695d8522ba43007", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    奶白肌               = EffectMeta("奶白肌", True, "7478708795057753370", "7478708795057753370", "74feb842579ef07327bc8172458363e4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    好莱坞I              = EffectMeta("好莱坞I", True, "7226994281414692155", "7226994281414692155", "b255b7959f2c621cdbc5aa7cda9e7583", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    好莱坞II             = EffectMeta("好莱坞II", True, "7226995248814165308", "7226995248814165308", "41348d00e1ab4f1dbe6832f8b6224c13", [])
    好莱坞III            = EffectMeta("好莱坞III", True, "7312617341710372107", "7312617341710372107", "59b8ade3560f637686d6e4b0f56f97fe", [])
    好莱坞IV             = EffectMeta("好莱坞IV", True, "7312647197462367524", "7312647197462367524", "12657ebf4545c621bc0ca38944b9712c", [])
    嫣时                 = EffectMeta("嫣时", True, "7339908905713143051", "7339908905713143051", "aee9d89426e1208211df5d50a30fe1e8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    嫩肤                 = EffectMeta("嫩肤", True, "7300523145818148096", "7300523145818148096", "f79fa85e5e9238570b84b95505406213", [])
    嬉皮士               = EffectMeta("嬉皮士", True, "7131431284403981605", "7131431284403981605", "218af350afd9de1bfdd017218e7eeae4", [])
    子弹列车             = EffectMeta("子弹列车", True, "7202480777387445507", "7202480777387445507", "ee8aa0105ea992ace4fc114c34b08adc", [])
    安西娅               = EffectMeta("安西娅", True, "7270142995712773415", "7270142995712773415", "85e046726dee3b398e38a3d31b48e500", [])
    家宴                 = EffectMeta("家宴", True, "7330584144524643595", "7330584144524643595", "1cb453a49c768a3f9c086b047321c233", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    宿营                 = EffectMeta("宿营", True, "7127822311708691726", "7127822311708691726", "e8ad70a709e7a37282ee64779c874732", [])
    富士CC_I             = EffectMeta("富士CC I", True, "7268561936344780086", "7268561936344780086", "069ae1d53dc300c85b017cdf6df18550", [])
    富士NC_I             = EffectMeta("富士NC I", True, "7159156535640296737", "7159156535640296737", "bdce583bf77430b24e9f7d78d40a69eb", [])
    富士NC_II            = EffectMeta("富士NC II", True, "7159408376378559747", "7159408376378559747", "0fce68168c67f99c11bf1e05e933eb79", [])
    富士NC_III           = EffectMeta("富士NC III", True, "7159134459088899339", "7159134459088899339", "25f1e0d1d5997b56577a96de8de2005d", [])
    富士NN               = EffectMeta("富士NN", True, "7447157317457513743", "7447157317457513743", "015e667b8a037ff32dd679f96b40963d", [])
    富士x100             = EffectMeta("富士x100", True, "7394357532912782629", "7394357532912782629", "fc5765383ceef36fc858b8c4a4430bb8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    富士电影             = EffectMeta("富士电影", True, "7497919307628825866", "7497919307628825866", "50d92e8eabe03ff923e404ab3afdc371", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    富士蓝               = EffectMeta("富士蓝", True, "7246720031118101816", "7246720031118101816", "ca146f44fb50a5c1335149b2c1bd0079", [])
    富士蓝II             = EffectMeta("富士蓝II", True, "7226994246471945530", "7226994246471945530", "43bee1438c8372b1f4a8857650fab808", [])
    富士青               = EffectMeta("富士青", True, "7226994214029184313", "7226994214029184313", "77bfdff2d848539626acd538429cc660", [])
    富春山居             = EffectMeta("富春山居", True, "7208496124779302177", "7208496124779302177", "f5ef0379f91fb0004e2886a3bef4e9ce", [])
    小美好               = EffectMeta("小美好", True, "7468493795479276835", "7468493795479276835", "7d678f329443e66ad181f12a46e2df8c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    小麦色               = EffectMeta("小麦色", True, "7362076973981584691", "7362076973981584691", "ea639b8e75457d08c026eb753f8704e5", [])
    尘杏                 = EffectMeta("尘杏", True, "7131630640646081822", "7131630640646081822", "653c8a4ffafe89ec8a1b2ac30a8b249e", [])
    尘烟                 = EffectMeta("尘烟", True, "7148958479326153991", "7148958479326153991", "946cbb3cd0096e46d11cd91630bcd1bc", [])
    山晴                 = EffectMeta("山晴", True, "7246723856222719269", "7246723856222719269", "acbd5fdb5b04114a6eedffdf716ed6b3", [])
    山本                 = EffectMeta("山本", True, "7156638423191784735", "7156638423191784735", "2516de8cc9f3c5ba7e3d02cc9b7a709e", [])
    岚夏                 = EffectMeta("岚夏", True, "7260771472107441471", "7260771472107441471", "5d9760bfa20e1745f2da9d0dddc1f8f3", [])
    岩灰                 = EffectMeta("岩灰", True, "7221472488079904060", "7221472488079904060", "fdd078505b4a102962d962cf461e9544", [])
    川秋                 = EffectMeta("川秋", True, "7428504360910376229", "7428504360910376229", "4909c43172d4aa6a3557317390a6cb5c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    川野                 = EffectMeta("川野", True, "7361032844484857142", "7361032844484857142", "59694a68c2ed99fd1822b9d728532d51", [])
    市井                 = EffectMeta("市井", True, "7145394707156323591", "7145394707156323591", "3135422526252e5674d585a4d099dd97", [])
    幽海                 = EffectMeta("幽海", True, "7262350396566342975", "7262350396566342975", "280e721f50df8e0ee622da68f4879f91", [])
    底特律               = EffectMeta("底特律", True, "7336763348492553499", "7336763348492553499", "d1bcdfe293f329d701a0df1ef4ab5e16", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    庙会                 = EffectMeta("庙会", True, "7185309693131148555", "7185309693131148555", "e36b0d36967b31a89a953c35ca01e387", [])
    弥晖                 = EffectMeta("弥晖", True, "7148812815246134541", "7148812815246134541", "ad4ca90087a6855a24e76e5bc7bfcf66", [])
    彩光                 = EffectMeta("彩光", True, "7127824109093866760", "7127824109093866760", "0aeae3c00b2ff3d26f0bba78a0f0cda5", [])
    影部                 = EffectMeta("影部", True, "7168136171673963787", "7168136171673963787", "57ebfdd7bdad96f19879e1635d823fb8", [])
    往昔                 = EffectMeta("往昔", True, "7266322833800727844", "7266322833800727844", "9c2fecfb098b7fa06e47e95dbf2de4cb", [])
    徕卡I                = EffectMeta("徕卡I", True, "7268562944093408523", "7268562944093408523", "91730e54e94b7eeb40bcfbd8f7c9a3cf", [])
    徕卡II               = EffectMeta("徕卡II", True, "7268563047776587020", "7268563047776587020", "a75e26160d19e9db7d9be10f6e8056b7", [])
    徕卡Q2               = EffectMeta("徕卡Q2", True, "7500447762404724018", "7500447762404724018", "44b1d99f86da8399aeb745061acaf9b5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    心动夏               = EffectMeta("心动夏", True, "7261461692096220428", "7261461692096220428", "daffbda5fec8238d91024cb36610023d", [])
    忆山                 = EffectMeta("忆山", True, "7271278427309755688", "7271278427309755688", "919dd48c0590b884f6aabc4f46f63b3f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    忆时                 = EffectMeta("忆时", True, "7266325161433910591", "7266325161433910591", "606029f145342308907b3422f6c6872c", [])
    快照II               = EffectMeta("快照II", True, "7143760738765655310", "7143760738765655310", "94a1e1cdca9b003126ac25d1df655263", [])
    怀旧                 = EffectMeta("怀旧", True, "7494564488704806198", "7494564488704806198", "a20fb046d1381d7c948151543932f934", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    怦然心动             = EffectMeta("怦然心动", True, "7195889899738909990", "7195889899738909990", "48ce7e2b8db89c5f411f53d6d7750cb7", [])
    恍光                 = EffectMeta("恍光", True, "7237446176629345593", "7237446176629345593", "9c7e3ff19468cb967d0ff9b0d79ea23d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    情感故事电影         = EffectMeta("情感故事电影", True, "7509005376835079439", "7509005376835079439", "dcc9eccd46b98f0fcf40bfdee83940fe", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    情绪暗调             = EffectMeta("情绪暗调", True, "7398190560701386022", "7398190560701386022", "43202e6e7d8cffe88ce44627f4ef2e6f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    情辉                 = EffectMeta("情辉", True, "7329826553477565705", "7329826553477565705", "50b73c148b43973bedc2e6168a1638f5", [])
    慕斯                 = EffectMeta("慕斯", True, "7261185427703418169", "7261185427703418169", "038504b6474c25b4ce735d1d165c4198", [])
    扬帆远航             = EffectMeta("扬帆远航", True, "7487297020743404810", "7487297020743404810", "805da3fa2ca3e11f631e4b4534d3230c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    拐杖糖               = EffectMeta("拐杖糖", True, "7175093825659079991", "7175093825659079991", "de11b072c9e793ee23a87de1f7265880", [])
    捕风                 = EffectMeta("捕风", True, "7248566556593098024", "7248566556593098024", "2ebec31165718f44bbd2ecbc338c175a", [])
    摩登                 = EffectMeta("摩登", True, "7131219052021779719", "7131219052021779719", "178dab15fb53b396f20c89ccaec799a2", [])
    摩登暗银             = EffectMeta("摩登暗银", True, "7508033223973244187", "7508033223973244187", "a2924b52e3cb502e0e39827a62f6397a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    撕拉拍立得           = EffectMeta("撕拉拍立得", True, "7502647335218941220", "7502647335218941220", "604d0b6a7b3b23a0169e1dfd38deccba", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    攀岩                 = EffectMeta("攀岩", True, "7195930274918567180", "7195930274918567180", "928cb605e08b3e72110837d55afaa9d9", [])
    文艺少女             = EffectMeta("文艺少女", True, "7409360036096527670", "7409360036096527670", "4e871014a6115b63b432b99e127bcfef", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    新中式电影感         = EffectMeta("新中式电影感", True, "7493945636518104360", "7493945636518104360", "ea98a825bea08eae7b908e111bb6b428", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    新宿                 = EffectMeta("新宿", True, "7210646550974876984", "7210646550974876984", "1bb8524cde9b57773015e98ba17e0f7d", [])
    新年欢愉             = EffectMeta("新年欢愉", True, "7452802706139352370", "7452802706139352370", "8681ba97d1c52b8bf7cd6bf46d4eb340", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    新年祈愿             = EffectMeta("新年祈愿", True, "7449639935717559561", "7449639935717559561", "6fdd51986e85a150f9f888ff55a8b774", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    新年祈福             = EffectMeta("新年祈福", True, "7457598693915594025", "7457598693915594025", "1f14f122c962e65f7b3f775f171beec9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    新年粉肤             = EffectMeta("新年粉肤", True, "7449579862496431375", "7449579862496431375", "739bf508ebc8e84eae2359c9204826f8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    新年红               = EffectMeta("新年红", True, "7449639891694112010", "7449639891694112010", "1f4ee7c68ba5b40b13598d2688815c01", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    新年闪胶             = EffectMeta("新年闪胶", True, "7451471584533040395", "7451471584533040395", "f6c5902324dbe52306a59aff02876ceb", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    日与                 = EffectMeta("日与", True, "7343499312464137535", "7343499312464137535", "3f290f1ae811a241efaa987e21ea1419", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    日光吻               = EffectMeta("日光吻", True, "7226985203540053305", "7226985203540053305", "12c40e5f562e2f080e7ae157b1b925a8", [])
    日光肤               = EffectMeta("日光肤", True, "7486736825369840907", "7486736825369840907", "b60fec77dace518d22dba94a8b695407", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    日出增色             = EffectMeta("日出增色", True, "7526422478206356787", "7526422478206356787", "6074c700577f7d04bf32f6a92b48d7b9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    日和                 = EffectMeta("日和", True, "7338311462277991718", "7338311462277991718", "70b43e53688e11ab0f849a5768cf6f6f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    日料寿司             = EffectMeta("日料寿司", True, "7507632191380229402", "7507632191380229402", "60cddb5817475d59ae022444a47f5e7e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    日漫增色             = EffectMeta("日漫增色", True, "7493804773515316491", "7493804773515316491", "1e99ad9eaf4572e8a813993ed7971466", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    日系增色             = EffectMeta("日系增色", True, "7472373777469328667", "7472373777469328667", "edf1bd45853137dfc8d34657839b082f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    日系春和             = EffectMeta("日系春和", True, "7473805992308837659", "7473805992308837659", "345cff234af4dc0b6c906d8def6b11c6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    日落时刻             = EffectMeta("日落时刻", True, "7496524092779105551", "7496524092779105551", "c2e34cb2efeb788a5899bfffb6989ac8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    旧时代II             = EffectMeta("旧时代II", True, "7232217903536409893", "7232217903536409893", "779a72d4b71cd42f470008749a165d93", [])
    旧时来信             = EffectMeta("旧时来信", True, "7366562830486621459", "7366562830486621459", "1680dbb9fafa20e0a3c81e56b038508f", [])
    旧曲                 = EffectMeta("旧曲", True, "7266320092386938124", "7266320092386938124", "d95b63cc01d7d71f705b7a22861bbe08", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    旧金山               = EffectMeta("旧金山", True, "7159161900389977382", "7159161900389977382", "22f238fa32975ad165c124316008ab31", [])
    旷野                 = EffectMeta("旷野", True, "7275698024892943655", "7275698024892943655", "5d52166c545e774971e36e50cb218f04", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    旷野自然             = EffectMeta("旷野自然", True, "7501717343156981046", "7501717343156981046", "1322b0aef7226539eb2a3cead86fa495", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    旷野蓝               = EffectMeta("旷野蓝", True, "7131513310733765918", "7131513310733765918", "afa609a1dc4092fbb0eeb87363894c76", [])
    明亮春味             = EffectMeta("明亮春味", True, "7485240505257807138", "7485240505257807138", "bfb5aa3c2feef58512926f11c85cab93", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    明亮焕晴             = EffectMeta("明亮焕晴", True, "7470840671763565864", "7470840671763565864", "2de92eefc7b02e03fef523e65677073d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    明媚春景             = EffectMeta("明媚春景", True, "7482055184554806566", "7482055184554806566", "377e50499a9d84cd54bf6f326941f492", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    明媚自然             = EffectMeta("明媚自然", True, "7480823852470177034", "7480823852470177034", "5142e281e72f62ec65c1a801e0b88371", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    明媚透亮             = EffectMeta("明媚透亮", True, "7506413750665121060", "7506413750665121060", "707fbbec9a4b7a298c65151f73bbbdd5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    明煦                 = EffectMeta("明煦", True, "7343287054228327691", "7343287054228327691", "07ce35eb05d047fd0eccbc6b6c5a1d78", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    星沫                 = EffectMeta("星沫", True, "7196921394163141946", "7196921394163141946", "0f2a9922d473d11ef83991e93c8dd76f", [])
    春和                 = EffectMeta("春和", True, "7327596304173944127", "7327596304173944127", "dc13ebbcf22161cf0053e75c2d3b7f90", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春喜                 = EffectMeta("春喜", True, "7325335963318750515", "7325335963318750515", "fba27053f1a0a40cc1c97e91f61bdc19", [])
    春天淡彩             = EffectMeta("春天淡彩", True, "7479295356488977679", "7479295356488977679", "518c1fb623f3d4556e087e5f1d2b9b87", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春忆胶卷             = EffectMeta("春忆胶卷", True, "7483069698981104947", "7483069698981104947", "52c2d6550b16560a5b247db65e3c6b8b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春日序               = EffectMeta("春日序", True, "7477922252470652198", "7477922252470652198", "071a79fd559e4b05428cc4c83ac4c755", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春日樱               = EffectMeta("春日樱", True, "7493076668009958668", "7493076668009958668", "442fd0d11f067faeeb2c47e2500d30f7", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    春日清晰             = EffectMeta("春日清晰", True, "7477594530104085770", "7477594530104085770", "d19642d2f9573e92254abf9914e55ce7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春日清透             = EffectMeta("春日清透", True, "7485293187616066831", "7485293187616066831", "848bc05cfb1e5e7b9716ba47552407e8", [])
    春日美食III          = EffectMeta("春日美食III", True, "7486868815364492554", "7486868815364492554", "cb202891744256abbd40cfe028092216", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春日花间             = EffectMeta("春日花间", True, "7472064159065132325", "7472064159065132325", "59c64d43a532ecebca203a3e4f84b190", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春日韩胶             = EffectMeta("春日韩胶", True, "7481494936836197641", "7481494936836197641", "76e9e0b4346020ba2915cb56eecfcf64", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春桃肤               = EffectMeta("春桃肤", True, "7483917188638772517", "7483917188638772517", "23bead4c25fd90d46521297cc16c6bec", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春橙肤               = EffectMeta("春橙肤", True, "7481693425218194725", "7481693425218194725", "2198cca5453c2bdc16b9e61ac361619f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春游踏青             = EffectMeta("春游踏青", True, "7493581083628408102", "7493581083628408102", "234d177e20bb230887116e469115e40b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春澄                 = EffectMeta("春澄", True, "7332492044327243049", "7332492044327243049", "a316ade2301e4c7eec65c49eae5302b8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春风                 = EffectMeta("春风", True, "7148963827239963918", "7148963827239963918", "ae9468b81643a706f5cae5761eff19b8", [])
    昭和                 = EffectMeta("昭和", True, "7195780237790154042", "7195780237790154042", "211b05e6793f255052a1cc463864ed3d", [])
    晚宴                 = EffectMeta("晚宴", True, "7302041028205333786", "7302041028205333786", "af499ef2d522dda0857f2be9c7db00d0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晚晴                 = EffectMeta("晚晴", True, "7297143895408839947", "7297143895408839947", "987e48eb485c58a239d5d67d01b9c76a", [])
    晚柠                 = EffectMeta("晚柠", True, "7262634564428778752", "7262634564428778752", "b9058248c373fa4f49357e1c878ab6cb", [])
    晚樱                 = EffectMeta("晚樱", True, "7127609541839129886", "7127609541839129886", "c30e126bfe5accdb5902c5ba63c8579e", [])
    晚霞增色             = EffectMeta("晚霞增色", True, "7392898170524618023", "7392898170524618023", "ed6efd67ec78c21a530046b4a6cfbb66", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晨旭                 = EffectMeta("晨旭", True, "7279062968501832972", "7279062968501832972", "7450c20e328d6fc45b648d999806f2e8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    普林斯顿             = EffectMeta("普林斯顿", True, "7127615578705104135", "7127615578705104135", "ab9e14d92af596b94e91fd6253b510cd", [])
    晴天                 = EffectMeta("晴天", True, "7420253131079961868", "7420253131079961868", "df2d876976f447b305a67db1b43d070e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴天亮丽             = EffectMeta("晴天亮丽", True, "7454234032570764581", "7454234032570764581", "590feb6405078fdae397cc40bc72dd7c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴天增色             = EffectMeta("晴天增色", True, "7454234028141497610", "7454234028141497610", "a402e1fe28509c7046627674a1efabf8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴天灿烂             = EffectMeta("晴天灿烂 ", True, "7486890449207151891", "7486890449207151891", "a031700fb1a1b957e763b59c779db325", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴好假日             = EffectMeta("晴好假日", True, "7374709776623635724", "7374709776623635724", "9747e32d2ec1f251aee54d080ec5fc84", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴好风光             = EffectMeta("晴好风光", True, "7475397942715632922", "7475397942715632922", "026f69b8fbc1fedb3eb0939366c6617e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴春                 = EffectMeta("晴春", True, "7346542846863887635", "7346542846863887635", "ed510f73b526d21d1fcabfc410f664b8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴春奶蓝             = EffectMeta("晴春奶蓝", True, "7485769123176254770", "7485769123176254770", "16093c7dc49cdbf9fc2071831d96db5c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴朗                 = EffectMeta("晴朗", True, "7434746357233028390", "7434746357233028390", "c1298ed66eed37d0f9a1ad78fa7239ee", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴海                 = EffectMeta("晴海", True, "7525755037050539307", "7525755037050539307", "0e0a944fdee0ffede3163e628ae8f2e7", [])
    晴空漫游             = EffectMeta("晴空漫游", True, "7477810373060611338", "7477810373060611338", "37a68a5bac333f74da7afac747de12bd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴肤                 = EffectMeta("晴肤", True, "7365842976691604763", "7365842976691604763", "c3d640b01c7bb7f6ab7ebd598bf92811", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴谷                 = EffectMeta("晴谷", True, "7307191907514420491", "7307191907514420491", "2ad917b1c9f293648cf453201987fe5d", [])
    晴颜                 = EffectMeta("晴颜", True, "7468501080691789094", "7468501080691789094", "5714d281e174b0f66a0ccfb7745645ca", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晶透                 = EffectMeta("晶透", True, "7199095242476293435", "7199095242476293435", "17e30bbde014d6688a3b00203a7a8ea8", [])
    智能光线             = EffectMeta("智能光线", True, "7451897248885099795", "7451897248885099795", "79973825711b46f78f955ee564f2b122", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暖晨                 = EffectMeta("暖晨", True, "7312646382395936010", "7312646382395936010", "03737fce45a4ba22d225edbe7e36a04c", [])
    暖棕                 = EffectMeta("暖棕", True, "7405241190435523866", "7405241190435523866", "496fff58dbee33b2a2421403753f1f61", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暖黄                 = EffectMeta("暖黄", True, "7127830631601458440", "7127830631601458440", "7c7c4a40d7c44698a9db145eb8260156", [])
    暗光提亮             = EffectMeta("暗光提亮", True, "7446318175991368997", "7446318175991368997", "f85598ada312c86238f4402d075feb66", [])
    暗匣                 = EffectMeta("暗匣", True, "7159163878822153483", "7159163878822153483", "00729c25c8b262db946bb5ac80b8d1dc", [])
    暗夜明肤             = EffectMeta("暗夜明肤", True, "7328364126449765671", "7328364126449765671", "9fe0da0817604428adb38249ecae911c", [])
    暗影                 = EffectMeta("暗影", True, "7291203298630159676", "7291203298630159676", "21f3af497daf847e50efadc241f88a1a", [])
    暗曛                 = EffectMeta("暗曛", True, "7281163501047991608", "7281163501047991608", "893d483cd405343c9420015066e56096", [])
    暗调人像             = EffectMeta("暗调人像", True, "7485767950314655002", "7485767950314655002", "7100cf70453b486a99038971890c9411", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗调发光             = EffectMeta("暗调发光", True, "7413717074037525769", "7413717074037525769", "7607d3d95aa486b47b9245af5b59fc4a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗调古风             = EffectMeta("暗调古风", True, "7505272278574206219", "7505272278574206219", "113adc91ddc8eb89d24a1f353415a1b6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗调复古电影         = EffectMeta("暗调复古电影", True, "7494530599202327846", "7494530599202327846", "72f3b7b5cc1bc9a247025588e8815dfb", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗调电影             = EffectMeta("暗调电影", True, "7402945560623336758", "7402945560623336758", "bd89a7f21cb380fe362311146462d0fd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗调纪实电影         = EffectMeta("暗调纪实电影", True, "7493536391431785752", "7493536391431785752", "bc7a68297d80f6b3302e2826d66f67fe", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗金                 = EffectMeta("暗金", True, "7511619145864187136", "7511619145864187136", "725fc1d6b1623309eeee59015a5c6bdc", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗银                 = EffectMeta("暗银", True, "7177725752513793284", "7177725752513793284", "ad378d530ac056cb2b2e0b0ab171ede8", [])
    暗银II               = EffectMeta("暗银II", True, "7223630575888780602", "7223630575888780602", "33f209efb496924d6da0c7ad89bea81f", [])
    暮信                 = EffectMeta("暮信", True, "7279061785922080055", "7279061785922080055", "0635e0022bfbda491e52a8eef142b33d", [])
    暮川                 = EffectMeta("暮川", True, "7262351934785408267", "7262351934785408267", "187450ba96a5e11233e9d38396274d87", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暮樱                 = EffectMeta("暮樱", True, "7341257736983760182", "7341257736983760182", "470ab88faab84fe2c6de6300af28be5f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暮涛                 = EffectMeta("暮涛", True, "7145394582933572878", "7145394582933572878", "a4930081ec4b2a6fc96b85508cae899f", [])
    暮色约会             = EffectMeta("暮色约会", True, "7332396398157090089", "7332396398157090089", "920f4d54eb383be7327d76689d96f1a5", [])
    曼波                 = EffectMeta("曼波", True, "7233734975839898940", "7233734975839898940", "92b9d72c49094fa0280e1763b9002cac", [])
    月吟                 = EffectMeta("月吟", True, "7168108694285159719", "7168108694285159719", "98ee4013998d056bf434a4d2c62cf548", [])
    月辉                 = EffectMeta("月辉", True, "7476109983688576290", "7476109983688576290", "8cea6a07e5698d90c0d7ee40efee1f88", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    朦胧气质棕           = EffectMeta("朦胧气质棕", True, "7493920442613288219", "7493920442613288219", "43451fb4b7d714c1d835b9bd8f4254ec", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    木葵                 = EffectMeta("木葵", True, "7233731121610100020", "7233731121610100020", "424ca4570f07325b1124b3be3f7dd35f", [])
    末世天使             = EffectMeta("末世天使", True, "7506099780947430668", "7506099780947430668", "d7a4f329369b0f8232525d73bf9b9b91", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    杏铃                 = EffectMeta("杏铃", True, "7295630593063193865", "7295630593063193865", "2727cb3874cfcc3541fbf4f08052a6da", [])
    松绿                 = EffectMeta("松绿", True, "7246723559047941433", "7246723559047941433", "1aca4ded18b11bff899309955ed07c5c", [])
    果酥                 = EffectMeta("果酥", True, "7160594387594972446", "7160594387594972446", "f68ff633bab02132880a03034894d378", [])
    柔光                 = EffectMeta("柔光", True, "7395596262252334373", "7395596262252334373", "01d991f6057be53b6eb319f5c69a1798", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    柔焦                 = EffectMeta("柔焦", True, "7345412316621442354", "7345412316621442354", "e9449745f95a354e4d835961cbb0e674", [])
    柠檬海               = EffectMeta("柠檬海", True, "7258220845041061180", "7258220845041061180", "341ab073d16faca8edf318285dab36d9", [])
    柯达金200            = EffectMeta("柯达金200", True, "7517685395102977334", "7517685395102977334", "c28090d8f54cf11516c16126a0efb84d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    栖海                 = EffectMeta("栖海", True, "7349928965869538570", "7349928965869538570", "ef900ccea3b5ec0d5cb420b4ee487bcb", [])
    栩栩                 = EffectMeta("栩栩", True, "7177259623819316519", "7177259623819316519", "09c34a30d79f4c7332267b16eaca664e", [])
    格金                 = EffectMeta("格金", True, "7348301778909252879", "7348301778909252879", "256144ddabaf723badea240301660868", [])
    桃木                 = EffectMeta("桃木", True, "7252673818035064124", "7252673818035064124", "7e5d4fb53f764eaa07d6e465fd60588e", [])
    桃粉                 = EffectMeta("桃粉", True, "7297131749346135331", "7297131749346135331", "80b55b69c2b4662c65835f49ee46ad97", [])
    桃野                 = EffectMeta("桃野", True, "7199093989742562597", "7199093989742562597", "1a216be7e4423bb5962ff832faf45814", [])
    桐影                 = EffectMeta("桐影", True, "7275699191253339455", "7275699191253339455", "b77671ede2639384b704eb73722e928a", [])
    梦境                 = EffectMeta("梦境", True, "7127675251604917517", "7127675251604917517", "12627ad5e79adab77540c65ea8ee7cc2", [])
    梦幻夏               = EffectMeta("梦幻夏", True, "7377370067798985993", "7377370067798985993", "3adb502f6928cf41be040b6f52e1a48e", [])
    梦暮                 = EffectMeta("梦暮", True, "7272341241893768506", "7272341241893768506", "8d0fdc61596d3f60fa7f307241ea703b", [])
    梦核紫               = EffectMeta("梦核紫", True, "7261463763344248103", "7261463763344248103", "41ed7e729f06a288363ca93a928f8a90", [])
    棕榈                 = EffectMeta("棕榈", True, "7252676190073392444", "7252676190073392444", "113b463fa3945ef37700c7c52dfc6bb9", [])
    森山                 = EffectMeta("森山", True, "7242215081663008056", "7242215081663008056", "0dc17be521cf783590bebcf2a5c888df", [])
    森林徒步             = EffectMeta("森林徒步", True, "7524262165273005321", "7524262165273005321", "c889505e8e46aaeaa48f792c770ec042", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    森秋                 = EffectMeta("森秋", True, "7274575376095923497", "7274575376095923497", "b055e64a58bd8d9b882477c9be6ef3a6", [])
    森绿                 = EffectMeta("森绿", True, "7510128089511349555", "7510128089511349555", "992abfe865ee701777a6cccdf033dc2b", [])
    榄白                 = EffectMeta("榄白", True, "7169350167903112451", "7169350167903112451", "6068c4a2ea7f0854027347a938115dae", [])
    模糊氛围             = EffectMeta("模糊氛围", True, "7398486193924623628", "7398486193924623628", "103608c9a5a16edf4b9bba541db8324e", [])
    樱花粉肤             = EffectMeta("樱花粉肤", True, "7467985496988241204", "7467985496988241204", "01a1557eeb00bf1f68755765e18b4281", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    橘子海               = EffectMeta("橘子海", True, "7526948433597336832", "7526948433597336832", "823f1fb8e26bb8ee1406b027f30ac446", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    橘海                 = EffectMeta("橘海", True, "7278615838628924733", "7278615838628924733", "2c1496f259e375191ad52c8c43c6cf2f", [])
    橙蓝                 = EffectMeta("橙蓝", True, "7127561047048850718", "7127561047048850718", "4dd590015f2e14265dd5456a91ec86a6", [])
    欧若淡彩             = EffectMeta("欧若淡彩", True, "7479295334930205952", "7479295334930205952", "c188665c6348ae65e32b6e70a691151b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    毕业胶片             = EffectMeta("毕业胶片", True, "7510863205011393844", "7510863205011393844", "a064e9e21ae3fb3664c66b857d792902", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    气色                 = EffectMeta("气色", True, "7417468417852099894", "7417468417852099894", "8c94ade25035fdc85d27cb49ff9c85ef", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    气色透亮             = EffectMeta("气色透亮", True, "7527311213869403402", "7527311213869403402", "e87f59cca325712c1302c250448387ef", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    氧气甜白             = EffectMeta("氧气甜白", True, "7470913918186163468", "7470913918186163468", "d83fe74d8abe64f7bb31e01dc17ab59a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    氧气自然             = EffectMeta("氧气自然", True, "7501345307830013222", "7501345307830013222", "ddd0973ffc24018949081cbb922f8618", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    水泽                 = EffectMeta("水泽", True, "7210613511133646135", "7210613511133646135", "ae8b8e426b2c3fa77d2bc8db2f8bfb7b", [])
    沙漫                 = EffectMeta("沙漫", True, "7148776798715776292", "7148776798715776292", "b6a48f6276a19984c0e466362bcd0999", [])
    沙砾                 = EffectMeta("沙砾", True, "7160580722774920461", "7160580722774920461", "a796471629be7b3bfbd649deafca3ddb", [])
    法式少女             = EffectMeta("法式少女", True, "7480196177611230514", "7480196177611230514", "fcbe6cb7764d3023cd221aaecfdc7d8d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    法式甜粉             = EffectMeta("法式甜粉", True, "7480196167372999973", "7480196167372999973", "418873710a7304cc284104bd32eed187", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    法餐                 = EffectMeta("法餐", True, "7127655700532186398", "7127655700532186398", "b8b6d5ae88e12e25be14a2dd85b7cbc6", [])
    洛丽塔粉             = EffectMeta("洛丽塔粉", True, "7476109684169133362", "7476109684169133362", "cb02e21da652aa4dabd912a8b009df89", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    浅茶                 = EffectMeta("浅茶", True, "7221481120083283257", "7221481120083283257", "6acf81ddf75fc8c5ddb20f3a927dcaa3", [])
    浅草                 = EffectMeta("浅草", True, "7195783041376111932", "7195783041376111932", "8c4eb75992a7f07bd07e56c16b388d87", [])
    浓郁胶卷             = EffectMeta("浓郁胶卷", True, "7499121362351574282", "7499121362351574282", "ed6846e943d41e7776b9cfddbb1f0ce6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    浪语                 = EffectMeta("浪语", True, "7376495406487801139", "7376495406487801139", "3310cabac6dabcb702b1c7ec26831462", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    海上冲浪             = EffectMeta("海上冲浪", True, "7527721135824211243", "7527721135824211243", "ad7160ce93edefe64d911dcd42ead464", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    海松                 = EffectMeta("海松", True, "7145394304377163045", "7145394304377163045", "d94890916054949103ba41e9eb36e948", [])
    海水正蓝             = EffectMeta("海水正蓝", True, "7494117715142053130", "7494117715142053130", "5be967f1fc854f15d22c5103fcb43a3a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    海湾                 = EffectMeta("海湾", True, "7210611719180193083", "7210611719180193083", "98c3ab54b9c3903f2d9edec90ad90766", [])
    海盐                 = EffectMeta("海盐", True, "7473034636436852031", "7473034636436852031", "91b796a25fbca315800d4db4c4f4081e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    海盐夏日             = EffectMeta("海盐夏日", True, "7501729703544343820", "7501729703544343820", "34123fa8c0f71091c32795ae337f415d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    海盐蓝               = EffectMeta("海盐蓝", True, "7495702685765651775", "7495702685765651775", "bb5eaf7e5063d853dc0392bb7119c74e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    海边胶片             = EffectMeta("海边胶片", True, "7497887075627257114", "7497887075627257114", "05404c80bc61b9cd92805e6016579607", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    润光                 = EffectMeta("润光", True, "7199093300526173501", "7199093300526173501", "3916e1d5dc3a3522f4b883c3b1f2b43a", [])
    润白                 = EffectMeta("润白", True, "7366518614729493799", "7366518614729493799", "1686ce704f4899b9e9a1e42693f24037", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    涩谷                 = EffectMeta("涩谷", True, "7210645355136961852", "7210645355136961852", "7ca84443c2a14a2e9de11a5708a62a63", [])
    淡奶油               = EffectMeta("淡奶油", True, "7127668617101020423", "7127668617101020423", "e53103dabd1bbb6ab4481b18a4c42b2c", [])
    清冷国风             = EffectMeta("清冷国风", True, "7493171130753174835", "7493171130753174835", "7d053e14ed86f5176b46c2c9408ccd90", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清冷暗黑             = EffectMeta("清冷暗黑", True, "7398191077364124955", "7398191077364124955", "ad3d3e686cc83a8d59b097e11da88fec", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新度假             = EffectMeta("清新度假", True, "7503785630606904630", "7503785630606904630", "266afa90af699388a2c3fdb19d754cf5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新感               = EffectMeta("清新感", True, "7493819626330017078", "7493819626330017078", "35d73b32f29b709f39544491ede0838a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新明亮             = EffectMeta("清新明亮", True, "7429759193361435955", "7429759193361435955", "7bc0e54281c36e6de77a5615f27c4caa", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新春日             = EffectMeta("清新春日", True, "7463798716542111030", "7463798716542111030", "a1d039f3590e2adf5da1004cc2d73eda", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新晴空             = EffectMeta("清新晴空", True, "7456482453444726026", "7456482453444726026", "07019cfc5d2c3256ba47bf3bea3dbb00", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新暖食             = EffectMeta("清新暖食", True, "7481862972801879346", "7481862972801879346", "36c030d9a1c8557e81848189cc1af755", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新氧晴             = EffectMeta("清新氧晴", True, "7459675263652220171", "7459675263652220171", "2b31c0d9bf2a405612888fcb3995f873", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新绿妍             = EffectMeta("清新绿妍", True, "7436078162217274687", "7436078162217274687", "112dd9649310ed413c7408dd8f2f92d0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新花妍             = EffectMeta("清新花妍", True, "7478775634630659378", "7478775634630659378", "a6ccdb6e981df85838d0f41c39465a68", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新质感             = EffectMeta("清新质感", True, "7456482275618835763", "7456482275618835763", "3b08d9fe88051cfafaa416a4c414d7d2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清新透亮             = EffectMeta("清新透亮", True, "7439995840799722815", "7439995840799722815", "65bb0c559415d970de0bfc05ae12dcb0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰                 = EffectMeta("清晰", True, "7447719105563610404", "7447719105563610404", "5f6d758ab20aa947bba241a6b76b85b2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰严冬             = EffectMeta("清晰严冬", True, "7449939197223243058", "7449939197223243058", "d9d8276e9a3c42cfd6fc7f4ca7a4df81", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰净透             = EffectMeta("清晰净透", True, "7483183184826420519", "7483183184826420519", "8a899113236afdc2c594847f2f6f47a7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰增强             = EffectMeta("清晰增强", True, "7436068361622129929", "7436068361622129929", "04d65d54d326cdac7199f22fcb568546", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰增色             = EffectMeta("清晰增色", True, "7428650549572144411", "7428650549572144411", "70ba95840a5098b3da9177f37d833e3e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰增质             = EffectMeta("清晰增质", True, "7441960726274559282", "7441960726274559282", "b34ce1dffbe825638afca51c302d1e73", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰提升             = EffectMeta("清晰提升", True, "7443101069539953931", "7443101069539953931", "c3d50db262018318dffa816fb21a538b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰电影             = EffectMeta("清晰电影", True, "7435151579029769511", "7435151579029769511", "917f37af833a8ff548f59c513140f62c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰画质             = EffectMeta("清晰画质", True, "7441541255760284939", "7441541255760284939", "9f05ff28c43c9e08a23a0ad7e00783d2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰绿妍             = EffectMeta("清晰绿妍", True, "7494607226519260442", "7494607226519260442", "03691f968027b37c11855d789231cec5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰自然             = EffectMeta("清晰自然", True, "7473805985388317978", "7473805985388317978", "3e1cc9a595ff0c720a894699eb20a9d5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰花朵             = EffectMeta("清晰花朵", True, "7493197626645531928", "7493197626645531928", "dad9279c9aca95f1691b257001998384", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰萌宠             = EffectMeta("清晰萌宠", True, "7503810545670311206", "7503810545670311206", "aa7df625b33d7e1a71b8a631f774b14e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰质感             = EffectMeta("清晰质感", True, "7442390492307836186", "7442390492307836186", "92dd44e1cf31d63da9de52e93f0f9bb1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰透亮             = EffectMeta("清晰透亮", True, "7440517981374893327", "7440517981374893327", "142da1059c48af1f07e00b4e2d589545", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清爽                 = EffectMeta("清爽", True, "7392897785755897100", "7392897785755897100", "c012321a086ec42b7570338f557a713e", [])
    清爽夏颜             = EffectMeta("清爽夏颜", True, "7499484084197018889", "7499484084197018889", "62828fb39511d31fec4b3dacf2861925", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清透光感             = EffectMeta("清透光感", True, "7493540929874218281", "7493540929874218281", "5f5104a97960ff734ecef9eb568c5627", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清透感               = EffectMeta("清透感", True, "7496156231392873767", "7496156231392873767", "b2398ecc78f2a553abf3aa1f6b6e0fbc", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清透美食             = EffectMeta("清透美食", True, "7403664041945681191", "7403664041945681191", "3121bd38673441c5417ec3e6f0da13a2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清透萌宠             = EffectMeta("清透萌宠", True, "7473126624322391308", "7473126624322391308", "65f21eb6f46b4bc1620c3b942ccecadc", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清风绿妍             = EffectMeta("清风绿妍", True, "7486694625009339689", "7486694625009339689", "9e9143be40f46c6208dc96c55574e623", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    港风复古             = EffectMeta("港风复古", True, "7493874443639377164", "7493874443639377164", "c11f61a31f6ee77e6ca00916255a8395", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    港风夜景             = EffectMeta("港风夜景", True, "7408952560549104923", "7408952560549104923", "5ae3b44614fecb8e1e404bea862e3831", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    港风电影             = EffectMeta("港风电影", True, "7493845947546455307", "7493845947546455307", "d64afc32204dd52601a74a7a82dda04e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    漠土                 = EffectMeta("漠土", True, "7347670931646549282", "7347670931646549282", "9dfde36f1fab0e85773d04fadeb30650", [])
    漫樱                 = EffectMeta("漫樱", True, "7356883843376221475", "7356883843376221475", "1799ab3b4a9bf0957995b69d27195229", [])
    漫空                 = EffectMeta("漫空", True, "7210749292888280359", "7210749292888280359", "cd88f8152fffe8033bb5057fc2539319", [])
    漫荫                 = EffectMeta("漫荫", True, "7210758351595048195", "7210758351595048195", "fc46efdc25a15ca3958126a8c72c1cd8", [])
    漱石                 = EffectMeta("漱石", True, "7145394477249678606", "7145394477249678606", "ac50156682af7d7ce4e76eb731a5a832", [])
    潘多拉               = EffectMeta("潘多拉", True, "7127620215290039566", "7127620215290039566", "36e7d537966ee59eb61c326598546cb0", [])
    灯会                 = EffectMeta("灯会", True, "7145394908608662814", "7145394908608662814", "21472133401674a3e5645f79e9d30ae9", [])
    灯塔                 = EffectMeta("灯塔", True, "7262351970193640715", "7262351970193640715", "1a07b83501e168fa1d630a0d7891ce47", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    灰芋                 = EffectMeta("灰芋", True, "7199460195502689574", "7199460195502689574", "96b986718efbb22647ae5836b2c8ff43", [])
    灰调中性             = EffectMeta("灰调中性", True, "7476126948708617482", "7476126948708617482", "0ad9b7ad4e7e37fd3d9db635919c96be", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    灰调日常             = EffectMeta("灰调日常", True, "7484662695443090715", "7484662695443090715", "775159063b0b80ee165739845dd1813c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    灰麻                 = EffectMeta("灰麻", True, "7312645421271158070", "7312645421271158070", "38ff7fc68c3ad9d76d9527a6d0b560cb", [])
    灿金彩带             = EffectMeta("灿金彩带", True, "7467879231914118412", "7467879231914118412", "6616e3a1d378a44ed14ea50d8d25ca67", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    炊烟                 = EffectMeta("炊烟", True, "7194083900333755704", "7194083900333755704", "924d2235bf0485217a6897fb9504b456", [])
    烈日                 = EffectMeta("烈日", True, "7145395383475113230", "7145395383475113230", "cc04d06002980d31b709b833290441b2", [])
    烈空                 = EffectMeta("烈空", True, "7246722333010824508", "7246722333010824508", "849e979a487594a0da039ddd33e43c6b", [])
    烘挞                 = EffectMeta("烘挞", True, "7160598329817091364", "7160598329817091364", "8df6f056381a16178b36fa8ad6e559bf", [])
    烟橙                 = EffectMeta("烟橙", True, "7131582482608164132", "7131582482608164132", "e958619538087c86308f718045b292f2", [])
    烟花璀璨             = EffectMeta("烟花璀璨", True, "7328363415313993001", "7328363415313993001", "0d2282c9172ed09758f861849916ab4b", [])
    热带季风             = EffectMeta("热带季风", True, "7377368986276646171", "7377368986276646171", "2879146129f3375e8fefc940fe970397", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    热气腾腾             = EffectMeta("热气腾腾", True, "7463372376038755603", "7463372376038755603", "7512302ec39fcf1c3fe8eb3d88015094", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    热红酒               = EffectMeta("热红酒", True, "7447164085122256143", "7447164085122256143", "157ee7ccdd413e211df98ec989b9fac9", [])
    焕肤                 = EffectMeta("焕肤", True, "7127674287238008078", "7127674287238008078", "073940956259c1077acaec764f52f31c", [])
    焰色                 = EffectMeta("焰色", True, "7131539023817936158", "7131539023817936158", "efcc2f7cdccc176ce06f14d9029bcbf2", [])
    熏柏                 = EffectMeta("熏柏", True, "7145395127089909028", "7145395127089909028", "1081c5bbbf4ed18971b14f24316d1905", [])
    爱丽丝               = EffectMeta("爱丽丝", True, "7328694736565439807", "7328694736565439807", "deae47ffa17d61be87aabf804cea348c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    爱之城               = EffectMeta("爱之城", True, "7131656881805741325", "7131656881805741325", "3531cd81550d23dd7d10b4b8ec90ba9f", [])
    爱之城II             = EffectMeta("爱之城II", True, "7337929076042222899", "7337929076042222899", "1635b6718619a9832177e25c33f1968b", [])
    牙白                 = EffectMeta("牙白", True, "7172285234296278309", "7172285234296278309", "1c6bd0a57d892c86c845666b44a8f547", [])
    牛奶肌               = EffectMeta("牛奶肌", True, "7473369111490317595", "7473369111490317595", "330d7a689e6be431555bbfdb79c40222", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    牧野                 = EffectMeta("牧野", True, "7397751642390564134", "7397751642390564134", "9c3719579cfc7ed5c7b1cfb64f83e78e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    独行侠               = EffectMeta("独行侠", True, "7202485617026977056", "7202485617026977056", "50fc4f48bab6acc0b86f42c68a44e3dc", [])
    猎梦                 = EffectMeta("猎梦", True, "7148806074601164062", "7148806074601164062", "29250207ce609f25ddaad4a5ff618515", [])
    玄影灵               = EffectMeta("玄影灵", True, "7405509975939894567", "7405509975939894567", "32ec94003ae4974d96d095884f512660", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    玩趣                 = EffectMeta("玩趣", True, "7177267248753610023", "7177267248753610023", "3dd9c3beaf276b96f226c49ac2bcbdd0", [])
    琥珀                 = EffectMeta("琥珀", True, "7295599414180138250", "7295599414180138250", "4a9ef682fbe7b4214e681796d4b4c77d", [])
    璀璨                 = EffectMeta("璀璨", True, "7468943213143821587", "7468943213143821587", "da0d70b6d9194b356f971b8fcdaad992", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    甜妹感               = EffectMeta("甜妹感", True, "7486871767642950966", "7486871767642950966", "7eede1d6b72f5c5a56c0a2fc14397ad6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    甜心芭比             = EffectMeta("甜心芭比", True, "7505303260148878630", "7505303260148878630", "2ea342e24a99ce386418d5cb214ce807", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    田园野餐             = EffectMeta("田园野餐", True, "7374709634088668452", "7374709634088668452", "e7d118f203092058bd662381cd81854f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    电影增强             = EffectMeta("电影增强", True, "7439365849703550247", "7439365849703550247", "61b80862b0f2f60fb42dbf3974ccbcdc", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    电影增质             = EffectMeta("电影增质", True, "7435151398783765799", "7435151398783765799", "41a4b54d9a3918e6466be755a455667e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    电影感增强           = EffectMeta("电影感增强", True, "7486832436819578151", "7486832436819578151", "4c90165bf74665c89b9eba6408ef3bba", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    电影柔光             = EffectMeta("电影柔光", True, "7447126702137904420", "7447126702137904420", "8bc2fa65718e78742c45e937ee513599", [
                              EffectParam("intensity", 0.180, 0.000, 1.000)])
    """参数:
    intensity: 默认18%, 0% ~ 100%"""
    电影校正             = EffectMeta("电影校正", True, "7494169971136711977", "7494169971136711977", "8a967a661c33955a914ee2d6741f4abe", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    电影画质             = EffectMeta("电影画质", True, "7472770427245448474", "7472770427245448474", "3c17e8775c8ffd2f8875c1b06720a81d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    电影雪肤             = EffectMeta("电影雪肤", True, "7441124730066701604", "7441124730066701604", "39c3b6b1424f1a66e9a1d424f5623283", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    画报                 = EffectMeta("画报", True, "7239979137404833083", "7239979137404833083", "267ef83e978e1b8282afa81c88e8dfd4", [])
    画质修复             = EffectMeta("画质修复", True, "7507148382536764682", "7507148382536764682", "8839ae43389b979ea5b3af0210940455", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    画质高清             = EffectMeta("画质高清", True, "7439560136630471963", "7439560136630471963", "b08bde10ef963cf648e677615667fda3", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    登高                 = EffectMeta("登高", True, "7195925533031435558", "7195925533031435558", "688df92b416581b9cf33e543ae7ae03b", [])
    白富美               = EffectMeta("白富美", True, "7302336985513970963", "7302336985513970963", "9fb4286e708d3bbf2b6bc6af85120be2", [])
    白桃                 = EffectMeta("白桃", True, "7300522962937990415", "7300522962937990415", "2c277b4b642fa2a5d7ddd7bff681ff91", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    白皙                 = EffectMeta("白皙", True, "7524363630498827530", "7524363630498827530", "f534e97ffd440e75902dda9f72dcf132", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    百川                 = EffectMeta("百川", True, "7210616269597314362", "7210616269597314362", "cd1f1360bd1891f9b31c63542689d8ea", [])
    盐系                 = EffectMeta("盐系", True, "7127823742830398757", "7127823742830398757", "9d48681f2c1f584e9b93fa37485693d1", [])
    盐系清透             = EffectMeta("盐系清透", True, "7500997115917651227", "7500997115917651227", "7b5501b506c712a2567eefd55551c165", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    石山                 = EffectMeta("石山", True, "7194091413728922941", "7194091413728922941", "a9faf4808c5ec06b8d2ecc944a3682c6", [])
    砂金                 = EffectMeta("砂金", True, "7131655685321821477", "7131655685321821477", "9a4836294cf0cc48fcf84af02d963400", [])
    破晓                 = EffectMeta("破晓", True, "7348707347419712794", "7348707347419712794", "0f73c6cf0189f4c0e462e76102e46084", [])
    硬朗                 = EffectMeta("硬朗", True, "7127663097162075399", "7127663097162075399", "7f33d22c16b09c852f48314404c2b532", [])
    硬朗男孩             = EffectMeta("硬朗男孩", True, "7524592387742567689", "7524592387742567689", "b998c48b7bc0927ba03a6a0c866fa2d8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    碎芒                 = EffectMeta("碎芒", True, "7148945136280440101", "7148945136280440101", "c40eb1ab380e7e22f5a4a71d69520a54", [])
    碳烤                 = EffectMeta("碳烤", True, "7363537225620983067", "7363537225620983067", "596d7d07b942eff22e9f8aaa47918711", [])
    福桔                 = EffectMeta("福桔", True, "7323020458050260262", "7323020458050260262", "e0d586addaf8f3b790f011effa361c80", [])
    福运                 = EffectMeta("福运", True, "7453122471810714930", "7453122471810714930", "a6ec7e80c2ecff207da782397d0f9068", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    禾美                 = EffectMeta("禾美", True, "7260770496055168310", "7260770496055168310", "fce7d45ba040a90176adfc1cc74fb8be", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    私语                 = EffectMeta("私语", True, "7127674303306419464", "7127674303306419464", "7f8596dc2626cd91e642c6a17c953390", [])
    秋日物语II           = EffectMeta("秋日物语II", True, "7404121905780772122", "7404121905780772122", "1d70b53cb9e08dd8e5205d1f8d9258b1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    秋池                 = EffectMeta("秋池", True, "7145391965717253406", "7145391965717253406", "3a908de0c7ba051b7838f5515d523a2c", [])
    秋波                 = EffectMeta("秋波", True, "7196920471043050812", "7196920471043050812", "0ce8c8224ab832699cae7ebdbd7034e9", [])
    秋田胶片             = EffectMeta("秋田胶片", True, "7493760868576988443", "7493760868576988443", "6ebf281ef0ce140be9ea39457209139a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    科切拉               = EffectMeta("科切拉", True, "7502329862581996854", "7502329862581996854", "ea0880ddab806d8765dce61edba72dbc", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    科幻星球             = EffectMeta("科幻星球", True, "7501988309900528935", "7501988309900528935", "5d48a663f0d44ab86af1a5a48a7ac974", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    简餐                 = EffectMeta("简餐", True, "7127561998556073247", "7127561998556073247", "0c4b5c50cb8bd668c241a262984f940b", [])
    粉柔撕拉片           = EffectMeta("粉柔撕拉片", True, "7503540725334723875", "7503540725334723875", "22bc2bf6c87fab59f75217cd83c21eae", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    粉橘                 = EffectMeta("粉橘", True, "7131467442789846285", "7131467442789846285", "1fc9df6984d15546e3d28689ef43c334", [])
    粉白                 = EffectMeta("粉白", True, "7156647258342034702", "7156647258342034702", "fd5f2b2a42b0c54aa8df8b99c830ab36", [])
    粉白微曝光           = EffectMeta("粉白微曝光", True, "7481194247610174757", "7481194247610174757", "14b4910ed81667464beb2264bd80ae2a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    粉蓝烟花             = EffectMeta("粉蓝烟花", True, "7462636960557927699", "7462636960557927699", "92e7bc7ca6f8381bdf25c4540669f28b", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    素净                 = EffectMeta("素净", True, "7351018816215764233", "7351018816215764233", "3c792ad3327a3b6774aa89990dacf093", [])
    素简                 = EffectMeta("素简", True, "7300968790391606567", "7300968790391606567", "091f103fae7c3a0480f05be172a0c904", [])
    紫霞时分             = EffectMeta("紫霞时分", True, "7507920355613248803", "7507920355613248803", "0666e85ae9821a1ba83106da65094df9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    繁花似锦             = EffectMeta("繁花似锦", True, "7322666518536359204", "7322666518536359204", "f5d1f324f0f06bf4fc783095efd7dc1e", [])
    繁花如梦             = EffectMeta("繁花如梦", True, "7322665314980859177", "7322665314980859177", "d8bcaf063ca3ef2cd8d5f1642204a35f", [])
    繁花璀璨             = EffectMeta("繁花璀璨", True, "7322665617373351231", "7322665617373351231", "98b0d8c15909c10ef71f187df3e36c9f", [])
    红运                 = EffectMeta("红运", True, "7325421708809096467", "7325421708809096467", "31a7c3905e75dda75c86e104dcb5d222", [])
    纪实电影             = EffectMeta("纪实电影", True, "7493535052098358590", "7493535052098358590", "6270a0d32e121f2f157428a8fa71baf1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    纪实电影胶片         = EffectMeta("纪实电影胶片", True, "7501954865518677267", "7501954865518677267", "8276d9650078c937901324127c6a2733", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    纱雾                 = EffectMeta("纱雾", True, "7260772961462799627", "7260772961462799627", "acde0ae9bd3ee0a6684457d562f35e25", [])
    织乐                 = EffectMeta("织乐", True, "7148965677376736542", "7148965677376736542", "a319e3016fe180b247add4a6898b3cd0", [])
    经典港风             = EffectMeta("经典港风", True, "7449048410004507914", "7449048410004507914", "c0bedd6c0adf9e2be04aceb386d79ef3", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    绮思                 = EffectMeta("绮思", True, "7148796681176288548", "7148796681176288548", "d48bab64f2d456f4e5f577220fddd1a1", [])
    绿妍II               = EffectMeta("绿妍II", True, "7361401117672066345", "7361401117672066345", "2f29b2a050dc8c75c742e1ffb7be4cf0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    绿野                 = EffectMeta("绿野", True, "7148817459095670029", "7148817459095670029", "be31c5c42c288d05bd0a7ba6781c7d55", [])
    绿野仙踪             = EffectMeta("绿野仙踪", True, "7355426069840661798", "7355426069840661798", "62b937613f92773795a7e71048f547f6", [])
    绿野漫旅             = EffectMeta("绿野漫旅", True, "7409674961595518258", "7409674961595518258", "f4b64f852dc51be8707a058245200c09", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    美味brunch           = EffectMeta("美味brunch", True, "7494869214751182121", "7494869214751182121", "3e2f1a0747b5380d3adbbc60118de785", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    美好瞬间             = EffectMeta("美好瞬间", True, "7332345211621887251", "7332345211621887251", "1b989818420007070e3ecdc7df7fba1e", [])
    美拉德               = EffectMeta("美拉德", True, "7273782607257685309", "7273782607257685309", "f22f3b6e1ef2d6f6e5b7a9e3b753fe18", [])
    美白嫩肤             = EffectMeta("美白嫩肤", True, "7495821426562288915", "7495821426562288915", "97fe1998783848b457e99c2ca0dfc462", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    美食增色             = EffectMeta("美食增色", True, "7403664465390013735", "7403664465390013735", "ada69091300af58308e5bbdaa2c818dc", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    美高                 = EffectMeta("美高", True, "7239236880858877217", "7239236880858877217", "29446ccd642910767b50978b2fe45f4b", [])
    羽梦                 = EffectMeta("羽梦", True, "7213573482850880827", "7213573482850880827", "ee8c5d6e7808f4e6662d42298104b87b", [])
    老街                 = EffectMeta("老街", True, "7325416529166732583", "7325416529166732583", "f2f631bdba9a97d0527f708970fc2942", [])
    聆时                 = EffectMeta("聆时", True, "7279063581092531510", "7279063581092531510", "9e59d950f575eb8a28d1f789a3b8ab50", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    聚焦                 = EffectMeta("聚焦", True, "7320428711487098153", "7320428711487098153", "54fcd82f212e40df18ac882bd748f59c", [])
    胶片电影             = EffectMeta("胶片电影", True, "7496103061845249316", "7496103061845249316", "b1ceda65b100e3c6799c576668c9e945", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    自然增色             = EffectMeta("自然增色", True, "7477552975246937380", "7477552975246937380", "f77a303a6b12fff167afa54dbf437e31", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    自然春色             = EffectMeta("自然春色", True, "7478210864818965779", "7478210864818965779", "21a8812e6490383c0eaaa6121cc71454", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    自然雪肤             = EffectMeta("自然雪肤", True, "7446467221666204969", "7446467221666204969", "67e61e6010bb7464c7efc6c8b086c408", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    舞霞                 = EffectMeta("舞霞", True, "7226257534313631037", "7226257534313631037", "ab2ba28dc4104399f9ea733837bf9364", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    艾丽莎               = EffectMeta("艾丽莎", True, "7269240546810400011", "7269240546810400011", "720b5b57295f927d983152d9bffcf33c", [])
    芭比                 = EffectMeta("芭比", True, "7259718549634157882", "7259718549634157882", "aa97d157fa8642f46808cfda6c777fdd", [])
    花容                 = EffectMeta("花容", True, "7340950375127649577", "7340950375127649577", "b5d5c5fcaf7d85f5d06e540f69258653", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    花火增色             = EffectMeta("花火增色", True, "7446691478761508108", "7446691478761508108", "08297394b95f037a00a1f169d00fd322", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    花间                 = EffectMeta("花间", True, "7211008985187487036", "7211008985187487036", "6acce0fe02d2e0328e597abcb1043de3", [])
    花间II               = EffectMeta("花间II", True, "7356877435184450851", "7356877435184450851", "78e26d36522db19bd16b83f52ae81593", [])
    花食                 = EffectMeta("花食", True, "7261180740283403578", "7261180740283403578", "37b2683488f5e586c98256dab864ab84", [])
    苍橘                 = EffectMeta("苍橘", True, "7131605817958075685", "7131605817958075685", "43666fcf1f38cb2036f87b7e496ccec4", [])
    苦尽柑来             = EffectMeta("苦尽柑来", True, "7493339669950729481", "7493339669950729481", "72833304e3f98f8a607dc9006676cbcd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    英伦复古             = EffectMeta("英伦复古", True, "7481337713443048755", "7481337713443048755", "88568151518cb4c4f5fd605bd7260260", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    茶墨                 = EffectMeta("茶墨", True, "7177728466354326822", "7177728466354326822", "d80d22c59b7846cfe3a0e8970825b316", [])
    茶酪                 = EffectMeta("茶酪", True, "7160603159486827783", "7160603159486827783", "3115e57bcd131acf89d8bdef6cd11cbd", [])
    荒原                 = EffectMeta("荒原", True, "7410401136387132724", "7410401136387132724", "18d15902359bd0e9735acef5827fe229", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    荷郁                 = EffectMeta("荷郁", True, "7274241173764525324", "7274241173764525324", "a2d1350cccd85856e3a7d58aa73cf1c4", [])
    莫吉托               = EffectMeta("莫吉托", True, "7131419324622982408", "7131419324622982408", "9b6cb49204cfb1ae3b38e70f4f71a0a7", [])
    莫奈花园             = EffectMeta("莫奈花园", True, "7500930664041172278", "7500930664041172278", "2a39723f27860f53fe08437092bf9109", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    莱顿                 = EffectMeta("莱顿", True, "7381020276177276214", "7381020276177276214", "97eeba5f505a525c4781f0e7ae990fdd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    萌宠                 = EffectMeta("萌宠", True, "7394022809317526834", "7394022809317526834", "b12efc22acc27dcad4569d60c4f63a36", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    落日派对             = EffectMeta("落日派对", True, "7374708995501739305", "7374708995501739305", "e00847299fab64d98f8ae309c62b98aa", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    落日火烧云           = EffectMeta("落日火烧云", True, "7511197003057990952", "7511197003057990952", "4e1837427374dd8ae9fa60879e6a9240", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    落日电影             = EffectMeta("落日电影", True, "7501223866988039434", "7501223866988039434", "ae92cb31192486980824dce7bf4680fe", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    落日粉               = EffectMeta("落日粉", True, "7368141858603666698", "7368141858603666698", "66dd18db6e7d8f042e7cf8cd02e64af4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    落日鎏金             = EffectMeta("落日鎏金", True, "7374251948058447158", "7374251948058447158", "f5154a29054db9946d66ed823cb58006", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    蒸汽机               = EffectMeta("蒸汽机", True, "7232220370667883837", "7232220370667883837", "c6ccfd3ad46f0c3d4715907b325c0fac", [])
    蓝梦核               = EffectMeta("蓝梦核", True, "7237440664139484473", "7237440664139484473", "0d12a669f41b3b92d1a892f42b9e0d9b", [])
    蓝橙II               = EffectMeta("蓝橙II", True, "7337929426493132058", "7337929426493132058", "40056bb94f392bdc1ab305683e265b2b", [])
    蓝灰                 = EffectMeta("蓝灰", True, "7127667757839076645", "7127667757839076645", "aa8ef49b3edba824d41f097effe534c0", [])
    蓝调                 = EffectMeta("蓝调", True, "7127664822921022734", "7127664822921022734", "3f0f50b54a2486b3fe5cfbb68dfaeaae", [])
    蓝调时刻             = EffectMeta("蓝调时刻", True, "7392898023505792319", "7392898023505792319", "1bcdd5c706e257d4935503a026ee6b20", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    蓝调烟火             = EffectMeta("蓝调烟火", True, "7328363887542209828", "7328363887542209828", "fe2367155cae2d1d5c07c10a64e3b6ef", [])
    蓝调舞曲             = EffectMeta("蓝调舞曲", True, "7366562845120646463", "7366562845120646463", "95d43f9239219401b66eae286f0ccc1c", [])
    蓝金                 = EffectMeta("蓝金", True, "7341300292148907327", "7341300292148907327", "4107fa238d7b56801c9cc3a4a3a15c32", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    蔚蓝海域             = EffectMeta("蔚蓝海域", True, "7487297018998607131", "7487297018998607131", "6e6217924fb9c959e770c2dceb2e8a03", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    薄绿                 = EffectMeta("薄绿", True, "7344374695053102371", "7344374695053102371", "4d2965f4455177ada455bd38eec021b8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    薄荷奶绿             = EffectMeta("薄荷奶绿", True, "7478775705195547930", "7478775705195547930", "aa440e34665d6b825e6e5c51daddf4cd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    薄霞                 = EffectMeta("薄霞", True, "7199458491315145988", "7199458491315145988", "ef713708b453e556415724e90c886a95", [])
    薰草                 = EffectMeta("薰草", True, "7199455696017018151", "7199455696017018151", "9864263dc92e5a276336767b1845a731", [])
    藤宅                 = EffectMeta("藤宅", True, "7159133894975999244", "7159133894975999244", "50294465be1355e66f9b789711193204", [])
    街头                 = EffectMeta("街头", True, "7263357855678467364", "7263357855678467364", "cec28e1462ddc4ce254c41bc0465d083", [])
    裸粉                 = EffectMeta("裸粉", True, "7127671519450303775", "7127671519450303775", "cea47ac2c5469b0c7630c2bcd83e3e87", [])
    褪色胶卷             = EffectMeta("褪色胶卷", True, "7502716416567545099", "7502716416567545099", "8eee6f53a48048bc43e278fe7455fa6b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    西冷                 = EffectMeta("西冷", True, "7131899038625975559", "7131899038625975559", "582a118ed87f8ddfbf2bab6ce6ccbba2", [])
    西西里               = EffectMeta("西西里", True, "7131488780451663140", "7131488780451663140", "36c35e9b449bd69a2d186c044c8032c8", [])
    西雅图               = EffectMeta("西雅图", True, "7159175960414194982", "7159175960414194982", "d89963be26099b79db297b25e18011a6", [])
    诗诺                 = EffectMeta("诗诺", True, "7330543523042708790", "7330543523042708790", "ddc9145845f6f5548aba0c4f5ceb76ed", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    诗野                 = EffectMeta("诗野", True, "7385930407901990153", "7385930407901990153", "732ab9949e2fa049eafb47f349a435c5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    贝果                 = EffectMeta("贝果", True, "7131656881805856013", "7131656881805856013", "21f8c68e7dd3fe22071ed06d21cc328a", [])
    质感增蓝             = EffectMeta("质感增蓝", True, "7493589321014906162", "7493589321014906162", "56ce0511b0a6c57c13b9893e02c8b1d9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    质感婚礼             = EffectMeta("质感婚礼", True, "7482072671715396901", "7482072671715396901", "1cf92540897de95e6708796e98ed72e2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    质感新中式           = EffectMeta("质感新中式", True, "7493945660903787803", "7493945660903787803", "4d5b0b65c44336d48392212a0cf39f90", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    质感明亮             = EffectMeta("质感明亮", True, "7486202141447589174", "7486202141447589174", "1ecc6170aa764a51fac34de94d0acda5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    质感晴春             = EffectMeta("质感晴春", True, "7482408418578271514", "7482408418578271514", "ebd1b0610f7bd86277a84a4499e608e3", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    赏味                 = EffectMeta("赏味", True, "7127608379056459015", "7127608379056459015", "d29bc8b2ddd9d018da1309ba9a467517", [])
    赤墙                 = EffectMeta("赤墙", True, "7226238039155150139", "7226238039155150139", "bca90c246ee0eae785e624ceb339e9f9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    超清电影             = EffectMeta("超清电影", True, "7437195358075145484", "7437195358075145484", "b4d4468d83898c1aeb1a9dc4562e9675", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    超清电影卷           = EffectMeta("超清电影卷", True, "7475289663381540150", "7475289663381540150", "1a1a0b6e3a384118c2aec2ce7688b31c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    超清画质             = EffectMeta("超清画质", True, "7460107425375472935", "7460107425375472935", "64488ffa5f279bff5138ab001694354b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    超白                 = EffectMeta("超白", True, "7302338645938261287", "7302338645938261287", "08f7a0eb8cd3535a23b4360acc4cc2f0", [])
    超高清               = EffectMeta("超高清", True, "7471501720732863753", "7471501720732863753", "f15b1ce7b64f37660ec166de2156e0b5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    越岭                 = EffectMeta("越岭", True, "7193989203930123554", "7193989203930123554", "80634d76c41bb167ee4c2bec4172235b", [])
    越野                 = EffectMeta("越野", True, "7195931118166609190", "7195931118166609190", "f8f340ecb359e2dd7f155da84b06f013", [])
    轻氧夏               = EffectMeta("轻氧夏", True, "7522455016272121124", "7522455016272121124", "94ed475a3c59137c13fa00a9775987f2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    轻胶少女             = EffectMeta("轻胶少女", True, "7368463117287804197", "7368463117287804197", "5a1420dd511148188fa11d42998052ab", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    过期电影卷           = EffectMeta("过期电影卷", True, "7361791960652238143", "7361791960652238143", "7b98e4262666c36aeb965842cd14d10a", [])
    运动质感             = EffectMeta("运动质感", True, "7515060642705952011", "7515060642705952011", "375bb7107af2eadbb68bed5634e0c738", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    迷幻                 = EffectMeta("迷幻", True, "7233731748545203493", "7233731748545203493", "6eb7969f4e1becb256c90950b3cb8eb3", [])
    迷雾                 = EffectMeta("迷雾", True, "7160594413847203085", "7160594413847203085", "5143fc0b35bca33c7b010458ffe8f1d7", [])
    逆光拯救             = EffectMeta("逆光拯救", True, "7503403496117521690", "7503403496117521690", "215ef7f95fec78bf8ae7a287704ec22a", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    逆光提亮             = EffectMeta("逆光提亮", True, "7366260047401323811", "7366260047401323811", "8990c9bac399f2eaedfd706d99dbdd4e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    透氧肌肤             = EffectMeta("透氧肌肤", True, "7486780026029870386", "7486780026029870386", "28c30d84ec48ad647c130cd13699640d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    通透                 = EffectMeta("通透", True, "7530582568769522980", "7530582568769522980", "91c475f7f652322e83863e2e9105bbc2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    通透暖食             = EffectMeta("通透暖食", True, "7409674549467352374", "7409674549467352374", "cad4cbe7d4bc4b96a84ff02b53733227", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    通透氧感             = EffectMeta("通透氧感", True, "7506758417143450890", "7506758417143450890", "9b272a024e2b804c5c5d1a373b9dddcf", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    邂逅                 = EffectMeta("邂逅", True, "7271145889119440147", "7271145889119440147", "6b6957bc110b65e03bc5d9ae65de6d66", [])
    郁金香               = EffectMeta("郁金香", True, "7343831195924303123", "7343831195924303123", "15e11e4352b9891fd1a1969ff7841b6b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    都卡                 = EffectMeta("都卡", True, "7341296364598480178", "7341296364598480178", "fac476280a61adbc7a731a9ee538b0b1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    都城                 = EffectMeta("都城", True, "7148817291583474980", "7148817291583474980", "3c6ec02ca887c9fdca982be6b3916430", [])
    都市                 = EffectMeta("都市", True, "7312646683672825100", "7312646683672825100", "486a70b4dc6b3cbedf1ad34461022d78", [])
    都市电影II           = EffectMeta("都市电影II", True, "7406976302122618123", "7406976302122618123", "ac28bc6e0a041b86886720147edbc7cd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    酚蓝                 = EffectMeta("酚蓝", True, "7131322091839753502", "7131322091839753502", "29848db45e217e3af6f2ad05a252fea4", [])
    酷感辣妹             = EffectMeta("酷感辣妹", True, "7506178551725542696", "7506178551725542696", "89ff083b5e1c9d7fcde3556f6f116025", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    酷绿                 = EffectMeta("酷绿", True, "7281165120980454713", "7281165120980454713", "a8c562d272e85ba3920043355e3fdf69", [])
    醒春                 = EffectMeta("醒春", True, "7211006465358843196", "7211006465358843196", "3544111511d3c365e3068023059ed83e", [])
    里昂                 = EffectMeta("里昂", True, "7131643870714006821", "7131643870714006821", "634a11a0d1a1b69aa4ac2770aa47c7dc", [])
    野林                 = EffectMeta("野林", True, "7395470918245502234", "7395470918245502234", "55d1cb1e80f65e9b7de90b4634573223", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    野趣                 = EffectMeta("野趣", True, "7193983160231742772", "7193983160231742772", "dc9a0e3b25c1b462e5c684ac64bbb1b7", [])
    金喜                 = EffectMeta("金喜", True, "7323022101735083315", "7323022101735083315", "184ae43f227bd4d20edab495a6574610", [])
    金姜                 = EffectMeta("金姜", True, "7233733326517832995", "7233733326517832995", "5116f63c46a435d34ccb83fd58b3d009", [])
    金照落日             = EffectMeta("金照落日", True, "7385416407049194787", "7385416407049194787", "33cabc7aa2c2079319df9b4149e89758", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    金秋                 = EffectMeta("金秋", True, "7145394185108065567", "7145394185108065567", "dc9528761fa2ae6baedb466ee3ce5b12", [])
    金色韶华             = EffectMeta("金色韶华", True, "7376141023656873254", "7376141023656873254", "6fe8d7f355b0895a9b4bd4110d7f58d4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    铅绿                 = EffectMeta("铅绿", True, "7131509679246675208", "7131509679246675208", "a2f9487c275619234b3e3ca37badad36", [])
    银蓝                 = EffectMeta("银蓝", True, "7145394266209127694", "7145394266209127694", "e1f2f32043ab9fd801bfdbc9a9f708d3", [])
    镜粉                 = EffectMeta("镜粉", True, "7145390299370638600", "7145390299370638600", "26b6e129d49359d3112438c001f22926", [])
    闪星                 = EffectMeta("闪星", True, "7346450662185569555", "7346450662185569555", "f9bdd96e9282b3783dcc174484aa5fc6", [])
    闪耀派对             = EffectMeta("闪耀派对", True, "7471169568484953363", "7471169568484953363", "b188a83453552dc05b8f32619c7e3e40", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    阴天拯救             = EffectMeta("阴天拯救", True, "7361399516454604071", "7361399516454604071", "a219fa1f7b74d889f137be1ef3b136a6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    阿勒泰               = EffectMeta("阿勒泰", True, "7377370363035979034", "7377370363035979034", "3252b9d3b1d4e9d6110f343eba73e4c4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    陶瓷肌               = EffectMeta("陶瓷肌", True, "7234793127867878712", "7234793127867878712", "e7b66853ca5dbdb1c049d45225b355cb", [])
    随性                 = EffectMeta("随性", True, "7271140658071588132", "7271140658071588132", "6619560c233df84381e8c371b7387faa", [])
    雀染                 = EffectMeta("雀染", True, "7145394848361729288", "7145394848361729288", "c6bc39d80e10c8bfe361164e83585a01", [])
    雨皂                 = EffectMeta("雨皂", True, "7145678373530946824", "7145678373530946824", "af2869df0cbd9ea0ac0443206e91b135", [])
    雨空                 = EffectMeta("雨空", True, "7196917591909109052", "7196917591909109052", "ffe686005136a692517b6e19e4e490e7", [])
    雪地胶片             = EffectMeta("雪地胶片", True, "7431914829876694324", "7431914829876694324", "fb5e7ff5746e82dc6a426e2731012359", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    雪地胶片II           = EffectMeta("雪地胶片II", True, "7431914902177991970", "7431914902177991970", "e739418605bc306c84cde37fd76b937a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    雪地胶片III          = EffectMeta("雪地胶片III", True, "7431914955747691810", "7431914955747691810", "52e66f9849aed0df650660c2cc97a9f5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    雪挞                 = EffectMeta("雪挞", True, "7262376135202327871", "7262376135202327871", "319cab31ed6a056c3f5256a357eb9b96", [])
    雪白肤               = EffectMeta("雪白肤", True, "7426222844872330522", "7426222844872330522", "10cdb8b77362ba307e5cbe93b83209bd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    雾都                 = EffectMeta("雾都", True, "7312646650202262820", "7312646650202262820", "00b8522f76bf9a991e0a6090f63747ee", [])
    雾野                 = EffectMeta("雾野", True, "7127823362356727077", "7127823362356727077", "6fbd00682d2a15e079bc242301e9b757", [])
    青巷                 = EffectMeta("青巷", True, "7185425707231644961", "7185425707231644961", "3ce24fadb400619dd73d6fbad3211229", [])
    青提                 = EffectMeta("青提", True, "7131290518838938887", "7131290518838938887", "9cd0e0ba2190b96f6eccacbed5151b24", [])
    青春                 = EffectMeta("青春", True, "7502056246804024611", "7502056246804024611", "ca3ed1c728e48270ab32bef1dd79b3ab", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    青春照               = EffectMeta("青春照", True, "7513077194952936767", "7513077194952936767", "754dec3e8e77d8fcb6e0902e63a923bd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    青春物语             = EffectMeta("青春物语", True, "7511949534042311946", "7511949534042311946", "885801c812396bb1688ef9bd45bfe4c0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    青春胶片             = EffectMeta("青春胶片", True, "7510888042761096459", "7510888042761096459", "d7cee0f1454e87ac7735278aef69ebc7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    青春记忆             = EffectMeta("青春记忆", True, "7495811579095682367", "7495811579095682367", "4ae2a67a3635524b1c0de0d6c34304d0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    青森                 = EffectMeta("青森", True, "7145390299106381086", "7145390299106381086", "9b0479f9bd81b1c22908e882f16610d8", [])
    青橙电影感           = EffectMeta("青橙电影感", True, "7478335987777572137", "7478335987777572137", "0acf322490d8427244fbfda12940b3f6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    青灰                 = EffectMeta("青灰", True, "7127671508264078599", "7127671508264078599", "a9b480c9b5bf91d2aa0b5e8388f53746", [])
    青黄                 = EffectMeta("青黄", True, "7127541821332409630", "7127541821332409630", "e777bf266933df88bfc019a84e6dd792", [])
    青黄II               = EffectMeta("青黄II", True, "7337932621046910262", "7337932621046910262", "059b7e40c1fe52a2451c35bd82e329e5", [])
    韦斯                 = EffectMeta("韦斯", True, "7226989951911562553", "7226989951911562553", "7162086ae8bf07df55d86ce535bdd75c", [])
    顺意                 = EffectMeta("顺意", True, "7186934131484331322", "7186934131484331322", "b22dbc165fbe869cc1522d8255afe928", [])
    颜白                 = EffectMeta("颜白", True, "7484983198800301321", "7484983198800301321", "55bd0be59e02370787cbafb22bace0e0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    风味                 = EffectMeta("风味", True, "7330579916272012580", "7330579916272012580", "7abbb099b234e92b6a7169f2ae6232b6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    风铃蓝               = EffectMeta("风铃蓝", True, "7261466919688015140", "7261466919688015140", "5bf0d1478c19629df96ad85b3301ec35", [])
    飒意                 = EffectMeta("飒意", True, "7248568718265978112", "7248568718265978112", "25a705fe908fad028d75a5b9bf30e4b7", [])
    食光II               = EffectMeta("食光II", True, "7478181967532543259", "7478181967532543259", "dee8c9a0537f6b78d56eb3b32a5f5de1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    食色                 = EffectMeta("食色", True, "7131644140340776205", "7131644140340776205", "8540ba0ddb988c6f5f4b69742ca94136", [])
    香浓                 = EffectMeta("香浓", True, "7330588808666156307", "7330588808666156307", "480c2599aaaf7be5a800c269dada7cdd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    驮月                 = EffectMeta("驮月", True, "7145394213339860261", "7145394213339860261", "ba8a3a6272282d63ee8b46c2e228e09b", [])
    高晴画质             = EffectMeta("高晴画质", True, "7486890470149246219", "7486890470149246219", "8bdb640b5e3aa5fcd6c19f31463f36f9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清                 = EffectMeta("高清", True, "7447039744229428534", "7447039744229428534", "838ba5b40cfb93c8c8f4ac23489dd0ce", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清4K               = EffectMeta("高清4K", True, "7463103811276655881", "7463103811276655881", "c7950f4b5629606b1c32165ec8967675", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清4k电影           = EffectMeta("高清4k电影", True, "7454130417562553651", "7454130417562553651", "cc6b3db256e26231e11fa48b17d80b71", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清II               = EffectMeta("高清II", True, "7325426821267295551", "7325426821267295551", "17a86357c081e0d080c9d501a66382d0", [])
    高清中性灰           = EffectMeta("高清中性灰", True, "7476126917280730378", "7476126917280730378", "34151fd0c9652a96e5debded17f272e9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清亮粉             = EffectMeta("高清亮粉", True, "7474611627338239282", "7474611627338239282", "202d1c83b5a7fa0e2bc1e29f28fd2d5f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清修复             = EffectMeta("高清修复", True, "7471501728546966835", "7471501728546966835", "9703a70d4a78fd4e9185a3cab90259c0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清修复III          = EffectMeta("高清修复III", True, "7402847660165713190", "7402847660165713190", "3bf03425397e50f8a51df7f69fe34138", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清冷冬             = EffectMeta("高清冷冬", True, "7446737538967932186", "7446737538967932186", "a29f0443ce7468781539fe86dc17918a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清冷调             = EffectMeta("高清冷调", True, "7478329447545081129", "7478329447545081129", "e56a34d74560aa6204b16da614a64c74", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清圣诞             = EffectMeta("高清圣诞", True, "7446290162922818870", "7446290162922818870", "4e9a65f2fdaa588f544c6b411e998547", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清增强             = EffectMeta("高清增强", True, "7426668776491453707", "7426668776491453707", "c28d7683eb3bbc58cd3b008b380ed551", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清增色             = EffectMeta("高清增色", True, "7440518219409968384", "7440518219409968384", "bdf331387c885b59eb154db384b9f801", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清增质             = EffectMeta("高清增质", True, "7436815358410886435", "7436815358410886435", "b2394c83d83e47b5f21b0307af48ac9e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清寒冬             = EffectMeta("高清寒冬", True, "7449684693982743817", "7449684693982743817", "dfd7cf9a4a54f20c70b2c9b2c5fbc6aa", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清影视             = EffectMeta("高清影视", True, "7437098009827036455", "7437098009827036455", "0cdff3f488d2dff927a695fdae418784", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清感               = EffectMeta("高清感", True, "7414810241453280549", "7414810241453280549", "f26fae62c0f2cc8b44506cd07d6a086e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清感II             = EffectMeta("高清感II", True, "7414810073731435785", "7414810073731435785", "b09366ac9d328a2594c8c0953e7f1167", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清感III            = EffectMeta("高清感III", True, "7414810202706447625", "7414810202706447625", "8c9985eeeedee5235a4943b845b240cd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清提亮             = EffectMeta("高清提亮", True, "7439995842477428004", "7439995842477428004", "100906363649af4f5176b8565f27fc39", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清提升             = EffectMeta("高清提升", True, "7443710725773675803", "7443710725773675803", "f65967d1ee75e1d946c95fe6c730240f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清春日             = EffectMeta("高清春日", True, "7476104906924100915", "7476104906924100915", "a0150e0273b470188e19f1b7b24e4ef1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清晴天             = EffectMeta("高清晴天", True, "7442389591140748570", "7442389591140748570", "e7b2e8a233f1d0bc5b71aca1f8fa44ed", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清晴日             = EffectMeta("高清晴日", True, "7448290256476065035", "7448290256476065035", "23940e28ee7ceab734e59b2102fc7904", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清暖调             = EffectMeta("高清暖调", True, "7431187754379136266", "7431187754379136266", "23aea64209982cc3a0a3b1acdd276b3e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清润颜             = EffectMeta("高清润颜", True, "7428629277110848768", "7428629277110848768", "1df56b348fb1eacd59e730e89e9b0363", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清漫晴             = EffectMeta("高清漫晴", True, "7442344329114422565", "7442344329114422565", "d948e6691c99022bb4cfed02a660245f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清焕晴             = EffectMeta("高清焕晴", True, "7471955373340101927", "7471955373340101927", "734bfe48985cc95384f10bb201f24dbe", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清电影             = EffectMeta("高清电影", True, "7413062310580800831", "7413062310580800831", "c6209556e6b9b723b7a2c7bf83d29051", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清电影卷           = EffectMeta("高清电影卷", True, "7452946862581058853", "7452946862581058853", "4ccd0bcc2434245db6d247397682b534", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清画质             = EffectMeta("高清画质", True, "7465342226118266162", "7465342226118266162", "3450ce5a0c73d4728321ba46ed98aed7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清绿妍             = EffectMeta("高清绿妍", True, "7451808659320900891", "7451808659320900891", "7d50bac0231c7a6538ff64ca8c9d3218", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清美食             = EffectMeta("高清美食", True, "7435865312907676978", "7435865312907676978", "88736302c2c09917ddf9dd6ebef77373", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清质感             = EffectMeta("高清质感", True, "7433451928773807397", "7433451928773807397", "30ae508cfe0edc3ec1f749c243997a2a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清雪景             = EffectMeta("高清雪景", True, "7444960692853148955", "7444960692853148955", "04a4ecbde473119e6b055fcc0d34eb4a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清雪肤             = EffectMeta("高清雪肤", True, "7447397442603076899", "7447397442603076899", "0fd44648b707fbea89ec49eaa2320b2d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清鲜明             = EffectMeta("高清鲜明", True, "7435675065498275081", "7435675065498275081", "46ab34769df26db38c9a7f84ca66c0d9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清黑白             = EffectMeta("高清黑白", True, "7429744855724641545", "7429744855724641545", "064d56e4db73deb306811f49462fffcb", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清默冬             = EffectMeta("高清默冬", True, "7450134286071631141", "7450134286071631141", "6d27a4cc883039e86d079f7a80e51b40", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高级影视             = EffectMeta("高级影视", True, "7513959933310749991", "7513959933310749991", "cadf521e0e50c405df615f7c07dbbcb1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高街                 = EffectMeta("高街", True, "7145394469666376991", "7145394469666376991", "7036694f303647fe7526848bb622947f", [])
    魅影                 = EffectMeta("魅影", True, "7175076304058895619", "7175076304058895619", "361328c4bc995c85053ea003268aefbf", [])
    魔都                 = EffectMeta("魔都", True, "7166480345666260263", "7166480345666260263", "cf4adfafcc5e59b9bddd8eeb4d20f44e", [])
    鲜亮                 = EffectMeta("鲜亮", True, "7428441733123345702", "7428441733123345702", "9c3aca0a52af31cc7d60152290156687", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    鲜明                 = EffectMeta("鲜明", True, "7320434750018047251", "7320434750018047251", "ba8b7cbf504c97a30c923d0d6a6c2b44", [])
    鲜明II               = EffectMeta("鲜明II", True, "7361400073533820196", "7361400073533820196", "350ff543fdd150a6f7e571aa3f467640", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    鲜明增强             = EffectMeta("鲜明增强", True, "7451608395745889586", "7451608395745889586", "208197f9859dd06b1868cd75859676d1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    鲜明增色             = EffectMeta("鲜明增色", True, "7463798839258909963", "7463798839258909963", "4c2512b58fb8debd1c75ce016a8919a5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    鲜美                 = EffectMeta("鲜美", True, "7330581892510649636", "7330581892510649636", "0f2146e69f0cf22a0e0aa733be623bd4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    鲜艳增色             = EffectMeta("鲜艳增色", True, "7497157143502654732", "7497157143502654732", "9008c9a3d5200c39fc34090ffca9a3d8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    鲜花增彩             = EffectMeta("鲜花增彩", True, "7494505446158503179", "7494505446158503179", "38823b82a91be95b6ac61dd9fe1054e8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    鲜花增色             = EffectMeta("鲜花增色", True, "7493083101426453796", "7493083101426453796", "f5b7e85440654ec13e83c55de61cb8fc", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    鲜花增艳             = EffectMeta("鲜花增艳", True, "7493457725431631142", "7493457725431631142", "bed611a951986953cad10fe37720acd1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    鹅冠                 = EffectMeta("鹅冠", True, "7308714123913612607", "7308714123913612607", "37be69ef37633c108a65ab994875d06e", [])
    黄昏                 = EffectMeta("黄昏", True, "7272330168717430075", "7272330168717430075", "eebcc8f84ff895bd0d66535d9ad44275", [])
    黄昏时               = EffectMeta("黄昏时", True, "7418828782020168999", "7418828782020168999", "844bdb555340709e50d47c842a6da1e7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    黑冰                 = EffectMeta("黑冰", True, "7131522303082466597", "7131522303082466597", "d03c03e8f1e67f5cff0a5671fe96dfb9", [])
    黑暗神话             = EffectMeta("黑暗神话", True, "7408496787398446362", "7408496787398446362", "0685a00dcd0068efd472e6019d312774", [])
    黑曜                 = EffectMeta("黑曜", True, "7223712396769119545", "7223712396769119545", "3b81efb578ddec8efa40dd0c5b754056", [])
    黑金                 = EffectMeta("黑金", True, "7414902721733479699", "7414902721733479699", "46eddfebd9864056c59bf8219cb671e9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    黑金红               = EffectMeta("黑金红", True, "7341266486536768831", "7341266486536768831", "66796ec5de5e85b2cf461fa49b4c0225", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    龙舌兰               = EffectMeta("龙舌兰", True, "7252674245396942139", "7252674245396942139", "254083154fd15d41d41cc3763eda9f40", [])
