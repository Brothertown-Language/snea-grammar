<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->
<!-- SPDX-License-Identifier: MIT -->

# The evergreen grammar-reconstruction methodology document — sections, figures, and generated payload

## 1. Intent

The grammar repository carries a PDF, compiled from tracked LaTeX, that
states which sources serve which evidence tier, when a claim may be pulled
from which tier, and the proofing state of the passages it rests on — and
that stays current as its inputs change.

This spec covers the document's content: its sections, its figures, its
generated tables, and the agent instructions that make its refresh a duty.
The machinery that builds it and the tracked files it renders are separate
specs.

**Design source.** The developer's statement of 2026-10-23: a top-level
evergreen PDF built from TeX, detailing the grammar sourcing documents and
their tiering and the rules for determining when to pull from which tier,
with ladder diagrams and flow charts as figures; the research behind the
document and the document itself kept current on changes to the source
corpus materials, including when proofed OCR'd segments land; unproofed
OCR'd segments treated as legitimate material with a checklist of what has
been proofed and what needs proofing; and the proofed extracts tracked as
supporting materials. The developer's direction of the same day to split the
work between the grammar repository and the corpus repository along
separation-of-concern lines, and to place submodule-registration adjustments
in scope.

## 2. Design record

### 2.1 The cut line with the corpus repository

The document's subject is the grammar program's method, and the method is
this repository's: the evidence tiers, the pull rules, the precedence order.
The evidence the document presents about the corpus's holdings is consumed
through the `corpus/` submodule, which this repository already holds; the
corpus repository consumes nothing from here, and a `grammar/` registration
in the corpus repository would close the graph corpus → grammar → corpus.
The document therefore joins a local authority with a corpus-side dataset,
and the join is generated rather than typed.

### 2.2 The sections

The document's section set is fixed; the sections are wired into `master.tex`
in this order.

| Section | What it carries | Figure |
|---------|-----------------|--------|
| Introduction and scope | the audience, what the document is and is not, the as-of anchors | — |
| The evidence ladder | the five rungs, what each supplies, the pull direction | F1 |
| The sourcing documents | the generated sourcing table: every document the corpus store holds, its registry id, the registry's class, the store's class, its tier role, its neighbour classification where it has one, where it is held, and its proofing state | — |
| The pull rules | the gap classes, the rung each may fill, the precedence order, the pending rule | F2, F3 |
| Governance | the community-dictionary exclusion and the basis for it | — |
| The proofing gate | what counts as OCR-derived, the working-copy rule, the coverage rule | F4 |
| The proofing checklist | the generated checklist table: what is proofed and what still needs proofing | — |
| Supporting materials | the generated supporting-materials table: the tracked proofed extracts the document's citations resolve against | F5 |
| Maintenance | the currency procedure, the cross-repository responsibilities, the change-control record | — |
| Glossary | the terms the document uses | — |

### 2.3 The figures

| Figure | What it shows |
|--------|---------------|
| F1 | The evidence ladder — five rungs, tier 1 at the top, the pull direction drawn downward, the callout that tier 4 supplies no surface forms, and the governance gate drawn as a barred side branch |
| F2 | The pull-decision flow chart — attestation first, then the gap class, then the rung, then the ranked source, then the disposition. Its terminal outcomes are the five dispositions the pull rules define (`central-arch`, `central-usage`, `internal-comparison`, `outgroup`, `incomplete-pending`), each labelled with what it yields; a tier-2 or tier-3 fill is labelled as such and never as an attested form |
| F3 | The fill-precedence diagram — the familial and evidential axes with each ranked source placed on them; a source entry at a point, a set entry as a labelled band, and the outgroup entry nearer the PSNEA end than rank 1, because the order ranks sources within a rung and never across rungs. F3 draws no ladder — the five rungs and the downward pull belong to F1 |
| F4 | The proofing pipeline — capture, OCR, human proofing pass, back-apply, tracked extract, citable; and the branch that leaves an unproofed passage as working-copy material |
| F5 | The traceability chain — a grammar record, its anchor, the corpus path, the tracked proofed extract, the page render |

