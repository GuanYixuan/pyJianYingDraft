import pyJianYingDraft as draft

from tests.helpers import fake_video_material, parse_dump


def _script_with_masked_segment():
    script = draft.ScriptFile(1920, 1080, 30, True)
    script.append_track(draft.TrackSpec(draft.TrackType.video))
    segment = draft.VideoSegment(fake_video_material(), draft.trange("0s", "2s"))
    segment.add_mask(draft.MaskType.线性)
    script.add_segment(segment)
    return script, segment


def test_mask_exports_to_both_legacy_and_common_arrays():
    script, segment = _script_with_masked_segment()
    dumped = parse_dump(script)
    materials = dumped["materials"]
    segment_json = dumped["tracks"][0]["segments"][0]

    legacy_masks = materials["masks"]
    common_masks = materials["common_mask"]

    assert len(legacy_masks) == 1
    assert len(common_masks) == 1
    assert legacy_masks[0]["id"] == common_masks[0]["id"]
    assert legacy_masks[0]["id"] in segment_json["extra_material_refs"]


def test_legacy_mask_entry_structure_unchanged():
    script, segment = _script_with_masked_segment()
    dumped = parse_dump(script)
    legacy_mask = dumped["materials"]["masks"][0]

    assert set(legacy_mask) == {
        "config", "id", "name", "platform", "position_info",
        "resource_type", "resource_id", "type",
    }


def test_common_mask_entry_contains_extended_fields():
    script, segment = _script_with_masked_segment()
    dumped = parse_dump(script)
    common_mask = dumped["materials"]["common_mask"][0]

    extended_fields = {
        "category", "category_id", "category_name", "is_old_version",
        "loader_work_space", "panel", "source_platform", "track_segment",
        "text_config",
    }
    assert extended_fields <= set(common_mask)
    assert common_mask["config"]["expansion"] == 0.0
    assert common_mask["type"] == "mask"
    assert common_mask["id"] == dumped["materials"]["masks"][0]["id"]
