# Architecture

This is the fast map of Huemiliator's current shape.

The repo is initialised, the docs spine exists, the package scaffold exists,
the picker kernel is implemented, the archived swatch source is frozen locally,
nearest-swatch resolution is live, and the first family taxonomy and rank layer
is live, the first replacement step is live, and the first loss-line layer is
live.

## System Map

| Surface | Role |
| --- | --- |
| `README.md` | public framing and current entrypoint |
| `pyproject.toml` | package metadata and dependency pins |
| `Makefile` | small operator command surface |
| `data/margaret2_swatches.json` | frozen archived swatch snapshot |
| `src/huemiliator/config.py` | app constants and swatch snapshot path |
| `src/huemiliator/colour_math.py` | shared colour metrics |
| `src/huemiliator/eval_db.py` | local SQLite evidence storage helpers |
| `src/huemiliator/eval_sampling.py` | long-run local sampler helpers |
| `src/huemiliator/families.py` | family taxonomy and same-family ranking |
| `src/huemiliator/picker.py` | macOS native picker and hex parsing |
| `src/huemiliator/pipeline.py` | shared deterministic one-up state |
| `src/huemiliator/resolution.py` | nearest-swatch resolver |
| `src/huemiliator/swatches.py` | swatch parsing and snapshot loading |
| `src/huemiliator/main.py` | CLI entrypoint and command routing |
| `scripts/freeze_margaret2_swatches.py` | snapshot refresh script |
| `output/jupyter-notebook/` | follow-along experiment notebook |
| `tests/` | runtime and repo contract tests |
| `docs/` | charter, decisions, runbook, research notes, and diagrams |

## Current State

What exists now:

- git repo
- package scaffold
- tracked docs
- macOS native UI picker command
- hex parsing from native picker output
- frozen local swatch snapshot from the archived `margaret2/pantone-colors`
  source surface
- nearest-swatch resolution against the frozen local snapshot
- fixed `delta-e cie76` distance rule
- source-order tie-break for duplicate-distance matches
- first closed family taxonomy:
  - `neutral`
  - `brown`
  - `red`
  - `orange`
  - `yellow`
  - `green`
  - `blue`
  - `purple`
  - `pink`
- same-family rank from one fixed ladder:
  - chromatic families sort by Lab chroma strength
  - `neutral` sorts by distance from mid-lightness
  - `brown` demotes the yellow/gold/olive shoulder below the earthy core
- brown boundary refinement:
  - darker earthy warm tones can enter `brown` before the neutral gate
  - pale warm neutrals still stay in `neutral`
- deterministic replacement rule:
  - move to the next higher rank inside the same family
  - clamp at the family top rank
- deterministic loss-line rule:
  - emit one fixed short line from a family-keyed bank
  - keep the line layer downstream of the replacement shade
- local SQLite evidence storage for deterministic outputs
- human PASS/FAIL verdicts on stored outputs
- long-run local source-order sampling over the frozen snapshot
- optional one-family runs that preserve source order inside the filtered subset
- one follow-along notebook for local inspection

## Target Runtime Path

1. The user picks a colour through the native macOS UI colour picker.
2. The runtime receives a hex code.
3. The runtime resolves the nearest swatch from the fixed archived
   [`margaret2/pantone-colors`](https://github.com/margaret2/pantone-colors)
   source surfaced at
   [`margaret2.github.io/pantone-colors`](https://margaret2.github.io/pantone-colors/)
   reference using `delta-e cie76`, with source order as the tie-break.
4. Pantone naming, if used, stays secondary to that reference match.
5. The runtime classifies the matched swatch into a closed Huemiliator-owned
   family set with fixed neutral and hue thresholds.
6. The runtime reads the same-family rank from one fixed family-strength ladder.
   - for `brown`, the yellow/gold/olive shoulder sits below the earthy core
7. The runtime selects the next same-family rank, clamped at the family top.
8. The runtime outputs the replacement shade.
9. The runtime appends one short fixed loss line from the matched family bank.
10. The local evidence lane can optionally record the deterministic output in
    SQLite for follow-along inspection.
11. The local sampler can append rows over time from the frozen snapshot in
    source order.
12. The human review lane can mark stored rows as `pass` or `fail`.
13. If a generated line is ever added later, it should sit after the colour
    decision, not inside it.

## Contracts

- the active input surface should stay narrow
- the live runtime surface is macOS-local
- the colour catalogue should stay fixed and repo-local
- the archived source should be frozen before runtime resolution uses it
- colour resolution should stay deterministic
- swatch distance should stay fixed to `delta-e cie76` until a later tracked change
- tie-breaks should preserve the frozen source order
- family taxonomy should stay explicit and closed
- same-family rank should stay on one fixed strength ladder
- one-up selection should stay deterministic and non-wrapping
- loss lines should stay fixed-bank and downstream of the colour decision
- local evidence storage should stay SQLite, local, and optional to the
  runtime loop
- long-run local sampling should stay deterministic and source-ordered
- the first verdict lane should stay human-owned and binary
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
