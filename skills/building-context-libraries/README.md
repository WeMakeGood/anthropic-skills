# Building Context Libraries

A skill for Claude that transforms organizational documents into structured knowledge bases for AI agents.

## What It Does

This skill guides Claude through a 5-phase workflow to analyze source documents and build a modular context library that gives domain-specific AI agents the organizational knowledge they need to work effectively.

**The core insight:** AI agents work better when they have structured, organization-specific context rather than trying to derive everything from raw documents or general knowledge.

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

### Phase 1: Analysis

Claude runs an inventory script to assess your source documents, then reads everything systematically to understand:

- Who the organization is and what they do
- How they work and who they serve
- Which content is high-stakes (legal, financial, third-party claims)
- Conflicts between documents (newer strategy vs. older operations)
- Information gaps that need resolution

### Phase 2: Propose Structure

Claude creates a proposal with:

- **Foundation modules** — Universal context all agents need
- **Shared modules** — Cross-functional knowledge for multiple agents
- **Specialized modules** — Domain-specific knowledge for particular roles
- **Conflict resolutions** — How contradictory documents will be handled
- **Gap analysis** — What's missing and whether it blocks progress

You approve before building begins.

### Phase 3: Build Modules

Claude creates the module structure with:

- Single source of truth (each fact in ONE place)
- Explicit cross-references between modules
- Confidence markers (`[CONFIRMED]`, `[PROPOSED]`, `[HISTORICAL]`)
- High-stakes markers with source citations

### Phase 4: Create Agent Definitions

For each domain agent, Claude creates:

- Module loading list and token budget
- Role description and responsibilities
- **Stakes-based verification guidance** — how to handle high/medium/low stakes content
- **Professional objectivity guidance** — when to challenge, verify, or flag for review
- **Uncertainty handling** — what to do when information is missing

### Phase 5: Validate

Scripts check for:

- Broken cross-references
- Duplicated information
- Token budget overruns
- Unmarked high-stakes content
- Missing verification guidance

## Key Concepts

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
```

## Outputs

```
context-library/
├── proposal.md              # Structure proposal (approved before build)
├── modules/
│   ├── foundation/          # F1_organizational_identity.md, etc.
│   ├── shared/              # S1_methodology.md, etc.
│   └── specialized/         # D1_sales_process.md, etc.
└── agents/
    ├── content-agent.md     # Agent definitions with module lists
    ├── sales-agent.md
    └── ...
```

## Scripts

The skill includes Python validation scripts:

```bash
# Analyze source documents (run first)
python3 scripts/analyze_sources.py ./source-documents

# Validate library structure
python3 scripts/validate_library.py ./context-library/modules

# Check token budgets per agent
python3 scripts/count_tokens.py ./context-library/modules ./context-library/agents
```

**Dependencies:** `tiktoken` (for token counting)

```bash
pip install tiktoken
```

## Example

**Input:**

```
Build a context library from the documents in ./makegood-docs/
Create agents for: content-writer, proposal-drafter, client-advisor
Output to: ./makegood-context/
```

**Output:** A complete context library with:

- 3-4 foundation modules (identity, positioning, voice, audience)
- 2-4 shared modules (methodology, engagement approach, pricing)
- 1-2 specialized modules per agent
- Agent definitions with verification guidance
- Validation report confirming no issues

## Tips for Best Results

1. **Gather comprehensive source documents** — strategic plans, style guides, service descriptions, team bios, case studies
2. **Include documents that show evolution** — helps identify what's current vs. historical
3. **Know your agents upfront** — the skill optimizes module structure for specific agent roles
4. **Resolve blocking gaps** — if critical information is missing, provide it before building

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
│   ├── ARCHITECTURE.md         # Module design, stakes classification
│   ├── TEMPLATES.md            # Module and agent templates
│   └── VALIDATION.md           # Validation checklist
└── scripts/
    ├── analyze_sources.py      # Source document inventory
    ├── validate_library.py     # Cross-reference and structure checks
    └── count_tokens.py         # Token budget calculator
```
