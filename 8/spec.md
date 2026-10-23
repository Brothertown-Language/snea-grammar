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

No proofing-state record exists: the errata register
(`corpus/docs/research/sources/OCR-ERRATA.tsv`) records corrections to
already-proofed spans in four mirrors, but no record states a document's
coverage — the state token, the pass date, and the covered locators — and
nothing records what remains unproofed. The rule itself is stated in this
repository's root `AGENTS.md` and in snea-grammar#4 §2.3.4; the pull rules,
the precedence order, and the join between a rule and the source that supplies
it are stated in the spec at snea-grammar#4 §2.3 and nowhere else in full. The per-source
classifications are machine-readable in `data/sources.yaml`; the tier-role
legend is a prose comment in that file, and the tier display names live in
the package (`src/snea_grammar/render.py`). No tracked document assembles the
ladder, the pull rules, the precedence order, and the proofing state into the
one place a reader or an agent can consult.

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
| The evidence tier of a source; the fill rules; the precedence order | this repository (`data/sources.yaml`; `data/fill-precedence.yaml`; snea-grammar#4 §2.3) |
| Which documents exist, where each is held, its disposition, its proofing state, the proofed readings | algonquian-library — the grammar-source store, proofing checklist, and tracked proofed extracts (algonquian-library#68) |
| The grammar records and the anchors that consume both | this repository (`data/grammar/`) |

The document therefore joins a local authority with a corpus-side dataset. The
join is generated, not typed: the sourcing table, the proofing checklist
table, the supporting-materials table, the bibliography, and the as-of
anchors are all produced by a generator from the tracked inputs, and the
tracked LaTeX sources carry no hand-written table rows (the generated-source
rule the corpus repository already applies to its rendered volume).

The corpus side produces the store's coverage: algonquian-library#68 seeds
the dossier with a row for every source id this repository's registry holds
and for every corpus work this repository's grammar records anchor, and its
criterion permits the row set to grow. The seam's growth rule is explicit:
when this repository's registry gains a source, the corpus store gains a row
for it in the same change, and the change is recorded on both sides. This
repository's join gate checks the coverage against the live records.

### 2.3 The machine-readable rule set

The document's rules are stated in prose, and prose that a document and a
registry must agree about drifts. The rules therefore also live in a
machine-readable file, `data/grammar-rules.yaml`: a file-level `revision`
date, and one entry per rule, each carrying an id, the canonical statement
the document renders, the scope it binds, and the authority it derives from.
The document renders each canonical statement verbatim inside the environment
`\grammarrule{<id>}`, and the rule-correspondence gate asserts the two-way
correspondence between the file's statements and the document's rendered
statements — sentence for sentence, not id for id, so that a reworded rule in
the document fails the gate. The gate runs inside `paper/build.sh`.

The rule set carries these rules:

| Id | Subject | Required term in the statement |
|----|---------|-------------------------------|
| `GRM-01` | The evidence ladder and the direction of the pull: tier 1 leads, and a lower rung is reached only where the rung above is silent | `tier 1` |
| `GRM-02` | Central corroboration supplies no surface forms | `surface form` |
| `GRM-03` | The three gap classes — architecture, usage, exponent — and what may fill each | `exponent` |
| `GRM-04` | The fill precedence order and its two ranking axes, familial distance and evidential distance | `familial` |
| `GRM-05` | Tier 2 fills where single-source attestation is silent | `tier 2` |
| `GRM-06` | Incompleteness stays visible: a row with no eligible source renders as pending | `pending` |
| `GRM-07` | Community dictionaries are excluded by default; use requires explicit authorization from the owning community | `community dictionar` |
| `GRM-08` | The OCR sourcing rule, cited to the corpus runbook's rules `OCR-1`…`OCR-9` | `working-copy` |
| `GRM-09` | Every pending row records a fill plan; the ladder is auditable, not silent | `fill plan` |
| `GRM-10` | Tier-2 precedence follows Costa 2007's dialect grouping | `Costa` |

### 2.4 The fill-precedence file

The fill precedence order — the ranked sources, the two ranking axes, and
each source's rationale — is stated in snea-grammar#4 §2.3.3, which is a spec
file in the issue store rather than a tracked file in this repository. A
document that renders the order needs a tracked form of it, so the order
becomes a tracked file, `data/fill-precedence.yaml`: one entry per ranked
source, with the keys `rank`, `source_id`, `group`, `familial_note`,
`evidential_note`, and `authority` — the authority being
snea-grammar#4 §2.3.3. Each of
the three note and rationale fields — `familial_note`, `evidential_note`, and
`authority` — is non-empty on every entry, and the document renders the
ranks, the source ids, and the notes. The file's entries are the order the
document renders. snea-grammar#4 §2.3.3 keeps its table and gains a pointer
to the file; the change-control table records the pointer, and the file is the
order's rendered form. The file's nine entries are fixed by the authority:
`T3` `omeara-1992`; `1` `costa-2003`; `2` `valentine-2001`; `3` `wolfart-1973`;
`4` `hockett-1939`; `5` the component substrate (a set); `6` the future-
adoption group (a set); `7` `baraga-1850`; `8` `okimasis`. A set entry carries
an empty `source_id` and a `group` name instead.

The two axes are not ranked against each other in the authority's
rationale, so the file carries no per-entry axis: each entry's familial note
and evidential note carry both. In F3 the entries are placed on the two axes
by their notes — a source entry at a point, a set entry as a labelled band —
and the `T3` entry, the Munsee Delaware outgroup source, is placed at the
nearest point to the other entries, since it is the nearest relative. F3
draws no ladder: the five rungs and the downward pull belong to F1. The order remains a provisional working
order pending linguist review, and the document says so.

### 2.5 The figures

Five figures carry the rules. They are TikZ/forest sources, compiled into the
document, and each is referenced from the section whose rule it shows.

| Figure | What it shows |
|--------|---------------|
| F1 | The evidence ladder — five rungs, tier 1 at the top, the pull direction drawn downward, the callout that tier 4 supplies no surface forms, and the governance gate drawn as a barred side branch |
| F2 | The pull-decision flow chart — attestation first, then the gap class, then the rung, then the ranked source, then the disposition. Its terminal outcomes are the five dispositions the pull rules define (`central-arch`, `central-usage`, `internal-comparison`, `outgroup`, `incomplete-pending`), each labelled with what it yields; a tier-2 or tier-3 fill is labelled as such and never as an attested form |
| F3 | The fill-precedence diagram — the familial and evidential axes with each ranked source placed on them |
| F4 | The proofing pipeline — capture, OCR, human proofing pass, back-apply, tracked extract, citable; and the branch that leaves an unproofed passage as working-copy material |
| F5 | The traceability chain — a grammar record, its anchor, the corpus path, the tracked proofed extract, the page render |

### 2.6 The document's sections and its generated payload

The document's section set is fixed; the sections are wired into `master.tex`
in this order.

| Section | What it carries | Figure |
|---------|-----------------|--------|
| Introduction and scope | the audience, what the document is and is not, the as-of anchors | — |
| The evidence ladder | the five rungs, what each supplies, the pull direction | F1 |
| The sourcing documents | the generated sourcing table: every document the corpus store holds — its registry id, the registry's class, the store's class, its tier role, its neighbour classification where it has one, where it is held, and its proofing state | — |
| The pull rules | the gap classes, the rung each may fill, the precedence order, the pending rule | F2, F3 |
| Governance | the community-dictionary exclusion and the basis for it | — |
| The proofing gate | what counts as OCR-derived, the working-copy rule, the coverage rule | F4 |
| The proofing checklist | the generated checklist table: what is proofed and what still needs proofing | — |
| Supporting materials | the generated supporting-materials table: the tracked proofed extracts the document's citations resolve against | F5 |
| Maintenance | the currency procedure, the cross-repository responsibilities, the change-control record | — |
| Glossary | the terms the document uses | — |

The generator writes six files into the document root's `generated/`
directory, and the document consumes them as follows:

| Generated file | How the document consumes it |
|----------------|-----------------------------|
| `sourcing-table.tex` | `\input` into the sourcing-documents section |
| `proofing-checklist.tex` | `\input` into the proofing-checklist section |
| `supporting-materials.tex` | `\input` into the supporting-materials section |
| `as-of-metadata.tex` | `\input` into the introduction section, where the anchor values are printed |
| `fill-precedence.tex` | `\input` into the pull-rules section, where the order, the notes, and the F3 figure's placements are rendered |
| `generated/references.bib` | `\addbibresource` in the preamble and processed by `biber` — the bibliography is not `\input`ed |

The hand-written sources hold the prose and the `\input` commands; the table
content, the precedence order, the bibliography entries, and the anchor values
live only in the generated files. One block is exempt: the maintenance
section's change-control record, a hand-maintained dated list refreshed by the
rule-change step, which carries no table rows and is not generated content. The build asserts that the generated payload reaches the
built PDF's text.

### 2.7 The proofing state in the document

The document carries the proofing state of the passages the grammar program
sources, in three places: the sourcing table's proofing column, the
proofing-checklist section, and the supporting-materials section. All three
are generated from the corpus store. The document states the rule that
unproofed OCR'd segments are legitimate working-copy material — available for
staging, diffing, and availability scoping, never backing a citation or an
anchor until a human proofing pass covers the passage — as its own rule
`GRM-08`, citing the corpus runbook's rules `OCR-1`…`OCR-9` by id and path.
The build gate resolves that citation: the cited path must exist under the
corpus submodule and the cited rule ids must be present in the runbook.

### 2.8 The currency machinery

The document's volatile inputs are the corpus store, the registry, and the
fill-precedence file; its stable inputs are the rule set and the section
sources. The drift detectors are mechanical and fail loud:

- **The generated-source gate.** The six generated files are tracked and
  byte-identical to the generator's output for the tracked inputs, and the
  tracked LaTeX sources contain no table content of their own.
- **The rule-correspondence gate.** The document's rendered `\grammarrule`
  statements equal the rule file's `statement` values, sentence for sentence,
  in both directions.
- **The freshness gate.** The document records three things about the corpus:
  the pinned commit it was generated against, a per-file digest manifest of
  the corpus store at that commit, and an aggregate digest over the manifest.
  The manifest maps each tracked file under
  `corpus/docs/research/data/grammar-sources/` to the SHA-256 of its content;
  the aggregate digest is the SHA-256 over the manifest's sorted path-and-digest
  lines. The
  drift check runs inside `paper/build.sh` **before** the generated-source
  comparison, and the build's gate order is fixed: the drift check, the
  generated-source comparison, the rule-correspondence check, the join
  gate, the precedence gate, then the compile. The drift check compares
  generated-source comparison: it compares the digest of the checked-out
  corpus store against the recorded digest and, when they differ, fails
  naming the drifting path and the recorded and current digests. The
  generated-source comparison runs after it, so a corpus change is reported
  as corpus drift rather than as a generated-file mismatch. The pin check
  compares the recorded commit against the checked-out submodule commit.
- **The join gate.** Every source in `data/sources.yaml` resolves to a corpus
  dossier row; every dossier row that carries a `registry_id` resolves to a
  registry source; every corpus work this repository's grammar records anchor
  resolves to a dossier row; the document's sourcing table carries one row per
  corpus dossier row, and its row count equals the dossier's row count. The
  join gate's wording is the one SC-12 states, and SC-12 governs. It runs
  inside `paper/build.sh`, after the drift check and before the compile.
- **The precedence gate.** The rendered fill-precedence order equals the
  tracked order in `data/fill-precedence.yaml`, and the sourcing table's
  rendered tier-role column equals the registry's tier roles for the same
  source. It runs inside `paper/build.sh`, after the join gate and before the
  compile.

The refresh duty is recorded in two places: this repository's root `AGENTS.md`
names the trigger events and the refresh steps, and the document folder's
`AGENTS.md` carries the procedure for the folder. The trigger events and the
steps each fires are fixed:

| Event | Refresh steps |
|-------|---------------|
| A corpus material change | advance the `corpus/` submodule pin to a commit carrying the change; regenerate the six generated files; rebuild the document |
| A proofed segment landing | the same three steps, with the checklist and supporting-materials tables picking up the new row |
| A rule change | edit `data/grammar-rules.yaml`; update the document's `\grammarrule` statements to the file's new `statement` values; regenerate the six generated files; rebuild the document; record the change in the document's maintenance section |
| A registry change | edit `data/sources.yaml`; add a row for the new source in the corpus store; regenerate the six generated files; rebuild the document; record the change in snea-grammar#4's change-control table |
| A fill-precedence change | edit `data/fill-precedence.yaml`; regenerate the six generated files; rebuild the document, so that the rendered order and the F3 figure follow the file; record the change in the document's maintenance section and in snea-grammar#4's change-control table |

The cross-repository half of the duty — the corpus repository
updating its store and naming this repository's corpus-pin advance and the
methodology document's refresh among the surfaces each event fires — is
recorded in the corpus repository's own agent instructions (algonquian-library#68 SC-9).

### 2.9 The document tree, the toolchain, and the assets

The document is an evergreen document, and it follows the convention the
phonetics repository established for that class: the document root is
`paper/evergreen/grammar-reconstruction-methodology/`, the per-document scope
registry is `paper/evergreen/EVERGREEN.md`, and the build entry point
`paper/build.sh` discovers document roots generically — every
`paper/evergreen/*/` directory. This repository has no master root, so the
discovery set is the evergreen roots alone, and a root without a `master.tex`
is skipped rather than listed as a document. The registry entry names the document, its path, its entry
file, its review owner, its scope globs, and its tracked binaries directory.

The document root holds `master.tex`, the `sections/` tree, the `figures/`
tree, the `generated/` directory, and the `outputs/` directory for the tracked
PDF — the document's output is committed, as the phonetics repository commits
its evergreen document's PDF; the generated bibliography lives at
`generated/references.bib`. The build creates the `build/`
directory for intermediates; it is not tracked, and the repository's
`.gitignore` excludes it. The repository-level assets are `paper/build.sh`,
`paper/fonts/` (the vendored CharisSIL faces, with their OFL text and a
provenance record), `paper/vendor/` (the vendored linguistic-example styles),
and `paper/README.md` (the toolchain provisioning note).

The preamble loads CharisSIL (for the IPA inventory), `gb4e` (numbered
linguistic examples), `tikz` and `forest` (the figures), `booktabs`,
`biblatex` with `biber`, and `hyperref` with `cleveref` after it. The
typesetting convention follows the phonetics repository's: `\sloppy`,
`\raggedbottom`, and flexible vertical lengths in the preamble, with no layout
enforcement in the build tooling. The document's date is fixed, not `\today`, so
that the tracked PDF's text matches a later fresh build's text.

**The toolchain precondition.** The build needs Python with `uv` and the
package's dependencies (`pyyaml`), `latexmk` with the XeLaTeX engine, `biber`,
and `pdftotext`, plus the TeX packages named above. The build invokes the
generator as `uv run python -m snea_grammar.docgen`, so a scratch-copy build
needs the same environment the repository's own build needs. The provisioning
note at `paper/README.md` states the requirement and the installation
command. On a machine without the toolchain, the build-dependent
tests skip with a reason naming the missing tool and the provisioning
command, following the skip-with-instruction convention the corpus repository
uses; the rest of the suite runs.

The tier labels the document prints come from the package's `TIER_NAMES`
(`src/snea_grammar/render.py`), which is the machine-readable display
vocabulary; the root `AGENTS.md`'s tier paragraph is aligned to it in the same
change, so that the document, the renderers, and the agent instructions name
the five rungs identically.

The generator lives in the package, `src/snea_grammar/docgen.py`, with a
command-line entry point in the style of the existing render CLI, so that the
document's content is produced by the same validated package that produces
the other renderings.

### 2.10 A live registry value outside the tier vocabulary

`data/sources.yaml` gives `masthay-1991` the tier role `neighbor` — a
Delaware-Mahican comparative source that is a neighbor language and not a
PSNEA member. The role sits outside the five-rung vocabulary, and
snea-grammar#4 SC-6 states that every registry tier role is in the 1–5
vocabulary, so the live registry contradicts that criterion today.

This issue resolves the contradiction in the registry rather than blessing
the value: the `masthay-1991` entry moves its neighbor marker out of
`tier_roles` into a `classification` field of its own, so that every
`tier_roles` value in the registry is one of the five tokens `tier1`…
`tier5`, as snea-grammar#4 SC-6 requires. After the amendment `masthay-1991`
carries no tier role: it is a neighbour-language comparison, not a rung of
the ladder, and its `classification` field says so. The registry's invariant
after the amendment is that every `colonial_primary` or `scholarly_edition`
source carries at least one tier role unless it carries a non-empty
`classification` marker, and `masthay-1991` is the sole such source;
`test/test_sources_registry.py` gains that case. The document renders the neighbor
marker as a classification outside the five rungs — the sourcing table's
neighbour row sits beside the ladder rather than on a rung — and `GRM-01`
states that the pull runs through the five rungs only. The change is recorded
in snea-grammar#4's change-control table.

## 3. Success criteria

| ID | Criterion | Class | Verification method |
|----|-----------|-------|---------------------|
| SC-1 | The named paths exist: the document root's `master.tex`, `sections/` tree, `figures/` tree, `generated/` directory, `generated/references.bib`, and `outputs/` directory; the repository-level `paper/build.sh`, `paper/fonts/`, `paper/vendor/`, `paper/README.md`, `paper/fonts/OFL-CharisSIL.txt`, and `paper/fonts/PROVENANCE.md` | structural | File-existence checks over the named paths |
| SC-2 | The document is registered in `paper/evergreen/EVERGREEN.md` with its name, path, entry file, review owner, scope globs, and tracked binaries directory, and `paper/build.sh --list` names the document root | behavioral | Read the registry and assert the six registry fields for the document; run the build script's listing mode and assert the document root appears in its output |
| SC-3 | The document root path appears in the root `AGENTS.md` repository-structure table; the root `AGENTS.md`'s Exports Contract section names the methodology document and states that it is not a contract surface; and `ROADMAP.md` carries a work item for this document | structural | A text check for the document root path in the root `AGENTS.md`; a text check that the Exports Contract section names the methodology document and states it is not a contract surface; a text check for the work item in `ROADMAP.md` |
| SC-4 | `bash paper/build.sh` produces the PDF from the tracked sources in a checkout with the corpus submodule materialized, and exits nonzero naming the submodule remedy when the submodule is not materialized; and the tracked `outputs/master.pdf` corresponds to the tracked sources — its extracted text equals the extracted text of a fresh build of them, so a hand edit to a section source cannot leave the committed PDF stale (PDF byte-identity is not reproducible, the build stamps a timestamp, so the comparison is text-level) | behavioral | Build in a scratch copy with the submodule materialized and assert the PDF exists; empty the submodule directory, rebuild, and assert a nonzero exit whose message names the submodule remedy; build into a temporary directory, extract the text of both the fresh PDF and the tracked `outputs/master.pdf`, and assert the two texts are equal |
| SC-5 | Every section in §2.6 is wired into `master.tex` and renders in the built PDF | behavioral | Build the document, extract the section headings from the built document's text, and assert each of the ten named sections is present |
| SC-6 | `data/grammar-rules.yaml` carries a file-level `revision` date and the ten rules of §2.3, each with a non-empty `statement`, `scope`, and `authority`, and each `statement` carrying its rule's required term; the document's rendered rule statements are exactly the file's `statement` values, compared sentence for sentence in both directions | behavioral | Read the rule file and assert the revision date, the ten ids, the three non-empty fields each, and each statement's required term; extract the statements inside the document's `\grammarrule{...}` environments and compare them with the file's `statement` values in both directions |
| SC-7 | The six generated files — `generated/sourcing-table.tex`, `generated/proofing-checklist.tex`, `generated/supporting-materials.tex`, `generated/as-of-metadata.tex`, `generated/fill-precedence.tex`, and `generated/references.bib` — are byte-identical to the generator's output for the tracked inputs | structural | Run the generator into a scratch directory and compare each output file byte for byte with its tracked counterpart |
| SC-8 | No tracked LaTeX source under the document root carries table content of its own: the sourcing table's rows, the checklist's rows, the supporting-materials rows, and the precedence order's rows appear only in the generated `.tex` files | structural | A test that reads the tracked LaTeX sources and asserts that no row of any of the four generated tables appears in them |
| SC-9 | Figures F1–F5 appear in the built PDF, each is referenced from a section source, and each carries its caption | behavioral | Extract the built document's text and assert the five captions are present; assert each figure's label is referenced from at least one section source |
| SC-10 | The built PDF's extracted text carries the generated payload: a known registry source id with its tier role and its proofing state from the generated sourcing table, the neighbour classification of `masthay-1991`, the checklist's status values, the supporting-materials rows, each bibliography entry's rendered title, and the precedence order's provisional-status statement; and the generated sourcing table places `masthay-1991`'s tier-role cell empty with the neighbour classification in the classification column | behavioral | Extract the built document's text and assert each payload element, with the source id, tier role, and proofing state taken from the generated sourcing table, the status values from the generated checklist table, the supporting rows from the generated supporting-materials table, and the titles from the generated bibliography; read the generated sourcing table and assert `masthay-1991`'s tier-role cell is empty and its classification cell carries the neighbour marker |
| SC-11 | The document's rule `GRM-08` carries a citation of the corpus runbook — a non-empty path and the rule ids `OCR-1`…`OCR-9` — and the citation resolves: the cited path exists under the corpus submodule, and the cited rule ids are present in that runbook | structural | A test that asserts `GRM-08`'s rendered statement carries a non-empty cited path and the nine rule ids, resolves the path under `corpus/`, and asserts each cited rule id appears in the runbook text |
| SC-12 | Every `colonial_primary` or `scholarly_edition` source in `data/sources.yaml` carries at least one tier role unless it carries a non-empty `classification` marker, and `masthay-1991` is the sole such source; the sourcing table carries one row per corpus dossier row — twenty-two under the corpus store's seed — and the table's row count equals the dossier's row count; every dossier row that carries a `registry_id` resolves to a source in `data/sources.yaml`, and every source in `data/sources.yaml` resolves to a dossier row; every corpus work the grammar records anchor resolves to a dossier row; the table's rendered tier-role column equals the registry's tier roles for the same source; every registry `tier_roles` value is one of the five tokens `tier1`…`tier5`; and the neighbor marker is carried in its own `classification` field | structural | A test over the registry, the grammar records' anchors, the corpus store, and the generated sourcing table |
| SC-13 | `data/fill-precedence.yaml` carries exactly the nine entries §2.4 fixes, in that rank order, with the keys §2.4 names, each entry's `familial_note`, `evidential_note`, and `authority` non-empty, and each entry carrying a `source_id` or a `group` name; the rendered fill-precedence order equals the tracked order — the same ranks and the same identifiers, in the same sequence — and each entry's familial note and evidential note appear in the built document's text | behavioral | Read the file and assert the nine entries' ranks and identifiers against §2.4's list, assert the keys and the non-empty fields on every entry; extract the rendered order and the notes from the built document's text and compare them with the file's entries in order |
| SC-14 | The drift check fails loud when the corpus store drifts from the record: with a corpus store file altered, the build exits nonzero and the message names the drifting path and the recorded and current digests; with the store unaltered, the build succeeds | behavioral | Build in a scratch copy with one corpus store file altered and assert a nonzero exit whose message names that path and both digests; build the unaltered copy and assert success |
| SC-15 | The document states its as-of anchors — the rule set's revision date, the corpus commit it was generated against, the corpus store's per-file digest manifest and the aggregate digest over it, and the tier vocabulary — and each anchor is stamped from a tracked input rather than typed by hand | structural | A test that reads the generated metadata file and compares each anchor with the tracked input it derives from — the rule file's `revision`, the submodule's commit, the store's digest manifest and aggregate, and the package's tier names — and asserts the document's text carries those values |
| SC-16 | The root `AGENTS.md` and `paper/evergreen/grammar-reconstruction-methodology/AGENTS.md` each bind each of §2.8's five trigger events to exactly the refresh steps §2.8's table fixes for that event | structural | A test that reads both files, locates each event name, and asserts the step text that follows it in that file is the step set §2.8's table fixes for that event |
| SC-17 | The root `AGENTS.md`'s five tier labels equal the package's `TIER_NAMES` values, in order | structural | A test that extracts the five tier labels from the root `AGENTS.md`'s tier paragraph and compares them with `TIER_NAMES` |
| SC-18 | The root `AGENTS.md` records the one-way corpus dependency and the decision not to add a `grammar/` submodule registration in the corpus repository, with the cycle named | structural | A text check over the root `AGENTS.md` for the dependency statement, the registration decision, and the cycle's ground |
| SC-19 | The `corpus/` submodule pin is advanced to a commit that carries the corpus store, and the document's recorded corpus commit matches the checked-out submodule commit | structural | A test that compares the recorded commit in the generated metadata with `git -C corpus rev-parse HEAD`, and asserts that the checked-out commit carries the store — `git -C corpus cat-file -e HEAD:docs/research/data/grammar-sources/dossier.tsv` succeeds |
| SC-20 | snea-grammar#4's change-control table carries a row naming this document as the human-readable form of its §2.3 fill machinery and recording the neighbour-marker amendment and the tracked fill-precedence file; where the issue-store worktree is absent, the check skips with a reason naming the provisioning step | structural | A file check on snea-grammar#4's spec for the change-control row and its two named subjects; in a checkout without the issue-store worktree, the test skips with a reason naming the provisioning command |
| SC-21 | The suite is green; on a machine without the TeX toolchain, the build-dependent tests skip with a reason naming the missing tool and the provisioning command | behavioral | `uv run pytest test/` executed in this repository, with the passing output recorded; where the toolchain is absent, the skips' reasons are read and each names the missing tool and the provisioning command |

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
it. The gates are therefore mechanical and fail loud: a stale generated file, a
drifted corpus store, a registry/dossier disagreement, a reworded rule, and a
precedence order that diverges from its tracked form each stop the build
rather than shipping a wrong document. The fill precedence order
remains a provisional working order pending linguist review, and the document
says so rather than presenting it as settled.

**Contract status.** The methodology document and the two new tracked data
files are not exports-contract surfaces: this repository's contract enumerates
the knowledge base, the rendered grammar documents, and the source registry.
The root `AGENTS.md`'s exports-contract section gains a line saying so; the
methodology document's PDF is committed as the document's own output, and the
document is a published artifact rather than a tracked export.

**Blast radius.** A new `paper/evergreen/` tree with its scope registry; a new
`paper/build.sh`, `paper/fonts/`, `paper/vendor/`, and `paper/README.md`; a
new `data/grammar-rules.yaml` and `data/fill-precedence.yaml`; one new module
in the package; the new gate tests under `test/`, including the build-dependent
tier that skips with a reason naming the missing tool and the provisioning
command; a corpus submodule pin advance; the root `AGENTS.md` (its
structure table, its tier paragraph, its agent conventions, its
exports-contract section, and the corpus-dependency statement); the document
folder's `AGENTS.md`; snea-grammar#4's spec, which gains the change-control
row and a pointer from its §2.3.3 to the tracked fill-precedence file; the `data/sources.yaml` neighbour-marker change and the registry test's new case;
`ROADMAP.md`; and a change-control row in snea-grammar#4's spec. The grammar
records, the three existing renderings, and the corpus repository's own
surfaces are untouched.

## 5. Non-goals

- The grammar records themselves, and the descriptive, teaching, and
  prescriptive renderings — snea-grammar#3, #4, and #5 own them.
- The evidence-tier assignment of any source, and the fill precedence order's
  content: this repository owns them, but this issue renders them, it does not
  re-decide them. The precedence order remains a provisional working order
  pending linguist review, and the document says so. The one exception is
  the neighbour-marker amendment §2.10 makes to `data/sources.yaml`, which
  corrects a registry value that sits outside the tier vocabulary rather than
  deciding any source's tier.
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
  advance in SC-19 depends on it, and its SC-9 carries the cross-repository
  refresh duty.
- snea-grammar#4 — the fill machinery, tier vocabulary, and precedence order
  this document renders. Its change-control record gains the cross-link, the
  neighbour-marker amendment, and the tracked fill-precedence file.
- algonquian-library#66, #34 — the copy set whose dispositions the sourcing
  table shows.
- snea-grammar#3 — the alternation rules, the first consumer of the tier
  vocabulary in the knowledge base.

---

*Co-authored with AI: OpenCode (ollama-cloud/minimax-m3.1-flash)*
