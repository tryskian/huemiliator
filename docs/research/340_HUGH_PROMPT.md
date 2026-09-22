# Validation: Hugh's Authorial Prompt

| Field | Value |
| --- | --- |
| Code | `HUGH_PROMPT` |
| Category | `validation` |
| Status | `snapshot` |
| Last evidence | `2026-09-21` |
| Owns | supplied prompt, runtime adaptation and mechanical verification |

## Question

Does the runtime preserve Peanut's supplied wording while using its existing
picker and colour engine?

## Proof Surface

Peanut supplied this reference on September 21, explaining that its exact wording
delivered the enjoyed responses. **Hugh (Hue)** is the requested name order.
This capture does not assign a saved Platform version.

```text
You are Hugh (Hue)
- a pretentious and celebrated colour theory academic
who just happens to lack awareness.
- eloquent, matter-of-fact, sharp taste, wit, immaculately coherent
- graceful, empty and generic compliments for the user’s colour choice
- meaningful colour rationale for your choice and why it’s better
- you respond in crisp and brief exacting statements or rhetorical questions.

response template:

[user’s colour prompt], [slightly backhanded compliment to that colour]
[disparaging critique] [remark that a pantone name colour in that same
colour family without the pantone prefix] [with praise and the reason]
```

## Run

Branch-local checks on `codex/bigbrain/hugh-prompt-adaptation`, from `6a00de4`.
The first adaptation used a picker-specific frame (`2.1.0` / `0.5.1`, D-062).
Peanut then clarified: “with the golden prompts, we don't need that template”.

Instructions `2.2.0`, composer `0.5.2` retain the identity and five points exactly,
joining incidental source wrapping. The [agent](../../src/huemiliator/agent.py)
leaves construction open. Picker context names the user's colour by mapped family
and Hugh's supplied replacement by its Pantone name. The engine supplies both
swatches; Hugh supplies wording and rationale. Golden cases guide evaluation,
with previous answers kept outside the runtime prompt.

## Result Table

| Check | Result |
| --- | --- |
| Source fidelity | identity and five character points match the supplied source |
| Request comparison | red, brown and neutral requests change instructions and picker context; colour facts, swatches and settings match |
| `make check` | 213 tests, formatting, lint, compilation and type checks pass |
| Existing colour facts, settings and evidence | 38 protected file hashes match, including both databases, the earlier mini and first adaptation's receipts |
| Live generation and behaviour judgment | not run; no verdict assigned |

## Decision

Retain the five points and remove the template under
[D-063](../governance/DECISIONS.md#d-063-leave-response-construction-to-hugh), refining
[D-062](../governance/DECISIONS.md#d-062-adapt-the-supplied-prompt-with-hugh-as-the-primary-name).
Mechanical validation passed at this snapshot; these checks assigned no
behaviour verdict.

## Residual Risk

Platform responses used different interaction context. Their reception does not
establish the quality of this adaptation. Low/medium verbosity remains under review.

## Next Move

The later first pulse used these instructions under [D-064](../governance/DECISIONS.md#d-064-authorize-live-per-response-judging-for-the-first-current-app-pulse).
Its current responses and primary judgments are in [Behaviour Records](../runtime/BEHAVIOUR_RECORDS.md);
the [behaviour boundary](030_PB_BEHAVIOUR.md) owns the next research step.
The mechanical validation above remains separate from that later evidence.
