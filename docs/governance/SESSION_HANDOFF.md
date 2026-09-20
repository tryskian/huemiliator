# Session Handoff

Last updated: 2026-09-20

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
| Direction | [D-060](DECISIONS.md#d-060-adapt-the-v10-foundation-to-hughs-colour-flow): adapt the [v10 benchmark](../research/470_V10_BENCHMARK.md) to Hugh's existing colour flow. Its exact template stays source evidence; v8/v9 remain comparisons. |
| Character | Hue (Hugh); five adapted positive directions, crisp delivery, model-owned wording and reasoning. D-057 leaves punctuation to Hugh's voice. |
| Runtime | bank-free composer `0.5.0`, instructions `2.0.0`; `gpt-5.6-luna` / `medium`, explicit low verbosity / Top P `0.98`. Deterministic family and shade selection supply the two swatches. |
| Evidence | v10 benchmark: green → yellow → red conversation; all logs use medium reasoning / low verbosity. Earlier [mini calibration](../research/220_RESPONSE_CONSTRUCTION.md) remains historical; outputs `4..6` retain pending judgments. |
| Carried wording correction | `.local/evals.sqlite` rows `20163..20166` are now four Peanut **FAILs**: “the responses are too basic.” Their historical colour-pulse anchors do not establish wording quality; [record](../research/230_CARRIED_WORDING.md) |

Supporting detail: [behaviour boundary](../research/030_PB_BEHAVIOUR.md), [historical
local language](../research/450_LOCAL_LANGUAGE.md), [pulse diagram](../diagrams/BEHAVIOUR_PULSE.md),
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
in-flight handling, pulse-wide aggregation and completion.
Existing `compose` supplies inspection records, including returned failures;
mechanical checks are separate from behaviour verdicts. The
[behaviour database and notebook](../runtime/BEHAVIOUR_RECORDS.md) preserve
original outputs and attributed judgment history under D-055. Pulse membership,
timing and aggregation remain open.

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

Complete integration validation of the bank-free composer and v1/v2 record
compatibility, then review fresh responses together when Peanut starts that work.
The [benchmark record](../research/470_V10_BENCHMARK.md) preserves the exact source;
[runtime directions](../../src/huemiliator/agent.py) own its adaptation. Existing
outputs `4..6` remain unjudged historical evidence; Peanut judges first if that
review resumes. Align the pulse brief before timed evaluation.

Follow [RUNBOOK](../runtime/RUNBOOK.md) for Git and closeout: `make end` on clean,
synced `main`, pending eval count zero.
