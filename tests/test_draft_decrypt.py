import base64
import json

import pytest
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

import pyJianYingDraft as draft
from pyJianYingDraft import exceptions
from pyJianYingDraft.draft_decrypt import JY_DRAFT_KEY_IV_OFFSETS, decrypt_jianying_draft, load_draft_content


def minimal_draft_content():
    return {
        "fps": 30,
        "duration": 0,
        "config": {"maintrack_adsorb": True},
        "canvas_config": {"width": 1920, "height": 1080},
        "materials": {"stickers": [], "effects": []},
        "tracks": [],
    }


def encrypt_like_jianying_draft(content):
    plaintext = json.dumps(content, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    key = b"0123456789abcdefghijklmnopqrstuv"
    iv = b"ABCDEF0123456789"
    ciphertext = AESGCM(key).encrypt(iv, plaintext, None)
    payload = bytearray(base64.b64encode(ciphertext))
    key_iv = key + iv
    for index, offset in enumerate(JY_DRAFT_KEY_IV_OFFSETS):
        payload[offset:offset] = key_iv[index * 4:index * 4 + 4]
    return bytes(payload)


def test_load_draft_content_reads_plain_json(tmp_path):
    path = tmp_path / "draft_content.json"
    path.write_text(json.dumps(minimal_draft_content()), encoding="utf-8")

    content = load_draft_content(str(path))

    assert content["fps"] == 30
    assert content["canvas_config"]["width"] == 1920


def test_load_draft_content_decrypts_jianying_6_draft(tmp_path):
    path = tmp_path / "draft_content.json"
    path.write_bytes(encrypt_like_jianying_draft(minimal_draft_content()))

    content = load_draft_content(str(path))

    assert content["fps"] == 30
    assert content["canvas_config"]["width"] == 1920


def test_decrypt_jianying_draft_rejects_invalid_payload():
    with pytest.raises(exceptions.DraftDecryptFailed):
        decrypt_jianying_draft(b"FAaAF/encrypted-payload")


def test_scriptfile_load_template_accepts_custom_decryptor(tmp_path):
    path = tmp_path / "draft_content.json"
    path.write_bytes(b"FAaAF/encrypted-payload")

    def decryptor(data, json_path):
        assert data.startswith(b"FAaAF")
        assert json_path == str(path)
        return minimal_draft_content()

    script = draft.ScriptFile.load_template(str(path), decryptor=decryptor)

    assert script.fps == 30
    assert script.width == 1920
    assert script.imported_tracks == []


def test_scriptfile_load_template_decrypts_jianying_6_draft(tmp_path):
    path = tmp_path / "draft_content.json"
    path.write_bytes(encrypt_like_jianying_draft(minimal_draft_content()))

    script = draft.ScriptFile.load_template(str(path))

    assert script.fps == 30
    assert script.width == 1920
    assert script.imported_tracks == []


def test_scriptfile_load_template_fills_defaults_for_newer_draft_shape(tmp_path):
    content = {
        "id": "newer-draft",
        "version": 360000,
        "new_version": "173.0.0",
        "config": {},
        "canvas_config": {"width": 720, "height": 1280},
        "materials": {},
    }
    path = tmp_path / "draft_content.json"
    path.write_bytes(encrypt_like_jianying_draft(content))

    script = draft.ScriptFile.load_template(str(path))

    assert script.fps == 30
    assert script.duration == 0
    assert script.maintrack_adsorb is True
    assert script.width == 720
    assert script.height == 1280
    assert script.imported_materials == {}
    assert script.imported_tracks == []


def test_decrypt_draft_file_writes_plain_json(tmp_path):
    src = tmp_path / "draft_content.json"
    dst = tmp_path / "plain.json"
    src.write_bytes(encrypt_like_jianying_draft(minimal_draft_content()))

    written = draft.decrypt_draft_file(
        str(src),
        str(dst),
    )

    assert written == str(dst)
    assert json.loads(dst.read_text(encoding="utf-8"))["config"]["maintrack_adsorb"] is True
