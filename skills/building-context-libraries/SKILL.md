---
name: building-context-libraries
description: Builds AI context libraries from organizational source documents. Creates modular knowledge bases that give domain agents organizational context. Use when building a context library, creating domain agent modules, or transforming organizational documents into LLM-optimized context.
---

# Building Context Libraries

Build structured context libraries that encode organizational knowledge for AI agents.

## Core Purpose

**You are creating prompts for LLM agents, not documentation for humans.**

Context modules must be:
- **Actionable** — An agent can use this to make decisions or produce output
- **Direct** — State facts and principles, not quotes or transcriptions
- **Clean** — No filler words, speech artifacts, incomplete thoughts, or conversational rambling

**The test:** If you pasted this module into an LLM's context, would it help the agent work effectively? Or would the agent be confused by messy transcription artifacts, verbatim quotes, and unprocessed source material?

**Raw source material is NOT a module.** Transcripts, interviews, and messy documents must be transformed into clean, structured knowledge. If your output reads like the source input, you have not done your job.

---

## Critical Rules

**ALL CONTENT MUST BE VERIFIED.** Every fact in the library must trace to a source document. This is non-negotiable.

- **NEVER invent details** — Use exact names, dates, locations, and legal terms from sources.
- **NEVER fill gaps** — Missing information is a gap to report, not a blank to fill.
- **NEVER skip source documents** — Read every file in the source index.
- **When in doubt, leave it out** — Omitting true information is recoverable; including false information is not.
- **Convert time spans to dates** — "25 years of experience" becomes "Founded in 1999" or "Working in industry since 1999." Time spans become outdated; dates remain accurate.

**PROPOSED CONTENT:** If the user approves including inferences or recommendations, mark them with `[PROPOSED]`. This is the only marker needed — all other content is verified by default.

**CONFLICT RESOLUTION:** When source documents contradict, surface the conflict to the user. Do not silently pick one version.

**TRANSFORM, DON'T TRANSCRIBE:** Your job is to extract meaning and create actionable guidance. Never copy verbatim quotes, speech patterns, or conversational text into modules. A quote is evidence that something is true — the module states what is true.

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

**FIRST: Read all reference files before doing anything else:**

1. [references/ARCHITECTURE.md](references/ARCHITECTURE.md) — Module design, content transformation, token management, stakes classification
2. [references/TEMPLATES.md](references/TEMPLATES.md) — Templates for source index, synthesis, modules, agents, proposal
3. [references/VALIDATION.md](references/VALIDATION.md) — Phase-by-phase validation checklists

**Do not proceed until you have read all three reference files.**

---

**THEN: Ask the user:**

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

This creates `<OUTPUT_PATH>/source-index.md` — your working checklist for the entire build.

**HOW TO USE THE INDEX:**

1. **Read the index first.** It lists every file you must process.

2. **Work through files in order.** For each file in the index:
   - Read the file
   - Update the index: mark it read, note any issues
   - Do NOT proceed to the next file until you've updated the index

3. **Update the index as you go.** The index has a "Reading Checklist" section:
   ```markdown
   ## Reading Checklist
   - [ ] 1. strategy-doc.md
   - [ ] 2. interview-transcript.md
   - [ ] 3. team-bios.md
   ```

   After reading each file, mark it complete:
   ```markdown
   - [x] 1. strategy-doc.md — read, ready to use
   - [x] 2. interview-transcript.md — read, needs synthesis
   - [ ] 3. team-bios.md
   ```

4. **Add notes as you discover them:**
   - Conflicts between documents → add to "Conflicts Identified" section
   - Missing information → add to "Gaps Identified" section
   - Reclassifications needed → update the file's Type/Status in the table

5. **The index is your source of truth.** When building modules later, you will reference this index to know which files to consult. If a file isn't marked as read in the index, you haven't processed it.

**DO NOT:**
- Skip files because they seem unimportant
- Read files without updating the index
- Proceed to Phase 2 until every file is marked read

