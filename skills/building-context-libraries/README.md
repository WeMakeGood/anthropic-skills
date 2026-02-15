# Building Context Libraries

A skill for Claude that transforms organizational documents into structured knowledge bases for AI agents.

## What It Does

This skill guides Claude through a 7-phase workflow to analyze source documents and build a modular context library that gives domain-specific AI agents the organizational knowledge they need to work effectively.

**The core insight:** AI agents work better when they have structured, organization-specific context rather than trying to derive everything from raw documents or general knowledge.

**Critical distinction:** Context modules are **prompts for LLM agents**, not documentation for humans. Transcripts and interviews must be *transformed* into clean, actionable knowledge — not transcribed or lightly edited. If a module reads like the source document, the skill has failed.

## Why Use It

**Without a context library:**
- Agents hallucinate organizational details
- Inconsistent outputs across different conversations
- No systematic way to update organizational knowledge
- High-stakes content (legal, financial) treated the same as general descriptions

**With a context library:**
- Agents draw from verified, sourced organizational facts
- Consistent voice, positioning, and accuracy
- Modular updates when information changes
- Stakes-based verification ensures high-risk content is handled carefully

## When to Use It

**Trigger phrases that work well:**

- "Build a context library from these documents"
- "Create domain agent modules for [organization]"
- "Transform these org docs into LLM-optimized context"
- "Set up a knowledge base for AI agents"

**Use cases:**

- Onboarding AI agents to work with a new organization
- Creating consistent context for multiple specialized agents
- Building knowledge bases that can be updated incrementally
- Ensuring AI outputs align with organizational voice and facts

## How It Works

### Phase 1: Index Sources

A Python script creates the **source index** — a master manifest of ALL source files:

```bash
python3 scripts/create_source_index.py ./source ./context-library
```

The script:
- Finds ALL markdown/text files (none are skipped)
- Classifies each by type (strategy, transcript, operational, etc.)
- Sets initial status (ready or needs-synthesis)
- Creates a reading checklist

Claude then reads EVERY file in the index and updates it with conflicts and gaps.

You approve the index before proceeding.

### Phase 2: Synthesize Complex Sources

For messy sources like transcripts and interviews, Claude creates **synthesis files**:

- One synthesis per complex source document
- Extracts facts, decisions, and principles
- Removes speech artifacts and filler words
- Flags ambiguous items for your clarification

You approve each synthesis. These become the "working sources" for module building.

**Session break point:** After Phase 2, you can stop and resume later. The source index and synthesis files persist — a new session reads these instead of re-reading original documents.

### Phase 3: Analyze Sources

Claude analyzes working sources to identify:

- **Work patterns** — What decisions and outputs agents will produce
- **Agent roles** — Which agents are needed, based on distinct work patterns (not taxonomy)
- **Content tiers** — Foundation (all agents), shared (multiple agents), specialized (specific agents)
- **Addenda candidates** — Volatile reference data (pricing, bios, catalogs) that belongs in addenda rather than modules

### Phase 4: Propose Structure

Claude creates a proposal with:

- **Foundation modules** — Universal context all agents need
- **Shared modules** — Cross-functional knowledge for multiple agents
- **Specialized modules** — Domain-specific knowledge for particular roles
- **Addenda** — Volatile reference data that modules point to (pricing, bios, service catalogs)
- **Conflict resolutions** — How contradictory documents will be handled
- **Gap analysis** — What's missing and whether it blocks progress

You approve before building begins.

**Mandatory session break:** Always start a new session before Phase 5.

### Phase 5: Build Modules & Addenda

Claude builds the library in order:

1. **Guardrail modules** — copied from templates (anti-hallucination, natural prose standards)
2. **Foundation modules** — organizational identity, positioning
3. **Shared modules** — methodology, engagement approach
4. **Specialized modules** — domain-specific depth
5. **Addenda** — volatile reference data (pricing tables, biographical details, service catalogs)

Modules are metaprompts — they tell agents how to behave, not just what facts exist. Addenda are data — they provide reference information that modules point to. Each module and addendum is verified against working sources.

