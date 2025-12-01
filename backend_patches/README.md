Backend patches and suggested changes for files outside this repo (r:\\Rob\\backend).

This folder contains suggested patches and automation scripts to:
- Replace hard-coded PII (birth_date, driver_license, iPhone serials, owner info) with a secure loader or environment variables.
- Add usage notes for `secrets_loader` to load identity and secrets for manifesto & daemon files.

Files:
- `manifesto_generator.suggested_patch.md`: instructions and suggested code to use `secrets_loader` and remove direct PII printing.
- `deimon_boots.suggested_patch.md`: instructions to replace PII with secure loader calls and avoid writing PII to logs.
- `hardstamp_signal.suggested_patch.md`: patch to read `IPHONE_SERIAL` from env and avoid hard-coded serials.

How to apply:
1. Open the file you want to update in your backend workspace (`r:\Rob\\backend`).
2. Apply the changes manually or via an automated script if you have write access in that repo.
3. Run tests and verify behavior.
