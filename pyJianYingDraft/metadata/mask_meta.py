"""视频蒙版元数据"""

from .effect_meta import Effect_enum

class Mask_meta:
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

class Mask_type(Effect_enum):
    """蒙版类型"""

    线性 = Mask_meta("线性", "line", "6791652175668843016", "636071", "1f467b8b9bb94cecc46d916219b7940a", 1.0)
    """默认遮挡下方部分"""
    镜面 = Mask_meta("镜面", "mirror", "6791699060140020232", "636073", "b2c0516d1f737f4542fb9b2862907817", 1.0)
    """默认保留两线之间部分"""
    圆形 = Mask_meta("圆形", "circle", "6791700663249146381", "636075", "9a55eae0e99ee6d1ecbc6defaf0501ec", 1.0)
    矩形 = Mask_meta("矩形", "rectangle", "6791700809454195207", "636077", "ef361d96c456cd6077c76d737f98898d", 1.0)
    爱心 = Mask_meta("爱心", "geometric_shape", "6794051276482023949", "636079", "0bf09fa1e3a32464fed4f71e49a8ab01", 1.115)
    星形 = Mask_meta("星形", "geometric_shape", "6794051169434997255", "636081", "155612dee601d3f5422a3fbeabc7610c", 1.05)
