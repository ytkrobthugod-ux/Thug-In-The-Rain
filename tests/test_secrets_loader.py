import os
import json
import tempfile
from pathlib import Path

from security.secrets_loader import load_roberto_memory


def test_load_from_env(monkeypatch):
    data = {"creator": "test"}
    monkeypatch.setenv('ROBERTO_PERMANENT_MEMORY', json.dumps(data))
    res = load_roberto_memory()
    assert res['creator'] == 'test'


def test_load_plaintext_file(monkeypatch, tmp_path):
    # Create a temp file and point to it, with explicit opt-in
    data = {"creator": "filetest"}
    p = tmp_path / 'memory.json'
    p.write_text(json.dumps(data))
    monkeypatch.setenv('ROBERTO_PERMANENT_MEMORY_PATH', str(p))
    monkeypatch.setenv('ROBERTO_ALLOW_PLAINTEXT_MEMORY', '1')
    res = load_roberto_memory()
    assert res['creator'] == 'filetest'
