# Hugh's Language Composer

`huemiliator compose <hex>` uses the fixed colour result and local language bank
to generate Hugh's visible response through the OpenAI Responses API. Composer
version `0.2.0` is an implemented staging surface. Its responses await behaviour
evaluation in the aligned 15-minute pulses.

## Setup and Use

The tracked [`.env.example`](../../.env.example) documents the key, model, and reasoning settings.
For a fresh setup, copy it to `.env` and add Hugh's key. The `.env` file stays
ignored by Git. It uses the same small configuration shape as Scorey:

```dotenv
OPENAI_API_KEY=your-key
HUEMILIATOR_MODEL=gpt-5.6-luna
HUEMILIATOR_REASONING_EFFORT=medium
```

An exported variable takes precedence over `.env`. An absent or blank model
setting uses `gpt-5.6-luna`; reasoning defaults to `medium` and is sent explicitly
as `reasoning.effort` in the API request. The current Luna model accepts `none`,
`low`, `medium`, `high`, `xhigh`, and `max`, as documented in the
[model reference](https://developers.openai.com/api/docs/models/gpt-5.6-luna).
Both settings appear in the dry-run and saved request. Model suitability remains
a behaviour-evaluation question. The bank and colour engine are local, while live
composition sends the supplied colour facts and language material to OpenAI.

```sh
huemiliator compose '#d9a6a1' --dry-run
huemiliator compose '#d9a6a1'
huemiliator compose '#d9a6a1' --format json
```

Dry-run prints the exact request packet as JSON and needs no API key. Text mode
prints the visible response after mechanical checks. JSON mode prints the full
inspection record. Standard output can be redirected to a chosen local file.
The command does not create files or modify the colour eval database.

## Selection and Composition

1. The existing colour pipeline selects the replacement deterministically.
2. Code filters bank entries by the actual input family, input/replacement hex
   equality, and resolved input/replacement name equality.
3. The request supplies the remaining entries, their meanings and conditions,
   slot values, connector senses, colour facts, and a single picker interaction.
4. The model selects and adapts wording under the five positive directions in
   [PB_BEHAVIOUR](../research/030_PB_BEHAVIOUR.md#instructions-and-judgment-lens).
5. It returns a complete line, the IDs of entries it reports using, and brief
   relationship descriptions identifying the claims and supporting basis.

The five directions are the complete `instructions` field. Entry conditions
are language data. Semantic conditions such as familiarity, explanatory support,
and an expectation behind a concession remain for the model to apply and the
evaluator to judge. The code supplies no random phrase selector or sentence
template. The model can adapt entries to fit its sentence.

The current `one-up`, `behaviour-facts`, and historical colour eval commands
retain their fixed family lines and contracts. Those lines and old response
instructions are omitted from the composition request. The replacement itself
is the same result from the same colour engine.

## Inspection Record

The `huemiliator.composition_record.v1` JSON contains:

- the exact API request, including instructions, facts, context, supplied bank
  entries, and output schema
- composer, instruction, and bank versions, plus bank and request hashes
- request start and completion timestamps
- API response ID, returned model, status, usage, and incomplete/refusal details
- the original output text and parsed composition
- mechanical issues and a `behaviour_verdict` of `null`

The bank hash covers the complete validated bank; the request includes the
filtered snapshot actually supplied. Hashes use canonical JSON with sorted keys,
compact separators, UTF-8, and unescaped Unicode. The request hash covers
`api_request`. These records identify what ran; they do not promise repeatable
model output.

Entry references and relationship descriptions are model-reported annotations
of its visible response. They are evidence to inspect, not independently
verified provenance or internal reasoning traces. For concession, the basis
field identifies an expectation and its source. The evaluator still checks
whether that expectation and the claimed relationship are supported.

## Mechanical Checks and Failures

Checks cover output shape, eligible entry IDs, an opening reference, the supplied
replacement name and hex, additional hexes, and connector records. They verify
that each of the four bank connector words appearing in the line has a record,
and that each recorded word appears in the line. They do not prove grammar,
voice, factual meaning, or fidelity of the model's annotations.

An incomplete response, refusal, malformed JSON, or failed mechanical check
retains its original output in the record. The command returns exit `2`, writes
the full JSON record to stdout even in text mode, and explains the issue on
stderr. Successful mechanical checks return exit `0`; neither status supplies a
behavioural PASS or FAIL. Configuration, input, or API failures return exit `1`.
API errors identify the error type and HTTP status without echoing provider text.

Each invocation makes one API attempt, with a 60-second request timeout and a
8,192-token output budget, including any model reasoning tokens. Automatic
retries and output repair are absent so a failed candidate remains observable.
`store=false` is set on the request. The implementation follows OpenAI's
[Structured Outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs).

## Next Method Step

The pulse still needs aligned case selection, timing, judgment criteria, and a
pulse-wide verdict rule. Composer smoke checks establish connectivity and the
recording path. The first completed 15-minute behaviour pulse will establish
the new behavioural evidence surface.
