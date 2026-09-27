# the review assistant Documentation Sufficiency

## RULE-DOC-001

### Purpose
Documentation verification Focus items.

### Trigger
Material billed doc-dependent operation without matching document.

### Evidence needed
Sublet invoice, tow bill, OEM procedure, scan report, teardown report, structural measurement / frame sheet when structural set-up/measure billed.

### Review behavior
Category: Doc Verify / Documentation Verification in Focus.

### Do not infer
Doc gap = CRITICAL STATUS alone.

### Exceptions
Stage not yet due (see ADAS_SCAN-002).

### Output behavior
STATUS ≤ NEEDS REVIEW for doc gaps; never CRITICAL from doc alone.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-DOC-002

### Purpose
Sublet proof at payment.

### Trigger
Frame, mechanical sublet, specialty lines without invoice.

### Evidence needed
Sublet invoice or carrier-accepted equivalent.

### Review behavior
Test at payment review when repair complete.

### Do not infer
Estimate line proves sublet performed.

### Exceptions
Sublet photo may support scope but not invoice amount.

### Output behavior
Line # + invoice gap in Focus.

### Satisfaction predicate
Sublet invoice (or carrier equivalent) matching billed sublet vendor/operation → SATISFIED. Sublet line on estimate alone → UNRESOLVED. Sublet photo supports scope but does not satisfy invoice requirement.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-DOC-003

### Purpose
Teardown / four-corner deferral.

### Trigger
Missing teardown or four-corner photos on active repair.

### Evidence needed
Stage and shop practice.

### Review behavior
Pre-complete → File Note not-yet-due; not default Focus.

### Do not infer
Never needed.

### Exceptions
Payment dispute on teardown scope.

### Output behavior
File Note for not-yet-due items.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.