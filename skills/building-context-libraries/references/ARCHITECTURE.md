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

**Default limit**: 20,000 tokens per agent's complete module set.

Budget allocation guidance:
- Foundation modules: ~5,000-6,000 tokens (shared across agents)
- Shared modules: ~4,000-8,000 tokens (varies by agent needs)
- Specialized modules: ~2,000-4,000 tokens (targeted)
- **Buffer**: Keep 20-30% for conversation context

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
