import os
import uuid
import imageio
import pymediainfo

from typing import Optional, Literal
from typing import Dict, List, Any

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
    """本地视频素材（视频或图片）, 一份素材可以在多个片段中使用"""

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

class Audio_material:
    """本地音频素材"""

    material_id: str
    """素材全局id, 自动生成"""
    material_name: str
    """素材名称"""
    path: str
    """素材文件路径"""

    duration: int
    """素材时长, 单位为微秒"""

    def __init__(self, path: str, material_name: Optional[str] = None):
        """从指定位置加载音频素材

        Args:
            path (`str`): 素材文件路径, 支持mp3, wav等常见音频文件.
            material_name (`str`, optional): 素材名称, 如果不指定, 默认使用文件名作为素材名称.

        Raises:
            `FileNotFoundError`: 素材文件不存在.
            `ValueError`: 不支持的素材文件类型.
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} does not exist")

        self.material_name = material_name if material_name else os.path.basename(path)
        self.material_id = uuid.uuid3(uuid.NAMESPACE_DNS, self.material_name).hex
        self.path = path

        if not pymediainfo.MediaInfo.can_parse():
            raise ValueError("Unsupported file type %s" % os.path.splitext(path)[1])
        info: pymediainfo.MediaInfo = pymediainfo.MediaInfo.parse(path)  # type: ignore
        self.duration = int(info.audio_tracks[0].duration * 1e3)  # type: ignore

    def export_json(self) -> Dict[str, Any]:
        return {
            "app_id": 0,
            "category_id": "",
            "category_name": "local",
            "check_flag": 1,
            "copyright_limit_type": "none",
            "duration": self.duration,
            "effect_id": "",
            "formula_id": "",
            "id": self.material_id,
            "intensifies_path": "",
            "is_ai_clone_tone": False,
            "is_text_edit_overdub": False,
            "is_ugc": False,
            "local_material_id": self.material_id,
            "music_id": self.material_id,
            "name": self.material_name,
            "path": self.path,
            "query": "",
            "request_id": "",
            "resource_id": "",
            "search_id": "",
            "source_from": "",
            "source_platform": 0,
            "team_id": "",
            "text_id": "",
            "tone_category_id": "",
            "tone_category_name": "",
            "tone_effect_id": "",
            "tone_effect_name": "",
            "tone_platform": "",
            "tone_second_category_id": "",
            "tone_second_category_name": "",
            "tone_speaker": "",
            "tone_type": "",
            "type": "extract_music",
            "video_id": "",
            "wave_points": []
        }
