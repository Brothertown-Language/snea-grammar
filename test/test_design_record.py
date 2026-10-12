# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""SC-10 (#118): the repo documents its scope boundaries and design — the
design record (structure-only scope, single-source multi-render, evidence
tiers, coverage/membership, notation, governance, roadmap) is present in the
repo's README/AGENTS.md."""

from pathlib import Path

DOCS = "\n".join(p.read_text(encoding="utf-8") for p in (Path("README.md"), Path("AGENTS.md"))).lower()


def test_scope_structure_only() -> None:
    assert "grammatical structure" in DOCS
    assert "vocabulary" in DOCS and "pointer" in DOCS
    assert "snea-phonetics" in DOCS


def test_single_source_multi_render() -> None:
    assert "single" in DOCS and "knowledge base" in DOCS
    for view in ("descriptive", "teaching", "prescriptive"):
        assert view in DOCS, view


def test_evidence_tiers_documented() -> None:
    for marker in ("snea-attested", "snea-internal", "munsee", "central", "proto-algonquian"):
        assert marker in DOCS, marker


def test_membership_documented() -> None:
    for language in ("massachusett-coweset", "narragansett", "mohegan-pequot-montauk", "quiripi", "unquachog", "loup", "niantic"):
        assert language in DOCS, language
    assert "neighbor" in DOCS


def test_notation_documented() -> None:
    assert "costa alphabet" in DOCS and "ipa" in DOCS


def test_governance_documented() -> None:
    assert "excluded" in DOCS
    assert "modern mohegan dictionary" in DOCS or "community dictionary" in DOCS


def test_roadmap_documented() -> None:
    assert "brothertown language" in DOCS
    assert "phase 1" in DOCS or "phase 2" in DOCS
