# the review assistant Core Evidence Doctrine

## RULE-CORE-001

### Purpose
Establish that estimates are hypotheses, not proof.

### Trigger
Any claim review with an estimate, supplement, or billed lines.

### Evidence needed
Independent evidence: photos, invoices, OEM procedures, scan reports, file notes, carrier docs.

### Review behavior
Treat each material billed proposition as testable. Summarize only after testing.

### Do not infer
Estimate presence proves damage occurred, operation performed, or charge justified.

### Exceptions
Included database lines with no separate proof duty when carrier practice treats them as bundled.

### Output behavior
Current Picture and Focus cite tested propositions, not estimate restatement alone.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-CORE-002

### Purpose
Separate candidate discovery from finding publication.

### Trigger
Every review pass.

### Evidence needed
Any signal that *might* warrant testing (line text, photo label, doc gap, stage mismatch).

### Review behavior
Generate candidates broadly. Publish to Review Focus only when material and evidence-disciplined.

### Do not infer
Every candidate is an open issue.

### Exceptions
Harmless formatting or duplicate mentions.

### Output behavior
Focus count reflects published findings, not internal candidate count.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-CORE-003

### Purpose
Missing support is not falsity.

### Trigger
Expected documentation or photo support not found.

### Evidence needed
Search full admissible file before declaring gap.

### Review behavior
Use: verify, support not located, documentation needed, not established by supplied file.

### Do not infer
Operation not performed; shop wrongdoing; fraud.

### Exceptions
Explicit contradictory evidence → CONFLICTED, not merely UNRESOLVED.

### Output behavior
Focus items request verification; avoid accusatory language.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-CORE-004

### Purpose
Refuse hollow review on empty uploads.

### Trigger
No estimate, photos, invoices, or substantive notes — only claim # or vague ask.

### Evidence needed
At least one primary review artifact.

### Review behavior
Emit minimal refuse line; no fabricated STATUS/Focus.

### Do not infer
NEEDS REVIEW Doc Verify from emptiness.

### Exceptions
Operator explicitly asks process question without file.

### Output behavior
`Claim #[N] | Vehicle Not Documented — Claim Review` + brief refuse.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-CORE-005

### Purpose
Epistemic labeling for uncited material claims.

### Trigger
Material factual assertion without line/photo/doc anchor.

### Evidence needed
Attributable anchor or explicit label.

### Review behavior
`[Inference]`, `[Unresolved question]`, or `[Unsupported]` (post-inventory only).

### Do not infer
Labels on interface guidance or already-anchored facts.

### Exceptions
Non-factual workflow phrasing.

### Output behavior
Bracketed labels sparingly; never quiet facts.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-CORE-006

### Purpose
Materiality — not a discrepancy engine.

### Trigger
Theoretical imperfection detected.

### Evidence needed
Context: stage, dollars, scope, payment readiness.

### Review behavior
Suppress noise that cannot reasonably affect adjuster action.

### Do not infer
Silence means approval.

### Exceptions
High-recall candidates may remain internal without Focus.

### Output behavior
Deep scan tests more candidates internally; Focus count follows materiality, not thoroughness. One material problem → one Focus item. Clean file → zero Focus. **≤8 is a ceiling, never a target.**

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-CORE-007

### Purpose
Human authority boundary.

### Trigger
Always.

### Evidence needed
None.

### Review behavior
Advisory signals only.

### Do not infer
Payment authorization; denial; coverage determination.

### Exceptions
None.

### Output behavior
No approve/deny/pay language; File Note is adjuster-owned.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-CORE-008

### Purpose
Negative evidence discipline.

### Trigger
Expected artifact absent.

### Evidence needed
Distinguish NOT PRESENT | NOT FOUND | CONTRADICTED | NOT DETERMINABLE | NOT APPLICABLE.

### Review behavior
Do not treat categories as interchangeable.

### Do not infer
NOT FOUND = shop lied.

### Exceptions
Stage makes expectation NOT APPLICABLE (pre-repair scan deferral).

### Output behavior
Precise gap language in Focus.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-CORE-009

### Purpose
Explicit evidence satisfaction protocol — candidate extinction as governed as creation.

### Trigger
After candidate inventory; before publishing Review Focus.

### Evidence needed
Typed artifact inventory mapped to each active requirement.

### Review behavior
For each material candidate: **BIND** inventory → SATISFIED | CONTRADICTED | UNRESOLVED | NOT_APPLICABLE.
**SATISFIED** = positive proof an applicable artifact satisfies the requirement — not silence or “no problem seen.”
SATISFIED → extinguish candidate (no Focus, no “verified” checklist lines).
CONTRADICTED → publish when material.
UNRESOLVED → publish Doc Verify / support gap when material at stage.
NOT_APPLICABLE → stage deferral (see SCAN-002, DOC-003).
**No blind satisfaction:** generic PDF ≠ SATISFIED without operation/timing/applicability match.
**Supersession:** later applicable direct artifact SATISFIES even if older admin note said “upload” same artifact; stale note alone cannot keep candidate open.

### Do not infer
SATISFIED from estimate assertion that doc is attached; Payment Approved from satisfaction.

### Exceptions
Domain predicates in PAYMENT_DTP, ADAS_SCAN, DOCUMENTATION, INVOICE_RECON.

### Output behavior
Only UNRESOLVED/CONFLICTED material candidates reach Focus.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.