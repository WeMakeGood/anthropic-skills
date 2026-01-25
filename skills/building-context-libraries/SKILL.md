---
name: building-context-libraries
description: Builds AI context libraries from organizational source documents. Creates modular knowledge bases that give domain agents organizational context. Use when building a context library, creating domain agent modules, or transforming organizational documents into LLM-optimized context.
---

# Building Context Libraries

Build structured context libraries that encode organizational knowledge for AI agents.

## Critical Rules

**GROUNDING (CRITICAL - READ CAREFULLY):** Every fact in the library MUST trace to a specific source document. But grounding means the INFORMATION is sourced, not that you copy the source text.
- **NEVER invent details** — Use exact names, dates, locations, and legal terms from sources. Do not substitute similar-sounding alternatives.
- **NEVER fill gaps with plausible content** — Missing information is a gap to report, not a blank to fill creatively.
- **NEVER mark invented content as [CONFIRMED]** — If you cannot point to the source document where you learned this fact, it is NOT confirmed.
- **NEVER copy verbatim quotes from transcripts or interviews** — Synthesize the information into clear prose. Conversational speech is raw material, not finished content.
- **When in doubt, leave it out** — Omitting true information is recoverable; including false information damages trust permanently.

**CONFLICT RESOLUTION:** When source documents contradict each other, surface the conflict to the user. Do not silently resolve by picking one version.

**EPISTEMIC MARKERS:** Unmarked content is confirmed by default. Only mark exceptions:
- **Unmarked** — Verified from working sources. This is the default; no marker needed.
- `[PROPOSED]` — Logical inference, not explicitly stated in sources. User should verify.
- `[HISTORICAL]` — Explicitly superseded by newer documents.

**PROFESSIONAL OBJECTIVITY:** If source documents have significant gaps, inconsistencies, or quality issues, report this directly. The library's value depends on accurate representation, not completeness theater.

**FLEXIBILITY OVER RIGIDITY:** Capture principles and decision-making frameworks, not locked-in methodologies. If a source document describes a specific approach (e.g., "we use Claude"), extract the underlying principle (e.g., "our evaluation criteria for AI tools") rather than encoding the specific choice. The library should enable future decisions, not constrain them.

**NATURAL PROSE FOR EXTERNAL-FACING AGENTS:** Agents that produce marketing, website copy, case studies, or other external-facing content must include writing style guardrails to avoid AI-detectable patterns. See [references/TEMPLATES.md](references/TEMPLATES.md) for the Natural Prose section.

## Before Starting

Ask the user:

1. **"Where are your source documents?"**
   - Could be a folder path, multiple paths, or files in current directory
   - Accept whatever structure they have

2. **"Where should I create the context library?"**
   - Default suggestion: `./context-library/`
   - User may want it elsewhere

3. **"What domain agents will use this library?"**
   - Get list of roles/agents, OR
   - Ask if there's a requirements document

Store these as:
- `SOURCE_PATH` - where to read from
- `OUTPUT_PATH` - where to write library
- `AGENTS` - list of domain agents needed

---

## Build Process Overview

The build process creates persistent artifacts at each phase, enabling:
- **Session breaks** — Stop and resume in a new session
- **Compaction** — New sessions read artifacts, not original sources
- **Auditability** — User can review and correct at each checkpoint

**Phases:**
1. **Index** — Analyze and classify all source documents
2. **Synthesize** — Transform complex sources into clean working documents
3. **Propose** — Design module structure based on ready sources
4. **Build** — Create modules from indexed sources
5. **Validate** — Verify and get final approval

**Key artifacts:**
- `source-index.md` — Master list of all sources and their status
- `synthesis/*.md` — Cleaned versions of complex source documents
- `proposal.md` — Structural plan for the library
- `modules/` — The actual context library content
- `agents/` — Agent definitions

---

## Phase 1: Index Sources

**Create the source index — the master manifest for the entire build.**

First, run the inventory script to get file listings:

```bash
python3 <skill_dir>/scripts/analyze_sources.py <SOURCE_PATH>
```

Then create `<OUTPUT_PATH>/source-index.md`:

```markdown
# Source Index

**Generated:** [date]
**Source path:** [SOURCE_PATH]
**Status:** [indexing | synthesizing | ready | building | complete]

## Source Files

| File | Type | Status | Working Source | Notes |
|------|------|--------|----------------|-------|
| [path] | [type] | [status] | [path or "original"] | [notes] |

## Conflicts Identified

- [Conflict description]: [File A] vs [File B]

## Gaps Identified

- [Gap description]
```

**For each source file, determine:**

1. **Type** — How should this document be handled?
   - `strategy` — Polished positioning, decisions (use directly)
   - `operational` — Current processes, structures (use directly)
   - `transcript` — Conversational, needs synthesis
   - `interview` — Q&A format, needs synthesis
   - `notes` — Meeting notes, may need synthesis
   - `reference` — Supporting material (use directly)

