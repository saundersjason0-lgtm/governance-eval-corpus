#!/usr/bin/env python3
"""Pair-diff validator for sublet repair fixtures."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

REPAIR = Path(__file__).resolve().parents[1]
PRESENT = REPAIR / "fixtures/sublet_present_clean/claim.txt"
ABSENT = REPAIR / "fixtures/sublet_absent_clean/claim.txt"
OUT = REPAIR / "PAIR_DIFF.md"


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def body(text: str) -> str:
    idx = text.find("=== ADAPTER META")
    return text[:idx].rstrip() if idx >= 0 else text.strip()


def normalize_lines(text: str) -> list[str]:
    return [ln.rstrip() for ln in body(text).splitlines()]


def main() -> int:
    p_text = PRESENT.read_text(encoding="utf-8")
    a_text = ABSENT.read_text(encoding="utf-8")
    p_lines = normalize_lines(p_text)
    a_lines = normalize_lines(a_text)

    diffs: list[tuple[int, str, str]] = []
    max_len = max(len(p_lines), len(a_lines))
    for i in range(max_len):
        pl = p_lines[i] if i < len(p_lines) else ""
        al = a_lines[i] if i < len(a_lines) else ""
        if pl != al:
            diffs.append((i + 1, pl, al))

    # Allowed substantive diff: DOCUMENTS sublet invoice line + claim header
    allowed_patterns = [
        re.compile(r"^Claim #:"),
        re.compile(r"^Frame-house sublet invoice:"),
    ]
    material_other: list[tuple[int, str, str]] = []
    for line_no, pl, al in diffs:
        if not any(pat.search(pl) or pat.search(al) for pat in allowed_patterns):
            material_other.append((line_no, pl, al))

    clean = len(material_other) == 0 and len(diffs) > 0

    lines = [
        "# Pair-Diff — Sublet Repair Fixtures",
        "",
        f"- present fixture SHA256: `{sha256_file(PRESENT)}`",
        f"- absent fixture SHA256: `{sha256_file(ABSENT)}`",
        f"- total line diffs (body): {len(diffs)}",
        f"- material diffs outside allowed fields: {len(material_other)}",
        f"- PAIR_DIFF_CLEAN: **{'TRUE' if clean else 'FALSE'}**",
        "",
        "## Line differences",
        "",
    ]
    for line_no, pl, al in diffs:
        lines.append(f"### Line {line_no}")
        lines.append(f"- PRESENT: `{pl}`")
        lines.append(f"- ABSENT: `{al}`")
        lines.append("")

    if material_other:
        lines.append("## STOP — unexpected material differences")
        for line_no, pl, al in material_other:
            lines.append(f"- Line {line_no}: `{pl}` vs `{al}`")

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0 if clean else 1


if __name__ == "__main__":
    raise SystemExit(main())
