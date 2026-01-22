---
name: building-context-libraries
description: Builds AI context libraries from organizational source documents. Creates modular knowledge bases that give domain agents organizational context. Use when building a context library, creating domain agent modules, or transforming organizational documents into LLM-optimized context.
---

# Building Context Libraries

Build structured context libraries that encode organizational knowledge for AI agents.

## Critical Rules

**GROUNDING:** Every fact in the library MUST trace to a specific source document. Never synthesize "common knowledge" or infer organizational practices.

**CONFLICT RESOLUTION:** When source documents contradict each other, surface the conflict to the user. Do not silently resolve by picking one version.

**EPISTEMIC MARKERS:** Use `[CONFIRMED]`, `[PROPOSED]`, `[HISTORICAL]` consistently. When in doubt, use the more conservative marker.

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

## Build Process

### Phase 1: Analysis

**MANDATORY FIRST STEP - Run the inventory script:**

First, locate this skill's directory (where this SKILL.md lives), then run:

```bash
python3 <skill_dir>/scripts/analyze_sources.py <SOURCE_PATH>
```

For example, if this skill is at `.claude/skills/building-context-libraries/`:
```bash
python3 .claude/skills/building-context-libraries/scripts/analyze_sources.py ./source
```

You MUST run this script before reading any documents. It provides:
- Complete file inventory with word/token counts
- Estimated final library size
- Reading order guidance

**DO NOT skip this step or substitute with `ls` or manual file discovery.**

**REQUIRED:** After running the script, read ALL documents systematically (not sampling). Do not proceed to Phase 2 until you have read every document.

As you read, identify:

**Organizational Understanding:**
- Who is this organization?
- What do they do?
- How do they work?
- Who do they serve?

**Content Stakes Assessment:**
As you read, note which content carries high stakes (errors cause significant harm):
- Legal, compliance, or contractual claims
- Financial figures and metrics
- Claims about partners, clients, or third parties
- Credentials, certifications, regulatory status

This assessment informs how modules are built and how agents handle different content.

**Content Conflict Detection (CRITICAL):**
Look for documents that indicate strategic changes, reorganizations, or updated positioning. Common indicators:
- Documents with dates (newer overrides older)
- Documents titled "Strategic...", "Reorganization...", "Updated..."
- Gap analysis or interview guides (indicate missing information)
- Requirements documents that specify what should be built

**When conflicts are found between documents:**
1. **Identify the conflict explicitly** - What does Document A say vs Document B?
2. **Determine which is authoritative** - Usually newer strategic docs override older operational docs
3. **Mark historical content** - Old positioning becomes `[HISTORICAL]`, not deleted
4. **Ask the user if unclear** - Don't assume; conflicts may need human decision

**Check for documented gaps:**
- Look for gap analysis documents, interview guides, or TODO markers
- These indicate information that is KNOWN to be missing
- These become BLOCKING gaps in your proposal

### Phase 2: Propose Structure

Create `<OUTPUT_PATH>/proposal.md` with:
- Proposed foundation modules (universal context)
- Proposed shared modules (cross-functional)
- Proposed specialized modules (domain-specific)
- Module-to-agent mapping for each agent in `AGENTS`

**Content Conflicts Section (REQUIRED):**
- List all identified conflicts between source documents
- For each conflict: what changed, which document is authoritative, how you'll handle it
- Ask user to confirm conflict resolutions before proceeding

**Information Gaps Section (REQUIRED):**
- **Blocking gaps**: Information that MUST exist but doesn't (from gap analysis docs or missing critical content)
- **Limiting gaps**: Information that would help but isn't essential
- **Enhancing gaps**: Nice-to-have information

If BLOCKING gaps exist, note that the library cannot be completed until they are resolved (e.g., through interviews, additional documentation).

**Do not minimize gaps to make the proposal look better.** If the source documents are insufficient for a quality library, say so directly.

**STOP. Get explicit user approval before building. Do not proceed on implied or partial approval.**

### Phase 3: Build Modules

After approval, create folder structure:
```
<OUTPUT_PATH>/
├── modules/
│   ├── foundation/
│   ├── shared/
│   └── specialized/
├── agents/
└── proposal.md
```

Build modules in order:
1. **Foundation first** → `modules/foundation/`
2. **Shared next** → `modules/shared/`
3. **Specialized last** → `modules/specialized/`

Use formats from [references/TEMPLATES.md](references/TEMPLATES.md).

Key rules:
- Single source of truth: each fact in ONE module only
- Explicit references: `See [Module Name]` for cross-module info
- Mark confidence: `[CONFIRMED]`, `[PROPOSED]`, or `[HISTORICAL]`

### Phase 4: Create Agent Definitions

For each agent in `AGENTS`, create definition in `<OUTPUT_PATH>/agents/`:
- List required modules
- Estimate total tokens
- Include behavioral guidance
- Define verification behaviors based on content stakes
- Specify professional objectivity guidelines (when to challenge, verify, flag)
- **For agents producing external-facing content:** Include Natural Prose guardrails (banned vocabulary, banned structures, required behaviors)

### Phase 5: Validate

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

**STOP. Get user approval on final library.**

## Key Principles

**Concise modules**: Include only organization-specific knowledge. Don't explain concepts Claude already knows.

**Reference, don't repeat**: If info exists in Module A, Module B says "See [Module A]" - never duplicates.

**Confidence markers**: Mark all facts as `[CONFIRMED]` (from sources), `[PROPOSED]` (inference), or `[HISTORICAL]` (may be outdated).

**Token awareness**: The 20K token guideline per agent is a planning target, not a hard limit. Prioritize completeness and coherence over aggressive compression. If an agent needs 22K tokens to be effective, that's acceptable. If it needs 35K, consider whether some modules can be split or made optional.

**Principles over prescriptions**: Extract decision-making frameworks, not specific methodologies. A module should help agents make good decisions in new situations, not lock them into documented past choices. Ask: "Does this content enable flexibility or constrain it?"

## When to Stop and Ask

**REQUIRED:** Get explicit user approval at these checkpoints:
- After gathering requirements (before analysis)
- After proposing structure (before building)
- When source documents have significant gaps
- When you identify conflicts between source documents
- After validation (before declaring complete)

**Do not proceed past a checkpoint without explicit approval.** "Sounds good" or similar is sufficient; silence or topic change is not.

## References

- [references/ARCHITECTURE.md](references/ARCHITECTURE.md) - Module design principles and content stakes classification
- [references/TEMPLATES.md](references/TEMPLATES.md) - Module and agent formats (includes verification/objectivity guidance)
- [references/VALIDATION.md](references/VALIDATION.md) - Validation checklist
