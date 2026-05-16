# Research

Last updated: 2026-05-15

Huemiliator keeps the tracked research lane small on purpose.

Tracked research notes should answer three things quickly:

- what the current proof surface is
- what the durable notes are
- what the next narrow correction is

Tracked research-note names stay descriptive and topic-first, with lowercase
kebab-case filenames.

Private scratch and raw operator notes stay in `docs/peanut/`.

## Current Research State

| Item | Current state |
| --- | --- |
| phase | `pre-beta` |
| active proof surface | closed third corrected `red` rerun at `id > 18423` |
| current totals | `1268 total / 1162 pass / 106 fail / 0 pending` |
| current question | what is the next narrow `red` correction? |
| next family lane | `red` first, `yellow` queued behind it |
| live DB rule | keep only the current proof surface in `eval_outputs` |

## Research Map

| Surface | Type | What it says now |
| --- | --- | --- |
| [Brown Context Dependence](./brown-context-dependence.md) | durable note | `brown` behaves like a contextual bucket rather than a clean spectral category |
| [Red-to-Orange Edge Drift](./red-to-orange-edge-drift.md) | active note | the next `red` cut should be a narrow warm-clay / peach edge escape |

## How To Read This Folder

```mermaid
flowchart LR
  A["closed proof surface"]
  B["tracked research note"]
  C["next narrow correction"]
  D["fresh rerun"]
  E["new proof surface"]

  A --> B --> C --> D --> E
```

- durable notes hold category-level or method-level claims that survived
  more than one rerun
- active notes hold the current research edge
- handoff and decisions carry repo truth; research notes explain what the
  signal means

## Current Signal

- the broad pink-peach and brown-wine seams are already much tighter
- the coherent muted-red local cluster should stay in `red`
- the next likely cut is a warm-clay / peach edge escape from `red` to
  `orange`
- the smaller remaining dark-to-pale jumps should wait behind that family cut

## Plans

Plans are useful, but they are not evidence.

Current planned sequence:

1. keep the closed third corrected `red` rerun as the active proof surface
2. cut the next narrow `red` correction
3. rerun `red`
4. only then decide whether the remaining dark-to-pale jumps are still family
   issues or a later rank kernel
