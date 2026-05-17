# Pre-Beta 1.0: Fail-Pressure Pulse

Date: `2026-05-16`

## What This Pre-Beta Asks

Should Huemiliator treat a bounded family run as the real binary unit once seam
density matters more than single-row replay?

## Status

Maybe, and the current corrected `red` proof surface is strong enough to make
the question worth staging explicitly.

The closed third corrected `red` rerun proved that row-level family correction
can narrow a real seam without widening the runtime contract. This pre-beta
note asks whether the next method step should move the binary judgment up one
level:

- the pulse becomes the binary unit
- the rows become evidence inside the pulse

## Eval Shape

This is not `Beta 1.0` yet.

It is the staging contract for a possible `1.0` promotion.

The proposed pulse shape for Huemiliator is:

- keep the colour runtime local and deterministic
- keep the active family lane narrow
- start small:
  - around `15` rows
- row evidence is judged first as:
  - `anchor`
  - `counted seam`
  - `excluded noise`
- the pulse verdict is binary:
  - `PASS`
  - `FAIL`

Counted pulse rules:

- more anchors than counted seams: `PASS`
- more counted seams than anchors: `FAIL`
- tie: `FAIL`

Exclusion rules:

- raw pulse size stays visible
- counted pulse size stays visible
- every excluded row needs a narrow reason
- excluded rows stay reviewable after the pulse

## Current Huemiliator Read

| Surface | Result |
| --- | --- |
| staged lane | `pre-Beta 1.0` |
| active proof surface | closed third corrected `red` rerun at `id > 18423` |
| current blocker | repair sampler truth and true source-order targeting |
| current evidence store | `.local/evals.sqlite` still holds row evidence |
| first Beta 1.0 target | `red` |

## What This Would Change

If this graduates into `Beta 1.0`, Huemiliator would change the unit of
judgment for bounded family runs:

- current closed comparison surface:
  - row-level `PASS / FAIL`
  - family-lane rerun proof surface
- `Beta 1.0` candidate:
  - row-level evidence labeling inside the pulse
  - pulse-level `PASS / FAIL`

That would make family-level seam shape harder to fake:

- one lucky row could not make the whole run look healthy
- seam density would matter more than isolated wins
- exclusion review would become part of pulse hygiene

## What Stays The Same

- the picker runtime stays local and deterministic
- the frozen `margaret2` snapshot stays the primary colour reference
- runtime still owns swatch matching, family assignment, rank, and one-up
- the active technical seam is still the warm-clay / peach shoulder inside
  `red`

## What It Still Needs

- repair scoped sampler truth
- repair true source-order targeting
- repair the surfaced `contract` command
- a tight evidence taxonomy for:
  - `anchor`
  - `counted seam`
  - `excluded noise`
- one first promoted pulse target:
  - `red`

## What Would Promote It

This becomes `Beta 1.0` only when Huemiliator starts the first real pulse run.

Promotion boundary:

1. pulse contract is accepted as the next eval unit
2. the first bounded `red` pulse is launched
3. the research index flips from staged `pre-Beta 1.0` to active `Beta 1.0`
4. pulse evidence, not just hypothesis text, becomes the current method
