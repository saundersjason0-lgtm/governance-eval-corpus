# the review assistant Estimate Review

## RULE-EST-001

### Purpose
Domain isolation for estimate review mode.

### Trigger
Standard collision/comprehensive PD file review.

### Evidence needed
Estimate/supplement/photos/docs in session.

### Review behavior
Prioritize auto PD evidence. Dormant: injury, PIP, medical, liability, policy unless dependency shown.

### Do not infer
Irrelevant domains must be deleted from file.

### Exceptions
Explicit cross-domain fact in file (e.g., injury note affecting rental only if rental facts exist).

### Output behavior
No injury/PIP Focus from estimate-only review.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-EST-002

### Purpose
Default manual-line and billed-process proof pass.

### Trigger
Every estimate review — supplement-added, S03, manual, part-code, judgment lines.

### Evidence needed
Photos, invoices, sublet docs, OEM procedure, estimate notes, scan/cal docs appropriate to charge.

### Review behavior
Test each active nonstandard line. CCC profile audit is supplementary — not exhaustive issue list.

### Do not infer
Low-dollar lines suppressed by higher audit finding.

### Exceptions
Related operations may share one legitimate proof artifact.

### Output behavior
Line # in Focus; gap language: matching support not located in supplied evidence.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-EST-003

### Purpose
Proposition testing workflow.

### Trigger
Each material estimate line or workflow assertion.

### Evidence needed
Map proposition → expected support family → actual file inventory.

### Review behavior
SUPPORTED / CONFLICTED / UNRESOLVED / NOT_DETERMINABLE before surfacing.

### Do not infer
Summary equals review.

### Exceptions
Bundled INCL lines.

### Output behavior
Focus explains test result, not line description alone.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-EST-004

### Purpose
CCC audit / EIF economics as supplementary signal.

### Trigger
CCC profile audit, EIF, threshold language in dump.

### Evidence needed
Same CCC attach with threshold amount + % for ACV candidate.

### Review behavior
Audit findings do not replace manual-line proof pass. Do not treat audit as complete issue list.

### Do not infer
Audit silence means line supported.

### Exceptions
EIF/No A/M variant lines — surface when audit cites part (Knowledge: PARTS_LABOR).

### Output behavior
May inform economics; does not suppress separate proof gaps.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-EST-005

### Purpose
ACV / total-loss display discipline (simplified).

### Trigger
ACV, RTV, total loss risk in Snapshot.

### Evidence needed
Documented ACV source (file, Carfax, KBB, CCC audit attach with amount+%).

### Review behavior
Never invent 75% threshold. Never back-solve ACV from estimate÷threshold. Unresolved ACV alone ≠ Focus.

### Do not infer
Estimate total = ACV.

### Exceptions
Chat/document ACV update overrides stale CCC candidate.

### Output behavior
ACV line shows source; RTV/TL only when ACV resolved.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-EST-006

### Purpose
Active line state — deleted/superseded lines.

### Trigger
Estimate with revisions, supplements, zeroed lines.

### Evidence needed
Line active state in governing estimate.

### Review behavior
Do not test or Focus deleted/superseded lines.

### Do not infer
Historical lines still billed.

### Exceptions
None.

### Output behavior
Focus only active governing lines.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.