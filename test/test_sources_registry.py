# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""SC-7 (#118): the source registry's governance classification.

The registry distinguishes colonial-era/scholarly sources from modern
community dictionaries; community dictionaries are marked excluded-by-default
(governance-gated); colonial/scholarly anchors carry their evidence-tier
roles.
"""

import pytest

from snea_grammar.registry import load_sources

REGISTRY_PATH = "data/sources.yaml"


@pytest.fixture
def sources() -> dict[str, dict]:
    entries = load_sources(REGISTRY_PATH)
    return {e["id"]: e for e in entries}


def test_modern_mohegan_dictionary_is_gated(sources: dict[str, dict]) -> None:
    entry = sources["modern-mohegan-dictionary"]
    assert entry["class"] == "community_dictionary"
    assert entry["governance"] == "excluded_by_default"


def test_every_community_dictionary_is_gated(sources: dict[str, dict]) -> None:
    community = [e for e in sources.values() if e["class"] == "community_dictionary"]
    assert community, "registry must classify its community dictionaries"
    assert all(e.get("governance") == "excluded_by_default" for e in community)


def test_colonial_and_scholarly_anchors_carry_tier_roles(sources: dict[str, dict]) -> None:
    expectations = {
        "eliot-bible-1663": "tier1",
        "eliot-grammar-1666": "tier1",
        "costa-2007": "tier2",
        "hewson-1993": "tier5",
        "aubin-1975": "tier5",
    }
    for source_id, expected_role in expectations.items():
        assert expected_role in sources[source_id]["tier_roles"], source_id


def test_no_community_dictionary_is_included_by_default(sources: dict[str, dict]) -> None:
    gated = {e["id"] for e in sources.values() if e.get("governance") == "excluded_by_default"}
    community = {e["id"] for e in sources.values() if e["class"] == "community_dictionary"}
    assert community <= gated


def test_disavowal_recorded_for_the_mohegan_dictionary(sources: dict[str, dict]) -> None:
    entry = sources["modern-mohegan-dictionary"]
    assert "disavowed" in entry["note"].lower()
