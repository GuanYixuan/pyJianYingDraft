"""定义视频/文本动画相关类"""

import uuid

from typing import Union, Optional
from typing import Literal, Dict, List, Any

from .time_util import Timerange

from .metadata import AnimationMeta
from .metadata import IntroType, OutroType, GroupAnimationType
from .metadata import TextIntro, TextOutro, TextLoopAnim

class Animation:
    """一个视频/文本动画效果"""

    name: str
    """动画名称, 默认取为动画效果的名称"""
    effect_id: str
    """另一种动画id, 由剪映本身提供"""
    animation_type: str
    """动画类型, 在子类中定义"""
    resource_id: str
    """资源id, 由剪映本身提供"""

    start: int
    """动画相对此片段开头的偏移, 单位为微秒"""
    duration: int
    """动画持续时间, 单位为微秒"""

    is_video_animation: bool
    """是否为视频动画, 在子类中定义"""

    def __init__(self, animation_meta: AnimationMeta, start: int, duration: int):
        self.name = animation_meta.title
        self.effect_id = animation_meta.effect_id
        self.resource_id = animation_meta.resource_id

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

            "start": self.start,
            "duration": self.duration,
            # 不导出path和request_id
        }

class VideoAnimation(Animation):
    """一个视频动画效果"""

    animation_type: Literal["in", "out", "group"]

    def __init__(self, animation_type: Union[IntroType, OutroType, GroupAnimationType],
                 start: int, duration: int):
        super().__init__(animation_type.value, start, duration)

        if isinstance(animation_type, IntroType):
            self.animation_type = "in"
        elif isinstance(animation_type, OutroType):
            self.animation_type = "out"
        elif isinstance(animation_type, GroupAnimationType):
            self.animation_type = "group"

        self.is_video_animation = True

class Text_animation(Animation):
    """一个文本动画效果"""

    animation_type: Literal["in", "out", "loop"]

    def __init__(self, animation_type: Union[TextIntro, TextOutro, TextLoopAnim],
                 start: int, duration: int):
        super().__init__(animation_type.value, start, duration)

        if isinstance(animation_type, TextIntro):
            self.animation_type = "in"
        elif isinstance(animation_type, TextOutro):
            self.animation_type = "out"
        elif isinstance(animation_type, TextLoopAnim):
            self.animation_type = "loop"

        self.is_video_animation = False

class SegmentAnimations:
    """附加于某素材上的一系列动画

    对视频片段：入场、出场或组合动画；对文本片段：入场、出场或循环动画"""

    animation_id: str
    """系列动画的全局id, 自动生成"""

    animations: List[Animation]
    """动画列表"""

    def __init__(self):
        self.animation_id = uuid.uuid4().hex
        self.animations = []

    def get_animation_trange(self, animation_type: Literal["in", "out", "group", "loop"]) -> Optional[Timerange]:
        """获取指定类型的动画的时间范围"""
        for animation in self.animations:
            if animation.animation_type == animation_type:
                return Timerange(animation.start, animation.duration)
        return None

    def add_animation(self, animation: Union[VideoAnimation, Text_animation]) -> None:
        # 不允许添加超过一个同类型的动画（如两个入场动画）
        if animation.animation_type in [ani.animation_type for ani in self.animations]:
            raise ValueError(f"当前片段已存在类型为 '{animation.animation_type}' 的动画")

        if isinstance(animation, VideoAnimation):
            # 不允许组合动画与出入场动画同时出现
            if any(ani.animation_type == "group" for ani in self.animations):
                raise ValueError("当前片段已存在组合动画, 此时不能添加其它动画")
            if animation.animation_type == "group" and len(self.animations) > 0:
                raise ValueError("当前片段已存在动画时, 不能添加组合动画")
        elif isinstance(animation, Text_animation):
            if any(ani.animation_type == "loop" for ani in self.animations):
                raise ValueError("当前片段已存在循环动画, 若希望同时使用循环动画和入出场动画, 请先添加出入场动画再添加循环动画")

        self.animations.append(animation)

    def export_json(self) -> Dict[str, Any]:
        return {
            "id": self.animation_id,
            "type": "sticker_animation",
            "multi_language_current": "none",
            "animations": [animation.export_json() for animation in self.animations]
        }
