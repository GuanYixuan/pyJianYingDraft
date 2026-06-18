"""读取和解密剪映草稿内容的辅助函数"""

import base64
import binascii
import json
import os
from typing import Any, Callable, Dict, Optional, Union
from urllib import error, request
from uuid import uuid4

from . import exceptions

Decryptor = Callable[[bytes, str], Union[str, bytes, Dict[str, Any]]]

HTWMEDIA_DECRYPT_URL = "https://htwmedia.dpdns.org/home/DecryptDraft"
ENV_DECRYPT_API_KEY = "PYJY_DRAFT_DECRYPT_API_KEY"
ENV_DECRYPT_API_URL = "PYJY_DRAFT_DECRYPT_API_URL"

JY_DRAFT_KEY_IV_OFFSETS = (0, 7, 20, 33, 40, 47, 59, 66, 76, 89, 99, 127)
JY_DRAFT_KEY_LENGTH = 32
JY_DRAFT_IV_LENGTH = 16
JY_DRAFT_KEY_IV_LENGTH = JY_DRAFT_KEY_LENGTH + JY_DRAFT_IV_LENGTH
JY_DRAFT_MIN_ENCRYPTED_SIZE = 131


def is_probably_encrypted(data: bytes) -> bool:
    """判断草稿内容是否不像明文 JSON。"""
    return not data.lstrip().startswith((b"{", b"["))


def parse_draft_content(data: bytes, *, path: str = "") -> Dict[str, Any]:
    """将明文草稿内容解析为字典。"""
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise exceptions.DraftContentEncrypted(_encrypted_message(path)) from exc

    try:
        content = json.loads(text)
    except json.JSONDecodeError as exc:
        if is_probably_encrypted(data):
            raise exceptions.DraftContentEncrypted(_encrypted_message(path)) from exc
        raise

    if not isinstance(content, dict):
        raise ValueError("草稿内容必须是JSON对象")
    return content


def load_draft_content(
    json_path: str,
    *,
    decryptor: Optional[Decryptor] = None,
    decrypt_api_key: Optional[str] = None,
    decrypt_api_url: Optional[str] = None,
) -> Dict[str, Any]:
    """读取草稿 JSON，必要时自动解密新版剪映草稿。"""
    with open(json_path, "rb") as f:
        data = f.read()

    try:
        return parse_draft_content(data, path=json_path)
    except exceptions.DraftContentEncrypted as encrypted_exc:
        try:
            decrypted = decrypt_jianying_draft(data)
        except exceptions.DraftDecryptFailed as local_exc:
            if decryptor is not None:
                decrypted = decryptor(data, json_path)
            else:
                api_key = decrypt_api_key or os.getenv(ENV_DECRYPT_API_KEY)
                if not api_key:
                    raise local_exc from encrypted_exc
                decrypted = decrypt_with_htwmedia_api(
                    json_path,
                    api_key=api_key,
                    api_url=decrypt_api_url or os.getenv(ENV_DECRYPT_API_URL) or HTWMEDIA_DECRYPT_URL,
                )

    return _parse_decrypted_result(decrypted, path=json_path)


def decrypt_jianying_draft(data: bytes) -> bytes:
    """解密剪映 6+ 的 `draft_content.json` 内容并返回明文 JSON bytes。"""
    try:
        from cryptography.exceptions import InvalidTag
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    except ImportError as exc:
        raise exceptions.DraftDecryptFailed(
            "本地解密剪映6+草稿需要安装 cryptography: pip install cryptography"
        ) from exc

    payload = b"".join(data.split())
    if len(payload) < JY_DRAFT_MIN_ENCRYPTED_SIZE:
        raise exceptions.DraftDecryptFailed("加密草稿内容过短，无法按剪映6+格式解密")

    key_iv = b"".join(payload[offset:offset + 4] for offset in JY_DRAFT_KEY_IV_OFFSETS)
    if len(key_iv) != JY_DRAFT_KEY_IV_LENGTH:
        raise exceptions.DraftDecryptFailed("加密草稿中的密钥/IV数据不完整")

    encoded_ciphertext = bytearray(payload)
    for offset in sorted(JY_DRAFT_KEY_IV_OFFSETS, reverse=True):
        del encoded_ciphertext[offset:offset + 4]

    try:
        ciphertext_and_tag = base64.b64decode(bytes(encoded_ciphertext), validate=True)
    except (binascii.Error, ValueError) as exc:
        raise exceptions.DraftDecryptFailed("加密草稿内容不是有效的剪映6+ Base64数据") from exc

    try:
        return AESGCM(key_iv[:JY_DRAFT_KEY_LENGTH]).decrypt(
            key_iv[JY_DRAFT_KEY_LENGTH:],
            ciphertext_and_tag,
            None,
        )
    except InvalidTag as exc:
        raise exceptions.DraftDecryptFailed("草稿解密校验失败，可能不是当前支持的剪映6+加密格式") from exc
    except ValueError as exc:
        raise exceptions.DraftDecryptFailed("草稿解密失败: %s" % exc) from exc


