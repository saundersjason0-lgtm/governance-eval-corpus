# Assistant Bundle Upload Manifest (v0.2.1)

How to load the frozen behavioral corpus into a host assistant.

## Instructions

`INSTRUCTIONS.md` — review doctrine, algorithm, and output contract.
Keep it whole; it is sized to fit typical instruction-field limits.

## Knowledge uploads (`knowledge/`)

Upload each Markdown file separately so the host can retrieve relevant sections.

| File | Domain |
|------|--------|
| `CORE_EVIDENCE.md` | Doctrine, epistemic labels, inventory, materiality, human authority |
| `ESTIMATE_REVIEW.md` | Proposition testing, manual lines, domain isolation |
| `PHOTO_DAMAGE.md` | Line-to-photo matching, refinish process proof, damage alignment |
| `PARTS_LABOR.md` | Part codes, included operations, unsupported operations |
| `ADAS_SCAN.md` | Scan/calibration billing vs reports, stage deferral |
| `DOCUMENTATION.md` | Document verification, reports, sublet proof |
| `PAYMENT_DTP.md` | Payment provenance, direct-to-payee authorization |
| `INVOICE_RECON.md` | Invoice vs estimate reconciliation |
| `WORKFLOW_CHRONOLOGY.md` | Operational stage, current picture, continuity |

## Verification before use

```bash
python scripts/validate_before_run.py
```

This checks that every knowledge file is present, every fixture has a claim
file, golden case IDs match the fixture matrix, and the composed system
prompt builds cleanly.
