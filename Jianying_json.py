import os
import json, uuid
import imageio

from enum import Enum
from typing import Optional, Literal, Union, Dict, List, Any

from animation_meta import Video_intro_type, Video_outro_type

class Crop_settings:
    """素材的裁剪设置, 各属性均在0-1之间, 注意素材的坐标原点在左上角"""

    upper_left_x: float
    upper_left_y: float
    upper_right_x: float
    upper_right_y: float
    lower_left_x: float
    lower_left_y: float
    lower_right_x: float
    lower_right_y: float

    def __init__(self, *, upper_left_x: float = 0.0, upper_left_y: float = 0.0,
                 upper_right_x: float = 1.0, upper_right_y: float = 0.0,
                 lower_left_x: float = 0.0, lower_left_y: float = 1.0,
                 lower_right_x: float = 1.0, lower_right_y: float = 1.0):
        """初始化裁剪设置, 默认参数表示不裁剪"""
        self.upper_left_x = upper_left_x
        self.upper_left_y = upper_left_y
        self.upper_right_x = upper_right_x
        self.upper_right_y = upper_right_y
        self.lower_left_x = lower_left_x
        self.lower_left_y = lower_left_y
        self.lower_right_x = lower_right_x
        self.lower_right_y = lower_right_y

    def export_json(self) -> Dict[str, Any]:
        return {
            "upper_left_x": self.upper_left_x,
            "upper_left_y": self.upper_left_y,
            "upper_right_x": self.upper_right_x,
            "upper_right_y": self.upper_right_y,
            "lower_left_x": self.lower_left_x,
            "lower_left_y": self.lower_left_y,
            "lower_right_x": self.lower_right_x,
            "lower_right_y": self.lower_right_y
        }

class Video_material:
    """视频素材（视频或图片）"""

    material_id: str
    """素材全局id, 自动生成"""
    local_material_id: str
    """素材本地id, 意义暂不明确"""
    material_name: str
    """素材名称"""
    path: str
    """素材文件路径"""
    duration: int
    """素材时长, 单位为微秒"""
    height: int
    """素材高度"""
    width: int
    """素材宽度"""
    crop_settings: Crop_settings
    """素材裁剪设置"""
    material_type: Literal["video", "photo"]
    """素材类型: 视频或图片"""

    VIDEO_POSTFIX = (".mp4", ".mov", ".avi", ".flv", ".wmv", ".rmvb", ".mkv")
    IMAGE_POSTFIX = (".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".psd", ".eps", ".svg")

    def __init__(self, path: str, material_name: Optional[str] = None, crop_settings: Crop_settings = Crop_settings()):
        """从指定位置加载视频（或图片）素材

        Args:
            path (`str`): 素材文件路径, 支持mp4, mov, avi等常见视频文件及jpg, jpeg, png等图片文件.
            material_name (`str`, optional): 素材名称, 如果不指定, 默认使用文件名作为素材名称.
            crop_settings (`Crop_settings`, optional): 素材裁剪设置, 默认不裁剪.

        Raises:
            `FileNotFoundError`: 素材文件不存在.
            `ValueError`: 不支持的素材文件类型.
        """

        self.material_name = material_name if material_name else os.path.basename(path)
        self.material_id = uuid.uuid3(uuid.NAMESPACE_DNS, self.material_name).hex
        self.path = path
        self.crop_settings = crop_settings
        self.local_material_id = ""

        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} does not exist")
        postfix = os.path.splitext(path)[1]
        if postfix in self.VIDEO_POSTFIX:
            vid = imageio.get_reader(path)

            self.material_type = "video"
            self.duration = int(round(vid.get_meta_data()['duration'] * 1e6))
            self.width, self.height = [int(x) for x in vid.get_meta_data()["size"]]
            vid.close()
        elif postfix in self.IMAGE_POSTFIX:
            pic = imageio.imread(path)

            self.material_type = "photo"
            self.duration = 10800000000 # 相当于无限长
            self.height, self.width, _ = pic.shape
        else:
            raise ValueError(f"Unsupported file type {postfix}")

    def export_json(self) -> Dict[str, Any]:
        video_material_json = {
            "aigc_type": "none",
            "audio_fade": None,
            "cartoon_path": "",
            "category_id": "",
            "category_name": "local",
            "check_flag": 63487,
            "crop": self.crop_settings.export_json(),
            "crop_ratio": "free",
            "crop_scale": 1.0,
            "duration": self.duration,
            "extra_type_option": 0,
            "formula_id": "",
            "freeze": None,
            "has_audio": False,
            "height": self.height,
            "id": self.material_id,
            "intensifies_audio_path": "",
            "intensifies_path": "",
            "is_ai_generate_content": False,
            "is_copyright": False,
            "is_text_edit_overdub": False,
            "is_unified_beauty_mode": False,
            "local_id": "",
            "local_material_id": self.local_material_id,
            "material_id": self.material_id,
            "material_name": self.material_name,
            "material_url": "",
            "matting": {
                "flag": 0,
                "has_use_quick_brush": False,
                "has_use_quick_eraser": False,
                "interactiveTime": [],
                "path": "",
                "strokes": []
            },
            "media_path": "",
            "object_locked": None,
            "origin_material_id": "",
            "path": self.path,
            "picture_from": "none",
            "picture_set_category_id": "",
            "picture_set_category_name": "",
            "request_id": "",
            "reverse_intensifies_path": "",
            "reverse_path": "",
            "smart_motion": None,
            "source": 0,
            "source_platform": 0,
            "stable": {
                "matrix_path": "",
                "stable_level": 0,
                "time_range": {"duration": 0, "start": 0}
            },
            "team_id": "",
            "type": self.material_type,
            "video_algorithm": {
                "algorithms": [],
                "complement_frame_config": None,
                "deflicker": None,
                "gameplay_configs": [],
                "motion_blur_config": None,
                "noise_reduction": None,
                "path": "",
                "quality_enhance": None,
                "time_range": None
            },
            "width": self.width
        }
        return video_material_json

