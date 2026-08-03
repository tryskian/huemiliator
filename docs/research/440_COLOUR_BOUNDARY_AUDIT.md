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

Do the strongest family-balanced mixed Lab bins from `colour-boundaries` expose
classifier seams before chart and Polinko-facing eval expansion?

## Status

Closed.

The first three colour-boundary report pulses launched from the strongest mixed
Lab bins in `huemiliator colour-boundaries --limit 3 --samples-per-family 1`.

The first pulse passed at `20154..20158`:
`5 anchors / 0 counted seams / 0 excluded`.

The second pulse passed at `20159..20162`:
`4 anchors / 0 counted seams / 0 excluded`.

The third pulse passed at `20163..20166`:
`4 anchors / 0 counted seams / 0 excluded`.

The prior live proof surfaces were quarantined locally before later pulses:

| Archived surface | Rows | Archive |
| --- | ---: | --- |
| `20151..20153` | `3` | `.local/parked/eval-surface-20260803T215237Z-beta-1-0-boundary-balanced-warm-low-chroma-preflight.jsonl` |
| `20154..20158` | `5` | `.local/parked/eval-surface-20260803T220104Z-beta-1-0-colour-boundary-warm-low-chroma-five-family-pass.jsonl` |
| `20159..20162` | `4` | `.local/parked/eval-surface-20260803T220515Z-beta-1-0-colour-boundary-neutral-brown-orange-yellow-pass.jsonl` |

## Boundary Source

| Signal | Value |
| --- | --- |
| report command | `huemiliator colour-boundaries --limit 1 --samples-per-family 1` |
| Lab a* bin | `10..20` |
| Lab b* bin | `10..20` |
| swatches in bin | `57` |
| family counts | `brown 31`, `neutral 9`, `pink 9`, `orange 5`, `red 3` |
| seed mode | `explicit-input-hex` |

## First Pulse Rows

| Output | Family sample | Input | Runtime family | Replacement | Label |
| ---: | --- | --- | --- | --- | --- |
| `20154` | `249` `Bison` | `#6e4f3a` | `brown` | `Tannin` | `anchor` |
| `20155` | `311` `Macaroon` | `#b38b71` | `neutral` | `Natural` | `anchor` |
| `20156` | `333` `Evening sand` | `#ddb6ab` | `pink` | `Silver pink` | `anchor` |
| `20157` | `319` `Pale peach` | `#fed1bd` | `orange` | `Tender peach` | `anchor` |
| `20158` | `681` `Ash rose` | `#b5817d` | `red` | `Renaissance rose` | `anchor` |

## Second Boundary Source

| Signal | Value |
| --- | --- |
| report command | `huemiliator colour-boundaries --limit 3 --samples-per-family 1` |
| Lab a* bin | `0..10` |
| Lab b* bin | `10..20` |
| swatches in bin | `129` |
| family counts | `neutral 88`, `brown 32`, `orange 6`, `yellow 3` |
| seed mode | `explicit-input-hex` |

## Second Pulse Rows

| Output | Family sample | Input | Runtime family | Replacement | Label |
| ---: | --- | --- | --- | --- | --- |
| `20159` | `20` `Angora` | `#dfd1bb` | `neutral` | `Lamb's wool` | `anchor` |
| `20160` | `104` `Lead gray` | `#8a7963` | `brown` | `Rocky road` | `anchor` |
| `20161` | `236` `Incense` | `#af9a7e` | `orange` | `Travertine` | `anchor` |
| `20162` | `97` `Twill` | `#a79b82` | `yellow` | `Aloe wash` | `anchor` |

## Third Boundary Source

| Signal | Value |
| --- | --- |
| report command | `huemiliator colour-boundaries --limit 3 --samples-per-family 1` |
| Lab a* bin | `10..20` |
| Lab b* bin | `0..10` |
| swatches in bin | `58` |
| family counts | `neutral 20`, `pink 20`, `brown 15`, `red 3` |
| seed mode | `explicit-input-hex` |

## Third Pulse Rows

| Output | Family sample | Input | Runtime family | Replacement | Label |
| ---: | --- | --- | --- | --- | --- |
| `20163` | `297` `Almondine` | `#a78c8b` | `neutral` | `Plum kitten` | `anchor` |
| `20164` | `843` `Silver pink` | `#dcb1af` | `pink` | `Grapeade` | `anchor` |
| `20165` | `404` `Fudgesickle` | `#63403a` | `brown` | `Beaver fur` | `anchor` |
| `20166` | `894` `Mellow rose` | `#d9a6a1` | `red` | `Ash rose` | `anchor` |

## Read

The first warm low-chroma five-family junction and the second neutral / brown /
orange / yellow junction both held under exact-input sampling. The third
neutral / pink / brown / red junction also held. The boundary report is useful
for candidate selection, but these pulses do not justify a classifier edit.

Next colour-boundary work should move to another promoted mixed bin or chart
signal rather than retesting these passed surfaces.

## Validation

```bash
PYTHONPATH=src .venv/bin/python -m huemiliator colour-boundaries --limit 1 --samples-per-family 1
PYTHONPATH=src .venv/bin/python -m huemiliator eval-pulse-start --input-hex "#6e4f3a" --input-hex "#b38b71" --input-hex "#ddb6ab" --input-hex "#fed1bd" --input-hex "#b5817d" --quarantine-label "beta 1 0 boundary balanced warm low chroma preflight"
PYTHONPATH=src .venv/bin/python -m huemiliator eval-pulse-report 20154 20158
PYTHONPATH=src .venv/bin/python -m huemiliator colour-boundaries --limit 3 --samples-per-family 1
PYTHONPATH=src .venv/bin/python -m huemiliator eval-pulse-start --input-hex "#dfd1bb" --input-hex "#8a7963" --input-hex "#af9a7e" --input-hex "#a79b82" --quarantine-label "beta 1 0 colour boundary warm low chroma five family pass"
PYTHONPATH=src .venv/bin/python -m huemiliator eval-pulse-report 20159 20162
PYTHONPATH=src .venv/bin/python -m huemiliator eval-pulse-start --input-hex "#a78c8b" --input-hex "#dcb1af" --input-hex "#63403a" --input-hex "#d9a6a1" --quarantine-label "beta 1 0 colour boundary neutral brown orange yellow pass"
PYTHONPATH=src .venv/bin/python -m huemiliator eval-pulse-report 20163 20166
```
