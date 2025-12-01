#!/usr/bin/env bash
# Safely remove roberto_permanent_memory.json from tracking and commit changes.
# WARNING: This script makes changes to git history in a safe manner (untracked remove only), do not use to rewrite history.

set -euo pipefail

SOURCE=${1:-backend/roberto_permanent_memory.json}

if [ ! -f "$SOURCE" ]; then
  echo "Source not found: $SOURCE"
  exit 1
fi

echo "Backing up current plaintext file to $SOURCE.bak"
cp "$SOURCE" "$SOURCE.bak"

echo "Staging placeholder addition, .gitignore updates, and secrets dir"
git add .gitignore
git add security/roberto_permanent_memory.json.example
git rm --cached "$SOURCE" || true
git add security/secrets || true
git commit -m "Remove plaintext roberto_permanent_memory.json from tracking and add secure loader/placeholder"

echo "File removed from tracking. Consider purging git history if needed using 'git filter-repo' or contact the repo owner if a secure purge is required."

exit 0
