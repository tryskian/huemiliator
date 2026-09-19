#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

TOTAL_STEPS=14
if [ "${END_SKIP_STOP:-}" = "1" ]; then
	TOTAL_STEPS=$((TOTAL_STEPS - 1))
fi
if [ "${END_SKIP_GIT_CHECK:-}" = "1" ]; then
	TOTAL_STEPS=$((TOTAL_STEPS - 1))
fi

STEP=1

run_step() {
	local label="$1"
	shift
	echo "[end] ${STEP}/${TOTAL_STEPS} ${label}"
	"$@"
	STEP=$((STEP + 1))
}

echo "[end] starting end-of-day routine in: $ROOT_DIR"
run_step "end-docs-check" make --no-print-directory end-docs-check
run_step "doctor-env" make --no-print-directory doctor-env
run_step "tracked path leak check" make --no-print-directory path-leak-check
run_step "local path leak audit" make --no-print-directory path-leak-audit-local
run_step "lint-docs" make --no-print-directory lint-docs
run_step "scripts-check" make --no-print-directory scripts-check
run_step "check" make --no-print-directory check
run_step "package-check" make --no-print-directory package-check
run_step "package-install-check" make --no-print-directory package-install-check
run_step "security-checks" make --no-print-directory security-checks
run_step "pending eval gate" make --no-print-directory end-pending-check

if [ "${END_SKIP_STOP:-}" = "1" ]; then
	echo "[end] stop background tasks skipped (preflight only; day is not closed)"
else
	run_step "stop background tasks" make --no-print-directory decaffeinate
fi

run_step "session snapshot" make --no-print-directory session-status

if [ "${END_SKIP_GIT_CHECK:-}" = "1" ]; then
	echo "[end] git closeout skipped (preflight only; day is not closed)"
else
	run_step "git closeout" bash ./scripts/check_end_git_clean.sh
fi

echo "[end] done"
