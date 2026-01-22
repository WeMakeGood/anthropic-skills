# Context Library Architecture

## Module Hierarchy

Context libraries use three tiers:

### Foundation Modules
Universal organizational context loaded by all or most agents.

Typical foundation modules:
- **Organizational Identity**: Legal entity, leadership, history, contact info
- **Strategic Positioning**: What we do, what makes us unique, value proposition
- **Communication Principles**: Voice, tone, terminology, words to avoid
- **Target Market**: Who we serve, ideal client characteristics

### Shared Modules
Cross-functional knowledge used by multiple (not all) agents.

Typical shared modules:
- Service/product methodology
- Client engagement approach
- Content development standards
- Financial/contractual frameworks
- Partner/vendor relationships

### Specialized Modules
Domain-specific knowledge for particular agent roles.

Examples:
- Sales process details (for sales agents)
- Technical specifications (for technical agents)
- HR policies (for HR agents)

## Single Source of Truth

**Critical rule**: Each piece of information exists in exactly ONE module.

Wrong:
```markdown
# Module A
Our mission is to help nonprofits thrive.

# Module B
Our mission is to help nonprofits thrive.  ← DUPLICATE
```

Right:
```markdown
# Module A (Foundation)
Our mission is to help nonprofits thrive.

# Module B (Shared)
> See [Organizational Identity] for mission statement.
```

## Cross-Reference Patterns

Use explicit references:

```markdown
> **See [Module Name]** for [specific information].

> **Requires [Module Name]** for complete context.

> **Related:** [Module Name] covers [complementary topic].
```

## Confidence Markers

Mark all information:

- `[CONFIRMED]` - Verified from authoritative source document
- `[PROPOSED]` - Logical inference, not explicitly stated in sources
- `[HISTORICAL]` - Was true but may have changed

Example:
```markdown
[CONFIRMED] Founded in 2005 as Frazier Media.

[PROPOSED] Typical project duration is 4-8 weeks based on past work.

[HISTORICAL] Previously positioned as "advocacy consultancy" (pre-2025).
```

## Token Budget Management

**Guideline**: ~20,000 tokens per agent's complete module set.

This is a planning target, not a hard constraint. The goal is effective agents, not minimal agents.

**Budget allocation guidance:**
- Foundation modules: ~5,000-8,000 tokens (shared across agents)
- Shared modules: ~4,000-10,000 tokens (varies by agent needs)
- Specialized modules: ~2,000-5,000 tokens (targeted)
- **Buffer**: Leave room for conversation context

**When to exceed the guideline:**
- Content is coherent and can't be meaningfully split
- Removing content would harm agent effectiveness
- The agent's role genuinely requires broad context

**When to tighten:**
- Agent is loading modules it rarely uses
- Content is duplicated across modules
- Explanatory content could be trimmed (Claude knows most concepts)

Run `python scripts/count_tokens.py` to measure actual usage.

## Module Naming Convention

Format: `{tier_prefix}{number}_{descriptive_name}.md`

Examples:
- `F1_organizational_identity.md`
- `S3_client_engagement.md`
- `D2_sales_process.md`

Use lowercase with underscores. Keep names descriptive but concise.

## Agent Definition Structure

Each agent needs:
1. List of modules to load
2. Total token estimate
3. Role description
4. Behavioral guidance

Agents should load:
- All relevant foundation modules
- Shared modules for their function
- Specialized modules for their domain

## Principles Over Prescriptions

Context libraries should enable future decisions, not constrain them. Avoid encoding specific methodologies when principles would serve better.

### What to Capture

**Good (flexible):**
```markdown
## AI Tool Evaluation

When selecting AI tools, we prioritize:
- Alignment with our ethical AI principles (see F3)
- Ability to work with organizational context
- Transparency in how outputs are generated
- Cost sustainability for nonprofit clients
```

**Bad (locked-in):**
```markdown
## AI Tool Selection

We use Claude for all AI work because:
- It handles long context well
- It's more honest than competitors
- Our workflows are built around it
```

The first version helps agents evaluate *any* tool. The second locks the organization into a specific choice.

### Common Over-Specification Patterns