### 2.4 The generated payload

The generator writes six files into the document root's `generated/`
directory: `sourcing-table.tex`, `proofing-checklist.tex`,
`supporting-materials.tex`, `as-of-metadata.tex`, `fill-precedence.tex`, and
`references.bib`. The first five are `\input` by their sections; the
bibliography is `\addbibresource`d and processed by `biber`. The hand-written
sources hold the prose and the `\input` commands; the table content, the
precedence order, the bibliography entries, and the anchor values live only
in the generated files. One block is exempt: the maintenance section's
change-control record, a hand-maintained dated list refreshed by the
rule-change step, which carries no table rows and is not generated content.

The sourcing table carries the registry's class and the store's class as
separate columns, and the neighbour classification in a column of its own, so
that a source with no tier role — a neighbour-language comparison — shows
its classification outside the rung column.

### 2.5 The rules the document renders

The document's rules are rendered verbatim from the tracked rule set, inside
the environment `\grammarrule{<id>}`; the fill-precedence order is rendered
from the tracked order file, together with the notes that carry the two
ranking axes. The rule set's and the order file's own schemas, and the
neighbour-marker correction in the source registry, are a separate spec.

The document's rule `GRM-08` carries the citation of the corpus runbook: a
non-empty path and the rule ids `OCR-1`…`OCR-9`, resolved under the corpus
submodule.

### 2.6 The as-of anchors and the currency duty

The document states its as-of anchors — the rule set's revision date, the
corpus commit it was generated against, the corpus store's per-file digest
manifest and the aggregate digest over it, and the tier vocabulary — each
stamped from a tracked input rather than typed by hand. The corpus commit
and the digests are the drift record the pipeline's drift check compares
against.

The refresh duty is recorded in this repository's root `AGENTS.md` and in the
document folder's `AGENTS.md`, each binding the trigger events to the steps
each fires:

| Event | Refresh steps |
|-------|---------------|
| A corpus material change | advance the `corpus/` submodule pin to a commit carrying the change; regenerate the six generated files; rebuild the document |
| A proofed segment landing | the same three steps, with the checklist and supporting-materials tables picking up the new row |
| A rule change | edit the rule set; update the document's `\grammarrule` statements to the file's new values; regenerate the six generated files; rebuild the document; record the change in the document's maintenance section |
| A fill-precedence change | edit the order file; regenerate the six generated files; rebuild the document; record the change in the document's maintenance section and in snea-grammar#4's change-control table |
| A registry change | edit the source registry; add a row for the new source in the corpus store; regenerate the six generated files; rebuild the document; record the change in snea-grammar#4's change-control table |

The cross-repository half of the duty — the corpus repository updating its
store and naming this repository's corpus-pin advance and the methodology
document's refresh among the surfaces each event fires — is recorded in the
corpus repository's own agent instructions (algonquian-library#68).

## 3. Success criteria

