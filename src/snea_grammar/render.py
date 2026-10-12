# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""The three renderers over the single knowledge base.

Descriptive, teaching, and prescriptive views all consume the same validated
records; they differ in presentation and in what they surface about norms
and evidence. Renderers are pure functions over a loaded ``KnowledgeBase`` —
dependencies are supplied from outside; the CLI wires them.

Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .model import GrammarRecord
from .registry import DEFAULT_LANGUAGES_PATH, DEFAULT_REGISTRY_PATH, load_languages, load_sources
from .validate import validate_directory

DEFAULT_GRAMMAR_DIR = Path("data/grammar")

TIER_NAMES: dict[int, str] = {
    1: "SNEA-attested",
    2: "SNEA-internal comparison",
    3: "Munsee Delaware outgroup",
    4: "Central Algonquian corroboration",
    5: "Proto-Algonquian reconstruction",
}


@dataclass(frozen=True)
class KnowledgeBase:
    """The validated knowledge base: records plus the two registries."""

    records: tuple[GrammarRecord, ...]
    sources: tuple[dict[str, Any], ...]
    languages: tuple[dict[str, Any], ...]


def load_knowledge_base(
    grammar_dir: Path = DEFAULT_GRAMMAR_DIR,
    sources_path: Path = DEFAULT_REGISTRY_PATH,
    languages_path: Path = DEFAULT_LANGUAGES_PATH,
) -> KnowledgeBase:
    """Load and validate the knowledge base; raise on schema violations."""
    violations = validate_directory(grammar_dir)
    if violations:
        detail = "; ".join(f"{name}: {errors}" for name, errors in violations.items())
        raise ValueError(f"knowledge base failed validation: {detail}")
    import yaml

    records = tuple(
        GrammarRecord.from_dict(yaml.safe_load(p.read_text(encoding="utf-8"))) for p in sorted(grammar_dir.glob("*.yaml"))
    )
    return KnowledgeBase(
        records=records,
        sources=tuple(load_sources(sources_path)),
        languages=tuple(load_languages(languages_path)),
    )


EVIDENCE_STANDING: dict[int, str] = {
    1: "attested — recorded in SNEA primary documentation",
    2: "comparative — reconstructed by SNEA-internal comparison",
    3: "outgroup — from the Munsee Delaware comparison",
    4: "corroborative — Central Algonquian material corroborates the architecture; no surface form is borrowed from it",
    5: "reconstructed — Proto-Algonquian anchor; not SNEA-attested",
}


def _record_section(record: GrammarRecord) -> list[str]:
    lines = [
        f"### {record.id} — {record.title}",
        "",
        f"*Kind:* {record.kind}  |  *Evidence tier:* {record.evidence_tier} ({TIER_NAMES[record.evidence_tier]})",
        "",
        f"*Evidence standing:* {EVIDENCE_STANDING[record.evidence_tier]}",
        "",
        record.statement,
        "",
        "Realizations:",
        "",
    ]
    lines.extend(f"- **{lang}:** {value}" for lang, value in record.realizations.items())
    lines.extend(["", f"Sources: {', '.join(record.source_anchors)}"])
    return lines


def render_descriptive(kb: KnowledgeBase) -> str:
    """The evidence-tiered view: every claim carries its evidence."""
    lines = [
        "# SNEA grammar — descriptive view",
        "",
        "One shared structural system for the SNEA languages. Every claim",
        "carries exactly one evidence tier and its source anchors.",
        "",
    ]
    for record in kb.records:
        lines.extend(_record_section(record))
        norm = record.norm_status
        if norm.state == "provisional":
            lines.append("Norm status: provisional — not community-ratified; a repo default standing until decided")
        else:
            lines.append(f"Norm status: {norm.state}")
        lines.append("")
    return "\n".join(lines)


def render_teaching(kb: KnowledgeBase) -> str:
    """The pedagogical view: the same core, sequenced and example-led."""
    lines = [
        "# SNEA grammar — teaching view",
        "",
        "The grammar of the Southern New England Algonquian languages,",
        "taught from their shared structure. Where a point is not yet",
        "settled, that is stated plainly rather than glossed over.",
        "",
        "## Start here: how the language is built",
        "",
    ]
    by_kind: dict[str, list[GrammarRecord]] = {}
    for record in kb.records:
        by_kind.setdefault(record.kind, []).append(record)
    kind_intro = {
        "structure": "## Structures — what every SNEA sentence is made of",
        "rule": "## Rules — how forms relate to each other",
        "paradigm": "## Paradigms — the shape of the endings",
    }
    for kind in ("structure", "rule", "paradigm"):
        if kind not in by_kind:
            continue
        lines.extend(["", kind_intro[kind], ""])
        for record in by_kind[kind]:
            lines.extend(_record_section(record))
            lines.append("")
    lines.extend(
        [
            "## Where this comes from",
            "",
            "Every point above carries its evidence tier — from attested",
            "colonial-era text down to family-level reconstruction — so you can",
            "see how firm each piece is.",
            "",
        ]
    )
    return "\n".join(lines)


def render_prescriptive(kb: KnowledgeBase) -> str:
    """The norm view: what is in force, recorded — never invented."""
    lines = [
        "# SNEA grammar — prescriptive view",
        "",
        "The norm layer of the grammar. Norms are recorded, not invented:",
        "where a community has decided, the decision is cited; where it has",
        "not, the variants are stated and the decision is left to the",
        "community.",
        "",
    ]
    for record in kb.records:
        norm = record.norm_status
        lines.extend([f"### {record.id} — {record.title}", ""])
        if norm.state == "ratified":
            lines.append(f"**Norm in force:** {record.statement.splitlines()[0]}")
            lines.append("")
            lines.append(f"Ratified by {norm.ratified_by}, {norm.ratified_date} ({norm.provenance_anchor}).")
        elif norm.state == "unratified_variants":
            lines.append("**no norm yet — variants attested:**")
            lines.append("")
            lines.extend(f"- {variant}" for variant in norm.variants)
            lines.append("")
            lines.append("Choosing among these is a community decision, recorded here when made.")
        else:
            lines.append(f"**Provisional default (not community-ratified):** {record.statement.splitlines()[0]}")
            lines.append("")
            lines.append("This default stands until a community ratification is recorded.")
        lines.append("")
    return "\n".join(lines)
