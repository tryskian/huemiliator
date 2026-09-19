# Session Handoff

Last updated: 2026-09-18

## Start Here

1. Run:
   - `make start`
2. Ground on the startup-docs read across:
   - `README.md`
   - `docs/governance/CHARTER.md`
   - `docs/governance/DECISIONS.md`
   - `docs/runtime/ARCHITECTURE.md`
   - `docs/runtime/RUNBOOK.md`
   - `docs/governance/SESSION_HANDOFF.md`
3. Confirm execution context:
   - repo root or dedicated worktree
   - active branch from `git branch --show-current`
   - host or devcontainer mode
   - clean `main` or feature branch
4. Return the startup breakdown:
   - current state
   - risks
   - next kernel
   - repo or worktree context
   - active branch
5. Start one active kernel.

## Current Staging

| Surface | Current direction |
| --- | --- |
| Boundary | [Pre-Beta: 15-Minute Behaviour Pulses](../research/030_PB_BEHAVIOUR.md), `staged` |
| Focus | Huey's behaviour using the stable colour foundation |
| Agent setup | approximately five short, positive directions with room to reason |
| Eval ownership | assistant runs each 15-minute pulse and supplies verdicts |
| Stopping point | beta note and diagrams prepared; draft review is the next session's entry |
| Review next | draft instructions beside the judgment lens and [execution diagram](../diagrams/BEHAVIOUR_PULSE.md) |
| First behaviour evidence | awaits staging completion and the first pulse |

The human lead clarified this direction on September 18. The restored colour
implementation is the starting point for the transition. Draft wording and
mechanics are identified as proposals in the boundary note; the next research
focus is already chosen.

## Carried Implementation Snapshot

Huemiliator is a small, local, agent-backed colour mini chatbot with a real
picker runtime, deterministic one-up logic, and a closed `Beta 1.0`
fail-pressure pulse lane for the current non-OCR logic method boundary.

The core tracked shape is:

- README now states the Polinko research model is staged for the next beta:
  - status language is model-level, not repo-only
  - badges align with the shared toy-factory status pattern
- dependency/security cleanup is current on `main`:
  - grouped Python dependency updates are merged
  - no open Huemiliator PRs remain
- local shell helper contracts are now a named gate:
  - `make scripts-check` validates tracked `scripts/*.sh`
  - closeout runs the gate before the broader `make check`
- Mac-wide keep-awake control is external to the repo lifecycle:
  - the Coffee Codex plugin owns the one shared session
  - `make start` and `make end` leave that session unchanged
- bare `huemiliator` keeps the runtime local and CLI-first
- the active input surface is the native macOS colour picker
- the canonical user state is one hex code
- the runtime owns swatch matching, family assignment, same-family rank, and
  deterministic one-up selection with neutral undertone-bucket selection
- the loss line stays downstream of the colour decision
- route and family correctness stay binary
- the broader corrected `neutral` continuation at `20106..20120` is the carried
  prior proof surface
- the warm-edge `orange` yellow-gold audit pulse at `20121..20128` is the
  carried warm-edge proof surface
- the warm-edge `yellow` green / olive audit pulse at `20129..20139` is the
  carried warm-edge proof surface
- the warm-edge `orange` pale straw / buff / blush audit pulse at
  `20140..20145` is the carried warm-edge proof surface
- the warm-edge `yellow` residual chartreuse audit pulse at `20146..20150` is
  the carried warm-edge proof surface
- the warm-neutral peach / pearl audit pulse at `20151..20153` is the carried
  warm-edge proof surface
- the colour-boundary warm low-chroma five-family pulse at `20154..20158` is
  the carried colour-boundary proof surface
- the colour-boundary neutral / brown / orange / yellow pulse at
  `20159..20162` is the carried colour-boundary proof surface
- the colour-boundary neutral / pink / brown / red pulse at `20163..20166` is
  the latest proof surface
- the corrected split stack at `20097..20105` cleared the nine cool-edge seams
  from the failed `20082..20096` source surface
