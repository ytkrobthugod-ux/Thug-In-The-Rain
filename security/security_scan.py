"""
Simple PII scan script for workspace.
Searches for common PII-like patterns (birth_date, driver_license, phone numbers, emails, iphone serials, names) in text files.
"""
import re
from pathlib import Path
import argparse

PATTERNS = {
    'birth_date': re.compile(r"birth[_ ]date|birthdate|birth_date", re.IGNORECASE),
    'driver_license': re.compile(r"driver[_ ]license|driverlicense", re.IGNORECASE),
    'email': re.compile(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+"),
    'iphone_serial': re.compile(r"G[A-Z0-9]{9}") ,
    'full_name_roberto': re.compile(r"Roberto\s+Villarreal|Roberto\s+Villarreal\s+Martinez", re.IGNORECASE),
    'cash_app': re.compile(r"\$[A-Za-z0-9_]+")
}


def scan_files(root: Path, include_exts=('.py','.md','.txt','.json','.yaml','.yml')):
    findings = []
    for p in root.rglob('*'):
        try:
            if not p.is_file():
                continue
            if p.suffix.lower() not in include_exts:
                continue
            text = p.read_text(errors='ignore')
            for name, pat in PATTERNS.items():
                for m in pat.finditer(text):
                    findings.append((str(p), name, m.group(0).strip()))
        except Exception:
            # ignore unreadable files
            continue
    return findings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', default='.', help='Root folder to scan')
    args = parser.parse_args()
    root = Path(args.root)
    results = scan_files(root)
    if not results:
        print('No PII-like patterns found in scanned files.')
        return 0
    print('\nFound potential PII entries:')
    for path, kind, match in results:
        print(f"- {kind}: {match} in {path}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
