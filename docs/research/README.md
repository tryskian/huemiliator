# Research

Last updated: 2026-05-25

Huemiliator keeps the tracked research lane small on purpose.

Each beta is a distinct eval approach. This folder preserves the method shifts
that changed what the evidence means.

Raw run notes and scratch material stay out of the tracked research surface
until they become evidence.

Tracked research-note names use the category code contract:
`NNN_CODE.md` or `NNN_CODE-QUALIFIER.md`. Dates live inside the docs, not in
filenames.

The live file map and shared category/status vocabulary live in
[Research Legend](./000_LEGEND.md).

Private scratch and raw operator notes stay in `docs/peanut/`.

## Current Stage

| Signal | Current read |
| --- | --- |
| live research lane | `Beta 1.0` fail-pressure pulse |
| active proof surface | third bounded `neutral` continuation at `20082..20096` |
| verdict unit | pulse-level proof surface |
| comparison surface | closed third corrected `red` rerun at `id > 18423` |
| beta question | next narrow `neutral` correction after the current fail surface |

## Current Research State

| Item | Current state |
| --- | --- |
| stage | `Beta 1.0` |
| active proof surface | `neutral` continuation at `20082..20096` |
| current totals | `15 total / 4 pass / 11 fail / 0 pending` |
| current question | next `neutral` correction after the current fail surface |
| active beta note | `020_B10` |
| closed staging note | `010_PB10` |
| staged method note | `410_N3` |
| active family lane | `neutral` |
| stable prior lanes | `red` through `brown`, with `neutral` still active |
| current audit note | `310_RED_ORANGE_AUDIT` |
| comparison baseline | closed third corrected `red` rerun at `18424..19691` |
| live DB rule | keep only the current proof surface in `eval_outputs` |

## Family Range Palette

![Huemiliator family range palette](./family-range-palette.svg)

The chips sample the current classifier order from the frozen swatch snapshot.

## Research Map

| Surface | Type | What it says now |
| --- | --- | --- |
| [Research Legend](./000_LEGEND.md) | legend | file map, code ranges, filename contract, category meanings, and status language |
| [Pre-Beta 1.0 Fail-Pressure Pulse](./010_PB10.md) | staging note | the closed staging contract that led into the first live `Beta 1.0` pulse |
| [Beta 1.0 Fail-Pressure Pulse](./020_B10.md) | active beta note | two bounded `red` pulses pass, `yellow` parks cleanly after one fail-and-recovery stack, `green` parks on two clean passes, `blue` parks behind a corrected rerun, `purple` parks on two clean `15 / 0` pulses, `pink` parks behind a clean second continuation, `orange` parks after one fail surface plus recovery, `brown` parks on three clean bounded pulses, and `neutral` now breaks into lilac, mint, blue, pearl, and peach drift on its third continuation |
| [Brown Context Dependence](./120_BROWN.md) | durable note | `brown` behaves like a contextual bucket rather than a clean spectral category |
| [Red Orange Edge Drift](./210_RED_ORANGE.md) | active note | the next `red` cut is still a narrow warm-clay / peach edge escape |
| [Red Orange Edge Drift Audit](./310_RED_ORANGE_AUDIT.md) | audit note | the audit blockers are repaired and the red lane is now parked as a stable prior baseline inside `Beta 1.0` |
| [Neutral Three-Pulse Split](./410_N3.md) | staged method note | the next `neutral` read would split the nine cool-edge seams in `20082..20096` into three smaller eval pulses |

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

| Doc kind | Job |
| --- | --- |
| durable note | holds category-level or method-level claims that survived more than one rerun |
| active note | holds the current research edge |
| handoff / decision | carries repo truth while research notes explain what the signal means |

## Current Signal

![Huemiliator Beta 1.0 eval pulse stacked bars](./eval-pulse-stack.svg)

Each horizontal bar is one 15-row pulse. Lane labels use row-family truth from
the eval rows; archive labels stay annotations.

| Lane | Current read |
| --- | --- |
| `red` | parked; the coherent muted-red local cluster stays in `red` |
| `yellow` | failed once, corrected, and parked; the yellow-to-green correction and chartreuse cut are explicit |
| `green` | parked behind two clean pulses |
| `blue` | parked after the blue-drift correction; one aqua seam remains |
| `purple` | parked behind two clean pulses |
| `pink` | warm-orange and wine drift opened, then the lane closed cleanly |
| `orange` | pale straw, buff, blush, cream, straw, olive, and yellow-gold drift were exposed, then corrected |
| `brown` | parked behind three clean pulses despite the older context-dependence read |
| `neutral` | active fail surface; lilac, mint, blue, pearl, and peach pressure outweigh the remaining neutral anchors |

| Method / runtime signal | Read |
| --- | --- |
| verdict unit | fail-pressure pulse is the active `Beta 1.0` unit |
| comparison baseline | closed third corrected `red` rerun stays the row-level comparison baseline |
| scoped sampling | current sampling truth matches the runtime ladder again |
| operator surface | pulse start, label, report, and local quarantine are live |
| next boundary | smaller remaining dark-to-pale jumps wait behind the current family cut |

## Active Neutral Pressure

| Pressure group | Rows | Read |
| --- | --- | --- |
| lilac / mauve | `20082`, `20083`, `20094` | staged pulse 1 |
| blue / jade | `20085`, `20090`, `20091` | staged pulse 2 |
| mint / green | `20086`, `20087`, `20095` | staged pulse 3 |
| warm residue | `20084`, `20088` | secondary residue outside the cool-edge split |

## Plans

Plans are useful, but they are not evidence.

| Step | Move | Gate |
| ---: | --- | --- |
| 1 | keep `20082..20096` as the current active proof surface | no broader continuation until the active fail surface is handled |
| 2 | carry the parked `red`, `yellow`, `green`, `blue`, `purple`, `pink`, `orange`, and `brown` proof stacks as the comparison stack | keep `neutral` as the only active family lane |
| 3 | treat `brown` as parked behind three clean bounded pulses | do not reopen the old context-dependence read without new evidence |
| 4 | stage the next `neutral` read as three smaller eval pulses across the nine cool-edge seams | use the staged `3 x 3` split in `410_N3` |
| 5 | decide whether another broader continuation from source order `48` is useful | only after the smaller neutral read is complete |

These betas and staged notes are research architectures. They are not app
release versions, package versions, branch names, or one more sweep.

| Surface | Verdict unit | What it proves |
| --- | --- | --- |
| closed row-level `red` rerun | row-level family proof | family-correction baseline |
| `Beta 1.0` | bounded fail-pressure pulse | current live lane-by-lane verdicts |

Later method surfaces do not erase earlier ones. They narrow what each verdict
is allowed to mean.