- the broader `neutral` continuation from source order `48` passed at `14 / 1`
  and is now quarantined locally
- the first warm-edge audit pulse passed at `8 / 0`
- the second warm-edge audit pulse passed at `11 / 0`
- the third warm-edge audit pulse passed at `6 / 0`
- the fourth warm-edge audit pulse passed at `5 / 0`
- the fifth warm-edge audit pulse passed at `3 / 0`
- the first colour-boundary audit pulse passed at `5 / 0`
- the second colour-boundary audit pulse passed at `4 / 0`
- the third colour-boundary audit pulse passed at `4 / 0`
- the closed third corrected `red` rerun remains the closed row-level
  comparison baseline
- fail-pressure pulse is now the current verdict unit
- `420_RESIDUE` is closed as the residue source map; no new group is queued
  without fresh promoted evidence

Canonical live work stays on the repo `.local` surface. Superseded eval rows
stay quarantined locally instead of mixing back into the live DB.

## Active Kernel

- The documentation pass is complete: the boundary note, diagrams, and re-entry
  pointers carry the chosen method and distinguish draft mechanics.
- Resume with review of the four positive directions beside the judgment lens.
  The fixed-line role, actual agent setup, timing convention, and pulse-wide
  verdict rule remain staging choices for alignment.

## Next Slice

1. Read [PB_BEHAVIOUR](../research/030_PB_BEHAVIOUR.md) and the
   [staged execution diagram](../diagrams/BEHAVIOUR_PULSE.md).
2. Review the four positive draft directions beside the candidate judgment lens.
3. Align the actual agent setup, fixed-line role, pulse timing, observation unit,
   and pulse-wide verdict rule with the human lead.
4. Use the aligned choices to define the next implementation kernel. The first
   completed behaviour pulse will supply the evidence for method activation.

The closed colour stack below remains comparison context. Its full sequence
and interpretation live in [B10](../research/020_B10.md), with the latest
proof in [COLOUR_BOUNDARY_AUDIT](../research/440_COLOUR_BOUNDARY_AUDIT.md).

## Carried Colour Research Snapshot

- closed colour research lane: `Beta 1.0`
- carried prior proof surface: broader corrected `neutral` continuation at
  `20106..20120`
- carried warm-edge proof surface: `orange` yellow-gold audit pulse at
  `20121..20128`
- carried warm-edge proof surface: `yellow` green / olive audit pulse at
  `20129..20139`
- carried warm-edge proof surface: `orange` pale straw / buff / blush audit
  pulse at `20140..20145`
- carried warm-edge proof surface: `yellow` residual chartreuse audit pulse at
  `20146..20150`
- carried warm-edge proof surface: warm-neutral peach / pearl audit pulse at
  `20151..20153`
- carried colour-boundary proof surface: warm low-chroma five-family pulse at
  `20154..20158`
- carried colour-boundary proof surface: neutral / brown / orange / yellow
  pulse at `20159..20162`
- latest proof surface: colour-boundary neutral / pink / brown / red pulse at
  `20163..20166`
- carried prior pulse result: `14 anchors / 1 counted seam / 0 excluded`
- carried warm-edge pulse result: `8 anchors / 0 counted seams / 0 excluded`
- carried warm-edge pulse result: `11 anchors / 0 counted seams / 0 excluded`
- carried warm-edge pulse result: `6 anchors / 0 counted seams / 0 excluded`
- carried warm-edge pulse result: `5 anchors / 0 counted seams / 0 excluded`
- carried warm-edge pulse result: `3 anchors / 0 counted seams / 0 excluded`
- carried colour-boundary pulse result: `5 anchors / 0 counted seams / 0 excluded`
- carried colour-boundary pulse result: `4 anchors / 0 counted seams / 0 excluded`
- latest pulse result: `4 anchors / 0 counted seams / 0 excluded`
- stable red pulse results:
  - `19692..19706` -> `11 anchors / 4 counted seams / 0 excluded`
  - `19707..19721` -> `10 anchors / 5 counted seams / 0 excluded`
