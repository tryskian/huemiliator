# Beta 1.0: Fail-Pressure Pulse

Date: `2026-05-21`

## What This Beta Says

The first eighteen bounded pulses now read like this:

- two `red` passes
- one `yellow` core pass
- one targeted `yellow` fail
- one corrected targeted `yellow` pass
- one final targeted `yellow` pass clean enough to park the lane
- one opening `green` pass
- one deeper `green` continuation pass
- one opening `blue` pass with a visible shoulder
- one deeper `blue` continuation pass with the same visible shoulder
- one corrected `blue` rerun that tightens the shoulder to a single residual seam
- one opening `purple` pass that stays clean across the first tranche
- one deeper `purple` continuation pass that stays equally clean
- one opening `pink` pass with a visible warm-orange and wine shoulder
- one deeper `pink` continuation pass that closes the lane cleanly
- one opening `orange` pass with a visible pale straw, buff, and blush shoulder
- one deeper `orange` continuation pass that narrows that shoulder
- one deeper orange-gold continuation pass that holds a cream, straw, and olive edge

Fail-pressure pulse is no longer a staged boundary. It is the active
`Beta 1.0` method surface for non-OCR Huemiliator eval work.

## Active Pulse Snapshot

| Surface | Result |
| --- | --- |
| stage | `Beta 1.0` |
| active family lane | `orange` |
| pulse pattern | `source-order` |
| pulse source-order start | `383` |
| pulse size | `15` |
| active proof surface | `19947..19961` |
| pulse verdict | `PASS` |
| anchors | `10` |
| counted seams | `5` |
| excluded noise | `0` |
| comparison baseline | closed third corrected `red` rerun at `18424..19691` |

## Quarantine Boundary

The current `Beta 1.0` active surface was reached through one baseline archive
plus seventeen clean pulse rollovers:

- row-level comparison baseline:
  - `closed third corrected red rerun`
  - `1268` archived rows
  - `.local/parked/eval-surface-20260522T001236Z-closed-third-corrected-red-rerun.jsonl`
- first `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 1 red tranche 001`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T002145Z-beta-1-0-pulse-1-red-tranche-001.jsonl`
- second `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 2 red tranche 002`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T003037Z-beta-1-0-pulse-2-red-tranche-002.jsonl`
- third `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 3 yellow tranche 001`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T003539Z-beta-1-0-pulse-3-yellow-tranche-001.jsonl`
- fourth `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 4 yellow tranche 002`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T005009Z-beta-1-0-pulse-4-yellow-tranche-002.jsonl`
- fifth `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 5 yellow tranche 003`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T010326Z-beta-1-0-pulse-5-yellow-tranche-003.jsonl`
- sixth `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 6 yellow tranche 004`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T010949Z-beta-1-0-pulse-6-yellow-tranche-004.jsonl`
- seventh `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 7 green tranche 001`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T011302Z-beta-1-0-pulse-7-green-tranche-001.jsonl`
- eighth `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 8 green tranche 002`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T011733Z-beta-1-0-pulse-8-green-tranche-002.jsonl`
- ninth `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 9 blue tranche 001`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T013650Z-beta-1-0-pulse-9-blue-tranche-001.jsonl`
- tenth `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 10 blue tranche 002`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T014834Z-beta-1-0-pulse-10-blue-tranche-002.jsonl`
- eleventh `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 11 blue tranche 003`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T015452Z-beta-1-0-pulse-11-blue-tranche-003.jsonl`
- twelfth `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 12 purple tranche 001`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T015833Z-beta-1-0-pulse-12-purple-tranche-001.jsonl`
- thirteenth `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 13 purple tranche 002`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T021414Z-beta-1-0-pulse-13-purple-tranche-002.jsonl`
- fourteenth `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 14 pink tranche 001`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T022127Z-beta-1-0-pulse-14-pink-tranche-001.jsonl`
- fifteenth `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 15 pink tranche 002`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T022930Z-beta-1-0-pulse-15-pink-tranche-002.jsonl`
- sixteenth `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 16 orange tranche 001`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T023943Z-beta-1-0-pulse-16-orange-tranche-001.jsonl`
- seventeenth `Beta 1.0` pulse rollover:
  - `beta 1 0 pulse 17 orange tranche 002`
  - `15` archived rows
  - `.local/parked/eval-surface-20260522T024557Z-beta-1-0-pulse-17-orange-tranche-002.jsonl`

