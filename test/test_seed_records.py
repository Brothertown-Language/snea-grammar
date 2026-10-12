# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""SC-4/SC-5 data side (#118): the seed knowledge base validates and carries
the marking states the renderers must surface; the languages registry carries
the PSNEA membership determination."""

from pathlib import Path

import yaml

from snea_grammar.model import GrammarRecord
from snea_grammar.registry import load_languages
from snea_grammar.validate import validate_directory

GRAMMAR_DIR = "data/grammar"


def _all_records() -> list[GrammarRecord]:
    records = []
    for path in sorted(Path(GRAMMAR_DIR).glob("*.yaml")):
        records.append(GrammarRecord.from_dict(yaml.safe_load(path.read_text(encoding="utf-8"))))
    return records


def test_validator_passes_over_seed_directory() -> None:
    assert validate_directory(Path(GRAMMAR_DIR)) == {}


def test_seed_carries_tier4_and_tier5_records() -> None:
    by_id = {r.id: r for r in _all_records()}
    assert by_id["PSN-STR-003"].evidence_tier == 4
    assert by_id["PSN-STR-004"].evidence_tier == 5


def test_seed_carries_ratified_norm_with_provenance() -> None:
    by_id = {r.id: r for r in _all_records()}
    norm = by_id["PSN-RUL-005"].norm_status
    assert norm.state == "ratified"
    assert norm.ratified_by and norm.ratified_date and norm.provenance_anchor


def test_seed_carries_unratified_variant_point() -> None:
    by_id = {r.id: r for r in _all_records()}
    norm = by_id["PSN-RUL-006"].norm_status
    assert norm.state == "unratified_variants"
    assert len(norm.variants) >= 2


def test_every_seed_record_resolves_through_the_model() -> None:
    records = _all_records()
    assert records, "seed knowledge base must not be empty"
    assert all(r.source_anchors for r in records)
    assert all(r.realizations for r in records)


def test_languages_registry_membership() -> None:
    languages = {entry["name"]: entry["status"] for entry in load_languages()}
    members = {name for name, status in languages.items() if status == "member"}
    expected_members = {
        "Massachusett-Coweset",
        "Narragansett proper",
        "Mohegan-Pequot-Montauk",
        "Quiripi-Naugatuck",
        "Unquachog",
        "Loup",
        "Western Niantic",
        "Eastern Niantic",
    }
    assert members == expected_members
    assert languages["Delaware-Mahican"] == "neighbor"
    assert languages["Abenaki"] == "neighbor"
    for dataless in ("Tunxis", "Siwanoy", "Setauket"):
        assert languages[dataless] == "projected", dataless
    assert languages["Etchemin"] == "uncertain"
