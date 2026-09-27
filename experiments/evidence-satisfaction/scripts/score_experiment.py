#!/usr/bin/env python3
"""Standalone scorer for the evidence-satisfaction champion/challenger experiment.

No external dependencies: reads FIXTURE_MATRIX.json + GOLDEN_EXPECTATIONS.json,
scores every raw/v*/<fixture>_runNN.txt against the golden regexes, and writes
scored/STANDALONE_RUN_RESULTS.jsonl + scored/STANDALONE_RUN_SUMMARY.json.

Deterministic: the same raw outputs scored against the same goldens always
produce the same verdicts. Resolution logic is a faithful port of the original
experiment scorer; the only deliberate change is the canonical hash (plain
SHA-256 over whitespace-normalized output text instead of the original
product-internal canonicalizer).
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

EXP = Path(__file__).resolve().parents[1]

FOCUS_RE = re.compile(
    r"REVIEW FOCUS\s*\n(.*?)(?=\nASSISTANT TAKE|\Z)", re.DOTALL | re.IGNORECASE
)
STATUS_RE = re.compile(
    r"STATUS:\s*\**?(NO OPEN ITEMS|NEEDS REVIEW|CRITICAL REVIEW)\**?",
    re.IGNORECASE,
)
UNSUPPORTED_RE = re.compile(r"\[Unsupported\][^\n]*", re.IGNORECASE)
INFERENCE_RE = re.compile(r"\[Inference\][^\n]*", re.IGNORECASE)
UNRESOLVED_RE = re.compile(r"\[Unresolved question\][^\n]*", re.IGNORECASE)
BOLD_RE = re.compile(r"\*\*[^*]+\*\*")


def extract_focus(text: str) -> str:
    m = FOCUS_RE.search(text)
    return m.group(1).strip() if m else ""


def pattern_match(pattern: str, text: str) -> bool:
    return bool(re.search(pattern, text, re.IGNORECASE | re.DOTALL))


def canonical_sha256(text: str) -> str:
    norm = re.sub(r"\s+", " ", text).strip().lower()
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def extract_epistemic_markers(text: str) -> dict[str, int]:
    return {
        "unsupported_assertions": len(UNSUPPORTED_RE.findall(text)),
        "inferences": len(INFERENCE_RE.findall(text)),
        "unresolved_questions": len(UNRESOLVED_RE.findall(text)),
    }


def repeatability_label(flags: list[bool]) -> str:
    return f"{sum(1 for f in flags if f)}/{len(flags)}"


def score_run(raw: str, golden: dict) -> dict[str, Any]:
    focus = extract_focus(raw)
    markers = extract_epistemic_markers(raw)

    forbidden_hit = any(
        pattern_match(p, focus) for p in golden.get("forbidden_in_review_focus", [])
    )
    required_hit = any(
        pattern_match(p, focus) for p in golden.get("required_in_review_focus", [])
    )
    no_material = bool(re.search(r"no material review items", focus, re.I))

    if golden["evidence_state"] == "present":
        target_suppressed = (not forbidden_hit) and (no_material or not focus.strip())
        target_published = forbidden_hit
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

    m = STATUS_RE.search(raw)
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
        "status": m.group(1).upper() if m else None,
        "canonical_sha256": canonical_sha256(raw),
        "unsupported_assertions": markers["unsupported_assertions"],
        "inferences": markers["inferences"],
        "unresolved_questions": markers["unresolved_questions"],
        "review_focus_excerpt": focus[:500],
    }


def confusion_bucket(evidence_state: str, scored: dict) -> str:
    if evidence_state == "present":
        return "true_suppression" if scored["target_suppressed"] else "false_publication"
    return "true_publication" if scored["target_published"] else "false_suppression"


def classify_failure(scored: dict, golden: dict) -> str | None:
    if scored["correct_resolution"]:
        return None
    return scored["resolution_behavior"]


def main() -> int:
    goldens = {
        c["case_id"]: c
        for c in json.loads((EXP / "GOLDEN_EXPECTATIONS.json").read_text())["cases"]
    }
    fixtures = json.loads((EXP / "FIXTURE_MATRIX.json").read_text())["fixtures"]
    fx_by_dir = {f["fixture_dir"]: f for f in fixtures}

    run_results: list[dict] = []
    for ver_dir in sorted((EXP / "raw").glob("v*")):
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
            golden = goldens[fx["case_id"]]
            scored = score_run(raw_path.read_text(encoding="utf-8"), golden)
            scored["version"] = version
            scored["run_number"] = run_n
            scored["raw_path"] = str(raw_path.relative_to(EXP))
            scored["confusion_bucket"] = confusion_bucket(fx["evidence_state"], scored)
            scored["failure_class"] = classify_failure(scored, golden)
            run_results.append(scored)

    if not run_results:
        print("No raw outputs found under raw/ — run run_experiment.py first.")
        return 1

    scored_dir = EXP / "scored"
    scored_dir.mkdir(exist_ok=True)
    with (scored_dir / "STANDALONE_RUN_RESULTS.jsonl").open("w", encoding="utf-8") as fh:
        for r in run_results:
            fh.write(json.dumps(r) + "\n")

    by_version: dict[str, list] = defaultdict(list)
    for r in run_results:
        by_version[r["version"]].append(r)

    summary: dict[str, Any] = {
        "scored_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "scorer": "standalone (no product-internal canonicalizer)",
        "run_count": len(run_results),
        "versions": {},
    }
    for ver, rows in by_version.items():
        by_case: dict[str, list[bool]] = defaultdict(list)
        for r in rows:
            by_case[r["case_id"]].append(r["correct_resolution"])
        summary["versions"][ver] = {
            "runs": len(rows),
            "correct_rate": round(
                sum(1 for r in rows if r["correct_resolution"]) / len(rows), 4
            ),
            "repeatability_by_case": {
                cid: repeatability_label(flags) for cid, flags in by_case.items()
            },
            "false_suppressions": sorted(
                {r["case_id"] for r in rows
                 if r["evidence_state"] == "absent" and not r["correct_resolution"]}
            ),
            "false_publications": sorted(
                {r["case_id"] for r in rows
                 if r["evidence_state"] == "present" and not r["correct_resolution"]}
            ),
        }

    (scored_dir / "STANDALONE_RUN_SUMMARY.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(f"scored {len(run_results)} runs -> scored/STANDALONE_RUN_SUMMARY.json")
    for ver, s in summary["versions"].items():
        print(f"  {ver}: {s['runs']} runs, correct_rate={s['correct_rate']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
