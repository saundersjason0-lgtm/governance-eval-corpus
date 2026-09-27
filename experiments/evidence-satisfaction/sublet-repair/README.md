# Sublet Repair — benchmark correction

Measurement-only extension of the parent evidence-satisfaction experiment.
**Does not modify assistant behavior.**

## Why it exists

The original `EVAL-SUBLET-PRESENT` cell paired estimate Line 88 (**$890**)
with an invoice billing **$925**. Both corpus versions published an
invoice-variance review item — a **benchmark mismatch**, not an
evidence-satisfaction failure: the model was right to flag a real $35
variance.

This repair re-runs 12 calls against a clean counterfactual pair:

| Cell | Invoice |
|------|---------|
| PRESENT-CLEAN | `EVAL-SUBLET-MATCH-890` — Line 88 **$890**, invoice **$890** |
| ABSENT-CLEAN | no applicable invoice |

The original 48-call artifacts in `../` remain **immutable**.

## Run

```bash
python scripts/validate_before_run.py      # from the parent experiment
python scripts/run_experiment.py --fixtures-dir sublet-repair/fixtures
python sublet-repair/scripts/score_repair.py
```

Bring your own model adapter; see `../scripts/run_experiment.py --help`.
The reference repair ran 12 calls (gpt-5.5, reasoning high); outputs are
preserved under `raw/`.

## Artifacts

| Path | Role |
|------|------|
| `REPAIR_MANIFEST.json` | Repair metadata |
| `GOLDEN_EXPECTATIONS.json` | Frozen pre-run expectations |
| `FIXTURE_MATRIX.json` | Fixture registry |
| `PAIR_DIFF.md` | Pair-diff validation of the clean counterfactual |
| `invoices/` | Synthetic invoice PDF + preview for the MATCH-890 cell |
| `raw/` | Verbatim model outputs (reference run) |
| `scored/` | Reference-run telemetry and summaries |
