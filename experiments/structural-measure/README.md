# Structural Measure — evidence-state experiment

24 model calls. One billed operation (structural set-up / measure) tested
across four evidence states:

| Case | Evidence state | Expected resolution |
|------|----------------|---------------------|
| STRUCT_MEASURE_ABSENT | absent | UNRESOLVED — publish the review item |
| STRUCT_MEASURE_PRESENT | present | SATISFIED — suppress it |
| STRUCT_MEASURE_WRONG_DOC | absent (an irrelevant document is supplied) | UNRESOLVED — publish |
| STRUCT_MEASURE_PREMATURE_STAGE | deferred (repair not yet complete) | NOT_APPLICABLE — neither publish nor suppress as a finding |

The wrong-document and premature-stage cells target two common governance
failure modes: treating an irrelevant document as support, and demanding
proof before the evidence could exist.

Corpus v0.2.1 vs v0.2.2: support-remediation wording variants; both score
identically on the reference run.

## Reference results (gpt-5.5, reasoning high)

24/24 correct on both corpus versions, 3/3 repeatability on every case.

## Reproduce

```bash
python scripts/validate_before_run.py
python scripts/run_experiment.py --adapter <dotted.path:callable> --model-label <label>
python scripts/score_experiment.py
```
