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

## 2. Design record

### 2.1 What the document states, and what it does not

The document states four things, each of which a reader of the grammar
program needs and none of which is currently readable outside a spec file:

1. **The evidence ladder** — the five tiers (SNEA-attested; SNEA-internal
   comparison; Munsee Delaware outgroup; Central Algonquian corroboration;
   Proto-Algonquian anchor), what each rung may supply, and the direction of
   the pull.
2. **The sourcing documents** — every source the grammar program may anchor
   to, its class, its tier role, where it is held, and its proofing state.
3. **The pull rules** — the gap classes (architecture, usage, exponent), which
   rung may fill which class, the fill precedence order within a rung, and the
   rule that a row with no eligible source stays visibly pending.
4. **The proofing gate** — what counts as OCR-derived, that unproofed OCR is
   working-copy material, that the proofing pass covers the used portions at
   locator level, and what is currently proofed and what is not.

The document does not restate the grammar itself, the lexicon, or the
phonetic realization — those are the other renderings and the other
repositories' surfaces. It is the method document.

### 2.2 Where the document lives, and the cut line with the corpus repository

The document lives in this repository. The evidence it presents about the
corpus's holdings is consumed through the `corpus/` submodule, which this
repository already holds; the corpus repository consumes nothing from this
repository, and a `grammar/` submodule registration in the corpus repository
would close the graph into a cycle.

The cut line is fact ownership, and it is the one already drawn in
snea-grammar#4 §2.4:

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

### 2.3 The machine-readable rule set

The document's rules are stated in prose, and prose that a document and a
registry must agree about drifts. The rules therefore also live in a
machine-readable file, `data/grammar-rules.yaml`: one entry per rule, each
carrying an id, the canonical sentence the document renders, the scope it
binds, and the authority it derives from. The document renders the canonical
sentences verbatim inside a marked environment, and the build gate asserts
the two-way correspondence: every rule in the file is rendered, and every
rendered rule has an entry in the file.

The rule set covers, at minimum: the ladder and the pull direction
(`GRM-01`); Central corroboration supplying no surface forms (`GRM-02`); the
three gap classes and what may fill each (`GRM-03`); the fill precedence
order and its two ranking axes (`GRM-04`); tier 2 filling where single-source
attestation is silent (`GRM-05`); incompleteness staying visible (`GRM-06`);
community dictionaries excluded by default (`GRM-07`); the OCR sourcing rule,
cited to the corpus runbook's rules (`GRM-08`); the fill-plan recording duty
(`GRM-09`); tier-2 precedence following Costa 2007's dialect grouping
(`GRM-10`).

### 2.4 The figures

Five figures carry the rules. They are TikZ/forest sources, compiled into the
document, and each is referenced from the section whose rule it shows.

| Figure | What it shows |
|--------|---------------|
| F1 | The evidence ladder — five rungs, tier 1 at the top, the pull direction drawn downward, the callout that tier 4 supplies no surface forms, and the governance gate drawn as a barred side branch |
| F2 | The pull-decision flow chart — attestation first, then the gap class, then the rung, then the ranked source, then the disposition, with the three terminal outcomes: attested form, usage statement, visibly pending |
| F3 | The fill-precedence diagram — the familial and evidential axes with each ranked source placed on them |
| F4 | The proofing pipeline — capture, OCR, human proofing pass, back-apply, tracked extract, citable; and the branch that leaves an unproofed passage as working-copy material |
| F5 | The traceability chain — a grammar record, its anchor, the corpus path, the tracked proofed extract, the page render |

### 2.5 The proofing state in the document

The document carries the proofing state of the passages the grammar program
sources, in two places: the sourcing table's proofing column, and a
checklist section that lists what is proofed and what still needs proofing.
Both are generated from the corpus store. The document states the rule that
unproofed OCR'd segments are legitimate working-copy material — available for
staging, diffing, and availability scoping, never backing a citation or an
anchor until a human proofing pass covers the passage — as its own rule
`GRM-08`, citing the corpus runbook's rules `OCR-1`…`OCR-7` by id and path.
The build gate resolves that citation: the cited path must exist under the
corpus submodule and the cited rule ids must be present in the runbook.

### 2.6 The currency machinery

The document's volatile inputs are the corpus store and the registry; its
stable inputs are the rule set and the section sources. The drift detectors
are mechanical and fail loud:

- **The generated-source gate.** The four generated files are tracked and
  byte-identical to the generator's output for the tracked inputs.
- **The freshness gate.** The document records the corpus pin it was
  generated against; when the checked-out corpus store differs from that
  record, the build fails naming the drift.
- **The join gate.** Every in-program source in `data/sources.yaml` resolves
  to a corpus dossier row and the reverse holds; the document's sourcing
  table row count equals the join size.

The refresh duty is recorded in two places: this repository's root `AGENTS.md`
names the trigger events and the refresh steps, and the document folder's
`AGENTS.md` carries the procedure for the folder. The trigger events are a
corpus material change, a proofed segment landing, a rule change, and a
registry change. The cross-repository duty — the corpus repository updating
its store and advancing this repository's corpus pin — is recorded in the
corpus repository's own agent instructions (algonquian-library#68 SC-7).

### 2.7 The document tree and the toolchain

The document lives at `paper/grammar-reconstruction-methodology/`: `master.tex`,
a `sections/` tree, `figures/`, a `generated/` directory, `references.bib`
(generated), `outputs/` for the tracked PDF, and `build/` for intermediates.
The repository's build entry point is `paper/build.sh`, following the
convention in the phonetics repository.

