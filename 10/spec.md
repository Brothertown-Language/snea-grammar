<!-- SPDX-FileCopyrightText: 2026 Michael Conrad -->
<!-- SPDX-License-Identifier: MIT -->

# The machine-readable rule set, the tracked fill-precedence order, and the registry correction

## 1. Intent

The grammar repository carries its rules and its fill-precedence order as
tracked, machine-readable files, so that the methodology document renders
them rather than restating them, and the registry's tier-role vocabulary
holds.

This spec covers the three tracked inputs the document is built from: the
rule set, the order file, and the source registry's neighbour-marker
correction — with the cross-links that make them the authority the document
and the corpus-side store resolve against.

**Design source.** The developer's statement of 2026-10-23 requires the
document to detail the tiering and the rules for determining when to pull
from which tier, and to stay current; a rendered document whose rules live
only in prose drifts from the registry that governs them.

## 2. Design record

### 2.1 The rule set

`data/grammar-rules.yaml`: a file-level `revision` date, and one entry per
rule, each carrying an id, the canonical statement the document renders, the
scope the rule binds, and the authority the rule derives from. The document
renders the statements verbatim, and the pipeline's rule-correspondence gate
compares them sentence for sentence, so a rule cannot be dropped from the
document, reworded in the document, or appear in the document without an
entry in the file.

The ten rules, each with the term its statement must carry:

| Id | Subject | Required term |
|----|---------|---------------|
| `GRM-01` | The evidence ladder and the direction of the pull: tier 1 leads, and a lower rung is reached only where the rung above is silent | `tier 1` and `silent` |
| `GRM-02` | Central corroboration supplies no surface forms | `surface form` |
| `GRM-03` | The three gap classes — architecture, usage, exponent — and what may fill each | `architecture`, `usage`, and `exponent` |
| `GRM-04` | The fill precedence order and its two ranking axes, familial distance and evidential distance | `familial` and `evidential` |
| `GRM-05` | Tier 2 fills where single-source attestation is silent | `tier 2` |
| `GRM-06` | Incompleteness stays visible: a row with no eligible source renders as pending | `pending` |
| `GRM-07` | Community dictionaries are excluded by default; use requires explicit authorization from the owning community | `community dictionar` and `authoriz` |
| `GRM-08` | The OCR sourcing rule, cited to the corpus runbook's rules `OCR-1`…`OCR-9` | `working-copy` |
| `GRM-09` | Every pending row records a fill plan; the ladder is auditable, not silent | `fill plan` |
| `GRM-10` | Tier-2 precedence follows Costa 2007's dialect grouping | `Costa` |

### 2.2 The order file

`data/fill-precedence.yaml`: one entry per ranked source, with the keys
`rank`, `source_id`, `group`, `familial_note`, `evidential_note`, `status`,
and `authority` — the authority being snea-grammar#4 §2.3.3. The two notes,
the status, and the authority are non-empty on every entry, and the `status` is
`provisional-pending-linguist-review`.

The file carries the authority's main table only: the authority's Table B
— related languages beyond the current tier vocabulary — is out of scope
pending the tier ruling, and the file gains those entries only when that
ruling lands. The file's entries are the order the authority's main table
states: `T3` `omeara-1992`;
`1` `costa-2003`; `2` `valentine-2001`; `3` `wolfart-1973`; `4`
`hockett-1939`; `5` the component substrate (a set); `6` the future-adoption
group (a set); `7` `baraga-1850`; `8` `okimasis`. A set entry carries an
empty `source_id` and a `group` name instead. The two axes are not ranked
against each other in the authority's rationale, so the file carries no
per-entry axis-ranking value: the two axes' rationales are carried
separately, in `familial_note` and `evidential_note`.

snea-grammar#4 §2.3.3 keeps its table and gains a pointer to the file, and
the file is the order's rendered form. The order remains a provisional
working order pending linguist review, and the document says so.

### 2.3 The registry correction

`data/sources.yaml` gives `masthay-1991` the tier role `neighbor` — a
Delaware-Mahican comparative source that is a neighbor language and not a
PSNEA member. The role sits outside the five-rung vocabulary, and
snea-grammar#4 SC-6 states that every registry tier role is in the 1–5
vocabulary, so the live registry contradicts that criterion.

This spec resolves the contradiction in the registry rather than blessing the
value: the `masthay-1991` entry moves its neighbor marker out of
`tier_roles` into a `classification` field of its own. After the amendment
`masthay-1991` carries no tier role — it is a neighbour-language
comparison, not a rung of the ladder, and its `classification` field says
so. The registry's invariant after the amendment: every `tier_roles` value
is one of the five tokens `tier1`…`tier5`; every `colonial_primary` or
`scholarly_edition` source carries at least one tier role unless it carries
a non-empty `classification` marker; and `masthay-1991` is the sole such
source. `test/test_sources_registry.py` gains that case.

