#!/bin/bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
status="$(python3 scripts/push_status.py)"
git add .
if ! git diff --cached --quiet; then
    git commit -m "status: $status"
fi
git push
cp .vimrc ~/.vimrc
