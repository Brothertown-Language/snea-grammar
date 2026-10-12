<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->
<!-- SPDX-License-Identifier: MIT -->

# snea-grammar

Grammar knowledge base for Southern New England Algonquian (SNEA): the
**Proto-SNEA (PSNEA) grammar** — one shared structural system for the SNEA
languages, with per-language realization layers — rendered as **descriptive**,
**teaching**, and **prescriptive** grammar documents from a single
machine-readable knowledge base.

Part of the Brothertown Language Development Project: the project works
toward a proper synthesis of the ancestor SNEA varieties the Brothertown
people historically spoke; PSNEA is the neutral ancestral foundation that
synthesis builds on.

## Notation standard

Surface forms are written in the **Costa alphabet** — the phonemic
orthography used in the scholarly SNEA literature: vowels `a e i o u` with
length marking (`ā ē ī ō`), consonants `p t k č s š h m n w y`, preaspiration
written as `h` before stops. **IPA** carries phonemic precision where the
alphabet alone is not enough. Community-facing orthographies (e.g. the
Wôpanâak orthography) are **rendering overrides** applied at display time —
the storage form is always the Costa alphabet.

## The three renderers

    uv run python -m snea_grammar.render_cli --view descriptive   # evidence-tiered
    uv run python -m snea_grammar.render_cli --view teaching      # pedagogical
    uv run python -m snea_grammar.render_cli --view prescriptive  # norm layer

All three consume the same knowledge base under `data/grammar/`.

## Status

Repository establishment increment — see `AGENTS.md` for the architecture,
governance, and scope record (the design record: scope, single-source
multi-render, evidence tiers, membership, notation, governance, roadmap),
and the spec at `Brothertown-Language/snea-phonetics#118` for the
requirements. For the forward work map — pending items, blockers, and
interdependencies — see [`ROADMAP.md`](ROADMAP.md).

## License

MIT — see `LICENSE`.

---

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
