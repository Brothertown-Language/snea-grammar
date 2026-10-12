# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""SC-6 (#118): the notation standard is documented and applied — seed
surface forms are written in the Costa alphabet."""

from pathlib import Path

import yaml

from snea_grammar.render import load_knowledge_base

COSTA_ALPHABET: frozenset[str] = frozenset("aeiouptkčšhmnwyāēīō")


def test_readme_documents_the_standard_and_the_override() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "Costa alphabet" in readme
    assert "IPA" in readme
    assert "override" in readme.lower()


def test_seed_surface_forms_use_the_costa_alphabet() -> None:
    checked = 0
    for path in sorted(Path("data/grammar").glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        form = data.get("surface_form")
        if form is None:
            continue
        stray = sorted(set(str(form)) - COSTA_ALPHABET)
        assert not stray, f"{path.name} surface_form {form!r} strays from the Costa alphabet: {stray}"
        checked += 1
    assert checked >= 1, "the seed knowledge base must exercise the notation check"


def test_records_load_after_notation_check() -> None:
    assert load_knowledge_base().records
