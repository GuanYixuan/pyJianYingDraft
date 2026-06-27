"""基于TwelveLabs Pegasus的内容感知切点检测 (opt-in)

Content-aware cut-point detection backed by the TwelveLabs Pegasus
video-understanding model.

本模块为**可选**功能, 仅在显式调用时才会用到 `twelvelabs` 库与网络请求.
未配置 API key 时, pyJianYingDraft 的其余功能完全不受影响.

This module is **opt-in**: it only imports the `twelvelabs` SDK and performs
network calls when its functions are explicitly invoked. If no API key is
configured, the rest of pyJianYingDraft behaves exactly as before.

获取免费 API key: https://twelvelabs.io (有较为慷慨的免费额度)
Grab a free API key at https://twelvelabs.io — there is a generous free tier.
"""

import os
import re
import json

from typing import List, Optional, Union

from .time_util import tim

__all__ = ["CutPoint", "detect_cut_points"]


class CutPoint:
    """Pegasus 检测到的一个内容切点 (a single content-aware cut point)"""

    time: int
    """切点时间, 单位为微秒 (cut time, in microseconds)"""
    label: str
    """该切点对应场景的简短描述 (short label describing the scene at this cut)"""

    def __init__(self, time: int, label: str = ""):
        """构造一个切点

        Args:
            time (`int`): 切点时间, 单位为微秒.
            label (`str`, optional): 场景的简短描述, 默认为空.
        """
        self.time = time
        self.label = label

    def __repr__(self) -> str:
        return f"CutPoint(time={self.time}, label={self.label!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CutPoint):
            return False
        return self.time == other.time and self.label == other.label


# 提示词要求模型仅返回JSON, 便于稳健解析
_DEFAULT_PROMPT = (
    "You are a professional video editor. Identify the natural scene cut points "
    "in this video — moments where the shot, location, speaker, or action clearly "
    "changes. Respond with ONLY a JSON array (no prose, no markdown fences). Each "
    "element must be an object {\"time\": <seconds, number>, \"label\": <short "
    "description, string>}. \"time\" is the offset in seconds from the start of "
    "the video where the new scene begins. Sort the array ascending by time and "
    "do not include time 0."
)


def _extract_json_array(text: str) -> List[dict]:
    """从模型回复中稳健地提取JSON数组

    Pegasus 有时会在JSON外包裹少量说明文字或```代码块```, 此处做尽量宽松的解析.
    """
    # 去除markdown代码块围栏
    fenced = re.search(r"```(?:json)?\s*(.*?)```", text, re.DOTALL)
    if fenced:
        text = fenced.group(1)

    # 优先尝试整体解析
    try:
        parsed = json.loads(text)
        if isinstance(parsed, list):
            return [item for item in parsed if isinstance(item, dict)]
    except (json.JSONDecodeError, ValueError):
        pass

    # 退而求其次: 截取第一个 '[' 到最后一个 ']' 之间的内容
    start, end = text.find("["), text.rfind("]")
    if start != -1 and end != -1 and end > start:
        try:
            parsed = json.loads(text[start:end + 1])
            if isinstance(parsed, list):
                return [item for item in parsed if isinstance(item, dict)]
        except (json.JSONDecodeError, ValueError):
            pass

    raise ValueError("无法从Pegasus回复中解析出切点JSON数组, 原始回复:\n%s" % text)


