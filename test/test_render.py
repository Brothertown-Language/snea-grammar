# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""SC-3 (#118): three renderers — descriptive, teaching, prescriptive —
each consume the same knowledge base and produce a human-readable document."""

import pytest

from snea_grammar.render import (
    KnowledgeBase,
    load_knowledge_base,
    render_descriptive,
    render_prescriptive,
    render_teaching,
)

SEED_IDS = ["PSN-STR-001", "PSN-RUL-002", "PSN-STR-003", "PSN-STR-004", "PSN-RUL-005", "PSN-RUL-006", "PSN-PAR-007"]


@pytest.fixture
def kb() -> KnowledgeBase:
    return load_knowledge_base()


@pytest.mark.parametrize("renderer", [render_descriptive, render_teaching, render_prescriptive])
def test_each_renderer_produces_a_document_with_the_seed_records(kb: KnowledgeBase, renderer) -> None:
    document = renderer(kb)
    assert document.strip(), f"{renderer.__name__} produced an empty document"
    for record_id in SEED_IDS:
        assert record_id in document, f"{renderer.__name__} missing {record_id}"


def test_renderers_share_one_knowledge_base(kb: KnowledgeBase) -> None:
    assert len(kb.records) == len(SEED_IDS)
    assert kb.sources and kb.languages


def test_render_cli_writes_all_three_views(tmp_path) -> None:
    import subprocess

    for view in ("descriptive", "teaching", "prescriptive"):
        out = tmp_path / f"{view}.md"
        result = subprocess.run(
            ["uv", "run", "python", "-m", "snea_grammar.render_cli", "--view", view, "--out", str(out)],
            capture_output=True,
            text=True,
            check=True,
        )
        assert result.returncode == 0
        assert out.read_text(encoding="utf-8").strip()
