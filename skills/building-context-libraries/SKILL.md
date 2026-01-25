---
name: building-context-libraries
description: Builds AI context libraries from organizational source documents. Creates modular knowledge bases that give domain agents organizational context. Use when building a context library, creating domain agent modules, or transforming organizational documents into LLM-optimized context.
---

# Building Context Libraries

Build structured context libraries that encode organizational knowledge for AI agents.

## Critical Rules

**ALL CONTENT MUST BE VERIFIED.** Every fact in the library must trace to a source document. This is non-negotiable.

- **NEVER invent details** — Use exact names, dates, locations, and legal terms from sources.
- **NEVER fill gaps** — Missing information is a gap to report, not a blank to fill.
- **NEVER skip source documents** — Read every file in the source index.
- **When in doubt, leave it out** — Omitting true information is recoverable; including false information is not.

**PROPOSED CONTENT:** If the user approves including inferences or recommendations, mark them with `[PROPOSED]`. This is the only marker needed — all other content is verified by default.

**CONFLICT RESOLUTION:** When source documents contradict, surface the conflict to the user. Do not silently pick one version.

**SYNTHESIS, NOT TRANSCRIPTION:** Extract and synthesize information from sources. Modules contain organizational knowledge for LLM agents, not reference material for humans.

---

## Source Type Handling

Different sources require different processing. The goal is always: **synthesized knowledge an LLM can act on.**

| Source Type | Contains | Extract | Do NOT Include |
|-------------|----------|---------|----------------|
| **Strategy docs** | Decisions, positioning | Frameworks, principles, positioning statements | — (use directly) |
| **Transcripts** | Conversational speech | Facts and decisions expressed | Verbatim quotes, filler words, speech patterns |
| **Interview quotes** | Verbatim statements | The insights and meaning | The quotes themselves |
| **Case studies** | Client examples | Methodology patterns, anonymized learnings | Client names, specific metrics, testimonials |
| **Bios/profiles** | Personnel info | Names, roles, expertise areas | Personal details irrelevant to agents |
| **Competitive intel** | Market analysis | Differentiators, positioning frameworks | Competitor-specific details that may change |
| **Financial docs** | Numbers, metrics | Verified figures marked HIGH-STAKES | Unverified or dated numbers |
| **Process docs** | Procedures | Decision criteria, "If X, do Y" patterns | Step-by-step procedures (agents adapt) |

**Key principle:** A quote in a source document is evidence of what someone said — it's not content to copy into a module. Synthesize what the quote *means* for how agents should behave.

**Example transformation:**

Source (interview):
> "We really try to meet clients where they are. If they're just starting with AI, we don't overwhelm them with technical stuff. We focus on quick wins first."

Module content:
```
Client engagement adapts to AI maturity:
- Early-stage clients: Focus on quick wins, minimize technical complexity
- Mature clients: Deeper technical integration appropriate
```

The quote is evidence; the module contains actionable guidance.

---

## Before Starting

Ask the user:

1. **"Where are your source documents?"**
2. **"Where should I create the context library?"** (default: `./context-library/`)
3. **"What domain agents will use this library?"**

Store these as `SOURCE_PATH`, `OUTPUT_PATH`, and `AGENTS`.

---

## Build Process

### Phase 1: Create Source Index

**Run the indexing script to create the source manifest:**

```bash
python3 <skill_dir>/scripts/create_source_index.py <SOURCE_PATH> <OUTPUT_PATH>
```

This creates `<OUTPUT_PATH>/source-index.md` with:
- Every source file listed (the script finds ALL files — none are skipped)
- Automatic type classification (strategy, transcript, operational, etc.)
- Initial status (ready or needs-synthesis)
- A reading checklist you must complete

**YOU MUST READ EVERY FILE IN THE INDEX.** The script has already determined which files exist. Do not skip files or decide they are "unimportant."

After reading all files, update the index with:
- Conflicts identified between documents
- Information gaps discovered
- Any reclassifications needed

**STOP. Get user approval on source index before proceeding.**

---

### Phase 2: Synthesize Complex Sources

For each file marked `needs-synthesis`, create a clean working document.

Create synthesis files in `<OUTPUT_PATH>/synthesis/`:

