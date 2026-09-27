#!/usr/bin/env python3
"""Standalone scorer for the sublet-repair benchmark correction.

The original evidence-satisfaction run used a mismatched invoice fixture for
the SUBLET-PRESENT cell (estimate line $890 vs invoice $925), so both corpus
versions "failed" that cell for benchmark reasons, not evidence-satisfaction
reasons. This repair re-ran the sublet pair with a clean counterfactual:

  * PRESENT-CLEAN: invoice matches the estimate line exactly ($890)
  * ABSENT-CLEAN:  no applicable invoice

Reads this directory's GOLDEN_EXPECTATIONS.json + FIXTURE_MATRIX.json, scores
raw/v*/<fixture>_runNN.txt with the same resolution logic as the parent
experiment, and writes scored/STANDALONE_REPAIR_RESULTS.jsonl and
scored/STANDALONE_REPAIR_SUMMARY.json.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPAIR = Path(__file__).resolve().parents[1]

FOCUS_RE = re.compile(
    r"REVIEW FOCUS\s*\n(.*?)(?=\nASSISTANT TAKE|\Z)", re.DOTALL | re.IGNORECASE
)
UNSUPPORTED_RE = re.compile(r"\[Unsupported\][^\n]*", re.IGNORECASE)
INFERENCE_RE = re.compile(r"\[Inference\][^\n]*", re.IGNORECASE)
UNRESOLVED_RE = re.compile(r"\[Unresolved question\][^\n]*", re.IGNORECASE)


def extract_focus(text: str) -> str:
    m = FOCUS_RE.search(text)
    return m.group(1).strip() if m else ""


def pattern_match(pattern: str, text: str) -> bool:
    return bool(re.search(pattern, text, re.IGNORECASE | re.DOTALL))


def canonical_sha256(text: str) -> str:
    norm = re.sub(r"\s+", " ", text).strip().lower()
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def score_run(raw: str, golden: dict) -> dict[str, Any]:
    focus = extract_focus(raw)
    forbidden_hit = any(
        pattern_match(p, focus) for p in golden.get("forbidden_in_review_focus", [])
    )
    required_hit = any(
        pattern_match(p, focus) for p in golden.get("required_in_review_focus", [])
    )
    no_material = bool(re.search(r"no material review items", focus, re.I))

    if golden["evidence_state"] == "present":
        target_suppressed = (not forbidden_hit) and (no_material or not focus.strip())
        target_published = forbidden_hit or (focus.strip() and not no_material)
    else:
        target_published = required_hit or (
            forbidden_hit and golden["evidence_state"] == "absent"
        )
        target_suppressed = not target_published and no_material

    if golden["evidence_state"] == "present":
        correct = target_suppressed
        resolution_behavior = "SATISFIED" if target_suppressed else "FALSE_PUBLICATION"
    else:
        correct = target_published
        resolution_behavior = "UNRESOLVED" if target_published else "FALSE_SUPPRESSION"

    return {
        "case_id": golden["case_id"],
        "family": golden["family"],
        "evidence_state": golden["evidence_state"],
        "target_candidate": golden["target_candidate"],
        "expected_resolution": golden["expected_resolution"],
        "target_suppressed": target_suppressed,
        "target_published": target_published,
        "correct_resolution": correct,
        "resolution_behavior": resolution_behavior,
        "canonical_sha256": canonical_sha256(raw),
        "unsupported_assertions": len(UNSUPPORTED_RE.findall(raw)),
        "inferences": len(INFERENCE_RE.findall(raw)),
        "unresolved_questions": len(UNRESOLVED_RE.findall(raw)),
        "review_focus_excerpt": focus[:500],
    }


def main() -> int:
    goldens = {
        c["case_id"]: c
        for c in json.loads((REPAIR / "GOLDEN_EXPECTATIONS.json").read_text())["cases"]
    }
    fixtures = json.loads((REPAIR / "FIXTURE_MATRIX.json").read_text())["fixtures"]
    fx_by_dir = {f["fixture_dir"]: f for f in fixtures}

    run_results: list[dict] = []
    for ver_dir in sorted((REPAIR / "raw").glob("v*")):
        version = ver_dir.name
        for raw_path in sorted(ver_dir.glob("*_run*.txt")):
            m = re.match(r"(.+)_run(\d+)$", raw_path.stem)
            if not m:
                continue
            fixture_dir, run_n = m.group(1), int(m.group(2))
            fx = fx_by_dir.get(fixture_dir)
            if not fx:
                print(f"warning: no fixture entry for {fixture_dir}; skipping")
                continue
            scored = score_run(raw_path.read_text(encoding="utf-8"), goldens[fx["case_id"]])
            scored["version"] = version
            scored["run_number"] = run_n
            scored["raw_path"] = str(raw_path.relative_to(REPAIR))
            run_results.append(scored)

    if not run_results:
        print("No raw repair outputs found.")
        return 1

    scored_dir = REPAIR / "scored"
    scored_dir.mkdir(exist_ok=True)
    with (scored_dir / "STANDALONE_REPAIR_RESULTS.jsonl").open("w", encoding="utf-8") as fh:
        for r in run_results:
            fh.write(json.dumps(r) + "\n")

    by_version: dict[str, list] = defaultdict(list)
    for r in run_results:
        by_version[r["version"]].append(r)
    summary: dict[str, Any] = {
        "scored_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "scorer": "standalone (no product-internal canonicalizer)",
        "run_count": len(run_results),
        "versions": {
            ver: {
                "runs": len(rows),
                "correct_rate": round(
                    sum(1 for r in rows if r["correct_resolution"]) / len(rows), 4
                ),
            }
            for ver, rows in by_version.items()
        },
    }
    (scored_dir / "STANDALONE_REPAIR_SUMMARY.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(f"scored {len(run_results)} repair runs -> "
          f"scored/STANDALONE_REPAIR_SUMMARY.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
