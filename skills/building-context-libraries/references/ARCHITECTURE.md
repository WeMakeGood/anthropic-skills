# Context Library Architecture

## Modules Are Metaprompts, Not Documentation

Context libraries exist to shape how LLM agents *behave* with organizational knowledge. Modules are not fact sheets — they are system prompt components that change agent behavior.

### Content vs. Context vs. Metaprompting

Source documents contain **content** (raw facts). The agent building this library defaults to copying content into modules because it's easier than transformation. This produces modules that are useless — fact sheets an agent reads but doesn't act on.

| Level | What It Is | Example |
|-------|-----------|---------|
| **Content** (source material) | Raw facts from documents | "We offer workshops, coaching, and consulting services" |
| **Context** (minimum bar for modules) | Processed knowledge that shapes behavior | "Each service format fits a different client need — workshops for shared vocabulary, coaching for personal development, consulting for structural change. Recommending the right one depends on the prospect's challenge, not on listing all three." |
| **Metaprompting** (target for modules) | Instructions that tell the agent how to think | "When a prospect describes their challenge, match one format to their situation. Never present all three as a menu — that forces the prospect to self-diagnose." |

**Every module section should be context or metaprompting.** The transformation test:

1. **Does this change how the agent behaves?** Content doesn't. Context/metaprompting does.
2. **Could the agent act on this without further interpretation?** If the agent would need to figure out *what to do with* the information, you've written content, not context.
3. **Does this read like a Wikipedia article or like a system prompt?** Modules should read like the latter.

### Writing for LLM Consumption

**LLMs process context differently than humans:**
- LLMs read the entire context; humans scan and skip
- LLMs don't need explanations of concepts they already know
- LLMs benefit from explicit decision criteria and conditional logic
- LLMs can't follow external links or reference other documents not in context
- LLMs work best with direct, declarative statements

**Write metaprompts, not summaries:**

| Instead of... | Write... |
|---------------|----------|
| "The organization has 50 employees" | "When clients ask about capacity, lead with expertise areas, not headcount — headcount changes quarterly, expertise positioning doesn't" |
| "Services include Advisory, Implementation, Managed" | "When recommending services, match to client readiness: Advisory for exploration-stage, Implementation for committed adopters, Managed for ongoing support" |
| "It's important to understand that..." | State the behavioral instruction directly |
| "See [external document] for details" | Encode the information in the module |
| Varied synonyms for style | Consistent terminology throughout |

**Token efficiency matters:**
- Every token costs money and consumes context window
- Cut preambles, transitions, and hedging language
- Front-load behavioral instructions, then supporting context
- Use "If X, do Y" patterns for decision logic
- Don't explain what Claude already knows (general concepts, industry basics)

**Effective module patterns:**
```markdown
## Client Engagement

When qualifying a new client:
- If AI maturity is early-stage → recommend Advisory engagement, emphasize quick wins
- If AI maturity is intermediate → recommend Implementation, scope 8-12 week project
- If AI maturity is advanced → recommend Managed services, propose ongoing retainer

Never recommend Managed before the client has completed at least one Implementation engagement.
```

This pattern tells the agent what to DO. A content-only version would just list the three service tiers.

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

### Transforming Transcripts and Interviews

Transcripts are the messiest source type. Machine transcription adds errors. Conversational speech includes filler words, false starts, tangents, and incomplete thoughts. Your job is to extract the *meaning* and discard the mess.

**What transcripts contain (discard or transform all of this):**
- Filler words: "um," "uh," "you know," "like," "I mean"
- False starts: "We usually — well, actually we sometimes —"
- Tangents and digressions
- Conversational hedging: "I think maybe," "sort of," "kind of"
- Repetition and restarts
- Transcription errors and artifacts
- Speaker attributions for routine statements
- **Time spans** — Convert to dates (see below)

**What to extract (keep only this):**
- Facts and decisions stated
- Principles and values expressed
- Processes and approaches described
- Organizational positions and stances

**Example transformation:**