```markdown
# Synthesis: [Original Filename]

**Source:** [path to original]
**Status:** draft

---

## [Topic Area]

[Clear prose stating facts extracted from the source]

## [Topic Area]

[Additional content organized by topic]

---

## Flagged for Clarification

- [Ambiguous statement needing user input]

---
```

**Synthesis rules:**
- One synthesis per source file
- Extract facts, decisions, principles — not verbatim quotes
- Preserve exact names, dates, figures
- Flag ambiguities — don't interpret them
- Update source index when complete (status → `synthesized`)

**STOP. Get user approval on ALL syntheses before proposing structure.**

**Session break point:** After Phase 2, the source index and syntheses can be used to resume in a new session.

---

### Phase 3: Propose Structure

Create `<OUTPUT_PATH>/proposal.md` — a structural plan, not content.

**Proposal includes:**
1. Proposed modules (name, purpose, source references, estimated tokens)
2. Agent-module mapping (which agents load which modules, total tokens per agent)
3. Content conflicts and proposed resolutions
4. Information gaps (blocking / limiting / enhancing)
5. Questions requiring user decision

**Proposal does NOT include:**
- Pre-written module content
- Organization summaries
- Draft text

**Target 12,000-18,000 tokens per agent.** If sources don't support this, report the gap.

**STOP. Get explicit user approval before building.**

---

### Phase 4: Build Modules

Create folder structure:
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

**Build modules SEQUENTIALLY:**
1. Foundation modules first
2. Shared modules next
3. Specialized modules last

**For each module:**

1. **Before writing:** Re-read the relevant working sources (originals or syntheses)

2. **While writing:** Every fact must be in a working source. If you cannot point to where a fact appears, do not include it (or mark `[PROPOSED]` if user has approved inferences).

3. **After writing:** Verify against sources before proceeding to the next module.

**Writing for LLM consumption:**
- Be direct — state facts, don't introduce them
- Front-load key information
- Use consistent terminology
- Encode decision criteria as "If X, do Y" patterns
- Don't explain concepts Claude already knows

**Key rules:**
- Single source of truth: each fact in ONE module only
- Explicit cross-references: `See [Module Name]` for related info
- No duplication

---

### Phase 5: Create Agent Definitions

For each agent, create a definition in `<OUTPUT_PATH>/agents/`:
- List required modules
- Estimate total tokens
- Include behavioral guidance
- Define verification behaviors for high-stakes content
- For external-facing agents: Include Natural Prose guardrails

---

### Phase 6: Validate

Run validation scripts:
```bash
python3 <skill_dir>/scripts/validate_library.py <OUTPUT_PATH>/modules
python3 <skill_dir>/scripts/count_tokens.py <OUTPUT_PATH>/modules <OUTPUT_PATH>/agents
```

Check for:
- Broken cross-references
- Duplicated information
- Token budget issues
- Missing required content

Update source index status to `complete`.

**STOP. Get user approval on final library.**

---

## Key Principles

**Modules are prompts, not documentation.** Write for LLMs: direct, declarative, no preambles.

**Verified content only.** Every fact must trace to a source. Thin modules with verified facts beat rich modules with hallucinations.

**Reference, don't repeat.** Each fact exists in one module only.

**Use the token budget.** Target 12,000-18,000 tokens per agent. Under 10,000 usually means missing context.

**Principles over prescriptions.** Extract decision frameworks, not locked-in methodologies.

---

## Checkpoints

| After Phase | What User Reviews |
|-------------|-------------------|
| 1. Index | File list, classifications, conflicts, gaps |
| 2. Synthesize | Each synthesis document |
| 3. Propose | Module structure, agent mapping |
| 6. Validate | Complete library |

**Do not proceed without explicit approval.**

---

## Resuming a Previous Session

If `<OUTPUT_PATH>/source-index.md` exists:
1. Read the source index
2. Check the status field
3. Read any existing syntheses
4. Continue from the appropriate phase

Use synthesis files as working sources — do not re-read original transcripts.

---

## References

- [references/ARCHITECTURE.md](references/ARCHITECTURE.md) - Module design, content stakes
- [references/TEMPLATES.md](references/TEMPLATES.md) - Templates for all artifacts
- [references/VALIDATION.md](references/VALIDATION.md) - Validation checklist