**STOP. Get user approval on completed source index before proceeding.**

---

### Phase 2: Synthesize Complex Sources

The script marks files as `needs-synthesis` based on file type, but this is only a **preliminary classification**. You must evaluate each file before processing.

**EVALUATE BEFORE SYNTHESIZING:**

For each file marked `needs-synthesis` in the index:

1. **Read the file first**
2. **Decide if it actually needs synthesis:**
   - YES if: Contains filler words, speech artifacts, conversational rambling, verbatim quotes, unstructured content
   - NO if: Already clean, well-organized, directly usable by an LLM agent
3. **If NO synthesis needed:** Update the index (change status to `ready`, note "reviewed - already clean")
4. **If YES synthesis needed:** Proceed with synthesis below

**Also check for existing synthesis files:**
- If `<OUTPUT_PATH>/synthesis/[filename]-synthesis.md` exists, read it instead of re-synthesizing
- Update the index (status → `synthesized`, add working source path)

**HOW TO DO SYNTHESIS (only for files that actually need it):**

1. **For each file that genuinely needs synthesis:**
   a. Create synthesis file in `<OUTPUT_PATH>/synthesis/[filename]-synthesis.md`
   b. **Update the source index immediately:**
      - Change status from `needs-synthesis` to `synthesized`
      - Add the synthesis path to the "Working Source" column
   c. Present synthesis to user for review

2. **Do not batch syntheses** — complete and update index for each file before starting the next

**Synthesis file format:**

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

**CRITICAL: What synthesis IS and IS NOT:**

Synthesis IS:
- Extracting the *meaning* from messy source material
- Stating facts in clean, direct prose
- Organizing information by topic
- Creating content an LLM agent can act on

Synthesis is NOT:
- Copying quotes with "they said X"
- Preserving conversational structure
- Including filler words, false starts, or rambling
- Transcription with light editing

**Example — WRONG (transcription):**
```
John mentioned that "we've always tried to, you know, meet clients where they are"
and emphasized that the team believes in "starting with quick wins."
```

**Example — RIGHT (synthesis):**
```
Client Engagement Approach:
- Adapt to client's current state and capabilities
- Start with quick wins before complex implementations
```

The first example is useless to an LLM agent. The second is actionable guidance.

**After completing ALL syntheses:**
1. Update source index status to `ready`
2. Present completed index showing all syntheses to user

**STOP. Get user approval on ALL syntheses before proposing structure.**

**Session break point:** After Phase 2, the source index and syntheses can be used to resume in a new session.

---

### Phase 3: Propose Structure

Create `<OUTPUT_PATH>/proposal.md` — a structural plan describing WHAT you will build, not the content itself.

**CRITICAL: NO CONTENT IN PROPOSALS**

The proposal describes structure. It does NOT contain:
- Summaries of organizational information
- Draft module text
- Descriptions of what the organization does/believes/offers
- Any content that would go IN a module

If you find yourself writing sentences like "The organization focuses on..." or "Key services include..." — STOP. That's content, not structure.

**CRITICAL: NO FABRICATION**

Every fact in the proposal must come from working sources. If you haven't read it in a source file, don't write it. This includes:
- Organization names, descriptions, or positioning
- Service offerings or methodologies
- Team information or credentials
- Any specific details about the organization

**Proposal structure:**

1. **Module list** — ID, name, purpose (what question it answers), which sources inform it, estimated tokens
2. **Agent-module mapping** — Which agents load which modules, total tokens per agent
3. **Conflicts** — Contradictions found in sources, proposed resolution
4. **Gaps** — Missing information classified as blocking/limiting/enhancing
5. **Questions** — Decisions requiring user input

**Token estimates:**
- Base estimates on source content richness, not arbitrary targets
- 20,000 tokens maximum per agent, but include all useful verified content
- Do NOT compress to hit a low number — sparse modules are worse than rich ones

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

Update source index status to `building`.

