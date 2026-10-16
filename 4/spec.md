---
issue_number: 4
title: "[SPEC] PSNEA paradigm architecture — Goddard & Bragdon primary (blocked on its mirror); Eliot 1666 secondary"
state: open
created_at: "2026-10-12T04:50:00Z"
synced_from: "https://github.com/Brothertown-Language/snea-grammar/issues/4"
---

# PSNEA paradigm architecture — tier-1 attestation leading

**Author:** AI agent
**Design source:** the 2026-10-11/12 design sessions (developer rulings, recorded in the
snea-phonetics#118 design record and the developer-approved `ROADMAP.md`, item W2);
revised 2026-10-12 per the developer's guidance on the authority of
**Dr. Keith Cunningham** (historical linguist, Nanticoke Language Project; Georgetown
PhD 2024, historical phonology of Nanticoke — verified live): "the Goddard Bragdon
Natick grammar is the primary grammar to use. fill in missing pieces and usage can be
taken from Nishnaabemwin Reference Grammar plus other items like the Cree grammar."

## 1. Goal

Assemble the PSNEA paradigm architecture — the inflectional system itself — as
grammar records, with tier-1 attestation leading: the design session's directive is
that PSNEA forms lead the rendered output once available, per-language realization
layers carry the differences, and dataless ancestors are covered by projection.

## 2. Design record

### 2.1 Dependency (hard gate) and the attestation ranking

**Per Dr. Keith Cunningham's guidance (2026-10-12), the primary grammar is Goddard &
Bragdon 1988** — *Native Writings in Massachusett* (APS Memoir 185): the scholarly
edition of the native-written Natick/Massachusett corpus, with its grammatical
analysis of that corpus. **Implementation is blocked on the Goddard & Bragdon
mirror** (algonquian-library#34, where it is now the primary target). Eliot 1666
(*The Indian Grammar Begun*, dense paradigm sets) is demoted to the secondary
attestation stream — still mirrored and used, but G&B leads.

The disposition rule (mirrored or documented-unavailable with evidence) governs
what "unblocked" means: if the G&B disposition comes back documented-unavailable,
this spec's tier-1 lead re-scopes to Eliot 1666 (or the next available attestation
stream) and the change is recorded here.

### 2.2 The inflectional domains

Paradigm records (`kind: paradigm`) for:

- **Person/number/obviation** on nominals and verbs — the architecture is attested
  (PSN-STR-001: Eliot's Massachusett obviative forms) and reconstructed at the
  family level (PSN-STR-004: Bloomfield 1946 §117).
- **The four verb subtypes** — animate intransitive, inanimate intransitive,
  transitive animate, transitive inanimate.
- **The two orders** — independent and conjunct; both attested in the tracked
  material (conjunct: Eliot 1663 Psalms 68:13 ‹wesôag› via Costa 2007).
- **Possessed-noun inflection** — possessor person/number marking, the obviative
  possessor rule.

### 2.3 Evidence discipline

- **Tier 1 leads**: exponents drawn from attested SNEA material — **Goddard &
  Bragdon 1988 primary** (per Dr. Cunningham's guidance), Eliot 1666 secondary —
  each form carrying its citation.
- **Tier 5 anchors the skeleton**: Bloomfield 1946 §117 (mirrored) — the PA
  architecture the paradigm tables are built against.
- **Tier 4 corroborates and fills**: the Ojibwe component datasets (mirrored), and
  — per Dr. Cunningham's guidance — the named Central reference grammars:
  **Valentine 2001, *Nishnaabemwin Reference Grammar*** (U Toronto Press; Odawa and
  Eastern Ojibwe; verified live 2026-10-12) and **Wolfart 1973, *Plains Cree: A
  Grammatical Study*** (APS Trans 63.5; identified as the standard Cree reference
  grammar, verified live). Where SNEA attestation is silent, missing pieces of
  architecture and usage may be filled from these reference grammars and their
  usage patterns — always tier-4-marked, Central-origin labeled, and never blended
  into PSNEA surface claims (Central corroborates architecture, never supplies
  surface forms).
- **Tier 2 fills from SNEA-internal comparison** where single-source attestation is
  silent, constrained by Costa 2007's dialectology.
- Where attestation is silent everywhere, the paradigm row is left **visibly
  incomplete** (pending marking) — the renderers' incompleteness machinery governs.
- **Evidence traces render everywhere**: attested-form citations appear in every
  rendered view (descriptive, teaching, prescriptive) — the same binding rule that
  carries tier and norm-status markings into all three outputs (snea-phonetics#118
  §2.2 rule 1).

## 3. Success criteria

| ID | Criterion | Class | Verification method |
|----|-----------|-------|---------------------|
| SC-1 | Paradigm records exist for the four inflectional domains of §2.2, passing the schema validator | structural | `uv run pytest test/` — validator passes; a coverage test maps ≥1 paradigm record to each domain |
| SC-2 | Every tier-1 paradigm record's anchors include the Goddard & Bragdon mirror path (or, for secondary-stream records, the Eliot 1666 mirror path) and resolve to existing files under the corpus submodule | structural | The anchor-resolution test, extended to the new records, passes |
| SC-3 | Central corroboration stays architecture-only: tier-4 records carry no `surface_form` fields | structural | A test asserting every tier-4 record in the paradigm set has no surface-form field |
| SC-4 | The paradigms render in all three views, with attested-row citations present in each view | behavioral | Run the three renderers; each of the three outputs contains the paradigm record ids AND the citation strings for attested rows |
| SC-5 | Incomplete paradigm rows render with visible incompleteness (pending marking), per the establishment machinery | behavioral | A paradigm record with a pending PSNEA row renders with the pending marking in all three views |
| SC-6 | The source registry carries the Central reference grammars named by the guidance — `valentine-2001` (Nishnaabemwin Reference Grammar) and `wolfart-1973` (Plains Cree: A Grammatical Study) — as `scholarly_edition` entries with tier-4 roles; the Goddard & Bragdon entry stands as the primary tier-1 attestation source | structural | Registry checks: both new entries present with class and tier role; the G&B entry carries the primary-attestation role |

## 4. Non-goals

- Alternation rules (item W1, snea-grammar#3).
- The realization profile (item W3, snea-grammar#5) — per-language exponent choices
  over this core.
- Phonetic realization (snea-phonetics).
- Vocabulary/lexicon content.
- Mirroring itself (corpus#34's deliverable).

## 5. Change control

| Date | Change | Author |
|------|--------|--------|
| 2026-10-12 | Initial spec from the design sessions and ROADMAP W2 | AI agent |
| 2026-10-12 | Per Dr. Keith Cunningham's guidance: G&B 1988 promoted to primary grammar (gate flips to its mirror); Eliot 1666 demoted to secondary; Valentine 2001 + Wolfart 1973 named as tier-4 fill references (architecture and usage); registry SC-6 added | AI agent |

---

🤖 Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)
