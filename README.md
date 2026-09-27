# governance-eval-corpus

Most benchmarks ask whether the model got the right answer. This one asks
whether it had any right to give one.

Governance failures rarely look like wrong answers. They look like authority
outrunning evidence: a fluent, confident finding the file doesn't support; a
conclusion that doesn't move when the evidence does; uncertainty quietly
collapsed into a verdict. This corpus measures those behaviors directly — in
auto physical-damage claim review, a narrow domain where they are checkable.

## The instrument

**Paired counterfactual fixtures.** Every test family ships as twins: an
evidence-PRESENT fixture and an evidence-ABSENT fixture, identical except for
the supporting document. The model can't pass by memorizing the fixture —
the twins demand opposite conclusions from near-identical inputs.

**Frozen goldens, no LLM judge.** Each case declares its expected resolution
before the run. Scoring is deterministic pattern matching against the model's
output. There is no LLM judge, and therefore no judge to flatter the model.

**Champion/challenger.** Two corpus versions differing by exactly one
documented change, so the eval measures the *delta*: did the change improve
governance behavior, and where?

**Repeat runs.** Three runs per cell, reported as x/3. A governance property
that holds one time in three is not a property.

## What it found

| Experiment | Runs | Result |
|---|---|---|
| Evidence satisfaction (v0.1.0 → v0.2.0) | 48 | correct rate 0.833 → **0.875** |
| Structural measure (v0.2.1, v0.2.2) | 24 | correct rate **1.0** / **1.0** |
| Sublet-repair correction pack | 12 | correct rate **1.0** / **1.0** |

Reference runs used gpt-5.5 at high reasoning; raw outputs and scores are
preserved in `raw/` and `scored/`. The harness itself is model-agnostic.

## Quickstart

```bash
cd experiments/evidence-satisfaction
python scripts/validate_before_run.py
python scripts/run_experiment.py --adapter dry_run --runs 1   # smoke test
python scripts/score_experiment.py
```

Bring your own model by implementing the adapter protocol documented in
`scripts/run_experiment.py`:

```python
adapter(system_prompt, user_prompt, run_tag) -> str
```

Standard library only. No dependencies to install, no API keys for the
smoke test.

## Do you need EAT to use this?

No. The harness is fixtures, an adapter protocol, and a deterministic
scorer — any model plugs in. EAT is the theory behind why the measurement
matters, not a prerequisite for running it.

Two things to know:

1. **The scorer grades an output contract.** It pattern-matches a
   `REVIEW FOCUS` section and counts epistemic markers (`[Inference]`,
   `[Unsupported]`, `[Unresolved question]`). Prompt your model into that
   format first — otherwise the scores measure formatting compliance,
   not evidence behavior.
2. **The goldens are single-rater**, calibrated on an EAT-lineage system.
   A differently architected assistant can be well-governed in ways this
   scorer can't see. This corpus measures what it measures; it doesn't
   certify anything.

## What's inside

```
experiments/
  evidence-satisfaction/     48-call champion/challenger experiment
    corpus/v0.1.0, v0.2.0    frozen behavioral corpora (assistant bundles)
    fixtures/                8 synthetic claim fixtures (4 present/absent pairs)
    scripts/                 validate → run → score (stdlib only)
    raw/, scored/            reference outputs + deterministic scores
    reports/                 analysis of the reference run
    sublet-repair/           12-call benchmark correction for the sublet cell
  structural-measure/        24-call evidence-state experiment
EVAL_DESIGN.md               the full methodology
SANITIZATION.md              what was scrubbed, renamed, and rewritten — and why
```

## Why this exists

Section 5 of Microsoft's draft Humanist AI Code of Conduct admits its
evaluation coverage is incomplete. This corpus is a concrete, runnable answer
to that gap: an instrument for testing whether an assistant's conclusions stay
within its evidence, mapped to §§2.4, 3.3, and 5 in `EVAL_DESIGN.md`. It was
built to be used — run it against your own models, break it, improve it.

## Limitations

Synthetic fixtures in one narrow domain. Single-rater goldens (the corpus
author). One reference model. No independent annotation study. This is not a
safety benchmark, and it doesn't certify compliance with anything. It measures
three governance behaviors, repeatably, and shows its work.

## License

MIT. An independent research artifact by Jason Saunders.
