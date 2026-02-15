# Phase 3: Analyze Sources

> **CRITICAL RULES — Read these first, even if you read nothing else:**
> - NEVER invent details. Every fact must come from a working source you actually read.
> - NEVER fill gaps with plausible information. Gaps are gaps — report them.
> - Re-read working sources before analyzing. Do not work from memory.
> - Every agent you derive must be justified by work patterns found in sources.
> - Content tiering must be based on how agents USE information, not taxonomy.

---

## What This Phase Does

Analyze the working sources (originals marked `ready` + synthesis files) to identify:
1. What kinds of work agents will do with this knowledge
2. Which agents are needed and what they need to know
3. How information should be tiered (foundation/shared/specialized)
4. Where information consolidates or conflicts

This phase produces an analysis document that feeds directly into the Phase 4 proposal.

## Before You Start

1. **Read `<OUTPUT_PATH>/build-state.md`** — confirm Phase 2 is complete.
2. **Read `<OUTPUT_PATH>/source-index.md`** — this tells you which working sources to use.
3. **For each file:** use the Working Source column. `ready` files → read originals. `synthesized` files → read the synthesis file path.

---

## Step 1: Identify Work Patterns

Read through all working sources and identify the types of work agents will perform with this knowledge. Look for:

- **Decision types** — What decisions would agents need to make? (client qualification, content voice, pricing guidance, program recommendations)
- **Output types** — What would agents produce? (proposals, content, reports, responses)
- **Knowledge domains** — What subject areas emerge? (organizational identity, services, methodology, programs)

Create `<OUTPUT_PATH>/analysis.md` and document:

```markdown
# Source Analysis

**Generated:** YYYY-MM-DD

## Work Patterns Identified

### [Pattern Name]
- **What agents do:** [description]
- **Knowledge required:** [what they need to know]
- **Sources informing this:** [list of working sources]

### [Pattern Name]
...
```

## Step 2: Derive Agents

Based on work patterns, identify which agents are needed. Each agent should represent a distinct role, not just a knowledge domain.

**Good agent derivation (role-based):**
- "Content Writer" — produces external communications in the organization's voice
- "Program Advisor" — recommends programs based on client needs
- "Proposal Developer" — creates tailored service proposals

**Bad agent derivation (taxonomy-based):**
- "Identity Agent" — just knows about the org (what would it *do*?)
- "Services Agent" — just knows services (too generic)

For each proposed agent, document:
- Role description (what it does, not what it knows)
- Work patterns it serves
- Knowledge domains it needs
- Which working sources contain relevant content

## Step 3: Tier Content

Classify knowledge into tiers based on how agents use it:

### Foundation (all or most agents need this)
- Organizational identity, values, positioning
- Communication standards and voice
- Ethical guidelines and constraints

### Shared (multiple agents, not all)
- Client engagement methodology
- Service descriptions
- Content standards

### Specialized (specific agents only)
- Program-specific details
- Domain-specific processes
- Role-specific knowledge

**The tiering test:** For each piece of knowledge, ask: "How many agents need this to do their job?" If most → foundation. If several → shared. If one or two → specialized.

## Step 3.5: Identify Addenda Candidates

As you tier content, some source material won't fit into modules — not because it's unimportant, but because it's **data rather than behavioral guidance**. This content belongs in addenda (see ARCHITECTURE.md "Addenda" section).

**The classification test:**
- Does the agent need this to *decide how to behave*? → module
- Does the agent need to *look up specific data*? → addendum
- Would this change when processes are redesigned? → module
- Would this change when the business evolves (prices, people, offerings)? → addendum

**Common addenda candidates:**
- Pricing tables, rate cards, fee structures
- Biographical details and career timelines
- Service catalogs and current offerings
- Team rosters and organizational charts

Document addenda candidates in analysis.md:

```markdown
## Addenda Candidates

### [Addendum Name]
- **Content:** [what data this would contain]
- **Sources:** [which working sources contain this data]
- **Referenced by:** [which modules would point to this]
- **Update frequency:** [how often this data changes]
```

---

## Step 4: Consolidation Test

Check for information that should consolidate:
- Same fact stated differently across sources → pick the authoritative version
- Related facts scattered across sources → identify which module will unify them
- Conflicting information → add to conflicts list for user resolution

## Step 5: Update Build State

Update `<OUTPUT_PATH>/build-state.md`:
- Phase 3 status → `complete`
- Note key findings: agent count, module count estimates, blocking gaps
- Set next phase file → `references/phases/PHASE_4_PROPOSE.md`

---

## No Gate — Continue to Phase 4

Phase 3 analysis feeds directly into Phase 4 proposal. No separate user approval needed — the user reviews the analysis as part of the proposal.

---

## After This Phase

Read [PHASE_4_PROPOSE.md](PHASE_4_PROPOSE.md) to create the structure proposal.

**Session break point:** After Phase 3, analysis.md and build-state.md can be used to resume in a new session.
