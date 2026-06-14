# Red Orange Edge Drift Audit

Date: `2026-05-16`

## What This Note Asked

Does the active branch still support the same narrow `red` claim, and is the
repo ready to log fresh `red` evidence?

This audit is now closed evidence for the representative red-orange case.

## Short Answer

Yes on the claim. No on the first real Beta 1.0 pulse.

The source proof surface still supported the same warm-clay / peach edge read,
but the branch surfaced sampler-truth and source-order blockers that should be
repaired before fresh `red` rows were logged.

Those blockers were repaired before the first `Beta 1.0` pulse, and the later
bounded red pulses passed.

## Audit Snapshot

| Surface | Result |
| --- | --- |
| source proof surface | closed third corrected `red` rerun |
| source totals | `1268 total / 1162 pass / 106 fail / 0 pending` |
| source ids | `18424..19691` |
| branch finding | narrow `red -> orange` edge still looked right |
| promotion gate | repair scoped sampler truth and true source-order targeting first |
| later bounded read | red pulses at `19692..19706` and `19707..19721` passed |

## Confirmed Signal

- the source proof surface still matched the tracked red read
- the dominant repeated fail seam is still the warm-clay / peach drift
- the coherent muted-red local cluster still looks healthy enough to keep in
  `red`
- the next red family cut was still the same narrow target

## Repeated Fail Drift

| Seam | Repeated examples |
| --- | --- |
| warm clay / peach edge | `Auburn -> Tawny orange`, `Desert rose -> Burnt brick`, `Garnet rose -> Desert rose`, `Holly berry -> Dusted clay`, `Rio red -> Ginger`, `Slate rose -> Crabapple`, `Terra cotta -> Burnt henna` |

## Rerun Blockers

- scoped `red` sampling can emit `orange` rows after the warm-clay edge
  override
- `start_source_order` stops meaning real snapshot source order once family
  filtering is applied
- the surfaced `contract` command is still a status fallback rather than a
  truthful dispatch path

## What It Points To

1. keep the closed third corrected `red` rerun as the source proof surface
2. repair sampler truth and source-order targeting
3. repair the dead `contract` command while the surfaced truth gaps are open
4. only then launch the first bounded `red` Beta 1.0 pulse
5. only then judge whether the smaller dark-to-pale jumps are still real signal

## Branch Repair Update

Date: `2026-05-17`

- scoped `red` sampling now follows the same effective runtime routing as the
  live ladder, so named warm-clay edge swatches no longer leak into `red`
  scoped rows
- `start_source_order` now applies before scope filtering and points at the
  real snapshot source-order surface again
- the surfaced `contract` command now dispatches truthfully instead of falling
  through to `status`
- validation is green on the repair branch: `make check`

## Beta 1.0 Launch Update

Date: `2026-05-21`

- the first bounded `red` Beta 1.0 pulse launched at `19692..19706`
- the closed third corrected `red` rerun was quarantined locally before the
  new pulse was seeded
- the first pulse passed at:
  - `11 anchors`
  - `4 counted seams`
  - `0 excluded`
- the warm-clay / peach drift is still visible, but it no longer outweighs
  the lane around it in the first bounded pulse

## Deeper Cluster Update

Date: `2026-05-21`

- the next bounded `red` pulse targeted the older repeated fail cluster at
  source-order `850`
- the latest red proof surface is now `19707..19721`
- that deeper cluster also passed at:
  - `10 anchors`
  - `5 counted seams`
  - `0 excluded`
- the older repeated fail cluster is still a real drift, but it no longer
  dominates the lane under bounded pulse pressure

## Current Read

The red-orange edge is closed as an audit gate and retained as a representative
case. Later red work is optional follow-up, not the next required boundary.
