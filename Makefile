PYTHON ?= python3
VENV ?= .venv
BIN := $(VENV)/bin
PY := $(shell if [ -x "$(BIN)/python" ]; then echo "$(BIN)/python"; else echo "$(PYTHON)"; fi)
CAFFEINATE_PID_FILE ?= /tmp/huemiliator-caffeinate.pid
CAFFEINATE_LOG ?= /tmp/huemiliator-caffeinate.log
CAFFEINATE_CMD ?= /usr/bin/caffeinate -d -i -m
PIP_AUDIT_ARGS ?=

.PHONY: install env doctor-env path-leak-check path-leak-audit-local test lint lint-docs format-check format typecheck precommit-install precommit-run prepush-run check package-check package-install-check security-checks app startup-docs-read session-status caffeinate decaffeinate caffeinate-status decaffeinate-status start rituals end end-preflight end-docs-check end-pending-check end-git-check

install:
	$(PYTHON) -m venv $(VENV)
	$(BIN)/python -m pip install --upgrade pip
	$(BIN)/python -m pip install -e ".[dev]"

env:
	@test -d "$(VENV)" || (echo "Missing .venv. Run make install." && exit 1)
	@echo "Opening shell in $(VENV)"
	@. "$(BIN)/activate" && exec "$$SHELL" -i

doctor-env:
	$(PY) ./scripts/doctor_env.py

path-leak-check:
	$(PY) ./scripts/path_leak_check.py --scope tracked

path-leak-audit-local:
	$(PY) ./scripts/path_leak_check.py --scope local

test:
	PYTHONPATH=src $(PY) -m pytest

lint:
	$(PY) -m ruff check scripts src tests

lint-docs:
	@set -eu; \
	files="$$(git ls-files '*.md')"; \
	if [ -z "$$files" ]; then \
		echo "No tracked markdown files to lint."; \
		exit 0; \
	fi; \
	npx --yes markdownlint-cli2 $$files

format-check:
	$(PY) -m ruff format --check scripts src tests

format:
	$(PY) -m ruff format scripts src tests

typecheck:
	PYTHONPATH=src $(PY) -m mypy scripts src tests

precommit-install:
	$(PY) -m pre_commit install --install-hooks --hook-type pre-commit --hook-type pre-push

precommit-run:
	$(PY) -m pre_commit run --all-files

prepush-run:
	$(PY) -m pre_commit run --all-files --hook-stage pre-push

check:
	$(MAKE) --no-print-directory format-check
	$(MAKE) --no-print-directory lint
	$(PY) -m compileall scripts src tests
	$(MAKE) --no-print-directory typecheck
	$(MAKE) --no-print-directory test
	git diff --check

package-check:
	PYTHONPATH=src $(PY) -m build

package-install-check:
	$(PY) -m pip install --no-deps -e .
	$(PY) -c "import importlib; importlib.import_module('huemiliator'); importlib.import_module('huemiliator.main')"

security-checks:
	$(PY) -m pip_audit $(PIP_AUDIT_ARGS)

startup-docs-read:
	$(PY) ./scripts/read_startup_docs.py

app:
	PYTHONPATH=src $(PY) -m huemiliator

caffeinate:
	@set -eu; \
	if [ "$$(uname -s)" != "Darwin" ]; then \
		echo "caffeinate is macOS-only; skipping."; \
		exit 0; \
	fi; \
	if [ -f "$(CAFFEINATE_PID_FILE)" ]; then \
		PID=$$(cat "$(CAFFEINATE_PID_FILE)" 2>/dev/null || true); \
		if [ -n "$$PID" ] && kill -0 "$$PID" 2>/dev/null; then \
			echo "caffeinate already running (PID $$PID)."; \
			exit 0; \
		fi; \
		rm -f "$(CAFFEINATE_PID_FILE)"; \
	fi; \
	nohup $(CAFFEINATE_CMD) >"$(CAFFEINATE_LOG)" 2>&1 & \
	PID=$$!; \
	echo "$$PID" >"$(CAFFEINATE_PID_FILE)"; \
	sleep 0.1; \
	if kill -0 "$$PID" 2>/dev/null; then \
		echo "caffeinate started (PID $$PID)."; \
	else \
		rm -f "$(CAFFEINATE_PID_FILE)"; \
		echo "Failed to start caffeinate."; \
		exit 1; \
	fi

