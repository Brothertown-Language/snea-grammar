---
issue_number: 4
title: "[SPEC] PSNEA paradigm architecture — tier-1 attestation leading (blocked on Eliot 1666 mirror)"
state: open
created_at: "2026-10-12T04:50:00Z"
synced_from: "https://github.com/Brothertown-Language/snea-grammar/issues/4"
---

# PSNEA paradigm architecture — tier-1 attestation leading

**Author:** AI agent
**Design source:** the 2026-10-11/12 design sessions (developer rulings, recorded in the
snea-phonetics#118 design record and the developer-approved `ROADMAP.md`, item W2)

## 1. Goal

Assemble the PSNEA paradigm architecture — the inflectional system itself — as
grammar records, with tier-1 attestation leading: the design session's directive is
that PSNEA forms lead the rendered output once available, per-language realization
layers carry the differences, and dataless ancestors are covered by projection.

## 2. Design record

### 2.1 Dependency (hard gate)

**Implementation is blocked on the Eliot 1666 mirror** (algonquian-library#34): the
tier-1 lead for paradigms is Eliot 1666, *The Indian Grammar Begun* — ~65 pages of
dense mood/tense/person-number-object paradigm sets — and it is not yet mirrored in
the corpus. The parallel attestation stream, Goddard & Bragdon 1988 (*Native
Writings in Massachusett*, native-written documents), is likewise not yet mirrored
(scope of the same corpus issue). This spec records the requirement; record-writing
starts when the mirror lands. The corpus's disposition rule (mirrored or
documented-unavailable with evidence) governs what "unblocked" means: if the
disposition comes back documented-unavailable, this spec's tier-1 lead re-scopes to
the next available attestation stream and the change is recorded here.

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

- **Tier 1 leads**: exponents drawn from attested SNEA material (Eliot 1666;
  Goddard & Bragdon 1988), each form carrying its citation.
- **Tier 5 anchors the skeleton**: Bloomfield 1946 §117 (mirrored) — the PA
  architecture the paradigm tables are built against.
- **Tier 4 corroborates**: the Ojibwe component datasets (mirrored) — architecture
  only; Central supplies no surface forms.
- **Tier 2 fills from SNEA-internal comparison** where single-source attestation is
  silent, constrained by Costa 2007's dialectology.
- Where attestation is silent everywhere, the paradigm row is left **visibly
  incomplete** (pending marking) — the renderers' incompleteness machinery governs.

## 3. Success criteria

| ID | Criterion | Class | Verification method |
|----|-----------|-------|---------------------|
| SC-1 | Paradigm records exist for the four inflectional domains of §2.2, passing the schema validator | structural | `uv run pytest test/` — validator passes; a coverage test maps ≥1 paradigm record to each domain |
| SC-2 | Every tier-1 paradigm record's anchors include the Eliot 1666 mirror path (or the Goddard & Bragdon mirror path) and resolve to existing files under the corpus submodule | structural | The anchor-resolution test, extended to the new records, passes |
| SC-3 | Central corroboration stays architecture-only: tier-4 records carry no `surface_form` fields | structural | A test asserting every tier-4 record in the paradigm set has no surface-form field |
| SC-4 | The paradigms render in all three views; attested rows carry their citations | behavioral | Run the three renderers; each output contains the paradigm record ids; the descriptive output carries the citation strings |
| SC-5 | Incomplete paradigm rows render with visible incompleteness (pending marking), per the establishment machinery | behavioral | A paradigm record with a pending PSNEA row renders with the pending marking in all three views |

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

---

🤖 Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)
