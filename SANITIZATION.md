# Sanitization report

What this corpus is, what was removed or renamed to make it releasable, and
what was rewritten so it stands alone.

## Source

Synthetic evaluation fixtures and experiment harnesses authored by Jason
Saunders, extracted from a private development repository. The selected
material is synthetic: every fixture is labeled as a synthetic harness case,
and the release contains no customer data, no real claims, no employer
documents, no product runtime code, and no named internal implementation
details.

## Exclusions (not carried over)

- Persona/prompt experiments unrelated to the eval
- Deployment packs containing VIN-like values and employer references
- Product-internal scorer chain (canonical scorer, saved-scorer, and
  epistemic-chain modules) — replaced by clean-room standalone scorers
- Upload manifests and provenance files in their original form — replaced
  by generated generic versions
- Rejected/deferred design-history sections of the provenance matrices
  (product history, not eval-relevant)

## Renames

| Original | Sanitized | Notes |
|----------|-----------|-------|
| Internal review-assistant system names (2) | `the review assistant` / `assistant` | |
| Internal output-section labels | `ASSISTANT TAKE` | scorer regexes updated |
| Internal rule ID prefixes | `RULE-<DOMAIN>-<NNN>` | |
| Fixture/case ID prefix | `EVAL-<...>` | |
| Synthetic fixture ID prefix | `SYN-<...>` | |
| Prior-system name | `the prior system` | |
| Prior-system anchor tag | `PRIOR-ANCHOR` | |
| Internal bundle directory | `assistant-bundle/` | |
| Internal experiments directory | `experiments/` | |
| Pre-release version tags | `v0.x.y` | |
| Repair directory (underscore → hyphen) | `sublet-repair/` | |
| Internal provenance docs (2) | `CORPUS_PROVENANCE.md` | regenerated, product columns dropped |

## Rewrites (clean-room, stdlib only)

- `scripts/score_experiment.py` (both experiments): faithful port of the
  original resolution logic. The only deliberate change is the canonical hash
  (plain SHA-256 over normalized text instead of the product-internal
  canonicalizer).
- `scripts/run_experiment.py` (both): model-agnostic runner template. The
  originals called a hardcoded internal inference entrypoint; the template
  takes any adapter implementing
  `adapter(system_prompt, user_prompt, run_tag) -> str`.
- `scripts/validate_before_run.py` (both): the originals imported
  product-internal modules and one referenced a path that no longer exists;
  rewritten as a self-contained package check.
- `scripts/build_frozen_corpus.py`: regenerates the v0.1.0 corpus from v0.2.0
  via the documented satisfaction-layer removal, then verifies byte-identity
  with the shipped v0.1.0.
- `sublet-repair/scripts/score_repair.py`: standalone port of the repair scorer.

## Verification

- Automated scan of the shipped tree: no email addresses, phone numbers,
  credential-like strings, or VIN-like values.
- Post-build scrub (2026-09-27): four `CORPUS_PROVENANCE.md` migration tables
  carried a legacy source-family label containing an employer-name signal;
  renamed to the neutral `SYN-AUTO-EIF-*`. No employer-name tokens remain
  anywhere in the shipped tree.
- Session-ID scrub (2026-09-27): historical run-session identifiers in frozen
  telemetry/summary files embedded internal project-name fragments;
  re-prefixed to neutral `eval_*`. Raw model outputs untouched — scoring
  inputs are byte-identical.
- One scored report quoted an internal test-suite path; generalized to
  "the reference satisfaction suite."
- Known fictional-ID quirks, non-identifying, left byte-identical: one synthetic
  invoice PDF retains a fictional vendor label (`VN-ADV-10`) baked into the PDF
  stream, and one scored-output excerpt in
  `experiments/evidence-satisfaction/scored/RUN_RESULTS.jsonl` quotes a fictional
  vendor invoice ID (`VN-INV-SUBLET-02`). Both are synthetic fixture IDs with no
  product, employer, or personal attribution; the scored record is frozen as the
  faithful output of the reference run.
- No internal system names, employer-name signals, pre-release ID prefixes,
  or internal paths remain anywhere in the shipped tree, its reports, or
  this document.
- The standalone scorers reproduce **72/72** original verdicts
  (`correct_resolution` per run) against the sanitized raw outputs:
  48/48 evidence-satisfaction, 24/24 structural-measure.
- `build_frozen_corpus.py --verify-only`: the v0.1.0 corpus regenerates
  byte-identical from v0.2.0 via the documented transforms.
- `validate_before_run.py` passes for both experiments; the runner
  smoke-tests end-to-end with `--adapter dry_run`.
