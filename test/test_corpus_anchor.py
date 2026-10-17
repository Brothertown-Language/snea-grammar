# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""SC-8 (#118): the corpus relationship is wired — the corpus submodule is
present and every seed record's source anchor resolves to an existing path
under it."""

from pathlib import Path

import pytest
import yaml


def _records() -> list[dict]:
    return [yaml.safe_load(p.read_text(encoding="utf-8")) for p in sorted(Path("data/grammar").glob("*.yaml"))]


def test_corpus_submodule_is_materialized() -> None:
    corpus = Path("corpus")
    assert (corpus / ".git").exists(), "corpus submodule not initialized — run git submodule update --init"
    assert (corpus / "docs").is_dir()


@pytest.mark.parametrize("record", _records(), ids=lambda r: r["id"])
def test_seed_anchor_resolves_under_corpus(record: dict) -> None:
    for anchor in record["source_anchors"]:
        # Anchors point into the corpus submodule, or into the repo's private
        # library for developer-directed sources (e.g. the Cunningham
        # adjustments, 2026-10-16) — the private library is a gitignored,
        # session-local authority surface.
        assert anchor.startswith(("corpus/", "private/")), (
            f"{record['id']} anchor {anchor} must point into the corpus submodule or the private library"
        )
        assert Path(anchor).is_file(), f"{record['id']} anchor {anchor} does not resolve"


def test_anchor_path_is_relative_to_repo_root() -> None:
    for record in _records():
        for anchor in record["source_anchors"]:
            assert not anchor.startswith("/"), f"{record['id']} anchor must be repo-relative"