class Clip_settings:
    """素材片段的图像调节设置"""

    alpha: float
    """图像透明度, 0-1"""
    flip_horizontal: bool
    """是否水平翻转"""
    flip_vertical: bool
    """是否垂直翻转"""
    rotation: float
    """旋转角度, 可正可负"""
    scale_x: float
    """水平缩放比例"""
    scale_y: float
    """垂直缩放比例"""
    transform_x: float
    """水平位移, 单位为像素?"""
    transform_y: float
    """垂直位移, 单位为像素?"""

    def __init__(self, *, alpha: float = 1.0,
                 flip_horizontal: bool = False, flip_vertical: bool = False,
                 rotation: float = 0.0,
                 scale_x: float = 1.0, scale_y: float = 1.0,
                 transform_x: float = 0.0, transform_y: float = 0.0):
        """初始化图像调节设置, 默认参数表示不作任何图像变换"""
        self.alpha = alpha
        self.flip_horizontal, self.flip_vertical = flip_horizontal, flip_vertical
        self.rotation = rotation
        self.scale_x, self.scale_y = scale_x, scale_y
        self.transform_x, self.transform_y = transform_x, transform_y

    def export_json(self) -> Dict[str, Any]:
        clip_settings_json = {
            "alpha": self.alpha,
            "flip": {"horizontal": self.flip_horizontal, "vertical": self.flip_vertical},
            "rotation": self.rotation,
            "scale": {"x": self.scale_x, "y": self.scale_y},
            "transform": {"x": self.transform_x, "y": self.transform_y}
        }
        return clip_settings_json

class Timerange:
    """记录了起始时间及持续长度的时间范围"""
    start: int
    """起始时间, 单位为微秒"""
    duration: int
    """持续长度, 单位为微秒"""

    def __init__(self, start: int, duration: int):
        self.start = start
        self.duration = duration

    def export_json(self) -> Dict[str, int]:
        return {"start": self.start, "duration": self.duration}

class Keyframe:
    """一个关键帧（关键点）, 目前只支持线性插值"""

    kf_id: str
    """关键帧全局id, 自动生成"""
    time_offset: int
    """相对于素材起始点的时间偏移量"""
    values: List[float]
    """关键帧的值, 似乎一般只有一个元素"""

    def __init__(self, time_offset: int, value: float):
        """给定时间偏移量及关键值, 初始化关键帧"""
        self.kf_id = uuid.uuid4().hex

        self.time_offset = time_offset
        self.values = [value]

    def export_json(self) -> Dict[str, Any]:
        return {
            # 默认值
            "curveType": "Line",
            "graphID": "",
            "left_control": {"x": 0.0, "y": 0.0},
            "right_control": {"x": 0.0, "y": 0.0},
            # 自定义属性
            "id": self.kf_id,
            "time_offset": self.time_offset,
            "values": self.values
        }

