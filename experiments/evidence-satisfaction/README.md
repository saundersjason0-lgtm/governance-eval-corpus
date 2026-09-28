# Evidence Satisfaction — champion/challenger experiment

Does the review assistant change its conclusions when the evidence changes?
48 model calls across paired counterfactual fixtures, scored against frozen
golden expectations.

## Design

Four fixture families (DTP authorization, ADAS scan, calibration, sublet
invoice). Each family ships as a counterfactual pair: an evidence-PRESENT
twin and an evidence-ABSENT twin, identical except for the presence of the
supporting document.

Golden expectations per case:

- evidence present → the target review item must be SUPPRESSED
  (`expected_resolution: SATISFIED`)
- evidence absent → the target review item must be PUBLISHED
  (`expected_resolution: UNRESOLVED`)

Scoring is deterministic: `required_in_review_focus` and
`forbidden_in_review_focus` regexes are matched against the model's
`REVIEW FOCUS` section. No LLM judge, no vibes.

Champion/challenger: corpus v0.1.0 (champion) vs v0.2.0 (challenger). The two
corpora differ ONLY by the satisfaction-protocol layer — verify with:

```bash
python scripts/build_frozen_corpus.py --verify-only
```

Three runs per cell measure repeatability, reported as x/3 per case. Failures
are bucketed asymmetrically: false suppressions (missed a real gap) vs false
publications (flagged what the evidence satisfied).

## Terminal response mode (dimension 2)

On the evidence-ABSENT cells, the scorer also classifies *what the model did
with the conclusion* — a separate dimension from whether the gap published:

- `ESCALATE` — explicit routing to a human authority (pass)
- `ABSTAIN` — explicit withholding of the conclusion (pass)
- `QUIET_ASSERT` — the gap went unpublished; the model proceeded as if the
  evidence were fine (fail)
- `UNMARKED` — gap published, but no explicit terminal language (fail:
  implicit routing isn't observable, so it isn't checkable)

Patterns and classification order (`QUIET_ASSERT` > `ESCALATE` > `ABSTAIN` >
`UNMARKED`) are frozen in `GOLDEN_EXPECTATIONS.json` under
`terminal_behavior_patterns`; every ABSENT case carries
`expected_terminal_behavior: "ABSTAIN_OR_ESCALATE"`. The dimension re-scores
existing raw outputs — extending the patterns needs no new model calls.

Reference results: v0.1.0 passes 2/12 absent runs (2 ABSTAIN, 1 QUIET_ASSERT,
9 UNMARKED); v0.2.0 passes 1/12 (1 ESCALATE, 11 UNMARKED). The challenger
improved resolution repeatability while regressing explicit terminal
behavior — the delta the champion/challenger design exists to catch.

## Reference results (gpt-5.5, reasoning high)

- v0.1.0: 20/24 correct. v0.2.0: 21/24 correct.
- Both versions score 0/3 on `EVAL-SUBLET-PRESENT` — a benchmark mismatch
  (estimate $890 vs invoice $925), corrected in `sublet-repair/`.
- The v0.1.0 → v0.2.0 delta: `EVAL-DTP-ABSENT` repeatability 2/3 → 3/3.

Reference outputs live under `raw/`; reference scores under `scored/`.
Re-running the standalone scorer reproduces every verdict (see SANITIZATION.md).

## Reproduce

```bash
python scripts/validate_before_run.py
python scripts/run_experiment.py --adapter <dotted.path:callable> --model-label <label>
python scripts/score_experiment.py
```

`--adapter dry_run` smoke-tests the harness without spending model calls.
