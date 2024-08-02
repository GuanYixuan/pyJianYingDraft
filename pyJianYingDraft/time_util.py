"""定义时间范围类以及与时间相关的辅助函数"""

from typing import Union
from typing import Dict

SEC = 1000000
"""一秒=1e6微秒"""

def tim(inp: Union[str, float]) -> int:
    """将输入的字符串转换为微秒, 也可直接输入微秒数

    支持类似 "1h52m3s" 或 "0.15s" 这样的格式
    """
    if isinstance(inp, (int, float)):
        return int(round(inp))

    inp = inp.strip().lower()
    last_index: int = 0
    total_time: float = 0
    for unit, factor in zip(["h", "m", "s"], [3600*SEC, 60*SEC, SEC]):
        unit_index = inp.find(unit)
        if unit_index == -1: continue

        total_time += float(inp[last_index:unit_index]) * factor
        last_index = unit_index + 1

    return int(round(total_time))

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

def trange(start: Union[str, float], duration: Union[str, float]) -> Timerange:
        """Timerange的简便构造函数, 接受字符串或微秒数作为参数

        支持类似 "1h52m3s" 或 "0.15s" 这样的格式

        Args:
            start (Union[str, float]): 起始时间
            duration (Union[str, float]): 持续长度
        """
        return Timerange(tim(start), tim(duration))