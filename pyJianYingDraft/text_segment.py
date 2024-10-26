"""定义文本片段及其相关类"""

import json
import uuid

from typing import Dict, List, Tuple, Any
from typing import Union, Optional, Literal

from .time_util import Timerange, tim
from .segment import Base_segment, Clip_settings
from .animation import Segment_animations, Text_animation

from .metadata import Text_intro, Text_outro, Text_loop_anim

class Text_style:
    """字体样式类"""

    size: float
    """字体大小"""

    bold: bool
    """是否加粗"""
    italic: bool
    """是否斜体"""
    underline: bool
    """是否加下划线"""

    color: Tuple[float, float, float]
    """字体颜色, RGB三元组, 取值范围为[0, 1]"""
    alpha: float
    """字体不透明度"""

    align: Literal[0, 1, 2]
    """对齐方式"""
    vertical: bool
    """竖排文本"""

    def __init__(self, *, size: float = 8.0, bold: bool = False, italic: bool = False, underline: bool = False,
                 color: Tuple[float, float, float] = (1.0, 1.0, 1.0), alpha: float = 1.0,
                 align: Literal[0, 1, 2] = 0, vertical: bool = False):
        """
        Args:
            size (`float`, optional): 字体大小, 默认为8.0
            bold (`bool`, optional): 是否加粗, 默认为否
            italic (`bool`, optional): 是否斜体, 默认为否
            underline (`bool`, optional): 是否加下划线, 默认为否
            color (`Tuple[float, float, float]`, optional): 字体颜色, RGB三元组, 取值范围为[0, 1], 默认为白色
            alpha (`float`, optional): 字体不透明度, 取值范围[0, 1], 默认不透明
            align (`int`, optional): 对齐方式, 0: 左对齐, 1: 居中, 2: 右对齐, 默认为左对齐
            vertical (`bool`, optional): 是否是竖排文本, 默认为否
        """
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline

        self.color = color
        self.alpha = alpha

        self.align = align
        self.vertical = vertical

class Text_border:
    """文本描边的参数"""

    alpha: float
    """描边不透明度"""
    color: Tuple[float, float, float]
    """描边颜色, RGB三元组, 取值范围为[0, 1]"""
    width: float
    """描边宽度"""

    def __init__(self, *, alpha: float = 1.0, color: Tuple[float, float, float] = (0.0, 0.0, 0.0), width: float = 40.0):
        """
        Args:
            alpha (`float`, optional): 描边不透明度, 取值范围[0, 1], 默认为1.0
            color (`Tuple[float, float, float]`, optional): 描边颜色, RGB三元组, 取值范围为[0, 1], 默认为黑色
            width (`float`, optional): 描边宽度, 与剪映中一致, 取值范围为[0, 100], 默认为40.0
        """
        self.alpha = alpha
        self.color = color
        self.width = width / 100.0 * 0.2  # 此映射可能不完全正确

    def export_json(self) -> Dict[str, Any]:
        """导出JSON数据, 放置在素材content的styles中"""
        return {
            "content": {
                "solid": {
                    "alpha": self.alpha,
                    "color": list(self.color),
                }
            },
            "width": self.width
        }

