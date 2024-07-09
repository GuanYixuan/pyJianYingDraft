import os
import json, uuid
import imageio

from enum import Enum
from typing import Optional, Dict, List, Any

class Crop_settings:
    """素材的裁剪设置, 各属性均在0-1之间"""

    upper_left_x: float
    upper_left_y: float
    upper_right_x: float
    upper_right_y: float
    lower_left_x: float
    lower_left_y: float
    lower_right_x: float
    lower_right_y: float

    def __init__(self, upper_left_x: float = 0.0, upper_left_y: float = 0.0,
                 upper_right_x: float = 1.0, upper_right_y: float = 0.0,
                 lower_left_x: float = 0.0, lower_left_y: float = 1.0,
                 lower_right_x: float = 1.0, lower_right_y: float = 1.0):
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
    local_material_id: str
    material_name: str
    path: str
    duration: int
    height: int
    width: int
    crop_settings: Crop_settings
    material_type: str

    VIDEO_POSTFIX = (".mp4", ".mov", ".avi", ".flv", ".wmv", ".rmvb", ".mkv")
    IMAGE_POSTFIX = (".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".psd", ".eps", ".svg")

    def __init__(self, path: str, material_name: Optional[str] = None,
                 crop_settings: Crop_settings = Crop_settings(), local_material_id: str = ""):
        self.material_name = material_name if material_name else os.path.basename(path)
        self.material_id = uuid.uuid3(uuid.NAMESPACE_DNS, self.material_name).hex
        self.path = path
        self.crop_settings = crop_settings
        self.local_material_id = local_material_id

        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} does not exist")
        postfix = os.path.splitext(path)[1]
        if postfix in self.VIDEO_POSTFIX:
            vid = imageio.get_reader(path)

            self.material_type = "video"
            self.duration = int(vid.get_meta_data()['duration'])
            self.height, self.width = [int(x) for x in vid.get_meta_data()["size"]]
            vid.close()
        elif postfix in self.IMAGE_POSTFIX:
            pic = imageio.imread(path)

            self.material_type = "photo"
            self.duration = 10800000000
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
    alpha: float
    flip_horizontal: bool
    flip_vertical: bool
    rotation: float
    scale_x: float
    scale_y: float
    transform_x: float
    transform_y: float

    def __init__(self, alpha: float = 1.0,
                 flip_horizontal: bool = False, flip_vertical: bool = False,
                 rotation: float = 0.0,
                 scale_x: float = 1.0, scale_y: float = 1.0,
                 transform_x: float = 0.0, transform_y: float = 0.0):
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
    start: int
    duration: int

    def __init__(self, start: int, duration: int):
        self.start = start
        self.duration = duration

    def export_json(self) -> Dict[str, int]:
        return {"start": self.start, "duration": self.duration}

class Keyframe:
    """关键帧"""
    kf_id: str
    time_offset: int
    """相对于素材起始时间的偏移量"""
    values: List[float]

    def __init__(self, time_offset: int, value: float):
        self.kf_id = uuid.uuid4().hex

        self.time_offset = time_offset
        self.values = [value]

    def export_json(self) -> Dict[str, Any]:
        return {
            # 定义一致字段的默认值
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
    KFTypePositionX = "position_x",
    KFTypePositionY = "position_y",
    KFTypeRotation = "rotation",
    KFTypeScaleX = "scale_x",
    KFTypeScaleY = "scale_y",
    KFTypeAlpha = "alpha",
    KFTypeSaturation = "saturation",
    KFTypeContrast = "contrast",
    KFTypeBrightness = "brightness",

class Keyframe_list:
    """关键帧列表，记录某个特定属性的一系列关键帧"""
    list_id: str

    keyframe_property: Keyframe_property
    keyframes: List[Keyframe]

    def __init__(self, keyframe_property: Keyframe_property):
        self.list_id = uuid.uuid4().hex

        self.keyframe_property = keyframe_property
        self.keyframes = []

    def add_keyframe(self, time_offset: int, value: float):
        keyframe = Keyframe(time_offset, value)
        self.keyframes.append(keyframe)
        self.keyframes.sort(key=lambda x: x.time_offset)

    def export_json(self) -> Dict[str, Any]:
        keyframe_list_json = {
            "id": self.list_id,
            "keyframe_list": [kf.export_json() for kf in self.keyframes],
            "material_id": "",
            "property_type": self.keyframe_property.name
        }
        return keyframe_list_json

