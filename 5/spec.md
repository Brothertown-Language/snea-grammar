---
issue_number: 5
title: "[SPEC] Brothertown Language realization profile — Phase 2 community-ratified synthesis"
state: open
created_at: "2026-10-12T04:50:00Z"
synced_from: "https://github.com/Brothertown-Language/snea-grammar/issues/5"
---

# Brothertown Language realization profile — Phase 2 community-ratified synthesis

**Author:** AI agent
**Design source:** the 2026-10-11/12 design sessions (developer rulings, recorded in the
snea-phonetics#118 design record and the developer-approved `ROADMAP.md`, item W3)

## 1. Goal

Build the realization-profile layer through which the Brothertown Language — the
community-ratified synthesis of the ancestor SNEA varieties — lives over the PSNEA
core. The design session fixed the model: the profile is **recorded norm data with
provenance**, not a separate grammar and never an agent-invented blend; the
community decides, the repository records.

## 2. Design record

### 2.1 Gating

Implementation waits on:

1. **Phase 1 content** — the alternation rules (snea-grammar#3) and the paradigm
   architecture (snea-grammar#4): a profile selects among or instantiates core
   records; with too little core there is nothing to profile.
2. **The community ratification process itself** — community-gated, not
   agent-gated. The mechanism below can be built when the gates open; the profile's
   *content* arrives only as recorded community decisions.

### 2.2 The profile mechanism

- **Profile records** keyed to PSNEA core records: each profile record references
  the core record(s) it realizes and carries the profile's value for them — an
  exponent choice, a variant selection, an orthographic rendering decision.
- **Norm status per the existing schema**: `ratified` (real recorded provenance:
  ratifying body, date, decision reference) or `unratified_variants` (the ancestor
  varieties' attested variants listed, no norm). `provisional` exists for
  repo-default structural records, not for synthesis decisions — a synthesis value
  is either ratified on a recorded decision or openly unratified. **Legitimate
  ratification sources**: a recorded community decision, or a recorded project
  direction (the stake-holder's explicit determination, as with the notation
  standard PSN-RUL-005) — what is excluded is anything the agent invents. The
  seed's ratified profile value is a real recorded project direction: the
  Brothertown Language renders surface forms in the Costa alphabet + IPA (the
  2026-10-11 direction), which is a realization-layer decision by construction.
- **No fabrication, mechanically enforced**: the validator already rejects a
  ratified norm without provenance fields; this item extends the same discipline to
  profile records.
- **One grammar, mechanically**: profile records are a distinct record kind
  (`profile`, added to the kind vocabulary) and carry a required `realizes` field
  referencing existing core-record ids — the validator rejects a `realizes`
  reference to a nonexistent or non-core id. By construction a profile record
  cannot restate structure: it selects among or instantiates core records.
- **Community-orthography overrides are display-time only**: the storage form stays
  in the Costa alphabet (the recorded notation standard, PSN-RUL-005); overrides
  (e.g. the Wôpanâak orthography) live in a display-override structure applied by
  the renderers, never in stored surface forms.
- **One grammar**: profile records reference core record ids; they do not restate
  structural claims. The PSNEA core remains the single source; the profile is the
  realization layer.

## 3. Success criteria

| ID | Criterion | Class | Verification method |
|----|-----------|-------|---------------------|
| SC-1 | Profile records exist, each referencing the PSNEA core record(s) it realizes, passing the schema validator with norm status required | structural | `uv run pytest test/` — validator passes over profile records; a test asserts every profile record carries ≥1 core-record reference |
| SC-2 | A ratified profile value requires recorded provenance (ratifying body, date, decision reference); the validator rejects one without | structural | A test asserting the validator rejects a ratified profile record missing any provenance field, and accepts one with all three |
| SC-3 | Unratified profile points render as "no norm yet — variants attested" over the ancestor varieties' attested variants; ratified values render with their provenance | behavioral | Run the prescriptive renderer over seed profile data containing both states; assert both behaviors in the output |
| SC-4 | Community-orthography overrides are display-time only: stored surface fields validate against the Costa alphabet inventory, and the renderer applies the override mapping at output time | behavioral | A test asserting stored forms pass the inventory check while rendered output shows the overridden orthography |
| SC-5 | Profile records are `kind: profile` (a new kind in the vocabulary) with a required `realizes` field; the validator rejects a `realizes` reference to a nonexistent id or to a non-core record | structural | A test asserting the validator rejects a profile record whose `realizes` names a missing id or another profile record, and accepts one referencing existing structure/paradigm/rule records |

## 4. Non-goals

- The PSNEA core itself (items W1, W2).
- Convening or deciding community ratifications — the repository records decisions;
  the community's process is the community's.
- Per-language standalone grammars.
- Phonetic realization (snea-phonetics).

## 5. Change control

| Date | Change | Author |
|------|--------|--------|
| 2026-10-12 | Initial spec from the design sessions and ROADMAP W3 | AI agent |

---

🤖 Co-authored with AI: OpenCode (huggingface/zai-org/GLM-5.3-Flash)
