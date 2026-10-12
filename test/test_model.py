# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""SC-2 (#118): the knowledge-base data model and its validator.

Every grammar record carries (a) exactly one evidence tier from the tier
vocabulary, (b) at least one source anchor, (c) per-language realization
fields, (d) norm status with provenance fields or explicit provisional
status. The validator must reject records missing any of these and accept
well-formed ones.
"""

import pytest

from snea_grammar.model import GrammarRecord
from snea_grammar.validate import validate_record

WELLFORMED: dict = {
    "id": "PSN-001",
    "kind": "structure",
    "title": "Seed structure",
    "statement": "A well-formed grammar record statement.",
    "evidence_tier": 1,
    "source_anchors": ["corpus/docs/research/sources/costa2007.txt"],
    "realizations": {"PSNEA": "the shared form"},
    "norm_status": {"state": "provisional"},
}


def test_validator_accepts_wellformed_record() -> None:
    assert validate_record(WELLFORMED) == []


def test_validator_rejects_missing_evidence_tier() -> None:
    broken = {k: v for k, v in WELLFORMED.items() if k != "evidence_tier"}
    errors = validate_record(broken)
    assert errors, "missing evidence_tier must be rejected"
    assert any("evidence_tier" in e for e in errors)


def test_validator_rejects_out_of_vocabulary_tier() -> None:
    broken = {**WELLFORMED, "evidence_tier": 6}
    assert any("evidence_tier" in e for e in validate_record(broken))


def test_validator_rejects_empty_source_anchors() -> None:
    broken = {**WELLFORMED, "source_anchors": []}
    assert any("source_anchors" in e for e in validate_record(broken))


def test_validator_rejects_missing_realizations() -> None:
    broken = {k: v for k, v in WELLFORMED.items() if k != "realizations"}
    assert any("realizations" in e for e in validate_record(broken))


def test_validator_rejects_missing_norm_status() -> None:
    broken = {k: v for k, v in WELLFORMED.items() if k != "norm_status"}
    assert any("norm_status" in e for e in validate_record(broken))


def test_ratifed_norm_requires_provenance_fields() -> None:
    broken = {**WELLFORMED, "norm_status": {"state": "ratified"}}
    assert any("provenance" in e or "ratified" in e for e in validate_record(broken))


def test_unratified_variants_require_variants_list() -> None:
    broken = {**WELLFORMED, "norm_status": {"state": "unratified_variants"}}
    assert any("variants" in e for e in validate_record(broken))


def test_wellformed_record_loads_into_model() -> None:
    record = GrammarRecord.from_dict(WELLFORMED)
    assert record.id == "PSN-001"
    assert record.evidence_tier == 1


def test_unknown_norm_state_rejected() -> None:
    broken = {**WELLFORMED, "norm_status": {"state": "invented_state"}}
    assert validate_record(broken)


@pytest.mark.parametrize(
    "field",
    ["id", "kind", "title", "statement", "evidence_tier", "source_anchors", "realizations", "norm_status"],
)
def test_validator_rejects_missing_required_field(field: str) -> None:
    broken = {k: v for k, v in WELLFORMED.items() if k != field}
    assert any(field in e for e in validate_record(broken))