The preamble loads CharisSIL (vendored under `paper/fonts/` with its OFL
text, for the IPA inventory), `gb4e` (numbered linguistic examples),
`tikz` and `forest` (the figures), `booktabs`, `biblatex` with `biber`, and
`hyperref` with `cleveref` after it. The typesetting convention follows the
phonetics repository's: `\sloppy`, `\raggedbottom`, and flexible vertical
lengths in the preamble, with no layout enforcement in the build tooling.

The generator lives in the package, `src/snea_grammar/docgen.py`, with a
command-line entry point in the style of the existing render CLI, so that the
document's content is produced by the same validated package that produces
the other renderings.

## 3. Success criteria

| ID | Criterion | Class | Verification method |
|----|-----------|-------|---------------------|
| SC-1 | The document tree exists at `paper/grammar-reconstruction-methodology/` and holds `master.tex`, the section sources, the figure sources, the `generated/` directory, `paper/build.sh`, the vendored fonts, and the tracked output path; the tree path appears in the root `AGENTS.md` repository-structure table | structural | File-existence checks over the named paths; a text check that the tree path appears in the root `AGENTS.md` |
| SC-2 | `bash paper/build.sh` produces the PDF from the tracked sources in a checkout with the corpus submodule materialized; a build with an unmaterialized corpus submodule exits nonzero naming the remedy | behavioral | Run the build script in a scratch copy of the repository with the corpus submodule materialized and assert the PDF exists; run it with the corpus submodule directory emptied and assert a nonzero exit whose message names the submodule remedy |
| SC-3 | Every section named in the scope is wired into `master.tex` and renders in the built PDF; the rules rendered in the document are exactly the rules in `data/grammar-rules.yaml` — every file entry is rendered and every rendered rule has a file entry | behavioral | Build the document, extract the section headings and the rendered rule statements from the built sources, and compare the rule set with the file's entry set in both directions |
| SC-4 | The four generated files — sourcing table, proofing checklist table, bibliography, and as-of metadata — are byte-identical to the generator's output for the tracked inputs | structural | Run the generator into a scratch directory and compare each output file byte for byte with its tracked counterpart |
| SC-5 | Figures F1–F5 appear in the built PDF, each is referenced from a section source, and each carries its caption | behavioral | Extract the built document's text and assert the five captions are present; assert each figure's label is referenced from at least one section source |
| SC-6 | The document's citation of the corpus runbook resolves: the cited path exists under the corpus submodule, and the cited rule ids are present in that runbook | structural | A test that resolves the cited path under `corpus/` and asserts each cited rule id appears in the runbook text |
| SC-7 | The join holds: every in-program source in `data/sources.yaml` resolves to a corpus dossier row, every in-program dossier row resolves to a registry source, and the document's sourcing table row count equals the join size | structural | A test over the registry, the corpus store, and the generated sourcing table |
| SC-8 | The freshness gate fails loud when the corpus store drifts from the record: with the corpus store altered, the build exits nonzero and names the drift; with it unaltered, the build succeeds | behavioral | Build in a scratch copy with the corpus store's dossier altered and assert a nonzero exit naming the drift; build the unaltered copy and assert success |
| SC-9 | The document states its as-of anchors — the rule-set revision date, the corpus pin it was generated against, and the registry's tier vocabulary — and each anchor is stamped from a tracked input rather than typed by hand | structural | A test that reads the generated metadata file and compares each anchor with the tracked input it derives from, and asserts the document's text carries those values |
| SC-10 | The root `AGENTS.md` and `paper/grammar-reconstruction-methodology/AGENTS.md` each name the four trigger events — a corpus material change, a proofed segment landing, a rule change, a registry change — and the refresh steps that each event fires | structural | A test that asserts each event name and each named refresh surface appears in both files |
| SC-11 | The root `AGENTS.md` records the one-way corpus dependency and the decision not to add a `grammar/` submodule registration in the corpus repository, with the cycle named | structural | A text check over the root `AGENTS.md` for the dependency statement, the registration decision, and the cycle's ground |
| SC-12 | The `corpus/` submodule pin is advanced to a commit that carries the corpus store, and the document's recorded corpus pin matches the checked-out submodule commit | structural | A test that compares the recorded pin in the generated metadata with `git -C corpus rev-parse HEAD` |
| SC-13 | The default test tier is green with the document's gate tests included | behavioral | `uv run pytest test/` executed in this repository; the passing output recorded in the session evidence |

## 4. Non-goals

- The grammar records themselves, and the descriptive, teaching, and
  prescriptive renderings — snea-grammar#3, #4, and #5 own them.
- The evidence-tier assignment of any source, and the fill precedence order's
  content: this repository owns them, but this issue renders them, it does not
  re-decide them. The precedence order remains a provisional working order
  pending linguist review, and the document says so.
- Mirroring sources, standing up the corpus `private/` reference library, and
  performing the human proofing passes — algonquian-library#34, #44, #66, and
  #67 own them.
- The corpus-side store, checklist, and proofed extracts — algonquian-library#68
  builds them; this issue consumes them.
- The phonetic realization layer and the orthography-to-phoneme conversion
  method — the phonetics repository owns them.
- An ePub rendering of the document.

## 5. Relations and dependencies

- algonquian-library#68 — the corpus-side store, checklist, and tracked
  proofed extracts this document consumes. It lands first; the corpus pin
  advance in SC-12 depends on it.
- snea-grammar#4 — the fill machinery, tier vocabulary, and precedence order
  this document renders. Its change-control record gains the cross-link.
- algonquian-library#66, #34 — the copy set whose dispositions the sourcing
  table shows.
- snea-grammar#3 — the alternation rules, the first consumer of the tier
  vocabulary in the knowledge base.

---

*Co-authored with AI: OpenCode (ollama-cloud/minimax-m3.1-flash)*