### 2.4 The cross-links

snea-grammar#4's change-control table gains a row naming the methodology
document as the human-readable form of its §2.3 fill machinery, recording
the neighbour-marker amendment, and recording the tracked order file.
`ROADMAP.md` gains the work item the document introduces.

## 3. Success criteria

| ID | Criterion | Class | Verification method |
|----|-----------|-------|---------------------|
| SC-1 | `data/grammar-rules.yaml` carries a file-level `revision` date and the ten rules of §2.1, each with a non-empty `statement`, `scope`, and `authority` | structural | A test that reads the file and asserts the revision date, the ten ids, and the three non-empty fields on every entry |
| SC-2 | Every rule's `statement` carries its rule's required term from §2.1 | structural | A test that reads the file and asserts each statement contains its rule's required term |
| SC-3 | `data/fill-precedence.yaml` carries exactly the nine entries §2.2 fixes, in that rank order, each with a non-empty `familial_note`, `evidential_note`, `status`, and `authority`, each `status` being `provisional-pending-linguist-review`, and each carrying a `source_id` or a `group` name | structural | A test that reads the file and asserts the nine entries' ranks and identifiers, and the four non-empty fields on every entry |
| SC-4 | Every registry `tier_roles` value is one of the five tokens `tier1`…`tier5`; every `colonial_primary` or `scholarly_edition` source carries at least one tier role unless it carries a non-empty `classification` marker; and `masthay-1991` is the sole such source | structural | A test that reads `data/sources.yaml` and asserts the vocabulary, the invariant, and the named exception |
| SC-5 | snea-grammar#4's change-control table carries a row naming the methodology document, the neighbour-marker amendment, and the tracked order file, and snea-grammar#4's §2.3.3 carries a pointer to `data/fill-precedence.yaml`; where the issue-store worktree is absent, the check skips with a reason naming the provisioning step | structural | A file check on snea-grammar#4's spec for the change-control row and the §2.3.3 pointer; in a checkout without the issue-store worktree, the test skips with a reason naming the provisioning command |
| SC-6 | `ROADMAP.md` carries a work item for the methodology document, and the root `AGENTS.md` names the document root path `paper/evergreen/grammar-reconstruction-methodology/` in its repository-structure table | structural | A text check for the work item in `ROADMAP.md` and for the document root path in the root `AGENTS.md` |
| SC-7 | The default test tier is green with the rule set, the order file, and the registry checks included | behavioral | `uv run pytest test/` executed in this repository, with the passing output recorded |

## 4. Impact

**Consumers.** The methodology document, which renders both files; the
generator and the pipeline's gates, which read them; the corpus-side store,
which joins its rows against the registry's classifications; the grammar
program's records, whose `fill_plan` fields are the machine-readable
counterpart of the pull rules.

**Risk.** The rule set and the order file are the document's authority, and
the corpus-side store is joined against the registry: a registry value
outside its vocabulary, or a rule file that drifts from the document, breaks
the join or the document's claims. The gates that watch both are the
pipeline's rule-correspondence and join gates.

**Blast radius.** Two new tracked data files under `data/`; the
`data/sources.yaml` neighbour-marker change and the registry test's new
case; snea-grammar#4's spec, which gains a change-control row and a §2.3.3
pointer; `ROADMAP.md`; the root `AGENTS.md`'s structure table.

## 5. Non-goals

- The document's sections, figures, and prose — a separate spec.
- The build pipeline and its gates — a separate spec.
- The evidence-tier assignment of any source, and the fill precedence
  order's content: this repository owns them, but the document spec renders
  them. The one exception is the neighbour-marker amendment §2.3 makes,
  which corrects a registry value that sits outside the tier vocabulary
  rather than deciding any source's tier.
- The grammar records and the three existing renderings — snea-grammar#3,
  #4, and #5 own them.

## 6. Relations and dependencies

- The document spec — the document that renders these files; it lands after
  this one. The pipeline spec, which fixes the document root path this
  spec's SC-6 names, lands independently of it.
- The pipeline spec — the generator and the gates that read these files.
- snea-grammar#4 — the fill machinery, tier vocabulary, and precedence order
  these files state.
- algonquian-library#68 — the corpus-side store joined against the
  registry.

---

*Co-authored with AI: OpenCode (ollama-cloud/minimax-m3.1-flash)*
