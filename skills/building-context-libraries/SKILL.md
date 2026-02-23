---
name: building-context-libraries
description: Builds AI context libraries from organizational source documents. Creates modular knowledge bases that give domain agents organizational context. Use when building a context library, creating domain agent modules, or transforming organizational documents into LLM-optimized context.
---

# Building Context Libraries

Build structured context libraries that encode organizational knowledge for AI agents.

<purpose>
Claude defaults to copying content from sources — restating facts in cleaned-up form feels
productive but produces modules useless as agent context. This skill exists because context
libraries must contain metaprompting (instructions that change how agents behave), not content
(facts agents can parrot back). The skill enforces transformation at every phase, with
verification that output would actually change agent behavior if loaded into a system prompt.
</purpose>

## Core Purpose

**You are creating prompts for LLM agents, not documentation for humans.**

### Content vs. Context vs. Metaprompting

Source documents contain **content** — raw facts. Modules must deliver **context** and **metaprompting**:

| Level | What It Is | Example |
|-------|-----------|---------|
| **Content** (source) | Raw facts copied from documents | "We have three service tiers: Advisory, Implementation, and Managed" |
| **Context** (minimum) | Processed knowledge that shapes agent behavior | "Service tiers map to client maturity — Advisory for exploration, Implementation for committed adopters, Managed for ongoing support. The tier determines conversation framing, not just pricing." |
| **Metaprompting** (target) | Instructions that tell the agent how to think and act | "When recommending services, assess client AI maturity first. Never suggest Managed before the client has completed at least one Implementation engagement — it signals dependency, not partnership." |

**Modules should be metaprompting and context, not content.** The agent building this library defaults to copying content because it's easier than transformation. Resist this. Every section should answer: "How should an agent *behave* given this information?" — not just "What is the information?"

**The test:** If you pasted this module into an LLM's context, would it change how the agent behaves? Or would it just give the agent facts to parrot back?

**Raw source material is NOT a module.** Transcripts, interviews, and messy documents must be transformed into actionable agent instructions. If your output reads like the source input, you have not done your job.

---

## Critical Rules

**ALL CONTENT MUST BE VERIFIED.** Every fact in the library must trace to a source document. This is non-negotiable.

- **NEVER invent details** — Use exact names, dates, locations, and legal terms from sources.
- **NEVER fill gaps** — Missing information is a gap to report, not a blank to fill.
- **NEVER skip source documents** — Read every file in the source index.
- **When in doubt, leave it out** — Omitting true information is recoverable; including false information is not.
- **Convert time spans to dates** — "25 years of experience" becomes "Founded in 1999." Time spans become outdated; dates remain accurate.
- **TRANSFORM, DON'T TRANSCRIBE** — Extract meaning and create actionable guidance. Never copy verbatim quotes or speech patterns into modules.

**PROPOSED CONTENT:** During the build, mark inferences with `[PROPOSED]` for tracking. These markers are build-time artifacts — they are removed from finished modules before delivery, like verification logs. The finished module's language should make the epistemic status of each claim legible without markers.

**CONFLICT RESOLUTION:** When source documents contradict, surface the conflict to the user. Do not silently pick one version.

**CONVERGENCE AWARENESS:** When source documents describe the same underlying pattern differently, the convergence reveals something about the organization that neither document says alone. Explore intersections rather than filing information into the first plausible module. See [PHASE_3_ANALYZE.md](references/phases/PHASE_3_ANALYZE.md) for how this applies during analysis.

**SECOND-ORDER THINKING:** Tiering and agent derivation decisions have downstream consequences. If a piece of knowledge goes into foundation instead of shared, every agent sees it — including ones where it may cause confusion. If you derive agents by taxonomy instead of role, modules become fact sheets instead of behavioral guides. Trace the consequences of structural choices. See [PHASE_5_BUILD.md](references/phases/PHASE_5_BUILD.md) for how this applies during module writing.

**PREMATURE COMMITMENT CHECK:** Your first pass at agent derivation or content tiering may not be the best one. Before finalizing the proposal, check whether you defaulted to the first organizational structure that seemed reasonable or whether you considered alternatives.

---

## Reference Files

Read these before each phase and re-read after any context compaction:

1. [references/ARCHITECTURE.md](references/ARCHITECTURE.md) — Module design, content transformation, token management, stakes classification
2. [references/TEMPLATES.md](references/TEMPLATES.md) — Templates for source index, synthesis, modules, agents, proposal, build state
3. [references/VALIDATION.md](references/VALIDATION.md) — Phase-by-phase validation checklists

