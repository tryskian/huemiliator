<!-- @format -->

# Hypothesis Template

Use this for staged correction or method claims that are not yet active
boundaries and not yet live evidence lanes.

## Metadata

| Field | Value |
| --- | --- |
| Code | `NNN_HYPOTHESIS` |
| Category | `hypothesis` |
| Status | `staged`, `testing`, `supported`, `unsupported`, or `retired` |
| Last evidence | `YYYY-MM-DD` |
| Owns | one sentence naming the correction or method claim this doc is testing |

## Headline Shape

- `Hypothesis: Name`
- or `Method Hypothesis: Name`
- or `Family Hypothesis: Name`
- or `Correction Hypothesis: Name`

## Section Order

1. metadata table
2. `Question`
3. `Current Claim`
4. `Source Shape`
5. `Diagram`
6. `What Would Support It`
7. `What Would Break It`
8. `Why It Matters`
9. `Next Move`

## Required Hypothesis Moves

- state the exact claim in one sentence
- state the judged object, family lane, and verdict unit explicitly
- name the bounded source shape needed to test it
- define what counts as support and what counts as failure
- state whether the hypothesis should promote, narrow, or retire if confirmed

## Default Source Table

| Claim | Source shape | Judged object | Support signal | Break signal |
| --- | --- | --- | --- | --- |
| example correction | bounded pulse or split pulse | row, pulse, or correction | compact recovery read | compact drift read |

## Default Diagram Shape

```mermaid
flowchart TD
  A["Staged claim"]
  B["Bounded source shape"]
  C["Judged object"]
  D{"Observed signal"}
  E["Support"]
  F["Break"]
  G["Next boundary move"]

  A --> B --> C --> D
  D --> E --> G
  D --> F --> G
```

## Hypothesis Questions To Answer

- what exact claim is being tested?
- what bounded source would test it fairly?
- what family lane or proof surface supplies the evidence?
- what result would count as support?
- what result would count as a break?
- what should happen if the claim holds?

## Style Rules

- lead with the metadata table
- keep the claim tighter than the plan
- use tables for support and break conditions
- avoid turning the doc into a backlog dump
- keep candidate corrections separate from active runtime changes
- keep `Next Move` to the immediate test surface
