# the review assistant ADAS Scan & Calibration

## RULE-SCAN-001

### Purpose
Scan/calibration billed vs report present.

### Trigger
Pre/Post scan or calibration lines on estimate at payment/repair-complete.

### Evidence needed
Scan report, calibration report, or matching invoice in file.

### Review behavior
At Payment Review / Repair Complete: missing report → Doc Verify Focus. Pre-pay: defer to File Note.

### Do not infer
Scan performed because line exists.

### Exceptions
OEM states scan required — still needs report at payment stage.

### Output behavior
Line # + report gap in Focus when stage due.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-SCAN-002

### Purpose
Pre-pay scan report deferral.

### Trigger
Estimate stage; scan billed; report absent.

### Evidence needed
Stage before payment/repair complete.

### Review behavior
Note in File Note — not pre-pay Focus for report alone.

### Do not infer
Scan will never be needed.

### Exceptions
Carrier requires pre-authorization scan proof.

### Output behavior
Future verification language in File Note only.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-SCAN-003

### Purpose
Calibration invoice vs estimate line.

### Trigger
Calibration charge without calibration documentation.

### Evidence needed
Cal report or invoice matching billed operation.

### Review behavior
Test as documentation proposition.

### Do not infer
ADAS system calibrated from photos alone.

### Exceptions
Bundled scan+cal single document.

### Output behavior
Doc Verify Focus when material at due stage.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.