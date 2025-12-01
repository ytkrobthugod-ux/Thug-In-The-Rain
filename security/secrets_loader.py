"""
Safe secret loader for roberto_permanent_memory.json.

This module provides a secure way to load the permanent memory JSON either
from an environment variable, an encrypted file, or a plain file path.
It will not read any files that are not explicitly configured by environment
variables.
"""
from __future__ import annotations
import os
import json
import base64
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

try:
    from cryptography.fernet import Fernet
    _HAS_FERNET = True
except Exception:
    _HAS_FERNET = False


def _load_from_env(env_var: str = "ROBERTO_PERMANENT_MEMORY") -> Optional[Dict[str, Any]]:
    content = os.environ.get(env_var)
    if not content:
        return None
    try:
        return json.loads(content)
    except Exception:
        try:
            # maybe base64-encoded JSON
            data = base64.b64decode(content)
            return json.loads(data)
        except Exception as e:
            logger.exception("Failed to parse JSON from env var: %s", env_var)
            return None


def _decrypt_file(path: str, key: str) -> Optional[bytes]:
    if not _HAS_FERNET:
        logger.warning("cryptography not installed; cannot decrypt %s", path)
        return None
    try:
        f = Fernet(key)
        with open(path, "rb") as fh:
            enc = fh.read()
        return f.decrypt(enc)
    except Exception:
        logger.exception("Failed to decrypt file %s", path)
        return None


def load_roberto_memory(env_var: str = "ROBERTO_PERMANENT_MEMORY", path_env: str = "ROBERTO_PERMANENT_MEMORY_PATH", key_env: str = "ROBERTO_MEMORY_KEY") -> Optional[Dict[str, Any]]:
    """Load the roberto permanent memory safely.

    Strategy:
    - If `ROBERTO_PERMANENT_MEMORY` env var is set, parse it as JSON (or base64 JSON).
    - Else, if `ROBERTO_PERMANENT_MEMORY_PATH` points to a file and the file ends with `.enc`, decrypt with `ROBERTO_MEMORY_KEY`.
    - Else, if `ROBERTO_PERMANENT_MEMORY_PATH` points to a plain JSON file, load it only if `ROBERTO_ALLOW_PLAINTEXT_MEMORY` env var is set (explicit opt-in).
    """
    # 1) env var JSON
    data = _load_from_env(env_var=env_var)
    if data:
        return data

    # 2) file path
    path = os.environ.get(path_env)
    if not path:
        return None
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        logger.info("Permanent memory path %s does not exist", path)
        return None

    # encrypted file
    if path.endswith(".enc"):
        key = os.environ.get(key_env)
        if not key:
            logger.warning("Encrypted permanent memory needs %s in environment", key_env)
            return None
        plaintext = _decrypt_file(path, key)
        if not plaintext:
            return None
        try:
            return json.loads(plaintext)
        except Exception:
            logger.exception("Failed to parse JSON from decrypted memory file: %s", path)
            return None

    # fallback to plaintext file only when explicitly allowed
    if not os.environ.get("ROBERTO_ALLOW_PLAINTEXT_MEMORY"):
        logger.warning("Plaintext permanent memory file %s requires ROBERTO_ALLOW_PLAINTEXT_MEMORY=1 to be read", path)
        return None
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        logger.exception("Failed to read plaintext memory file: %s", path)
        return None


__all__ = ["load_roberto_memory"]
