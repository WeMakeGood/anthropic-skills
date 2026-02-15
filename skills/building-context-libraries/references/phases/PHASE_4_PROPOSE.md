# Phase 4: Propose Structure

> **CRITICAL RULES — Read these first, even if you read nothing else:**
> - NO CONTENT IN PROPOSALS. The proposal describes structure, not organizational information.
> - NO FABRICATION. Every detail must trace to a working source you actually read.
> - If you're writing "The organization focuses on..." or "Key services include..." — STOP. That's content.
> - Token estimates must reflect source richness, not arbitrary targets. Don't compress.
> - Every proposed module must answer: "What decision does this help an agent make?"

---

## What This Phase Does

Create a structural plan describing WHAT you will build — module names, purposes, source mappings, agent assignments, and token estimates. The proposal contains zero organizational content.

## Before You Start

1. **Read `<OUTPUT_PATH>/build-state.md`** — confirm Phase 3 is complete.
2. **Read `<OUTPUT_PATH>/analysis.md`** — this is your input for the proposal.
3. **Read `<OUTPUT_PATH>/source-index.md`** — reference for source mappings.

---

## Create the Proposal

Save to: `<OUTPUT_PATH>/proposal.md`

### Proposal Structure

```markdown
# Context Library Proposal

**Generated:** YYYY-MM-DD
**Source index:** [path]

---

<!-- EMBEDDED RULES (for session resilience):
When building modules from this proposal in Phase 5:
- Re-read working sources BEFORE writing each module. Do not write from memory.
- Modules are METAPROMPTS, not fact sheets. Write context and agent instructions, not copied content.
- NEVER invent details. If it's not in the working sources, it's not in the module.
- HIGH-STAKES content (legal names, EINs, addresses, titles, dates, financials) must be copied exactly.
- Read references/phases/PHASE_5_BUILD.md before starting any module.
- Re-read each module's SCOPE from this proposal before writing. Do not include content designated as addenda or assigned to other modules.

TRANSFORMATION TEST for every module section:
1. Does this change how the agent BEHAVES? If not, it's content — transform it.
2. Could the agent act on this without interpretation? If not, add "If X, do Y" logic.
3. Does this read like a system prompt or a Wikipedia article? Must be the former.

ACTOR TEST for every instruction:
"Who is performing this action — the LLM agent, or the human user?"
If the human: tell the LLM how to SUPPORT that behavior, not try to BE the human.

DURABILITY TESTS:
- VOLATILE SPECIFICS: Would this number, price, or list be wrong if it changed tomorrow? Move it to an addendum, don't embed it in the module. BUT: process parameters (escalation timelines, budget thresholds, review cycles) are durable behavioral guidance — keep them. Volatile = changes when business grows. Durable = changes only if processes are redesigned.
- CATALOG vs. GUIDE: Does this teach what exists, or how to create? Teach creation principles, not inventories. BUT: "If prospect says X, respond by Y" is behavioral guidance, not a catalog — keep objection-handling and response patterns.
- SCOPE BOUNDARIES: Is this content designated as addenda or for a different module? Reference it, don't include it. BUT: content near addenda in a source file is not automatically out of scope. Test against the proposal's assignment, not source file proximity. Methodology near pricing is still methodology.
- EXAMPLES as CONSTRAINTS: Does this list of categories/sectors restrict rather than illustrate? Frame as non-exhaustive and state criteria separately.

BAD:  "The organization offers Advisory, Implementation, and Managed services."
GOOD: "When recommending services, match to client AI maturity: Advisory for early-stage,
       Implementation for committed adopters, Managed for ongoing support needs."
-->

## Proposed Module Structure

### Foundation Modules

| ID | Name | Purpose (what decision it supports) | Key Sources | Est. Tokens |
|----|------|-------------------------------------|-------------|-------------|
| F1 | [Name] | [What question does this answer for agents?] | [source files] | [estimate] |

### Shared Modules

| ID | Name | Purpose | Used By | Key Sources | Est. Tokens |
|----|------|---------|---------|-------------|-------------|
| S1 | [Name] | [Purpose] | [which agents] | [source files] | [estimate] |

### Specialized Modules

| ID | Name | Purpose | Used By | Key Sources | Est. Tokens |
|----|------|---------|---------|-------------|-------------|
| D1 | [Name] | [Purpose] | [which agents] | [source files] | [estimate] |

### Addenda (Reference Data)

| ID | Name | Purpose | Referenced By | Key Sources | Update Frequency |
|----|------|---------|---------------|-------------|------------------|
| A1 | [Name] | [What data this provides] | [which modules] | [source files] | [quarterly/annually/on-demand] |

Addenda contain volatile reference data that modules point to. They are built after modules in Phase 5. They do NOT count against agent token budgets. See ARCHITECTURE.md for the module-vs-addenda classification test.

## Agent-Module Mapping

| Agent | Role | Foundation | Shared | Specialized | Est. Total |
|-------|------|------------|--------|-------------|------------|
| [Agent] | [What it does] | F1,F2 | S1,S2 | D1 | [X]K |

## Information Gaps

### Blocking (must resolve before building)
- [Gap]: [Impact] — **Need user input**

### Limiting (can proceed, noted in validation)
- [Gap]: [Impact]

### Enhancing (low priority)
- [Gap]: [Impact]

## Conflicts Requiring Resolution

- [Conflict]: Source A says X, Source B says Y — [proposed resolution]

## Questions for Approval

1. [Question about structure]
2. [Question about scope]

---

**Awaiting approval to proceed with build.**
```

