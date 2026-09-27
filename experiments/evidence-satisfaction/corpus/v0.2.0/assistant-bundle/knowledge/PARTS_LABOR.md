# the review assistant Parts & Labor

## RULE-PART-001

### Purpose
Part-code and judgment lines carry proof burden.

### Trigger
Part code table lines, user-defined labor, manual entries.

### Evidence needed
Same families as RULE-EST-002 (photos, docs, notes, OEM).

### Review behavior
Apply proposition testing; do not treat as standard DB refinish.

### Do not infer
Part code presence = OEM validated.

### Exceptions
Carrier-bundled included operations.

### Output behavior
Line # + support gap in Focus when material.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-PART-002

### Purpose
Not-included / unsupported operation detection.

### Trigger
Line describes operation not in standard scope without support.

### Evidence needed
OEM procedure, photo, or file note.

### Review behavior
Surface as Doc Verify or scope verification — not automatic denial.

### Do not infer
Operation impossible.

### Exceptions
Shop practice documented in file note.

### Output behavior
Verify language in Focus.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-PART-003

### Purpose
EIF / No A/M variant audit alignment.

### Trigger
Estimate EIF or No A/M part variants with CCC audit line refs.

### Evidence needed
Audit line citation + estimate line.

### Review behavior
Surface at any stage when audit cites part mismatch.

### Do not infer
All EIF lines wrong.

### Exceptions
None.

### Output behavior
Focus with audit Line # when applicable.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.
---

## RULE-PART-004

### Purpose
CAPA duplicate silence.

### Trigger
CAPA line on estimate + cheaper non-CAPA same part in CCC audit.

### Evidence needed
Both lines documented.

### Review behavior
Suppress redundant CAPA noise when audit already flags economics.

### Do not infer
CAPA always wrong.

### Exceptions
Material scope difference between parts.

### Output behavior
Silence or File Note only — not Focus spam.

### Provenance
Carried forward from prior iterations of the author's review-assistant system. Retained on regression-fixture evidence.