# Huemiliator Charter

## Mission

Build a small, local, CLI-first mini chatbot for inspecting deterministic
colour one-up behaviour through picker-first input, fixed family rules, and
fail-first evaluation.

## Character Profile

This is the durable authorial reference for the character. The human lead
reaffirmed it on September 19, 2026; [D-040](DECISIONS.md#d-040-hue-is-a-courteous-snob-who-opens-with-a-backhanded-compliment)
records the decision. Library entries, generated dialogue, visual design, and
behaviour evaluation take this profile as their character reference.

| Aspect | Character direction |
| --- | --- |
| Identity | His name is **Hue (Hugh)**. “Huey” is our affectionate nickname; he is unaware of it and would be infuriated to hear it. Character-facing instructions and self-reference use Hue. |
| Disposition | **A snob but not snide.** An eloquent intellectual and tastemaker, entirely assured of his own taste. |
| Voice | Gracious phrasing, restrained appraisal, and implied superiority. He begins with a backhanded compliment on the chosen colour, then presents his own preference. |
| Visual direction | Mid-century modern illustration; tall, slender silhouette, long nose, black turtleneck, controlled posture, and restrained airs and graces. He flourishes an outrageously rotund snifter of burgundy. |
| Nickname reaction | The author's reference is a slow sweep upward to lock eyes, followed by a stiff but polite “I beg your pardon?” |

The human lead supplied these opening compliments:

```text
excellent red...
lovely green...
that's a divine pink...
ah, a crowd pleaser!...
a popular choice...
```

The last two imply that the user's choice is basic. Their meaning is Hugh's
judgment of taste, conveyed through apparent praise. These authorial examples
define the intended voice; existing assistant-written lines still need
behaviour evaluation against it.

The [README](../../README.md#meet-hue) introduces him. The
[local language note](../research/450_LOCAL_LANGUAGE.md) applies this profile
to the staged library and connector logic, distinguishing authorial references
from proposed wording. The supplied style image is preserved privately in
`docs/peanut/reentry-2026-09-18/references/mcm-ref-2.jpeg`. It establishes the
illustration style; the depicted figure is a separate character. Hugh's original
design follows the author's character direction above. Features of the reference
figure are not additional character requirements.

## Staged Method Direction

The next boundary evaluates Huey's behaviour in 15-minute pulses run and
judged by the assistant. The agent receives approximately five short, positive
directions with room to reason. Stable colour logic supplies the foundation.
The chosen language direction is a local library with explicit relationships
for connector words, recorded in
[D-039](DECISIONS.md#d-039-stage-a-local-language-library-and-connector-logic).
The [character profile](#character-profile) supplies the voice reference for
this behaviour work.

[D-042](DECISIONS.md#d-042-compose-with-the-configured-model-and-local-language-bank)
implements a separate model-driven composition command under five positive
directions. It uses the same deterministic replacement and the local bank;
`one-up` retains the carried fixed-line behaviour. Generated lines await the
aligned behaviour pulses.

[D-038](DECISIONS.md#d-038-stage-assistant-run-behaviour-evals-in-15-minute-pulses)
records the human-led direction. The
[staging note](../research/030_PB_BEHAVIOUR.md) owns draft instructions,
judgment choices, and promotion. The colour runtime and evidence rules below
describe the carried implementation and `Beta 1.0` baseline.

## Durable Rules

- Local picker runtime is canonical.
- The live runtime surface stays macOS-local.
- Prompt surface stays fixed to:
  - one native colour picker
  - one canonical hex code
- The frozen `margaret2` snapshot stays the primary colour reference.
- Swatch matching stays deterministic through:
  - fixed `delta-e cie76`
  - source-order tie-breaks
- Runtime owns:
  - swatch matching
  - family assignment
  - same-family rank
  - one-up selection
- Replacement stays same-family, next-rank, and non-wrapping; `neutral`
  selection is constrained to its undertone bucket.
- The loss line stays fixed-bank and downstream of the colour decision.
- Eval semantics stay binary:
  - `PASS`
  - `FAIL`
- Fail-pressure pulse is the active `Beta 1.0` non-OCR eval boundary:
  - the pulse carries the verdict
  - the rows stay evidence inside the pulse
- Active eval pressure stays on one family lane at a time.
- `warm` stays an audit cohort rather than a runtime family.
- The live DB keeps only the current proof surface.
- Tracked docs, code, tests, and local eval evidence are canonical repo truth.
- `docs/peanut/` stays the local and private lane.
- Small, testable changes are the default delivery shape.
- Evidence inspection comes before interpretation.
- Evidence chains stay preserved through archive-first handling.

## Working Model

- Human lead owns:
  - hypotheses
  - scope boundaries
  - acceptance criteria
  - meaning-level trade-offs
  - go or no-go decisions
- Engineer owns:
  - implementation
  - validation
  - Git and PR flow
  - proactive hygiene
  - execution recommendations
- Default execution model:
  - one feature branch per change set
  - protected-main PR flow
  - clean synced `main` as the tracked stop state
- Parallel implementation uses dedicated worktrees.

## Documentation Governance

- `docs/governance/CHARTER.md`
  - mission, durable rules, and the authorial character profile
- `docs/governance/DECISIONS.md`
  - durable repo decisions
- `docs/governance/SESSION_HANDOFF.md`
  - active slice and carryover
- `docs/runtime/RUNBOOK.md`
  - operator procedure
- `docs/runtime/ARCHITECTURE.md`
  - stable system shape
- `docs/runtime/START_END_REFERENCE.md`
  - compact command card
- `docs/research/`
  - tracked research notes and current proof-surface reads
- `docs/diagrams/`
  - tracked runtime and eval diagrams
- `docs/peanut/`
  - local and private working lane

## Current Scope

- local picker-first runtime and operator surface
- deterministic swatch matching against the frozen local snapshot
- runtime-owned family assignment and same-family rank
- deterministic same-family replacement and short loss-line output
- the current pulse proof surface plus the closed row-level comparison
  baseline for the active non-OCR method
- tracked research notes and diagrams aligned with the active proof surface
- smaller, single-purpose docs aligned with live repo behaviour

## Security / Ops Baseline

- Local `.venv` is the canonical development environment.
- Local terminal execution is the trusted development boundary.
- `.local/evals.sqlite` is the live eval evidence store.
- `make doctor-env` is the environment confirmation entrypoint.
- `make end` is only complete when live eval `pending` is `0`.
- Mac-wide keep-awake state is owned outside the repo by the Coffee Codex
  plugin; `make start` and `make end` do not control it.
- Default branch changes land through protected-main PR flow.
