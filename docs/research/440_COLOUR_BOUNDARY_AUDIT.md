# Colour Boundary Audit

| Field | Value |
| --- | --- |
| Code | `COLOUR_BOUNDARY_AUDIT` |
| Category | `validation` |
| Status | `closed` |
| Date | `2026-08-03` |
| Last evidence | `2026-08-03` |
| Owns | colour-boundary report pulse proof before classifier edits |

## What This Asks

Does the strongest family-balanced mixed Lab bin from `colour-boundaries` expose
a classifier seam before chart and Polinko-facing eval expansion?

## Status

Closed.

The first colour-boundary report pulse launched from the strongest mixed Lab
bin in `huemiliator colour-boundaries --limit 1 --samples-per-family 1`.

The pulse passed at `20154..20158`:
`5 anchors / 0 counted seams / 0 excluded`.

The prior live proof surface was quarantined locally before the pulse:

| Archived surface | Rows | Archive |
| --- | ---: | --- |
| `20151..20153` | `3` | `.local/parked/eval-surface-20260803T215237Z-beta-1-0-boundary-balanced-warm-low-chroma-preflight.jsonl` |

## Boundary Source

| Signal | Value |
| --- | --- |
| report command | `huemiliator colour-boundaries --limit 1 --samples-per-family 1` |
| Lab a* bin | `10..20` |
| Lab b* bin | `10..20` |
| swatches in bin | `57` |
| family counts | `brown 31`, `neutral 9`, `pink 9`, `orange 5`, `red 3` |
| seed mode | `explicit-input-hex` |

## Pulse Rows

| Output | Family sample | Input | Runtime family | Replacement | Label |
| ---: | --- | --- | --- | --- | --- |
| `20154` | `249` `Bison` | `#6e4f3a` | `brown` | `Tannin` | `anchor` |
| `20155` | `311` `Macaroon` | `#b38b71` | `neutral` | `Natural` | `anchor` |
| `20156` | `333` `Evening sand` | `#ddb6ab` | `pink` | `Silver pink` | `anchor` |
| `20157` | `319` `Pale peach` | `#fed1bd` | `orange` | `Tender peach` | `anchor` |
| `20158` | `681` `Ash rose` | `#b5817d` | `red` | `Renaissance rose` | `anchor` |

## Read

The warm low-chroma five-family junction held under exact-input sampling. The
boundary report is useful for candidate selection, but this pulse does not
justify a classifier edit.

Next colour-boundary work should move to another promoted mixed bin or chart
signal rather than retesting this passed surface.

## Validation

```bash
PYTHONPATH=src .venv/bin/python -m huemiliator colour-boundaries --limit 1 --samples-per-family 1
PYTHONPATH=src .venv/bin/python -m huemiliator eval-pulse-start --input-hex "#6e4f3a" --input-hex "#b38b71" --input-hex "#ddb6ab" --input-hex "#fed1bd" --input-hex "#b5817d" --quarantine-label "beta 1 0 boundary balanced warm low chroma preflight"
PYTHONPATH=src .venv/bin/python -m huemiliator eval-pulse-report 20154 20158
```
