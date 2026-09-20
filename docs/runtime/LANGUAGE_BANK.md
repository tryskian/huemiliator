# Local Language Bank

The starter bank is a bundled, editable JSON resource:
[`src/huemiliator/data/language_bank.json`](../../src/huemiliator/data/language_bank.json).
Schema `huemiliator.language_bank.v1`, bank version `0.5.1`.

It supplies language for the next behaviour beta. The
[charter's character profile](../governance/CHARTER.md#character-profile) owns
Hugh's identity and voice. The author supplies six distinct appraisal adjectives,
two opening phrases, and the academic-flourish vocabulary recorded below.
Additional entries are assistant candidates awaiting behaviour evaluation.
Grammar, meaning, and usage annotations are assistant-authored.

## Inventory

| Role | Entries | Examples |
| --- | ---: | --- |
| Opening compliments | 21 | `a crowd pleaser!`, `that's a popular` |
| Appraisal words | 27 | `bold`, `lovely`, `sublime` |
| Modifiers | 11 | `rather`, `essentially`, `yet` |
| Appraisal phrases | 10 | `a certain elegance`, `a touch of distinction` |
| Aesthetic verdict cues | 16 | `just more satisfying`, `a quiet distinction` |
| Colour descriptions | 14 | the nine family labels, `the same colour`, `a new name` |
| Discourse phrases | 2 | `perhaps`, `indeed` |
| Function words | 2 | possessive `its`, interrogative `which` |
| Rhetorical phrases | 2 | `begs the question`, `surely` |
| Total language entries | 105 | 15 authorial references and 90 assistant candidates |

Fourteen connector records cover twelve words: `and`, `but`, `because`,
`although`, `therefore`, `however`, `yet`, `which`, `rather`, `essentially`,
`consequently`, and `nevertheless`. Separate senses of “but” and “yet” preserve
contrast and concession. Meanings, frames, and conditions are assistant-authored;
the source records identify the author's supplied words separately from the
additional candidate wording.

## Inspect It

```sh
huemiliator language-bank
huemiliator language-bank --format json
```

Text output groups wording by role and labels authorship. JSON output includes
the complete bank, meaning, grammar, usage conditions, slot bindings, and
provenance. Both commands load the packaged resource and validate its structure.
They work independently of the current directory, colour dataset, and eval DB.

The current `one-up` command continues to use its fixed family loss lines.
The separate [composer](COMPOSITION.md) now selects and adapts this material
through the configured model. The first behaviour pulse remains in staging.
Bank inspection neither generates a response nor assigns a behavioural verdict.

## Entry Contract

| Field | Meaning |
| --- | --- |
| `id` | stable identifier used in review and composition records |
| `role` | one of the nine inventory roles above |
| `text` | exact wording, optionally containing named fact slots |
| `grammar` | the entry's grammatical shape, including opening phrases |
| `meaning` | what the wording expresses |
| `requires` | IDs of usage conditions from the bank's condition registry |
| `source` | provenance record identifying human reference or assistant candidate |

For example, `appraisal.excellent` holds the author's adjective `excellent`,
links to the human source, and requires aesthetic appraisal plus grammatical
adjective attachment. The reference can apply across colour families.
`opening.popular_fragment` preserves `that's a popular` exactly, with a condition
requiring completion by a suitable noun or noun phrase. The repeated `lovely`
in the author's full list is represented once. Version `0.4.0` replaces the
five earlier full opening references with this material; the original quotations
remain in the character profile and historical requests retain their bank snapshot.

`verdict.just_more_satisfying` adapts the author's exact fragment “is just more
satisfying”; `opening.popular_one`, `opening.respectable_family`,
`opening.fine_choice`, `modifier.unequivocally`, and `verdict.finer` are
assistant candidates. Their wording, chronology, and saved-record context live
in the [local-language source history](../research/450_LOCAL_LANGUAGE.md);
[D-044](../governance/DECISIONS.md#d-044-hugh-delivers-aesthetic-verdicts-as-settled-fact)
owns the durable voice direction. Historical requests retain their bank
snapshots and meanings. The model chooses combinations; the bank does not
claim that any candidate has passed behaviour evaluation.

The declared slots bind to the existing behaviour fact packet:

| Slot | Fact field |
| --- | --- |
| `input_family` | `runtime_facts.family` |
| `replacement_name` | `runtime_facts.replacement.name` |

Slot names are the only interpolation form in this version. The composer
supplies their values alongside the entries; the model builds the response.
Version `0.3.0` limits language slots to the spoken colour references: the
chosen family and replacement Pantone name. The full fact packet still carries
hexes and input resolution for reasoning and inspection.

## Conditions and Connector Meaning

Conditions are named, human-readable requirements. They include:

- aesthetic appraisal and categorical, gracious verdicts
- particular input families
- equality or difference of the actual input and replacement hexes
- equality or difference of resolved swatch names
- grammatical attachment for individual words and phrases
- the supporting basis for a contrast, explanation, or concession

“Popular” and “crowd pleaser” retain the author's insinuation of basic taste.
The familiarity condition distinguishes that appraisal from a factual claim
about usage statistics. Literal colour comparisons require their corresponding
facts; this starter bank uses the supplied family labels and identity comparisons.
Hugh delivers aesthetic judgments with objective certainty. Where the input
and replacement have the same hex, any distinction must concern the choice
or naming while preserving the actual colour identity.

Connector records carry `id`, `word`, `relation`, `frame`, `meaning`, `requires`,
and `source`. Each expresses a reasoning relationship:

| Relationship | Wording | Supporting basis |
| --- | --- | --- |
| Addition | `and` | distinct related information |
| Contrast | `but`, `however`, `yet` | a relevant dimension of contrast |
| Explanation | `because` | why one idea explains or justifies the other |
| Concession | `although`, `but`, `yet`, `nevertheless` | an expectation and how the other idea holds despite it |
| Consequence | `therefore`, `consequently` | a premise and the inference to a conclusion |
| Elaboration | relative `which` | a clear antecedent and what the clause adds |
| Correction | `rather` | the formulation being sharpened or replaced |
| Restatement | `essentially` | an idea distilled with its meaning preserved |

Version `0.5.0` turns the 17 verdict clauses into phrases for Hugh to develop
in his own complete statement or rhetorical question. Earlier versions remain
in Git and their original composition records. Connector frames now describe
grammatical attachment, including independent clauses for semicolons.
Version `0.5.1` removes `verdict.finer_choice` ("the finer choice") at the
author's request. Original recorded responses retain their wording.

A question's implied claim belongs in the relationship annotation, with its supporting basis.
The model owns the complete sentence; these are meaning references, with room
for other grammatical constructions. The evaluator judges whether the expressed
relationship actually holds. The loader checks structural references only.

The author's wider flourish list also supplies language with other jobs:
`perhaps` qualifies a judgment, `its` has a possessive antecedent, and
`begs the question` introduces a connected question. `which` also has an
interrogative entry; `rather`, `essentially`, and `yet` also have modifier entries.
These lexical uses can occur without a two-idea connector relationship.
The response identifies that use through the corresponding language-entry ID.
The composer checks declared connectors for visible presence, while ambiguous
uses remain a semantic evaluation question. See the
[research note](../research/450_LOCAL_LANGUAGE.md#rhetorical-questions-and-academic-flourish)
for the author's list and the Probaboracle comparison.

## Extend and Check

1. Use the character profile to author a candidate with a distinct purpose.
2. Give it a stable ID, role, grammar, meaning, usage conditions, and source.
3. Preserve exact authorial references and label new wording as a candidate.
4. Update the bank version and this inventory when the content changes.
5. Run the bank checks and inspect the inventory:

```sh
PYTHONPATH=src .venv/bin/python -m pytest tests/test_language_bank.py
huemiliator language-bank
```

The validator rejects missing or unknown fields, duplicate IDs or wording within
a role, unknown source/condition references, and malformed or unsupported slots.
The tests also compare the authorial references with the charter and check colour
and connector conditions. Packaging includes the JSON resource in the wheel.

These checks establish that the bank can be loaded and inspected reliably.
Actual responses and assistant judgments in the aligned 15-minute pulses will
establish its behavioural quality.
