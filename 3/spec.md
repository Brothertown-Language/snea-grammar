---
issue_number: 3
title: "[SPEC] PSNEA alternation rules — morphophonology as grammar records"
state: open
created_at: "2026-10-12T04:50:00Z"
synced_from: "https://github.com/Brothertown-Language/snea-grammar/issues/3"
---

# PSNEA alternation rules — morphophonology as grammar records

**Author:** AI agent
**Design source:** the 2026-10-11/12 design sessions (developer rulings, recorded in the
snea-phonetics#118 design record and the developer-approved `ROADMAP.md`, item W1)

## 1. Goal

Assemble the PSNEA alternation rules — the morphophonological layer of the grammar —
as validated grammar records in this repository's knowledge base. The design session
ruled **alternation is grammar, keep it**: this repository emits Costa-alphabet forms
plus the alternation rules that derive them; orthographic/phonetic realization stays
with snea-phonetics. This is the one Phase-1 content stream unblocked today: every
needed anchor is already mirrored in the corpus submodule at v0.1.2.

## 2. Design record

### 2.1 The rule set (from the tracked mirrors)

Each rule is a `kind: rule` grammar record. The domains, with their tracked anchors
(all under the corpus submodule, verified at v0.1.2):

| Rule domain | Tracked anchor basis |
|---|---|
| Final PEA *r → š/s (the correspondence that also carries the paradigm-ending reconstruction: inanimate plural PA *-ari → SNEA -(a)š, 2sg AI imperative *-ro, theme-4 sign *-eTe) | `corpus/docs/research/sources/costa2007.txt` ll. 297–299 (law c), ll. 333–338 |
| k-palatalization — a PSNEA feature: → ty in Massachusett-Coweset, palatal stop in other SNEA, before PEA *m and some instances of PA *i; conditioning details "notoriously difficult to define" (Costa's own caveat, carried) | `corpus/docs/research/sources/costa2007.txt` ll. 109–120 |
| hš cluster — PEA *hr and *hx merge as hš (a PSNEA feature), with a documented reduction gradient: hs with gradient consistency in Unquachog (always), Loup (almost always), Quiripi and Montauk (occasionally) | `corpus/docs/research/sources/costa2007.txt` ll. 201–212, ll. 325–330 |
| Preaspiration hC retention — retained in Massachusett but routinely lost/simplified in colonial transcriptions (the recorder-failure caveat; Edwards 1787 and Prince & Speck 1904 are the recorders who write it) | tracked mirrors that attest it: `corpus/docs/research/sources/edwards-1787-observations-fulltext.txt`, `corpus/docs/research/sources/prince-speck-1904.txt`; caveat provenance: the snea-phonetics research cards |
| Vowel correspondences — the PSNEA-state vowel rows | the bottom-up PSNEA reconstruction record (`snea-phonetics` feasibility branch, `docs/research/psnea-stage-reconstruction.md` §4.2) reconciled against `costa2007.txt` |

Implementation verifies every anchor path and line range live before writing the
record; no rule is written from memory.

### 2.2 Contested rows — the tracked discipline

Rows the tracked sources disagree on, or that no tracked source licenses, are carried
**marked**, never silently adjudicated. For this item that means at minimum:

- **š/s merger** — the Trumbull-card table gives *š → /ʃ/ (sh) phonemically distinct
  from s in Massachusett, while Costa (citing Goddard 1978:75) states older PA *š had
  already merged with *s in all EA north of Delaware-Mahican before the new
  word-final *š was created. Both positions are card-attested; both are recorded;
  no adjudication without new tracked evidence.
- **š's distribution** — attested only word-finally (the new phoneme created by law
  c); elsewhere unattested in PSNEA.
- Vowel rows marked contested/unattested per the reconstruction record (the *e·
  discrepancy, schwa phonemicity, nasal-vowel status).

## 3. Success criteria

| ID | Criterion | Class | Verification method |
|----|-----------|-------|---------------------|
| SC-1 | Alternation rules exist as `kind: rule` records under `data/grammar/`, passing the schema validator, covering the five domains of §2.1 | structural | `uv run pytest test/` — validator passes over `data/grammar/`; a coverage test maps ≥1 record to each of the five domains |
| SC-2 | Every new rule record's source anchors resolve to existing files under the corpus submodule | structural | The existing anchor-resolution test pattern, extended to the new records, passes |
| SC-3 | Contested/unattested rows carry explicit status marking; the š/s merger record states both tracked positions; no record adjudicates a contested row without new tracked evidence | structural | Tests assert the marking on the named records and assert both š/s positions appear in the š/s record's statement |
| SC-4 | The new rules render in all three views with their evidence standing | behavioral | Run the three renderers; each output contains the new record ids and their evidence-standing lines |
| SC-5 | The hš reduction gradient renders per language — Unquachog, Loup, Quiripi, Montauk as distinct realization entries | behavioral | The descriptive rendering of the hš record lists the four languages with their gradient values |

## 4. Non-goals

- Phonetic realization or orthography conversion (snea-phonetics' domain; no regex
  anywhere).
- Paradigm exponents and architecture (item W2, snea-grammar#4).
- Adjudicating contested rows — that requires new tracked evidence, a separate
  decision.
- Any surface form not traceable to a tracked anchor.

## 5. Change control

| Date | Change | Author |
|------|--------|--------|
| 2026-10-12 | Initial spec from the design sessions and ROADMAP W1 | AI agent |

---

🤖 Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)
