import json
from pathlib import Path

import pyJianYingDraft as draft
import pytest

from pyJianYingDraft.exceptions import DraftContentLoadFailed
from tests.helpers import parse_dump


def _create_template_draft(tmp_path: Path, draft_name: str) -> Path:
    folder = draft.DraftFolder(str(tmp_path))
    script = folder.create_draft(draft_name, 1920, 1080)
    script.save()
    return tmp_path / draft_name / "draft_info.json"


def test_load_template_raises_stable_error_for_non_plain_content_without_fallback_loader(tmp_path):
    draft_content_path = _create_template_draft(tmp_path, "custom_format_template")
    draft_content_path.write_bytes(b"\x80not-json")

    folder = draft.DraftFolder(str(tmp_path))

    with pytest.raises(DraftContentLoadFailed):
        folder.load_template("custom_format_template")


def test_load_template_uses_fallback_loader_for_non_plain_content(tmp_path):
    draft_content_path = _create_template_draft(tmp_path, "custom_format_template")
    plain_content = draft_content_path.read_text(encoding="utf-8")
    raw_payload = b"custom payload"
    draft_content_path.write_bytes(raw_payload)

    seen = {}

    def fallback_loader(raw_data: bytes) -> str:
        seen["raw_data"] = raw_data
        return plain_content

    folder = draft.DraftFolder(str(tmp_path), fallback_loader=fallback_loader)
    script = folder.load_template("custom_format_template")

    assert seen["raw_data"] == raw_payload
    assert script.width == 1920
    assert script.height == 1080
    assert script.save_path == str(draft_content_path)


def test_load_template_accepts_dict_from_fallback_loader(tmp_path):
    draft_content_path = _create_template_draft(tmp_path, "custom_format_template")
    plain_content = draft_content_path.read_text(encoding="utf-8")
    draft_content_path.write_bytes(b"custom payload")

    folder = draft.DraftFolder(
        str(tmp_path),
        fallback_loader=lambda _: json.loads(plain_content),
    )
    script = folder.load_template("custom_format_template")

    assert script.width == 1920
    assert script.height == 1080


def test_duplicate_as_template_reuses_fallback_loader(tmp_path):
    draft_content_path = _create_template_draft(tmp_path, "custom_format_template")
    plain_content = draft_content_path.read_text(encoding="utf-8")
    draft_content_path.write_bytes(b"custom payload")

    folder = draft.DraftFolder(str(tmp_path), fallback_loader=lambda _: plain_content)
    script = folder.duplicate_as_template("custom_format_template", "copied_template")

    assert Path(script.save_path) == tmp_path / "copied_template" / "draft_info.json"
    assert (tmp_path / "copied_template" / "draft_info.json").exists()


def test_load_template_normalizes_sparse_template_content(tmp_path):
    draft_content_path = _create_template_draft(tmp_path, "sparse_template")
    draft_content_path.write_bytes(b"custom payload")

    sparse_content = {
        "duration": 123456,
        "canvas_config": {"width": 1920, "height": 1080},
        "tracks": [
            {
                "id": "track-1",
                "type": "text",
                "segments": [
                    {
                        "material_id": "text-material-1",
                        "target_timerange": {"duration": 1000},
                        "track_render_index": 7,
                    }
                ],
            }
        ],
    }

    folder = draft.DraftFolder(
        str(tmp_path),
        fallback_loader=lambda _: sparse_content,
    )
    script = folder.load_template("sparse_template")

    assert script.fps == 30
    assert script.maintrack_adsorb is True
    assert script.imported_tracks[0].name == ""
    assert not hasattr(script.imported_tracks[0], "render_index")
    assert script.imported_tracks[0].segments[0].target_timerange.start == 0

    dumped = parse_dump(script)
    assert dumped["tracks"][0]["segments"][0]["render_index"] == 0
    assert dumped["tracks"][0]["segments"][0]["track_render_index"] == 0


