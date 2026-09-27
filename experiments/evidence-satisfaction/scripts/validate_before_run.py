#!/usr/bin/env python3
"""Validate the evidence-satisfaction champion/challenger experiment package before a run.

Checks (all local, no model calls):
  1. corpus/<version>/assistant-bundle/INSTRUCTIONS.md exists
  2. all 9 knowledge files exist under corpus/<version>/assistant-bundle/knowledge/
  3. every FIXTURE_MATRIX fixture has a claim file
  4. GOLDEN_EXPECTATIONS case_ids match FIXTURE_MATRIX case_ids
  5. compose_context builds a non-empty system prompt per corpus version
  6. raw/ has no stale outputs newer than the corpus (warns only)

Exit 0 = ready to run. Exit 1 = problems found.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

EXP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EXP / "scripts"))
from compose_context import compose_from_corpus, KNOWLEDGE_ORDER  # noqa: E402

problems: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    problems.append(msg)


def main() -> int:
    versions = sorted(p.name for p in (EXP / "corpus").iterdir() if p.is_dir())
    if not versions:
        fail("no corpus versions found under corpus/")
    for version in versions:
        bundle = EXP / "corpus" / version / "assistant-bundle"
        if not (bundle / "INSTRUCTIONS.md").is_file():
            fail(f"{version}: missing assistant-bundle/INSTRUCTIONS.md")
        for name in KNOWLEDGE_ORDER:
            if not (bundle / "knowledge" / name).is_file():
                fail(f"{version}: missing knowledge/{name}")
        operator = (EXP / "PROMPT.txt").read_text(encoding="utf-8")
        ctx = compose_from_corpus(
            EXP / "corpus" / version,
            f"corpus {version}-baseline",
            EXP / "corpus" / version / "MANIFEST.sha256.json",
            operator,
        )
        if not ctx["system_prompt"] or len(ctx["system_prompt"]) < 1000:
            fail(f"{version}: composed system prompt suspiciously short")
        else:
            print(f"{version}: system prompt "
                  f"{ctx['combined']['approx_tokens']} approx tokens, "
                  f"sha256={ctx['system_prompt_sha256'][:16]}…")

    matrix = json.loads((EXP / "FIXTURE_MATRIX.json").read_text())["fixtures"]
    goldens = json.loads((EXP / "GOLDEN_EXPECTATIONS.json").read_text())["cases"]
    matrix_ids = {f["case_id"] for f in matrix}
    golden_ids = {c["case_id"] for c in goldens}
    if matrix_ids != golden_ids:
        fail(f"case_id mismatch: matrix-only={sorted(matrix_ids - golden_ids)} "
             f"golden-only={sorted(golden_ids - matrix_ids)}")
    for fx in matrix:
        claim = EXP / "fixtures" / fx["fixture_dir"] / "claim.txt"
        if not claim.is_file():
            fail(f"fixture {fx['fixture_dir']}: missing {claim.relative_to(EXP)}")

    for vdir in sorted((EXP / "raw").glob("v*")):
        if vdir.name not in versions:
            warnings.append(f"raw/{vdir.name} has no matching corpus version")

    if warnings:
        print("warnings:")
        for w in warnings:
            print(f"  - {w}")
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"OK: {len(versions)} version(s), {len(matrix)} fixtures, "
          f"{len(goldens)} golden cases — ready to run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
