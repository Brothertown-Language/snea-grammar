# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""SC-4/SC-5 (#118): incompleteness is visible and norms are recorded, not
invented — the rendered outputs must carry the markings."""

import pytest

from snea_grammar.render import (
    KnowledgeBase,
    load_knowledge_base,
    render_descriptive,
    render_prescriptive,
)


@pytest.fixture
def kb() -> KnowledgeBase:
    return load_knowledge_base()


def _section(document: str, record_id: str) -> str:
    start = document.index(record_id)
    next_at = document.find("### ", start + len(record_id))
    return document[start : next_at if next_at != -1 else len(document)]


def test_descriptive_marks_tier4_as_corroborative(kb: KnowledgeBase) -> None:
    section = _section(render_descriptive(kb), "PSN-STR-003")
    assert "corroborative" in section.lower()


def test_descriptive_marks_tier5_as_reconstructed(kb: KnowledgeBase) -> None:
    section = _section(render_descriptive(kb), "PSN-STR-004")
    assert "reconstructed" in section.lower()


def test_descriptive_marks_provisional_norm_status(kb: KnowledgeBase) -> None:
    section = _section(render_descriptive(kb), "PSN-STR-001")
    assert "not community-ratified" in section


def test_prescriptive_prints_no_norm_yet(kb: KnowledgeBase) -> None:
    section = _section(render_prescriptive(kb), "PSN-RUL-006")
    assert "no norm yet — variants attested" in section
    assert "n — Coweset" in section and "y — Narragansett" in section


def test_prescriptive_prints_ratified_norm_with_provenance(kb: KnowledgeBase) -> None:
    section = _section(render_prescriptive(kb), "PSN-RUL-005")
    assert "Norm in force" in section
    assert "2026-10-11" in section
    assert "snea-phonetics#118" in section
