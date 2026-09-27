# Evaluation design: decomposed governance measurement

## 1. The gap

Most AI benchmarks measure task success: did the model get the right answer?
Governance failures rarely look like wrong answers. They look like *authority
outrunning evidence* — a fluent, confident review item that the file doesn't
support; a conclusion that doesn't move when the evidence does; uncertainty
quietly collapsed into a finding.

This corpus measures those behaviors directly, in a narrow domain where they
are checkable: auto physical-damage claim review.

## 2. The instrument

**Paired counterfactual fixtures.** Each test family ships as twins: an
evidence-PRESENT fixture and an evidence-ABSENT fixture, identical except for
the supporting document. This isolates the single variable under test — the
model cannot pass by memorizing the fixture, because the two twins demand
opposite conclusions from near-identical inputs.

**Golden expectations, frozen before the run.** Each case declares an
`expected_resolution` (`SATISFIED` / `UNRESOLVED` / `NOT_APPLICABLE`) plus
`required_in_review_focus` and `forbidden_in_review_focus` regexes. Scoring is
deterministic pattern matching against the model's `REVIEW FOCUS` section.
There is no LLM judge, and therefore no judge to flatter the model.

**Champion/challenger.** The evidence-satisfaction experiment runs two corpus
versions that differ by exactly one documented change (the
satisfaction-protocol layer — verify with
`scripts/build_frozen_corpus.py --verify-only`). This turns the eval into a
*delta measurement*: did the change improve governance behavior, and where?

**Repeatability.** Three runs per cell, reported as x/3. A governance
property that holds 1/3 of the time is not a property.

**Asymmetric failure buckets.** False suppressions (the model stayed silent
about a real evidence gap) and false publications (the model flagged what
the evidence already satisfied) are reported separately, because they fail
in different directions with different costs.

**Epistemic markers.** Outputs are expected to carry `[Inference]`,
`[Unsupported]`, and `[Unresolved question]` labels. The scorer counts them.
A model that marks its uncertainty is behaving better than one with identical
conclusions and no markers — the human reviewer can see what is established
and what is not.

## 3. The three behaviors under test

1. **Evidence sensitivity** — the conclusion must change when the evidence
   changes. The present/absent twins make this falsifiable per case.
2. **Uncertainty preservation** — absent evidence must produce an explicit
   unresolved item, never invented support. Forbidden patterns (e.g.
   accusatory "fraud"/"overbill" language, "not performed" assertions)
   penalize the model for filling the gap with tone instead of evidence.
3. **Authority restraint** — satisfied evidence must suppress the review item.
   Flagging what the file already proves is authority without warrant.

## 4. Relation to the Microsoft Humanist AI Code of Conduct

This corpus was assembled alongside the author's consultation feedback on the
[Microsoft Humanist AI Code of Conduct](https://microsoft.ai/code-of-conduct/).
It operationalizes three of the behaviors raised there:

- **§2.4 — evidence-gated conclusions.** The paired counterfactuals test
  whether conclusions track evidence: publish on absent, suppress on
  present, and never assert beyond what the file supports.
- **§3.3 — uncertainty made visible.** The absent-evidence cells require
  explicit `UNRESOLVED` outcomes with epistemic markers, so uncertainty is
  preserved in the output instead of collapsed into a confident finding.
- **§5 — evaluation that can falsify.** Deterministic goldens, no LLM judge,
  repeatability reporting, and champion/challenger deltas are the
  methodological commitments: a governance eval should be able to say "this
  change made behavior worse," not just "the model is good."

This is a domain instrument, not a reading of the Code. It does not certify
compliance with anything.

## 5. Extending the corpus

To add a fixture family:

1. Write the PRESENT and ABSENT twins under `fixtures/<family>_present/` and
   `fixtures/<family>_absent/` (`claim.txt`; strip nothing — the runner
   removes the `=== ADAPTER META ===` block before the model sees it).
2. Register both in `FIXTURE_MATRIX.json` with `case_id`, `family`, and
   `evidence_state`.
3. Add golden expectations: `expected_resolution`, `required_in_review_focus`,
   `forbidden_in_review_focus`.
4. Run `validate_before_run.py`, then the runner, then the scorer.

Keep twins minimal: the *only* material difference should be the evidence
under test.

## 6. Limitations

- **Narrow domain.** Auto physical-damage claim review. The behaviors are
  general; the fixtures are not.
- **Synthetic fixtures.** Clean by construction. Real files are messier, and
  mess is where governance fails most interestingly.
- **Single-rater goldens.** Expectations were written by the corpus author.
  No independent annotation study.
- **One reference model.** Reference outputs are gpt-5.5 (reasoning high).
  The harness is model-agnostic; cross-model comparison is the point, but
  only one model has been run.
- **Not a safety benchmark.** This measures governance-relevant behavior in
  one domain. It does not test for harm, bias, or misuse.
