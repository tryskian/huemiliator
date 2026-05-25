# Neutral Three-Pulse Split

Date: `2026-05-24`

## What This Asks

Should the next `neutral` read stop using one larger bounded eval and instead
split the nine cool-edge seams inside `20082..20096` into three smaller eval
pulses of three rows each?

## Status

Probably yes, but this is staged, not active.

The current `neutral` fail surface is coherent enough to justify a smaller
method read. The nine dominant cool-edge seams are not random spread. They
cluster into three visible pressure groups:

- lilac / mauve drift
- blue / jade drift
- mint / green drift

This note stages a smaller-pulse method for the next `neutral` pass. It does
not replace `Beta 1.0`, and it does not change the current live proof surface
yet.

## Current Surface

| Item | Current state |
| --- | --- |
| active proof surface | `20082..20096` |
| active lane | `neutral` |
| counted result | `4 anchors / 11 counted seams / 0 excluded` |
| dominant fail shape | `9` cool-edge seams inside pale `neutral` |
| secondary residue | `2` warm seams |

## Proposed Pulse Split

Run the next `neutral` read as three smaller eval pulses of three rows each:

| Pulse | Output ids | Pressure group |
| --- | --- | --- |
| `pulse 1` | `20082`, `20083`, `20094` | lilac / mauve |
| `pulse 2` | `20085`, `20090`, `20091` | blue / jade |
| `pulse 3` | `20086`, `20087`, `20095` | mint / green |

Pulse rows:

- `pulse 1`: `Tapioca -> Lilac ash`, `Creme brulee -> Lilac snow`,
  `Petal pink -> Shrinking violet`
- `pulse 2`: `Sheer pink -> Bit of blue`, `Ecru -> Mystic blue`,
  `Navajo -> Moonlight jade`
- `pulse 3`: `Dew -> Water lily`, `Powder puff -> Whisper green`,
  `Bridal blush -> Hint of mint`

Keep the two warm seams outside that split as secondary residue:

- `20084` `Parchment -> Novelle peach`
- `20088` `Pearled ivory -> Pearl`

## What Stays The Same

- `Beta 1.0` remains the active research method
- pulse verdict stays the live verdict unit
- `neutral` remains the active family lane
- the current live proof surface stays `20082..20096` until a new pulse is run

## Why This Helps

The current `15`-row fail surface answers the broad question honestly, but it
mixes three cool-edge problems together:

- lilac / mauve pressure
- blue / jade pressure
- mint / green pressure

Three smaller pulses would make the next correction easier to read:

- one correction can be judged against one pressure group at a time
- a surviving seam stays attributable instead of hiding inside a mixed tranche
- the method can tell whether `neutral` needs one narrow cut or several

## Operational Note

Current pulse tooling already supports smaller bounded runs through
`huemiliator eval-pulse-start --count 3`.

This exact `3 x 3` split is still a staged research method, not yet a
first-class operator surface. The current command seeds contiguous
source-order rows, while this note stages three thematic cool-edge groups drawn
from the current fail surface.

## What Would Activate It

This method becomes active only when:

1. the next `neutral` correction is ready to test
2. the next eval read is intentionally run as three smaller pulses
3. the research index treats that smaller-pulse split as the current staged
   neutral method
