"""自定义异常类"""

class TrackNotFound(NameError):
    """未找到满足条件的轨道"""
class AmbiguousTrack(ValueError):
    """找到多个满足条件的轨道"""
class SegmentOverlap(ValueError):
    """新片段与已有的轨道片段重叠"""

class ExtensionFailed(ValueError):
    """替换素材时延伸片段失败"""