- first yellow comparison slice:
  - `19722..19736` -> `9 anchors / 6 counted seams / 0 excluded`
- yellow fail surface:
  - `19737..19751` -> `5 anchors / 10 counted seams / 0 excluded`
- corrected yellow recovery slice:
  - `19752..19766` -> `10 anchors / 5 counted seams / 0 excluded`
- parked yellow close:
  - `19767..19781` -> `15 anchors / 0 counted seams / 0 excluded`
- opening green pass:
  - `19782..19796` -> `15 anchors / 0 counted seams / 0 excluded`
- parked green close:
  - `19797..19811` -> `15 anchors / 0 counted seams / 0 excluded`
- opening blue pass:
  - `19812..19826` -> `10 anchors / 5 counted seams / 0 excluded`
- deeper blue continuation:
  - `19827..19841` -> `10 anchors / 5 counted seams / 0 excluded`
- parked blue close:
  - `19842..19856` -> `14 anchors / 1 counted seam / 0 excluded`
- opening purple pass:
  - `19857..19871` -> `15 anchors / 0 counted seams / 0 excluded`
- parked purple close:
  - `19872..19886` -> `15 anchors / 0 counted seams / 0 excluded`
- opening pink pass:
  - `19887..19901` -> `9 anchors / 6 counted seams / 0 excluded`
- parked pink close:
  - `19902..19916` -> `15 anchors / 0 counted seams / 0 excluded`
- opening orange pass:
  - `19917..19931` -> `9 anchors / 6 counted seams / 0 excluded`
- deeper orange continuation:
  - `19932..19946` -> `11 anchors / 4 counted seams / 0 excluded`
- deeper orange gold-edge continuation:
  - `19947..19961` -> `10 anchors / 5 counted seams / 0 excluded`
- orange fail surface:
  - `19962..19976` -> `7 anchors / 8 counted seams / 0 excluded`
- parked orange close:
  - `19977..19991` -> `15 anchors / 0 counted seams / 0 excluded`
- final orange row-order close:
  - `19992..20006` -> `15 anchors / 0 counted seams / 0 excluded`
- opening brown pass:
  - `20007..20021` -> `15 anchors / 0 counted seams / 0 excluded`
- deeper brown continuation:
  - `20022..20036` -> `15 anchors / 0 counted seams / 0 excluded`
- parked brown close:
  - `20037..20051` -> `15 anchors / 0 counted seams / 0 excluded`
- opening neutral pass:
  - `20052..20066` -> `11 anchors / 4 counted seams / 0 excluded`
- deeper neutral continuation:
  - `20067..20081` -> `9 anchors / 6 counted seams / 0 excluded`
- third neutral continuation fail surface:
  - `20082..20096` -> `4 anchors / 11 counted seams / 0 excluded`
- corrected neutral split:
  - `20097..20099` -> `3 anchors / 0 counted seams / 0 excluded`
  - `20100..20102` -> `3 anchors / 0 counted seams / 0 excluded`
  - `20103..20105` -> `3 anchors / 0 counted seams / 0 excluded`
- broader corrected neutral continuation:
  - `20106..20120` -> `14 anchors / 1 counted seam / 0 excluded`
- first warm-edge audit pulse:
  - `20121..20128` -> `8 anchors / 0 counted seams / 0 excluded`
- second warm-edge audit pulse:
  - `20129..20139` -> `11 anchors / 0 counted seams / 0 excluded`
- third warm-edge audit pulse:
  - `20140..20145` -> `6 anchors / 0 counted seams / 0 excluded`
- fourth warm-edge audit pulse:
  - `20146..20150` -> `5 anchors / 0 counted seams / 0 excluded`
- fifth warm-edge audit pulse:
  - `20151..20153` -> `3 anchors / 0 counted seams / 0 excluded`