| ID | Criterion | Class | Verification method |
|----|-----------|-------|---------------------|
| SC-1 | Every section in §2.2 is wired into `master.tex` and renders in the built PDF | behavioral | Build the document, extract the section headings from the built document's text, and assert each of the ten named sections is present |
| SC-2 | Figures F1–F5 compile into the built PDF, each is referenced from a section source, and each carries its caption; and the build log records no missing-file or float-lost error for them | behavioral | Extract the built document's text and assert the five captions; assert each figure's source file is `\input` by a section and its label is referenced; assert the build log carries no missing-file or float-lost error for the five |
| SC-3 | The built PDF's extracted text carries the generated payload: a known registry source id with its tier role and its proofing state, the neighbour classification of a tier-role-less source, the checklist's status values, the supporting-materials rows, each bibliography entry's rendered title, and the precedence order's provisional-status statement | behavioral | Extract the built document's text and assert each payload element, with the values taken from the generated files |
| SC-4 | The document's rendered `\grammarrule` statements equal the rule set's `statement` values, sentence for sentence, in both directions | behavioral | Extract the statements inside the document's `\grammarrule{...}` environments and compare them with the rule file's statements in both directions |
| SC-5 | The rendered fill-precedence order equals the tracked order — the same ranks and the same identifiers, in the same sequence — and each entry's familial and evidential notes appear in the built document's text | behavioral | Extract the rendered order and the notes from the built document's text and compare them with the order file's entries in order |
| SC-6 | The document's rule `GRM-08` carries a non-empty cited path and the nine rule ids, and the citation resolves: the cited path exists under the corpus submodule and the cited rule ids are present in that runbook | structural | A test that asserts `GRM-08`'s rendered statement carries a non-empty path and the nine ids, resolves the path under `corpus/`, and asserts each cited rule id appears in the runbook text |
| SC-7 | The tracked `outputs/master.pdf` corresponds to the tracked sources: its extracted text equals the extracted text of a fresh build of them (the comparison is text-level — a PDF build stamps a timestamp, and the document's date is fixed) | behavioral | Build the document into a temporary directory, extract the text of both the fresh PDF and the tracked PDF, and assert the two texts are equal |
| SC-8 | The root `AGENTS.md` and the document folder's `AGENTS.md` each carry a refresh-duty entry in their agent-conventions section, and in that entry each of §2.6's five trigger events names the actions its row fixes for it | structural | A test that reads each file's agent-conventions section, locates each of the five event names, and asserts that the actions of that event's row appear, in the row's order, within that event's entry |
| SC-9 | The document's maintenance section carries a change-control record whose entries are dated and name their subject, and it carries an entry for the current rule-set revision — carrying the rule file's `revision` date — and an entry naming the tracked order file | structural | A text check that the maintenance section's record contains the rule file's `revision` date and the order file's path |
| SC-10 | The default test tier is green with the document's gate tests included | behavioral | `uv run pytest test/` executed in this repository, with the passing output recorded |

## 4. Impact

**Consumers.** The grammar program itself: the method document tells a
linguist which source supports a claim and under what conditions the claim
may be made. The corpus repository consumes the reverse direction — this
repository's rules and registry are the authority the corpus-side dossier is
joined against (algonquian-library#68). The grammar records' `fill_plan`
fields (snea-grammar#4 SC-7) are the machine-readable counterpart of the
document's pull rules.

**Risk.** The document is published, and a document that misstates a rule or
a proofing state misleads a reader who has no way to see the machinery behind
it. The pipeline's gates are mechanical and fail loud, and this document's
content is rendered from the tracked files rather than typed, so a stale
generated file, a drifted corpus store, a registry/dossier disagreement, a
reworded rule, and a precedence order that diverges from its tracked form
each stop the build rather than shipping a wrong document. The fill
precedence order remains a provisional working order pending linguist
review, and the document says so.

**Blast radius.** The document tree's section and figure sources; the
document folder's `AGENTS.md`; the root `AGENTS.md`'s agent conventions and
its structure table.

## 5. Non-goals

- The document's build pipeline, the toolchain, the fonts, and the build
  gates — a separate spec.
- The machine-readable rule set, the tracked fill-precedence order, and the
  source registry's neighbour-marker correction — a separate spec.
- The grammar records and the descriptive, teaching, and prescriptive
  renderings — snea-grammar#3, #4, and #5 own them.
- The corpus-side store, checklist, and proofed extracts, and the human
  proofing passes themselves — algonquian-library#68 owns the store; the
  human pass is a developer activity that no issue owns.
- The phonetic realization layer and the orthography-to-phoneme method — the
  phonetics repository owns them.
- An ePub rendering of the document.

## 6. Relations and dependencies

- The document-pipeline spec — the build machinery this document is built
  by; it lands first.
- The knowledge-inputs spec — the rule set and the order file this document
  renders; it lands first.
- algonquian-library#68 — the corpus-side store, checklist, and tracked
  proofed extracts this document consumes, and the cross-repository refresh
  duty its SC-7 records.
- snea-grammar#4 — the fill machinery, tier vocabulary, and precedence order
  this document renders.

---

*Co-authored with AI: OpenCode (ollama-cloud/minimax-m3.1-flash)*
