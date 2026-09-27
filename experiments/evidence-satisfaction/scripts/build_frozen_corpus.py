#!/usr/bin/env python3
"""Regenerate the frozen v0.1.0 corpus from the v0.2.0 corpus.

The v0.1.0 (champion) corpus is the v0.2.0 (challenger) corpus with the
satisfaction-protocol layer removed:

  * "### Satisfaction predicate" sections stripped from knowledge files
  * the RULE-CORE-009 rule (evidence-resolution archaeology) removed from
    CORE_EVIDENCE.md
  * INSTRUCTIONS.md step 4 reverted from "Evidence binding & satisfaction"
    to "Proposition testing"

This is the auditable record of the champion/challenger delta: the two corpora
differ ONLY by these transforms. The script regenerates v0.1.0 from the
shipped v0.2.0 and verifies it byte-matches the shipped v0.1.0.

Usage: python scripts/build_frozen_corpus.py [--verify-only]
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

EXP = Path(__file__).resolve().parents[1]
V02 = EXP / "corpus" / "v0.2.0"
V01 = EXP / "corpus" / "v0.1.0"

KNOWLEDGE = [
    "CORE_EVIDENCE.md",
    "ESTIMATE_REVIEW.md",
    "PHOTO_DAMAGE.md",
    "PARTS_LABOR.md",
    "ADAS_SCAN.md",
    "DOCUMENTATION.md",
    "PAYMENT_DTP.md",
    "INVOICE_RECON.md",
    "WORKFLOW_CHRONOLOGY.md",
]

PROPOSITION_TESTING_STEP = (
    "4. **Proposition testing** \u2014 For each material candidate: what evidence "
    "would support it? what is present? \u2192 SUPPORTED | CONFLICTED | UNRESOLVED "
    "| NOT_DETERMINABLE | NOT_APPLICABLE."
)


def remove_satisfaction_sections(text: str) -> str:
    text = re.sub(
        r"\n### Satisfaction predicate\n.*?(?=\n### Provenance)",
        "\n",
        text,
        flags=re.DOTALL,
    )
    return re.sub(r"\n{3,}(### Provenance)", r"\n\n\1", text)


def remove_core_009(text: str) -> str:
    # NOTE: no trailing newline is added — the shipped v0.1.0 file has none,
    # and the rebuild must match it byte-for-byte.
    return re.sub(
        r"\n---\n\n## RULE-CORE-009\n.*", "", text, flags=re.DOTALL
    ).rstrip()


def revert_instructions_v01(text: str) -> str:
    return re.sub(
        r"4\. \*\*Evidence binding & satisfaction\*\* \u2014.*?supplied\.\n",
        PROPOSITION_TESTING_STEP + "\n",
        text,
        flags=re.DOTALL,
    )


def revert_file(rel: str, content: str) -> str:
    if rel == "VERSION":
        return "0.1.0\n"
    if rel == "assistant-bundle/UPLOAD_MANIFEST.md":
        return content.replace("(v0.2.0)", "(v0.1.0)")
    if rel == "assistant-bundle/INSTRUCTIONS.md":
        return revert_instructions_v01(content)
    if rel == "assistant-bundle/knowledge/CORE_EVIDENCE.md":
        return remove_core_009(content)
    if rel.endswith(".md") and "/knowledge/" in rel:
        return remove_satisfaction_sections(content)
    return content


def build() -> Path:
    tmp = EXP / "corpus" / ".v0.1.0-rebuild"
    if tmp.exists():
        shutil.rmtree(tmp)
    for name in ["VERSION", "assistant-bundle/INSTRUCTIONS.md",
                 "assistant-bundle/UPLOAD_MANIFEST.md",
                 *[f"assistant-bundle/knowledge/{n}" for n in KNOWLEDGE]]:
        src = V02 / name
        raw = src.read_text(encoding="utf-8")
        out = tmp / name
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(revert_file(name, raw), encoding="utf-8")
    return tmp


def main() -> int:
    verify_only = "--verify-only" in sys.argv
    tmp = build()
    mismatches: list[str] = []
    for src in sorted(tmp.rglob("*")):
        if not src.is_file():
            continue
        rel = src.relative_to(tmp)
        shipped = V01 / rel
        if not shipped.is_file():
            mismatches.append(f"{rel}: missing from shipped v0.1.0")
        elif src.read_bytes() != shipped.read_bytes():
            mismatches.append(f"{rel}: content differs from shipped v0.1.0")
    shutil.rmtree(tmp)
    if mismatches:
        print("REBUILD MISMATCH:")
        for m_ in mismatches:
            print(f"  - {m_}")
        return 1
    if verify_only:
        print("verify: rebuilt v0.1.0 from v0.2.0 matches shipped v0.1.0 exactly")
    else:
        print("rebuild: v0.1.0 regenerates byte-identical from v0.2.0 via the "
              "documented satisfaction-layer removal")
    return 0


if __name__ == "__main__":
    sys.exit(main())
