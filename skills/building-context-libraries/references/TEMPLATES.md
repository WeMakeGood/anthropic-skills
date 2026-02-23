# Module and Agent Templates

## Build State Template

The build state file tracks progress across sessions. It is the first file any resumed session reads. See `templates/build-state.md` for the full template.

Create this file at `<OUTPUT_PATH>/build-state.md` during Phase 1 (after completing the source index).

Key fields:
- **Current Phase** — which phase the build is in
- **Read this phase file next** — pointer to the phase instruction file in `references/phases/`
- **Phase Completion Status** — table tracking all 7 phases
- **Module Build Checklist** — tracks each module individually during Phase 5
- **User Decisions Log** — records conflicts resolved, gaps accepted, scope changes

---

## Source Index Template

The source index is the master manifest for the entire build. It tracks every source file, its status, and what working source to use for module building.

```markdown
# Source Index

**Generated:** YYYY-MM-DD
**Source path:** [SOURCE_PATH]
**Output path:** [OUTPUT_PATH]
**Status:** indexing | synthesizing | ready | building | complete

---

## Source Files

| File | Type | Status | Working Source | Notes |
|------|------|--------|----------------|-------|
| [relative/path/to/file.md] | strategy | ready | original | [brief note] |
| [relative/path/to/transcript.md] | transcript | needs-synthesis | — | [brief note] |
| [relative/path/to/transcript.md] | transcript | synthesized | synthesis/transcript-synthesis.md | [brief note] |

### Type Values
- `strategy` — Polished positioning, decisions (use directly)
- `operational` — Current processes, structures (use directly)
- `transcript` — Conversational, needs synthesis
- `interview` — Q&A format, needs synthesis
- `notes` — Meeting notes, may need synthesis
- `reference` — Supporting material (use directly)

### Status Values
- `ready` — Can be used directly for module building
- `needs-synthesis` — Must be synthesized before use
- `synthesized` — Synthesis complete, use the synthesis file
- `skip` — Not needed for this library (requires explicit user approval)

---

## HOW TO USE THIS INDEX

This index is your working checklist. Follow these steps:

1. **Read files in order** — process each file listed in the checklist below
2. **Update the checklist** — after reading each file, mark it [x] and add notes
3. **Add conflicts/gaps** — record issues in the sections below as you find them
4. **Do not skip files** — every file must be read and marked
5. **Do not proceed** to Phase 2 until all files are marked complete

---

## Reading Checklist

**Mark each file [x] as you read it. Add notes about what you found.**

- [ ] 1. `[path/to/file.md]` — *notes: [add after reading]*
- [ ] 2. `[path/to/another.md]` — *notes: [add after reading]*

---

## Conflicts Identified

**Add conflicts here as you discover them:**

*Example: Document A says X, but Document B says Y — need to resolve*

- *(none yet)*

---

## Gaps Identified

**Add missing information here as you discover it:**

*Example: No information found about pricing structure*

- *(none yet)*

---

## Next Steps

When ALL files above are marked [x]:

1. Review the Conflicts and Gaps sections you filled in
2. Update the Status field at the top to `ready`
3. Present this completed index to the user for approval
4. **Do NOT proceed to synthesis until user approves this index**
```

---

## Synthesis Template

One synthesis file per complex source document. Transforms messy source material (transcripts, interviews) into clean working documents that LLM agents can use.

**CRITICAL:** You are creating content for LLM agents, not preserving the original document. The synthesis must be:
- **Clean** — No filler words, speech artifacts, false starts, or conversational rambling
- **Direct** — State facts, don't attribute them with "they said" or "he mentioned"
- **Actionable** — An LLM agent could use this to make decisions
- **Organized** — Group by topic, not by speaker or chronology

```markdown
# Synthesis: [Original Filename]

**Source:** [path to original file]
**Generated:** YYYY-MM-DD
**Status:** draft | user-approved

---

## [Topic Area]

[Direct statements of fact. Not "John said X" but simply "X is true."]
[Organized principles, not conversational fragments.]
[Decision criteria in "If X, then Y" format where applicable.]

## [Topic Area]

[Additional synthesized content organized by topic.]

---

## Flagged for Clarification

Items that need user input before this synthesis can be approved:

- [Ambiguous statement — what did they mean by X?]
- [Unclear reference — who/what is Y?]
- [Possible error — source says Z but this seems inconsistent with...]

---

**Awaiting user review.**
```

