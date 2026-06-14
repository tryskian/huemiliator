# Warm Edge Residue Audit

| Field | Value |
| --- | --- |
| Code | `WARM_EDGE_AUDIT` |
| Category | `hypothesis` |
| Status | `active` |
| Date | `2026-06-09` |
| Last evidence | `2026-06-14` |
| Owns | warm-edge residue audit scope and active pulse read |

## What This Asks

After the full family-lane sweep, which warm residue groups still need bounded
`Beta 1.0` pressure?

## Status

Active.

The first warm-edge pulse launched from exact `orange` yellow-gold inputs and
passed at `20121..20128`: `8 anchors / 0 counted seams / 0 excluded`.

The second warm-edge pulse launched from the unique exact inputs in the
`yellow` green / olive evidence set and passed at `20129..20139`:
`11 anchors / 0 counted seams / 0 excluded`.

The third warm-edge pulse launched from exact `orange` pale straw / buff /
blush inputs and passed at `20140..20145`:
`6 anchors / 0 counted seams / 0 excluded`.

The previous live proof surfaces were quarantined locally before each pulse:

| Archived surface | Rows | Archive |
| --- | ---: | --- |
| `20106..20120` | `15` | `.local/parked/eval-surface-20260609T161558Z-beta-1-0-neutral-continuation-before-warm-edge-audit.jsonl` |
| `20121..20128` | `8` | `.local/parked/eval-surface-20260614T180152Z-beta-1-0-warm-edge-orange-yellow-gold-boundary-pass.jsonl` |
| `20129..20139` | `11` | `.local/parked/eval-surface-20260614T180546Z-beta-1-0-warm-edge-yellow-green-olive-shoulder-pass.jsonl` |

## Audit Boundary

| Boundary | In scope | Out of scope |
| --- | --- | --- |
| warm cohort | `red`, `orange`, `yellow`, and `brown` rows reachable through the local `warm` audit cohort | treating `warm` as a runtime family |
| warm-neutral residue | exact `neutral` rows with warm peach / pearl drift | assuming `--family warm` includes `neutral` |
| family sweep | historical counted seams that point at next scope | treating residue counts as live failure totals |
| runtime | evidence review before any runtime edit | classifier or one-up changes without a fresh promoted claim |

## Residue Groups

| Priority | Group | Evidence rows | Count | Current read | Sampling mode |
| ---: | --- | --- | ---: | --- | --- |
| 1 | `orange` yellow-gold boundary | `19962`, `19964`, `19965`, `19968`, `19970`, `19971`, `19973`, `19976` | `8` | passed at `20121..20128`; six rows now route `orange`, and `Honey` / `Ceylon yellow` route `yellow` | done: explicit inputs |
| 2 | `yellow` green / olive shoulder | `19723`, `19729`, `19730`, `19733`, `19734`, `19735`, `19737`, `19738`, `19741`, `19742`, `19743`, `19746`, `19747`, `19749`, `19750`, `19751` | `16` | passed at `20129..20139`; repeated rows collapse to `11` unique inputs, with olive-side rows routing `green` and brighter rows routing `yellow` | done: unique explicit inputs |
| 3 | `orange` pale straw / buff / blush shoulder | `19918`, `19919`, `19920`, `19921`, `19922`, `19923` | `6` | passed at `20140..20145`; all rows route and replace within `orange` | done: explicit inputs |
| 4 | `yellow` residual chartreuse shoulder | `19756`, `19757`, `19758`, `19765`, `19766` | `5` | smaller post-correction yellow residue | exact inputs preferred |
| 5 | warm `neutral` peach / pearl residue | `20084`, `20088`, `20107` | `3` | outside the cool-edge split; still visible after neutral parked | explicit inputs only |

## Comparison Baselines

| Surface | Rows | Read | Use |
| --- | --- | --- | --- |
| `red` warm-clay / peach shoulder | `19692`, `19694`, `19697`, `19699`, `19707`, `19709`, `19710`, `19714`, `19720` | closed under the red-orange audit and later red pulses | comparison only |
| `brown` family lane | none counted in the row-order `Beta 1.0` pulse stack | parked cleanly by row data | do not reopen without new evidence |
| cool `neutral` split | `20082`, `20083`, `20085`, `20086`, `20087`, `20090`, `20091`, `20094`, `20095` | corrected by the three-pulse split at `20097..20105` | do not reopen without a new cool-edge claim |

## Gate Before Sampling

| Gate | Rule |
| --- | --- |
| choose one group | do not run one broad warm pulse before selecting the edge group |
| choose the seed mode | use `--family warm` only for `red`, `orange`, `yellow`, and `brown`; use repeated `--input-hex` for mixed or `neutral` rows |
| preserve verdict units | a thematic group should stay a bounded pulse, not a loose row pile |
| keep live DB clean | no new pulse starts until the current `20140..20145` proof surface is intentionally replaced or quarantined |

## Recommendation

Use the `yellow` residual chartreuse shoulder as the next candidate if the
warm-edge audit continues. The first three warm-edge pulses already passed
cleanly, so do not rerun them without new evidence.
