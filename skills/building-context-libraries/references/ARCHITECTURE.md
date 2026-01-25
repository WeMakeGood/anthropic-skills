# Context Library Architecture

## Modules Are Prompt Engineering, Not Documentation

Context libraries exist to give LLMs organizational knowledge. This fundamentally shapes how modules should be written.

**LLMs process context differently than humans:**
- LLMs read the entire context; humans scan and skip
- LLMs don't need explanations of concepts they already know
- LLMs benefit from explicit decision criteria and conditional logic
- LLMs can't follow external links or reference other documents not in context
- LLMs work best with direct, declarative statements

**Write for LLM consumption:**

| Instead of... | Write... |
|---------------|----------|
| "It's important to understand that..." | State the fact directly |
| "See [external document] for details" | Encode the information in the module |
| "Our approach has evolved over time to emphasize..." | "[Topic] principles: [list]" |
| Varied synonyms for style | Consistent terminology throughout |
| Background context explaining why | Direct statements of what and how |

**Token efficiency matters:**
- Every token costs money and consumes context window
- Cut preambles, transitions, and hedging language
- Front-load the most important information
- Use "If X, then Y" patterns for decision logic
- Don't explain what Claude already knows (general concepts, industry basics)

**Effective LLM context patterns:**
```markdown
## [Topic]

[Category A]:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

[Category B]:
- [Criterion 1]
- [Criterion 2]
```

Structured lists with clear categories are more useful to an LLM than narrative prose.

## Content Transformation

Modules contain synthesized organizational knowledge — not source material. Transform content for LLM consumption.

### What Goes In vs. Stays Out

**Include in modules:**
- Decision frameworks ("If X, then Y")
- Organizational principles and values
- Positioning statements
- Service/offering descriptions
- Team structure and roles
- Verified facts (names, dates, figures)

**Do NOT include:**
- Verbatim quotes (synthesize the meaning instead)
- Client names or specific testimonials
- Detailed procedures (extract the decision logic)
- Historical context unless strategically relevant
- Competitive details that may become outdated
- Personal anecdotes or stories

### Transforming Quotes

Quotes in source documents are *evidence* — they inform what should go in modules, but aren't copied directly.

**Source quote:**
> "We always start with a discovery phase because we've learned that jumping straight to implementation usually fails."

**Module content:**
```
Engagement starts with discovery phase before implementation.
Rationale: Direct-to-implementation approaches have poor outcomes.
```

The quote proves the practice exists; the module states the practice.

### Transforming Case Studies

Case studies contain valuable methodology patterns but also client-specific details that don't belong in modules.

**Extract:**
- Methodology patterns ("We used X approach for Y situation")
- Success criteria ("The engagement succeeded when...")
- Lessons learned ("We learned to always...")

**Leave out:**
- Client names (anonymize: "a nonprofit client")
- Specific metrics ("increased donations 47%")
- Testimonials
- Timeline details

### Transforming Process Documents

Process documents often contain step-by-step procedures. Agents don't need procedures — they need decision criteria.

**Source (process doc):**
```
1. Receive client inquiry
2. Check if client is in target market
3. If yes, schedule discovery call
4. If no, refer to partner
```

**Module content:**
```
Client qualification:
- Target market: [criteria from source]
- Qualified → schedule discovery
- Not qualified → refer to partner network
```

The module encodes the *decision logic*, not the procedure.

---

## Module Design Philosophy

**Organize modules for USE, not for taxonomy.**

Modules should be designed around how agents will use them, not around information categories. The goal is to give each agent the context it needs to make good decisions.

**Wrong approach (taxonomy-based):**
- "Organizational Identity" module with all identity facts
- "Voice & Tone" module with all writing guidance
- "Services" module with all service descriptions

This creates many small modules that agents must combine, losing coherence.

**Right approach (use-based):**
- Fewer, richer modules organized around decision-making contexts
- Each module gives an agent what it needs for a type of work
- Foundation modules provide shared context; specialized modules provide depth

**The test:** For each proposed module, ask: "What decision does this help an agent make?" If the answer is unclear, the module may be too abstract or taxonomic.

## Module Hierarchy

Context libraries use three tiers:

### Foundation Modules
Universal organizational context loaded by all or most agents. These should be substantial (2,000-4,000 tokens each) because every agent needs this context.

