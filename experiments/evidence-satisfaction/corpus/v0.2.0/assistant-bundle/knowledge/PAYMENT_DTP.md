# the review assistant Payment & DTP

## RULE-PAY-001

### Purpose
Payment provenance — highest proven state only.

### Trigger
Claim Snapshot payment line.

### Evidence needed
Shop final bill, DTP secured note, Tri Star requested, STP issuance proof.

### Review behavior
Never Payment: Approved without explicit approval-for-payment proof. APPROVED ≠ ISSUED.

### Do not infer
Final bill = approved payment.

### Exceptions
Final Bill/Auth Present is workflow posture, not approval.

### Output behavior
Snapshot Payment: Requested | Pending Verification | Final Bill/Auth Present | Issued via STP | Not Evidenced.

### Satisfaction predicate
Applicable signed DTP / authorization artifact in inventory that establishes authorization for current payment posture → SATISFIED for signed-authorization documentation candidates. Estimate “DTP attached” language alone → UNRESOLVED. Payment Requested ≠ Payment Approved ≠ Issued.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-PAY-002

### Purpose
DTP photo without estimate trigger note.

### Trigger
DTP photo/PDF in file; estimate lacks Final Bill / DTP secured / Direction To Pay properties.

### Evidence needed
Visual DTP doc + estimate properties panel.

### Review behavior
Doc Verify Focus required; STATUS ≤ NEEDS REVIEW; never bury in Take/File Note only.

### Do not infer
CCC Audit Payment Requested = DTP trigger.

### Exceptions
None.

### Output behavior
Explicit Doc Verify Focus for auto-pay trigger gap.

### Satisfaction predicate
Estimate properties show Final Bill, DTP secured, or Direction To Pay trigger note → SATISFIED for autopay-gap candidate. DTP photo alone without trigger note → UNRESOLVED for this candidate (distinct from signed-authorization satisfaction).

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-PAY-003

### Purpose
CCC print Missing Final Bill ignore.

### Trigger
CCC audit/print shows Missing Final Bill.

### Evidence needed
CCC print/audit MFB vs shop final bill in file.

### Review behavior
Always ignore audit MFB for Snapshot Payment — never Pending from audit alone.

### Do not infer
No final bill needed when shop bill present.

### Exceptions
No DTP-photo exception elevating audit MFB.

### Output behavior
Use shop final bill posture when proven.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-PAY-004

### Purpose
Missing payment alone not Focus.

### Trigger
No payment evidence in file.

### Evidence needed
Absence of payment docs.

### Review behavior
Not Evidenced on Snapshot — not automatic Focus item.

### Do not infer
Payment blocked.

### Exceptions
Payment review stage with explicit payment workflow ask.

### Output behavior
Snapshot line only unless other material issues exist.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-PAY-005

### Purpose
Reserve / indemnity silence.

### Trigger
Reserve vs estimate chatter.

### Evidence needed
None.

### Review behavior
Do not discuss indemnity/exposure reserve. Rental RESERVED lifecycle OK.

### Do not infer
Reserve adequacy.

### Exceptions
None.

### Output behavior
No reserve recommendations.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.