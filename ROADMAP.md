<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->
<!-- SPDX-License-Identifier: MIT -->

# ROADMAP — work map and resumption guide

**Currency date: 2026-10-12.** This file orients a fresh-context agent
resuming the snea-grammar work. It carries the work-ordering logic, the
blockers, and the design-session rules that are not yet written anywhere
else. **Specs govern, not this file**: every work item below goes through
spec → plan → implement on its own issue before any code or data changes,
and where this map and a spec disagree, the spec wins. Update this map in
the same cycle as any change to the items it tracks.

## First-stop reading list

1. `AGENTS.md` — the design record (scope, architecture, tiers, membership,
   notation, governance, roadmap) and the exports contract.
2. The establishment spec: `Brothertown-Language/snea-phonetics#118`
   (`.issues/118/spec.md` in the snea-phonetics issue store) and its plan
   (`.issues/118/plan.md`) — the requirements the repository was built and
   verified against.
3. This file.
4. `docs/research/snea-grammar-feasibility.md` on branch
   `feature/snea-grammar-feasibility` of `snea-phonetics` — the feasibility
   research card that grounds all of it (live-verified 2026-10-11).

## Current state (2026-10-12)

| Fact | Value |
|------|-------|
| Repository established | PR #1 merged (merge commit `cae87c3`, 2026-10-12), closing snea-phonetics#118 |
| Corpus submodule pin | `algonquian-library` release tag **v0.1.2** (`53c837e`) — anchors verified against it |
| Test/verification state | 59 tests green; ruff + pyright clean at merge; fresh-context verify PASS on all ten SCs |
| Unmerged provenance | `feature/snea-grammar-feasibility` branch in snea-phonetics (research card + corpus pin sync; commits `942260b`, `69bccb7`, `5298580`) |
| Known governance conflict | The corpus MANIFEST (`corpus/docs/research/sources/MANIFEST.md`, "Sources Identified for Future Mirroring") lists *A Modern Mohegan Dictionary* as **High-priority for mirroring** — contrary to the project ruling below (item W4) |

## Operating rules — decided in the 2026-10-11 design session

These shaped the established design and bind every follow-on item. They are
expanded in the spec and the AGENTS.md design record; repeated here because
a fresh agent is most likely to trip on exactly these:

1. **Norms are recorded, not invented.** "No norm yet — variants attested"
   is a valid prescriptive state; provisional repo defaults render marked.
   Community ratification is recorded as data with provenance (ratifying
   body, date) — never manufactured by the agent.
2. **Central Algonquian material corroborates architecture, never supplies
   surface forms.** Surface forms trace to SNEA attestation or PSNEA
   reconstruction. (Tier-4 corroboration currently draws on the Ojibwe
   component datasets in the corpus submodule; Cree — named in the spec's
   tier vocabulary — is not mirrored yet.)
3. **Community dictionaries are excluded by default.** Community property;
   use requires explicit authorization from the owning community. Ruling
   basis: the Modern Mohegan Dictionary has been **disavowed by the Mohegan
   Nation** (developer ruling, 2026-10-11 session; no public record located —
   recorded on session authority in the feasibility card §5.1).
4. **PSNEA forms lead.** Phase 1 is the PSNEA grammar; the Brothertown
   Language — the community-ratified synthesis of the ancestor varieties —
   is Phase 2, built over the PSNEA core, not as a separate grammar.
5. **Renderers run on incomplete content.** "Even if incompletely to start
   off with" — incompleteness is visible in output, never silently absorbed.
6. **No invented linguistic content.** Every claim carries a tracked source
   anchor; verification honesty applies to every factual statement.
7. **No regex for orthography→phoneme conversion** (standing finding of
   snea-phonetics cards #2, #4, #7). The boundary with snea-phonetics: this
   repository emits Costa-alphabet forms plus the alternation rules that
   derive them; snea-phonetics handles orthographic/phonetic realization.
8. **Notation: Costa alphabet + IPA**, unless special instructions state
   otherwise (the recorded project decision — the seed's one ratified norm).

## Work items, blockers, interdependencies

| ID | Item | Repo | Blocked on | Unblocks |
|----|------|------|------------|----------|
| W1 | **Alternation rules (morphophonology) spec** — PEA *r → š/s; k-palatalization before PEA *m / PA *i; the hš cluster with its reduction gradient (Unquachog always, Loup almost, Quiripi/Montauk occasionally); preaspiration hC retention; vowel correspondences — including the contested rows (š/s merger, the *e· discrepancy, schwa status) carried with the tracked discipline's marking | snea-grammar | — (unblocked: Costa 2007 is mirrored at v0.1.2) | Phase 1 core content |
| W2 | **PSNEA paradigm architecture spec** — tier-1 attestation leading: person/number/obviation exponents, the four verb subtypes (AI/II/TA/TI), independent vs. conjunct orders, possessed-noun inflection; Bloomfield 1946 (mirrored) as the tier-5 skeleton, Ojibwe datasets as tier-4 corroboration | snea-grammar | **W5** (Eliot 1666 paradigms are the tier-1 lead and are not mirrored) | Phase 1 core content; W3 |
| W3 | **Brothertown Language realization profile spec (Phase 2)** — the community-ratified synthesis over the PSNEA core: norm provenance recording, the realization/exponent layer, community-orthography rendering overrides (display-time only) | snea-grammar | **W1 + W2** content, **and** the community ratification process itself (community-gated, not agent-gated — do not fabricate ratifications) | Phase 2 |
| W4 | **Governance annotation** on the Modern Mohegan Dictionary catalogue card (`corpus/docs/research/modern-mohegan-dictionary.md`) **and the MANIFEST row** — resolve the live conflict between the mirroring priority and the disavowal ruling | algonquian-library | — (unblocked) | Clean governance surface for every later item |
| W5 | **Mirror Eliot 1666** (*The Indian Grammar Begun*) in the corpus | algonquian-library | — (unblocked) | **W2**; tier-1 paradigm records generally |
| W6 | **Mirror Munsee Delaware materials** in the corpus — the tier-3 outgroup has zero corpus presence today (only Delaware-*Mahican* neighbor material: Schmick/Edwards/Masthay) | algonquian-library | — (unblocked) | All tier-3 records |
| W7 | **PR for `feature/snea-grammar-feasibility`** (snea-phonetics) — merges the feasibility research card + corpus pin sync; the provenance anchor for this whole program | snea-phonetics | — (unblocked) | Provenance durable in the tracked tree |

**Suggested order.** Start W1 (core, unblocked), W4 (urgent — governance
conflict with the project ruling), and W5 (+W6 in parallel) together; W2
follows the W5 merge; W3 waits on content and the community process; W7
anytime. Items sharing an authorization share one branch and one PR per
issue ticket.

## Provenance

- Design discussion: 2026-10-11 session (developer-directed); finalized by
  the developer's "ready for spec" and executed under "approved for PR".
- Spec/plan: snea-phonetics#118 — `.issues/118/{spec,plan}.md`.
- Feasibility card: `docs/research/snea-grammar-feasibility.md` (see W7).
- PSNEA membership and dialectology: tracked mirror
  `corpus/docs/research/sources/costa2007.txt` (Costa 2007, PAC 38).

---

*Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)*
