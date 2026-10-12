<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->
<!-- SPDX-License-Identifier: MIT -->
<!-- Provenance: AI-authored, OpenCode (huggingface/zai-org/GLM-5.3-Flash); established per Brothertown-Language/snea-phonetics#118 -->

# AGENTS.md — snea-grammar

Grammar knowledge base for Southern New England Algonquian (SNEA): the PSNEA
grammar — one shared structural system for the SNEA languages with
per-language realization layers — rendered as descriptive, teaching, and
prescriptive grammar documents from a single machine-readable knowledge base.

## Design Record

**Scope — grammatical structure only.** This repository owns grammar:
paradigm architecture, morphosyntax, and alternation (alternation is
grammar). Vocabulary is pointer-only — lexical claims reference the corpus
and community dictionaries; no blended lexicon is built here. Phonetic
realization is `snea-phonetics`' domain: the boundary between the two
repositories is the derived form written in the Costa alphabet plus the
alternation rules that derive it.

**Architecture — single source, multi-render.** One knowledge base
(`data/grammar/`, validated records) feeds three renderers:
descriptive (every claim carrying its evidence tier), teaching (the same
core presented pedagogically), and prescriptive (the norm layer). Rules
binding all three: incompleteness is visible, never silently absorbed; norms
are recorded, not invented (no norm yet — variants attested — is a valid
state); Central Algonquian material corroborates architecture and never
supplies surface forms.

**Evidence tiers.** 1 — SNEA-attested; 2 — SNEA-internal comparison;
3 — Munsee Delaware outgroup; 4 — Central corroboration (Ojibwe, Cree);
5 — Proto-Algonquian anchors. Every record carries exactly one tier and its
source anchors.

**Coverage and membership.** PSNEA membership per Costa 2007:
Massachusett-Coweset, Narragansett proper, Mohegan-Pequot-Montauk,
Quiripi-Naugatuck, Unquachog, Loup, Western and Eastern Niantic; Etchemin
uncertain; the dataless ancestors (Tunxis, Siwanoy, Setauket) are covered by
PSNEA projection. Delaware-Mahican and Abenaki are neighbors, not members.

**Notation.** Costa alphabet + IPA (see README for the standard and the
override rule), unless special instructions state otherwise.

**Governance.** The knowledge base builds from colonial-era primary sources
and scholarly editions. Modern community dictionaries are community
property and excluded by default — use requires explicit authorization from
the owning community. Ruling basis: the Modern Mohegan Dictionary has been
disavowed by the Mohegan Nation (project ruling, 2026-10-11). The source
registry (`data/sources.yaml`) carries the classification mechanically.

**Roadmap.** Phase 1 — the PSNEA grammar, PSNEA forms leading the rendered
output. Phase 2 — the Brothertown Language: the community-ratified synthesis
of the ancestor varieties' realization profiles over the PSNEA core.

## Repository Structure

| Path | What it is |
|------|-----------|
| `AGENTS.md` | This project guide — carries the exports contract (below). |
| `.gitignore` | Founding ignore rules — build dirs, `tmp/`, and the `.issues/` worktree are never tracked. |
| `.issues/` | Git **worktree** (orphan `issues-data` branch) holding all issue specs and artifacts. NOT a regular directory — see the worktree discipline section below. |
| `data/` | The knowledge base: grammar records (`data/grammar/`), the languages registry (`data/languages.yaml`), the source registry (`data/sources.yaml`). |
| `src/snea_grammar/` | Loader, validator, and the three renderers (descriptive / teaching / prescriptive) + CLI. |
| `test/` | Test suite. |
| `corpus/` | Submodule mount of the companion corpus repository (`algonquian-library`) — source mirrors the knowledge base anchors resolve against. |
| `pyproject.toml` | Toolchain declaration: pytest configuration, dev dependencies, lint/type configuration. |

## Exports Contract (machine contract)

This repository publishes a three-part exports surface to consumers:

1. **the knowledge base** — validated grammar records under `data/grammar/`
   (plus the languages and source registries);
2. **the rendered grammar documents** — descriptive, teaching, and
   prescriptive renderings produced by the renderers;
3. **the source registry** — the governance classification of every source
   the knowledge base may anchor to.

The exports contract is the only shared language between this repository and
its consumers (the Brothertown Language Development Project; `snea-phonetics`
consumes the boundary surface — derived forms written in the Costa alphabet
plus the alternation rules that derive them — and handles orthographic/
phonetic realization).

## The `.issues/` Worktree — CRITICAL

`.issues/` is a git worktree on an orphan `issues-data` branch, NOT a regular
directory. It is gitignored in the parent repo.

- All git operations against `.issues/` MUST run as `git -C .issues/ <command>`
  or via the local-issues tool.
- The parent repo's `git add .issues/` is FORBIDDEN — it corrupts git state.
- The worktree holds all issue specs, plans, and artifacts.

## Build / Test / Lint / Type-Check

| Task | Command | Note |
|------|---------|------|
| Sync dependencies | `uv sync` | Uses `pyproject.toml` |
| Run tests | `uv run pytest test/` | Full suite |
| Lint | `uvx ruff check src/ test/` | Python only |
| Type check | `uvx pyright src/` | Python only |

**Never** use bare `python`, `python3`, or `pip` — always prefix with
`uv run`/`uvx`.

## Agent Operating Conventions

- **Temp files**: all temporary scripts and output go ONLY in
  `{project_root}/tmp/` — never `/tmp/` or any other path. Clean up temp
  files after tasks.
- **AI attribution**: AI-authored content MUST include
  `Co-authored with AI: <AgentName> (<ModelId>)` (module docstrings, README
  footer, posted content last line).
- **Verification honesty**: never report memory as verified — every factual
  claim needs a live tool call.

---

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