**What synthesis IS:**
- Extracting meaning from messy sources
- Stating facts directly ("The company prioritizes X")
- Organizing by topic for agent consumption
- Creating actionable guidance

**What synthesis is NOT:**
- Preserving quotes with attribution
- Light editing of transcripts
- Keeping conversational structure
- "They said X, and also mentioned Y"

**WRONG (preserves transcript structure):**
```
John mentioned that the team "always tries to meet clients where they are."
He also noted that they focus on "quick wins" for new clients.
Sarah added that overwhelming clients with technical details is avoided.
```

**RIGHT (synthesized for agent use):**
```
## Client Engagement Approach

Adapt to client's current state:
- New clients: Focus on quick wins, minimize technical complexity
- Established clients: Deeper technical engagement appropriate

Avoid overwhelming clients with jargon regardless of their level.
```

**Rules for synthesis:**
- One synthesis per source file — do not combine multiple sources
- Extract facts, decisions, principles — never copy quotes
- Preserve exact names, dates, figures from the source
- Flag anything ambiguous — don't interpret
- Organize by topic, not by speaker or document order
- **Test:** Would an LLM agent find this useful, or confusing?

---

## Foundation Module Template

```markdown
---
module_id: F#
module_name: [Name]
tier: foundation
purpose: "[What question does this answer?]"
last_updated: YYYY-MM-DD
---

<!-- BUILD REMINDERS (remove from final module):
- Re-read working sources BEFORE writing this module. Do not write from memory.
- Re-read this module's SCOPE from the proposal. Do not include addenda or other-module content.
- This module should be METAPROMPTING — behavioral instructions for agents, not just facts.
- HIGH-STAKES content (legal names, EINs, addresses, titles, dates): copy EXACTLY from source.

TRANSFORMATION TEST — ask these three questions about every section you write:
1. Does this change how the agent BEHAVES? If not, it's content — transform it.
2. Could the agent act on this without further interpretation? If not, add decision logic.
3. Does this read like a Wikipedia article or a system prompt? It must read like the latter.

DURABILITY CHECKS:
- No volatile specifics (counts, prices, named lists that change). Move to an addendum and reference it instead. BUT: process parameters (timelines, thresholds, review cycles) are durable — keep them. Volatile = changes when business grows. Durable = changes only if processes are redesigned.
- Guide, don't catalog. Teach creation principles, not inventories of what exists. BUT: "If prospect says X, respond by Y" is behavioral guidance, not a catalog — keep response patterns.
- Respect scope boundaries. If content belongs in addenda or another module, reference it. BUT: content near addenda in a source file isn't automatically out of scope. Test against the proposal, not source proximity.
- Frame example lists as illustrative, not exhaustive. State criteria separately.

BAD:  "The organization offers Advisory, Implementation, and Managed services."
GOOD: "When recommending services, match to client AI maturity: Advisory for early-stage,
       Implementation for committed adopters, Managed for ongoing support needs."

If you catch yourself writing "The organization does X" without "When Y happens, do Z" — STOP and transform.

COMPACTION DEFENSE:
- Did you re-read ARCHITECTURE.md and the phase rules for this module? If not, stop and read them now.
- Did you check completed modules that share sources with this one? If not, check now.
- Do not restate content already in a completed module — cross-reference it instead.
-->

<!-- VERIFICATION LOG — REMOVE THIS BLOCK before finalizing. It is a build artifact, not part of the module.
| Fact | Source File | Exact Source Text |
|------|-------------|-------------------|
| [fact] | [file] | [exact quote] |
-->

# [Module Name]

## Purpose

[One paragraph: what decisions does this module help agents make?]

## Scope

**Included:** [What this covers]
**Not Included:** [What's in other modules] → See [Other Module]

---

## [Behavioral Section — what agents should DO with this knowledge]

[Metaprompting and context, not just facts.
"When discussing X, frame it as Y" not just "X exists."
"If asked about Z, respond by emphasizing A" not just "Z is true."]

### [Subsection]

[Decision criteria in "If X, do Y" format where applicable.]

---

## Cross-References

**Related:**
- [Module Name]: [How it relates]

---

## Agent Instructions

When using this module:
- [Specific behavioral guidance]
- [Priority rules for this knowledge area]
```