decaffeinate:
	@set -eu; \
	if [ "$$(uname -s)" != "Darwin" ]; then \
		echo "caffeinate is macOS-only; skipping."; \
		exit 0; \
	fi; \
	if [ ! -f "$(CAFFEINATE_PID_FILE)" ]; then \
		echo "No managed caffeinate PID file found."; \
		exit 0; \
	fi; \
	PID=$$(cat "$(CAFFEINATE_PID_FILE)" 2>/dev/null || true); \
	if [ -n "$$PID" ] && kill -0 "$$PID" 2>/dev/null; then \
		kill "$$PID"; \
		sleep 0.1; \
		echo "caffeinate stopped (PID $$PID)."; \
	else \
		echo "Stale PID file found; cleaning up."; \
	fi; \
	rm -f "$(CAFFEINATE_PID_FILE)"

caffeinate-status:
	@set -eu; \
	if [ "$$(uname -s)" != "Darwin" ]; then \
		echo "caffeinate status is only available on macOS."; \
		exit 0; \
	fi; \
	if [ -f "$(CAFFEINATE_PID_FILE)" ]; then \
		PID=$$(cat "$(CAFFEINATE_PID_FILE)" 2>/dev/null || true); \
		if [ -n "$$PID" ] && kill -0 "$$PID" 2>/dev/null; then \
			echo "Managed caffeinate: RUNNING (PID $$PID)."; \
		else \
			echo "Managed caffeinate: STALE PID file."; \
		fi; \
	else \
		echo "Managed caffeinate: OFF."; \
		EXISTING_PID=$$(pgrep -f "^/usr/bin/caffeinate -d -i -m( |$$)" | head -n 1 || true); \
		if [ -n "$$EXISTING_PID" ]; then \
			echo "Unmanaged caffeinate detected (PID $$EXISTING_PID); not owned by this repo."; \
		fi; \
	fi

decaffeinate-status: caffeinate-status

start:
	bash ./scripts/start_of_day_routine.sh

rituals:
	@cat docs/runtime/START_END_REFERENCE.md

end:
	@set -eu; \
	./scripts/end_of_day_routine.sh

end-preflight:
	END_SKIP_GIT_CHECK=1 END_SKIP_STOP=1 ./scripts/end_of_day_routine.sh

end-docs-check:
	$(PY) ./scripts/check_end_docs.py

end-pending-check:
	PYTHONPATH=src $(PY) ./scripts/eval_status.py --require-zero-pending

end-git-check:
	bash ./scripts/check_end_git_clean.sh

session-status:
	@set -eu; \
	echo "== Huemiliator Session Status =="; \
	echo "repo: $$(pwd)"; \
	if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then \
		echo "branch: $$(git branch --show-current)"; \
		if git diff --quiet --ignore-submodules HEAD -- && [ -z "$$(git ls-files --others --exclude-standard)" ]; then \
			echo "worktree: clean"; \
		else \
			echo "worktree: dirty"; \
		fi; \
	else \
		echo "branch: not a git repo"; \
		echo "worktree: unknown"; \
	fi; \
	if [ -f "docs/governance/SESSION_HANDOFF.md" ]; then \
		echo "handoff: docs/governance/SESSION_HANDOFF.md"; \
	fi; \
	if [ -f "docs/peanut/governance/SESSION_HANDOFF.md" ]; then \
		echo "local handoff: docs/peanut/governance/SESSION_HANDOFF.md"; \
	fi; \
	PYTHONPATH=src $(PY) ./scripts/eval_status.py
