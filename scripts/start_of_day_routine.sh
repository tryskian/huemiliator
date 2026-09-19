#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[start] starting morning routine in: $ROOT_DIR"
echo "[start] 1/7 workspace context"
printf 'repo root: %s\n' "$ROOT_DIR"
printf 'branch: %s\n' "$(git branch --show-current)"
git status --short --branch

echo "[start] 2/7 doctor-env"
make --no-print-directory doctor-env

echo "[start] 3/7 caffeinate"
make --no-print-directory caffeinate

echo "[start] 4/7 caffeinate-status"
make --no-print-directory caffeinate-status

echo "[start] 5/7 startup-docs-read"
make --no-print-directory startup-docs-read

echo "[start] 6/7 session-status"
make --no-print-directory session-status

echo "[start] 7/7 STARTUP GATE"
cat <<'EOF'
make start completed the mechanical bootstrap and inspected the tracked startup docs.

Startup completes after the next rehydrate update does all of this:

1. Use the inspected startup-doc surface:
   - README.md
   - docs/governance/CHARTER.md
   - docs/governance/DECISIONS.md
   - docs/runtime/RUNBOOK.md
   - docs/runtime/ARCHITECTURE.md
   - docs/governance/SESSION_HANDOFF.md
   - local docs/peanut/governance/SESSION_HANDOFF.md if present

2. Return 5 bullets:
   - current state
   - risks
   - next kernel
   - repo or worktree context
   - active branch

3. Confirm environment/workspace context:
   - canonical repo path is /abs/path/to/huemiliator
   - host vs devcontainer mode
   - active git branch
   - clean main or feature branch

4. Apply no-guessing controls:
   - prefer repo-scoped edits
   - preserve user shell profile files and global VS Code settings unless explicitly approved in-chat

5. Run one active kernel at a time.

6. Then execute the Next Kernel from SESSION_HANDOFF with minimal behavior drift and full validation.
EOF
