<!-- @format -->

# Huemiliator Research Template Folder

Local peanut draft for splitting the `huemiliator` research-doc standard into
reusable category templates.

## Kernel

| Rule | Choice |
| --- | --- |
| Target folder | `docs/research/` |
| Entry file | `README.md` |
| Legend file | `000_LEGEND.md` |
| Filename shape | `NNN_CODE.md` or `NNN_CODE-QUALIFIER.md` |
| Dates | inside docs, not filenames |
| Default style | concise and visual-forward |
| First content surface | chart, table, or diagram |

## Template Files

| Template | Use For |
| --- | --- |
| [legend.md](legend.md) | `000_LEGEND.md` |
| [boundary.md](boundary.md) | beta or eval-method boundary docs |
| [lane.md](lane.md) | current family or pulse evidence lane docs |
| [case.md](case.md) | representative drift, correction, or edge-case docs |
| [validation.md](validation.md) | rerun, gate, or proof-surface docs |
| [hypothesis.md](hypothesis.md) | staged correction or method hypothesis docs |
| [backlog.md](backlog.md) | source pool, family, and correction-candidate docs |

## Code Ranges

| Range | Role |
| ---: | --- |
| `000` | index and legend |
| `010-099` | method boundaries |
| `100-199` | family pulse lane docs |
| `200-299` | drift, correction, and edge-case docs |
| `300-399` | validation and gate-proof docs |
| `400-499` | hypotheses and backlog |

## Shared Metadata

Every category template starts with this table shape.

| Field | Value |
| --- | --- |
| Code | short lane code |
| Category | `legend`, `boundary`, `lane`, `case`, `validation`, `hypothesis`, or `backlog` |
| Status | current state |
| Last evidence | `YYYY-MM-DD` |
| Owns | one sentence naming the doc's job |

## README Palette Pattern

When a README spans multiple colour lanes, include a linked SVG palette asset
instead of a Mermaid diagram.

Palette assets should:

- use small range-chip cards for each family
- derive chips from the current classifier or frozen source snapshot
- label the family and sample count
- avoid external palette branding, marks, or exact trade dress

## Style Rules

- Treat README docs as visual maps.
- Use charts as first-class doc structure, not decoration.
- Let charts, tables, or diagrams do the heavy lifting.
- Lead with a chart, table, or diagram.
- Use stacked bar charts for signal, progress, or pass/fail pressure.
- Use diagrams for flow.
- Use tables for inventories.
- Use prose only for interpretation.
- Use one or two bullets per prose section.
- Prefer one compact Mermaid diagram when a contrast or eval flow is the point.
