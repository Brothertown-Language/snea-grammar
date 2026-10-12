# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""Registry loading (sources, languages).

The source registry classifies every source the knowledge base may anchor to:
``colonial_primary`` and ``scholarly_edition`` sources are usable and carry
their evidence-tier roles; ``community_dictionary`` sources are
``excluded_by_default`` (community property — use requires explicit
authorization from the owning community).

The languages registry carries the PSNEA membership determination (Costa
2007): ``member``, ``uncertain``, ``projected`` (dataless ancestors covered by
PSNEA projection), or ``neighbor`` (comparative languages outside the group).

Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)
"""

from pathlib import Path
from typing import Any

import yaml

DEFAULT_REGISTRY_PATH = Path("data/sources.yaml")
DEFAULT_LANGUAGES_PATH = Path("data/languages.yaml")


def load_sources(path: Path | str = DEFAULT_REGISTRY_PATH) -> list[dict[str, Any]]:
    """Load the source registry; return its entries as mappings."""
    source = Path(path)
    data = yaml.safe_load(source.read_text(encoding="utf-8"))
    return list(data["sources"])


def load_languages(path: Path | str = DEFAULT_LANGUAGES_PATH) -> list[dict[str, Any]]:
    """Load the languages registry; return its entries as mappings."""
    source = Path(path)
    data = yaml.safe_load(source.read_text(encoding="utf-8"))
    return list(data["languages"])