## Shared Module Template

```markdown
---
module_id: S#
module_name: [Name]
tier: shared
purpose: "[What question does this answer?]"
used_by: [agent types that need this]
last_updated: YYYY-MM-DD
---

<!-- BUILD REMINDERS (remove from final module):
- Re-read working sources BEFORE writing this module. Do not write from memory.
- Re-read this module's SCOPE from the proposal. Do not include addenda or other-module content.
- This module should be METAPROMPTING — behavioral instructions for agents, not just facts.
- HIGH-STAKES content (legal names, EINs, addresses, titles, dates): copy EXACTLY from source.

TRANSFORMATION TEST — ask these three questions about every section you write:
1. Does this change how the agent BEHAVES? If not, it's content — transform it.
2. Could the agent act on this without further interpretation? If not, add decision logic.
3. Does this read like a Wikipedia article or a system prompt? It must read like the latter.

DURABILITY CHECKS:
- No volatile specifics (counts, prices, named lists that change). Move to an addendum and reference it instead. BUT: process parameters (timelines, thresholds, review cycles) are durable — keep them. Volatile = changes when business grows. Durable = changes only if processes are redesigned.
- Guide, don't catalog. Teach creation principles, not inventories of what exists. BUT: "If prospect says X, respond by Y" is behavioral guidance, not a catalog — keep response patterns.
- Respect scope boundaries. If content belongs in addenda or another module, reference it. BUT: content near addenda in a source file isn't automatically out of scope. Test against the proposal, not source proximity.
- Frame example lists as illustrative, not exhaustive. State criteria separately.

BAD:  "The organization offers Advisory, Implementation, and Managed services."
GOOD: "When recommending services, match to client AI maturity: Advisory for early-stage,
       Implementation for committed adopters, Managed for ongoing support needs."

If you catch yourself writing "The organization does X" without "When Y happens, do Z" — STOP and transform.

COMPACTION DEFENSE:
- Did you re-read ARCHITECTURE.md and the phase rules for this module? If not, stop and read them now.
- Did you check completed modules that share sources with this one? If not, check now.
- Do not restate content already in a completed module — cross-reference it instead.
-->

<!-- VERIFICATION LOG — REMOVE THIS BLOCK before finalizing. It is a build artifact, not part of the module.
| Fact | Source File | Exact Source Text |
|------|-------------|-------------------|
| [fact] | [file] | [exact quote] |
-->

# [Module Name]

## Purpose

[What decisions does this module help agents make?]

## Scope

**Included:** [What this covers]
**Not Included:** [What's elsewhere] → See [Module]

---

## [Behavioral Section]

> **Requires [Foundation Module]** for organizational context.

[Metaprompting and context — behavioral instructions, not just information.]

### [Subsection]

[Decision criteria and behavioral guidance organized for agent use.]

---

## Cross-References

**Requires:**
- [Foundation Module]: [Why needed]

**Related:**
- [Module]: [Relationship]

---

## Agent Instructions

- [How agents apply this knowledge]
- [When it applies vs doesn't]
- [Priority rules]
```

## Specialized Module Template

