---
name: building-context-libraries
description: Builds AI context libraries from organizational source documents. Creates modular knowledge bases that give domain agents organizational context. Use when building a context library, creating domain agent modules, or transforming organizational documents into LLM-optimized context.
---

# Building Context Libraries

Build structured context libraries that encode organizational knowledge for AI agents.

## Core Purpose

**You are creating prompts for LLM agents, not documentation for humans.**

### Content vs. Context vs. Metaprompting

Source documents contain **content** — raw facts. Modules must deliver **context** and **metaprompting**:

| Level | What It Is | Example |
|-------|-----------|---------|
| **Content** (source) | Raw facts copied from documents | "We were founded in 2016, rebranded in 2023" |
| **Context** (minimum) | Processed knowledge that shapes agent behavior | "When writing about the organization's history, emphasize the AI-native transformation starting June 2023, not the original founding. The rebranding reflects a strategic shift, not just a name change." |
| **Metaprompting** (target) | Instructions that tell the agent how to think and act | "If a client asks about your AI experience, frame it as having been AI-native since inception — not as a recent adoption." |

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

**PROPOSED CONTENT:** If the user approves including inferences, mark them with `[PROPOSED]`. All other content is verified by default.

**CONFLICT RESOLUTION:** When source documents contradict, surface the conflict to the user. Do not silently pick one version.

---

## Reference Files

Read these as needed during the build:

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

## What DOESN'T Work

- **Transcribing instead of synthesizing:** Copying quotes with "they said X" produces content useless to LLM agents. Extract the *meaning*, state it directly.
- **Filling gaps with plausible content:** A thin module with verified facts is better than a rich module with hallucinations.
- **Writing from memory:** Re-read sources in the same turn you write modules. Memory blurs; sources don't.
- **Proposing content in Phase 4:** The proposal describes structure, not organizational information.
- **Compressing to hit token targets:** Include all useful verified content. Sparse modules lack context.
- **Skipping source index updates:** Update the index after every file read, synthesis, and status change.
- **Preserving time spans:** Convert to dates. "25 years of experience" becomes "since 1999."
- **Batching syntheses:** Complete each synthesis and update the index before starting the next.
- **Copying content instead of creating context:** Modules are metaprompts, not fact sheets. "Founded in 2016" is content. "Frame the founding story around the 2023 AI-native transformation" is context. Write the second kind.

---

## Checkpoints

| After Phase | What User Reviews |
|-------------|-------------------|
| 1. Index | File list, classifications, conflicts, gaps |
| 2. Synthesize | Each synthesis document |
| 4. Propose | Module structure, agent mapping |
| 6-7. Validate | Complete library |

**Do not proceed without explicit approval.**