- first colour-boundary audit pulse:
  - `20154..20158` -> `5 anchors / 0 counted seams / 0 excluded`
- second colour-boundary audit pulse:
  - `20159..20162` -> `4 anchors / 0 counted seams / 0 excluded`
- third colour-boundary audit pulse:
  - `20163..20166` -> `4 anchors / 0 counted seams / 0 excluded`
- research visuals:
  - `docs/research/family-range-palette.svg`
  - `docs/research/family-count-bars.svg`
  - `docs/research/active-fail-surface-split.svg`
  - `docs/research/eval-pulse-stack.svg`
  - `docs/research/eval-residue-family-bars.svg`
  - regenerate research charts with `npm run charts:research`
  - derive chart lane labels from row data; archive labels stay annotations
- historical question before the warm-edge audit: choose the next method or
  scope after all runtime family lanes have parked reads
- colour-audit continuation rule: new groups require fresh promoted evidence
- pulse operator surface: start, label, report, and local quarantine are live
- historical staging note: `010_PB10`
- corrected neutral method note: `410_N3`
- closed beta note: `020_B10`
- closed warm-edge note: `430_WARM_EDGE_AUDIT`
- closed colour-boundary note: `440_COLOUR_BOUNDARY_AUDIT`
- active family lane before the warm-edge audit: none selected after
  `neutral` park
- active family lane: none; colour-boundary audit is closed and no pulse is
  queued
- tracked research notes:
  - `000_LEGEND`
  - `010_PB10`
  - `020_B10`
  - `120_BROWN`
  - `210_RED_ORANGE`
  - `310_RED_ORANGE_AUDIT`
  - `410_N3`
  - `420_RESIDUE`
  - `430_WARM_EDGE_AUDIT`
  - `440_COLOUR_BOUNDARY_AUDIT`
- live DB rule: keep only the latest proof surface in `eval_outputs`

## Guardrails

- keep the repo small and local
- keep the live runtime surface macOS-local
- keep one active kernel at a time
- keep one active sampler at a time
- keep colour-audit pressure on one family lane at a time when a colour pulse is queued
- keep the live DB limited to the latest proof surface
- keep `.local/` and `docs/peanut/` local unless explicitly promoted
- capture notes, findings, and truth-surface changes as they emerge
- keep tracked docs truthful to the current repo surface
- keep tracked research-note names aligned with the `NNN_CODE` contract

## Pinned Later

- keep the procedure-first execution contract aligned across the repo family
- carry the same truth order across repos:
  - docs
  - live code
  - live DB
  - then change
- keep command and operator surfaces truthful; do not invent behaviour the repo
  does not actually implement

## Close A Session

1. Run:
   - `make end`
2. Treat `make end-preflight` as preflight only:
   - use it only when an explicit branch-local preflight was requested
   - do not treat it as a day-close substitute

## Copy/Paste Refresh Prompt

```text
Run make start. Use the startup-docs read across README.md,
docs/governance/CHARTER.md, docs/governance/DECISIONS.md,
docs/runtime/ARCHITECTURE.md, docs/runtime/RUNBOOK.md,
docs/governance/SESSION_HANDOFF.md, and local
docs/peanut/governance/SESSION_HANDOFF.md if present. Read the next method in
docs/research/030_PB_BEHAVIOUR.md and docs/diagrams/BEHAVIOUR_PULSE.md.

In 5 bullets: current state, risks, next kernel, repo or worktree context, and
active branch.

Confirm environment/workspace context: canonical repo path is
/abs/path/to/huemiliator, host vs devcontainer mode, active git branch, and
clean main or feature branch.

Apply no-guessing controls: prefer repo-scoped edits and preserve user shell
profile files and global VS Code settings unless explicitly approved in-chat.

Carry the agreed direction: stable colour logic, about five positive agent
directions, reasoning space, and assistant-run and judged 15-minute behaviour
pulses. Start with the beta notes and diagrams. Use the Next Slice to align
the next bounded kernel with the human lead, then execute that kernel.
```
