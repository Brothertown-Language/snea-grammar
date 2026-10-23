<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->
<!-- SPDX-License-Identifier: MIT -->

# Evergreen grammar-reconstruction methodology PDF — the sourcing tiers, the pull rules, and the proofing state

## 1. Goal

Build a top-level, evergreen document — a PDF compiled from tracked LaTeX —
that states how the Southern New England Algonquian grammar is reconstructed
from its sources: which grammar-sourcing documents exist, what evidence tier
each one serves, and the rule for when to pull from which tier. The document
carries the ladder and flow-chart figures that make those rules legible, and
it carries the proofing state of the passages it relies on.

The document is built to stay current. When the source corpus materials
change — a mirror lands, a proofed OCR'd segment lands, a disposition changes
— the research behind the document and the document itself are refreshed, and
the refresh is a recorded duty in this repository's agent instructions, not a
matter of memory.

**Design source.** The developer's statement of 2026-10-23: a top-level
evergreen PDF built from TeX, detailing the grammar sourcing documents and
their tiering and the rules for determining when to pull from which tier,
with ladder diagrams and flow charts as figures; the research behind the
document and the document itself kept current on changes to the source corpus
materials, including when proofed OCR'd segments land; unproofed OCR'd
segments treated as legitimate material with a checklist of what has been
proofed and what needs proofing; and the proofed extracts tracked as
supporting materials. The developer's direction of the same day to split the
work between the grammar repository and the corpus repository along
separation-of-concern lines, and to place submodule-registration adjustments
in scope. `ROADMAP.md` gains the work item this issue introduces.

## 2. Design record

### 2.1 What the document states, and what it does not

The document states four things, each of which a reader of the grammar
program needs:

1. **The evidence ladder** — the five tiers (SNEA-attested; SNEA-internal
   comparison; Munsee Delaware outgroup; Central Algonquian corroboration;
   Proto-Algonquian reconstruction), what each rung may supply, and the
   direction of the pull.
2. **The sourcing documents** — every source the grammar program may anchor
   to, its class, its tier role, where it is held, and its proofing state.
3. **The pull rules** — the gap classes (architecture, usage, exponent), which
   rung may fill which class, the fill precedence order within a rung, and the
   rule that a row with no eligible source stays visibly pending.
4. **The proofing gate** — what counts as OCR-derived, that unproofed OCR is
   working-copy material, that the proofing pass covers the used portions at
   locator level, and what is currently proofed and what is not.

No tracked non-spec document states the pull rules in full. The root
`AGENTS.md` summarizes the ladder and two of the rules — that incompleteness
stays visible and that Central material corroborates without supplying
surface forms — and `data/sources.yaml` carries the per-source classifications
in prose comments rather than as a machine-readable vocabulary. The pull
rules, the precedence order, the proofing gate, and the join between a rule
and the source that supplies it exist only in the spec at snea-grammar#4
§2.3, and nothing in this repository states the proofing state of the
passages the program sources.

The document does not restate the grammar itself, the lexicon, or the
phonetic realization — those are the other renderings and the other
repositories' surfaces. It is the method document.

### 2.2 Where the document lives, and the cut line with the corpus repository

The document lives in this repository. The evidence it presents about the
corpus's holdings is consumed through the `corpus/` submodule, which this
repository already holds; the corpus repository consumes nothing from this
repository.

The alternative placements were considered and rejected:

- **In the corpus repository** — the holdings and their proofing state would
  be at hand, but the tier assignment and the pull rules are this
  repository's authority, and a corpus-side document would restate them
  without being able to read them, creating a second, unauthoritative
  statement of the rules. It would also need a `grammar/` submodule
  registration, closing the graph corpus → grammar → corpus; mutually
  recursive submodule registration is not a shape the recursive initialization
  path supports, and the project topology places the corpus repository at the
  base of the family.
- **In the phonetics repository** — that repository holds the evergreen
  LaTeX corpus and its build machinery, but its subject is the
  orthography-to-phoneme conversion, and the grammar program's method is not
  its document.

The cut line is fact ownership. snea-grammar#4 §2.4 draws the boundary
between what lives in each repository for the materials; the table below
extends it with the proofing state, following algonquian-library#68 §2.1.

