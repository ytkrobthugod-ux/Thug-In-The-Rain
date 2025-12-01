## Summary
This PR adds secure relocation scripts and a loader to prevent storing PII in the repository. It includes:
- `security/secrets_loader.py` — secure loader for Roboto permanent memory
- `security/relocate_permanent_memory.py` — relocation and encryption script
- `security/roberto_permanent_memory.json.example` — redacted example file
- `.gitignore` update to prevent secrets being tracked
- `SECURITY.md` and `security/README.md` for instructions

## Checklist
- [ ] No PII/secret content remains in repository files.
- [ ] Replacement placeholder added.
- [ ] Tests for secrets loader pass.
- [ ] Owner approved key rotation & storage plan.

## Migration steps
1. Run the relocation script against any tracked `roberto_permanent_memory.json` in your repository or external path:
   - `python security/relocate_permanent_memory.py --source "r:\\Rob\\backend\\roberto_permanent_memory.json"`
2. Confirm the encrypted file `security/secrets/roberto_permanent_memory.json.enc` is in secure storage (or a secrets manager) but not in the repo.
3. Run `security/remove_plaintext_from_git.sh` to untrack and commit the placeholder.
4. Consider cleaning git history if the file had been committed previously (`git filter-repo` or `BFG`), and consult the owner for HMEC/GDPR policy.