```markdown
---
module_id: D#
module_name: [Name]
tier: specialized
purpose: "[Domain-specific question this answers]"
used_by: [specific agents]
last_updated: YYYY-MM-DD
---

<!-- BUILD REMINDERS (remove from final module):
- Re-read working sources BEFORE writing this module. Do not write from memory.
- Re-read this module's SCOPE from the proposal. Do not include addenda or other-module content.
- This module should be METAPROMPTING — behavioral instructions for agents, not just facts.
- HIGH-STAKES content (legal names, EINs, addresses, titles, dates): copy EXACTLY from source.

TRANSFORMATION TEST — ask these three questions about every section you write:
1. Does this change how the agent BEHAVES? If not, it's content — transform it.
2. Could the agent act on this without further interpretation? If not, add decision logic.
3. Does this read like a Wikipedia article or a system prompt? It must read like the latter.

DURABILITY CHECKS:
- No volatile specifics (counts, prices, named lists that change). Move to an addendum and reference it instead. BUT: process parameters (timelines, thresholds, review cycles) are durable — keep them. Volatile = changes when business grows. Durable = changes only if processes are redesigned.
- Guide, don't catalog. Teach creation principles, not inventories of what exists. BUT: "If prospect says X, respond by Y" is behavioral guidance, not a catalog — keep response patterns.
- Respect scope boundaries. If content belongs in addenda or another module, reference it. BUT: content near addenda in a source file isn't automatically out of scope. Test against the proposal, not source proximity.
- Frame example lists as illustrative, not exhaustive. State criteria separately.

BAD:  "The organization offers Advisory, Implementation, and Managed services."
GOOD: "When recommending services, match to client AI maturity: Advisory for early-stage,
       Implementation for committed adopters, Managed for ongoing support needs."

If you catch yourself writing "The organization does X" without "When Y happens, do Z" — STOP and transform.

COMPACTION DEFENSE:
- Did you re-read ARCHITECTURE.md and the phase rules for this module? If not, stop and read them now.
- Did you check completed modules that share sources with this one? If not, check now.
- Do not restate content already in a completed module — cross-reference it instead.
-->

<!-- VERIFICATION LOG — REMOVE THIS BLOCK before finalizing. It is a build artifact, not part of the module.
| Fact | Source File | Exact Source Text |
|------|-------------|-------------------|
| [fact] | [file] | [exact quote] |
-->

# [Module Name]

## Purpose

[What domain-specific decisions does this module enable?]

## Scope

**Included:** [Domain content]
**Not Included:**
- [General info] → See [Foundation Module]
- [Cross-functional] → See [Shared Module]

---

## [Domain Behavioral Section]

> **Requires [Shared Module]** for methodology.
> **Requires [Foundation Module]** for org context.

[Metaprompting and context — domain-specific behavioral instructions for agents.]

---

## Cross-References

**Requires:**
- [Foundation]: [Context needed]
- [Shared]: [Methodology needed]

---

## Agent Instructions

Agents with this module should:
- [Domain-specific behavioral guidance]
- [Decision rules for this domain]
```

## Agent Definition Template

```markdown
---
agent_name: [Name]
agent_domain: [domain]
purpose: "[What this agent does]"
modules:
  foundation:
    - F1_[name]
    - F_agent_behavioral_standards
  shared:
    - S1_[name]
    - S_natural_prose_standards  # if external-facing
  specialized:
    - D1_[name]
addenda:  # optional — only if this agent consults reference data
  - addendum_name: "[what data]"
estimated_tokens: [total]
last_updated: YYYY-MM-DD
---

# [Agent Name]

## Role

[2-3 sentences: what this agent does — focused on actions and decisions, not knowledge]

## Responsibilities

1. [Primary responsibility — what the agent produces or decides]
2. [Secondary responsibility]
3. [Additional responsibility]

## Knowledge Sources

| Area | Module | Why Needed |
|------|--------|------------|
| [Area] | [Module ID] | [What decisions this enables] |

## Reference Addenda (Optional)

If this agent consults reference data (pricing, biographical details, service catalogs), list the addenda here. Addenda are loaded on demand when modules direct the agent to consult them — they do not count against the module token budget.

| Addendum | When Consulted |
|----------|----------------|
| [addenda/name.md] | [What triggers the agent to load this — e.g., "When building proposals that include pricing"] |

## Guidelines

**Do:**
- [Behavioral instruction]
- [Approach to follow]

**Don't:**
- [Anti-pattern to avoid]
- [Common mistake]

## Domain-Specific Guidance (Optional)

Only add guidance here that extends beyond the standard guardrail modules:

- **Additional verification:** [e.g., "Always verify partner names against F1"]
- **Escalation:** [e.g., "Flag pricing questions for human review"]
- **Domain constraints:** [e.g., "Never provide legal advice"]

## Token Budget

- Foundation: [X] tokens
- Shared: [X] tokens
- Specialized: [X] tokens
- **Total: [X] tokens** ([X]% of per-agent limit)
- Addenda: not counted (loaded on demand)
```

