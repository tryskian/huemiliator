# Live Eval Workflow

This is the next-beta operating flow established by `D-036`. It changes the
eval pulse to a 15-minute live run with immediate binary verdicts. It does not
change Huey's deterministic runtime or invalidate the existing evidence
archive.

The alignment gate is deliberate. Choosing the question, source selection, and
cadence is a human-led decision before a pulse opens, not a decision made by
the diagram or sampler.

```mermaid
flowchart TD
  A["make start"]
  B["read governing docs and current evidence"]
  C["confirm feature branch, proof-surface status, and pending = 0"]
  D["select one bounded family lane or exact cohort"]
  E["align question, source selection, and cadence"]
  F{"human lead gives GO?"}
  G["stop: no live pulse opens"]
  H["archive the prior live proof surface"]
  I["start the 15-minute timer"]
  J["sample the next selected input"]
  K["resolve fixed runtime facts"]
  L["read the visible Huey output"]
  M["Huey applies the accepted judgement lens"]
  N["record PASS or FAIL immediately\nwith a concise fact-specific note"]
  O["append the ordered verdict to the live signal"]
  P{"15 minutes elapsed?"}
  Q["stop sampling and confirm pending = 0"]
  R["preserve rows, verdict order, and notes"]
  S["share facts, observations, and uncertainty"]
  T{"does the evidence support a narrow adjustment?"}
  U["propose the next adjustment for GO or NO-GO"]
  V["update research notes and diagrams with actual evidence"]
  W["validate, commit, PR, merge, and make end"]

  A --> B --> C --> D --> E --> F
  F -->|no| G
  F -->|yes| H --> I --> J --> K --> L --> M --> N --> O --> P
  P -->|no| J
  P -->|yes| Q --> R --> S --> T
  T -->|no| V
  T -->|yes| U --> V --> W

  classDef action fill:#d8f3dc,stroke:#2d6a4f,color:#1b4332
  classDef gate fill:#fff3bf,stroke:#b7791f,color:#744210
  classDef stop fill:#f3f4f6,stroke:#6b7280,color:#374151
  class A,B,C,D,E,H,I,J,K,L,M,N,O,Q,R,S,U,V,W action
  class F,P,T gate
  class G stop
```

## Method Boundaries

- The run lasts exactly `15` minutes.
- Every evaluation receives `PASS` or `FAIL` while the pulse is live.
- Verdict order is the live signal. It is preserved before interpretation.
- `retain`, `evict`, and legacy pulse labels are not verdicts or evidence
  labels for this method.
- Huey records verdicts by applying the human lead's established judgement
  standard. The human lead owns the research question, acceptance criteria,
  and GO or NO-GO decisions.
- Existing completed evals remain historical evidence. A live pulse changes
  neither the archive nor Huey's deterministic colour runtime.

## Authority

- [Charter](../governance/CHARTER.md): runtime rules, evidence handling, and
  human-lead ownership.
- [D-036](../governance/DECISIONS.md): 15-minute live `PASS`/`FAIL` method.
- [Architecture](../runtime/ARCHITECTURE.md): fixed facts before visible-output
  evaluation.
