# SPDX-FileCopyrightText: 2026 Michael Conrad
# SPDX-License-Identifier: MIT
"""The grammar-record data model.

A grammar record is one structural claim of the PSNEA grammar — a structure,
a paradigm, or a rule — carrying exactly one evidence tier, at least one
source anchor, per-language realizations, and a norm status.

Evidence tiers (spec §2.3, snea-phonetics#118):
  1 — SNEA-attested        4 — Central corroboration (architecture only)
  2 — SNEA-internal        5 — Proto-Algonquian anchor
  3 — Munsee Delaware

Norm states (spec §2.2): ``ratified`` (community decision, with provenance),
``provisional`` (repo default, marked as such), ``unratified_variants``
(variants attested, no norm yet).

Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)
"""

from dataclasses import dataclass
from enum import IntEnum
from typing import Any


class EvidenceTier(IntEnum):
    """The five-tier evidence ladder; every record carries exactly one."""

    SNEA_ATTESTED = 1
    SNEA_INTERNAL = 2
    MUNSEE_DELAWARE = 3
    CENTRAL_CORROBORATION = 4
    PROTO_ALGONQUIAN = 5


KIND_VOCABULARY: frozenset[str] = frozenset({"structure", "paradigm", "rule"})
NORM_STATES: frozenset[str] = frozenset({"ratified", "provisional", "unratified_variants"})

REQUIRED_FIELDS: tuple[str, ...] = (
    "id",
    "kind",
    "title",
    "statement",
    "evidence_tier",
    "source_anchors",
    "realizations",
    "norm_status",
)


@dataclass(frozen=True)
class NormStatus:
    """The norm status of a record: ratified, provisional, or unratified."""

    state: str
    ratified_by: str | None = None
    ratified_date: str | None = None
    provenance_anchor: str | None = None
    variants: tuple[str, ...] = ()


@dataclass(frozen=True)
class GrammarRecord:
    """One structural claim of the PSNEA knowledge base."""

    id: str
    kind: str
    title: str
    statement: str
    evidence_tier: EvidenceTier
    source_anchors: tuple[str, ...]
    realizations: dict[str, str]
    norm_status: NormStatus
    row_status: str | None = None  # attested | contested | unattested (optional)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GrammarRecord":
        norm = data["norm_status"]
        return cls(
            id=str(data["id"]),
            kind=str(data["kind"]),
            title=str(data["title"]),
            statement=str(data["statement"]),
            evidence_tier=EvidenceTier(int(data["evidence_tier"])),
            source_anchors=tuple(str(a) for a in data["source_anchors"]),
            realizations={str(k): str(v) for k, v in data["realizations"].items()},
            norm_status=NormStatus(
                state=str(norm["state"]),
                ratified_by=norm.get("ratified_by"),
                ratified_date=norm.get("ratified_date"),
                provenance_anchor=norm.get("provenance_anchor"),
                variants=tuple(str(v) for v in norm.get("variants", ())),
            ),
            row_status=data.get("row_status"),
        )
