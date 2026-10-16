# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""Spec snea-grammar#3: the PSNEA alternation rules.

Four in-scope rule domains (final PEA *r → š; k-palatalization; the hš
cluster with its reduction gradient; preaspiration hC) plus the š/s-merger
contested row — each as a validated record carrying its evidence tier,
tracked anchors, and explicit status markings.
"""

import subprocess
from pathlib import Path

import yaml

from snea_grammar.model import GrammarRecord
from snea_grammar.render import (
    KnowledgeBase,
    load_knowledge_base,
    render_descriptive,
    render_prescriptive,
    render_teaching,
)
from snea_grammar.validate import validate_directory, validate_record

DOMAIN_RECORDS = {
    "final-r": "PSN-RUL-008",
    "k-palatalization": "PSN-RUL-009",
    "hs-cluster": "PSN-RUL-010",
    "preaspiration": "PSN-RUL-011",
}
MERGER_RECORD = "PSN-RUL-012"


def _load(record_id: str) -> GrammarRecord:
    for path in sorted(Path("data/grammar").glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if data["id"] == record_id:
            return GrammarRecord.from_dict(data)
    raise AssertionError(f"record {record_id} not found")


def test_validator_passes_over_knowledge_base() -> None:
    assert validate_directory(Path("data/grammar")) == {}


def test_all_four_domains_covered() -> None:
    for domain, record_id in DOMAIN_RECORDS.items():
        record = _load(record_id)
        assert record.kind == "rule", domain
        assert record.evidence_tier in (1, 2, 3, 4, 5), domain


def test_contested_markings() -> None:
    merger = _load(MERGER_RECORD)
    assert merger.norm_status is not None
    data = yaml.safe_load(next(p for p in Path("data/grammar").glob("*.yaml") if MERGER_RECORD.replace("PSN-RUL-", "psn-rul-") in p.name).read_text(encoding="utf-8"))
    assert data["row_status"] == "contested"
    statement = merger.statement.lower()
    assert "merged" in statement, "Costa/Goddard position (pre-PSNEA merger) must appear"
    assert "distinct" in statement, "Trumbull-card position (š distinct from s) must appear"
    preasp = _load(DOMAIN_RECORDS["preaspiration"])
    preasp_data = yaml.safe_load(
        next(p for p in Path("data/grammar").glob("*.yaml") if DOMAIN_RECORDS["preaspiration"].replace("PSN-RUL-", "psn-rul-") in p.name).read_text(encoding="utf-8")
    )
    assert preasp_data["row_status"] == "contested"
    assert "record" in preasp.statement.lower() and ("fail" in preasp.statement.lower() or "omit" in preasp.statement.lower() or "unwritt" in preasp.statement.lower())


def test_k_palatalization_carries_the_divergence_note() -> None:
    record = _load(DOMAIN_RECORDS["k-palatalization"])
    assert "diverg" in record.statement.lower(), "the reconstruction-card divergence must be recorded on the rule"


def test_row_status_vocabulary_is_validated() -> None:
    base = {
        "id": "T-1",
        "kind": "rule",
        "title": "t",
        "statement": "s",
        "evidence_tier": 1,
        "source_anchors": ["corpus/docs/research/sources/costa2007.txt"],
        "realizations": {"PSNEA": "x"},
        "norm_status": {"state": "provisional"},
    }
    assert any("row_status" in e for e in validate_record({**base, "row_status": "invented_value"}))
    assert validate_record({**base, "row_status": "contested"}) == []


def test_hs_gradient_realizations() -> None:
    record = _load(DOMAIN_RECORDS["hs-cluster"])
    for language in ("Unquachog", "Loup", "Quiripi", "Montauk"):
        assert language in record.realizations, language
        assert "always" in record.realizations[language].lower() or "occasional" in record.realizations[language].lower()


def test_alternation_rules_render_in_all_three_views() -> None:
    kb: KnowledgeBase = load_knowledge_base()
    for renderer in (render_descriptive, render_teaching, render_prescriptive):
        document = renderer(kb)
        for record_id in (*DOMAIN_RECORDS.values(), MERGER_RECORD):
            assert record_id in document, f"{renderer.__name__} missing {record_id}"
        assert "Evidence standing" in document or "Norm" in document


def test_render_cli_smoke(tmp_path) -> None:
    out = tmp_path / "descriptive.md"
    result = subprocess.run(
        ["uv", "run", "python", "-m", "snea_grammar.render_cli", "--view", "descriptive", "--out", str(out)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert out.read_text(encoding="utf-8").strip()
