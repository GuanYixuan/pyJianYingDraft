import pytest

import pyJianYingDraft as draft


def test_tim_parses_common_duration_strings():
    assert draft.tim("1s") == 1_000_000
    assert draft.tim("1m2s") == 62_000_000
    assert draft.tim("0.15s") == 150_000
    assert draft.tim("1h2m3s") == 3_723_000_000


def test_tim_supports_negative_offsets():
    assert draft.tim("-2s") == -2_000_000


def test_trange_uses_duration_not_end_time():
    timerange = draft.trange("1s", "2s")

    assert timerange.start == 1_000_000
    assert timerange.duration == 2_000_000
    assert timerange.end == 3_000_000


def test_trange_seconds_accepts_end_or_duration():
    by_end = draft.trange_seconds(1.25, end=2.5)
    by_duration = draft.trange_seconds(1.25, duration=1.25)

    assert by_end == by_duration == draft.Timerange(1_250_000, 1_250_000)
    assert draft.trange_seconds(-1, end=0) == draft.Timerange(-1_000_000, 1_000_000)
    assert draft.trange_seconds(1, duration=0) == draft.Timerange(1_000_000, 0)


def test_trange_seconds_rounds_absolute_boundaries():
    bar = 60 / 136 * 4
    by_end = draft.trange_seconds(4 * bar, end=5 * bar)
    by_duration = draft.trange_seconds(4 * bar, duration=bar)

    assert by_end.start == 7_058_824
    assert by_end.end == 8_823_529
    assert by_end.duration == 1_764_705
    assert by_duration == by_end

def test_trange_seconds_requires_numeric_seconds():
    with pytest.raises(TypeError):
        draft.trange_seconds("1s", end=2)

def test_timerange_overlap_semantics():
    base = draft.Timerange(1_000_000, 2_000_000)

    assert base.overlaps(draft.Timerange(2_000_000, 2_000_000))
    assert not base.overlaps(draft.Timerange(3_000_000, 1_000_000))
    assert base.overlaps(draft.Timerange(1_500_000, 200_000))


def test_timerange_import_json_defaults_missing_start_to_zero():
    timerange = draft.Timerange.import_json({"duration": "2000"})

    assert timerange.start == 0
    assert timerange.duration == 2000
