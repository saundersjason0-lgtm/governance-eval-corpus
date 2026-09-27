# Corpus Provenance

Traceability from the author's prior review-assistant iterations to the knowledge rules in corpus `v0.2.2`.

| Rule ID | Domain | Problem addressed | Regression fixture | Implementation | Rationale | Status |
|---------|--------|-------------------|--------------------|----------------|-----------|--------|
| RULE-CORE-001 | core | Estimate treated as proof | SYN-CAUS-* | CORE_EVIDENCE.md | Core thesis | MIGRATED |
| RULE-CORE-002 | core | Candidate flood in Focus | review_focus_intent harness | CORE_EVIDENCE.md | Candidate≠finding | MIGRATED |
| RULE-CORE-003 | core | "Not performed" language | manual_line_proof fixtures | CORE_EVIDENCE.md | Support gap discipline | MIGRATED |
| RULE-CORE-004 | core | Fake review on empty upload | SYN-SVP-EMPTY-01 | CORE_EVIDENCE.md | Refuse hollow review | MIGRATED |
| RULE-CORE-005 | core | Quiet facts | EAL-001–010 | CORE_EVIDENCE.md + INSTRUCTIONS | Epistemic labels | MIGRATED |
| RULE-CORE-006 | core | Discrepancy engine | future_materiality harness | CORE_EVIDENCE.md | Materiality | SIMPLIFIED |
| RULE-CORE-007 | core | Authority creep | payment_provenance | CORE_EVIDENCE.md | Human authority | MIGRATED |
| RULE-CORE-008 | core | NOT FOUND = fraud tone | support_routing harness | CORE_EVIDENCE.md | Negative evidence | MIGRATED |
| RULE-CORE-009 | core | Candidate extinction semantic | satisfaction cases | CORE_EVIDENCE.md | Satisfaction protocol | NEW |
| RULE-EST-001 | estimate | Injury/PIP noise | SYN-GOV-* | ESTIMATE_REVIEW.md | Domain isolation | MIGRATED |
| RULE-EST-002 | estimate | Manual lines suppressed | s03_letdown_nib_* | ESTIMATE_REVIEW.md | Default proof pass | MIGRATED |
| RULE-EST-003 | estimate | Summary not review | SYN-ADV-* | ESTIMATE_REVIEW.md | Proposition testing | SIMPLIFIED |
| RULE-EST-004 | estimate | Audit exhaustive | ccc_audit_not_exhaustive | ESTIMATE_REVIEW.md | Audit supplementary | MIGRATED |
| RULE-EST-005 | estimate | Invent 75%, waffle | SYN-ACV-AUDIT-01, ADR-A | ESTIMATE_REVIEW.md | ACV discipline | SIMPLIFIED |
| RULE-EST-006 | estimate | Deleted line Focus | active_state harness | ESTIMATE_REVIEW.md | Active lines only | MIGRATED |
| RULE-EST-007 | estimate | Billed set-up/measure, no sheet | structural_measure fixtures | ESTIMATE_REVIEW.md | Measurement sheet at completion | NEW |
| RULE-PHOTO-001 | photo | Zone mismatch missed | SYN-COMPLEX-PAY-01 | PHOTO_DAMAGE.md | Line-photo tension | MIGRATED |
| RULE-PHOTO-002 | photo | Process proof gaps | manual_line_proof, SYN-VOCAB-DENIB | PHOTO_DAMAGE.md | Refinish proof | MIGRATED |
| RULE-PHOTO-003 | photo | Photo Summary bloat | ux_canonical | PHOTO_DAMAGE.md | Focus label quotes | MIGRATED |
| RULE-PHOTO-004 | photo | STATUS before coverage | refinish_photo_proof | PHOTO_DAMAGE.md | Coverage ordering | SIMPLIFIED |
| RULE-PART-001 | parts | Part code silent pass | part_code harness | PARTS_LABOR.md | Part code proof | MIGRATED |
| RULE-PART-002 | parts | Unsupported ops | part_code_unsupported_ops | PARTS_LABOR.md | Unsupported ops | MIGRATED |
| RULE-PART-003 | parts | EIF audit miss | SYN-AUTO-EIF-* | PARTS_LABOR.md | EIF variants | MIGRATED |
| RULE-PART-004 | parts | CAPA duplicate noise | CCC audit cases | PARTS_LABOR.md | CAPA silence | MIGRATED |
| RULE-SCAN-001 | adas | Scan Focus pre-pay | SYN-PAY-SCAN-02 | ADAS_SCAN.md | Stage-gated scan | MIGRATED |
| RULE-SCAN-002 | adas | Pre-pay scan noise | SYN-EST-SCAN-01 | ADAS_SCAN.md | Deferral | MIGRATED |
| RULE-SCAN-003 | adas | Cal invoice variance | SYN-INV-VAR-CAL-01 | ADAS_SCAN.md | Cal doc test | MIGRATED |
| RULE-DOC-001 | documentation | Doc→CRITICAL | gpt55_status_metrics | DOCUMENTATION.md | STATUS cap | MIGRATED |
| RULE-DOC-002 | documentation | Sublet invoice gap | SYN-COMPLEX-PAY-01 | DOCUMENTATION.md | Sublet at pay | MIGRATED |
| RULE-DOC-003 | documentation | Teardown pre-focus | future_materiality | DOCUMENTATION.md | Deferral | SIMPLIFIED |
| RULE-PAY-001 | payment | Approved invented | SYN-BEACON-PAY-01 | PAYMENT_DTP.md | Provenance ladder | MIGRATED |
| RULE-PAY-002 | payment | DTP buried | SYN-BEACON-DTP-GAP-01 | PAYMENT_DTP.md | DTP gap Focus | MIGRATED |
| RULE-PAY-003 | payment | Audit MFB pending | SYN-BEACON-MFB-01 | PAYMENT_DTP.md | Ignore audit MFB | MIGRATED |
| RULE-PAY-004 | payment | Payment noise Focus | SYN-CLEAN-* | PAYMENT_DTP.md | Not Evidenced OK | MIGRATED |
| RULE-PAY-005 | payment | Reserve talk | reserve_suppression | PAYMENT_DTP.md | Reserve ban | MIGRATED |
| RULE-INV-001 | invoice | Invoice drift | SYN-INV-MATCH-01 | INVOICE_RECON.md | Total match | MIGRATED |
| RULE-INV-002 | invoice | Invoice without report | SYN-INV-VAR-SCAN-01 | INVOICE_RECON.md | Linked scan test | MIGRATED |
| RULE-INV-003 | invoice | Sublet invoice gap | SYN-INV-SUBLET-02 | INVOICE_RECON.md | Sublet recon | MIGRATED |
| RULE-FLOW-001 | workflow | Wrong stage | stage_engine | WORKFLOW_CHRONOLOGY.md | Stage evidence | SIMPLIFIED |
| RULE-FLOW-002 | workflow | Story mismatch | SYN-COMPLEX-PAY-01 | WORKFLOW_CHRONOLOGY.md | Current Picture | MIGRATED |
| RULE-FLOW-003 | workflow | Stale stamp seed | anchor_deficit | WORKFLOW_CHRONOLOGY.md | Re-resolve | MIGRATED |
| RULE-FLOW-004 | workflow | Rental over-flag | SYN-RENTAL-EXT-01 | WORKFLOW_CHRONOLOGY.md | Rental isolation | MIGRATED |
| RULE-FLOW-005 | workflow | TL STATUS drift | SYN-TL-REVIEW-01 | WORKFLOW_CHRONOLOGY.md | STATUS bind | MIGRATED |

## Summary counts (v0.2.2)

| Status | Count |
|--------|-------|
| MIGRATED | 32 |
| SIMPLIFIED | 6 |
| NEW | 1 |
| DEFERRED | 6 |
| REJECTED | 4 |
| **Concepts reviewed** | **48** |
| **Knowledge RULE IDs** | **43** |

Note: the source matrix's product-internal columns (originating system, internal version) are intentionally omitted. Rules are retained on regression-fixture evidence: each rule traces to a synthetic fixture that exercises it.
