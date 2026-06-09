# Post-Sweep Residue Map

Date: `2026-06-06`

## What This Asks

After every runtime family lane has a parked `Beta 1.0` read, what should the
next eval scope be?

## Status

Triaged.

Promoted into [Warm Edge Residue Audit](./430_WARM_EDGE_AUDIT.md).

Do not launch another family-lane continuation by default. The row-order pulse
stack now says the useful next move is a residue-scope choice.

The family lanes are parked, but the counted-seam history still shows where
the next method could focus if the repo wants another eval boundary.

## Residue Chart

![Counted seams by family](./eval-residue-family-bars.svg)

The chart counts rows labelled `counted_seam` across the row-order `Beta 1.0`
pulse stack. It is not a live failure total. It is a map of where the method
found pressure before each lane parked or corrected.

## Residue Table

| Family | Counted seams | Current read |
| --- | ---: | --- |
| `orange` | `23` | largest historical pressure; corrected and parked after a clean row-order close |
| `neutral` | `22` | cool-edge collapse corrected; warm peach residue remains |
| `yellow` | `21` | green / olive pressure corrected and parked |
| `blue` | `11` | purple / aqua pressure narrowed to one residual seam and parked |
| `red` | `9` | warm-clay / peach pressure passed under bounded pulses |
| `pink` | `6` | warm-orange and wine opening drift closed cleanly |
| `green` | `0` | parked cleanly |
| `purple` | `0` | parked cleanly |
| `brown` | `0` | parked cleanly by row data despite stale archive labels |

## Scope Read

The next useful scope is not one more blind family lane. It is one of these:

| Candidate scope | Why it fits | Gate |
| --- | --- | --- |
| warm-edge residue audit | `orange`, `yellow`, and warm `neutral` residue carry the largest seam counts | define the edge groups before sampling |
| cool-neutral follow-up | the cool-edge split cleared, but its source failure was the sharpest neutral collapse | only reopen if a new cool-edge claim appears |
| chart-only closeout | all family lanes are parked and the residue map may be enough for this branch | no new runtime evidence needed |

## Recommendation

Use the warm-edge residue audit if the next task is still eval research.

The warm-edge residue audit is now active, and the first `orange` yellow-gold
boundary pulse passed at `20121..20128`.

Otherwise, stop at the chart-only closeout: `Beta 1.0` has a complete
family-lane sweep with row-order chart truth, a parked `neutral` lane, and no
pending eval rows.
