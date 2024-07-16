from enum import Enum

class Animation_meta:
    title: str
    is_vip: bool
    duration: float

    resource_id: str
    effect_id: str
    md5: str

    def __init__(self, title: str, is_vip: bool, duration: float, resource_id: str, effect_id: str, md5: str):
        self.title = title
        self.is_vip = is_vip
        self.duration = duration
        self.resource_id = resource_id
        self.effect_id = effect_id
        self.md5 = md5

class Intro_type(Enum):
    # 免费入场效果
    渐显        = Animation_meta("渐显", False, 0.5, "6798320778182922760", "624705", "af863de1e359fd4f54bb78f2e2749e1f")
    旋转        = Animation_meta("旋转", False, 0.5, "6798334070653719054", "624731", "b3018b8ae12d4a9421d81a3b263b7e88")
    斜切        = Animation_meta("斜切", False, 0.7, "7210657307938525751", "10696371", "a385761197d457f4599d231421045230")
    钟摆        = Animation_meta("钟摆", False, 0.5, "6b9d17389864da0a68d347365023849a", "636115", "6803260897117606414")
    雨刷        = Animation_meta("雨刷", False, 0.5, "0a8846e691446c6b2f583086567579a5", "634681", "6802871256849846791")
    雨刷_II     = Animation_meta("雨刷 II", False, 0.5, "f67c2ccd81956813d5b1303625bed354", "640101", "6805748897768542727")

    放大        = Animation_meta("放大", False, 0.5, "6798332733694153230", "624751", "028a77e121c22a4dd130a46a0ed90714")
    缩小        = Animation_meta("缩小", False, 0.5, "6798332584276267527", "624755", "7e0e6b55704b7fc20588fee77058e95c")
    轻微放大    = Animation_meta("轻微放大", False, 0.5, "6800268825611735559", "629085", "f6c8209ef7142fff6cf9c68573216371")
    动感放大    = Animation_meta("动感放大", False, 0.5, "6740867832570974733", "431662", "3d880239a1fa70fbaedcc7fd20794e22")
    动感缩小    = Animation_meta("动感缩小", False, 0.5, "6740868384637850120", "431658", "8357dd30914ef6ba1ba89dd12a83dc3e")

    向右滑动    = Animation_meta("向右滑动", False, 0.5, "6798333076469453320", "624743", "e3e2dad87aff58e7944fac67661b56b2")
    向左滑动    = Animation_meta("向左滑动", False, 0.5, "6798332871267324423", "624747", "dcae7883ea619dac2661a5f21795cc9f")
    向上滑动    = Animation_meta("向上滑动", False, 0.5, "6798333487523828238", "624739", "9598ba5dd6e4ce29c7c3ffded39fb3b9")
    向下滑动    = Animation_meta("向下滑动", False, 0.5, "6798333705401143816", "624735", "d34d52d5386e20de654b0fff9ea9704f")

    向右甩入    = Animation_meta("向右甩入", False, 0.5, "6739338727866241539", "431636", "228f76b86355e74087a9a80647236b88")
    向下甩入    = Animation_meta("向下甩入", False, 0.5, "6739338374441603598", "431638", "afb5afec3c42fa627a007ff609c83792")
    向右上甩入  = Animation_meta("向右上甩入", False, 0.5, "6740122731418751495", "431644", "12ae5b6cc0b2bff43e958d5ca2d574fe")
    向右下甩入  = Animation_meta("向右下甩入", False, 0.5, "f821a402edb042a9d68d825cb804ac6e", "431640", "6739395718223499787")
    向左上甩入  = Animation_meta("向左上甩入", False, 0.5, "6740122563692728844", "431648", "aa97897803351debd46c9182132c64c5")
    向左下甩入  = Animation_meta("向左下甩入", False, 0.5, "6739395445346275853", "431642", "269d5e19ed83faa5f5c72a1401e4564b")

    向右转入    = Animation_meta("向右转入", False, 0.5, "c447b8637ba24ae1111b087e8d5a5739", "638825", "6805019065761927694")
    向左转入    = Animation_meta("向左转入", False, 0.5, "aca9db228bf685cd9f02eb966252846e", "699157", "6816560956647150093")
    向上转入    = Animation_meta("向上转入", False, 0.5, "0247c3715de210fa89a4fc9f2f03b63c", "645307", "6808401616564130312")
    向上转入_II = Animation_meta("向上转入 II", False, 0.5, "6818747060649464327", "701961", "c66f550e7ab2de4ef4eb1ee7e7002fa3")

    左右抖动    = Animation_meta("左右抖动", False, 0.5, "6739418540421419524", "431654", "7572d7461e38d73c578aa8e4dca7163a")
    上下抖动    = Animation_meta("上下抖动", False, 0.5, "6739418390030455300", "431652", "bff95de5e1e4803ea64a52632bcfb361")
    轻微抖动    = Animation_meta("轻微抖动", False, 0.5, "6739418227031413256", "431664", "7ec99bda70fa6922395d65235991f9e5")
    轻微抖动_II = Animation_meta("轻微抖动 II", False, 0.5, "6739418677910704651", "431650", "8e29ab0a86dac5719300064821e8b63d")
    轻微抖动_III = Animation_meta("轻微抖动 III", False, 0.5, "6781683302672634382", "503136", "8482055860ab20c23102d78aa3486a7a")

    旋转开幕    = Animation_meta("旋转开幕", False, 1, "7186944542409495099", "8295043", "407822a27a67612c3caa3e4223aa32d3")
    折叠开幕    = Animation_meta("折叠开幕", False, 1.5, "7239273897491698232", "14506065", "17e0225f852c0798063d82440ca54185")
    跳转开幕    = Animation_meta("跳转开幕", False, 0.733333, "7279999334001676857", "23185431", "817876a62d2d05e4eef9ac4cfa9c70fe")
    抖动下降    = Animation_meta("抖动下降", False, 0.5, "9b04ce5965c78218e918f043cf12a879", "1206320", "6991764455931515422")
    漩涡旋转    = Animation_meta("漩涡旋转", False, 0.5, "6782010677520241165", "703281", "6e922bdebed1d87f9a63ba285a5dd792")
    镜像翻转    = Animation_meta("镜像翻转", False, 0.5, "6797338697625768455", "646003", "55ec076a5d62f7e80655e60c43f68f80")
    Kira游动    = Animation_meta("Kira游动", False, 2.266666667, "7311984593387655731", "34176967", "05daa2cb2b53e1830a0e657ede749daf")

    # 付费入场效果
    展开        = Animation_meta("展开", True, 0.5, "7221413342257091133", "12088589", "553acdb325d76533d6ecbd6d621d9b9e")
    闪现        = Animation_meta("闪现", True, 0.44, "7210363235906622012", "10668047", "6a680c49cd11a05f3eb0e5a3fed165f7")
    横向模糊    = Animation_meta("横向模糊", True, 0.5, "7301896031673782835", "29805902", "b8b953ad94b16c47601af887d4ccc8c9")
    侧滑        = Animation_meta("侧滑", True, 0.6, "7239559299196785209", "14524393", "c67d95e820752346af44e2cb515c0115")
    便利贴      = Animation_meta("便利贴", True, 0.9, "7379456870265655859", "70486392", "06613663efa8ef29beadf8746019c823")
    交错开幕    = Animation_meta("交错开幕", True, 1.1, "7280797339042714169", "23387955", "123322fa9ce7c37f0c2c35819f00b524")
    向上闪入    = Animation_meta("向上闪入", True, 0.7, "7273389803532456504", "21816946", "ecaffca7c7e1d7744fa296a29f65b366")
    水墨        = Animation_meta("水墨", True, 2.43333, "7321672946466951731", "39180627", "7e5d11c796a2e1bec5feb486e647e60b")
    拼图        = Animation_meta("拼图", True, 1.066666667, "7369889381357720102", "64963350", "4b721a1559eb3451d6cc358468537c49")
    向下甩动    = Animation_meta("向下甩动", True, 1.4, "7338320641306661410", "47050546", "060ee66b7f59d3d2c8064be5ae32171c")
    砸出波纹    = Animation_meta("砸出波纹", True, 1.56, "7255594501694034490", "18159482", "644483b024fc852955dd807da067d8e9")
    震波        = Animation_meta("震波", True, 0.8, "7115301367786246692", "3297068", "8aaccb8f112aa3cacd80fa79fcc1690f")
    震波_II     = Animation_meta("震波 II", True, 0.8333333333, "7211042099737662009", "10744265", "f8f236cd1279af3680bcc71dda889d97")
    震波_III    = Animation_meta("震波 III", True, 1.7, "3be0a1f04cf38bf05ed301ebaeb47ef8", "25545977", "7288985830578721336")
    聚合        = Animation_meta("聚合", True, 2, "7303524763589153306", "30391788", "c3293067129322c884d0865b99cb11bd")
    圆形开幕    = Animation_meta("圆形开幕", True, 0.9, "7218210014949806647", "11680735", "2c171ce2c85042bb518cbdc08ced9709")
    模糊聚焦    = Animation_meta("模糊聚焦", True, 1.2, "7337937899704291866", "46838778", "38841ccaef6186af6d516eeea116b3c6")
    向上滚动    = Animation_meta("向上滚动", True, 1, "7312341574988337690", "34388476", "14e7c85bfa04ecbacc1e63ee386840b7")
    抖动横移    = Animation_meta("抖动横移", True, 0.566666667, "7265946978792510010", "20437845", "e4951e1d7abcdbd4e8bf1cf33430def7")
    转圈圈      = Animation_meta("转圈圈", True, 0.8, "7246643852411408952", "15726741", "f2c920e366c3c733f1d86a8473aff310")
    抖动变焦    = Animation_meta("抖动变焦", True, 0.8, "7156911481563386381", "5414507", "04365018fdc27b7e1175b709a739f800")
    脉冲        = Animation_meta("脉冲", True, 0.9, "7379909514847326732", "70764198", "ae7fac0214409e340db6a600e97303da")
    老电视      = Animation_meta("老电视", True, 1.4, "7290754106417746491", "26091602", "4cbe6bdc6da704e481a40f44266cee0b")
    心形放大    = Animation_meta("心形放大", True, 1.5, "7042968847070007844", "1487080", "3bb1bb084e5ebf25e67fc078d3c6a119")
    流金        = Animation_meta("流金", True, 1.5, "7322367212142989850", "39438403", "6654a74eb923c201fe18765f18d4b367")
    分屏横移    = Animation_meta("分屏横移", True, 1, "7257878167023522365", "18746326", "dcadf2284399fe6200f77fad9a1ec41a")
    玻璃聚集    = Animation_meta("玻璃聚集", True, 1.7, "7340265236101861915", "48072242", "68c8e8f1eba4f4b2e3d35472f8b4822c")
    能量立方    = Animation_meta("能量立方", True, 1.33333333, "7359472053998588425", "58285135", "301b4ffff8510c87b7174161b2642ca3")
    曝光放射    = Animation_meta("曝光放射", True, 0.8, "7158737452939612703", "5529363", "09df65728356189436974e08c42bc578")
    旋转圆球    = Animation_meta("旋转圆球", True, 0.8, "7380298290140549647", "70989966", "19b93b0edea19a73d2cf7f818ace3265")
    划水        = Animation_meta("划水", True, 0.8, "7226632607939695161", "12811781", "57a259c58a4daddacc897c75ec9c10a4")
    烟雾弹      = Animation_meta("烟雾弹", True, 1.2, "7226641244938572346", "12815013", "8c5e4642b824c252b5a556bbbcbae767")
    果冻_I      = Animation_meta("果冻 I", True, 0.8, "7171640017574433294", "6725401", "4ef7f9da6b1331109620381229d55429")
    果冻_II     = Animation_meta("果冻 II", True, 0.8, "7171690870788329992", "6732061", "01d346b0f37b87c25c17a53309189432")
    拉丝滑入    = Animation_meta("拉丝滑入", True, 0.5, "7112725640901562887", "3179668", "913b99e9012d50f629c59a31e030b143")
    斜向拉丝    = Animation_meta("斜向拉丝", True, 0.6666, "7360531434487943743", "58777551", "60ba474a0460cb7e999830c02943e977")
    色散波纹    = Animation_meta("色散波纹", True, 0.83, "7299029942870741542", "28824874", "2ce459ce040280d7c4f36ab78a3612e5")
    交叉震动    = Animation_meta("交叉震动", True, 0.8333, "7222990639984546360", "12309329", "cde910202607be12ac747e2e76316e7f")
    冲撞        = Animation_meta("冲撞", True, 2, "7215530662986519096", "11320895", "aeadb248c06d074a2d98f425a57999f0")
    快速翻页    = Animation_meta("快速翻页", True, 0.16666, "7296381392340914715", "27878991", "6e1d71ff694a87526f9c5bb2c01c927d")
    闪屏        = Animation_meta("闪屏", True, 1.2, "c2f368ce853ab863a12c686bb99bb41e", "14904085", "7242155802209817147")
    四屏转换    = Animation_meta("四屏转换", True, 1, "fdd9abc8f2abadc0ae6e909779f282e6", "48492378", "7341283787143123507")
    分屏翻转    = Animation_meta("分屏翻转", True, 0.7, "013f6255cb0672198f26962bff3f788b", "18711457", "7257782721575916088")
    _2024       = Animation_meta("2024", True, 1.5, "d68370ce25f28ec80d9c0bb7e51e2324", "33056565", "7309774750677471794")
    多层环形    = Animation_meta("多层环形", True, 2, "54801ad31b13853ad1e3ccf945e89973", "42686363", "7329444938960081460")
    弹力分割    = Animation_meta("弹力分割", True, 1.06, "9f5878effce0a857900a4f050ea52318", "35994464", "7267827357627454013")
    画出爱心    = Animation_meta("画出爱心", True, 1.6, "6e5cdc1e7ece582da904ac520440e88a", "16211481", "7248901535894082105")
    发光矩形    = Animation_meta("发光矩形", True, 1.0333, "64852509d7cb2a578469b3438b94df52", "51093680", "7346511208171704841")
    扫描        = Animation_meta("扫描", True, 0.6, "191401f0b79c28d7569dfc356ba827b6", "34385508", "7312335732721324554")
    空间扭曲    = Animation_meta("空间扭曲", True, 1.16, "da3a08519a9315e3625173b71a4d8ee3", "28693486", "7298688232294715931")
    弹近        = Animation_meta("弹近", True, 1.5, "7314144465944318502", "35289246", "30c62d3ccb969173e5fa43511894116b")
    马赛克      = Animation_meta("马赛克", True, 1, "7282703408383922745", "23885083", "273c4952c915c9250f0b9edadac34148")
    立体翻转    = Animation_meta("立体翻转", True, 1.1, "7346505124820292150", "51089258", "bad88fa72b42b3c12099c31654575952")
    震动波纹    = Animation_meta("震动波纹", True, 1.5, "7307196313148330547", "31806105", "95760b6f7efe0016546e38852a981f49")
    十字震动    = Animation_meta("十字震动", True, 0.8, "33d4a2ff79aa2fb88fadd45aee1998e9", "54686020", "7352824361625063987")
    荧光爆闪    = Animation_meta("荧光爆闪", True, 1, "84d6cfae125a71855b500604748f1e19", "51992419", "7347948517471556096")
    爱心碰撞    = Animation_meta("爱心碰撞", True, 2.666666667, "119e873890708ee4817c9778dcb20b69", "41910725", "7327872475453198848")
    波纹弹动    = Animation_meta("波纹弹动", True, 1.2, "b29c4c4dbac023b27bac5d32e642f6bb", "50640360", "7345731405663441460")
