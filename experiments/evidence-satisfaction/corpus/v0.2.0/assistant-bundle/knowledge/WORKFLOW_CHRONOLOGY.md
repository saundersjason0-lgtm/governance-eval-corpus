# the review assistant Workflow & Chronology

## RULE-FLOW-001

### Purpose
Operational stage from evidence.

### Trigger
Any review with workflow cues.

### Evidence needed
Claim history, supplements, repair dates, payment docs, adjuster notes.

### Review behavior
Stage: Initial Estimate | In Repair | Repair Complete | Payment Review | etc. from file — not prior File Note stamps.

### Do not infer
Stage from CCC audit alone when contradicting shop docs.

### Exceptions
Explicit stage in ECC/CCC print when no conflict.

### Output behavior
Stage on Snapshot line.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-FLOW-002

### Purpose
Current Picture continuity states.

### Trigger
Estimate, photos, notes, chronology together.

### Evidence needed
Cross-artifact alignment.

### Review behavior
ALIGNED | REVIEW | OUT OF SEQUENCE | MATERIAL MISMATCH — plain reason below.

### Do not infer
Current Picture equals STATUS.

### Exceptions
REVIEW for mild chronology without material mismatch.

### Output behavior
Dedicated Current Picture section with evidence sentence.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-FLOW-003

### Purpose
Anchor fence — no seeding from stale stamps.

### Trigger
Every turn.

### Evidence needed
Current upload + current chat only.

### Review behavior
Re-resolve Payment, ACV, STATUS, Focus from current dump. Ignore PRIOR-ANCHOR / v= stamps in file notes.

### Do not infer
Prior File Note overrides current evidence.

### Exceptions
None.

### Output behavior
File Note prose only — no continuity stamps.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-FLOW-004

### Purpose
In Repair rental isolation.

### Trigger
In Repair stage with rental extension or missing rental bill.

### Evidence needed
Rental facts in file.

### Review behavior
Rental Status line only; STATUS NO OPEN ITEMS; Focus 0 for rental-only gaps.

### Do not infer
Rental doc gap = NEEDS REVIEW whole claim.

### Exceptions
Non-rental material issues still Focus.

### Output behavior
Rental Status section when facts exist.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-FLOW-005

### Purpose
STATUS authority (simplified).

### Trigger
Publishing STATUS line.

### Evidence needed
Focus severity, RTV band, qualified ACV.

### Review behavior
CRITICAL only for TL economics ≥70% with ACV — not doc gaps. Doc/scan/sublet alone → ≤ NEEDS REVIEW.

### Do not infer
NEEDS REVIEW = payment hold.

### Exceptions
Evidence Conflict at payment may be NEEDS REVIEW not CRITICAL.

### Output behavior
Single STATUS token matching rules.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.