**Source (transcript):**
```
Yeah so we, um, we really try to — I mean, it's something we've always believed in —
meeting clients where they are, you know? Like if they're just starting out with AI
stuff, we don't want to, like, overwhelm them with all the technical, you know,
jargon and complexity. We focus on quick wins first. That's been our approach.
```

**Synthesis output:**
```
Client Engagement Principles:
- Adapt approach to client's current AI maturity level
- Early-stage clients: prioritize quick wins, minimize technical complexity
- Avoid overwhelming clients with jargon
```

**NOT this (wrong — preserves conversational structure):**
```
The team mentioned that they "really try to meet clients where they are" and
believe in not "overwhelming them with technical jargon." They noted that
"quick wins" are prioritized for clients "just starting out with AI."
```

The wrong example is useless to an LLM agent — it's just transcription with quotation marks. The correct example provides actionable guidance.

**The test:** Would an LLM agent reading your synthesis be able to make decisions? Or would it be confused by conversational artifacts?

### Converting Time Spans to Dates

Time spans become outdated the moment the calendar changes. Always convert relative time references to absolute dates or years.

**Wrong (becomes outdated):**
- "25 years of experience"
- "Founded over two decades ago"
- "We've been doing this for 15 years"
- "A 10-year track record"

**Right (remains accurate):**
- "Founded in 1999" or "Working in industry since 1999"
- "Founded in 2003"
- "Operating since 2009"
- "Track record from 2014 to present"

**When you can't determine the exact date:**
- If the source says "25 years" and was written in 2024, calculate: "since 1999" or "founded approximately 1999"
- If the source date is unknown, flag for clarification rather than guessing
- Mark calculated dates: "Founded approximately 1999 [calculated from '25 years' in 2024 source]"

**Why this matters:** A module stating "25 years of experience" is wrong by year 2 and increasingly wrong thereafter. "Since 1999" remains accurate indefinitely.

### Avoiding Volatile Specifics

Time spans are one type of volatile detail, but not the only one. Never include details in **modules** whose accuracy depends on a point-in-time snapshot. Instead, move volatile data to an **addendum** (see "Addenda" under Module Hierarchy) and reference it from the module:

- **Counts of things that change** — number of skills, team members, clients, courses, partners
- **Specific prices, rates, or fee structures** → move to a pricing addendum
- **Named lists of tools, skills, or platforms** that are actively evolving
- **Enrollment, participation, or growth numbers**
- **Biographical details** that will be updated → move to a biographical addendum

**Wrong (volatile data embedded in module):**
- "13 skills on GitHub"
- "Retainers at $3,500/mo and $6,000/mo"
- "Team of 5 certified consultants"

**Right (module references addendum):**
- "The skills library is actively developed and publicly available on GitHub"
- "For current retainer pricing, see addenda/pricing-and-rates.md"
- "The consulting team includes certified practitioners at multiple levels"

**The test:** If this number or list changed tomorrow, would the module be wrong? If yes, move the data to an addendum and reference it. The volatile data still gets built — it lives in `addenda/`, not in `modules/`.

### Volatile Specifics vs. Durable Process Parameters

Not all numbers are volatile. The volatile specifics rule targets **snapshot data** — values that change as the business evolves. It does NOT target **process parameters** — operational thresholds, timelines, and criteria that define how work gets done.

**Volatile (exclude — these expire):**
- "13 skills on GitHub" — count changes weekly
- "Retainers at $3,500/mo" — pricing changes quarterly
- "5 certified consultants" — headcount changes with hiring

**Durable (include — these are behavioral guidance):**
- "Escalate unresponsive clients within 2 business days" — process parameter
- "Engagements under $10K use a PSA; over $10K use an MSA" — decision threshold
- "Allow 2-week buffer between discovery and proposal" — timeline guidance
- "Review cycles run on 30/60/90 day intervals" — operational rhythm

**The distinction:** Would this change because the business *grew or evolved* (volatile), or would it only change if the organization *redesigned its processes* (durable)? Process parameters are behavioral instructions — they tell the agent how to advise. Filtering them out strips the module of the decision logic it exists to provide.

