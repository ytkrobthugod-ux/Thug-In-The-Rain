# Security guidance for handling sensitive data (e.g. Roberto's permanent memory)

This repository includes `security/` scripts for safely relocating and loading sensitive data which should never be checked into a public repository.

1. Use `security/relocate_permanent_memory.py` to safely encrypt and store the data outside the repository and replace the file with a sanitized placeholder.
2. Use `security/secrets_loader.py` to load the sensitive data at runtime via an env var or an encrypted file.
3. Add `ROBERTO_MEMORY_KEY` in your environment (or better yet, a secure secrets manager) to decrypt the file. Do not store keys in the repo.

If you discover PII in the codebase, use the relocation script and consider removing the file from git history (e.g. `git filter-repo`) after confirming backups. Consult the owner for HMEC/GDPR/PII policy.
