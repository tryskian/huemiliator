# Session Handoff

Last updated: 2026-09-21

## Start Here

Run `make start` for the mechanical snapshot; its titles/dates are a summary.
Read [README](../../README.md), [CHARTER](CHARTER.md),
[DECISIONS](DECISIONS.md), [ARCHITECTURE](../runtime/ARCHITECTURE.md),
[RUNBOOK](../runtime/RUNBOOK.md) and this handoff directly; read the private
handoff if present. Report state, risks, next scope, workspace/host and branch.

## Current State

[Runtime](../runtime/COMPOSITION.md) uses the
[September 21 authorial prompt](../research/340_HUGH_PROMPT.md): **Hugh (Hue)**,
five verbatim character points and a response frame adapted to the picker.
Composer `0.5.1`, instructions `2.1.0`. The engine supplies the family,
deterministic same-family replacement and both swatches; Hugh composes the words.

**Platform v15 remains the prior experiment reference.** Our intended settings are
`gpt-5.6-luna` / `medium`, explicit low verbosity and Top P `0.98`.
Low versus medium verbosity is under review; preserve requested settings
separately from returned metadata. The application sends
`store=false` and omits reasoning summary; the source experiment enabled storage
and requested `auto` summary. Source/settings record:
`docs/peanut/research/2026-09-20-golden-smoke-audit/V15_REFERENCE.md`.

The [verified archive](../research/330_EVAL_ARCHIVE.md) left both live eval
stores empty. Archived colour rows `20163..20166` retain four Peanut **FAILs**;
behaviour rows `1..3` retain both evaluators' FAILs; `4..6` remain unjudged.
Mechanical integration and historical colour anchors establish no wording verdict.

## Proposed Next Slice

The direct-v15 verbosity mini completed six independent requests: pink, snow and
olive at low and medium. All completed; returned verbosity matched each request.
Peanut's judgments come first and remain pending. Exact receipts and paired answers:
`docs/peanut/research/2026-09-21-verbosity-comparison/README.md`.

Those responses used the earlier v15 reference, not today's app adaptation.
The [prompt record](../research/340_HUGH_PROMPT.md) owns its source and mechanical
checks; fresh app behaviour judgment remains open. The original six-colour smoke
proposal, SQLite/notebook adaptation and vector retrieval remain separate work.

The documentation conventions audit is report-only:
`docs/peanut/research/2026-09-21-documentation-conventions/README.md`.

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