When you encounter a number during self-check, ask: "Is this a price, count, or enrollment figure? Or is this a threshold, timeline, or criterion that defines how work is done?" Only filter the former.

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

### Focused, Not Monolithic

Use-based organization does not mean "put everything an agent might need into one large module." Each module should serve a **single, clear decision-making context.** When a module starts absorbing content from multiple unrelated source areas just because they're all "relevant," it is becoming monolithic.

**Signals a module needs splitting:**
- It covers multiple distinct decision-making contexts (e.g., both "how to qualify a prospect" and "how to structure an engagement")
- It exceeds ~4,000 tokens and is still growing
- Content from shared sources is being duplicated because it "fits" in multiple modules
- The module's Purpose statement requires "and" to describe what it does

**The principle:** More specific, non-duplicative modules with clear cross-references are better than fewer monolithic modules that attempt to be comprehensive. An agent loading three focused 2,000-token modules has better context than one loading a single 6,000-token module that covers too much ground. The cross-references between focused modules create structure that helps the agent navigate, while monolithic modules create a wall of text that degrades retrieval quality.

### Guiding, Not Cataloging

Modules can drift into cataloging existing content — listing all courses, enumerating all services, inventorying all tools — instead of providing creation and decision guidance. This is especially dangerous when a skill or tool can discover existing content on its own.

**Wrong (catalog — tells the agent what exists):**
```markdown
## Training Programs
Program 1: Fundamentals (6 sessions, conceptual)
Program 2: Applied Skills (7 sessions, hands-on exercises)
Program 3: Advanced Integration (7 sessions, progressive complexity)
...
```

**Right (guide — tells the agent how to create):**
```markdown
## Program Design Principles
When designing a new program:
- Structure around progressive complexity: each session builds on the prior one
- Include a practical exercise in every session, not just presentation
- Start with conceptual framing, then move to applied practice, then integration

Programs should be reusable across client cohorts with minimal customization.
```

**The test:** If the organization added a new program tomorrow, would this module need updating? If yes, you've cataloged instead of guided. The agent can look things up — the module should teach it how to think.

### Response Patterns Are Not Catalogs

A specific case of the catalog vs. guide distinction: **competitive objection handling** and **recurring scenario responses** are behavioral guidance, not competitor inventories. When a source document describes how to respond to a specific, recurring situation ("the prospect says they already have AI through their CRM"), that's an "If X, do Y" pattern — exactly what modules exist to provide.

**Wrong (filters out a response pattern because it mentions a competitor category):**
```markdown
For competitive positioning, see S1: Client & Market Context.
```

**Right (encodes the behavioral response):**
```markdown
When a prospect says "we already have AI through our CRM/platform":
- Acknowledge what they have — don't dismiss embedded AI features
- Distinguish between embedded AI (vendor-configured, limited to one tool) and custom implementation (organization-configured, cross-functional)
- Frame the gap: "What can your team do with AI that your CRM vendor didn't anticipate?"
```

**The test:** Is this a list of competitors (catalog), or a response framework for a recurring conversation (behavioral guidance)? If it follows an "If the prospect says X, respond by Y" pattern, it belongs in the module.

### Respecting Scope Boundaries

The proposal defines what content belongs in each module and what content is designated as addenda or out-of-scope. When writing a module, the proposal's scope boundary is authoritative — not the availability of information in source files.

When you re-read sources (Step 2b in PHASE_5_BUILD.md), you encounter ALL information in those files — including content the proposal explicitly assigned elsewhere. The temptation is to include "relevant" verified facts because they're right there. Resist this.

**The rule:** If the proposal assigns content to addenda or to a different module, do NOT include it in the module you're writing. Reference it instead.

**Wrong (scope leak):**
```markdown
## Leadership
### Jane Smith
Born 1978 in Denver. Attended State University (1996-2000).
Worked in management consulting for 12 years before founding...
```

