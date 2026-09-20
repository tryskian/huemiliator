# Response Construction Case

| Field | Value |
| --- | --- |
| Code | `RESPONSE_CONSTRUCTION` |
| Category | `case` |
| Status | prior observed failure; D-054 construction alignment implemented; fresh mini mechanical-only; behaviour unproven |
| Prior evidence | `2026-09-19 America/Toronto`; three cases, not a 15-minute pulse |
| Prior setup | Luna / medium; instructions `1.2.0`; composer and bank `0.4.0` |
| Unit | each visible response with supplied facts and context |
| Current alignment | instructions `1.3.0`; bank `0.5.0`; composer `0.4.0`; 106 entries and 14 connector senses |
| Fresh receipt | [cue mini](../../.local/behaviour-mini-evals/20260920T012801Z-cues/README.md): red/green mechanical exit `2`, brown exit `0`; behaviour judgments pending |

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

## D-054 Small Construction Alignment

Following the user's “start small, following probsie's method” direction,
[D-054](../governance/DECISIONS.md#d-054-start-with-language-cues-and-model-owned-sentences)
records the primary's bounded implementation: the local bank, one model
generation and composer `0.4.0` remain; 17 full verdict clauses become short
cues under the same IDs; connector attachment is clarified; and the five
directions align to D-046. Instructions are `1.3.0` and the bank `0.5.0`.
Behaviour remains unproven and pulse staging is unchanged.

Three fresh samples of the same inputs are preserved in the linked receipt.
Peanut judges first; assistant judgments follow with separate attribution.
The earlier failures remain unchanged. Directions and bank changed together,
so this comparison cannot isolate either change's effect.
