# Session Handoff

Last updated: 2026-09-19

## Start Here

Run `make start` for the mechanical snapshot, then read `README.md`, `CHARTER`,
`DECISIONS`, `ARCHITECTURE`, `RUNBOOK` and this handoff directly. The startup
reader emits titles/dates; its output does not supply the documents' contents.
Read the private peanut handoff if present. Report current state, risks, next
scope, workspace/host and active branch before implementation.

## Current Staging

| Surface | Current state |
| --- | --- |
| Research | [15-minute behaviour pulses](../research/030_PB_BEHAVIOUR.md), staged; the assistant runs pulses and supplies verdicts |
| Character | [Hue (Hugh)](CHARTER.md#character-profile); D-046's agreed five-point configuration is recorded, with broader runtime/library alignment pending |
| Language | [Bank](../runtime/LANGUAGE_BANK.md) `0.4.0`: 106 entries, including 15 authorial references and 91 assistant candidates; 14 connector senses |
| Composer | [Composition](../runtime/COMPOSITION.md) `0.4.0`, instruction version `1.2.0`, configured `gpt-5.6-luna` with `medium` reasoning |
| Presentation | Actual selected swatch labelled by family; Hugh's replacement labelled by its supplied Pantone name; hexes remain rendering/evidence data |
| Observations | [Smoke records and authorial FAILs](../research/450_LOCAL_LANGUAGE.md#behaviour-evidence-to-establish) retain their individual setups and verdict owners |
| Behaviour evidence | First aligned pulse pending; timing, observation unit and pulse-wide verdict aggregation still require alignment |

The library makes adjective references and meaningful connective relations
available while the model constructs the sentence. Rhetorical questions can
carry implied claims in relationship annotations. Mechanical checks establish
interface compliance; behavioural coherence and character fit await evaluation.
The [local-language hypothesis](../research/450_LOCAL_LANGUAGE.md) owns the
research interpretation and exact authorial history.

## Active Kernel

Narrow documentation workflow trial under
[D-050](DECISIONS.md#d-050-use-a-continuing-documentation-task). Correct and
condense the assigned documents using the completed audit. Runtime, language
resources, model settings and original evidence retain their existing state.

### Documentation Task

**Huey documentation**, `01a0bb88-752b-7762-88f7-8ad5c23a3ac9`, is the continuing
lead in the same local checkout. It retains documentation context and can use
bounded internal helpers. The primary owns final review, integration and Git.

| Owner | This assignment |
| --- | --- |
| Documentation lead | Research README and `450_LOCAL_LANGUAGE`; runtime `LANGUAGE_BANK`, `RUNBOOK`, `START_END_REFERENCE`; diagrams `BEHAVIOUR_PULSE`, `PIPELINE`; template `legend` |
| Primary engineer | Charter, decision, handoff and collaboration diagram; preservation checks and integration |

The eight-file lead assignment and internal source review are complete; primary
review restored chart context, smoke-run chronology and accurate diagram flow.
Validation and Git outcomes are recorded in the private trial receipt. Pre-edit copies and hashes are in
`.local/documentation-workflow-20260919/`; the manifest covers all tracked
sources and 35 original evidence files. Private trial notes belong in
`docs/peanut/research/2026-09-19-documentation-workflow/`. Source captures remain
in `docs/peanut/transcripts/`. The existing audit is
`docs/peanut/research/330_DOCS_AUDIT.md`.

Longer historical consolidation, remaining decision-log cleanup and broad
template simplification stay in the audit queue. The current trial does not
claim to complete that larger backlog.

## Carried Colour Baseline

The deterministic picker, frozen swatch snapshot, family/rank selection and
same-family replacement remain the factual foundation. Neutral replacement
retains its undertone constraint; the carried `one-up` command uses fixed lines.
The [pipeline](../diagrams/PIPELINE.md) owns that implementation map.

[Beta 1.0](../research/020_B10.md) is closed. The latest colour-boundary proof is
`20163..20166`: four anchors, zero counted seams and zero exclusions. Its owner is
[COLOUR_BOUNDARY_AUDIT](../research/440_COLOUR_BOUNDARY_AUDIT.md); earlier warm-edge
proof belongs to [WARM_EDGE_AUDIT](../research/430_WARM_EDGE_AUDIT.md). Beta 1.0
retains the complete pulse ledger and closed row-level comparison.
The [pulse chart](../research/eval-pulse-stack.svg) retains each pulse's row
range and anchor/seam counts.

No colour pulse is queued. A fresh colour-audit group requires promoted evidence;
`warm` remains an audit cohort. Superseded rows stay quarantined locally, and
the live colour DB retains its latest proof surface. These are carried findings,
not a fresh live-DB inspection during the documentation trial.

## Next Slice

1. Resume behaviour staging from [PB_BEHAVIOUR](../research/030_PB_BEHAVIOUR.md),
   [LOCAL_LANGUAGE](../research/450_LOCAL_LANGUAGE.md) and the
   [staged pulse diagram](../diagrams/BEHAVIOUR_PULSE.md).
2. Align the next bounded runtime/library change with D-046; instruction version
   `1.2.0` still carries earlier guidance. Inspect the bank and composer records
   as evidence for that comparison.
3. Align pulse timing, observation unit and the pulse-wide verdict rule before
   the first behaviour run. Its completed evidence will support method activation.

## Operating References

| Need | Owner |
| --- | --- |
| Concise source-faithful documentation, maintained as findings emerge | [Charter](CHARTER.md#documentation-governance), D-049/D-050 and [research templates](../runtime/templates/README.md) |
| Delegation, source capture and two review steps | [Collaboration](../diagrams/COLLABORATION.md) |
| Commands, workspace procedure and protected-main flow | [Runbook](../runtime/RUNBOOK.md) and [command card](../runtime/START_END_REFERENCE.md) |
| Day close | `make end` on clean synced `main`, with pending eval count zero; branch preflight is distinct |
| Mac-wide keep-awake | External Coffee plugin, managed independently of repository lifecycle |

Keep one active scope, coordinate file ownership, and preserve local evidence
and private notes in their existing lanes. Read sources before interpretation;
record findings and diagrams together, with exact wording and attribution.