**Right (scope boundary respected):**
```markdown
## Leadership
Jane Smith (CEO) leads strategy and client relationships.
Alex Chen (CTO) leads product development and technical delivery.

For detailed founder backgrounds, see addenda/founder-bios.md.
```

The fact that biographical information is verified and available does not mean it belongs in the organizational identity module. A module about organizational identity should reference founder bios, not contain them.

### Scope Proximity Is Not Scope Assignment

A common over-filtering error: content that appears *near* addenda content in a source file gets excluded along with it. The scope boundary test is whether the **proposal assigned** the content elsewhere — not whether it shares a paragraph or section with excluded content.

**Example:** A source document discusses proposal-building methodology in the same section as specific pricing. The pricing is addenda. The methodology ("present mixed pricing models," "structure proposals around phased delivery") is behavioral guidance that belongs in the module.

**Wrong (over-filters by proximity):**
```markdown
For proposal structure and pricing, see addenda/pricing-and-rates.md.
```

**Right (separates the behavioral guidance from the excluded data):**
```markdown
When structuring proposals:
- Present mixed pricing models (fixed-fee phases + retainer options) to give clients flexibility
- Structure around phased delivery so clients can evaluate before committing to full scope
- For specific pricing tiers and rate cards, see addenda/pricing-and-rates.md
```

**The test:** Does the proposal assign THIS specific content to addenda? Or does it only assign the data point (the price, the rate, the dollar amount) while the surrounding methodology is in-scope? Exclude the data, keep the guidance.

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

### Addenda (Reference Data)

Addenda are the volatile counterpart to durable modules. They contain reference data that agents consult on demand — not behavioral instructions that shape how agents think.

| Component | Contains | Changes When | Loaded | Token Budget |
|-----------|----------|-------------|--------|-------------|
| **Modules** | Metaprompting — behavioral instructions, decision frameworks, "If X, do Y" logic | Processes are redesigned | Always (per agent definition) | Counts against per-agent limit (10% of model context window) |
| **Addenda** | Data — pricing tables, rate cards, biographical details, service catalogs, inventories | Business evolves (prices change, people join, services added) | On demand (when a module directs the agent to consult) | Does not count against limit |

**The classification test:**
1. Does the agent need this to *decide how to behave* (module) or to *look up specific data* (addendum)?
2. Would this change because processes were redesigned (module) or because the business evolved (addendum)?
3. Is this a behavioral instruction or a reference fact?

**The relationship rule:** Modules reference addenda; addenda don't reference modules. A module says `See addenda/pricing-and-rates.md for current rates.` The addendum contains the rates — no behavioral instructions, no agent guidance, no decision logic.

**Examples from practice:**
- Pricing tables, billing rates, retainer packages → addendum
- "When structuring proposals, present mixed pricing models" → module (behavioral guidance *about* pricing)
- Founder biographical timelines, career histories → addendum
- "When referencing the founder, emphasize the technology-to-consulting through-line" → module (behavioral guidance *about* biography)
- Service catalogs, current offerings, team roster → addendum
- "Match service tier to client AI maturity" → module (decision logic *about* services)

**Addenda are proposed in Phase 4, built in Phase 5, and validated in Phase 7** — alongside modules, with equivalent source verification but without the metaprompting transformation test.

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

**Operationalizing this rule:** The proposal's Shared Source Ownership table assigns each content area from shared sources to exactly one module. During the build, before writing any module, check this table and the completed modules that share sources. If content is already owned by another module, cross-reference it — do not restate it, even in different words.

**The duplication test:** If two modules contain the same underlying fact — even with different phrasing or different behavioral instructions built on top — that is duplication. The fact belongs in one module. Other modules reference it and add their own behavioral layer on top of the reference.

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

**Build-time markers:** During construction, use `[PROPOSED]` for inferences and `[HIGH-STAKES]` for content requiring exact-copy verification. These markers are removed before delivery — they enforce discipline during the build but don't appear in the finished library. The finished module's language should make epistemic status legible naturally.

