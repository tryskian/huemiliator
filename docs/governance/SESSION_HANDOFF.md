# Session Handoff

Last updated: 2026-09-20

## Start Here

Run `make start` for the mechanical snapshot; its titles/dates are a summary.
Read [README](../../README.md), [CHARTER](CHARTER.md),
[DECISIONS](DECISIONS.md), [ARCHITECTURE](../runtime/ARCHITECTURE.md),
[RUNBOOK](../runtime/RUNBOOK.md) and this handoff directly; read the private
handoff if present. Report state, risks, next scope, workspace/host and branch.

## Current State

[Runtime](../runtime/COMPOSITION.md) remains the bank-free **adapted v10**:
composer `0.5.0`, instructions `2.0.0`, five positive directions and model-owned
wording. The engine supplies deterministic same-family, next-rank,
non-wrapping replacement and both swatches.

**Platform v15 is the selected research reference.** Our intended settings are
`gpt-5.6-luna` / `medium`, explicit low verbosity and Top P `0.98`.
Peanut's settings record governs despite the UI/log discrepancy; preserve
requested settings separately from returned metadata. The application sends
`store=false` and omits reasoning summary; the source experiment enabled storage
and requested `auto` summary. Source/settings record:
`docs/peanut/research/2026-09-20-golden-smoke-audit/V15_REFERENCE.md`.

The [verified archive](../research/330_EVAL_ARCHIVE.md) left both live eval
stores empty. Archived colour rows `20163..20166` retain four Peanut **FAILs**;
behaviour rows `1..3` retain both evaluators' FAILs; `4..6` remain unjudged.
Mechanical integration and historical colour anchors establish no wording verdict.

## Proposed Next Slice

The smoke audit is complete; implementation is unstarted. Review:
`docs/peanut/research/2026-09-20-golden-smoke-audit/REVIEW.md`.

The proposal is a bounded direct-v15 runner: six independent, fresh,
non-streaming cases (chartreuse, pink, snow, lavender, coral, olive), explicit
settings, and one immutable JSON receipt per attempt, including failures before
an answer. Keep original text and assign no automatic behaviour verdict.
The source export's six answered turns were conversational, not independent tests.

Before implementation/live work, settle case purposes and SDK compatibility
for recorded reasoning mode. The cases probe wording without establishing
colour-boundary coverage. SQLite/notebook adaptation is later separate work;
vector retrieval and Platform capture also remain proposals:
`docs/peanut/research/2026-09-20-vector-store-report/README.md`.

## Method and Continuity

The primary's 15-minute behaviour pulses remain staged. Peanut judges first,
then the same primary records a separate attributed `PASS` or `FAIL` with a
short reason under [D-052](DECISIONS.md#d-052-judge-the-first-behaviour-rounds-together).
Shared-phase duration and transition to independent judgment remain open.
Before timed activation, align cases, observation unit, clock/judgment timing,
in-flight handling, aggregation and completion. Carry
[“your pink”](../research/240_YOUR_PINK.md) as context; judge whole responses.

Peanut owns scope, meaning, acceptance and go/no-go. The primary owns operation,
canonical evidence, source preservation, review and Git/PR flow.

### Documentation Task

**Huey documentation**, `01a0bb88-752b-7762-88f7-8ad5c23a3ac9`, remains the
continuing lead. Bounded briefs name sources, versions, evidence and owned files;
the primary reviews and integrates under the
[collaboration contract](../diagrams/COLLABORATION.md).
Private source-continuity context:
`docs/peanut/research/2026-09-20-transcript-context/README.md`.
Today's findings and open questions:
`docs/peanut/research/2026-09-20-session-findings.md`.

## Closeout

Follow [RUNBOOK](../runtime/RUNBOOK.md): recheck live evidence, then `make end` on clean,
synced `main` with pending eval count zero.