2. **Status** — What state is this source in?
   - `ready` — Can be used directly for module building
   - `needs-synthesis` — Must be synthesized before use
   - `synthesized` — Synthesis complete, use the synthesis file
   - `skip` — Not needed for this library

3. **Working Source** — What file should module building use?
   - For `ready` files: `original`
   - For `synthesized` files: path to synthesis file

**STOP. Get user approval on source index before synthesizing.**

The user may:
- Reclassify files (e.g., mark something as `skip`)
- Identify additional conflicts or gaps
- Approve to proceed

---

## Phase 2: Synthesize Complex Sources

**For each file marked `needs-synthesis`, create a clean working document.**

Create synthesis files in `<OUTPUT_PATH>/synthesis/`:
- Name: `[original-filename]-synthesis.md`
- One synthesis per source file

**What synthesis does:**
- Extracts facts, decisions, and principles from messy source material
- Removes speech artifacts, filler words, incomplete thoughts
- Organizes information by topic
- Preserves exact names, dates, figures — no invention

**What synthesis does NOT do:**
- Invent information not in the source
- Interpret ambiguous statements (flag these instead)
- Combine multiple sources (each synthesis is one source)

**Synthesis format:**

```markdown
# Synthesis: [Original Filename]

**Source:** [path to original]
**Generated:** [date]
**Status:** [draft | user-approved]

---

## [Topic Area]

[Synthesized content — clear prose stating facts from the source]

## [Topic Area]

[Synthesized content]

---

## Flagged for Clarification

- [Ambiguous statement that needs user input]
- [Unclear reference that needs verification]

---

**Awaiting user review.**
```

**After creating each synthesis:**
1. Update the source index: change status to `synthesized`, set working source to synthesis path
2. Present to user for review

**STOP. Get user approval on ALL syntheses before proposing structure.**

The user may:
- Correct errors in syntheses
- Clarify flagged items
- Approve to proceed

**Session break point:** After all syntheses are approved, the source index and synthesis files contain everything needed to continue in a new session. A new session can read these artifacts instead of the original sources.

---

## Phase 3: Propose Structure

**Design the module structure based on ready sources.**

Read from the source index to identify working sources (either originals marked `ready` or synthesis files).

Create `<OUTPUT_PATH>/proposal.md` describing what you will build. **This is a structural plan, not a draft of content.**

**What the proposal IS:**
- A list of proposed modules with names, purposes, and estimated tokens
- Module-to-agent mapping showing which agents load which modules
- Identified conflicts and proposed resolutions
- Information gaps that may affect module quality