**FIRST: Copy standard guardrail modules.**

Before building organization-specific modules, copy the guardrail templates:

1. Copy `<skill_dir>/templates/guardrails/F_agent_behavioral_standards.md` to `<OUTPUT_PATH>/modules/foundation/`
2. Copy `<skill_dir>/templates/guardrails/S_natural_prose_standards.md` to `<OUTPUT_PATH>/modules/shared/`
3. Update the module IDs and dates in the copied files
4. Customize organization-specific references (e.g., module cross-references)

These modules are **required**:
- **F_agent_behavioral_standards** — All agents load this. Defines anti-hallucination, epistemic honesty, and professional objectivity rules.
- **S_natural_prose_standards** — External-facing agents load this. Defines writing standards that avoid AI-detectable patterns.

**Do not skip or significantly modify these modules.** They prevent the most common and damaging failure modes.

---

**HOW TO BUILD MODULES:**

**CRITICAL: Write-Time Verification**

Do NOT write from memory. For each module:

1. **Re-read sources in the same turn you write.** Even if you read files in Phase 1, re-read the specific sources for this module immediately before writing.

2. **Copy exact facts.** Legal names, EINs, emails, titles, dates — copy verbatim from source. Do not paraphrase.

3. **Create a verification log** as you write:

   | Fact | Source File | Exact Source Text |
   |------|-------------|-------------------|
   | [fact you're including] | [filename] | [exact quote from source] |

4. **If you can't point to the source, don't include it.** No gap-filling. No "plausible" information.

5. **One module at a time.** Complete and verify each module before starting the next.

---

**Module Building Steps:**

1. **Consult the source index** before writing each module:
   - Check which files have status `ready` (use originals)
   - Check which files have status `synthesized` (use the synthesis file path)
   - The "Working Source" column tells you which file to read

2. **For each module in the proposal:**
   a. Identify which working sources contain relevant content (from index)
   b. Re-read those specific working sources
   c. Write the module using only facts from those sources
   d. Verify before proceeding to next module

3. **Build SEQUENTIALLY:**
   - Foundation modules first
   - Shared modules next
   - Specialized modules last

**For each module:**

1. **Before writing:** Check the source index. Read the working sources listed for this module's content.

2. **While writing:** Every fact must be in a working source from the index. If you cannot point to where a fact appears, do not include it (or mark `[PROPOSED]` if user has approved inferences).

3. **After writing:** Verify against working sources before proceeding to the next module.

**After writing each module:**

Run verification:
```bash
python3 <skill_dir>/scripts/verify_module.py <module_path> <SOURCE_PATH>
```

If any facts are flagged as unverified:
1. Check the source files
2. Either find the source and confirm, or remove the fact
3. Do not proceed to next module until verification passes

---

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
- List required modules (all agents must include F#_agent_behavioral_standards)
- External-facing agents must also include S#_natural_prose_standards
- Estimate total tokens
- Add domain-specific guidance if needed (beyond standard guardrails)

**Do not duplicate guardrail content in agent definitions.** The standard guardrail modules handle anti-hallucination, epistemic honesty, professional objectivity, and natural prose. Agent definitions should only add domain-specific extensions.

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

**INCLUDE ALL USEFUL CONTENT.** Do not compress or summarize to "save tokens." If verified content would help an agent make better decisions, include it.

**What to cut (wasted tokens):**
- Preambles and introductions
- Filler phrases ("In order to effectively...")
- Explanations of concepts Claude already knows
- Redundant content across modules

**What to keep (useful tokens):**
- All verified facts from sources
- Decision criteria and frameworks
- Organizational context
- Specific details that inform agent behavior

**Verified content only.** Every fact must trace to a source. Include all verified content that's relevant — don't artificially compress.

**Modules are prompts, not documentation.** Direct, declarative, front-loaded. This style is efficient, allowing more content without waste.

**Reference, don't repeat.** Each fact exists in one module only. Cross-reference instead of duplicating.

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
