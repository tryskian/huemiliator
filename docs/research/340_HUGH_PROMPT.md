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

Instructions `2.1.0`, composer `0.5.1`, branch
`codex/bigbrain/hugh-prompt-adaptation`. The identity and five points retain their
wording; incidental source wrapping is joined. The response frame adapts two slots:

| Source slot | Runtime slot |
| --- | --- |
| user's colour prompt | mapped colour family |
| Pantone recommendation | supplied same-family replacement, using its Pantone name alone |

The [agent](../../src/huemiliator/agent.py) owns this text. The engine still supplies
both swatches and the replacement; Hugh supplies the wording and rationale.

## Result Table

| Check | Result |
| --- | --- |
| Source fidelity | identity and five character points match the supplied source |
| Request comparison | red, brown and neutral requests change only their instructions; swatches and settings match |
| `make check` | 213 tests, formatting, lint, compilation and type checks pass |
| Existing colour facts, settings and evidence | 34 protected file hashes match, including both databases and the earlier mini |
| Live generation and behaviour judgment | not run; no verdict assigned |

## Decision

Adopt the supplied wording under [D-062](../governance/DECISIONS.md#d-062-adapt-the-supplied-prompt-with-hugh-as-the-primary-name).
Mechanical validation remains separate from shared behaviour judgment.

## Residual Risk

Platform responses used different interaction context. Their reception does not
establish the quality of this adaptation. Low/medium verbosity remains under review.

## Next Move

Review responses using the adapted instructions under the Peanut-first method.
This change activates no timed pulse or settings revision.