That keeps the live DB truthful to one current proof surface at a time.

## Current Counted Seams

The active orange continuation still carries a visible shoulder, but it now
reads more as cream, straw, and olive than as the lighter blush opening.

Counted seam rows:

- `Double cream -> Creampuff`
- `Sunlight -> Straw`
- `Straw -> Cocoon`
- `Rattan -> Ecru olive`
- `Reed yellow -> Apricot gelato`

## Current Anchors

The orange-gold core still survives around that deeper shoulder.

Representative anchors:

- `Copper -> Oak buff`
- `Jojoba -> Coral sands`
- `Parsnip -> Almost apricot`
- `Raffia -> Burnt henna`
- `Bamboo -> Warm apricot`
- `Cocoon -> Pastry shell`
- `Southern moss -> Butterum`
- `Olivenite -> Amber gold`
- `Antique gold -> Peach`
- `Mimosa -> Burnt orange`

## Beta Note

This beta is moving with much cleaner forward pressure than the earlier
row-level eval shape.

- clean passes are stacking across multiple family lanes instead of collapsing
  back into the same repeated seam
- when a seam is real, it is showing up quickly as one narrow shoulder instead
  of hiding inside a large mixed batch
- once a correction lands, the next bounded pulse is able to move forward
  instead of dragging the same proof surface back through another long loop
- local quarantine is helping keep that motion honest by preserving the older
  surface without forcing it to stay live

## What It Means

The first four pulses still matter together. They established the red baseline,
showed a yellow core pass, and then exposed the targeted yellow shoulder as a
real fail surface.

The fifth pulse matters because it proves the explicit correction changed the
runtime behavior:

- anchors are back above counted seams
- the earlier green-olive collapse no longer dominates the rerun
- no excluded rows were needed to force the recovery
- the remaining pressure is smaller and more chartreuse than olive
- that remaining pressure still includes green-named rows inside `yellow`
- the final chartreuse cut is now explicit in runtime code

The sixth pulse closes the yellow lane:

- the targeted rerun comes back at `15 anchors / 0 counted seams`
- no residual chartreuse seam remains inside the active pulse
- `yellow` can now park beside `red`

`Green` is the next active family lane.

The seventh pulse opens that lane cleanly:

- the former yellow-edge carryovers now hold as green
- the deeper early-green core also stays clean
- no counted seams or exclusions were needed

The eighth pulse keeps that read intact:

- the second green continuation also comes back at `15 anchors / 0 counted seams`
- no new seam appears as the lane moves deeper
- `green` can now park beside `red` and `yellow`

The ninth pulse opens blue honestly:

- the tranche passes under pressure at `10 anchors / 5 counted seams`
- the visible shoulder is purple and aqua, not a full lane collapse
- `blue` stays active and needs a deeper continuation read before any park call

The tenth pulse keeps that read consistent:

- the deeper continuation also passes at `10 anchors / 5 counted seams`
- the same purple-and-aqua shoulder repeats rather than widening into a full collapse
- `blue` still does not park honestly without an explicit correction

The eleventh pulse makes that correction visible in runtime evidence:

- the rerun improves to `14 anchors / 1 counted seam`
- the old green-and-aqua replacements are gone from the active blue slice
- one residual aqua seam remains at `Twilight purple -> Aquarelle`
- `blue` is now stable enough to park behind the corrected rerun

The twelfth pulse opens purple cleanly:

- the opening tranche comes back at `15 anchors / 0 counted seams`
- no same-family shoulder appears in the earliest purple slice
- `purple` stays active, but it now opens from a clean pass rather than a repair lane

The thirteenth pulse keeps that read intact:

- the deeper continuation also comes back at `15 anchors / 0 counted seams`
- no new seam appears as the lane moves deeper
- `purple` is now stable enough to park

The fourteenth pulse opens pink honestly:

- the tranche passes under pressure at `9 anchors / 6 counted seams`
- the visible shoulder is warm-orange and wine, not a full lane collapse
- `pink` stays active and needs a deeper continuation read before any park call

The fifteenth pulse closes that lane cleanly:

- the deeper continuation comes back at `15 anchors / 0 counted seams`
- the opening warm-orange and wine shoulder does not repeat deeper in the lane
- `pink` is now stable enough to park
- `orange` becomes the next active family lane

The sixteenth pulse opens orange honestly:

- the tranche passes under pressure at `9 anchors / 6 counted seams`
- the visible shoulder is pale straw, buff, and blush, not a full lane collapse
- `orange` stays active and needs a deeper continuation read before any park call

