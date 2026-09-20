# Research Legend

| Field | Value |
| --- | --- |
| Code | `000_LEGEND` |
| Category | `legend` |
| Status | `active` |
| Last evidence | `2026-08-03` |
| Last updated | `2026-09-20` |
| Owns | file map, code ranges, categories, and shared status language |

## File Map

| Code | File | Meaning | Category | Status |
| --- | --- | --- | --- | --- |
| `README` | `README.md` | research entry and current-state index | `legend` | `active` |
| `PB10` | `010_PB10.md` | pre-Beta 1.0 fail-pressure pulse boundary | `boundary` | `closed` |
| `B10` | `020_B10.md` | `Beta 1.0` fail-pressure pulse boundary | `boundary` | `closed` |
| `PB_BEHAVIOUR` | `030_PB_BEHAVIOUR.md` | assistant-run 15-minute behaviour pulse staging | `boundary` | `staged` |
| `BROWN` | `120_BROWN.md` | brown context-dependence lane | `lane` | `snapshot` |
| `RED_ORANGE` | `210_RED_ORANGE.md` | red-to-orange edge drift case | `case` | `representative` |
| `RESPONSE_CONSTRUCTION` | `220_RESPONSE_CONSTRUCTION.md` | historical wording failures and pending cue mini | `case` | `snapshot` |
| `CARRIED_WORDING` | `230_CARRIED_WORDING.md` | attributed correction of four carried wording verdicts | `case` | `closed` |
| `YOUR_PINK` | `240_YOUR_PINK.md` | Peanut's contextual high-signal example for shared judgment | `case` | `representative` |
| `RO_AUDIT` | `310_RED_ORANGE_AUDIT.md` | red-orange edge audit proof | `validation` | `closed` |
| `320_BANK_FREE_ALIGNMENT` | `320_BANK_FREE_ALIGNMENT.md` | source audit, adaptation and integration checks | `validation` | `snapshot` |
| `330_EVAL_ARCHIVE` | `330_EVAL_ARCHIVE.md` | verified archive and empty live eval stores | `validation` | `closed` |
| `N3` | `410_N3.md` | corrected neutral three-pulse split | `validation` | `closed` |
| `RESIDUE` | `420_RESIDUE.md` | post-sweep counted-seam source map | `backlog` | `closed` |
| `WARM_EDGE_AUDIT` | `430_WARM_EDGE_AUDIT.md` | warm-edge residue audit proof and closeout rule | `validation` | `closed` |
| `COLOUR_BOUNDARY_AUDIT` | `440_COLOUR_BOUNDARY_AUDIT.md` | colour-boundary report pulse proof | `validation` | `closed` |
| `LOCAL_LANGUAGE` | `450_LOCAL_LANGUAGE.md` | superseded library hypothesis and source history | `hypothesis` | `archived` |
| `BANK_FREE_FOUNDATION` | `460_BANK_FREE_FOUNDATION.md` | preserved v8/v9 platform comparisons | `hypothesis` | `snapshot` |
| `V10_BENCHMARK` | `470_V10_BENCHMARK.md` | selected behavioural foundation and exact source evidence | `hypothesis` | `snapshot` |

`RESIDUE` is the closed source map; `WARM_EDGE_AUDIT` is the closed proof
surface promoted from that map. `COLOUR_BOUNDARY_AUDIT` is the report-derived
proof surface for mixed Lab bins.

`PB_BEHAVIOUR` owns the next research direction and staged judgment mechanics.
The runtime directions are implemented; the closed colour findings remain the
carried baseline.
`LOCAL_LANGUAGE` preserves the superseded experiment. `V10_BENCHMARK` owns the
selected platform source; `320_BANK_FREE_ALIGNMENT` records its adaptation to Hugh's
existing colour flow. Source templates remain distinct from runtime directions.

## Ordering

| Range | Role |
| ---: | --- |
| `000` | index and legend |
| `010-099` | method boundaries |
| `100-199` | family pulse lane docs |
| `200-299` | drift, correction, and edge-case docs |
| `300-399` | validation and gate-proof docs |
| `400-499` | hypotheses and backlog |

## Filename Contract

| Rule | Shape |
| --- | --- |
| file names | `NNN_CODE.md` or `NNN_CODE-QUALIFIER.md` |
| dates | inside docs, not filenames |
| entry file | `README.md` |
| legend file | `000_LEGEND.md` |
| code style | short, uppercase, and stable once linked |

## Status Meanings

| Status | Meaning |
| --- | --- |
| `staged` | next boundary or claim, not live evidence yet |
| `active` | current live boundary or lane |
| `closed` | finished evidence surface held and moved into baseline |
| `parked` | lane is stable enough to leave behind the active lane |
| `snapshot` | bounded read captured for reference |
| `representative` | case stands in for a wider seam cleanly |
| `anchor` | case or row holds under the active lens |
| `counted_seam` | case or row is a counted failure under the active lens |
| `excluded_noise` | case or row is excluded from the verdict with an explicit reason |
| `source_pool` | backlog pool has candidates but no promoted claim |
| `triaged` | backlog pool has an initial read and promotion rule |
| `promoted` | backlog item moved into a boundary, lane, case, or hypothesis |
| `running` | validation is in progress |
| `failed` | validation did not hold |
| `archived` | preserved but no longer active |

## Category Meanings

| Category | Owns |
| --- | --- |
| `legend` | file map, code ranges, and shared status language |
| `boundary` | beta, pre-beta, or eval-method boundary |
| `lane` | active, parked, or closed family evidence lane and read |
| `case` | one representative output, row, pulse, or bounded slice |
| `validation` | eval, runtime, branch preflight, or closeout proof |
| `hypothesis` | staged correction or method claim before promotion or retirement |
| `backlog` | candidate drift groups, source pools, and parked follow-up lanes |
