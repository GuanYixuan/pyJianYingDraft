import os
from pathlib import Path

from pyJianYingDraft.jianying_controller import (
    _candidate_export_dirs,
    _find_exported_video_file,
    _find_recent_video_file,
)


def test_candidate_export_dirs_include_output_parent(tmp_path):
    output_file = tmp_path / "exports" / "video.mp4"

    candidates = _candidate_export_dirs(str(output_file))

    assert candidates[0] == output_file.parent
    assert len(candidates) == len({str(path).lower() for path in candidates})


def test_find_recent_video_file_picks_newest_video_after_start(tmp_path):
    export_dir = tmp_path / "exports"
    export_dir.mkdir()
    old_video = export_dir / "old.mp4"
    new_video = export_dir / "new.mov"
    note = export_dir / "note.txt"
    old_video.write_bytes(b"old")
    new_video.write_bytes(b"new")
    note.write_text("ignore", encoding="utf-8")

    old_time = 1000.0
    new_time = 2000.0
    old_video.touch()
    new_video.touch()
    note.touch()
    os.utime(old_video, (old_time, old_time))
    os.utime(new_video, (new_time, new_time))
    os.utime(note, (new_time + 100, new_time + 100))

    found = _find_recent_video_file([export_dir], started_at=1500.0)

    assert found == str(new_video)


def test_find_recent_video_file_returns_none_without_new_video(tmp_path):
    export_dir = tmp_path / "exports"
    export_dir.mkdir()
    old_video = export_dir / "old.mp4"
    old_video.write_bytes(b"old")
    os.utime(old_video, (1000.0, 1000.0))

    assert _find_recent_video_file([export_dir], started_at=1500.0) is None


def test_find_exported_video_file_prefers_requested_output_parent(tmp_path, monkeypatch):
    output_dir = tmp_path / "requested"
    common_dir = tmp_path / "common"
    output_dir.mkdir()
    common_dir.mkdir()
    requested_video = output_dir / "requested.mp4"
    common_video = common_dir / "common.mp4"
    requested_video.write_bytes(b"requested")
    common_video.write_bytes(b"common")
    os.utime(requested_video, (2000.0, 2000.0))
    os.utime(common_video, (3000.0, 3000.0))

    monkeypatch.setattr(
        "pyJianYingDraft.jianying_controller._candidate_export_dirs",
        lambda output_path: [output_dir, common_dir],
    )

    found = _find_exported_video_file(str(output_dir / "target.mp4"), started_at=1500.0)

    assert found == str(requested_video)