def test_template_dump_preserves_original_track_array_order(tmp_path):
    draft_content_path = _create_template_draft(tmp_path, "ordered_template")
    draft_content_path.write_bytes(b"custom payload")

    folder = draft.DraftFolder(
        str(tmp_path),
        fallback_loader=lambda _: {
            "duration": 123456,
            "canvas_config": {"width": 1920, "height": 1080},
            "tracks": [
                {
                    "id": "track-1",
                    "type": "text",
                    "name": "first_track",
                    "segments": [
                        {
                            "material_id": "text-material-1",
                            "target_timerange": {"start": 0, "duration": 1000},
                            "render_index": 10,
                        }
                    ],
                },
                {
                    "id": "track-2",
                    "type": "text",
                    "name": "second_track",
                    "segments": [
                        {
                            "material_id": "text-material-2",
                            "target_timerange": {"start": 0, "duration": 1000},
                            "render_index": 1,
                        }
                    ],
                },
            ],
        },
    )
    script = folder.load_template("ordered_template")

    dumped = parse_dump(script)

    assert [track["name"] for track in dumped["tracks"]] == ["first_track", "second_track"]
    assert [track["segments"][0]["render_index"] for track in dumped["tracks"]] == [0, 1]


def test_list_imported_tracks_preserves_internal_order_and_supports_type_filter(tmp_path):
    draft_content_path = _create_template_draft(tmp_path, "list_template")
    draft_content_path.write_bytes(b"custom payload")

    folder = draft.DraftFolder(
        str(tmp_path),
        fallback_loader=lambda _: {
            "duration": 123456,
            "canvas_config": {"width": 1920, "height": 1080},
            "tracks": [
                {"id": "track-1", "type": "text", "name": "text_a", "segments": []},
                {"id": "track-2", "type": "audio", "name": "audio_a", "segments": []},
                {"id": "track-3", "type": "text", "name": "text_b", "segments": []},
            ],
        },
    )
    script = folder.load_template("list_template")

    all_tracks = script.list_imported_tracks()
    text_tracks = script.list_imported_tracks(draft.TrackType.text)

    assert [track.name for track in all_tracks] == ["text_a", "audio_a", "text_b"]
    assert [track.name for track in text_tracks] == ["text_a", "text_b"]


def test_list_imported_tracks_returns_live_references(tmp_path):
    draft_content_path = _create_template_draft(tmp_path, "reference_template")
    draft_content_path.write_bytes(b"custom payload")

    folder = draft.DraftFolder(
        str(tmp_path),
        fallback_loader=lambda _: {
            "duration": 123456,
            "canvas_config": {"width": 1920, "height": 1080},
            "tracks": [
                {"id": "track-1", "type": "text", "name": "original_name", "segments": []},
            ],
        },
    )
    script = folder.load_template("reference_template")

    track = script.list_imported_tracks(draft.TrackType.text)[0]
    track.name = "renamed_track"

    dumped = parse_dump(script)

    assert dumped["tracks"][0]["name"] == "renamed_track"


def test_get_imported_track_uses_internal_order_for_indexing(tmp_path):
    draft_content_path = _create_template_draft(tmp_path, "indexed_template")
    draft_content_path.write_bytes(b"custom payload")

    folder = draft.DraftFolder(
        str(tmp_path),
        fallback_loader=lambda _: {
            "duration": 123456,
            "canvas_config": {"width": 1920, "height": 1080},
            "tracks": [
                {"id": "track-1", "type": "text", "name": "text_a", "segments": []},
                {"id": "track-2", "type": "text", "name": "text_b", "segments": []},
            ],
        },
    )
    script = folder.load_template("indexed_template")

    assert script.get_imported_track(draft.TrackType.text, index=0).name == "text_a"
    assert script.get_imported_track(draft.TrackType.text, index=1).name == "text_b"


def test_import_track_supports_explicit_insert_position(tmp_path):
    source_path = _create_template_draft(tmp_path, "source_template")
    source_path.write_bytes(b"custom payload")
    source_folder = draft.DraftFolder(
        str(tmp_path),
        fallback_loader=lambda _: {
            "duration": 123456,
            "canvas_config": {"width": 1920, "height": 1080},
            "tracks": [
                {"id": "source-track-1", "type": "text", "name": "source_text", "segments": []},
            ],
        },
    )
    source_script = source_folder.load_template("source_template")

    target_script = draft.ScriptFile(1920, 1080, 30, True)
    anchor_ref = target_script.append_track(draft.TrackSpec(draft.TrackType.video, "video"))

    target_script.import_track(
        source_script,
        source_script.get_imported_track(draft.TrackType.text, index=0),
        under_track=anchor_ref,
    )

    dumped = parse_dump(target_script)
    assert [track["name"] for track in dumped["tracks"]] == ["source_text", "video"]
