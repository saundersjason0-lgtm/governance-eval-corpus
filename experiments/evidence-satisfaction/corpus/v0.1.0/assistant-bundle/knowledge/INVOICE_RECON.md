# the review assistant Invoice Reconciliation

## RULE-INV-001

### Purpose
Invoice total vs estimate alignment.

### Trigger
Shop invoice/final bill in file with estimate total.

### Evidence needed
Invoice PDF/image, estimate total, line mapping when available.

### Review behavior
Test match, under, over, mixed variance patterns.

### Do not infer
Invoice present = payment approved.

### Exceptions
Partial supplements not yet on invoice.

### Output behavior
Focus on material variance; cite invoice + estimate anchors.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-INV-002

### Purpose
Scan/cal line on invoice without report.

### Trigger
Invoice lists scan/cal charge; report absent.

### Evidence needed
Invoice line + documentation set.

### Review behavior
Link to RULE-SCAN-001 proposition test.

### Do not infer
Invoice line proves scan completed.

### Exceptions
Invoice is the report (some carriers).

### Output behavior
Doc Verify with invoice line ref.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-INV-003

### Purpose
Sublet invoice vs estimate sublet line.

### Trigger
Sublet on estimate; invoice in or missing from file.

### Evidence needed
Matching vendor invoice.

### Review behavior
Amount and scope proposition test.

### Do not infer
Photo of area replaces invoice.

### Exceptions
Combined invoice for multiple lines.

### Output behavior
Focus with line # and invoice status.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.