---

## Module Design Rules

### Purpose Test
Every module must answer: "What decision does this help an agent make?" If the answer is unclear, the module is too abstract or taxonomic.

### Organize for Use, Not Taxonomy

**Wrong (taxonomy-based):**
- "Organizational Facts" — a grab-bag of facts
- "Services List" — just a list

**Right (use-based):**
- "Organizational Identity & Positioning" — helps agents represent the org authentically
- "Client Engagement Methodology" — helps agents guide client interactions

### Token Estimates

- Base on source content richness, not arbitrary targets
- Per-agent module budget: **10% of the target model's context window** (e.g., 20K tokens for a 200K-context model). Addenda do not count — they are loaded on demand.
- Most modules should be 2,000-4,000 tokens
- Modules under 1,000 tokens are almost certainly too thin
- Do NOT compress to hit a low number — sparse modules are worse than rich ones

### Standard Guardrail Modules

Every library includes two required guardrail modules (copied from templates during Phase 5):
- **F_agent_behavioral_standards** — All agents load this
- **S_natural_prose_standards** — External-facing agents load this

Include these in the agent-module mapping. Do not create custom versions.

---

## Update Build State

Update `<OUTPUT_PATH>/build-state.md`:
- Phase 4 status → `complete (pending approval)`
- Set next phase file → `references/phases/PHASE_5_BUILD.md`
- Log module list and agent list for Phase 5 tracking

## Gate: User Approval Required

Before requesting approval, write:
- "Proposal saved to: [path]"
- "Modules proposed: [count] foundation, [count] shared, [count] specialized"
- "Addenda proposed: [count]"
- "Agents proposed: [count]"
- "Blocking gaps: [list or 'none']"

**STOP. Get explicit user approval before building.**

After approval, update build-state.md: Phase 4 status → `complete`.

---

## After This Phase

**STOP. Do not continue to Phase 5 in this session.**

Phase 5 is the longest phase and the highest risk for context compaction. Starting Phase 5 with a full context window is critical — the metaprompting transformation rules must be fresh when writing modules, not buried under thousands of tokens of prior conversation.

Tell the user:

> "Phase 4 is complete. **Start a new conversation** before Phase 5 (Build). Phase 5 needs a fresh context window — it's the longest phase and the metaprompting instructions must be fully loaded when writing modules. In the new session, invoke the building-context-libraries skill and it will resume from build-state.md."

Do not begin Phase 5 even if the user asks to continue. Explain that module quality degrades significantly when Phase 5 runs in a compacted context.
