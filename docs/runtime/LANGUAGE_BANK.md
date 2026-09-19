# Local Language Bank

The starter bank is a bundled, editable JSON resource:
[`src/huemiliator/data/language_bank.json`](../../src/huemiliator/data/language_bank.json).
Schema `huemiliator.language_bank.v1`, bank version `0.3.0`.

It supplies language for the next behaviour beta. The
[charter's character profile](../governance/CHARTER.md#character-profile) owns
Hugh's identity and voice. His five authorial openings are preserved verbatim;
additional entries are assistant candidates awaiting behaviour evaluation.

## Inventory

| Role | Entries | Examples |
| --- | ---: | --- |
| Opening compliments | 24 | `excellent red...`, `a most agreeable choice...` |
| Appraisal words | 24 | `lovely`, `refined`, `discerning` |
| Modifiers | 9 | `rather`, `quite`, `decidedly` |
| Appraisal phrases | 10 | `a certain elegance`, `a touch of distinction` |
| Aesthetic verdicts | 17 | `{replacement_name} is just more satisfying`, `{replacement_name} has a quiet distinction` |
| Colour descriptions | 14 | the nine family labels, `the same colour`, `a new name` |
| Total language entries | 98 | five authorial references and 93 assistant candidates |

Five connector records cover four words: `and.addition`, `but.contrast`,
`but.concession`, `because.explanation`, and `although.concession`.
Separate senses of “but” preserve the difference between a contrast and a
defeated expectation.

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
| `id` | stable identifier used in review and future composition records |
| `role` | one of the six inventory roles above |
| `text` | exact wording, optionally containing named fact slots |
| `grammar` | the entry's grammatical shape, including opening phrases |
| `meaning` | what the wording expresses |
| `requires` | IDs of usage conditions from the bank's condition registry |
| `source` | provenance record identifying human reference or assistant candidate |

For example, `opening.excellent_red` retains `excellent red...`, links to the
human source, and requires the red family plus aesthetic appraisal. The
`verdict.just_more_satisfying` template asserts aesthetic superiority after the
opening compliment, with the chosen name bound to the supplied replacement.
It is an assistant adaptation of the author's exact fragment “is just more
satisfying”. All seventeen verdict templates remain labelled as assistant
candidates. Version `0.2.0` replaces the former `preference.*` entries with new
`verdict.*` IDs; saved requests retain their original bank and meanings.
The new `opening.popular_one` adapts the author's worked line to pair “a popular
one” with “the finer choice”. The full line is preserved in the
[character profile](../governance/CHARTER.md#character-profile); the bank's
adapted opening is labelled as an assistant candidate. The author supplied
the line to illustrate structure and rhythm; the model chooses its own wording
from the available material.
`opening.respectable_family` adapts the author's “A respectable red...” to the
mapped input family. It replaces the earlier “a most respectable choice...”
after the author identified the resulting opening as awkward.
The intellectual-voice example adds `opening.fine_choice`,
`modifier.unequivocally`, and `verdict.finer` as separate resources. Their
combination remains the model's choice; the complete authorial line is a voice
reference, and deliberate echoes such as “fine / finer” remain available.

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
and `source`. In `A because B`, the registered condition requires a basis for
why B explains A. In `Although A, B`, it requires the expectation raised by A,
its source, and how B holds despite it. Those relationships are defined for the
composer and evaluator; the loader checks references, not their truth for a
particular input.

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
The tests also compare the authorial openings with the charter and check colour
and connector conditions. Packaging includes the JSON resource in the wheel.

These checks establish that the bank can be loaded and inspected reliably.
Actual responses and assistant judgments in the aligned 15-minute pulses will
establish its behavioural quality.
