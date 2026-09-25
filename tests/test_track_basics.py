import pytest

import pyJianYingDraft as draft
from pyJianYingDraft.exceptions import SegmentOverlap
from pyJianYingDraft.track import Track

from tests.helpers import fake_audio_material, fake_video_material


def test_track_accepts_matching_segment_type():
    track = Track(draft.TrackType.audio, "audio", 0, False)
    segment = draft.AudioSegment(fake_audio_material(), draft.trange("0s", "1s"))

    track.add_segment(segment)

    assert len(track.segments) == 1
    assert track.segments[0] is segment


def test_track_rejects_mismatched_segment_type():
    track = Track(draft.TrackType.audio, "audio", 0, False)
    segment = draft.VideoSegment(fake_video_material(), draft.trange("0s", "1s"))

    with pytest.raises(TypeError):
        track.add_segment(segment)


def test_track_rejects_overlapping_segments():
    track = Track(draft.TrackType.audio, "audio", 0, False)
    first = draft.AudioSegment(fake_audio_material(material_id="audio-1"), draft.trange("0s", "2s"))
    second = draft.AudioSegment(fake_audio_material(material_id="audio-2"), draft.trange("1s", "2s"))

    track.add_segment(first)

    with pytest.raises(SegmentOverlap):
        track.add_segment(second)


def test_track_accepts_beat_aligned_segments_in_seconds():
    track = Track(draft.TrackType.video, "video", 0, False)
    material = fake_video_material(duration=60_000_000)
    bar = 60 / 136 * 4

    for i in range(8):
        track.add_segment(draft.VideoSegment(
            material,
            draft.trange_seconds(i * bar, end=(i + 1) * bar),
        ))

    assert len(track.segments) == 8
    assert all(previous.end == following.start
               for previous, following in zip(track.segments, track.segments[1:]))


def test_track_still_rejects_one_microsecond_overlap():
    track = Track(draft.TrackType.audio, "audio", 0, False)
    material = fake_audio_material()
    track.add_segment(draft.AudioSegment(material, draft.Timerange(0, 1_000_000)))

    with pytest.raises(SegmentOverlap):
        track.add_segment(draft.AudioSegment(material, draft.Timerange(999_999, 1_000_000)))


def test_track_end_time_reflects_last_segment_end():
    track = Track(draft.TrackType.audio, "audio", 0, False)
    first = draft.AudioSegment(fake_audio_material(material_id="audio-1"), draft.trange("0s", "1s"))
    second = draft.AudioSegment(fake_audio_material(material_id="audio-2"), draft.trange("2s", "1s"))

    track.add_segment(first)
    track.add_segment(second)

    assert track.end_time == draft.tim("3s")
