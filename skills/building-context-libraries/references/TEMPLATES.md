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
- `skip` — Not needed for this library

---

## Conflicts Identified

- [Description of conflict]: [File A] vs [File B]

## Gaps Identified

- [Description of missing information]

---

**Awaiting user approval to proceed.**
```

---

## Synthesis Template

One synthesis file per complex source document. Transforms messy source material (transcripts, interviews) into clean working documents.

**CRITICAL:** Extract facts from the source. Do NOT invent information. Flag ambiguous statements for user clarification.

```markdown
# Synthesis: [Original Filename]

**Source:** [path to original file]
**Generated:** YYYY-MM-DD
**Status:** draft | user-approved

---

## [Topic Area]

[Clear prose stating facts extracted from the source. No filler words, speech artifacts, or incomplete thoughts.]

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

**Rules for synthesis:**
- One synthesis per source file — do not combine multiple sources
- Extract facts, decisions, principles — not verbatim quotes
- Preserve exact names, dates, figures from the source
- Flag anything ambiguous — don't interpret
- Organize by topic for clarity

---

## Foundation Module Template

```markdown
---
module_id: F#
module_name: [Name]
tier: foundation
purpose: "[What question does this answer?]"
confidence: [CONFIRMED/PROPOSED/MIXED]
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

[CONFIRMED] Information from source documents.

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
confidence: [CONFIRMED/PROPOSED/MIXED]
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

[CONFIRMED] Information from sources.

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
confidence: [CONFIRMED/PROPOSED/MIXED]
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

[CONFIRMED] Domain-specific information.

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

## Verification & Professional Objectivity

This section defines how the agent handles accuracy, verification, and user interactions. Calibrate to the agent's domain and typical use cases.

### Stakes-Based Verification

| Content Stakes | Agent Behavior |
|----------------|----------------|
| HIGH | [e.g., "Always cite source module. Flag if user asks to modify or extrapolate. Recommend human review before external use."] |
| MEDIUM | [e.g., "Cite source when directly quoting. Note when inferring from patterns."] |
| LOW | [e.g., "Use freely. Note if information may be outdated."] |

### Professional Objectivity

Agents should serve the user's actual needs, not just validate their assumptions. Define behaviors for this agent:

- **Challenge when:** [e.g., "User request contradicts documented strategy", "Proposed approach has known pitfalls", "Request requires information the agent doesn't have"]
- **Verify before:** [e.g., "Making claims about partners or clients", "Citing specific figures", "Describing legal or compliance status"]
- **Flag for review:** [e.g., "Any output intended for external audiences", "Modifications to high-stakes content", "Novel claims not in source modules"]

### Uncertainty Handling

When the agent lacks information or confidence:
- [e.g., "State clearly: 'This isn't covered in my context modules.'"]
- [e.g., "Offer to help frame the question for human research."]
- [e.g., "Never fabricate details to appear more helpful."]

### Natural Prose (External-Facing Content Only)

**Include this section only for agents that produce marketing, website copy, case studies, proposals, or other external-facing content.** Skip for internal-only agents.

```markdown
## Natural Prose

Write like a domain expert in [field], not an AI assistant.

**Banned vocabulary:** pivotal, crucial, vital, testament to, underscores, highlights, vibrant, tapestry, delve, foster, garner, leverage, landscape (figurative), holistic, robust, synergy, cutting-edge, groundbreaking, nestled, showcases, boasts, elevate

**Banned structures:**
- "Not only X but Y" — parallelisms that oversell
- "serves as" / "stands as" — use "is" instead
- "-ing" phrases for empty analysis ("highlighting the importance," "showcasing their commitment")
- Vague attribution ("experts say," "industry leaders") — name sources or state directly
- Formulaic balance ("Despite challenges, [positive spin]")

**Required:**
- Use "is" not "serves as"
- Repeat nouns rather than cycling through synonyms
- Be specific with numbers and names
- Match the voice of actual [practitioners/executives/marketers] in this field
```

Calibrate the specific vocabulary and voice guidance to the organization's industry and the agent's domain.

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
