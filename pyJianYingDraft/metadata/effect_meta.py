"""元数据类型定义"""

from enum import Enum

from typing import List, Dict, Any
from typing import TypeVar, Optional

class EffectParam:
    """特效参数信息"""

    name: str
    """参数名称"""
    default_value: float
    """默认值"""
    min_value: float
    """最小值"""
    max_value: float
    """最大值"""

    def __init__(self, name: str, default_value: float, min_value: float, max_value: float):
        self.name = name
        self.default_value = default_value
        self.min_value = min_value
        self.max_value = max_value

class EffectParamInstance(EffectParam):
    """特效参数实例"""

    index: int
    """参数索引"""
    value: float
    """当前值"""

    def __init__(self, meta: EffectParam, index: int, value: float):
        super().__init__(meta.name, meta.default_value, meta.min_value, meta.max_value)
        self.index = index
        self.value = value

    def export_json(self) -> Dict[str, Any]:
        return {
            "default_value": self.default_value,
            "max_value": self.max_value,
            "min_value": self.min_value,
            "name": self.name,
            "parameterIndex": self.index,
            "portIndex": 0,
            "value": self.value
        }

# 基础特效元数据, 直接用于滤镜/文字/视频特效
class EffectMeta:
    """特效元数据, 直接用于滤镜/文字/视频特效"""

    name: str
    """效果名称"""
    is_vip: bool
    """是否为VIP特权"""

    resource_id: str
    """资源ID"""
    effect_id: str
    """效果ID"""
    md5: str

    params: List[EffectParam]
    """效果的参数信息"""

    def __init__(self, name: str, is_vip: bool, resource_id: str, effect_id: str, md5: str, params: List[EffectParam] = []):
        self.name = name
        self.is_vip = is_vip
        self.resource_id = resource_id
        self.effect_id = effect_id
        self.md5 = md5
        self.params = params

    def parse_params(self, params: Optional[List[Optional[float]]]) -> List[EffectParamInstance]:
        """解析参数列表(范围0~100), 返回参数实例列表"""
        ret: List[EffectParamInstance] = []

        if params is None: params = []
        for i, param in enumerate(self.params):
            val = param.default_value
            if i < len(params):
                input_v = params[i]
                if input_v is not None:
                    if input_v < 0 or input_v > 100:
                        raise ValueError("Invalid parameter value %f within %s" % (input_v, str(param)))
                    val = param.min_value + (param.max_value - param.min_value) * input_v / 100.0  # 从0~100映射到实际值
            ret.append(EffectParamInstance(param, i, val))
        return ret


EffectEnumSubclass = TypeVar("EffectEnumSubclass", bound="EffectEnum")

class EffectEnum(Enum):
    """特效枚举基类, 提供一个`from_name`方法用于根据名称获取特效元数据"""

    @classmethod
    def from_name(cls: "type[EffectEnumSubclass]", name: str) -> EffectEnumSubclass:
        """根据名称获取特效元数据, 忽略大小写、空格和下划线

        Args:
            name (str): 特效名称

        Raises:
            `ValueError`: 特效名称不存在
        """
        name = name.lower().replace(" ", "").replace("_", "")
        for effect in cls:
            if effect.name.lower().replace(" ", "").replace("_", "") == name:
                return effect
        raise ValueError(f"Effect named '{name}' not found")

# 动画元数据
class AnimationMeta:
    """动画元数据, 用于视频/文字片段的入场/出场/组合动画"""

    title: str
    is_vip: bool
    duration: int
    """效果默认时长, 单位为微秒"""

    resource_id: str
    effect_id: str
    md5: str

    def __init__(self, title: str, is_vip: bool, duration: float, resource_id: str, effect_id: str, md5: str):
        self.title = title
        self.is_vip = is_vip
        self.duration = int(round(duration * 1e6))
        self.resource_id = resource_id
        self.effect_id = effect_id
        self.md5 = md5

# 蒙版元数据
class MaskMeta:
    """蒙版元数据"""

    name: str
    """转场名称"""

    resource_type: str
    """资源类型, 与蒙版形状相关"""

    resource_id: str
    """资源ID"""
    effect_id: str
    """效果ID"""
    md5: str

    default_aspect_ratio: float
    """默认宽高比(宽高都是相对素材的比例)"""

    def __init__(self, name: str, resource_type: str, resource_id: str, effect_id: str, md5: str, default_aspect_ratio: float):
        self.name = name
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.effect_id = effect_id
        self.md5 = md5

        self.default_aspect_ratio = default_aspect_ratio

# 转场元数据
class TransitionMeta:
    """转场元数据"""

    name: str
    """转场名称"""
    is_vip: bool
    """是否为VIP特权"""

    resource_id: str
    """资源ID"""
    effect_id: str
    """效果ID"""
    md5: str

    default_duration: int
    """默认持续时间, 单位为微秒"""
    is_overlap: bool
    """是否允许重叠(?)"""

    def __init__(self, name: str, is_vip: bool, resource_id: str, effect_id: str, md5: str, default_duration: float, is_overlap: bool):
        self.name = name
        self.is_vip = is_vip
        self.resource_id = resource_id
        self.effect_id = effect_id
        self.md5 = md5

        self.default_duration = int(round(default_duration * 1e6))
        self.is_overlap = is_overlap