**What the proposal is NOT:**
- Pre-written module content (that's Phase 4)
- An "Organization Summary" or similar content preview
- Detailed text that will appear in modules

**Proposal sections:**

1. **Proposed Modules** — For each module:
   - Name and ID (e.g., F1, S3, D2)
   - One-sentence purpose
   - Which working sources inform it
   - Estimated token count
   - Which agents will load it

2. **Agent-Module Mapping** — Table showing each agent and its module set with total token estimate. Most agents should be 12,000-18,000 tokens.

3. **Content Conflicts** (REQUIRED):
   - List conflicts between source documents
   - For each: what changed, which is authoritative, how you'll handle it
   - Ask user to confirm resolutions

4. **Information Gaps** (REQUIRED):
   - **Blocking**: Cannot build without this
   - **Limiting**: Reduces quality but not blocking
   - **Enhancing**: Nice to have

5. **Questions for Approval** — Specific decisions you need confirmed

**Do not minimize gaps to make the proposal look better.** If sources are insufficient, say so.

**STOP. Get explicit user approval before building. Do not proceed on implied or partial approval.**

---

## Phase 4: Build Modules

**Create modules using ONLY the indexed working sources.**

After approval, create folder structure:
```
<OUTPUT_PATH>/
├── source-index.md
├── synthesis/
├── proposal.md
├── modules/
│   ├── foundation/
│   ├── shared/
│   └── specialized/
└── agents/
```

**CRITICAL: Build modules SEQUENTIALLY, not in parallel.**

Build modules ONE AT A TIME in this order:
1. **Foundation modules first** → `modules/foundation/`
2. **Shared modules next** → `modules/shared/`
3. **Specialized modules last** → `modules/specialized/`

**For EACH module, follow this sequence:**

1. **Before writing:** Consult the source index. Identify which working sources (originals or syntheses) contain relevant information. Re-read those specific files.

2. **While writing:** For every fact you include:
   - Is this fact in one of the working sources listed in the index?
   - Can you point to where in that source?
   - If NO to either → do not include it, or mark as `[PROPOSED]`

   **Write for LLM consumption.** These modules are prompts, not documentation:
   - Be direct — state facts, don't introduce them
   - Front-load key information
   - Use consistent terminology throughout
   - Encode decision criteria as "If X, do Y" patterns
   - Don't explain concepts Claude already knows

3. **After writing:** Verify the module against working sources:
   - Check each `[CONFIRMED]` statement
   - If a statement isn't supported by working sources, change to `[PROPOSED]` or remove it

**Do not proceed to the next module until the current one is verified.**

Use formats from [references/TEMPLATES.md](references/TEMPLATES.md).

Key rules:
- Single source of truth: each fact in ONE module only
- Explicit references: `See [Module Name]` for cross-module info
- Mark exceptions only: `[PROPOSED]` or `[HISTORICAL]` — unmarked content is confirmed

---

## Phase 5: Create Agent Definitions

For each agent in `AGENTS`, create definition in `<OUTPUT_PATH>/agents/`:
- List required modules
- Estimate total tokens
- Include behavioral guidance
- Define verification behaviors based on content stakes
- Specify professional objectivity guidelines (when to challenge, verify, flag)
- **For agents producing external-facing content:** Include Natural Prose guardrails (banned vocabulary, banned structures, required behaviors)

---

## Phase 6: Validate

Run validation scripts from this skill's `scripts/` directory:
```bash
python3 <skill_dir>/scripts/validate_library.py <OUTPUT_PATH>/modules
python3 <skill_dir>/scripts/count_tokens.py <OUTPUT_PATH>/modules <OUTPUT_PATH>/agents
```

Check for:
- Broken cross-references
- Duplicated information
- Token budget overruns (default: 20K per agent)
- Missing required content
- **All [CONFIRMED] facts verified against working sources**

Update source index status to `complete`.

**STOP. Get user approval on final library.**

---

## Key Principles

**Modules are prompts, not documentation**: You're writing context for LLMs, not docs for humans. Be direct and declarative. Use "If X, then Y" patterns. Front-load key information. Cut preambles and transitions. Every token costs money — make them count.

**Richness over minimalism**: Agents need enough context to work effectively. Most modules should be 2,000-4,000 tokens. BUT: Richness means *sourced* content, not invented content. A thin module with verified facts is better than a rich module with hallucinations. If sources don't support 2,000 tokens of content, report the gap rather than filling it creatively.

**Don't explain what Claude knows**: Skip explanations of general concepts (what AI is, how nonprofits work). But DO include organization-specific application of those concepts.

**Reference, don't repeat**: If info exists in Module A, Module B says "See [Module A]" - never duplicates.

**Unmarked = confirmed**: All unmarked content must be verifiable in working sources. Only use markers for exceptions: `[PROPOSED]` for inferences, `[HISTORICAL]` for superseded info. If you can't verify a fact, either mark it `[PROPOSED]` or remove it.

**Use the token budget**: The 20K guideline exists to be used, not avoided. An agent at 8,000 tokens is probably missing useful context. Target 12,000-18,000 tokens for most agents. Only go below 10,000 if the agent's role is genuinely narrow.

**Principles over prescriptions**: Extract decision-making frameworks, not specific methodologies. A module should help agents make good decisions in new situations, not lock them into documented past choices. Ask: "Does this content enable flexibility or constrain it?"

---

## When to Stop and Ask

**REQUIRED:** Get explicit user approval at these checkpoints:

| After Phase | Checkpoint | What User Reviews |
|-------------|------------|-------------------|
| 1. Index | Source index approved | File classifications, identified conflicts/gaps |
| 2. Synthesize | All syntheses approved | Each synthesis document |
| 3. Propose | Proposal approved | Module structure, agent mapping, gap handling |
| 6. Validate | Final library approved | Complete library with validation report |

**Do not proceed past a checkpoint without explicit approval.** "Sounds good" or similar is sufficient; silence or topic change is not.

**Session breaks:** After Phase 1 or Phase 2, the source index (and syntheses) contain everything needed to continue in a new session. Update the index status field to track progress:
- `indexing` — Phase 1 in progress
- `synthesizing` — Phase 2 in progress
- `ready` — Phases 1-2 complete, ready for proposal
- `building` — Phase 4 in progress
- `complete` — All phases done

---

## Resuming a Previous Session

If the user has an existing source index:

1. Read `<OUTPUT_PATH>/source-index.md`
2. Check the status field to determine current phase
3. Read any existing synthesis files
4. Continue from the appropriate phase

Do NOT re-read original source documents if syntheses exist — use the synthesis files as your working sources.

---

## References

- [references/ARCHITECTURE.md](references/ARCHITECTURE.md) - Module design principles and content stakes classification
- [references/TEMPLATES.md](references/TEMPLATES.md) - Module and agent formats (includes verification/objectivity guidance)
- [references/VALIDATION.md](references/VALIDATION.md) - Validation checklist
