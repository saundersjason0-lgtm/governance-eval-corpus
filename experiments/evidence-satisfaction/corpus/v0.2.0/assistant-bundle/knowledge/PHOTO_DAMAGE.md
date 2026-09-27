# the review assistant Photo & Damage Evidence

## RULE-PHOTO-001

### Purpose
Estimate line ↔ photo alignment testing.

### Trigger
Billed repair line with photos in file.

### Evidence needed
Photo labels/zones vs line description (panel, operation, area).

### Review behavior
Detect MATERIAL MISMATCH when photo documents different zone than billed line.

### Do not infer
Single photo must exist for every line.

### Exceptions
Assembly photos supporting multiple related lines.

### Output behavior
Evidence Conflict or Current Picture MISMATCH with line # and photo label quote.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-PHOTO-002

### Purpose
Refinish process proof (spray-out, let-down, FSB, nib/buff, mask, etc.).

### Trigger
Manual refinish process lines on estimate.

### Evidence needed
Process photos, spray-out card, let-down panel, finish sand/buff documentation.

### Review behavior
All stages for spray-out/FSB/tow-class proof; test billed process not just refinish labor generically.

### Do not infer
Refinish labor line proves sub-processes.

### Exceptions
Shared proof for related operations when file genuinely supports group.

### Output behavior
Separate Focus or combined when same evidence requirement.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-PHOTO-003

### Purpose
Photo evidence in Focus without Photo Summary section.

### Trigger
Photo supports or contradicts a Focus item.

### Evidence needed
Exact photo label text from file/manifest.

### Review behavior
Quote label in Focus: `'Completed front repair'` etc.

### Do not infer
Default Photo Summary gallery.

### Exceptions
Operator requests photo digest explicitly.

### Output behavior
Labels inside Focus items only on default quick review.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-PHOTO-004

### Purpose
Photo coverage due-now vs defer.

### Trigger
Missing photo classes before Focus/STATUS.

### Evidence needed
Stage + operation class (tow, spray-out, FSB due all stages).

### Review behavior
Run photo coverage check before publishing STATUS/Focus when due.

### Do not infer
All missing photos are Focus at FNOL.

### Exceptions
Pre-pay deferral for scan reports (see DOCUMENTATION).

### Output behavior
Due-now gaps → Focus; not-yet-due → File Note only.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.