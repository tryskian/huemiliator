# Architecture

This is the fast map of Huemiliator's current shape.

The repo is initialised, the docs spine exists, the package scaffold exists,
the picker kernel is implemented, the archived swatch source is frozen locally,
and nearest-swatch resolution is live.

## System Map

| Surface | Role |
| --- | --- |
| `README.md` | public framing and current entrypoint |
| `pyproject.toml` | package metadata and dependency pins |
| `Makefile` | small operator command surface |
| `data/margaret2_swatches.json` | frozen archived swatch snapshot |
| `src/huemiliator/config.py` | app constants and swatch snapshot path |
| `src/huemiliator/picker.py` | macOS native picker and hex parsing |
| `src/huemiliator/resolution.py` | nearest-swatch resolver |
| `src/huemiliator/swatches.py` | swatch parsing and snapshot loading |
| `src/huemiliator/main.py` | CLI entrypoint and command routing |
| `scripts/freeze_margaret2_swatches.py` | snapshot refresh script |
| `tests/` | runtime and repo contract tests |
| `docs/` | charter, decisions, runbook, research notes, and diagrams |

## Current State

What exists now:

- git repo
- package scaffold
- tracked docs
- macOS native picker command
- hex parsing from native picker output
- frozen local swatch snapshot from the archived source page
- nearest-swatch resolution against the frozen local snapshot
- fixed `delta-e cie76` distance rule
- source-order tie-break for duplicate-distance matches
- minimal validation tooling

What does not exist yet:

- family map
- one-up resolver
- eval storage

## Target Runtime Path

1. The user picks a colour through the native macOS colour picker.
2. The runtime receives a hex code.
3. The runtime resolves the nearest swatch from the fixed
   [`margaret2.github.io/pantone-colors`](https://margaret2.github.io/pantone-colors/)
   reference using `delta-e cie76`, with source order as the tie-break.
4. Pantone naming, if used, stays secondary to that reference match.
5. The runtime reads the family and rank from Huemiliator-owned metadata.
6. The runtime selects the deterministic one-up in that same family.
7. The runtime outputs the replacement shade.
8. If a generated line is added later, it should sit after the colour decision,
   not inside it.

## Contracts

- the active input surface should stay narrow
- the live runtime surface is macOS-local
- the colour catalogue should stay fixed and repo-local
- the archived source should be frozen before runtime resolution uses it
- colour resolution should stay deterministic
- swatch distance should stay fixed to `delta-e cie76` until a later tracked change
- tie-breaks should preserve the frozen source order
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