class Keyframe_property(Enum):
    """关键帧所控制的属性类型"""

    position_x = "KFTypePositionX"
    position_y = "KFTypePositionY"
    rotation = "KFTypeRotation"

    scale_x = "KFTypeScaleX"
    """单独控制X轴缩放比例"""
    scale_y = "KFTypeScaleY"
    """单独控制Y轴缩放比例"""
    uniform_scale = "UNIFORM_SCALE"
    """同时控制X轴及Y轴缩放比例"""

    alpha = "KFTypeAlpha"
    saturation = "KFTypeSaturation"
    contrast = "KFTypeContrast"
    brightness = "KFTypeBrightness"

class Keyframe_list:
    """关键帧列表, 记录与某个特定属性相关的一系列关键帧"""

    list_id: str
    """关键帧列表全局id, 自动生成"""
    keyframe_property: Keyframe_property
    """关键帧对应的属性"""
    keyframes: List[Keyframe]
    """关键帧列表"""

    def __init__(self, keyframe_property: Keyframe_property):
        """为给定的关键帧属性初始化关键帧列表"""
        self.list_id = uuid.uuid4().hex

        self.keyframe_property = keyframe_property
        self.keyframes = []

    def add_keyframe(self, time_offset: int, value: float):
        """给定时间偏移量及关键值, 向此关键帧列表中添加一个关键帧"""
        keyframe = Keyframe(time_offset, value)
        self.keyframes.append(keyframe)
        self.keyframes.sort(key=lambda x: x.time_offset)

    def export_json(self) -> Dict[str, Any]:
        keyframe_list_json = {
            "id": self.list_id,
            "keyframe_list": [kf.export_json() for kf in self.keyframes],
            "material_id": "",
            "property_type": self.keyframe_property.value
        }
        return keyframe_list_json


class Animation:
    """一个动画效果"""

    name: str
    """动画名称, 默认取为动画效果的名称"""
    effect_id: str
    """另一种动画id, 由剪映本身提供"""
    animation_type: str
    resource_id: str
    """资源id, 由剪映本身提供"""

    start: int
    """动画相对此片段开头的偏移, 单位为微秒"""
    duration: int
    """动画持续时间, 单位为微秒, 各动画有其默认值"""

    category_id: str
    category_name: str

    is_video_animation: bool

    def __init__(self, animation_type: Union[Video_intro_type, Video_outro_type], start: Optional[int] = None, duration: Optional[int] = None):
        type_meta = animation_type.value
        self.name = type_meta.title
        self.effect_id = type_meta.effect_id
        self.resource_id = type_meta.resource_id

        if isinstance(animation_type, Video_intro_type):
            self.animation_type = "in"
            self.category_id = "in"
            self.category_name = "入场"

            if start is None: start = 0
            if duration is None: duration = int(round(type_meta.duration * 1e6))
            self.is_video_animation = True
        elif isinstance(animation_type, Video_outro_type):
            self.animation_type = "out"
            self.category_id = "out"
            self.category_name = "出场"

            if duration is None: duration = int(round(type_meta.duration * 1e6))
            if start is None: raise ValueError("Outro animation must have a start time")
            self.is_video_animation = True

        self.start = start
        self.duration = duration

    def export_json(self) -> Dict[str, Any]:
        return {
            "anim_adjust_params": None,
            "platform": "all",
            "panel": "video" if self.is_video_animation else "",
            "material_type": "video" if self.is_video_animation else "sticker",

            "name": self.name,
            "id": self.effect_id,
            "type": self.animation_type,
            "resource_id": self.resource_id,
            "category_id": self.category_id,
            "category_name": self.category_name,

            "start": self.start,
            "duration": self.duration,
            # 不导出path和request_id字段
        }

class Segment_animations:
    """附加于某素材上的一系列动画（一般是入场、出场）"""
    animation_id: str
    animation_type: str

    animations: List[Animation]

    def __init__(self, animation_type: str = "sticker_animation"):
        self.animation_id = uuid.uuid4().hex
        self.animation_type = animation_type
        self.animations = []

    def add_animation(self, animation: Animation):
        self.animations.append(animation)

    def export_json(self) -> Dict[str, Any]:
        return {
            "id": self.animation_id,
            "type": self.animation_type,
            "multi_language_current": "none",
            "animations": [animation.export_json() for animation in self.animations]
        }