def detect_cut_points(video_url: Optional[str] = None, *,
                      asset_id: Optional[str] = None,
                      api_key: Optional[str] = None,
                      model_name: str = "pegasus1.5",
                      prompt: Optional[str] = None,
                      max_tokens: int = 2048,
                      temperature: float = 0.2,
                      min_gap: Union[str, float] = "1s",
                      client: Optional[object] = None) -> List[CutPoint]:
    """利用 TwelveLabs Pegasus 模型检测视频的内容感知切点

    需要安装可选依赖 `twelvelabs` (``pip install "twelvelabs>=1.2.8"``), 并提供 API key.
    API key 按以下顺序解析: 显式 `api_key` 参数 > 环境变量 `TWELVELABS_API_KEY`.
    **本函数不会硬编码任何密钥.**

    Detect content-aware cut points in a video using TwelveLabs Pegasus.
    Requires the optional `twelvelabs` dependency and an API key resolved from
    the `api_key` argument or the `TWELVELABS_API_KEY` environment variable.

    Args:
        video_url (`str`, optional): 视频的公开可访问URL (公网URL最大支持4GB). 与 `asset_id` 二选一.
        asset_id (`str`, optional): 已上传到 TwelveLabs 的素材ID (本地直传上限200MB). 与 `video_url` 二选一.
        api_key (`str`, optional): TwelveLabs API key, 缺省时读取环境变量 `TWELVELABS_API_KEY`.
        model_name (`str`, optional): Pegasus 模型名称, 默认 `"pegasus1.5"`.
        prompt (`str`, optional): 自定义提示词, 默认要求模型返回切点JSON数组.
        max_tokens (`int`, optional): 生成上限, 默认2048 (Pegasus 1.5 要求 >=512).
        temperature (`float`, optional): 采样温度, 默认0.2 以求稳定输出.
        min_gap (`Union[str, float]`, optional): 合并间隔过近的切点的最小间隔, 默认 `"1s"`. 传入 0 可禁用.
        client (optional): 预先构造好的 `twelvelabs.TwelveLabs` 客户端, 供测试或复用连接时注入.

    Returns:
        `List[CutPoint]`: 按时间升序排列的切点列表 (单位为微秒).

    Raises:
        `ImportError`: 未安装 `twelvelabs` 库.
        `ValueError`: 未提供视频来源、缺少 API key, 或无法解析模型回复.
    """
    if (video_url is None) == (asset_id is None):
        raise ValueError("请且仅提供 `video_url` 或 `asset_id` 之一")

    if client is None:
        try:
            from twelvelabs import TwelveLabs
        except ImportError as exc:  # pragma: no cover - 取决于运行环境
            raise ImportError(
                "使用 TwelveLabs 切点检测需要安装可选依赖, 请执行: pip install \"twelvelabs>=1.2.8\""
            ) from exc

        key = api_key or os.environ.get("TWELVELABS_API_KEY")
        if not key:
            raise ValueError(
                "未找到 TwelveLabs API key, 请设置环境变量 TWELVELABS_API_KEY 或传入 `api_key` 参数. "
                "可在 https://twelvelabs.io 免费获取."
            )
        client = TwelveLabs(api_key=key)

    # 延迟导入视频上下文类型, 避免在未安装SDK时报错
    from twelvelabs.types import VideoContext_Url, VideoContext_AssetId
    if video_url is not None:
        video_context = VideoContext_Url(url=video_url)
    else:
        video_context = VideoContext_AssetId(asset_id=asset_id)

    response = client.analyze(  # type: ignore[attr-defined]
        model_name=model_name,
        video=video_context,
        prompt=prompt if prompt is not None else _DEFAULT_PROMPT,
        max_tokens=max_tokens,
        temperature=temperature,
    )

    items = _extract_json_array(response.data)

    min_gap_us = tim(min_gap)
    cut_points: List[CutPoint] = []
    for item in items:
        if "time" not in item:
            continue
        try:
            time_us = int(round(float(item["time"]) * 1e6))
        except (TypeError, ValueError):
            continue
        if time_us <= 0:
            continue
        label = str(item.get("label", "")).strip()
        cut_points.append(CutPoint(time_us, label))

    cut_points.sort(key=lambda cp: cp.time)

    # 合并间隔过近的切点
    if min_gap_us > 0 and cut_points:
        merged: List[CutPoint] = [cut_points[0]]
        for cp in cut_points[1:]:
            if cp.time - merged[-1].time >= min_gap_us:
                merged.append(cp)
        cut_points = merged

    return cut_points
