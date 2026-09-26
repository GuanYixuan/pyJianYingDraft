from pathlib import Path

import pyJianYingDraft as draft
import pytest

from tests.helpers import parse_dump


def _load_template_script(tmp_path: Path, draft_name: str, tracks):
    folder = draft.DraftFolder(str(tmp_path))
    script = folder.create_draft(draft_name, 1920, 1080)
    script.save()

    draft_content_path = tmp_path / draft_name / "draft_info.json"
    draft_content_path.write_bytes(b"custom payload")

    folder = draft.DraftFolder(
        str(tmp_path),
        fallback_loader=lambda _: {
            "duration": 123456,
            "canvas_config": {"width": 1920, "height": 1080},
            "tracks": tracks,
        },
    )
    return folder.load_template(draft_name)


def test_insert_track_before_imported_track_preserves_overall_order(tmp_path):
    script = _load_template_script(
        tmp_path,
        "insert_before_imported",
        [
            {"id": "track-1", "type": "text", "name": "text_a", "segments": []},
            {"id": "track-2", "type": "text", "name": "text_b", "segments": []},
        ],
    )

    anchor = script.list_imported_tracks()[1]
    inserted_ref = script.insert_track(
        draft.TrackSpec(draft.TrackType.video, "inserted_video"),
        under_track=anchor,
    )

    assert inserted_ref.name == "inserted_video"
    dumped = parse_dump(script)
    assert [track["name"] for track in dumped["tracks"]] == ["text_a", "inserted_video", "text_b"]


def test_insert_tracks_over_track_ref_preserves_block_order():
    script = draft.ScriptFile(1920, 1080, 30, True)
    first_ref = script.append_track(draft.TrackSpec(draft.TrackType.video, "first"))
    second_ref = script.append_track(draft.TrackSpec(draft.TrackType.video, "second"))

    refs = script.insert_tracks(
        [
            draft.TrackSpec(draft.TrackType.audio, "middle_a"),
            draft.TrackSpec(draft.TrackType.text, "middle_b"),
        ],
        over_track=first_ref,
    )

    assert [ref.name for ref in refs] == ["middle_a", "middle_b"]
    assert [track.name for track in script.tracks.values()] == ["first", "middle_a", "middle_b", "second"]

    dumped = parse_dump(script)
    assert [track["name"] for track in dumped["tracks"]] == ["first", "middle_a", "middle_b", "second"]


def test_insert_track_at_index_uses_full_track_order(tmp_path):
    script = _load_template_script(
        tmp_path,
        "insert_at_index",
        [
            {"id": "track-1", "type": "text", "name": "imported_a", "segments": []},
            {"id": "track-2", "type": "text", "name": "imported_b", "segments": []},
        ],
    )
    script.append_track(draft.TrackSpec(draft.TrackType.audio, "tail"))

    script.insert_track(
        draft.TrackSpec(draft.TrackType.video, "middle"),
        at_index=1,
    )

    dumped = parse_dump(script)
    assert [track["name"] for track in dumped["tracks"]] == ["imported_a", "middle", "imported_b", "tail"]


def test_insert_track_rejects_multiple_location_hints():
    script = draft.ScriptFile(1920, 1080, 30, True)
    anchor = script.append_track(draft.TrackSpec(draft.TrackType.video, "anchor"))

    with pytest.raises(ValueError):
        script.insert_track(
            draft.TrackSpec(draft.TrackType.audio, "new_track"),
            under_track=anchor,
            at_index=0,
        )


def test_insert_track_rejects_foreign_imported_track_anchor(tmp_path):
    script_a = _load_template_script(
        tmp_path,
        "foreign_anchor_a",
        [{"id": "track-1", "type": "text", "name": "text_a", "segments": []}],
    )
    script_b = _load_template_script(
        tmp_path,
        "foreign_anchor_b",
        [{"id": "track-2", "type": "text", "name": "text_b", "segments": []}],
    )

    foreign_anchor = script_a.list_imported_tracks()[0]

    with pytest.raises(ValueError):
        script_b.insert_track(
            draft.TrackSpec(draft.TrackType.video, "new_track"),
            under_track=foreign_anchor,
        )


def test_insert_track_rejects_out_of_range_index():
    script = draft.ScriptFile(1920, 1080, 30, True)

    with pytest.raises(IndexError):
        script.insert_track(
            draft.TrackSpec(draft.TrackType.video, "new_track"),
            at_index=1,
        )
