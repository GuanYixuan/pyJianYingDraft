"""定义时间范围类以及与时间相关的辅助函数"""

from typing import Dict, Optional, Union

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
        return cls(int(json_obj.get("start", 0)), int(json_obj["duration"]))

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


def trange_seconds(start: Union[int, float], *,
                   end: Optional[Union[int, float]] = None,
                   duration: Optional[Union[int, float]] = None) -> Timerange:
    """用**秒数**起点及终点或时长构造时间范围

    分别将起点和终点取整到微秒，再计算整数微秒时长。相同的秒数时长在不同
    起点处可能得到相差1微秒的结果；连续片段建议共用绝对终点作为下一段起点。

    Args:
        start (int or float): 起点，单位为秒，可为负数
        end (int or float, optional): 终点，单位为秒，与duration只能提供一个
        duration (int or float, optional): 时长，单位为秒，与end只能提供一个

    Raises:
        TypeError: 提供了非数值参数
        ValueError: end和duration未提供或同时提供，数值非有限，或时间范围为负
    """
    if (end is None) == (duration is None):
        raise ValueError("必须且只能提供end或duration其中一个参数")

    for name, value in (("start", start), ("end", end), ("duration", duration)):
        if value is None:
            continue
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{name}必须是以秒为单位的数值")

    if duration is not None:
        if duration < 0:
            raise ValueError(f"duration不能为负数: {duration}")
        end_seconds = start + duration
    elif end is not None:
        end_seconds = end
    else:
        raise ValueError("必须且只能提供end或duration其中一个参数")

    if end_seconds < start:
        raise ValueError(f"end不能早于start: start={start}, end={end_seconds}")

    start_us = round(start * SEC)
    end_us = round(end_seconds * SEC)
    return Timerange(start_us, end_us - start_us)


def srt_tstamp(srt_tstamp: str) -> int:
    """解析srt中的时间戳字符串, 返回微秒数"""
    sec_str, ms_str = srt_tstamp.split(",")
    parts = sec_str.split(":") + [ms_str]

    total_time = 0
    for value, factor in zip(parts, [3600*SEC, 60*SEC, SEC, 1000]):
        total_time += int(value) * factor
    return total_time
