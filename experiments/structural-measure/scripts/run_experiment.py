#!/usr/bin/env python3
"""Model-agnostic runner for the structural-measure experiment.

You bring the model; the runner handles corpus composition, fixture iteration,
run repetition, and raw-output capture. Harness metadata (``=== ADAPTER META
===``) is stripped from the claim text before the model ever sees it.

Adapter protocol::

    adapter(system_prompt: str, user_prompt: str, run_tag: str) -> str

Configure with ``--adapter dotted.path.to:adapter`` or the ``EVAL_MODEL_ADAPTER``
environment variable. A built-in ``dry_run`` adapter echoes fixture names for
smoke-testing the harness without spending model calls::

    python scripts/run_experiment.py --adapter dry_run --runs 1

Recorded runs from the reference execution (gpt-5.5, reasoning high) are
preserved under ``raw/``. Re-running with a different model produces a new
``raw/`` tree you can score with ``scripts/score_experiment.py``.

Outputs: ``raw/<version>/<fixture_dir>_runNN.txt`` (model output, verbatim).
"""

from __future__ import annotations

import argparse
import importlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

EXP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EXP / "scripts"))
from compose_context import compose_from_corpus  # noqa: E402

ADAPTER_MARKER = "=== ADAPTER META ==="


def strip_meta(claim_text: str) -> str:
    idx = claim_text.find(ADAPTER_MARKER)
    return claim_text[:idx].rstrip() if idx >= 0 else claim_text.strip()


def load_adapter(spec: str) -> Callable[[str, str, str], str]:
    if spec == "dry_run":
        def dry_run(system_prompt: str, user_prompt: str, run_tag: str) -> str:
            first = user_prompt.splitlines()[0] if user_prompt else ""
            return (
                "STATUS: NEEDS REVIEW\n\nREVIEW FOCUS\n"
                f"1. dry-run echo for {run_tag}: {first}\n\n"
                "ASSISTANT TAKE\nDry run — no model called."
            )
        return dry_run
    module_name, _, attr = spec.partition(":")
    if not attr:
        raise ValueError("adapter spec must be 'dotted.path:callable' or 'dry_run'")
    module = importlib.import_module(module_name)
    fn = getattr(module, attr)
    if not callable(fn):
        raise ValueError(f"adapter {spec} is not callable")
    return fn


def main() -> int:
    ap = argparse.ArgumentParser(description="Run the structural-measure experiment.")
    ap.add_argument("--adapter", default=os.environ.get("EVAL_MODEL_ADAPTER", "dry_run"))
    ap.add_argument("--runs", type=int, default=3, help="runs per fixture/version cell")
    ap.add_argument("--versions", nargs="*", default=None,
                    help="corpus versions to run (default: all under corpus/)")
    ap.add_argument("--fixtures-dir", default="fixtures",
                    help="fixture directory, relative to experiment root")
    ap.add_argument("--model-label", default="unlabeled",
                    help="label recorded in telemetry for this model")
    args = ap.parse_args()

    adapter = load_adapter(args.adapter)
    manifest = json.loads((EXP / "EXPERIMENT_MANIFEST.json").read_text())
    operator_prompt = (EXP / manifest.get("operator_prompt_file", "PROMPT.txt")).read_text(
        encoding="utf-8"
    )
    fixtures = json.loads((EXP / "FIXTURE_MATRIX.json").read_text())["fixtures"]

    versions = args.versions or sorted(
        p.name for p in (EXP / "corpus").iterdir() if p.is_dir()
    )
    started = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    telemetry: list[dict[str, Any]] = []
    total = 0

    for version in versions:
        corpus_dir = EXP / "corpus" / version
        ctx = compose_from_corpus(
            corpus_dir,
            f"corpus {version}-baseline",
            corpus_dir / "MANIFEST.sha256.json",
            operator_prompt,
        )
        print(f"version {version}: system_prompt_sha256={ctx['system_prompt_sha256'][:16]}…")
        raw_dir = EXP / "raw" / version
        raw_dir.mkdir(parents=True, exist_ok=True)
        for fx in fixtures:
            claim_path = EXP / args.fixtures_dir / fx["fixture_dir"] / "claim.txt"
            if not claim_path.is_file():
                print(f"  skip {fx['fixture_dir']}: no claim file at {claim_path}")
                continue
            claim_body = strip_meta(claim_path.read_text(encoding="utf-8"))
            user_text = f"{operator_prompt}\n\n{claim_body}"
            for run_idx in range(1, args.runs + 1):
                run_tag = f"{version}_{fx['fixture_dir']}_run{run_idx:02d}"
                t0 = time.time()
                try:
                    output = adapter(ctx["system_prompt"], user_text, run_tag)
                except Exception as exc:  # noqa: BLE001
                    print(f"  adapter failed on {run_tag}: {exc}")
                    continue
                dt = time.time() - t0
                (raw_dir / f"{fx['fixture_dir']}_run{run_idx:02d}.txt").write_text(
                    output if output.endswith("\n") else output + "\n",
                    encoding="utf-8",
                )
                telemetry.append({
                    "run_tag": run_tag,
                    "version": version,
                    "case_id": fx["case_id"],
                    "model_label": args.model_label,
                    "adapter": args.adapter,
                    "duration_s": round(dt, 2),
                    "system_prompt_sha256": ctx["system_prompt_sha256"],
                })
                total += 1
                print(f"  {run_tag} ({dt:.1f}s)")

    tel_path = EXP / "scored" / "RUN_TELEMETRY.jsonl"
    tel_path.parent.mkdir(exist_ok=True)
    with tel_path.open("a", encoding="utf-8") as fh:
        for row in telemetry:
            fh.write(json.dumps(row) + "\n")
    print(f"done: {total} calls across {len(versions)} version(s); started {started}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
