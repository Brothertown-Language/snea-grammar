<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->
<!-- SPDX-License-Identifier: MIT -->

# The document pipeline — the evergreen tree, the toolchain, and the build gates

## 1. Intent

The grammar repository can build the methodology document from tracked
sources, and its build fails loud — naming the cause — when the document
falls behind the corpus store, the rule set, the order file, or the
registry.

This spec covers the build machinery: the document tree's skeleton, the
evergreen scope registry, the toolchain, the generator, and the build gates.
The document's content and the tracked files it renders are separate specs.

**Design source.** The developer's statement of 2026-10-23 requires the
document to stay current as the source corpus materials change, including
when proofed OCR'd segments land; the machinery that detects the drift is
this spec's subject.

## 2. Design record

### 2.1 The evergreen convention

The document is an evergreen document, and it follows the convention the
phonetics repository established for that class: the document root is
`paper/evergreen/grammar-reconstruction-methodology/`, the per-document scope
registry is `paper/evergreen/EVERGREEN.md`, and the build entry point
`paper/build.sh` discovers document roots generically — every
`paper/evergreen/*/` directory. This repository has no master root, so the
discovery set is the evergreen roots alone, and a root without a `master.tex`
is skipped rather than listed as a document. The registry entry names the
document, its path, its entry file, its review owner, its scope globs, and
its tracked binaries directory.

### 2.2 The assets

`paper/build.sh`; `paper/fonts/` — the vendored CharisSIL faces with their
OFL text and a provenance record; `paper/vendor/` — the vendored
linguistic-example styles; and `paper/README.md` — the toolchain
provisioning note. The document root holds `master.tex`, the `sections/`
tree, the `figures/` tree, the `generated/` directory, and the `outputs/`
directory for the tracked PDF. The build creates the `build/` directory for
intermediates; it is not tracked, and the repository's `.gitignore` excludes
it.

The preamble loads CharisSIL (for the IPA inventory), `gb4e` (numbered
linguistic examples), `tikz` and `forest` (the figures), `booktabs`,
`biblatex` with `biber`, and `hyperref` with `cleveref` after it. The
typesetting convention follows the phonetics repository's: `\sloppy`,
`\raggedbottom`, and flexible vertical lengths in the preamble, with no
layout enforcement in the build tooling. The document's date is fixed, not
`\today`, so that the tracked PDF's text matches a later fresh build's text.

### 2.3 The toolchain precondition

The build needs Python with `uv` and the package's dependencies (`pyyaml`),
`latexmk` with the XeLaTeX engine, `biber`, and `pdftotext`, plus the TeX
packages named above. The build invokes the generator as
`uv run python -m snea_grammar.docgen`, so a scratch-copy build needs the
same environment the repository's own build needs. The provisioning note at
`paper/README.md` states the requirement and the installation command. On a
machine without the toolchain, the build-dependent tests skip with a reason
naming the missing tool and the provisioning command, following the
skip-with-instruction convention the corpus repository uses.

### 2.4 The generator

`src/snea_grammar/docgen.py`, with a command-line entry point in the style
of the existing render CLI — `uv run python -m snea_grammar.docgen --out <dir>`
— so that the document's content is produced by the same validated package
that produces the other renderings. It reads the registry, the rule set, the
order file, and the corpus store under the `corpus/` submodule, and writes the
six generated files into the directory `--out` names. Its output is
deterministic: the same inputs produce byte-identical outputs.

### 2.5 The build gates

The build's gate order is fixed, and each gate fails loud naming its cause:

1. **The drift check** — compares the checked-out corpus store's per-file
   digests and its aggregate digest against the digests the document
   recorded, and when they differ fails naming the drifting path and the
   recorded and current digests. It never compares generated files, which
   the next gate does, so a corpus change is reported as corpus drift rather
   than as a generated-file mismatch.
2. **The generated-source comparison** — compares the six generated files
   with the generator's output for the tracked inputs.
3. **The rule-correspondence check** — compares the document's rendered
   `\grammarrule` statements with the rule set's `statement` values, sentence
   for sentence, in both directions.
4. **The join gate** — every dossier row that carries a `registry_id`
   resolves to a registry source, every corpus work the grammar records
   anchor resolves to a dossier row, and the sourcing table carries one row
   per dossier row. A registry source the store has no row for fails this
   gate, and the store gains that row in the same change — the
   cross-repository duty the corpus store's agent instructions record.