## Addendum Template

Addenda contain volatile reference data — not behavioral instructions. They are proposed alongside modules in Phase 4, built after modules in Phase 5, and validated in Phase 7.

```markdown
---
addendum_id: A#_[name]
addendum_name: [Name]
purpose: "[What reference data this provides]"
referenced_by: [which modules reference this addendum]
update_frequency: "[quarterly | annually | on-demand | when-changed]"
last_updated: YYYY-MM-DD
---

<!-- VERIFICATION LOG — REMOVE THIS BLOCK before finalizing. It is a build artifact, not part of the addendum.
| Data Point | Source File | Exact Source Text |
|------------|-------------|-------------------|
| [data] | [file] | [exact quote] |
-->

# [Addendum Name]

> **This is a reference addendum, not a module.** It contains data that changes
> as the business evolves. Modules reference this file rather than embedding
> its contents. When this data changes, update this file — modules will not
> need to change.

---

## [Data Section]

[Tables, lists, rates, biographical details, catalogs, inventories —
whatever reference data this addendum provides.
HIGH-STAKES content (pricing, legal details) must be copied exactly from source.]

---

*Source: [source files]*
*Last verified: YYYY-MM-DD*
```

**Addenda design rules:**
- **Data only.** If you're writing "When X, do Y" — that belongs in a module, not an addendum.
- **Source-verified.** Every data point must trace to a working source, same as modules.
- **Referenced, not orphaned.** At least one module must point to this addendum. If no module references it, it shouldn't exist.
- **Self-contained.** Each addendum covers one type of reference data. Don't combine pricing and biographies in one file.
- **Update-aware.** The frontmatter includes `update_frequency` so the user knows how often to review it.

---

## Proposal Template

**IMPORTANT:** The proposal describes STRUCTURE, not content. Do not pre-write module content or summarize organizational information. The proposal lists what modules and addenda you will create and why.

```markdown
# Context Library Proposal

## Proposed Module Structure

### Foundation Modules

| ID | Name | Purpose | Est. Tokens |
|----|------|---------|-------------|
| F1 | [Name] | [Purpose] | [Est] |

### Shared Modules

| ID | Name | Purpose | Used By | Est. Tokens |
|----|------|---------|---------|-------------|
| S1 | [Name] | [Purpose] | [Agents] | [Est] |

### Specialized Modules

| ID | Name | Purpose | Used By | Est. Tokens |
|----|------|---------|---------|-------------|
| D1 | [Name] | [Purpose] | [Agents] | [Est] |

### Addenda (Reference Data)

| ID | Name | Purpose | Referenced By | Key Sources | Update Frequency |
|----|------|---------|---------------|-------------|------------------|
| A1 | [Name] | [What data this provides] | [which modules] | [sources] | [quarterly/annually/on-demand] |

## Shared Source Ownership

<!-- When a source file feeds multiple modules, assign each content area to one module.
     This prevents duplication during the Phase 5 build. -->

| Source File | Content Area | Owned By | Other Modules Cross-Reference Via |
|-------------|-------------|----------|-----------------------------------|

## Agent-Module Mapping

| Agent | Foundation | Shared | Specialized | Total |
|-------|------------|--------|-------------|-------|
| [Agent] | F1,F2,F3 | S1,S2 | D1 | [X]K |

## Information Gaps

### Blocking
- [Gap]: [Impact] - **Need input before proceeding**

### Limiting
- [Gap]: [Impact] - Can proceed, note in validation

### Enhancing
- [Gap]: [Impact] - Low priority

## Questions for Approval

1. [Question about structure]
2. [Question about scope]

---

**Awaiting approval to proceed with build.**
```
