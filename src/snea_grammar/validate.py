# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""Schema validation for grammar records.

``validate_record`` returns the list of schema violations for one record
(empty list = well-formed); ``validate_directory`` walks a record directory
and returns per-file violation lists.

Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)
"""

from pathlib import Path
from typing import Any

import yaml

from .model import KIND_VOCABULARY, NORM_STATES, REQUIRED_FIELDS


def validate_record(data: dict[str, Any]) -> list[str]:
    """Validate one grammar record; return its schema violations."""
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"missing required field: {field}")
    if "evidence_tier" in data:
        tier = data["evidence_tier"]
        if not isinstance(tier, int) or tier not in (1, 2, 3, 4, 5):
            errors.append(f"evidence_tier must be one of 1-5, got {tier!r}")
    if "source_anchors" in data:
        anchors = data["source_anchors"]
        if not isinstance(anchors, list) or not anchors or not all(isinstance(a, str) for a in anchors):
            errors.append("source_anchors must be a non-empty list of anchor paths")
    if "kind" in data and data["kind"] not in KIND_VOCABULARY:
        errors.append(f"kind must be one of {sorted(KIND_VOCABULARY)}, got {data['kind']!r}")
    if "realizations" in data:
        realizations = data["realizations"]
        if not isinstance(realizations, dict) or not realizations:
            errors.append("realizations must be a non-empty per-language mapping")
        elif not all(isinstance(v, str) and v for v in realizations.values()):
            errors.append("realizations values must be non-empty strings")
    if "norm_status" in data:
        errors.extend(_validate_norm_status(data["norm_status"]))
    if "row_status" in data and data["row_status"] not in ("attested", "contested", "unattested"):
        errors.append(f"row_status must be one of attested/contested/unattested, got {data['row_status']!r}")
    return errors


def _validate_norm_status(norm: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(norm, dict) or "state" not in norm:
        return ["norm_status must be a mapping with a state field"]
    state = norm["state"]
    if state not in NORM_STATES:
        errors.append(f"norm_status.state must be one of {sorted(NORM_STATES)}, got {state!r}")
        return errors
    if state == "ratified":
        for field in ("ratified_by", "ratified_date", "provenance_anchor"):
            if not norm.get(field):
                errors.append(f"ratified norm requires provenance field: {field}")
    if state == "unratified_variants":
        variants = norm.get("variants")
        if not isinstance(variants, list) or not variants or not all(isinstance(v, str) for v in variants):
            errors.append("unratified_variants requires a non-empty variants list")
    return errors


def validate_directory(path: Path) -> dict[str, list[str]]:
    """Validate every ``*.yaml`` record file under ``path``; return violations."""
    violations: dict[str, list[str]] = {}
    for record_file in sorted(path.glob("*.yaml")):
        data = yaml.safe_load(record_file.read_text(encoding="utf-8"))
        errors = validate_record(data) if isinstance(data, dict) else ["record must be a mapping"]
        if errors:
            violations[record_file.name] = errors
    return violations
