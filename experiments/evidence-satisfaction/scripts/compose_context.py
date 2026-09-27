#!/usr/bin/env python3
"""Compose assistant system context from frozen experiment corpus (not live working files)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

KNOWLEDGE_ORDER = [
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


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compose_from_corpus(
    corpus_dir: Path,
    baseline_id: str,
    baseline_manifest_path: Path,
    operator_prompt: str,
) -> dict[str, Any]:
    instructions_path = corpus_dir / "assistant-bundle/INSTRUCTIONS.md"
    instructions = instructions_path.read_text(encoding="utf-8")
    blocks = ["===== BEGIN ASSISTANT KNOWLEDGE CORPUS ====="]
    per_file: list[dict[str, Any]] = []
    for name in KNOWLEDGE_ORDER:
        path = corpus_dir / "assistant-bundle/knowledge" / name
        text = path.read_text(encoding="utf-8")
        blocks.append(f"===== BEGIN ASSISTANT KNOWLEDGE: {name} =====")
        blocks.append(text.rstrip())
        blocks.append(f"===== END ASSISTANT KNOWLEDGE: {name} =====")
        per_file.append(
            {
                "file": name,
                "chars": len(text),
                "bytes": path.stat().st_size,
                "sha256": _sha256_file(path),
            }
        )
    blocks.append("===== END ASSISTANT KNOWLEDGE CORPUS =====")
    corpus = "\n".join(blocks) + "\n"

    system_parts = [
        instructions.rstrip(),
        "",
        "===== the review assistant SYSTEM CONTEXT: FULL KNOWLEDGE (COGNITION EXPERIMENT — ALL FILES INJECTED) =====",
        corpus.rstrip(),
    ]
    system_prompt = "\n".join(system_parts) + "\n"

    # behavioral corpus hash = concat of manifest file hashes
    manifest_hashes: list[str] = []
    if baseline_manifest_path.is_file():
        manifest = json.loads(baseline_manifest_path.read_text(encoding="utf-8"))
        for entry in manifest["files"]:
            rel = entry["path"]
            p = corpus_dir / rel
            manifest_hashes.append(_sha256_file(p))

    corpus_sha = _sha256_text("".join(manifest_hashes))

    return {
        "version": (corpus_dir / "VERSION").read_text(encoding="utf-8").strip(),
        "baseline_id": baseline_id,
        "baseline_manifest_path": str(baseline_manifest_path),
        "baseline_manifest_sha256": _sha256_file(baseline_manifest_path) if baseline_manifest_path.is_file() else None,
        "behavioral_corpus_sha256": corpus_sha,
        "instructions": {
            "chars": len(instructions),
            "sha256": _sha256_file(instructions_path),
            "approx_tokens": len(instructions) // 4,
        },
        "knowledge_corpus": {"files": per_file, "chars": len(corpus), "approx_tokens": len(corpus) // 4},
        "knowledge_order": KNOWLEDGE_ORDER,
        "combined": {
            "chars": len(system_prompt),
            "approx_tokens": len(system_prompt) // 4,
        },
        "system_prompt_sha256": _sha256_text(system_prompt),
        "operator_prompt": operator_prompt,
        "operator_prompt_sha256": _sha256_text(operator_prompt),
        "system_prompt": system_prompt,
    }
