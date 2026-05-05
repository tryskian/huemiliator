# Research

Huemiliator keeps the tracked research lane small on purpose.

The repo is in contract-lock stage. No runtime evidence exists yet.

Raw notes and private scratch material stay in the local `docs/peanut/` lane.

## Current Phase

Current phase:

- `pre-beta`
- `contract lock`

Current question:

Can a closed picker input support deterministic Pantone resolution and a stable
same-family one-up rule?

Current finding:

- the repo baseline is set
- the input surface is locked to the native colour picker for v1
- the canonical inventory source is locked to the Pantone repo surface
- family assignment and same-family rank remain to be defined
- no runtime evidence has been produced yet

## Next Research Move

The first meaningful runtime kernel should prove:

- hex ingestion
- nearest Pantone resolution
- explicit family assignment
- deterministic one-up in the same family

That first evidence lane should stay binary:

- `pass`
- `fail`

## Plans

Plans are useful, but they are not evidence.

Current planned sequence:

1. freeze the Pantone dataset into the repo
2. define the first family taxonomy
3. define the same-family ranking rule
4. implement the narrow runtime path
5. add PASS/FAIL evaluation for matching and transform correctness

## Probaboracle And Scorey Context

Huemiliator belongs to the same toy line, but its progression is different:

- `probaboracle`: closed prompt surface to reasoned generation
- `scorey`: closed prompt surface to deterministic routing plus reasoned fragments
- `huemiliator`: open colour selection to deterministic resolution plus deterministic transform