---

## Build Process Overview

The build runs in 7 phases across multiple sessions. Each phase has a dedicated instruction file in `references/phases/` that contains everything needed for that phase.

| Phase | Name | Instruction File | Description |
|-------|------|------------------|-------------|
| 1 | Index | [PHASE_1_INDEX.md](references/phases/PHASE_1_INDEX.md) | Inventory and classify all source documents |
| 2 | Synthesize | [PHASE_2_SYNTHESIZE.md](references/phases/PHASE_2_SYNTHESIZE.md) | Transform messy sources into clean working documents |
| 3 | Analyze | [PHASE_3_ANALYZE.md](references/phases/PHASE_3_ANALYZE.md) | Identify work patterns, derive agents, tier content |
| 4 | Propose | [PHASE_4_PROPOSE.md](references/phases/PHASE_4_PROPOSE.md) | Design module structure and agent-module mapping |
| 5 | Build | [PHASE_5_BUILD.md](references/phases/PHASE_5_BUILD.md) | Write modules with write-time source verification |
| 6-7 | Agents & Validate | [PHASE_6_7_AGENTS_VALIDATE.md](references/phases/PHASE_6_7_AGENTS_VALIDATE.md) | Create agent definitions and validate library |

**Before starting any phase:** Read the phase instruction file. It contains all rules, procedures, and gates for that phase.

---

## Session Groupings

The build is designed to survive context compaction by splitting work across sessions:

| Session | Phases | Why Together |
|---------|--------|-------------|
| A | 1 (Index) + 2 (Synthesize) | Short phases, naturally sequential, low compaction risk |
| B | 3 (Analyze) + 4 (Propose) | Analysis feeds directly into proposal, moderate length |
| C | 5 (Build) | Longest phase, highest risk — one module at a time with re-read protocol |
| D | 6-7 (Agents + Validate) | Short phases, use completed modules as input |

Sessions A and B may combine if compaction hasn't occurred. **The boundary between B and C is mandatory** — always start a new session before Phase 5. Phase 5 needs a full context window for the metaprompting transformation rules to work.

---

## Starting a New Build

1. **Ask the user:**
   - "Where are your source documents?" → `SOURCE_PATH`
   - "Where should I create the context library?" (default: `./context-library/`) → `OUTPUT_PATH`
   - "What domain agents will use this library?" → `AGENTS`

2. **Read the Phase 1 instruction file:** [references/phases/PHASE_1_INDEX.md](references/phases/PHASE_1_INDEX.md)

3. **Begin Phase 1.**

---

## Resuming a Build

If `<OUTPUT_PATH>/build-state.md` exists:

1. **Read `build-state.md` first** — it tells you the current phase, what's done, and what's next.
2. **Read the phase instruction file** it points to.
3. **Continue from where work left off.**

If `build-state.md` does not exist but `source-index.md` does:

1. **Read `source-index.md`** — check its status field and reading checklist.
2. **Determine the current phase** from the index status.
3. **Read the appropriate phase instruction file.**
4. **Create `build-state.md`** to track progress going forward.

---

<failed_attempts>
## What DOESN'T Work

- **Transcribing instead of synthesizing:** Copying quotes with "they said X" produces content useless to LLM agents. Extract the *meaning*, state it directly.
- **Filling gaps with plausible content:** A thin module with verified facts is better than a rich module with hallucinations.
- **Writing from memory:** Re-read sources in the same turn you write modules. Memory blurs; sources don't.
- **Proposing content in Phase 4:** The proposal describes structure, not organizational information.
- **Compressing to hit token targets:** Include all useful verified content. Sparse modules lack context.
- **Skipping source index updates:** Update the index after every file read, synthesis, and status change.
- **Preserving time spans:** Convert to dates. "25 years of experience" becomes "since 1999."
- **Batching syntheses:** Complete each synthesis and update the index before starting the next.
- **Copying content instead of creating context:** Modules are metaprompts, not fact sheets. "The organization has 50 employees" is content. "When clients ask about team size, frame capacity in terms of expertise areas, not headcount" is context. Write the second kind.
</failed_attempts>

---

## Checkpoints

| After Phase | What User Reviews |
|-------------|-------------------|
| 1. Index | File list, classifications, conflicts, gaps |
| 2. Synthesize | Each synthesis document |
| 4. Propose | Module structure, agent mapping |
| 6-7. Validate | Complete library |

**Do not proceed without explicit approval.**
