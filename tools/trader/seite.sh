#!/usr/bin/env bash
# Webseite bauen (verschlüsselt) und auf den Branch gh-pages pushen. Braucht PUSH_URL (mit Token) und cryptography.
set -euo pipefail
python3 tools/trader/site.py build
cd _site
rm -rf .git
git init -q -b gh-pages
git config user.name "github-actions[bot]"
git config user.email "41898283+github-actions[bot]@users.noreply.github.com"
git add -A
git commit -q -m "Webseite $(date -u +%Y-%m-%dT%H:%MZ)"
git push -q -f "$PUSH_URL" gh-pages
