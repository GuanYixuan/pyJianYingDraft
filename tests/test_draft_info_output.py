"""Draft output compatibility with JianYing 6.0+ (verified against 11.4.0).

JianYing 6.0+ reads `draft_info.json`; `draft_content.json` is only recognised
by the draft-package import flow, which renames it. A draft dropped into the
draft folder under the legacy name is reported as corrupted.
"""

from __future__ import annotations

import json

import pyJianYingDraft as draft

from tests.helpers import fake_audio_material, fake_video_material


def test_create_draft_saves_as_draft_info_json(tmp_path):
    folder = draft.DraftFolder(str(tmp_path))
    script = folder.create_draft("new_draft", 1920, 1080)
    script.save()

    assert (tmp_path / "new_draft" / "draft_info.json").exists()


def test_load_template_reads_draft_info_json(tmp_path):
    folder = draft.DraftFolder(str(tmp_path))
    folder.create_draft("tpl", 1920, 1080).save()

    loaded = folder.load_template("tpl")

    assert loaded.width == 1920
    assert loaded.height == 1080


def test_load_template_falls_back_to_legacy_file_name(tmp_path):
    folder = draft.DraftFolder(str(tmp_path))
    folder.create_draft("legacy", 1920, 1080).save()

    # A draft produced by JianYing <= 5.9 only has the legacy file name.
    draft_dir = tmp_path / "legacy"
    (draft_dir / "draft_info.json").rename(draft_dir / "draft_content.json")

    loaded = folder.load_template("legacy")

    assert loaded.width == 1920


def test_save_inline_materials_copies_files_into_draft_folder(tmp_path):
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "video.mp4").write_bytes(b"fake-video")
    (outside / "audio.mp3").write_bytes(b"fake-audio")

    folder = draft.DraftFolder(str(tmp_path))
    script = folder.create_draft("inlined", 1920, 1080)
    script.materials.videos.append(fake_video_material(path=str(outside / "video.mp4")))
    script.materials.audios.append(fake_audio_material(path=str(outside / "audio.mp3")))

    script.save(inline_materials=True)

    materials_dir = tmp_path / "inlined" / "materials"
    assert (materials_dir / "video.mp4").exists()
    assert (materials_dir / "audio.mp3").exists()

    content = json.loads((tmp_path / "inlined" / "draft_info.json").read_text(encoding="utf-8"))
    exported = [item["path"] for item in content["materials"]["videos"]]
    exported += [item["path"] for item in content["materials"]["audios"]]
    assert exported, "expected materials in the exported draft"
    assert all(path.startswith(str(materials_dir)) for path in exported)


def test_save_without_inline_materials_keeps_original_paths(tmp_path):
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "video.mp4").write_bytes(b"fake-video")

    folder = draft.DraftFolder(str(tmp_path))
    script = folder.create_draft("plain", 1920, 1080)
    script.materials.videos.append(fake_video_material(path=str(outside / "video.mp4")))

    script.save()

    assert not (tmp_path / "plain" / "materials").exists()
    content = json.loads((tmp_path / "plain" / "draft_info.json").read_text(encoding="utf-8"))
    assert content["materials"]["videos"][0]["path"] == str(outside / "video.mp4")
