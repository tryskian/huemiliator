# Architecture

This is the fast map of Huemiliator's current shape.

The repo is initialised, the docs spine exists, and the package scaffold exists.
The runtime is not yet implemented.

## System Map

| Surface | Role |
| --- | --- |
| `README.md` | public framing and current entrypoint |
| `pyproject.toml` | package metadata and dependency pins |
| `Makefile` | small operator command surface |
| `src/huemiliator/config.py` | app constants and future dataset paths |
| `src/huemiliator/main.py` | current scaffold entrypoint |
| `tests/` | scaffold contract tests |
| `docs/` | charter, decisions, runbook, research notes, and diagrams |

## Current State

What exists now:

- git repo
- package scaffold
- tracked docs
- minimal validation tooling

What does not exist yet:

- colour picker surface
- Pantone dataset ingestion
- family map
- one-up resolver
- eval storage

## Target Runtime Path

1. The user picks a colour through a native colour picker.
2. The runtime receives a hex code.
3. The runtime resolves the nearest Pantone entry from the fixed inventory.
4. The runtime reads the family and rank from Huemiliator-owned metadata.
5. The runtime selects the deterministic one-up in that same family.
6. The runtime outputs the better colour.
7. If a generated line is added later, it should sit after the colour decision,
   not inside it.

## Contracts

- the active input surface should stay narrow
- the colour catalogue should stay fixed and repo-local
- colour resolution should stay deterministic
- family mapping should stay explicit
- one-up selection should stay deterministic
- eval verdicts should stay binary:
  - `pass`
  - `fail`

## Docs Ownership

| Doc | Job |
| --- | --- |
| `README.md` | public framing and entrypoint |
| `docs/governance/CHARTER.md` | durable rules and working model |
| `docs/governance/DECISIONS.md` | durable runtime and eval decisions |
| `docs/governance/SESSION_HANDOFF.md` | current checkpoint and next kernel |
| `docs/runtime/ARCHITECTURE.md` | stable system map |
| `docs/runtime/RUNBOOK.md` | operator procedure and validation |
| `docs/research/README.md` | current research framing |
| `docs/diagrams/PIPELINE.md` | canonical target flow |
