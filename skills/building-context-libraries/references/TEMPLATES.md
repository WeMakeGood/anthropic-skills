# Module and Agent Templates

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

# [Module Name]

## Purpose

[One paragraph: what organizational knowledge does this provide?]

## Scope

**Included:** [What this covers]
**Not Included:** [What's in other modules] → See [Other Module]

---

## [Content Section]

[Verified information from source documents]

### [Subsection]

[Organized content]

---

## Cross-References

**Related:**
- [Module Name]: [How it relates]

---

## Agent Instructions

When using this module:
- [How to apply this knowledge]
- [What to prioritize]
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

# [Module Name]

## Purpose

[What cross-functional knowledge does this provide?]

## Scope

**Included:** [What this covers]
**Not Included:** [What's elsewhere] → See [Module]

---

## [Content Section]

> **Requires [Foundation Module]** for organizational context.

[Verified information from sources]

### [Subsection]

[Content organized for clarity]

| Item | Description |
|------|-------------|
| ... | ... |

---

## Cross-References

**Requires:**
- [Foundation Module]: [Why needed]

**Related:**
- [Module]: [Relationship]

---

## Agent Instructions

- [How agents apply this]
- [When it applies vs doesn't]
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

# [Module Name]

## Purpose

[Domain-specific knowledge for particular roles]

## Scope

**Included:** [Domain content]
**Not Included:**
- [General info] → See [Foundation Module]
- [Cross-functional] → See [Shared Module]

---

## [Domain Content]

> **Requires [Shared Module]** for methodology.
> **Requires [Foundation Module]** for org context.

[Verified domain-specific information]

---

## Cross-References

**Requires:**
- [Foundation]: [Context needed]
- [Shared]: [Methodology needed]

---

## Agent Instructions

Agents with this module can:
- [Domain capability 1]
- [Domain capability 2]
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
    - F2_[name]
  shared:
    - S1_[name]
  specialized:
    - D1_[name]
estimated_tokens: [total]
last_updated: YYYY-MM-DD
---

# [Agent Name]

## Role

[2-3 sentences: what this agent does]

## Responsibilities

1. [Primary responsibility]
2. [Secondary responsibility]
3. [Additional responsibility]

## Knowledge Sources

| Area | Module | Why Needed |
|------|--------|------------|
| [Area] | [Module] | [Reason] |

## Guidelines

**Do:**
- [Behavior]
- [Approach]

**Don't:**
- [Avoid]
- [Pitfall]

## Required Modules

All agents must load **F#_agent_behavioral_standards** (anti-hallucination, epistemic honesty, professional objectivity).

External-facing agents must also load **S#_natural_prose_standards** (AI-detectable writing patterns to avoid).

These modules are copied from `templates/guardrails/` during Phase 4. Do not duplicate their content in agent definitions — just reference them in the modules list.

## Domain-Specific Guidance (Optional)

If this agent has domain-specific verification needs beyond the standard guardrails, add them here:

- **Additional verification:** [e.g., "Always verify partner names against F1"]
- **Escalation:** [e.g., "Flag pricing questions for human review"]
- **Domain constraints:** [e.g., "Never provide legal advice"]

## Token Budget

- Foundation: [X] tokens
- Shared: [X] tokens
- Specialized: [X] tokens
- **Total: [X] tokens** ([X]% of 20K limit)
```

## Proposal Template

**IMPORTANT:** The proposal describes STRUCTURE, not content. Do not pre-write module content or summarize organizational information. The proposal lists what modules you will create and why.

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
