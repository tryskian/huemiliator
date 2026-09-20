# Response Construction Case

| Field | Value |
| --- | --- |
| Code | `RESPONSE_CONSTRUCTION` |
| Category | `case` |
| Status | observed failure; historical construction study; no method adopted |
| Evidence | `2026-09-19 America/Toronto`; three current-setup cases, not a 15-minute pulse |
| Setup | Luna / medium; instructions `1.2.0`; composer and bank `0.4.0` |
| Unit | each visible response with supplied facts and context |

## Source Packet

The [mini receipt](../../.local/behaviour-mini-evals/20260920T010230Z-316de2/README.md),
[manifest](../../.local/behaviour-mini-evals/20260920T010230Z-316de2/manifest.json),
and [judgments](../../.local/behaviour-mini-evals/20260920T010230Z-316de2/judgments.jsonl)
preserve three records. Peanut judged the mini first, followed by
separately attributed assistant judgments; all three were `FAIL`. Their
attributions remain separate.

## Observed Failure

The red, green and brown responses all end with `is the finer choice`, and all
use `however`. Peanut flagged the repeated ending and punctuation. Assistant
interpretation: each semicolon follows a noun phrase without a finite verb, so
it does not join independent clauses.
That is a grammar diagnosis of the punctuation concern, not a claim about
Peanut's exact wording. Reported entry IDs use `verdict.finer`; the supplied
bank also contains the literal `{replacement_name} is the finer choice`.
IDs are not treated as a causal or internal trace.

## Construction Study

The [study manifest](../../.local/response-construction-study-20260919/manifest.json)
preserves snapshots. History moves from a model call
([snapshot](../../.local/response-construction-study-20260919/01-initial-agent.ts),
commit `7eb59e3`) to a fragment picker
([snapshot](../../.local/response-construction-study-20260919/02-fragment-prototype.ts),
commit `fb7b24c`) and then a node generator
([snapshot](../../.local/response-construction-study-20260919/03-node-generator.ts),
commit `421aa2c`) that selected certainty and a base, then appended optional
hinge/wobble and conclusion fragments with commas. Recovered snapshots are historical, not current main
ancestry or proof of success. Early Python main-line snapshots
([bootstrap](https://github.com/tryskian/probaboracle/blob/7bcf521e84b7b2a576618d4f74bdf479cb16204f/src/probaboracle/agent.py),
commit `7bcf521`; [shared cues](https://github.com/tryskian/probaboracle/blob/561470050bb5f6668fad7e746835d9cbf2bc4f83/src/probaboracle/agent.py)
and [config](https://github.com/tryskian/probaboracle/blob/561470050bb5f6668fad7e746835d9cbf2bc4f83/src/probaboracle/config.py),
commit `5614700`) use prompt text. Config names four cue roles: certainty
signal, indecision signal, connective or hinge, and soft conclusion. These are
prompt text for one generation, not executable stages. Probaboracle's
[decisions](https://github.com/tryskian/probaboracle/blob/af4b3dc7ec287519a27f2622b827d84039282317/docs/governance/DECISIONS.md)
D-008/D-010 reinforce shared cues and model sentence ownership; D-024 and
D-048 describe punctuation and stock-phrase failures. These are historical lessons.

## Proposed Next Alignment

Keep Hugh's approved local library. Review whole-clause verdict entries and how
connectors attach to phrases or clauses, while letting the model compose
meaningful judgment and rationale. This remains a proposal; runtime is unchanged.
