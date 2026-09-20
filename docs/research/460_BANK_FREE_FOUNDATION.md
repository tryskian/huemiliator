# Bank-Free Character Foundation

| Field | Value |
| --- | --- |
| Status | foundation accepted by Peanut; repo alignment open; punctuation scope clarified by D-057 |
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

Peanut accepted these as “good enough to establish huey's foundation”, initially
questioning the em dash. The later clarification below resolves that concern.
This supplies a character foundation, without a
formal row PASS, pulse result or independently verified colour rationale.

## Inspected Platform Setup

Chrome exposed the orange log's developer prompt and prior responses. The
published `huey-v2` editor advanced through `v1` and `v2`, then Peanut supplied
the revised `v3`. Exact prompt transcriptions and source identifiers
are in the [local capture](../../.local/bank-free-foundation-20260920/browser-source.json).
This is a visible-source record, not a raw API request export.

| Setting | Original orange log | Published editor (`v3`) |
| --- | --- | --- |
| Model / effort / verbosity | `gpt-5.6-luna` / `medium` / `low` | same |
| Reasoning summary | `detailed` | `auto` |
| Top P | `0.98` | not displayed |
| Input context | `orange`, with earlier colour responses displayed in linked history | visible conversation: `pink`, then `purple` |

Both prompts use Peanut's five character directions, followed by a response
shape: acknowledge the input, offer a slightly judgmental compliment, then
praise a same-family Pantone colour by title with an extravagant rationale.
The original template includes “use a pretentious flourishy comparative turn”
and the literal fragment “without and”; the published version replaces that
turn instruction with “then praise” and removes the stray “without”. Neither
prompt supplies a vocabulary bank. The response shape is authorial direction.

In `v3`, Peanut changed “groundedly verbose” to “slightly verbose”; the revised
template remained. The visible pink and purple outputs use semicolons and
shade names without catalogue codes or the Pantone prefix. These are browser
observations, with no attributed verdict or causal claim about the prompt edit.

The displayed reasoning summaries supply no proof of internal reasoning.
The platform prompt asks the model to
choose the better shade; the repo currently supplies a deterministic replacement.
That difference needs alignment before claiming equivalent setups.

## Punctuation Scope

Peanut clarified: “those punctuation canaries are for when we're writing for me”.
Under [D-057](../governance/DECISIONS.md#d-057-scope-punctuation-canaries-to-peanuts-writing),
Hugh uses punctuation suited to his character, grammar and meaning. An em dash
alone supplies no failure signal. The assistant's proposed punctuation restriction
is withdrawn; earlier grammar findings and attributed verdicts retain their scope.

Peanut also supplied yellow and Mauve samples for a new `v4` experiment.
Their [local source record](../../.local/platform-v4-20260920/shared-samples.json)
preserves the exact shared outputs and prompt identifier. The yellow response
contains an em dash; Mauve uses a semicolon. Neither has an attributed verdict.
`v4` is user-reported; its prompt text/settings have not been inspected here.

## Open Alignment

The latest reported experiment is Peanut's `v4`; `v3` remains the latest
browser-inspected prompt. Capture the new setup before repo alignment.
Rhetorical questions remain available under D-046. Punctuation suppression and
the assistant's earlier context comparison are no longer queued work.

The [staged diagram](../diagrams/BEHAVIOUR_PULSE.md) shows the target flow.
The repo still implements composer `0.4.0`, instructions `1.3.0` and bank `0.5.1`.
Earlier banks, response bytes and verdicts remain historical evidence; planned
bank simplification is superseded by this direction.
