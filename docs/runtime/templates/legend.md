<!-- @format -->

# Research Legend

| Code | File | Meaning | Category | Status |
| --- | --- | --- | --- | --- |
| `PB10` | `010_PB10.md` | pre-Beta 1.0 fail-pressure pulse boundary | `boundary` | `closed` |
| `B10` | `020_B10.md` | `Beta 1.0` fail-pressure pulse boundary | `boundary` | `active` |
| `BROWN` | `120_BROWN.md` | brown context-dependence lane | `lane` | `snapshot` |
| `RED_ORANGE` | `210_RED_ORANGE.md` | red-to-orange edge drift case | `case` | `representative` |
| `RO_AUDIT` | `310_RED_ORANGE_AUDIT.md` | red-orange edge audit proof | `validation` | `closed` |
| `N3` | `410_N3.md` | staged neutral three-pulse method claim | `hypothesis` | `staged` |

## Ordering

| Range | Role |
| ---: | --- |
| `000` | index and legend |
| `010-099` | method boundaries |
| `100-199` | family pulse lane docs |
| `200-299` | drift, correction, and edge-case docs |
| `300-399` | validation and gate-proof docs |
| `400-499` | hypotheses and backlog |

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
