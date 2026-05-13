PYTHON ?= python3
VENV ?= .venv
BIN := $(VENV)/bin
PY := $(shell if [ -x "$(BIN)/python" ]; then echo "$(BIN)/python"; else echo "$(PYTHON)"; fi)

.PHONY: install env doctor-env test lint format-check format typecheck check package-check app session-status start rituals end end-preflight end-docs-check end-git-check

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

test:
	PYTHONPATH=src $(PY) -m pytest

lint:
	$(PY) -m ruff check scripts src tests

format-check:
	$(PY) -m ruff format --check scripts src tests

format:
	$(PY) -m ruff format scripts src tests

typecheck:
	PYTHONPATH=src $(PY) -m mypy scripts src tests

check:
	$(MAKE) --no-print-directory format-check
	$(MAKE) --no-print-directory lint
	$(PY) -m compileall scripts src tests
	$(MAKE) --no-print-directory typecheck
	$(MAKE) --no-print-directory test
	git diff --check

package-check:
	PYTHONPATH=src $(PY) -m build

app:
	PYTHONPATH=src $(PY) -m huemiliator

start:
	@set -eu; \
	echo "== Huemiliator Start =="; \
	echo "docs to read:"; \
	for path in \
		README.md \
		docs/governance/CHARTER.md \
		docs/governance/DECISIONS.md \
		docs/runtime/RUNBOOK.md \
		docs/runtime/ARCHITECTURE.md \
		docs/governance/SESSION_HANDOFF.md; do \
		echo "- $$path"; \
	done; \
	if [ -f "docs/peanut/governance/SESSION_HANDOFF.md" ]; then \
		echo "- docs/peanut/governance/SESSION_HANDOFF.md"; \
	fi; \
	echo "repo: $$(pwd)"; \
	echo "branch: $$(git branch --show-current)"; \
	git status --short --branch; \
	$(MAKE) --no-print-directory doctor-env; \
	$(MAKE) --no-print-directory session-status

rituals:
	@cat docs/runtime/START_END_REFERENCE.md

end:
	@set -eu; \
	./scripts/end_of_day_routine.sh

end-preflight:
	end_SKIP_GIT_CHECK=1 ./scripts/end_of_day_routine.sh

end-docs-check:
	$(PY) ./scripts/check_end_docs.py

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
	fi
