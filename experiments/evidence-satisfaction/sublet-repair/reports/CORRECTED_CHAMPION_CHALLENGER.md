# Corrected Champion / Challenger Interpretation

## VIEW 1 — Original 48-call experiment (immutable)

### v0.1.0
- present_false_publication_rate: 25.00%
- absent_catch_rate: 91.67%
- sublet_present repeatability: 0/3

### v0.2.0
- present_false_publication_rate: 25.00%
- absent_catch_rate: 100.00%
- sublet_present repeatability: 0/3

## VIEW 2 — Decontaminated benchmark (DTP+Scan+Cal original + repaired Sublet)
### v0.1.0
- present_false_publication_rate: 0.00%
- absent_catch_rate: 91.67%
- paired_discrimination (sublet repair only): 3/3
- confusion: TS=12 FP=None TP=11 FS=1

### v0.2.0
- present_false_publication_rate: 0.00%
- absent_catch_rate: 100.00%
- paired_discrimination (sublet repair only): 3/3
- confusion: TS=12 FP=None TP=12 FS=None

## Decision: A — PROMOTE_V0_2 (narrow DTP robustness; ceiling-equivalent elsewhere)

Rationale:
- Original sublet_present was BENCHMARK_MISMATCH ($925 invoice vs $890 estimate).
- Repaired sublet v0.1 paired: 3/3
- Repaired sublet v0.2 paired: 3/3
- Corrected absent catch v0.1: 91.67% v0.2: 100.00%
- Corrected present FP rate v0.1: 0.00% v0.2: 0.00%
