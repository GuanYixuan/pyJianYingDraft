"""Draft output compatibility with JianYing 6.0+ (verified against 11.4.0).

JianYing 6.0+ reads `draft_info.json`; `draft_content.json` is only recognised
by the draft-package import flow, which renames it. A draft dropped into the
draft folder under the legacy name is reported as corrupted.
"""

from __future__ import annotations

import pyJianYingDraft as draft


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