### Phase 6: Create Agent Definitions

For each domain agent, Claude creates:

- Module loading list (all agents load `F_agent_behavioral_standards`)
- External-facing agents also load `S_natural_prose_standards`
- Optional reference addenda (loaded on demand, don't count against token budget)
- Token budget estimate
- Role description and responsibilities
- Domain-specific guidance (beyond standard guardrails, if needed)

**Standard guardrails are loaded as modules, not duplicated in agent definitions.**

### Phase 7: Validate

Scripts and manual checks verify:

- Broken cross-references (modules and addenda)
- Duplicated information
- Token budget overruns
- Unmarked high-stakes content
- Missing verification guidance
- Facts not traceable to working sources
- Addenda quality (data only, no behavioral instructions, properly referenced)

## Key Concepts

### Source Index & Working Sources

The **source index** is the master manifest tracking all source files. Each file is classified by type and status:

| Type | Description | Handling |
|------|-------------|----------|
| `strategy` | Polished positioning, decisions | Use directly |
| `operational` | Current processes, structures | Use directly |
| `transcript` | Conversational speech | Needs synthesis |
| `interview` | Q&A format | Needs synthesis |
| `notes` | Meeting notes | May need synthesis |
| `reference` | Supporting material | Use directly |

**Working sources** are what module building actually uses — either original files marked `ready` or synthesis files for complex sources.

### Modules vs. Addenda

The library produces two types of output:

| Component | Contains | Changes When | Token Budget |
|-----------|----------|-------------|-------------|
| **Modules** | Metaprompting — behavioral instructions, decision frameworks | Processes are redesigned | Counts against 20K limit |
| **Addenda** | Data — pricing, bios, catalogs, rate cards | Business evolves | Does not count (loaded on demand) |

Modules reference addenda (`See addenda/pricing.md for current rates`). Addenda don't contain behavioral instructions.

### Content Stakes Classification

Not all information carries equal weight. The skill teaches Claude to classify content by consequences of errors:

| Stakes Level | Examples | Handling |
|--------------|----------|----------|
| **HIGH** | Legal claims, financials, certifications, third-party claims | Must have source citation, triggers verification behaviors |
| **MEDIUM** | Service descriptions, methodologies, team roles | Should have source, `[PROPOSED]` acceptable if marked |
| **LOW** | General overviews, internal terminology, process preferences | `[PROPOSED]` acceptable |

### Professional Objectivity

Agent definitions include guidance on serving user needs rather than just validating assumptions:

- **Challenge when:** User request contradicts documented strategy
- **Verify before:** Making claims about partners, clients, or figures
- **Flag for review:** Output intended for external audiences

### Module Hierarchy

```
Foundation     → Universal context (identity, positioning, voice)
    ↓
Shared         → Cross-functional (methodology, engagement, standards)
    ↓
Specialized    → Domain-specific (sales process, technical specs, HR)
    ↓
Addenda        → Reference data (pricing, bios, catalogs — loaded on demand)
```

## Outputs

```
context-library/
├── source-index.md           # Master manifest of all sources
├── build-state.md            # Progress tracking across sessions
├── analysis.md               # Source analysis (work patterns, agent derivation)
├── proposal.md               # Structure proposal (approved before build)
├── synthesis/                # Cleaned versions of complex sources
│   ├── interview-1-synthesis.md
│   └── transcript-synthesis.md
├── modules/
│   ├── foundation/           # F1_organizational_identity.md, etc.
│   ├── shared/               # S1_methodology.md, etc.
│   └── specialized/          # D1_sales_process.md, etc.
├── addenda/                  # Volatile reference data
│   ├── pricing-and-rates.md
│   └── founder-bios.md
└── agents/
    ├── content-writer.md     # Agent definitions with module lists
    ├── client-advisor.md
    └── ...
```

## Scripts

The skill includes Python validation scripts:

```bash
# Create source index (run first)
python3 scripts/create_source_index.py ./source ./context-library

# Analyze source documents (detailed inventory)
python3 scripts/analyze_sources.py ./source-documents

# Validate library structure
python3 scripts/validate_library.py ./context-library/modules

# Check token budgets per agent
python3 scripts/count_tokens.py ./context-library/modules ./context-library/agents

# Verify module facts against sources
python3 scripts/verify_module.py ./context-library/modules/F1_identity.md ./sources
```

## Example

**Input:**

```
Build a context library from the documents in ./makegood-docs/
Create agents for: content-writer, proposal-drafter, client-advisor
Output to: ./makegood-context/
```

**Output:** A complete context library with:

- Source index tracking all source files and their status
- Synthesis files for any transcripts or interviews
- 3-4 foundation modules (identity, positioning, voice, audience)
- 2-4 shared modules (methodology, engagement approach)
- 1-2 specialized modules per agent
- Addenda for volatile data (pricing, biographical details, service catalogs)
- Agent definitions with module lists and optional addenda references
- Validation report confirming no issues

## Session Breaks & Resumption

The index-based architecture supports stopping and resuming:

- **After Phase 1-2:** Source index + syntheses exist — resume with analysis
- **After Phase 3-4:** Proposal approved — **mandatory break** before Phase 5
- **After Phase 5:** Modules + addenda complete — resume with agent definitions
- **build-state.md** tracks progress, points to the current phase instruction file

When resuming, Claude reads the artifacts instead of re-reading original sources. This enables:

- Long builds to span multiple sessions
- Context compaction without losing work
- User review at natural checkpoints

## Tips for Best Results

1. **Gather comprehensive source documents** — strategic plans, style guides, service descriptions, team bios, case studies
2. **Include documents that show evolution** — helps identify what's current vs. historical
3. **Know your agents upfront** — the skill optimizes module structure for specific agent roles
4. **Resolve blocking gaps** — if critical information is missing, provide it before building
5. **Review syntheses carefully** — they become the working sources for everything after

## Limitations

- Requires source documents (can't build from scratch)
- Token budgets assume ~20K context per agent (adjust for your model)
- High-stakes content still needs human verification for external use
- Cannot resolve conflicting information without user input

## File Structure

```
building-context-libraries/
├── SKILL.md                    # Main skill instructions
├── README.md                   # This file
├── references/
│   ├── ARCHITECTURE.md         # Module design, content transformation, addenda architecture
│   ├── TEMPLATES.md            # All templates (modules, addenda, agents, proposal, build state)
│   ├── VALIDATION.md           # Phase-by-phase validation checklists
│   └── phases/                 # Per-phase instruction files
│       ├── PHASE_1_INDEX.md
│       ├── PHASE_2_SYNTHESIZE.md
│       ├── PHASE_3_ANALYZE.md
│       ├── PHASE_4_PROPOSE.md
│       ├── PHASE_5_BUILD.md
│       └── PHASE_6_7_AGENTS_VALIDATE.md
├── templates/
│   ├── build-state.md          # Progress tracking template
│   └── guardrails/
│       ├── F_agent_behavioral_standards.md   # Required: anti-hallucination, epistemic honesty
│       └── S_natural_prose_standards.md      # Required for external-facing agents
└── scripts/
    ├── create_source_index.py  # Creates source-index.md (run first)
    ├── analyze_sources.py      # Source document inventory (detailed analysis)
    ├── validate_library.py     # Cross-reference and structure checks
    ├── count_tokens.py         # Token budget calculator
    └── verify_module.py        # Check module facts against sources
```

## Guardrail Modules

Every context library includes two standard guardrail modules (copied from `templates/guardrails/`):

**F_agent_behavioral_standards.md** (Foundation, all agents)
- Anti-hallucination requirements and source grounding
- Epistemic honesty and confidence calibration
- HIGH-STAKES content verification
- Professional objectivity rules
- Uncertainty handling

**S_natural_prose_standards.md** (Shared, external-facing agents)
- Banned AI-detectable vocabulary
- Banned syntactic patterns
- Required writing behaviors
- Context-specific guidance
- Revision checklist

These modules prevent the most common failure modes: hallucination, sycophancy, and AI-detectable writing patterns.