**Speculative frameworks:** If a source document mentions "three types of users," ask: Is this a confirmed organizational framework, or an illustrative example? Don't encode speculation as methodology.

**Illustrative examples as prescriptions:** A case study showing *one way* something was done shouldn't become *the way* it must be done.

**Current state as permanent state:** "We currently use X" should become "Our criteria for selecting tools like X" unless there's strategic commitment to X specifically.

### The Test

Before including detailed methodology, ask:
1. Is this grounded in source documents, or am I synthesizing?
2. Does this enable flexibility or constrain it?
3. Would this content still be useful if circumstances changed?
4. Am I capturing principles or prescriptions?

## Information Gaps

When source documents lack needed information:

1. Note the gap in your proposal
2. Classify impact:
   - **BLOCKING**: Agent cannot function
   - **LIMITING**: Agent works but reduced capability
   - **ENHANCING**: Would improve but not essential
3. Ask user for BLOCKING gaps before proceeding
4. Mark LIMITING/ENHANCING gaps in validation report

Never invent information to fill gaps.

## Content Stakes Classification

Not all information carries equal weight. Classify content by the consequences of errors:

### Stakes Levels

**HIGH STAKES** — Errors cause significant harm
- Legal claims, compliance requirements, contractual obligations
- Financial figures, pricing, revenue data
- Claims about partners, clients, or third parties
- Credentials, certifications, regulatory status
- Public commitments or promises

**MEDIUM STAKES** — Errors cause confusion or inefficiency
- Service descriptions, methodologies, processes
- Team roles and responsibilities
- Timeline and milestone information
- Technical specifications

**LOW STAKES** — Errors cause minor inconvenience
- General descriptions and overviews
- Historical context (non-binding)
- Internal terminology definitions
- Process preferences (non-critical)

### How Stakes Affect Module Content

1. **Mark stakes explicitly** in modules containing high-stakes content:
   ```markdown
   [HIGH-STAKES] Annual revenue: $2.4M (FY2024 audited financials)
   [HIGH-STAKES] SOC 2 Type II certified since 2022
   ```

2. **Source requirements by stakes level:**
   - HIGH: Must have explicit source document citation
   - MEDIUM: Should have source; [PROPOSED] acceptable if clearly marked
   - LOW: [PROPOSED] acceptable based on pattern inference

3. **Verification guidance:** High-stakes content should trigger verification behaviors in agents (see Agent Definition Template).

### Stakes in Agent Definitions

When defining agents, specify how they should handle different stakes levels:
- Which content requires human verification before external use?
- Which claims should the agent flag for review?
- What should the agent do when asked to extrapolate from high-stakes data?

This calibrates agent behavior to the actual risk profile of different information.

## Natural Prose (External-Facing Agents)

Agents that produce marketing content, website copy, case studies, or other external-facing text must avoid AI-detectable writing patterns. LLMs have distinctive verbal tics that trained readers recognize instantly.

### When to Include

- **Marketing/communications agents** → Always include Natural Prose section
- **Content creation agents** → Always include
- **Internal documentation agents** → Skip (lower risk)
- **Research/analysis agents** → Skip unless output is published

### What to Include

The Natural Prose section in agent definitions should specify:

**Banned vocabulary:** Words that appear far more frequently in AI text than human writing:
- Significance words: pivotal, crucial, vital, cornerstone, testament to, underscores, highlights
- Promotional language: vibrant, tapestry, cutting-edge, groundbreaking, nestled, showcases, boasts
- AI favorites: delve, foster, garner, leverage, landscape (figurative), holistic, robust, synergy

**Banned structures:**
- Negative parallelisms: "Not only X, but Y"
- Copula avoidance: "serves as" instead of "is"
- Superficial -ing analysis: "highlighting the importance of..."
- Vague attribution: "experts say," "industry leaders"
- Formulaic false balance: "Despite challenges, [positive spin]"

**Required behaviors:**
- Use simple verbs ("is" not "serves as")
- Repeat nouns rather than cycling through synonyms
- Be concrete with numbers and specifics
- Match the voice of actual practitioners in the field

See [TEMPLATES.md](TEMPLATES.md) for the complete Natural Prose section to include in agent definitions.
