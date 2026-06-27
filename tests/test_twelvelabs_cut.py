"""TwelveLabs Pegasus 切点集成的单元测试

这些测试不触网: 切点解析直接喂入模型回复文本, 草稿切分通过注入 `cut_points` 完成.
另有一个标记为 `media` 的实时测试, 仅在设置了 `TWELVELABS_API_KEY` 时运行.
"""

import os

import pytest

import pyJianYingDraft as draft
from pyJianYingDraft.twelvelabs_cut import CutPoint, _extract_json_array, detect_cut_points

from tests.helpers import fake_video_material


def test_extract_json_array_plain():
    text = '[{"time": 1.5, "label": "a"}, {"time": 3.0, "label": "b"}]'
    items = _extract_json_array(text)
    assert items == [{"time": 1.5, "label": "a"}, {"time": 3.0, "label": "b"}]


def test_extract_json_array_with_fence_and_prose():
    text = "Sure! Here are the cuts:\n```json\n[{\"time\": 2, \"label\": \"x\"}]\n```\nHope that helps."
    items = _extract_json_array(text)
    assert items == [{"time": 2, "label": "x"}]


def test_extract_json_array_raises_on_garbage():
    with pytest.raises(ValueError):
        _extract_json_array("no json here")


class _FakeResponse:
    def __init__(self, data):
        self.data = data


class _FakeClient:
    """模拟 twelvelabs.TwelveLabs.analyze 的最小客户端"""
    def __init__(self, data):
        self._data = data
        self.last_kwargs = None

    def analyze(self, **kwargs):
        self.last_kwargs = kwargs
        return _FakeResponse(self._data)


def test_detect_cut_points_parses_and_merges():
    client = _FakeClient(
        '[{"time": 0, "label": "start"},'
        ' {"time": 2.0, "label": "scene a"},'
        ' {"time": 2.4, "label": "too close"},'
        ' {"time": 5.0, "label": "scene b"}]'
    )
    pts = detect_cut_points(video_url="https://example.com/v.mp4", client=client, min_gap="1s")

    # time 0 被丢弃; 2.4s 与 2.0s 间隔过近被合并
    assert pts == [CutPoint(2_000_000, "scene a"), CutPoint(5_000_000, "scene b")]
    # 确认请求使用了 URL 视频上下文
    assert client.last_kwargs["model_name"] == "pegasus1.5"


def test_detect_cut_points_requires_one_source():
    with pytest.raises(ValueError):
        detect_cut_points(client=_FakeClient("[]"))
    with pytest.raises(ValueError):
        detect_cut_points(video_url="u", asset_id="a", client=_FakeClient("[]"))


def test_import_pegasus_cuts_splits_material_offline():
    material = fake_video_material(duration=10_000_000)  # 10s
    script = draft.ScriptFile(1920, 1080, 30, True)

    cut_points = [CutPoint(3_000_000, "a"), CutPoint(7_000_000, "b")]
    script.import_pegasus_cuts(material, "auto_cut", cut_points=cut_points)

    track = script.tracks["auto_cut"]
    assert track.track_type == draft.TrackType.video
    # 边界 0 / 3 / 7 / 10 -> 三段
    segments = track.segments
    assert len(segments) == 3
    durations = [seg.target_timerange.duration for seg in segments]
    assert durations == [3_000_000, 4_000_000, 3_000_000]
    starts = [seg.target_timerange.start for seg in segments]
    assert starts == [0, 3_000_000, 7_000_000]


def test_import_pegasus_cuts_respects_min_clip_duration():
    material = fake_video_material(duration=10_000_000)
    script = draft.ScriptFile(1920, 1080, 30, True)

    # 0.5s 处的切点会产生一个过短(<1s)的首段, 应被丢弃
    cut_points = [CutPoint(500_000, "tiny"), CutPoint(5_000_000, "mid")]
    script.import_pegasus_cuts(material, "auto_cut", cut_points=cut_points, min_clip_duration="1s")

    durations = [seg.target_timerange.duration for seg in script.tracks["auto_cut"].segments]
    # 首段 [0, 0.5s] 被丢弃, 余下 [0.5s, 5s] 和 [5s, 10s]
    assert durations == [4_500_000, 5_000_000]


@pytest.mark.media
@pytest.mark.skipif(not os.environ.get("TWELVELABS_API_KEY"), reason="需要 TWELVELABS_API_KEY")
def test_detect_cut_points_live():
    """实时调用 Pegasus, 验证能返回有序的切点(需联网及有效 API key)"""
    pts = detect_cut_points("https://media.w3.org/2010/05/sintel/trailer.mp4")
    assert len(pts) > 0
    assert all(isinstance(p, CutPoint) for p in pts)
    times = [p.time for p in pts]
    assert times == sorted(times)
    assert all(t > 0 for t in times)
