import pyJianYingDraft as draft

from tests.helpers import fake_video_material, parse_dump


def _script_with_video():
    script = draft.ScriptFile(1920, 1080, 30, True)
    script.append_track(draft.TrackSpec(draft.TrackType.video))
    segment = draft.VideoSegment(fake_video_material(), draft.trange("0s", "2s"))
    return script, segment


def _assert_only_last_mix_mode(script, segment):
    dumped = parse_dump(script)
    mix_modes = [effect for effect in dumped["materials"]["effects"] if effect["type"] == "mix_mode"]
    segment_json = dumped["tracks"][0]["segments"][0]

    assert len(mix_modes) == 1
    assert mix_modes[0]["name"] == draft.MixModeType.滤色.value.name
    assert mix_modes[0]["id"] in segment_json["extra_material_refs"]
    assert segment.mix_mode is not None
    assert segment_json["extra_material_refs"].count(mix_modes[0]["id"]) == 1


def test_repeated_mix_mode_before_adding_segment_keeps_only_last_mode():
    script, segment = _script_with_video()
    segment.set_mix_mode(draft.MixModeType.正片叠底)
    assert segment.mix_mode is not None
    first_id = segment.mix_mode.global_id
    segment.set_mix_mode(draft.MixModeType.滤色)
    script.add_segment(segment)

    _assert_only_last_mix_mode(script, segment)
    assert segment.mix_mode is not None
    assert segment.mix_mode.global_id == first_id


def test_repeated_mix_mode_after_adding_segment_updates_registered_material():
    script, segment = _script_with_video()
    segment.set_mix_mode(draft.MixModeType.正片叠底)
    script.add_segment(segment)
    assert segment.mix_mode is not None
    first_id = segment.mix_mode.global_id
    segment.set_mix_mode(draft.MixModeType.滤色)

    _assert_only_last_mix_mode(script, segment)
    assert segment.mix_mode is not None
    assert segment.mix_mode.global_id == first_id
