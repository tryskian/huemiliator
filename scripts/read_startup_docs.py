from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_DOCS = (
    Path("README.md"),
    Path("docs/governance/CHARTER.md"),
    Path("docs/governance/DECISIONS.md"),
    Path("docs/runtime/RUNBOOK.md"),
    Path("docs/runtime/ARCHITECTURE.md"),
    Path("docs/governance/SESSION_HANDOFF.md"),
)
OPTIONAL_LOCAL_DOCS = (Path("docs/peanut/governance/SESSION_HANDOFF.md"),)

LAST_UPDATED_PATTERN = re.compile(
    r"^Last updated:\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE
)
TITLE_PATTERN = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def extract_title(text: str) -> str | None:
    match = TITLE_PATTERN.search(text)
    if match is None:
        return None
    return match.group(1).strip()


def find_last_updated(text: str) -> str | None:
    match = LAST_UPDATED_PATTERN.search(text)
    if match is None:
        return None
    return match.group(1)


def summarize_doc(path: Path) -> str:
    text = path.read_text()
    title = extract_title(text) or "untitled"
    updated = find_last_updated(text)
    summary = f"- {path.as_posix()} | {title}"
    if updated is not None:
        summary += f" | Last updated: {updated}"
    return summary


def main() -> int:
    failures: list[str] = []
    summaries: list[str] = []
    checked_docs: list[Path] = []

    for path in REQUIRED_DOCS:
        checked_docs.append(path)
        if not path.exists():
            failures.append(f"{path}: missing required startup doc")
            continue
        summaries.append(summarize_doc(path))

    for path in OPTIONAL_LOCAL_DOCS:
        if not path.exists():
            continue
        checked_docs.append(path)
        summaries.append(summarize_doc(path))

    if failures:
        print("startup-docs-read: FAIL", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"startup-docs-read: PASS ({len(checked_docs)} docs inspected)")
    for summary in summaries:
        print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
