# Failure Classification

| Run | Version | Case | Behavior | Classification |
|-----|---------|------|----------|----------------|
| dtp_absent run03 | v0.1 | EVAL-DTP-ABSENT | NO OPEN ITEMS; treated estimate "DTP secured" as sufficient without signed artifact | REASONING_MISS |
| sublet_present ×3 | v0.1 | EVAL-SUBLET-PRESENT | Invoice variance Focus ($925 vs $890) despite invoice attached | BENCHMARK_MISMATCH |
| sublet_present ×3 | v0.2 | EVAL-SUBLET-PRESENT | Same invoice variance Focus | BENCHMARK_MISMATCH |

No RETRIEVAL_MISS (full knowledge injection).

No OUTPUT_MISS identified (Focus matches reasoning).

Offline v0.2 contradiction case (CASE-11): CONTRADICTED preserves review — PASS in the reference satisfaction suite.
