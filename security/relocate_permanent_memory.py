"""
Relocate permanent memory JSON to a secure, encrypted location and replace with a placeholder to avoid tracking PII in repo.

Usage:
  python relocate_permanent_memory.py --source "path/to/roberto_permanent_memory.json" --dest "security/secrets"

It will encrypt the file using `ROBERTO_MEMORY_KEY` env var (Fernet key) if present, otherwise it will generate a key and print it to the console. The encrypted file will be written to `dest` with `.enc` suffix.
"""
from __future__ import annotations
import argparse
import os
import json
import base64
import shutil
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

try:
    from cryptography.fernet import Fernet
    _HAS_FERNET = True
except Exception:
    _HAS_FERNET = False


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def encrypt_and_write(content: bytes, dest_path: Path, key: bytes | None):
    if key is None or not _HAS_FERNET:
        # fallback: store base64 encoded, but still keep outside repo
        encoded = base64.b64encode(content)
        dest_path.write_bytes(encoded)
        logger.warning("cryptography not available; saving base64-encoded file instead: %s", dest_path)
        return
    f = Fernet(key)
    enc = f.encrypt(content)
    dest_path.write_bytes(enc)


def sanitize_and_write_placeholder(orig_path: Path, placeholder_path: Path):
    placeholder = {
        "message": "Sensitive permanent memory relocated outside of repository.",
        "notice": "This file is a placeholder. Do not store PII in the repository."
    }
    placeholder_path.write_text(json.dumps(placeholder, indent=2))
    logger.info("Wrote placeholder to: %s", placeholder_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', '-s', type=str, required=True, help='Path to the current permanent memory JSON file')
    parser.add_argument('--dest', '-d', type=str, default='security/secrets', help='Destination folder for encrypted secrets')
    parser.add_argument('--force', '-f', action='store_true', help='Force overwrite of destination file if it exists')
    args = parser.parse_args()

    source = Path(args.source).expanduser()
    if not source.exists():
        logger.error("Source not found: %s", source)
        return 1

    dest_folder = Path(args.dest).expanduser()
    ensure_dir(dest_folder)

    # read content
    content = source.read_bytes()

    # get or generate key
    env_key = os.environ.get('ROBERTO_MEMORY_KEY')
    if env_key:
        key = env_key.encode('utf-8')
    else:
        if _HAS_FERNET:
            key = Fernet.generate_key()
            logger.warning('No ROBERTO_MEMORY_KEY found. Generated key: %s — store this in environment securely', key.decode())
        else:
            key = None

    # dest path
    dest_path = dest_folder / (source.name + '.enc')
    if dest_path.exists() and not args.force:
        logger.error('Destination already exists: %s — use --force to overwrite', dest_path)
        return 2

    encrypt_and_write(content, dest_path, key)

    # Replace original with sanitized placeholder (do not delete)
    placeholder_path = source.parent / (source.name)
    sanitize_and_write_placeholder(source, placeholder_path)

    logger.info("Relocated and encrypted permanent memory to %s", dest_path)
    logger.info("PLEASE: add %s and %s to your secure secrets manager and remove the plaintext from backups.", dest_path, 'ROBERTO_MEMORY_KEY')
    logger.info("Make sure to add the secrets directory and original file path to .gitignore to avoid re-adding the plaintext to the repo.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
