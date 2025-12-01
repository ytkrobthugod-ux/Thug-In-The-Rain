# Secure relocation and loading of Roberto permanent memory

This folder contains scripts and utilities for relocating and loading the sensitive `roberto_permanent_memory.json` file in a secure fashion.

Important notes:
- Never commit raw PII to the repository. Use the relocation script to encrypt and move the file to a `secrets/` folder outside of source control.
- Keep `ROBERTO_MEMORY_KEY` in your secure environment (Key Vault, HashiCorp Vault, or other secret manager). Do not store keys in the repository.
- For local development, a developer may set `ROBERTO_PERMANENT_MEMORY` environment variable with base64-encoded JSON (not recommended for production).

Scripts:
- `relocate_permanent_memory.py` — Encrypts and relocates permanent memory to `security/secrets` and writes a placeholder to the original path.
- `secrets_loader.py` — Library that loads memory securely via an env var or encrypted file. It requires `ROBERTO_MEMORY_KEY` in the environment to decrypt `.enc` files.

Example flow:
1. Generate a secure Fernet key and store it in your secret manager or environment variable `ROBERTO_MEMORY_KEY`.
   - `python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"`
2. Run the relocation script using the path to your existing `roberto_permanent_memory.json` file:
   - `python security/relocate_permanent_memory.py --source "path/to/roberto_permanent_memory.json"
3. Export `ROBERTO_PERMANENT_MEMORY_PATH` in your environment or in your secrets manager and set `ROBERTO_MEMORY_KEY` to allow service to decrypt when necessary.

Loading:
Use the loader in your service code:

```python
from security.secrets_loader import load_roberto_memory
memory = load_roberto_memory()
```

This function will only return a value if the environment is configured correctly. Plaintext fallback from repository files is disabled by default.
