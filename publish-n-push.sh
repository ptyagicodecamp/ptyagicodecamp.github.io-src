#!/bin/bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
TMP_OUTPUT="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_OUTPUT"
}
trap cleanup EXIT

cd "$ROOT_DIR"

echo "Generating published site into temp output..."
./.venv/bin/pelican content -o "$TMP_OUTPUT" -s publishconf.py

echo "Syncing generated site into output repo..."
rsync -a --delete --exclude '.git' "$TMP_OUTPUT"/ "$ROOT_DIR/output"/

echo "Pushing source repo changes..."
git add -A .gitignore pelicanconf.py publish-n-push.sh themes/Flex
git commit -m "Vendor Flex theme for publishing" || true
git push origin HEAD:master

echo "Pushing generated website..."
git -C output add .
git -C output commit -m "Publish themed site" || true
git -C output push origin HEAD:master

echo "Updating output submodule pointer..."
git add output
git commit -m "Update published site submodule" || true
git push origin HEAD:master