| Fact | Owner |
|------|-------|
| The evidence tier of a source; the fill rules; the precedence order | this repository (`data/sources.yaml`; snea-grammar#4 §2.3) |
| Which documents exist, where each is held, its disposition, its proofing state, the proofed readings | algonquian-library — the grammar-source store, proofing checklist, and tracked proofed extracts (algonquian-library#68) |
| The grammar records and the anchors that consume both | this repository (`data/grammar/`) |

The document therefore joins a local authority with a corpus-side dataset. The
join is generated, not typed: the sourcing table, the proofing checklist
table, the bibliography, and the as-of anchors are all produced by a
generator from the tracked inputs, and the tracked LaTeX sources carry no
hand-written table rows (the generated-source rule the corpus repository
already applies to its rendered volume).

The corpus side produces the store's coverage: algonquian-library#68 requires
a dossier row for every source id in this repository's `data/sources.yaml` and
for every corpus work this repository's grammar records anchor, and its seed
row set names both. This repository's join gate checks that coverage against
the live records.

### 2.3 The machine-readable rule set

The document's rules are stated in prose, and prose that a document and a
registry must agree about drifts. The rules therefore also live in a
machine-readable file, `data/grammar-rules.yaml`: a file-level `revision`
date, and one entry per rule, each carrying an id, the canonical statement
the document renders, the scope it binds, and the authority it derives from.
The document renders each canonical statement verbatim inside the environment
`\grammarrule{<id>}`, and the build gate asserts the two-way correspondence
between the file's statements and the document's rendered statements — sentence
for sentence, not id for id, so that a reworded rule in the document fails the
gate.

The rule set carries these rules:

| Id | Subject |
|----|---------|
| `GRM-01` | The evidence ladder and the direction of the pull: tier 1 leads, and a lower rung is reached only where the rung above is silent |
| `GRM-02` | Central corroboration supplies no surface forms |
| `GRM-03` | The three gap classes — architecture, usage, exponent — and what may fill each |
| `GRM-04` | The fill precedence order and its two ranking axes, familial distance and evidential distance |
| `GRM-05` | Tier 2 fills where single-source attestation is silent |
| `GRM-06` | Incompleteness stays visible: a row with no eligible source renders as pending |
| `GRM-07` | Community dictionaries are excluded by default; use requires explicit authorization from the owning community |
| `GRM-08` | The OCR sourcing rule, cited to the corpus runbook's rules `OCR-1`…`OCR-8` |
| `GRM-09` | Every pending row records a fill plan; the ladder is auditable, not silent |
| `GRM-10` | Tier-2 precedence follows Costa 2007's dialect grouping |

### 2.4 The figures

Five figures carry the rules. They are TikZ/forest sources, compiled into the
document, and each is referenced from the section whose rule it shows.

| Figure | What it shows |
|--------|---------------|
| F1 | The evidence ladder — five rungs, tier 1 at the top, the pull direction drawn downward, the callout that tier 4 supplies no surface forms, and the governance gate drawn as a barred side branch |
| F2 | The pull-decision flow chart — attestation first, then the gap class, then the rung, then the ranked source, then the disposition. Its terminal outcomes are the five dispositions the pull rules define (`central-arch`, `central-usage`, `internal-comparison`, `outgroup`, `incomplete-pending`), each labelled with what it yields; a tier-2 or tier-3 fill is labelled as such and never as an attested form |
| F3 | The fill-precedence diagram — the familial and evidential axes with each ranked source placed on them |
| F4 | The proofing pipeline — capture, OCR, human proofing pass, back-apply, tracked extract, citable; and the branch that leaves an unproofed passage as working-copy material |
| F5 | The traceability chain — a grammar record, its anchor, the corpus path, the tracked proofed extract, the page render |

### 2.5 The document's sections

The document's section set is fixed; the sections are wired into `master.tex`
in this order.

| Section | What it carries | Figure |
|---------|-----------------|--------|
| Introduction and scope | the audience, what the document is and is not, the as-of anchors | — |
| The evidence ladder | the five rungs, what each supplies, the pull direction | F1 |
| The sourcing documents | the generated sourcing table: every source, its class, its tier role, where it is held, its proofing state | — |
| The pull rules | the gap classes, the rung each may fill, the precedence order, the pending rule | F2, F3 |
| Governance | the community-dictionary exclusion and the basis for it | — |
| The proofing gate | what counts as OCR-derived, the working-copy rule, the coverage rule | F4 |
| The proofing checklist | the generated checklist table: what is proofed and what still needs proofing | — |
| Supporting materials | the tracked proofed extracts the document's citations resolve against | F5 |
| Maintenance | the currency procedure, the cross-repository responsibilities, the change-control record | — |
| Glossary | the terms the document uses | — |

The generated payload reaches the document: the sourcing table, the
proofing-checklist table, and the bibliography are `\input` from the
`generated/` directory, and the build asserts that their content appears in
the built PDF's extracted text.

### 2.6 The proofing state in the document

The document carries the proofing state of the passages the grammar program
sources, in two places: the sourcing table's proofing column, and the
proofing-checklist section that lists what is proofed and what still needs
proofing. Both are generated from the corpus store. The document states the
rule that unproofed OCR'd segments are legitimate working-copy material —
available for staging, diffing, and availability scoping, never backing a
citation or an anchor until a human proofing pass covers the passage — as its
own rule `GRM-08`, citing the corpus runbook's rules `OCR-1`…`OCR-8` by id
and path. The build gate resolves that citation: the cited path must exist
under the corpus submodule and the cited rule ids must be present in the
runbook.

### 2.7 The currency machinery

The document's volatile inputs are the corpus store and the registry; its
stable inputs are the rule set and the section sources. The drift detectors
are mechanical and fail loud:

- **The generated-source gate.** The four generated files are tracked and
  byte-identical to the generator's output for the tracked inputs, and the
  tracked LaTeX sources contain no table content of their own.
- **The freshness gate.** The document records two things about the corpus:
  the pinned commit it was generated against, and a digest of the corpus
  store's files at that commit. The freshness gate compares the digest of the
  checked-out corpus store against the recorded digest, and fails naming the
  drift when they differ; the pin check compares the recorded commit against
  the checked-out submodule commit.
- **The join gate.** Every source in `data/sources.yaml` resolves to a corpus
  dossier row and the reverse holds; every corpus work this repository's
  grammar records anchor resolves to a dossier row; the document's sourcing
  table row count equals the join size.

The refresh duty is recorded in two places: this repository's root `AGENTS.md`
names the trigger events and the refresh steps, and the document folder's
`AGENTS.md` carries the procedure for the folder. The trigger events are a
corpus material change, a proofed segment landing, a rule change, and a
registry change. The cross-repository half of the duty — the corpus repository
updating its store and naming this repository's corpus-pin advance and the
methodology document's refresh among the surfaces each event fires — is
recorded in the corpus repository's own agent instructions
(algonquian-library#68 SC-9).

### 2.8 The document tree and the toolchain

The document is an evergreen document, and it follows the convention the
phonetics repository established for that class: the document root is
`paper/evergreen/grammar-reconstruction-methodology/`, the per-document scope
registry is `paper/evergreen/EVERGREEN.md`, and the build entry point
`paper/build.sh` discovers document roots generically — the master root plus
every `paper/evergreen/*/` directory — so that adding a document requires no
script change. The registry entry names the document, its path, its entry
file, its review owner, its scope globs, and its tracked binaries directory.

The document root holds `master.tex`, the `sections/` tree, the `figures/`
tree, the `generated/` directory, `references.bib` (generated), the `outputs/`
directory for the tracked PDF, and the `build/` directory for intermediates.
The repository-level assets are `paper/fonts/` (the vendored CharisSIL faces
with their OFL text) and `paper/vendor/` (the vendored linguistic-example
styles).

The preamble loads CharisSIL (for the IPA inventory), `gb4e` (numbered
linguistic examples), `tikz` and `forest` (the figures), `booktabs`,
`biblatex` with `biber`, and `hyperref` with `cleveref` after it. The
typesetting convention follows the phonetics repository's: `\sloppy`,
`\raggedbottom`, and flexible vertical lengths in the preamble, with no layout
enforcement in the build tooling.

The tier labels the document prints come from the package's `TIER_NAMES`
(`src/snea_grammar/render.py`), which is the machine-readable display
vocabulary; the root `AGENTS.md`'s tier paragraph is aligned to it in the same
change, so that the document, the renderers, and the agent instructions name
the five rungs identically.

The generator lives in the package, `src/snea_grammar/docgen.py`, with a
command-line entry point in the style of the existing render CLI, so that the
document's content is produced by the same validated package that produces
the other renderings.

### 2.9 A live registry value outside the tier vocabulary

`data/sources.yaml` gives `masthay-1991` the tier role `neighbor` — a
Delaware-Mahican comparative source that is a neighbor language and not a
PSNEA member. The role sits outside the five-rung vocabulary, and
snea-grammar#4 SC-6 states that every registry tier role is in the 1–5
vocabulary, so the live registry contradicts that criterion today.

This issue resolves the contradiction in the registry rather than blessing
the value: the `masthay-1991` entry moves its neighbor marker out of
`tier_roles` into a `classification` field of its own, so that every
`tier_roles` value in the registry is one of the five tiers, as
snea-grammar#4 SC-6 requires. The document renders the neighbor marker as a
classification outside the five rungs — the sourcing table's neighbour row
sits beside the ladder rather than on a rung — and `GRM-01` states that the
pull runs through the five rungs only. The change is recorded in
snea-grammar#4's change-control table.

## 3. Success criteria

| ID | Criterion | Class | Verification method |
|----|-----------|-------|---------------------|
| SC-1 | The document root `paper/evergreen/grammar-reconstruction-methodology/` holds `master.tex`, the `sections/` tree, the `figures/` tree, the `generated/` directory, `references.bib`, the `outputs/` directory, and the `build/` directory; the repository-level `paper/build.sh`, `paper/fonts/`, and `paper/vendor/` exist at those paths | structural | File-existence checks over the named paths |
| SC-2 | The document is registered in `paper/evergreen/EVERGREEN.md` with its name, path, entry file, review owner, scope globs, and tracked binaries directory, and `paper/build.sh --list` names the document root | behavioral | Read the registry and assert the six registry fields for the document; run the build script's listing mode and assert the document root appears in its output |
| SC-3 | The document root path appears in the root `AGENTS.md` repository-structure table | structural | A text check for the document root path in the root `AGENTS.md` |
| SC-4 | `bash paper/build.sh` produces the PDF from the tracked sources in a checkout with the corpus submodule materialized, and exits nonzero naming the submodule remedy when the submodule is not materialized | behavioral | Build in a scratch copy with the submodule materialized and assert the PDF exists; empty the submodule directory, rebuild, and assert a nonzero exit whose message names the submodule remedy |
| SC-5 | Every section in §2.5 is wired into `master.tex` and renders in the built PDF | behavioral | Build the document, extract the section headings from the built document's text, and assert each of the ten named sections is present |
| SC-6 | `data/grammar-rules.yaml` carries a file-level `revision` date and the ten rules of §2.3, each with a non-empty `statement`, `scope`, and `authority`; the document's rendered rule statements are exactly the file's `statement` values, compared sentence for sentence in both directions | behavioral | Read the rule file and assert the revision date, the ten ids, and the three non-empty fields each; extract the statements inside the document's `\grammarrule{...}` environments and compare them with the file's `statement` values in both directions |
| SC-7 | The four generated files — sourcing table, proofing checklist table, bibliography, and as-of metadata — are byte-identical to the generator's output for the tracked inputs | structural | Run the generator into a scratch directory and compare each output file byte for byte with its tracked counterpart |
| SC-8 | No tracked LaTeX source under the document root carries table content of its own: the sourcing table's rows, the checklist's rows, the bibliography's entries, and the as-of anchor values appear only in the generated files | structural | A test that reads the tracked LaTeX sources, strips the `\input` of the generated files, and asserts that none of the generated files' table rows appears in the hand-written sources |
| SC-9 | Figures F1–F5 appear in the built PDF, each is referenced from a section source, and each carries its caption | behavioral | Extract the built document's text and assert the five captions are present; assert each figure's label is referenced from at least one section source |
| SC-10 | The built PDF's extracted text carries the generated payload: a known registry source id with its proofing state from the generated sourcing table, the checklist's status values, the bibliography's entries, and the precedence order's provisional-status statement | behavioral | Extract the built document's text and assert each of the four payload elements is present, with the registry source id and the proofing state taken from the generated sourcing table and the status values taken from the generated checklist table |
| SC-11 | The document's citation of the corpus runbook resolves: the cited path exists under the corpus submodule, and the cited rule ids are present in that runbook | structural | A test that resolves the cited path under `corpus/` and asserts each cited rule id appears in the runbook text |
| SC-12 | Every source in `data/sources.yaml` resolves to a corpus dossier row, every corpus work the grammar records anchor resolves to a dossier row, the document's sourcing table row count equals the join size, every registry `tier_roles` value is one of the five tier roles, and the neighbor marker is carried in its own `classification` field | structural | A test over the registry, the grammar records' anchors, the corpus store, and the generated sourcing table |
| SC-13 | The freshness gate fails loud when the corpus store drifts from the record: with the corpus store's files altered, the build exits nonzero and names the drift; with them unaltered, the build succeeds | behavioral | Build in a scratch copy with the corpus store's files altered and assert a nonzero exit naming the drift; build the unaltered copy and assert success |
| SC-14 | The document states its as-of anchors — the rule set's revision date, the corpus commit it was generated against, the digest of the corpus store at that commit, and the tier vocabulary — and each anchor is stamped from a tracked input rather than typed by hand | structural | A test that reads the generated metadata file and compares each anchor with the tracked input it derives from — the rule file's `revision`, the submodule's commit, the store's digest, and `TIER_NAMES` — and asserts the document's text carries those values |
| SC-15 | The root `AGENTS.md` and `paper/evergreen/grammar-reconstruction-methodology/AGENTS.md` each name the four trigger events — a corpus material change, a proofed segment landing, a rule change, a registry change — and the refresh steps that each event fires | structural | A test that asserts each event name and each named refresh surface appears in both files |
| SC-16 | The root `AGENTS.md` records the one-way corpus dependency and the decision not to add a `grammar/` submodule registration in the corpus repository, with the cycle named | structural | A text check over the root `AGENTS.md` for the dependency statement, the registration decision, and the cycle's ground |
| SC-17 | The `corpus/` submodule pin is advanced to a commit that carries the corpus store, and the document's recorded corpus commit matches the checked-out submodule commit | structural | A test that compares the recorded commit in the generated metadata with `git -C corpus rev-parse HEAD` |
| SC-18 | The default test tier is green with the document's gate tests included | behavioral | `uv run pytest test/` executed in this repository; the passing output recorded in the session evidence |

## 4. Impact

**Consumers.** The grammar program itself: the method document tells a linguist
which source supports a claim and under what conditions the claim may be
made. The corpus repository consumes the reverse direction — this repository's
rules and registry are the authority the corpus-side dossier is joined
against (algonquian-library#68). The grammar records' `fill_plan` fields
(snea-grammar#4 SC-7) are the machine-readable counterpart of the document's
pull rules.

**Risk.** The document is published, and a document that misstates a rule or
a proofing state misleads a reader who has no way to see the machinery behind
it. The gates are therefore mechanical and fail loud: a stale generated file,
a drifted corpus store, and a registry/dossier disagreement each stop the
build rather than shipping a wrong document. The fill precedence order
remains a provisional working order pending linguist review, and the document
says so rather than presenting it as settled.

**Blast radius.** A new `paper/evergreen/` tree with its scope registry, a new
`data/grammar-rules.yaml`, one new module in the package, a corpus submodule
pin advance, the root `AGENTS.md` (its structure table, its tier paragraph,
its agent conventions, and the corpus-dependency statement), the
`data/sources.yaml` neighbour-marker change, and a change-control row in
snea-grammar#4's spec. The grammar records, the three existing renderings,
and the corpus repository's own surfaces are untouched.

## 5. Non-goals

- The grammar records themselves, and the descriptive, teaching, and
  prescriptive renderings — snea-grammar#3, #4, and #5 own them.
- The evidence-tier assignment of any source, and the fill precedence order's
  content: this repository owns them, but this issue renders them, it does not
  re-decide them. The precedence order remains a provisional working order
  pending linguist review, and the document says so.
- Mirroring sources and standing up the corpus `private/` reference library —
  algonquian-library#34, #44, and #66 own them.
- The corpus-side store, checklist, and proofed extracts, and the human
  proofing passes themselves: the store and the record of proofing state are
  algonquian-library#68's; the human pass is a developer activity that no
  issue owns, and the agent never marks a passage proofed.
- The phonetic realization layer and the orthography-to-phoneme conversion
  method — the phonetics repository owns them.
- An ePub rendering of the document.

## 6. Relations and dependencies

- algonquian-library#68 — the corpus-side store, checklist, and tracked
  proofed extracts this document consumes. It lands first; the corpus pin
  advance in SC-17 depends on it, and its SC-9 carries the cross-repository
  refresh duty.
- snea-grammar#4 — the fill machinery, tier vocabulary, and precedence order
  this document renders. Its change-control record gains the cross-link and
  the neighbour-marker amendment.
- algonquian-library#66, #34 — the copy set whose dispositions the sourcing
  table shows.
- snea-grammar#3 — the alternation rules, the first consumer of the tier
  vocabulary in the knowledge base.

---

*Co-authored with AI: OpenCode (ollama-cloud/minimax-m3.1-flash)*