def decrypt_draft_file(
    json_path: str,
    output_path: Optional[str] = None,
    *,
    decryptor: Optional[Decryptor] = None,
    decrypt_api_key: Optional[str] = None,
    decrypt_api_url: Optional[str] = None,
) -> str:
    """将草稿文件解密并写出为明文 JSON 文件。

    返回写出的文件路径。若未指定`output_path`, 默认写到同目录的
    `draft_content_decrypted.json`。
    """
    content = load_draft_content(
        json_path,
        decryptor=decryptor,
        decrypt_api_key=decrypt_api_key,
        decrypt_api_url=decrypt_api_url,
    )
    if output_path is None:
        output_path = os.path.join(os.path.dirname(json_path), "draft_content_decrypted.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=4)
    return output_path


def decrypt_with_htwmedia_api(
    json_path: str,
    *,
    api_key: str,
    api_url: str = HTWMEDIA_DECRYPT_URL,
    timeout: float = 60,
) -> str:
    """调用公开的 HDraft/JyDraft 解密接口解密草稿。

    该接口由第三方服务提供，调用会上传草稿文件内容。默认的模板加载
    不会自动调用它，只有显式传入 API key 或设置环境变量时才会使用。
    """
    boundary = "----pyJianYingDraftDraftDecrypt%s" % uuid4().hex
    file_name = os.path.basename(json_path) or "draft_content.json"
    with open(json_path, "rb") as f:
        file_data = f.read()

    body = b"".join([
        ("--%s\r\n" % boundary).encode("ascii"),
        ('Content-Disposition: form-data; name="jsonFile"; filename="%s"\r\n' % file_name).encode("utf-8"),
        b"Content-Type: application/octet-stream\r\n\r\n",
        file_data,
        b"\r\n",
        ("--%s--\r\n" % boundary).encode("ascii"),
    ])
    req = request.Request(
        api_url,
        data=body,
        method="POST",
        headers={
            "Content-Type": "multipart/form-data; boundary=%s" % boundary,
            "Content-Length": str(len(body)),
            "X-API-KEY": api_key,
        },
    )

    try:
        with request.urlopen(req, timeout=timeout) as resp:
            resp_text = resp.read().decode("utf-8")
    except error.URLError as exc:
        raise exceptions.DraftDecryptFailed("调用草稿解密接口失败: %s" % exc) from exc

    try:
        payload = json.loads(resp_text)
    except json.JSONDecodeError as exc:
        raise exceptions.DraftDecryptFailed("解密接口返回的内容不是JSON") from exc

    if not payload.get("success", False):
        msg = payload.get("msg") or payload.get("message") or "未知错误"
        raise exceptions.DraftDecryptFailed("解密接口返回失败: %s" % msg)

    draft_content = payload.get("draft_content")
    if not isinstance(draft_content, str):
        raise exceptions.DraftDecryptFailed("解密接口未返回draft_content字段")
    return draft_content


def _parse_decrypted_result(result: Union[str, bytes, Dict[str, Any]], *, path: str) -> Dict[str, Any]:
    if isinstance(result, dict):
        return result
    if isinstance(result, str):
        data = result.encode("utf-8")
    elif isinstance(result, bytes):
        data = result
    else:
        raise TypeError("解密器返回值必须是str、bytes或dict")
    try:
        return parse_draft_content(data, path=path)
    except exceptions.DraftContentEncrypted as exc:
        raise exceptions.DraftDecryptFailed("解密器返回的内容仍然不是明文JSON") from exc


def _encrypted_message(path: str) -> str:
    location = " '%s'" % path if path else ""
    return (
        "草稿文件%s看起来是剪映6+版本加密后的draft_content.json。"
        "将自动尝试本地解密；如失败，可传入decryptor回调，"
        "或传入decrypt_api_key/设置%s作为兜底。"
    ) % (location, ENV_DECRYPT_API_KEY)