If you cannot point to where a fact appears in working sources, either:
1. Remove it, or
2. Mark it `[PROPOSED]` during the build (only if user has approved including inferences) — then rewrite to make the inferential status clear in the language itself when removing the marker

**Superseded information:** If newer documents override older ones, use the newer information. Do not include outdated content — it wastes tokens and confuses agents.

## Write-Time Source Protocol

Modules must be written with sources open, not from memory.

**The problem:** Reading many files creates blurred impressions. By writing time, the agent "remembers" facts incorrectly but writes them with confidence.

**The solution:** Re-read specific sources immediately before writing each module, in the same context turn.

**Required process:**
1. Identify which source files inform this module (from proposal)
2. Read those files (even if read earlier)
3. Write the module with sources visible
4. For HIGH-STAKES content (legal entity, EIN, addresses, titles, credentials): copy exact text

**What counts as HIGH-STAKES (must be copied exactly):**
- Legal entity names and structure
- EIN, tax status, formation details
- Email addresses, phone numbers, physical addresses
- Leadership titles
- Dates (founding, milestones)
- Financial figures
- Credentials and certifications

**Verification log format:**

Every module draft should include (can be removed in final):

```markdown
<!-- VERIFICATION
| Fact | Source | Exact Text |
|------|--------|------------|
| California LLC | Organization Information.md | "Entity Type: California Limited Liability Company" |
-->
```

## Token Budget Management

**Guideline**: The module budget per agent is **10% of the target model's context window** (e.g., 20K tokens for a 200K-context model like Claude Sonnet). This limit scales automatically as models gain larger context windows. Addenda do not count against this budget — they are loaded on demand. The goal is not to minimize tokens — it's to include all useful verified content.

**DO NOT artificially compress content to "save tokens."** If the content is verified and helps the agent make better decisions, include it.

**What counts as waste (cut this):**
- Preambles and introductions
- Filler phrases
- Explaining concepts Claude already knows
- Duplicated content across modules
- General industry knowledge (not org-specific)

**What counts as useful content (keep this):**
- Verified facts from sources
- Decision frameworks and criteria
- Organizational context and positioning
- Specific details that inform agent behavior
- Examples that clarify how to apply principles

**The right size is determined by content, not a target number.** Some agents need more context than others. Include what's useful; cut what's wasteful. Don't compress useful content to hit an arbitrary token count.

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

**Illustrative examples as prescriptions:** A case study showing *one way* something was done shouldn't become *the way* it must be done. This extends to lists of categories, sectors, types, or use cases — always frame them as non-exhaustive illustrations of breadth, and state the actual qualification or selection criteria separately.

**Wrong (list becomes a restriction):**
```
Client sectors: Healthcare, Education, Environmental, Arts, Social Services
```

**Right (list illustrates breadth, criteria are separate):**
```
The organization serves any mission-driven organization meeting the qualification criteria in S1.
Past work spans healthcare, education, environmental, arts, and social services
sectors — these illustrate breadth, not boundaries.
```

**The test:** If someone from a sector NOT on this list matched the qualification criteria, would this module make the agent hesitate to engage? If yes, the framing is too restrictive.

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

1. **During the build, mark high-stakes content with `[HIGH-STAKES]`** to enforce exact-copy discipline. This marker is removed before delivery — the finished module relies on the foundation guardrail's process gates for verification behavior rather than inline markers.

2. **Source requirements by stakes level:**
   - HIGH: Must be verifiable in working sources; copy exact text during build
   - MEDIUM: Should be verifiable; `[PROPOSED]` acceptable during build if clearly marked
   - LOW: `[PROPOSED]` acceptable during build based on pattern inference

3. **In finished modules:** High-stakes content is identified by the foundation guardrail's condition test (significant irreversible harm + accuracy depends on verified organizational specifics), not by inline markers. The agent's process gates handle verification behavior at runtime.

## Standard Guardrail Modules

Every context library includes two standard guardrail modules, copied from `templates/guardrails/` during Phase 4:

### F_agent_behavioral_standards (Foundation)

