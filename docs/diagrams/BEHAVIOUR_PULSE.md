# Staged Behaviour Pulse

| Field | Value |
| --- | --- |
| Status | `staged` |
| Direction recorded | `2026-09-18`; shared judgment `2026-09-19`; bank-free correction `2026-09-20` |
| Owns | responsibilities and information flow for the next behaviour eval method |
| Boundary note | [Pre-Beta: 15-Minute Behaviour Pulses](../research/030_PB_BEHAVIOUR.md) |

```mermaid
flowchart LR
  H["Peanut / human lead<br/>method and scope"]
  A["Primary assistant<br/>operate, preserve and integrate"]
  C["Deterministic colour engine<br/>facts"]
  X["Hugh (Hue)<br/>free-text composition"]
  J["Initial rounds<br/>Peanut + assistant judge together"]
  I["Later path<br/>assistant judges after alignment"]
  F["Attributed judgments<br/>responses, facts and reasons"]

  H -->|"scope + lens"| A
  A -->|"input"| C
  A -->|"authorial points + context"| X
  C -->|"colour facts"| X
  X -->|"response + setup"| A
  A -->|"preserved response"| J
  H --> J
  A -.->|"after alignment"| I
  J --> F
  I --> F
```

The flow separates assistant operation from judgment ownership. It does not
choose whether joint judgment occurs during or after the 15-minute clock; both
clock boundaries and judgment timing remain staging choices. Initial rounds are
judged by Peanut and the primary assistant together. Independent assistant
judgment is a later path only after alignment.

## Reading the Diagram

| Surface | Responsibility |
| --- | --- |
| Peanut / human lead | defines method and scope, aligns staging choices and acceptance |
| Primary assistant | operates pulse, preserves canonical evidence and integrates the result |
| Colour engine | supplies deterministic matching, family, rank and replacement facts |
| Huey | develops wording and relationships from character directions, facts and context |
| Initial joint judgment | Peanut and the assistant develop the assistant's reading of signal and nuance |
| Pulse evidence | preserves actual setup, responses, attributed judgments and reasons |

The [composer](../runtime/COMPOSITION.md) adapts the [supplied prompt](../research/340_HUGH_PROMPT.md)
under D-063. The model owns wording and sentence construction; the deterministic
[pipeline](PIPELINE.md) supplies colour facts and the replacement. The primary
operates the pulse, Peanut and the assistant share initial judgment, and any later
independent judgment remains conditional.

## Implemented Starting Point

The bank-free composer uses five authorial points and picker context, Luna / medium
reasoning, low verbosity and Top P `0.98`. Its v2 local records preserve setup and actual
free-text output, including mechanical failures. The [integration record](../research/320_BANK_FREE_ALIGNMENT.md)
owns validation. Timing, observation unit, pulse-wide verdict rule and the length
of shared judgment remain open in the [boundary note](../research/030_PB_BEHAVIOUR.md).

The [behaviour database and notebook](../runtime/BEHAVIOUR_RECORDS.md) now
store original records and attributed judgment history. This supplies a review
surface while the timed pulse protocol remains staged.