class Track_segment:
    """安放在轨道上的一个片段"""

    segment_id: str
    """片段全局id, 自动生成"""
    material_id: str
    """使用的素材id"""
    source_timerange: Timerange
    """截取的素材片段的时间范围"""
    target_timerange: Timerange
    """片段在轨道上的时间范围"""

    common_keyframes: List[Keyframe_list]
    """各属性的关键帧列表"""
    keyframe_refs: List[str]
    """意义不明"""
    extra_material_refs: List[str]
    """附加的素材id列表, 用于链接动画等"""
    clip_settings: Clip_settings
    """图像调节设置"""

    uniform_scale: bool
    """是否锁定XY轴缩放比例"""

    def __init__(self, material: Video_material,
                 target_timerange: Timerange,
                 source_timerange: Timerange = Timerange(0, 5000000),
                 clip_settings: Clip_settings = Clip_settings()):
        self.segment_id = uuid.uuid4().hex
        self.material_id = material.material_id

        self.clip_settings = clip_settings

        self.common_keyframes = []
        self.keyframe_refs = []
        self.extra_material_refs = []
        self.uniform_scale = True
        self.source_timerange = source_timerange
        self.target_timerange = target_timerange

    def attach_animation(self, animation: Segment_animations):
        """将给定的动画链接到此片段, 你仍然需要调用`Script_file.add_animation`来将动画添加到素材列表中"""
        self.extra_material_refs.append(animation.animation_id)

    def add_keyframe(self, _property: Keyframe_property, time_offset: int, value: float):
        """为给定属性创建一个关键帧, 并自动加入到关键帧列表中

        Args:
            _property (`Keyframe_property`): 要控制的属性
            time_offset (`int`): 关键帧的时间偏移量, 单位为微秒
            value (`float`): 属性在`time_offset`处的值
        """
        if (_property == Keyframe_property.scale_x or _property == Keyframe_property.scale_y) and self.uniform_scale:
            self.uniform_scale = False
        elif _property == Keyframe_property.uniform_scale:
            if not self.uniform_scale: raise ValueError("Cannot set uniform_scale when scale_x or scale_y already exist")
            _property = Keyframe_property.scale_x

        for kf_list in self.common_keyframes:
            if kf_list.keyframe_property == _property:
                kf_list.add_keyframe(time_offset, value)
                return
        kf_list = Keyframe_list(_property)
        kf_list.add_keyframe(time_offset, value)
        self.common_keyframes.append(kf_list)

    def export_json(self) -> Dict[str, Any]:
        fields = {
            # 定义一致字段的默认值
            "caption_info": None,
            "cartoon": False,
            "enable_adjust": True,
            "enable_color_correct_adjust": False,
            "enable_color_curves": True,
            "enable_color_match_adjust": False,
            "enable_color_wheels": True,
            "enable_lut": True,
            "enable_smart_color_adjust": False,
            "group_id": "",
            "hdr_settings": {"intensity": 1.0, "mode": 1, "nits": 1000},
            "intensifies_audio": False,
            "is_placeholder": False,
            "is_tone_modify": False,
            "last_nonzero_volume": 1.0,
            "render_index": 0,
            "responsive_layout": {"enable": False, "horizontal_pos_layout": 0, "size_layout": 0, "vertical_pos_layout": 0, "target_follow": ""},
            "reverse": False,
            "speed": 1.0,
            "template_id": "",
            "template_scene": "default",
            "track_attribute": 0,
            "track_render_index": 0,
            "visible": True,
            "volume": 1.0,
            # 写入自定义字段
            "id": self.segment_id,
            "material_id": self.material_id,
            "common_keyframes": [kf_list.export_json() for kf_list in self.common_keyframes],
            "extra_material_refs": self.extra_material_refs,
            "keyframe_refs": self.keyframe_refs,
            "source_timerange": self.source_timerange.export_json(),
            "target_timerange": self.target_timerange.export_json(),
            "clip": self.clip_settings.export_json(),
            "uniform_scale": {"on": self.uniform_scale, "value": 1.0},
        }

        return fields

class Script_file:

    content: Dict[str, Any]

    TEMPLATE_FILE = "draft_content_template.json"

    def __init__(self):
        with open(self.TEMPLATE_FILE, "r", encoding="utf-8") as f:
            self.content = json.load(f)

    def add_material(self, material: Video_material):
        self.content["materials"]["videos"].append(material.export_json())

    def add_segment(self, segment: Track_segment):
        self.content["tracks"][0]["segments"].append(segment.export_json())
        self.content["duration"] = max(self.content["duration"], segment.target_timerange.start + segment.target_timerange.duration)

    def add_animation(self, animation: Segment_animations):
        self.content["materials"]["material_animations"].append(animation.export_json())

    def dumps(self) -> str:
        return json.dumps(self.content, ensure_ascii=False, indent=4)
