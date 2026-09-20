# Bank-Free Character Foundation

| Field | Value |
| --- | --- |
| Status | foundation accepted by Peanut; repo alignment and punctuation open |
| Source | Peanut's API-platform excerpts and browser inspection, September 20, 2026 |
| Decision | [D-056](../governance/DECISIONS.md#d-056-establish-a-bank-free-character-foundation) |

## Direction and Evidence

Peanut corrected the method: “we aren't supposed to use word banks”. Hugh
composes from character direction and grounded colour context. The following
generated outputs are research observations, separate from the generation
prompt. Foundation acceptance applies to the character direction; the repo
still implements the earlier bank-based composer.

```text
Red, a predictably forceful choice—Pantone 7621 C perfects its crimson lineage with sovereign warmth, disciplined drama, and the rare dignity of knowing when not to shout.
```

Peanut: “it's not exactly right as it has the pantone value but it's a good one!”
The visible replacement should use its shade name under D-045; the catalogue code is
the identified miss.

```text
Orange, a flamboyantly competent choice—Tangerine elevates its citrus lineage
with incandescent optimism, cultivated exuberance, and the confidence
of a sunset that has overdressed.
```

Peanut accepted these as “good enough to establish huey's foundation”, while
identifying the em-dash issue. This supplies a character foundation, without a
formal row PASS, pulse result or independently verified colour rationale.

## Inspected Platform Setup

Chrome exposed the orange log's developer prompt and prior responses. The
published `huey-v2` editor advanced from `v1` to `v2` during inspection, with the
same visible character text. Exact prompt transcriptions and source identifiers
are in the [local capture](../../.local/bank-free-foundation-20260920/browser-source.json).
This is a visible-source record, not a raw API request export.

| Setting | Original orange log | Published editor |
| --- | --- | --- |
| Model / effort / verbosity | `gpt-5.6-luna` / `medium` / `low` | same |
| Reasoning summary | `detailed` | `auto` |
| Top P | `0.98` | not displayed |
| Input context | `orange`, with earlier colour responses displayed in linked history | later `v2` observation had an empty conversation |

Both prompts use Peanut's five character directions, followed by a response
shape: acknowledge the input, offer a slightly judgmental compliment, then
praise a same-family Pantone colour by title with an extravagant rationale.
The original template includes “use a pretentious flourishy comparative turn”
and the literal fragment “without and”; the published version replaces that
turn instruction with “then praise” and removes the stray “without”. Neither
prompt supplies a vocabulary bank. The response shape is authorial direction.

Earlier replies repeat the em-dash construction. Context reinforcement is a
hypothesis to test, not a causal finding. The displayed reasoning summaries
supply no proof of internal reasoning. The platform prompt asks the model to
choose the better shade; the repo currently supplies a deterministic replacement.
That difference needs alignment before claiming equivalent setups.

## Next Experiment

Untested assistant proposals: compare fresh-context output with the observed
conversation setup, then isolate any punctuation instruction as a separate
change. Candidate direction: “Use conjunctions to connect clauses and full stops
to separate complete statements.” Fold any agreed punctuation direction into
the compact voice instructions and inspect raw responses. Rhetorical questions
remain available under D-046. No punctuation change or new generation was run.

The [staged diagram](../diagrams/BEHAVIOUR_PULSE.md) shows the target flow.
The repo still implements composer `0.4.0`, instructions `1.3.0` and bank `0.5.1`.
Earlier banks, response bytes and verdicts remain historical evidence; planned
bank simplification is superseded by this direction.
