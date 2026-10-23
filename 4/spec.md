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
**Revised again 2026-10-23** per the developer's direction to make the Central fill
library concrete (valentine-2001 / wolfart-1973 / online grammars) and to fix the
library boundaries: grammar sources are held by algonquian-library; the knowledge
extracted from them is held here.

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
analysis of that corpus. **Implementation is blocked on the G&B copy disposition
corpus-side** (algonquian-library#34, MANIFEST discipline; the work is also staged in
the algonquian-library#44 private/ reference copy set as
`private/Wampanoak/Goddard-Bragdon-NativeWritings-II-ocr.pdf`). Either landing path
counts: the disposition is `mirrored` (public mirror under
`docs/research/sources/`) or the `private/` reference copy — recorded corpus-side
before this spec's tier-1 anchors are added. Eliot 1666 (*The Indian Grammar
Begun*, dense paradigm sets) is demoted to the secondary attestation stream — still
mirrored (algonquian-library#34's pass) and used, but G&B leads.

The disposition rule (mirrored, private-dispositioned, or documented-unavailable with
evidence) governs what "unblocked" means: if the G&B disposition comes back
documented-unavailable, this spec's tier-1 lead re-scopes to Eliot 1666 (or the next
available attestation stream) and the change is recorded here.

The tier-4 fill machinery (§2.3) gates separately: Valentine 2001 and Wolfart 1973
anchors land only when the corpus-side private/ disposition (algonquian-library#44
copy set; #66 promotion/mirror pass) materializes the copies in the corpus checkout.

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

### 2.3 The fill machinery (revised 2026-10-23)

#### 2.3.1 Gap types — what may be filled, by whom

"Missing pieces and usage" (the guidance) are two different gap classes with
different rules, plus a third the guidance does *not* authorize:

| Gap type | Question | Fill source | Rule |
|----------|----------|-------------|------|
| architecture | does the PSNEA category exist? | PA skeleton (tier 5, Bloomfield §117) + Central corroboration (tier 4) | freely fillable, Central-marked |
| usage | how does the category behave — person/number co-occurrence, possession, obviative possessor mechanics, order distribution? | Valentine 2001, Wolfart 1973, the open-access Cree/Ojibwe grammars | fillable as *statements* — never as forms (SC-3) |
| exponent | what does the PSNEA marker look like? | **nothing Central** | SNEA-internal comparison (tier 2) or visibly pending |

#### 2.3.2 The fill ladder

Ordered, and required to be *recorded* rather than applied silently — each pending
row carries its `fill_plan` (SC-7):

1. **tier 1** — attested SNEA material: G&B primary, Eliot secondary, the tracked
   colonial-primary streams.
2. **tier 2** — SNEA-internal comparison, constrained by Costa 2007's dialectology.
3. **tier 3** — Munsee Delaware outgroup; the `corpus/data/csv/Delaware_Munsee/`
   component dataset is already mirrored.
4. **tier 4** — Central corroboration: the fill library of §2.3.3.
5. **incomplete-pending** — no eligible source; the row renders visibly pending
   (the renderers' incompleteness machinery governs).

#### 2.3.3 The fill precedence order (familial + evidential distance; added 2026-10-23)

**Status: provisional working order**, adopted 2026-10-23, assumed approved
pending linguist review; review outcomes flow through change control here and
in algonquian-library#66. **Scope: all related-language grammars, not only the
Cree/Ojibwean line** (widened 2026-10-23) — tier-3 Eastern prose sources, the
full Central set, and related languages beyond the current tier vocabulary
(table B below), each ranked by the same axes. The order ranks fill-in sources
*within* the ladder's rungs (it never re-ranks the rungs): **familial
distance** — genealogical closeness to PSNEA — and **evidential distance** —
temporal drift from the PSNEA construction window plus fullness/analytic
standard of the source. Ranking input is the two axes only; the guidance's
source-naming order identifies sources, not their precedence.

Familial axis: Munsee Delaware (tier 3) precedes every Central source by
shared Eastern descent — and the whole Eastern side shares the PEA defining
changes (vowel-length loss, \*e → \*ə, final-vowel loss) documented in the
mirrored Goddard 1980, *Eastern Algonquian as a genetic subgroup*
(`corpus/docs/research/sources/goddard1980.*`), the textual warrant for
ranking the Eastern non-SNEA comparanda (table B) above every Central source.
Within tier 4 all Central languages are *equidistant
familially* — Central subgrouping is contested and no Central subgroup shares
known innovations with SNEA — so the familial axis resolves to the
**retention profile**: proximity of the documented inflectional system to the
PA skeleton (Bloomfield §117, the tier-5 anchor). Evidential axis: temporal
closeness of the documentation to the PSNEA window, then fullness and
analytic standard. Every rationale is a working claim, subject to linguist
review.

| Rank | Source | Familial note | Evidential note |
|------|--------|---------------|-----------------|
| T3 | `omeara-1992` — Munsee prose: O'Meara, *Delaware Reference Grammar* (UTP; JWM1992 in the component bibliography — verified live 2026-10-23); Goddard's Munsee/Unami analysis stream; `Delaware_Munsee`/`Delaware_Unami` datasets already mirrored | nearest relative — outranks all tier-4 by the ladder itself | full modern scholarly reference grammar |
| 1 | `costa-2003` — Miami-Illinois | most PA-conservative documented Central inflection (notably uncontracted PA independent-order material) | historical grammar of a language documented across the same colonial window as SNEA; full modern scholarly treatment |
| 2 | `valentine-2001` — Nishnaabemwin (Odawa/Eastern Ojibwe) | conservative verb architecture; Ojibwean-level sound innovations as caveat | exhaustive modern reference grammar, fullest usage coverage in the set |
| 3 | `wolfart-1973` — Plains Cree | fullest PA-style person/obviation/possession retention; documented independent-order contraction as caveat | standard scholarly Cree reference (APS Trans 63.5); more compact than rank 2 |
| 4 | `hockett-1939` — Potawatomi | Ojibwean sibling of rank 2; radical phonological divergence makes it a cautionary comparator | full 1939 dissertation (staged in algonquian-library#44 copy set) |
| 5 | component substrate — `corpus/data/csv/` Central datasets + O'Brien charts | all Central families, citation-keyed | machine-readable cross-check **beneath every rank above**, not a prose-usage source |
| 6 | Menominee (Bloomfield 1975), Meskwaki, Kickapoo (Voorhis stream), Shawnee (Voegelin stream) — future adoption | conservative Central comparators; each carries a cited scholarly stream in the component bibliography (LB1975; AD1986–2017 + Goddard & Dahlstrom 2022; PV1967–1988; CV1935–1959) | none has an adopted full-grammar monograph — dataset-backed pending the algonquian-library#66 candidate inventory |
| 7 | `baraga-1850` — Otchipwe (Ojibwe) grammar | substantively Ojibwean | missionary-era, pre-linguistic analysis — corroboration-only weight |
| 8 | `okimasis` — Cree: Language of the Plains | substantively Cree | pedagogical register — lowest scholarly weight; corroboration-only |

**Table B — related languages beyond the current tier vocabulary** (ranked by
the same axes; **adoption pending the tier ruling** — the evidence ladder
(snea-phonetics#118 §2.3) carries no rung for non-Central/non-SNEA comparanda,
and the registry stays closed to them until the design record is extended
(SC-6); they scope in the algonquian-library#66 candidate inventory and
corpus-side dispositions only):

| Rank | Language — prose source | Familial note | Evidential note |
|------|-------------------------|---------------|-----------------|
| B1 | Mi'kmaq — Pacifique's grammar (Hewson & Francis, 1990, Algonquian & Iroquoian Linguistics — verified live 2026-10-23); Hewson stream in the bibliography; `Mikmaq` datasets mirrored | Eastern, shares the PEA defining changes (mirrored Goddard 1980) | scholarly re-edition of a Jesuit-era treatment; divergent Eastern inflection as caveat |
| B2 | Passamaquoddy-Maliseet — Francis & Leavitt stream (DAF_RL1994, RL1985/1992) + LeSourd's Passamaquoddy work (PL1995/2004/2009); `Passamaquoddy_Maliseet` datasets mirrored | Eastern, same warrant | dictionary-plus-analysis stream rather than one monolithic grammar; online portals are community-gated (governance gate applies) |
| B3 | Western Abenaki — Day 1995 (GMD1995 in the bibliography); Edwards 1787 already mirrored | Eastern **neighbor** (not a PSNEA member per Costa 2007's membership ruling) — comparative role only | dictionary-plus-grammar tradition |
| B4 | Arapaho — Cowell & Moss, *The Arapaho Language* (U Press Colorado, 2008; AC_AM2008 in the bibliography — verified live 2026-10-23) | Plains branch — deepest familial distance in this table | exemplary modern full reference grammar (544 pp) |
| B5 | Blackfoot — Frantz stream (DF1966–2017 in the bibliography) | Plains branch | monograph scoping pending |
| B6 | Cheyenne — Leman stream (WL1979/1985) | Plains branch | monograph scoping pending |
| — | Powhatan | Eastern; SNEA-adjacency unresolved | component-data-only (`corpus/data/csv/Powhatan/`) |

Tier-2 (SNEA-internal) precedence follows Costa 2007's dialect grouping:
the Massachusett–Coweset–Narragansett block, then Mohegan-Pequot-Montauk and
the Niantics, then Quiripi/Unquachog, then Loup, per Costa 2007's grouping.

#### 2.3.4 The tier-4 fill library and its dispositions

- **The named reference grammars (in-copyright):** Valentine 2001
  (*Nishnaabemwin Reference Grammar*, U Toronto Press — already staged in
  algonquian-library#44's private/ copy set as `nishnaabemwin-hq-ocr.pdf`, with 25
  page-numbered citations already carried in `Ojibwe_Common.ndjson`) and Wolfart
  1973 (*Plains Cree: A Grammatical Study*, APS Trans 63.5 — excluded from the #44
  copy set as uncited; the promotion pass is algonquian-library#66, with this spec's
  §2.3 as the recorded need evidence). Anchored via the corpus `private/`
  reference-library mechanism (the PSN-RUL-011/013/014/015 precedent —
  `test/test_corpus_anchor.py` accepts `private/` anchors as a gitignored,
  session-local authority surface); such records land only when the copy exists
  in the corpus checkout (no dangling anchors).
- **Mirrorable online grammars (open access, verified live 2026-10-23):** Baraga,
  *A Theoretical and Practical Grammar of the Otchipwe Language* (1850; 1879 ed. —
  public-domain era, archive.org CIHM copies) and Okimāsis, *Cree: Language of the
  Plains* (U Regina Press open textbook). Mirror requests ride algonquian-library#66;
  registry entries follow the MANIFEST landing (SC-6).
- **Already-mirrored Central material (already mirrored):** the Central
  component datasets — `corpus/data/csv/Cree_Plains/`, `Cree_Swampy/`,
  `Cree_Moose_Swampy/`, `Ojibwe_Odawa/`, `Ojibwe_Eastern/`, `Potawatomi/`,
  `Menominee/`, `Meskwaki/`, `Miami_Illinois/` (row-citation-keyed, incl.
  Ahenakew & Wolfart 1983/1991 in `corpus/data/json/citationKeys.json`) — and the
  O'Brien Ojibwe paradigm-chart mirror
  (`corpus/docs/research/sources/bigorrin-waabu11-obrien-charts-abc.html`). Eastern-
  group Cree sets (`Cree_East`, `Cree_Innu`, `Cree_Naskapi_*`) are not tier-4.
- **Tier 2 still fills where single-source attestation is silent** — costed into the
  ladder above the Central rung, constrained by Costa 2007's dialectology.
- **Governance gate for online candidates:** university-press/lab and scholarly
  open-access works classify `scholarly_edition`; community-authored teaching
  materials classify `community_dictionary` (excluded by default) unless authorized
  — the modern-Mohegan-dictionary ruling pattern.
- Where attestation is silent everywhere, the paradigm row stays **visibly
  incomplete** (pending marking) — never silently absorbed.

#### 2.3.5 Rendering and provenance

- **Evidence traces render everywhere**: attested-form citations appear in every
  rendered view (descriptive, teaching, prescriptive) — the same binding rule that
  carries tier and norm-status markings into all three outputs (snea-phonetics#118
  §2.2 rule 1). Central-corroboration fills render **prefixed explicitly**
  ("Central corroboration — *source*, *locator*") in every view, so no reader can
  mistake a usage-fill for attestation (SC-8).
- **Tier 4 carries no surface forms** (SC-3) — usage fill lands as architecture
  statements with pinpoint locators; Central-derived exponent shapes never enter
  PSNEA claims.
- **Every pending row records a fill_plan** — `gap_type` (§2.3.1's classes),
  `candidates` (source-registry ids, **listed in the §2.3.3 precedence
  order** — highest-precedence eligible source first), `disposition` (one of
  `central-arch`/`central-usage`/`internal-comparison`/`outgroup`/
  `incomplete-pending`) — the ladder is auditable, not silent (SC-7).

### 2.4 Library boundaries (added 2026-10-23)

The division of labor between this repository and the corpus library — no
grammar-source folder set exists here beyond the existing `private/` precedent,
and none is created:

| Thing | Lives in |
|-------|----------|
| Mirrorable source documents (colonial primaries, public-domain-era Central grammars, open-access textbooks, component datasets, paradigm-chart mirrors) | algonquian-library — `docs/research/sources/` mirrors + `data/csv` component database; tracked via #34/#66 |
| In-copyright reference works (Valentine 2001, Wolfart 1973, G&B 1988) | algonquian-library `private/` reference library (#44 machinery; need-filtered; promotion is a deliberate recorded step — #66) |
| Classification of every source, mirrored or not | this repo — `data/sources.yaml` |
| Locator pins / fill provenance for un-landed sources | this repo — `fill_plan` candidates + registry notes, resolving to corpus paths only once the copy lands |
| Grammar knowledge extracted from any source | this repo — `data/grammar/` records; the corpus is the source surface, the knowledge base is ours |
| Working extract notes, if ever needed | this repo — `data/notes/` (contingency row; no such folder planned) |

## 3. Success criteria

| ID | Criterion | Class | Verification method |
|----|-----------|-------|---------------------|
| SC-1 | Paradigm records exist for the four inflectional domains of §2.2, passing the schema validator | structural | `uv run pytest test/` — validator passes; a coverage test maps ≥1 paradigm record to each domain |
| SC-2 | Every tier-1 paradigm record's anchors include the G&B disposition path — a corpus mirror path or a corpus `private/` reference path — recorded corpus-side (#34/#44/#66) and resolving under the corpus submodule before the record lands; private/ anchors resolve session-locally per the PSN-RUL precedent (test/test_corpus_anchor.py) | structural | The anchor-resolution test, extended to the new records, passes |
| SC-3 | Central corroboration stays architecture-only: tier-4 records carry no `surface_form` fields | structural | A test asserting every tier-4 record in the paradigm set has no surface-form field |
| SC-4 | The paradigms render in all three views, with attested-row citations present in each view | behavioral | Run the three renderers; each of the three outputs contains the paradigm record ids AND the citation strings for attested rows |
| SC-5 | Incomplete paradigm rows render with visible incompleteness (pending marking), per the establishment machinery | behavioral | A paradigm record with a pending PSNEA row renders with the pending marking in all three views |
| SC-6 | The source registry classifies the fill library: `valentine-2001` and `wolfart-1973` as `scholarly_edition` tier-4 entries with their corpus landing paths/locators (#44/#66); registry entries for every Central component dataset and mirrored online grammar (baraga, okimāsis) that a tier-4 record actually cites, each carrying its `corpus/` path; the G&B entry stands as the primary tier-1 attestation source; **no registry entry exists for the §2.3.3 table B comparanda pending the tier ruling** | structural | Registry checks: entries present with class, tier role, and resolvable locator; the G&B entry carries the primary-attestation role; every registry tier role ∈ 1–5 vocabulary |
| SC-7 | Every paradigm record with a pending PSNEA row carries a `fill_plan` (gap_type ∈ §2.3.1 classes, candidates = registry ids listed in the §2.3.3 precedence order, disposition ∈ §2.3.5's enum); no pending row is silently empty; `incomplete-pending` rows carry the reason no source is eligible | structural | Coverage test: every pending row inspected; invalid dispositions and out-of-order candidate lists fail the suite |
| SC-8 | Central-derived fill renders distinctly: any fill content sourced from a tier-4 registry entry is prefixed "Central corroboration — <source>, <locator>" in all three views, styled separately from attestation citations | behavioral | Run the three renderers over a paradigm record containing a tier-4-sourced fill; the prefix appears in each view |

## 4. Non-goals

- Alternation rules (item W1, snea-grammar#3).
- The realization profile (item W3, snea-grammar#5) — per-language exponent choices
  over this core.
- Phonetic realization (snea-phonetics).
- Vocabulary/lexicon content.
- Mirroring and private-library execution itself — algonquian-library#34, #44, #66
  own the copy set; only the anchor paths, registry rows, and `fill_plan` fields
  land here.

## 5. Change control

| Date | Change | Author |
|------|--------|--------|
| 2026-10-12 | Initial spec from the design sessions and ROADMAP W2 | AI agent |
| 2026-10-12 | Per Dr. Keith Cunningham's guidance: G&B 1988 promoted to primary grammar (gate flips to its mirror); Eliot 1666 demoted to secondary; Valentine 2001 + Wolfart 1973 named as tier-4 fill references (architecture and usage); registry SC-6 added | AI agent |
| 2026-10-23 | Fill machinery made concrete per developer direction: §2.3 split into gap types / ladder / tier-4 library dispositions (private/ anchoring per #44, promotion pass algonquian-library#66, component datasets as first-class tier-4, governance gate for online candidates); §2.4 library boundaries added; SC-2 extended to the disposition paths, SC-6 extended to the full library, SC-7 (fill_plan coverage) and SC-8 (Central rendering prefix) added | AI agent |
| 2026-10-23 | §2.3.3 fill precedence order added: tier-4 sources ranked by familial + evidential distance only (guidance's source-naming order dropped from the ranking rationale; Miami-Illinois leads, component substrate noted as a beneath-the-ranks layer; tier-2 precedence per Costa 2007's grouping); marked provisional, assumed approved, submitted for linguist review; SC-7 extended to enforce candidate order | AI agent |
| 2026-10-23 | §2.3.3 widened beyond the Cree/Ojibwean line per developer direction: tier-3 prose sources added (O'Meara 1992 per the component bibliography); rank 6 extended to the full Central future-adoption stream (Menominee/Meskwaki/Kickapoo/Shawnee — LB1975, AD stream, PV stream, CV stream); table B added for related languages beyond the tier vocabulary (Eastern non-SNEA: Mi'kmaq / Passamaquoddy-Maliseet / Abenaki; Plains: Arapaho / Blackfoot / Cheyenne; Powhatan note), warranted by the mirrored Goddard 1980 EA-subgrouping; the tier gap is flagged as a design-record question for the developer ruling, registry stays closed to table B (SC-6 extended); corpus-side inventory (algonquian-library#66 SC-4) carries the matching scoping | AI agent |

---

🤖 Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)