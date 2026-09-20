# Session Handoff

Last updated: 2026-09-19

## Start Here

Run `make start` for the mechanical snapshot; its titles/dates are a summary.
Read [README](../../README.md), [CHARTER](CHARTER.md),
[DECISIONS](DECISIONS.md), [ARCHITECTURE](../runtime/ARCHITECTURE.md),
[RUNBOOK](../runtime/RUNBOOK.md) and this handoff directly; read the private
handoff if present. Report state, risks, next scope, workspace/host and branch.

## Current Stage and Setup

Behaviour evaluation is staged on stable deterministic colour facts. Hugh gets
about five positive directions and room to reason.

| Surface | Current state |
| --- | --- |
| Character | Hue (Hugh); [D-046](DECISIONS.md#d-046-record-hughs-agreed-academic-configuration) is agreed, broader instruction/library alignment pending |
| Runtime | `gpt-5.6-luna` / `medium`; bank `0.4.0`; composer `0.4.0`; instructions `1.2.0` |
| Evidence | [mini calibration](../research/220_RESPONSE_CONSTRUCTION.md): Peanut judged all three FAIL for repeated endings and flagged punctuation; first aligned pulse pending |

Supporting detail: [behaviour boundary](../research/030_PB_BEHAVIOUR.md), [local
language](../research/450_LOCAL_LANGUAGE.md), [pulse diagram](../diagrams/BEHAVIOUR_PULSE.md),
[closed colour baseline](../research/020_B10.md) and [pipeline](../diagrams/PIPELINE.md).
Read when working the behaviour kernel.

## Method and Open Choices

The primary assistant operates 15-minute pulses and preserves canonical evidence.
Peanut and the same primary assistant judge initial rounds together under
[D-052](DECISIONS.md#d-052-judge-the-first-behaviour-rounds-together) to learn
signal and nuance. Judgments are `PASS` or
`FAIL` with an attributed, short reason. Shared-phase duration and transition
to later independent assistant judgment remain open.

Before activation, align cases, observation unit, clock/judgment timing,
in-flight handling, attributed records, pulse-wide aggregation and completion.
Existing `compose` supplies inspection records, including returned failures;
mechanical checks are separate from behaviour verdicts. Additional automation
and storage choices remain proposals.

## Ownership and Continuity

- Peanut owns scope, meaning, acceptance and go/no-go.
- The primary owns operation, canonical `.local` evidence, source preservation,
  review and Git/PR flow.

### Documentation Task

**Huey documentation**, `01a0bb88-752b-7762-88f7-8ad5c23a3ac9`, is the continuing
lead with optional internal helpers. Briefs name the question, sources/versions,
evidence and owned files. The lead returns concise, checked documentation;
the primary reviews meaning and integrates. The [collaboration contract](../diagrams/COLLABORATION.md)
keeps pulse operation and canonical evidence with the primary.

## Next Step and Closeout

Review early response construction against the mini failures before aligning
instructions/library with D-046. Version `1.2.0` retains earlier guidance.
Agree a short pulse brief before the first shared run.
Follow [RUNBOOK](../runtime/RUNBOOK.md) for Git and closeout: `make end` on clean,
synced `main`, pending eval count zero.