**All agents load this module.** It defines behavioral standards as upstream process gates — steps that make certain failure modes architecturally difficult rather than naming them and monitoring for them:
- Source-before-statement gate (grounds all claims in provided context)
- Epistemic calibration gate (language signals the status of each claim without prescribed markers)
- Reframe-before-committing gate (interrupts first-framing momentum)
- Second-order check gate (surfaces unintended consequences)
- HIGH-STAKES condition test (two conditions: irreversible harm + organizational-specific accuracy)
- Professional challenge (accuracy over agreement)

### S_natural_prose_standards (Shared)

**External-facing agents load this module.** It defines:
- Banned AI-detectable vocabulary (pivotal, crucial, delve, leverage, etc.)
- Banned syntactic patterns (parallelisms, copula avoidance, vague attribution)
- Required writing behaviors (simple verbs, noun repetition, specificity)
- Context-specific guidance by content type
- Revision checklist

### When to Load Each Module

| Agent Type | F_agent_behavioral_standards | S_natural_prose_standards |
|------------|------------------------------|---------------------------|
| Marketing/communications | Required | Required |
| Content creation | Required | Required |
| Internal documentation | Required | Skip |
| Research/analysis | Required | Skip (unless published) |

**Do not write custom guardrail sections in agent definitions.** Load the standard modules and add only domain-specific extensions if needed.

## Session Architecture

The context library build process runs across multiple sessions. This is by design — the process is too long for a single context window, and auto-compaction destroys critical instructions and facts.

### Why Sessions Exist

When Claude Code's auto-compact triggers during a build:
- **Skill instructions vanish** — critical rules (never invent, re-read sources, transform don't transcribe) are lost; the agent reverts to default summarize/paraphrase behavior
- **Specific facts blur** — titles, names, dates read from source files get reconstructed from memory, producing confident wrong information
- **Classification decisions are lost** — already-clean documents get re-synthesized, losing nuance

### How the Architecture Prevents This

1. **Phase-specific instruction files** in `references/phases/` — the agent reads only the phase file it needs, when it needs it. Each file is self-contained with its own critical rules block.

2. **Embedded rules in data files** — source-index.md, proposal.md, and module templates contain embedded rules as redundant safety nets. Even after full compaction, when the agent reads source-index.md to figure out what to do next, it encounters the rules.

3. **Build state tracking** — `build-state.md` in the output directory records current phase, completed work, user decisions, and a pointer to which phase instruction file to read next. Any new session reads this first.

### Session Groupings

| Session | Phases | Why Together |
|---------|--------|-------------|
| A | 1 (Index) + 2 (Synthesize) | Short phases, naturally sequential, low compaction risk |
| B | 3 (Analyze) + 4 (Propose) | Analysis feeds directly into proposal, moderate length |
| **MANDATORY BREAK** | | **Always start a new session before Phase 5** |
| C | 5 (Build) | Longest phase, highest risk — one module at a time with re-read protocol |
| D | 6-7 (Agents + Validate) | Short phases, use completed modules as input |

Sessions A and B may combine if compaction hasn't occurred. **The boundary between B and C is mandatory.** Phase 5 needs a full context window — the metaprompting transformation rules must be fresh when writing modules, not buried under thousands of tokens of prior conversation. Without this, the agent reverts to copying content instead of creating metaprompts.

### How to Resume From Any Point

1. Read `<OUTPUT_PATH>/build-state.md` — it tells you the current phase and what's done
2. Read the phase instruction file it points to
3. Continue from where work left off

If `build-state.md` doesn't exist but `source-index.md` does, determine the current phase from the index status and create `build-state.md` to track progress going forward.

### Build State File

The `build-state.md` file (template in `templates/build-state.md`) tracks:
- Current phase and sub-step
- Phase completion status for all 7 phases
- Module build checklist (for Phase 5 — the longest phase)
- User decisions log (conflicts resolved, gaps accepted, scope changes)
- Pointer to current phase instruction file
- Session history (optional, for debugging)