Typical foundation modules:
- **Organizational Identity**: Who we are, what we do, how we work, who leads us — rich enough for an agent to represent the organization authentically
- **Brand & Communication**: Voice, tone, values in action — rich enough to write in the organization's voice
- **Ethical Framework**: Principles that guide decisions — rich enough to make judgment calls

### Shared Modules
Cross-functional knowledge used by multiple (not all) agents. Each should be substantial enough to support the decisions it informs.

Typical shared modules:
- Client engagement approach
- Service methodology
- Content standards
- Financial frameworks

### Specialized Modules
Domain-specific knowledge for particular agent roles.

Examples:
- Program details (for program-focused agents)
- Technical processes (for technical agents)
- Curriculum content (for learning agents)

## Single Source of Truth

**Critical rule**: Each piece of information exists in exactly ONE module.

Wrong:
```markdown
# Module A
[Fact X]

# Module B
[Fact X]  ← DUPLICATE
```

Right:
```markdown
# Module A (Foundation)
[Fact X]

# Module B (Shared)
> See [Module A] for [Fact X].
```

## Cross-Reference Patterns

Use explicit references:

```markdown
> **See [Module Name]** for [specific information].

> **Requires [Module Name]** for complete context.

> **Related:** [Module Name] covers [complementary topic].
```

## Content Verification

**All content must be verified.** Every fact must trace to a working source.

**Working sources** are:
- Original source files marked `ready` in the source index
- Synthesis files for sources that needed synthesis

**The only marker:** `[PROPOSED]` — Use this for inferences or recommendations that the user has approved including. Everything else is verified fact from sources.

If you cannot point to where a fact appears in working sources, either:
1. Remove it, or
2. Mark it `[PROPOSED]` (only if user has approved including inferences)

**Superseded information:** If newer documents override older ones, use the newer information. Do not include outdated content — it wastes tokens and confuses agents.

## Token Budget Management

**Guideline**: ~20,000 tokens per agent's complete module set.

This is a planning target to be *used*, not avoided. The goal is effective agents with rich context.

**Expected ranges:**
- Most agents should land at **12,000-18,000 tokens**
- Agents under 10,000 tokens are likely missing useful context
- Agents over 20,000 tokens should be reviewed for unnecessary duplication

**Budget allocation guidance:**
- Foundation modules: ~6,000-10,000 tokens total (shared across agents)
- Shared modules: ~4,000-8,000 tokens per agent's selection
- Specialized modules: ~2,000-4,000 tokens (targeted)

**Individual module sizing:**
- Most modules should be **2,000-4,000 tokens**
- Modules under 1,000 tokens are almost certainly too thin
- A 600-800 token module suggests over-compression

**Warning signs of over-compression:**
- Multiple modules under 1,000 tokens
- Agents totaling under 10,000 tokens
- Module descriptions are thin bullet points rather than usable guidance
- Agents lack context to make nuanced decisions

**When to trim:**
- Content is duplicated across modules
- Explanatory content about general concepts (not organization-specific)
- Agent is loading modules it doesn't actually use

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
## [Decision Area]

When selecting [type of thing], we prioritize:
- [Principle 1]
- [Principle 2]
- [Principle 3]
```

**Bad (locked-in):**
```markdown
## [Decision Area]

We use [specific tool] because:
- [Reason specific to that tool]
- [Another tool-specific reason]
```

The first version helps agents evaluate *any* option using principles. The second locks the organization into a specific choice that may change.

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

When working sources lack needed information:

1. Note the gap in the source index (Phase 1)
2. Carry gaps forward to the proposal (Phase 3)
3. Classify impact:
   - **BLOCKING**: Agent cannot function — must resolve before building
   - **LIMITING**: Agent works but reduced capability — note in validation
   - **ENHANCING**: Would improve but not essential — low priority
4. Ask user about BLOCKING gaps before proceeding to build

**Never invent information to fill gaps.** A thin module with verified facts is better than a rich module with hallucinations.

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
   [HIGH-STAKES] [Financial claim from source document]
   [HIGH-STAKES] [Certification/credential from source document]
   ```

2. **Source requirements by stakes level:**
   - HIGH: Must be verifiable in working sources
   - MEDIUM: Should be verifiable; `[PROPOSED]` acceptable if clearly marked
   - LOW: `[PROPOSED]` acceptable based on pattern inference

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
