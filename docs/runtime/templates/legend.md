<!-- @format -->

# Research Legend

This template supplies the shared vocabulary for a tracked research index. It
does not assert the current status of any project note.

## File-map row

| Code | File | Meaning | Category | Status |
| --- | --- | --- | --- | --- |
| `<CODE>` | `NNN_CODE.md` | `<one-line job>` | `<category>` | `<status>` |

Use the general filename contract `NNN_CODE.md` or
`NNN_CODE-QUALIFIER.md`. Boundary notes may use project-specific codes such as
`010_PB10.md` or `020_B10.md`; those are dated examples, not a restriction on
the other categories.

## Ordering

| Range | Role |
| ---: | --- |
| `000` | index and legend |
| `010-099` | method boundaries |
| `100-199` | family pulse lane docs |
| `200-299` | drift, correction, and edge-case docs |
| `300-399` | validation and gate-proof docs |
| `400-499` | hypotheses and backlog |

## Status meanings

| Status | Meaning |
| --- | --- |
| `staged` | next boundary or claim, not live evidence yet |
| `active` | current live boundary or lane |
| `closed` | finished evidence surface held in the baseline |
| `parked` | lane stable enough to leave behind the active lane |
| `snapshot` | bounded read captured for reference |
| `representative` | case stands in for a wider seam |
| `anchor` | case or row holds under the active lens |
| `counted_seam` | case or row is a counted failure under the active lens |
| `excluded_noise` | case or row excluded with an explicit reason |
| `source_pool` | candidate pool with no promoted claim |
| `triaged` | candidate pool has an initial read and promotion rule |
| `promoted` | backlog item moved into a research surface |
| `running` | validation is in progress |
| `failed` | validation did not hold |
| `archived` | preserved but no longer active |

## Category meanings

| Category | Owns |
| --- | --- |
| `legend` | file map, code ranges, and shared status language |
| `boundary` | beta, pre-beta, or eval-method boundary |
| `lane` | active, parked, or closed family evidence lane and read |
| `case` | one representative output, row, pulse, or bounded slice |
| `validation` | eval, runtime, branch preflight, or closeout proof |
| `hypothesis` | staged correction or method claim before promotion or retirement |
| `backlog` | candidate drift groups, source pools, and parked follow-up lanes |