The seventeenth pulse keeps that read but narrows it:

- the deeper continuation comes back at `11 anchors / 4 counted seams`
- the same shoulder stays visible, but less of the slice collapses into it
- the orange core is holding better as the lane moves deeper
- `orange` still stays active and needs one more continuation read before any park call

The eighteenth pulse keeps orange active but changes the pressure shape:

- the deeper continuation comes back at `10 anchors / 5 counted seams`
- the visible shoulder now reads as cream, straw, and olive rather than the earlier pale blush opening
- the orange-gold core still holds, but the next slice is now close to a true orange-to-yellow test
- `orange` still stays active and needs a fourth continuation read before any park call

## Comparison Read

Compared against the closed row-level rerun and the earlier `red` pulses:

- row-level comparison baseline:
  - `1268 total / 1162 pass / 106 fail / 0 pending`
- first bounded pulse:
  - `15 total / 11 pass / 4 fail / 0 pending`
- second bounded pulse:
  - `15 total / 10 pass / 5 fail / 0 pending`
- third bounded pulse:
  - `15 total / 9 pass / 6 fail / 0 pending`
- fourth bounded pulse:
  - `15 total / 5 pass / 10 fail / 0 pending`
- fifth bounded pulse:
  - `15 total / 10 pass / 5 fail / 0 pending`
- sixth bounded pulse:
  - `15 total / 15 pass / 0 fail / 0 pending`
- seventh bounded pulse:
  - `15 total / 15 pass / 0 fail / 0 pending`
- eighth bounded pulse:
  - `15 total / 15 pass / 0 fail / 0 pending`
- ninth bounded pulse:
  - `15 total / 10 pass / 5 fail / 0 pending`
- tenth bounded pulse:
  - `15 total / 10 pass / 5 fail / 0 pending`
- eleventh bounded pulse:
  - `15 total / 14 pass / 1 fail / 0 pending`
- twelfth bounded pulse:
  - `15 total / 15 pass / 0 fail / 0 pending`
- thirteenth bounded pulse:
  - `15 total / 15 pass / 0 fail / 0 pending`
- fourteenth bounded pulse:
  - `15 total / 9 pass / 6 fail / 0 pending`
- fifteenth bounded pulse:
  - `15 total / 15 pass / 0 fail / 0 pending`
- sixteenth bounded pulse:
  - `15 total / 9 pass / 6 fail / 0 pending`
- seventeenth bounded pulse:
  - `15 total / 11 pass / 4 fail / 0 pending`
- current bounded pulse:
  - `15 total / 10 pass / 5 fail / 0 pending`

The row-level rerun stays important as the closed comparison baseline, but the
live verdict unit is now the bounded pulse and the active proof surface is the
most recent judged tranche.

## What Stays Open

The two `red` pulses answer two pressure questions:

- can the early `red` shoulder survive a bounded pass/fail pulse
- can the deeper old repeat cluster survive a bounded pass/fail pulse

The four `yellow` pulses now answer four more:

- can a bright-core `yellow` tranche survive a bounded pulse before the
  green-olive shoulder takes over
- does that green-olive shoulder dominate once `yellow` is targeted directly
- does the explicit yellow-to-green cut restore a passing targeted rerun
- does the final chartreuse cut clean the remaining shoulder enough to park

The two `green` pulses answer two more:

- does the opening green shoulder hold cleanly once `yellow` is parked
- does the deeper green continuation stay clean enough to park the lane

The first three `blue` pulses answer three more:

- does the earliest blue opening survive a bounded pulse without collapsing into
  the purple and aqua shoulder
- does the deeper blue continuation repeat that same shoulder rather than widening into a lane collapse
- does the explicit blue shoulder correction recover a stable local pass without damaging the blue core

The open question moves forward:

- does the fourth bounded `orange` continuation keep the visible cream, straw,
  and olive shoulder subordinate, or does the orange-to-yellow boundary open up

Later `red` work is optional follow-up, not the next required gate.

## Next Kernel

The clean follow-through question is:

1. keep `19947..19961` as the current active proof surface
2. carry the two passing `red` pulses plus the parked `yellow`, `green`,
   `blue`, `purple`, and `pink` proof stacks as the comparison stack
3. treat the third `orange` continuation as a stable follow-through pass with a
   cream, straw, and olive edge
4. run the fourth bounded `orange` continuation from source order `478`
