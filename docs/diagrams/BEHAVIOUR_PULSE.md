# Staged Behaviour Pulse

| Field | Value |
| --- | --- |
| Status | `staged` |
| Direction recorded | `2026-09-18`; local library clarified `2026-09-19` |
| Owns | responsibilities and information flow for the next behaviour eval method |
| Boundary note | [Pre-Beta: 15-Minute Behaviour Pulses](../research/030_PB_BEHAVIOUR.md) |

```mermaid
sequenceDiagram
  participant L as Human lead
  participant A as Assistant evaluator
  participant C as Colour engine
  participant H as Huey
  participant B as Local language library

  L->>A: Align method, scope and staging choices
  A->>H: Compact positive directions
  loop 15-minute behaviour pulse
    A->>C: Selected colour input
    C-->>A: Fixed colour facts
    A->>H: Facts and interaction context
    H->>B: Select fitting language and relationship shapes
    B-->>H: Eligible words, phrases and sentence shapes
    H->>H: Compose claims with a supported relationship
    H-->>A: Actual response
    A->>A: Inspect, judge and preserve reasons
  end
  A-->>L: Pulse evidence and findings
  L->>A: Align the next bounded step
```

## Reading the Diagram

| Surface | Responsibility |
| --- | --- |
| Human lead | defines the method and scope, aligns staging choices, and steers the next step |
| Colour engine | supplies deterministic matching, family, rank, and replacement facts |
| Huey under evaluation | acts on the small positive instruction set with room to reason |
| Local language library | supplies wording and relationship shapes with usage conditions |
| Assistant evaluator | runs the pulse, inspects responses, assigns verdicts, and records supporting reasons |
| Pulse evidence | preserves the actual setup, observations, and judgments for discussion |

The directions and evaluator lens have distinct recipients. The final payload
is a staging choice, including which fields from the existing fact export reach
Huey. The [library draft](../research/450_LOCAL_LANGUAGE.md) describes connector
relationships and language entries; Huey's selection and composition mechanism
remains to be chosen. Clock boundaries and judgment timing are also staging
choices documented in the boundary note.

## Implemented Starting Point

The [current pipeline](PIPELINE.md) supplies colour results and fixed family
lines. `behaviour-facts` exposes those facts with response-contract metadata.
The existing SQLite records describe colour outputs and their judgments.

This diagram describes the next execution shape. Its local library, composer,
behavioural record, and pulse-wide verdict rule remain to be aligned and
implemented. The first completed pulse will establish the new evidence surface.