class Text_segment(Base_segment):
    """文本片段类, 目前仅支持设置基本的字体样式"""

    text: str
    """文本内容"""
    style: Text_style
    """字体样式"""

    clip_settings: Clip_settings
    """图像调节设置"""
    border: Optional[Text_border]
    """文本描边参数, None表示无描边"""

    animations_instance: Optional[Segment_animations]
    """动画实例, 可能为空

    在放入轨道时自动添加到素材列表中
    """

    extra_material_refs: List[str]
    """附加的素材id列表, 用于链接动画/特效等"""

    def __init__(self, text: str, timerange: Timerange, *,
                 style: Optional[Text_style] = None, clip_settings: Optional[Clip_settings] = None,
                 border: Optional[Text_border] = None):
        """创建文本片段, 并指定其时间信息、字体样式及图像调节设置

        片段创建完成后, 可通过`Script_file.add_segment`方法将其添加到轨道中

        Args:
            text (`str`): 文本内容
            timerange (`Timerange`): 片段在轨道上的时间范围
            style (`Text_style`, optional): 字体样式
            clip_settings (`Clip_settings`, optional): 图像调节设置, 默认不做任何变换
            border (`Text_border`, optional): 文本描边参数, 默认无描边
        """
        super().__init__(uuid.uuid4().hex, timerange)

        self.text = text
        self.style = style or Text_style()
        self.clip_settings = clip_settings or Clip_settings()
        self.border = border

        self.animations_instance = None
        self.extra_material_refs = []

    def add_animation(self, animation_type: Union[Text_intro, Text_outro, Text_loop_anim],
                      duration: Union[str, float] = 500000) -> "Text_segment":
        """将给定的入场/出场/循环动画添加到此片段的动画列表中, 出入场动画的持续时间可以自行设置, 循环动画则会自动填满其余无动画部分

        注意: 若希望同时使用循环动画和入出场动画, 请**先添加出入场动画再添加循环动画**

        Args:
            animation_type (`Text_intro`, `Text_outro` or `Text_loop_anim`): 文本动画类型.
            duration (`str` or `float`, optional): 动画持续时间, 单位为微秒, 仅对入场/出场动画有效.
                若传入字符串则会调用`tim()`函数进行解析. 默认为0.5秒
        """
        duration = min(tim(duration), self.target_timerange.duration)

        if isinstance(animation_type, Text_intro):
            start = 0
        elif isinstance(animation_type, Text_outro):
            start = self.target_timerange.duration - duration
        elif isinstance(animation_type, Text_loop_anim):
            intro_trange = self.animations_instance and self.animations_instance.get_animation_trange("in")
            outro_trange = self.animations_instance and self.animations_instance.get_animation_trange("out")
            start = intro_trange.start if intro_trange else 0
            duration = self.target_timerange.duration - start - (outro_trange.duration if outro_trange else 0)
        else:
            raise TypeError("Invalid animation type %s" % type(animation_type))

        if self.animations_instance is None:
            self.animations_instance = Segment_animations()
            self.extra_material_refs.append(self.animations_instance.animation_id)

        self.animations_instance.add_animation(Text_animation(animation_type, start, duration))

        return self

    def export_material(self) -> Dict[str, Any]:
        """与此文本片段联系的素材, 以此不再单独定义Text_material类"""
        # 叠加各类效果的flag
        check_flag: int = 7
        if self.border: check_flag |= 8

        return {
            "add_type": 0,

            "typesetting": int(self.style.vertical),
            "alignment": self.style.align,

            # ?
            # "caption_template_info": {
            #     "category_id": "",
            #     "category_name": "",
            #     "effect_id": "",
            #     "is_new": False,
            #     "path": "",
            #     "request_id": "",
            #     "resource_id": "",
            #     "resource_name": "",
            #     "source_platform": 0
            # },

            # 混合 (+4)
            # "global_alpha": 1.0,

            # 描边 (+8), 似乎也会被content覆盖
            # "border_alpha": 1.0,
            # "border_color": "",
            # "border_width": 0.08,

            # 背景 (+16)
            # "background_style": 0,
            # "background_color": "",
            # "background_alpha": 1.0,
            # "background_round_radius": 0.0,
            # "background_height": 0.14,
            # "background_width": 0.14,
            # "background_horizontal_offset": 0.0,
            # "background_vertical_offset": 0.0,

            # 发光 (+64)，属性由extra_material_refs记录

            # 阴影 (+32)
            # "has_shadow": False,
            # "shadow_alpha": 0.9,
            # "shadow_angle": -45.0,
            # "shadow_color": "",
            # "shadow_distance": 5.0,
            # "shadow_point": {
            #     "x": 0.6363961030678928,
            #     "y": -0.6363961030678928
            # },
            # "shadow_smoothing": 0.45,

            # 整体字体设置, 似乎会被content覆盖
            # "font_category_id": "",
            # "font_category_name": "",
            # "font_id": "",
            # "font_name": "",
            # "font_path": "",
            # "font_resource_id": "",
            # "font_size": 15.0,
            # "font_source_platform": 0,
            # "font_team_id": "",
            # "font_title": "none",
            # "font_url": "",
            # "fonts": [],

            # 似乎会被content覆盖
            # "text_alpha": 1.0,
            # "text_color": "#FFFFFF",
            # "text_curve": None,
            # "text_preset_resource_id": "",
            # "text_size": 30,
            # "underline": False,


            "base_content": "",
            "bold_width": 0.0,

            "check_flag": check_flag,
            "combo_info": {
                "text_templates": []
            },
            "content": json.dumps({
                "styles": [
                    {
                        "fill": {
                            "alpha": 1.0,
                            "content": {
                                "render_type": "solid",
                                "solid": {
                                    "alpha": self.style.alpha,
                                    "color": list(self.style.color)
                                }
                            }
                        },
                        # "font": {
                        #     "id": "",
                        #     "path": "***.ttf"
                        # },
                        "range": [0, len(self.text)],
                        "size": self.style.size,
                        "bold": self.style.bold,
                        "italic": self.style.italic,
                        "underline": self.style.underline,
                        "strokes": [self.border.export_json()] if self.border else []
                    }
                ],
                "text": self.text
            }),
            "fixed_height": -1.0,
            "fixed_width": -1.0,
            "force_apply_line_max_width": False,

            "group_id": "",

            "id": self.material_id,
            "initial_scale": 1.0,
            "inner_padding": -1.0,
            "is_rich_text": False,
            "italic_degree": 0,
            "ktv_color": "",
            "language": "",
            "layer_weight": 1,
            "letter_spacing": 0.0,
            "line_feed": 1,
            "line_max_width": 0.82,
            "line_spacing": 0.02,
            "multi_language_current": "none",
            "name": "",
            "original_size": [],

            "preset_category": "",
            "preset_category_id": "",
            "preset_has_set_alignment": False,
            "preset_id": "",
            "preset_index": 0,
            "preset_name": "",

            "recognize_task_id": "",
            "recognize_type": 0,
            "relevance_segment": [],

            "shape_clip_x": False,
            "shape_clip_y": False,
            "source_from": "",
            "style_name": "",
            "sub_type": 0,
            "subtitle_keywords": None,
            "subtitle_template_original_fontsize": 0.0,
            "text_to_audio_ids": [],
            "tts_auto_update": False,
            "type": "text",

            "underline_offset": 0.22,
            "underline_width": 0.05,

            "use_effect_default_color": True,
            "words": {
                "end_time": [],
                "start_time": [],
                "text": []
            }
        }

    def export_json(self) -> Dict[str, Any]:
        ret = super().export_json()
        ret.update({
            # 与Video_segment一致的部分
            "clip": self.clip_settings.export_json(),
            # "hdr_settings": null,
            # "uniform_scale": {},

            # 与Media_segment一致的部分
            "source_timerange": None,
            "speed": 1.0,
            "volume": 1.0,
            "extra_material_refs": self.extra_material_refs,
        })
        return ret
