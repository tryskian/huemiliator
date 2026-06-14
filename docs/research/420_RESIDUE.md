# Post-Sweep Residue Map

Date: `2026-06-06`

## What This Asks

After every runtime family lane has a parked `Beta 1.0` read, what should the
next eval scope be?

## Status

Closed.

This map was triaged, promoted into
[Warm Edge Residue Audit](./430_WARM_EDGE_AUDIT.md), and closed by that audit.

Do not launch another family-lane continuation by default. The row-order pulse
stack now says the useful next move is a residue-scope choice.

The family lanes are parked, and the counted-seam history now stays as a source
map for future promoted claims rather than an active backlog.

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
| warm-edge residue audit | `orange`, `yellow`, and warm `neutral` residue carried the largest seam counts | closed by explicit-input audit |
| cool-neutral follow-up | the cool-edge split cleared, but its source failure was the sharpest neutral collapse | only reopen if a new cool-edge claim appears |
| chart-only closeout | all family lanes are parked and the residue map is closed | no new runtime evidence needed |

## Recommendation

Use the warm-edge residue audit as the closed proof surface if the next task
needs the residue read.

The warm-edge residue audit is now closed. The first `orange` yellow-gold
boundary pulse passed at `20121..20128`, and the second `yellow` green / olive
shoulder pulse passed at `20129..20139`. The third `orange` pale straw / buff /
blush shoulder pulse passed at `20140..20145`. The fourth `yellow` residual
chartreuse shoulder pulse passed at `20146..20150`, and the fifth warm-neutral
peach / pearl residue pulse passed at `20151..20153`.

The chart-only closeout is now the current state: `Beta 1.0` has a complete
family-lane sweep with row-order chart truth, a parked `neutral` lane, and no
pending eval rows.