5. **The precedence gate** — the rendered fill-precedence order equals the
   tracked order, and the sourcing table's rendered tier-role column equals
   the registry's tier roles.

Then the compile. The pin check — the document's recorded corpus commit against the
checked-out submodule commit — is part of the drift check, so a corpus pin
that advanced without the document's regeneration is reported as drift.

## 3. Success criteria

| ID | Criterion | Class | Verification method |
|----|-----------|-------|---------------------|
| SC-1 | The named paths exist: the document root's `master.tex`, `sections/` tree, `figures/` tree, `generated/` directory, and `outputs/` directory; and the repository-level `paper/build.sh`, `paper/fonts/`, `paper/vendor/`, `paper/README.md`, `paper/fonts/OFL-CharisSIL.txt`, and `paper/fonts/PROVENANCE.md` | structural | File-existence checks over the named paths |
| SC-2 | The document is registered in `paper/evergreen/EVERGREEN.md` with its name, path, entry file, review owner, scope globs, and tracked binaries directory, and `paper/build.sh --list` names the document root | behavioral | Read the registry and assert the six registry fields; run the build script's listing mode and assert the document root appears in its output |
| SC-3 | The provisioning note names each required tool — Python with `uv`, `latexmk` with the XeLaTeX engine, `biber`, and `pdftotext` — with its installation command; and where a tool is absent, the build-dependent tests skip with a reason naming the missing tool and the provisioning command | structural | A text check over `paper/README.md` for each of the four tools and an installation command; in a checkout without a tool, a test's skip reason is read and checked for the missing tool and the command |
| SC-4 | `bash paper/build.sh` produces the PDF from the tracked sources with the corpus submodule materialized, and exits nonzero naming the submodule remedy when the submodule is not materialized | behavioral | Build in a scratch copy with the submodule materialized and assert the PDF exists; empty the submodule directory, rebuild, and assert a nonzero exit whose message names the submodule remedy |
| SC-5 | The generator reads the registry, the rule set, the order file, and the corpus store, writes the six generated files into the directory `--out` names, and produces byte-identical output for the same inputs | structural | Run the generator twice with `--out` naming a scratch directory and compare the two runs byte for byte, and compare each output with its tracked counterpart |
| SC-6 | Each of the five build gates fails loud naming its cause when its condition is violated, and the gates run in the §2.5 order | behavioral | In a scratch copy, break each gate's condition in turn — a corpus store file altered, the corpus pin moved, a generated file edited, a rule statement reworded, a dossier row removed, the order file reordered — and assert the build exits nonzero with a message naming that gate's cause; assert the reported cause order matches §2.5 |
| SC-7 | The default test tier is green with the pipeline's gate tests included | behavioral | `uv run pytest test/` executed in this repository, with the passing output recorded |

## 4. Impact

**Consumers.** The methodology document, which this pipeline builds; the
grammar program's readers, who receive the tracked PDF; the corpus
repository, whose store the drift check watches.

**Risk.** The gates are the only thing standing between a stale input and a
published document that misstates a rule or a proofing state, so a gate that
fails silently is worse than no gate. The build's failure modes are
therefore named, and the toolchain's absence produces a reasoned skip
rather than a red suite.

**Blast radius.** A new `paper/evergreen/` tree with its scope registry; a
new `paper/build.sh`, `paper/fonts/`, `paper/vendor/`, and `paper/README.md`;
one new module in the package; the corpus submodule pin advance; the
`build/` exclusion already carried by the repository's `.gitignore`.

## 5. Non-goals

- The document's sections, figures, and prose — a separate spec.
- The rule set, the order file, and the registry correction — a separate
  spec.
- The grammar records and the three existing renderings — snea-grammar#3,
  #4, and #5 own them.
- The corpus-side store and its tool — algonquian-library#68 owns them.

## 6. Relations and dependencies

- The document spec — the content this pipeline builds; it lands after this
  one.
- The knowledge-inputs spec — the rule set and the order file the generator
  reads; it lands before this one.
- algonquian-library#68 — the corpus store the drift check watches and the
  join gate reads.

---

*Co-authored with AI: OpenCode (ollama-cloud/minimax-m3.1-flash)*
