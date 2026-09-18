from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text()


def assert_make_target(makefile: str, target: str) -> None:
    assert re.search(rf"(?m)^{re.escape(target)}:", makefile), target


def test_makefile_exposes_closeout_tooling_targets() -> None:
    makefile = read("Makefile")

    for target in (
        "lint-docs",
        "scripts-check",
        "package-check",
        "package-install-check",
        "security-checks",
        "end-pending-check",
    ):
        assert_make_target(makefile, target)


def test_end_routine_uses_make_targets() -> None:
    script = read("scripts/end_of_day_routine.sh")

    for command in (
        'run_step "lint-docs" make --no-print-directory lint-docs',
        'run_step "scripts-check" make --no-print-directory scripts-check',
        'run_step "package-check" make --no-print-directory package-check',
        'run_step "package-install-check" '
        "make --no-print-directory package-install-check",
        'run_step "security-checks" make --no-print-directory security-checks',
        'run_step "pending eval gate" make --no-print-directory end-pending-check',
    ):
        assert command in script


def test_repo_lifecycle_does_not_own_mac_wide_power_control() -> None:
    makefile = read("Makefile")
    lifecycle = "\n".join(
        (
            makefile,
            read("scripts/start_of_day_routine.sh"),
            read("scripts/end_of_day_routine.sh"),
        )
    )

    for target in (
        "caffeinate",
        "caffeinate-status",
        "decaffeinate",
        "decaffeinate-status",
    ):
        assert not re.search(rf"(?m)^{re.escape(target)}:", makefile), target

    for local_power_control in (
        "CAFFEINATE_",
        "/usr/bin/caffeinate",
        "make --no-print-directory caffeinate",
        "make --no-print-directory decaffeinate",
    ):
        assert local_power_control not in lifecycle

    docs = "\n".join(
        (
            read("docs/runtime/RUNBOOK.md"),
            read("docs/runtime/START_END_REFERENCE.md"),
            read("docs/governance/DECISIONS.md"),
        )
    )
    for coffee_action in ("`coffee`", "`coffee start`", "`coffee stop`"):
        assert coffee_action in docs


def test_runtime_docs_name_the_closeout_targets() -> None:
    docs = "\n".join(
        read(path)
        for path in (
            "docs/runtime/RUNBOOK.md",
            "docs/runtime/START_END_REFERENCE.md",
            "docs/governance/DECISIONS.md",
        )
    )

    for command in (
        "make lint-docs",
        "make scripts-check",
        "make package-install-check",
        "make security-checks",
        "make end-pending-check",
    ):
        assert command in docs


def test_shell_script_contract_checker_accepts_tracked_scripts() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/check_shell_scripts.py"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )

    assert "shell-script-contracts: PASS" in result.stdout
    assert "scripts checked" in result.stdout
