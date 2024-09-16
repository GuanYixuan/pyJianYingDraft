"""定义时间范围类以及与时间相关的辅助函数"""

from typing import Union
from typing import Dict

SEC = 1000000
"""一秒=1e6微秒"""

def tim(inp: Union[str, float]) -> int:
    """将输入的字符串转换为微秒, 也可直接输入微秒数

    支持类似 "1h52m3s" 或 "0.15s" 这样的格式, 可包含负号以表示负偏移
    """
    if isinstance(inp, (int, float)):
        return int(round(inp))

    sign: int = 1
    inp = inp.strip().lower()
    if inp.startswith("-"):
        sign = -1
        inp = inp[1:]

    last_index: int = 0
    total_time: float = 0
    for unit, factor in zip(["h", "m", "s"], [3600*SEC, 60*SEC, SEC]):
        unit_index = inp.find(unit)
        if unit_index == -1: continue

        total_time += float(inp[last_index:unit_index]) * factor
        last_index = unit_index + 1

    return int(round(total_time) * sign)

class Timerange:
    """记录了起始时间及持续长度的时间范围"""
    start: int
    """起始时间, 单位为微秒"""
    duration: int
    """持续长度, 单位为微秒"""

    def __init__(self, start: int, duration: int):
        """构造一个时间范围

        Args:
            start (int): 起始时间, 单位为微秒
            duration (int): 持续长度, 单位为微秒
        """

        self.start = start
        self.duration = duration

    @classmethod
    def import_json(cls, json_obj: Dict[str, str]) -> "Timerange":
        """从json对象中恢复Timerange"""
        return cls(int(json_obj["start"]), int(json_obj["duration"]))

    @property
    def end(self) -> int:
        """结束时间, 单位为微秒"""
        return self.start + self.duration

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Timerange):
            return False
        return self.start == other.start and self.duration == other.duration

    def overlaps(self, other: "Timerange") -> bool:
        """判断两个时间范围是否有重叠"""
        return not (self.end <= other.start or other.end <= self.start)

    def __repr__(self) -> str:
        return f"Timerange(start={self.start}, duration={self.duration})"

    def __str__(self) -> str:
        return f"[start={self.start}, end={self.end}]"

    def export_json(self) -> Dict[str, int]:
        return {"start": self.start, "duration": self.duration}

def trange(start: Union[str, float], duration: Union[str, float]) -> Timerange:
    """Timerange的简便构造函数, 接受字符串或微秒数作为参数

    支持类似 "1h52m3s" 或 "0.15s" 这样的格式

    Args:
        start (Union[str, float]): 起始时间
        duration (Union[str, float]): 持续长度, 注意**不是结束时间**
    """
    return Timerange(tim(start), tim(duration))

def srt_tstamp(srt_tstamp: str) -> int:
    """解析srt中的时间戳字符串, 返回微秒数"""
    sec_str, ms_str = srt_tstamp.split(",")
    parts = sec_str.split(":") + [ms_str]

    total_time = 0
    for value, factor in zip(parts, [3600*SEC, 60*SEC, SEC, 1000]):
        total_time += int(value) * factor
    return total_time
