# Phase 5: Build Modules & Addenda

> **CRITICAL RULES — Read these first, even if you read nothing else:**
> - Re-read working sources IN THE SAME TURN you write each module or addendum. NEVER write from memory.
> - Modules are METAPROMPTS — they tell agents how to behave, not just what facts exist.
> - Addenda are DATA — they provide reference information that modules point to.
> - NEVER invent details. If it's not in the working sources, it's not in the output.
> - HIGH-STAKES content (legal names, EINs, addresses, titles, dates, financials): copy EXACTLY.
> - One module or addendum at a time. Complete and verify each before starting the next.
> - Update build-state.md after completing each module or addendum.

---

## What This Phase Does

Build every module and addendum listed in the approved proposal. This is the longest and highest-risk phase. Each module and addendum is an independent unit of work — if context is lost mid-build, read build-state.md to see which are done and continue from there.

## Before You Start

1. **Read `<OUTPUT_PATH>/build-state.md`** — check which modules are already complete.
2. **Read `<OUTPUT_PATH>/proposal.md`** — this is your build plan. Note the embedded rules comment block.
3. **Read `<OUTPUT_PATH>/source-index.md`** — this tells you which working sources to use.
4. **Read [references/ARCHITECTURE.md](../ARCHITECTURE.md)** — module design philosophy, content transformation rules, token management.

---

## Content vs. Context vs. Metaprompting

This is the most important concept in module building. Source documents contain **content** (raw facts). Modules must deliver **context** and **metaprompting** (processed knowledge that shapes agent behavior).

| Level | What It Is | Example |
|-------|-----------|---------|
| **Content** (wrong) | Raw facts copied from sources | "Organization has 50 employees. Headquarters in Denver. Offers three service tiers." |
| **Context** (minimum) | Processed knowledge shaping behavior | "Team size is less important than expertise depth. When clients ask about capacity, frame it around specialized skill areas, not headcount. Headcount changes; expertise positioning doesn't." |
| **Metaprompting** (target) | Instructions for how the agent thinks | "If a prospect asks 'how big is your team,' respond with expertise areas first, then note the team is sized to maintain senior-level attention on every engagement. Never lead with a number that will be outdated next quarter." |

### The Transformation Test

For each section you write, ask:

1. **Does this change how the agent behaves?** If yes → good (context/metaprompting). If no → you've just listed facts (content).
2. **Could the agent act on this without further interpretation?** If yes → good. If the agent would need to figure out *what to do with* the information → transform it.
3. **Does this read like a Wikipedia article or like an agent system prompt?** It should read like the latter.

### Common Content-to-Metaprompt Transformations

| Source content | Bad module (content) | Good module (metaprompting) |
|---------------|---------------------|----------------------------|
| "We offer workshops, coaching, and consulting" | "Services: workshops, coaching, consulting" | "When a prospect describes their challenge, recommend the format that fits their learning style and timeline — workshops for teams needing shared vocabulary, coaching for leaders needing personal support, consulting for organizations needing structural change. Don't list all three; match one." |
| "Our team includes 5 certified consultants" | "Team: 5 certified consultants" | "When clients ask about team credentials, emphasize the certification count only if relevant to the engagement. For technical proposals, lead with specific expertise areas rather than headcount." |
| "We've been in business for 12 years" | "History: 12 years in business" | "Tenure signals stability but isn't a differentiator. When prospects ask about experience, anchor on outcomes delivered — years in business is context, not a selling point. Lead with what you've done, not how long you've existed." |

---

## Folder Structure

Create if not already present:

```
<OUTPUT_PATH>/
├── source-index.md
├── build-state.md
├── synthesis/
├── proposal.md
├── analysis.md
├── modules/
│   ├── foundation/
│   ├── shared/
│   └── specialized/
├── addenda/
└── agents/
```

---

## Step 1: Copy Standard Guardrail Modules

Before building organization-specific modules:

1. Copy `<skill_dir>/templates/guardrails/F_agent_behavioral_standards.md` → `<OUTPUT_PATH>/modules/foundation/`
2. Copy `<skill_dir>/templates/guardrails/S_natural_prose_standards.md` → `<OUTPUT_PATH>/modules/shared/`
3. Update the module IDs and dates in the copied files
4. Customize organization-specific cross-references

These modules are **required** — do not skip or significantly modify them.

---

## Step 2: Build Modules One at a Time

For EACH module in the proposal, follow this exact sequence:

### 2a. Identify Sources

Consult the source index. For this module:
- Which files have status `ready`? → use originals
- Which files have status `synthesized`? → use the synthesis file path in Working Source column

### 2a.5. Re-Read Architecture and Phase Rules (MANDATORY)

**Read [references/ARCHITECTURE.md](../ARCHITECTURE.md) NOW** — specifically the "Single Source of Truth" and "Content Transformation" sections. Also re-read the "Content vs. Context vs. Metaprompting" section at the top of this file.

This step runs for EVERY module. Do not skip it because you believe you remember the rules. After context compaction, your understanding of module design rules degrades to generic summarization behavior — but you will not know compaction occurred. Re-reading takes seconds; writing a module from degraded rules takes a rollback.

### 2b. Re-Read Sources (MANDATORY)

**Read the working sources for this module NOW.** Even if you read them before. Even if you think you remember. Read them again in this turn.

This is not optional. After context compaction, your "memory" of file contents is unreliable. The source file is the truth.

### 2b.5. Check Completed Modules for Overlap (MANDATORY)

Before writing this module, **read the completed modules that share any source files with this one.** Consult the proposal's Shared Source Ownership table (or, if that table doesn't exist, check which modules list overlapping Key Sources in the proposal tables).

For each overlapping module, note what content it already covers. When you encounter that content in sources during writing:
- **Do not restate it.** Use a cross-reference: `See [Module Name] for [topic].`
- If you need the same underlying fact for a different behavioral instruction, state the instruction without restating the fact: `Building on the [topic] framework in [Module Name], when [specific context], [specific instruction].`

This step prevents the most common duplication pattern: two modules that share a source file both transforming the same content into behavioral instructions. Shared source files are the highest risk — if this module and another both use the same source, duplication is almost certain unless you check.

### 2c. Re-Read Metaprompting Rules (MANDATORY)

Before writing, re-read the "Content vs. Context vs. Metaprompting" section at the top of this file. If context compaction has occurred, that section may no longer be in your working memory. Re-reading it takes 30 seconds and prevents the most common failure mode: writing content instead of metaprompting.

If you cannot see the section above, here is the minimum you need:

> **Modules are system prompts, not fact sheets.** Every section must tell agents how to BEHAVE, not just list information. The transformation test: (1) Does this change agent behavior? (2) Could the agent act on it without interpretation? (3) Does it read like a system prompt, not a Wikipedia article?
>
> BAD: "The organization offers Advisory, Implementation, and Managed services."
> GOOD: "When recommending services, match to client AI maturity: Advisory for early-stage, Implementation for committed adopters, Managed for ongoing support."

### 2d. Write the Module

Write with sources fresh in context. Use the module template from [references/TEMPLATES.md](../TEMPLATES.md).

**While writing, maintain a verification log.** This log is a build artifact — it ensures every fact is sourced during writing but **must be removed from the final module** before Phase 5 is complete. Agents don't need it; it wastes tokens and can cause instruction conflicts.

```markdown
<!-- VERIFICATION LOG
| Fact | Source File | Exact Source Text |
|------|-------------|-------------------|
| [fact in module] | [filename] | [exact quote from source] |
-->
```

**Before writing, re-read this module's scope from the proposal.** Note what is explicitly out-of-scope or designated as addenda. If you encounter that content in sources, reference it — do not include it.

**Module writing principles:**

- **Be a metaprompt, not a fact sheet.** Every section should tell agents how to behave, not just list information. Ask: "Given this fact, what should the agent DO differently?"
- **Front-load behavioral instructions.** Start sections with what the agent should do, then provide supporting context.
- **Encode decision criteria as "If X, do Y" patterns.** Agents need decision logic, not descriptions.
- **State facts directly** — no preambles, introductions, or "In order to..."
- **Use consistent terminology** throughout all modules
- **Don't explain concepts Claude already knows** — focus on organization-specific knowledge
- **Guide, don't catalog.** Teach the agent how to create and decide, not what currently exists. If a skill or tool can discover existing content, focus on creation principles instead.
- **Avoid volatile specifics.** Don't embed counts, prices, or named lists that will change. Move this data to an addendum and reference it from the module instead.
- **Question the obvious behavioral instruction.** The first metaprompt transformation you think of may not be the best one. "12 years in business" → "Mention tenure in proposals" is mechanical. A better transformation considers *when* tenure matters (credibility with cautious buyers) and when it doesn't (innovation-focused prospects). If you can write a more useful behavioral instruction by considering how the agent will actually encounter this information, do so.
- **Trace second-order effects of behavioral instructions.** A foundation-level instruction shapes every agent that loads the module. Consider: does this instruction serve all the agents that will receive it, or does it help some while constraining others? If a content writer needs to frame organizational history differently than a proposal developer, the instruction belongs in specialized modules, not foundation.
- **Stay focused — don't build monoliths.** A module serves one clear decision-making context. If you're absorbing content from many source areas because it all seems "relevant," the module is becoming monolithic. Three focused 2,000-token modules with cross-references serve agents better than one 6,000-token module covering too much ground. If the module's purpose requires "and" to describe, consider splitting.

**Prompt design principles — modules ARE prompts:**

Modules are system prompts for domain agents. The behavioral guidance you write will shape how those agents process information. Structure that guidance as upstream process requirements, not named prohibitions.

- **Structure as process gates, not failure monitors.** Instead of naming a failure mode and telling the agent to watch for it, require an upstream step that makes the failure architecturally difficult. "Never hallucinate" monitors for a named failure. "Before stating a claim, locate its source in your context modules" requires a step that prevents the failure from occurring. Write the second kind.
- **Let language carry epistemic status.** Don't prescribe bracket markers or labeling conventions for agents to use in their output. Instead, write instructions that require the agent's language itself to make clear whether something is sourced, inferred, or the agent's reasoning. "Mark inferences with [Inferred]" is a formatting rule that can be followed mechanically. "The reader should always be able to tell whether they're receiving a sourced claim, a logical extension, or your analysis — because your language makes the distinction legible" is an epistemic discipline.
- **Define high-stakes by condition, not category.** Don't list categories of high-stakes content (legal names, dates, financials). Instead, define the two conditions that make content high-stakes: an error would cause significant harm that's difficult to undo, AND accuracy depends on organizational specifics requiring verified sourcing. This lets agents correctly identify high-stakes content the list didn't anticipate.
- **Challenge before agreement.** Write agent instructions that prioritize accuracy over agreeability. Frame this as a process requirement — "When a request contradicts documented strategy, cite the contradiction and offer an alternative" — not as a personality trait ("Be honest and direct").
- **Don't duplicate the guardrail module's job.** F_agent_behavioral_standards already defines process gates for sourcing, epistemic calibration, reframing, and second-order effects. Domain modules should extend those gates to their specific context, not restate them. If a module needs to say "verify partner names," frame it as "the Source Before Statement gate applies with particular importance to partner names — verify against [specific addendum]."

**What to include:**
- All verified facts from working sources relevant to this module's purpose
- Decision frameworks and behavioral instructions
- Cross-references to other modules: `See [Module Name] for [specific info]`
- `[HIGH-STAKES]` markers on content requiring exact-copy verification (build-time artifact — removed before delivery)
- `[PROPOSED]` markers on user-approved inferences (build-time artifact — removed before delivery)

**What to exclude:**
- Verbatim quotes from sources
- General knowledge not specific to the organization
- Content that belongs in another module (reference instead)
- Duplicated information

### 2e. Self-Check: Module Quality

Before moving on, read what you just wrote and check these nine points:

**Metaprompting checks:**
1. **Pick any section.** Does it tell the agent what to DO, or does it just state what IS? If the latter, rewrite it.
2. **Look for "The organization..." sentences.** Each one should have a corresponding "When X, do Y" instruction. If it doesn't, add one or cut the sentence.
3. **Look for human-directed language.** Phrases like "It's important to understand..." or "Think of it this way..." are written for humans, not LLM agents. Rewrite as direct instructions.
4. **Look for the agent talking about itself.** If the module tells the agent to "use AI" or "ask AI," that's confused — the agent IS the AI. Rewrite to describe the workflow from the agent's perspective.

**Durability checks:**
5. **Look for numbers, prices, or named lists that will change.** Each one should be moved to an addendum rather than embedded in the module. "13 skills on GitHub" expires tomorrow — "the skills library is publicly available on GitHub" doesn't. If the data belongs in a proposed addendum, reference it: "See addenda/[name].md for current [data]." **Exception:** Process parameters (escalation timelines, budget thresholds, review cycles) are durable behavioral guidance, not volatile data — keep them. Ask: would this change because the business *grew* (volatile) or because it *redesigned its processes* (durable)?
6. **Look for inventories or catalogs** (lists of existing courses, tools, clients, projects). Ask: does the agent need this list, or does it need the principles for creating/selecting from such lists? If a skill or tool can discover the current inventory, focus on creation guidance instead. **But don't confuse response patterns with catalogs:** "If a prospect says X, respond by Y" is behavioral guidance, even if X references a competitor category. Objection-handling frameworks belong in modules.
7. **Check the module scope from the proposal.** Does any section contain content that was designated as addenda or assigned to a different module? If so, replace with a cross-reference. **But watch for proximity over-filtering:** content that appears *near* addenda content in a source file is not automatically out of scope. The test is whether the *proposal* assigned it elsewhere, not whether it shares a paragraph with excluded data. Methodology guidance near pricing data is still methodology.
8. **Look for lists of categories, sectors, or types.** Are they framed as exhaustive or illustrative? Do they state qualification criteria, or does the list itself function as the criteria? If someone from a category NOT on the list matched the criteria, would the agent hesitate?

**Cross-module duplication check:**
9. **Scan completed modules that share sources with this one.** Does any section substantially repeat content already in another module? If so, replace the duplicate with a cross-reference. Restating the same fact with different phrasing is still duplication. The test: if you updated this fact, would you need to update it in two modules? If yes, it should only exist in one.

If more than 2 checks fail, the module needs rework. Re-read the relevant rules and rewrite before proceeding.

### 2f. Verify Sources

After writing, run:
```bash
python3 <skill_dir>/scripts/verify_module.py <module_path> <SOURCE_PATH>
```

If any facts are flagged as unverified:
1. Check the working sources
2. Either find the source and confirm, or remove the fact
3. Do not proceed to next module until verification passes

### 2g. Clean Up and Update Build State

After completing and verifying each module:
1. **Remove build-time artifacts** from this module now:
   - Delete the `<!-- VERIFICATION LOG ... -->` HTML comment block
   - Remove all `[HIGH-STAKES]` markers (the exact-copy discipline they enforced is already baked into the text)
   - Remove all `[PROPOSED]` markers (rewrite the surrounding language so the epistemic status is clear without the marker — e.g., "Based on patterns in the source material..." rather than a bracket tag)
   Do not defer cleanup to end-of-phase — context loss causes deferred cleanup to be forgotten.
2. Update `<OUTPUT_PATH>/build-state.md`:
   - Mark the module as `complete` in the module checklist
   - Note any issues or user decisions needed

---

## Step 3: Build Addenda

After all modules are complete, build the addenda listed in the proposal. Addenda are **data, not metaprompting** — this is the one place where stating facts directly ("The hourly rate is $250") is correct.

### Why Addenda Come Last

Modules must be written first because they define the cross-references. A module says "for current pricing, see addenda/pricing-and-rates.md" — that reference must exist before you build the addendum it points to. Building in this order also ensures you know exactly what data each addendum needs to contain.

### For EACH Addendum in the Proposal

#### 3a. Identify Sources

Same as modules: consult the source index, use `ready` originals or `synthesized` working sources.

#### 3b. Re-Read Sources (MANDATORY)

Same rule as modules. Read the working sources for this addendum NOW.

#### 3c. Write the Addendum

Write with sources fresh in context. Use the addendum template from [references/TEMPLATES.md](../TEMPLATES.md).

**Addenda writing principles:**

- **State data directly.** This is reference material, not metaprompting. "The Advisory tier is $15,000/month" is correct here.
- **Organize for lookup.** Structure data so agents can find specific values quickly — tables, clear headings, logical grouping.
- **HIGH-STAKES protocol still applies.** Exact pricing, legal details, biographical dates — copy character-by-character from working sources.
- **No behavioral instructions.** If you're writing "When X, do Y" — that belongs in a module, not an addendum.
- **Include source attribution.** Every data point must trace to a working source.
- **Prose addenda need prose quality.** Some addenda contain content that agents will surface to external audiences — founder bios, organizational descriptions, about-us text. These are still data (not metaprompting), but they need to read like a human practitioner wrote them. Apply the practitioner voice gate from S_natural_prose_standards: identify who would write this, adopt their perspective, test each sentence. A founder bio that reads like an AI-generated LinkedIn summary undermines the same credibility the context library is designed to protect.

**While writing, maintain a verification log** (same format as modules). This log **must be removed from the final addendum** before Phase 5 is complete.

```markdown
<!-- VERIFICATION LOG
| Fact | Source File | Exact Source Text |
|------|-------------|-------------------|
| [data point] | [filename] | [exact quote from source] |
-->
```

#### 3d. Self-Check: Addenda Quality

Before moving on, check these five points:

1. **Does this contain only data, not behavioral instructions?** If any section tells agents how to behave ("When clients ask about pricing, respond by..."), move that guidance to the appropriate module.
2. **Is every data point verified against working sources?** Check the verification log. No gaps.
3. **Is the update frequency realistic?** Would this need updating quarterly, annually, or on-demand? Does the frontmatter reflect that?
4. **Does at least one module reference this addendum?** Search completed modules for cross-references to this addendum. Orphaned addenda shouldn't exist — if no module points to it, either add a reference or question whether the addendum is needed.
5. **If this addendum contains prose that agents will surface externally** (bios, descriptions, about-us text): does it pass the practitioner voice test? Would a human in this role write it this way? If it sounds like AI-generated copy, rewrite from the practitioner's perspective.

#### 3e. Verify Sources

Same as modules — run the verification script:
```bash
python3 <skill_dir>/scripts/verify_module.py <addendum_path> <SOURCE_PATH>
```

#### 3f. Clean Up and Update Build State

After completing each addendum:
1. **Remove build-time artifacts** from this addendum now:
   - Delete the `<!-- VERIFICATION LOG ... -->` block
   - Remove all `[HIGH-STAKES]` markers (addenda contain data, not behavioral instructions — the exact-copy discipline is already baked in)
2. Update `<OUTPUT_PATH>/build-state.md`:
   - Mark the addendum as `complete` in the addenda checklist
   - Note any issues or user decisions needed

---

## Build Order

1. **Foundation modules first** — these provide context shared across agents
2. **Shared modules next** — these build on foundation context
3. **Specialized modules last** — these add domain-specific depth
4. **Addenda last** — these contain the data that modules reference

---

## HIGH-STAKES Content Protocol

For content classified as HIGH-STAKES (legal names, EINs, tax status, addresses, titles, dates, financials, credentials):

1. **Find the exact text in the working source**
2. **Copy it character-by-character** — do not paraphrase
3. **Mark it `[HIGH-STAKES]`** during writing (this marker is removed before delivery — it ensures exact-copy discipline during the build)
4. **Log it in the verification table** with the exact source text

If you cannot find the exact text in a working source, do NOT include it. Even if you "remember" it. Especially if you "remember" it.

---

## After All Modules and Addenda Are Complete

1. **Confirm all build-time artifacts are removed.** Each module's verification log, `[HIGH-STAKES]` markers, and `[PROPOSED]` markers should have been removed in Step 2g/3f. Scan all modules and addenda for any remaining artifacts and remove them.
2. Update source index status to `building` → `complete`
3. Update build-state.md: Phase 5 status → `complete`
4. Set next phase file → `references/phases/PHASE_6_7_AGENTS_VALIDATE.md`

No gate after Phase 5 — continue to Phase 6-7 for agent definitions and validation.

---

## After This Phase

Read [PHASE_6_7_AGENTS_VALIDATE.md](PHASE_6_7_AGENTS_VALIDATE.md) to create agent definitions and validate.

**Session break point:** After Phase 5, build-state.md tracks which modules are complete. A new session reads build-state.md, then this phase file, and continues from the next incomplete module. Each module is independent — no context from previous modules is needed beyond what's in the proposal and working sources.

**Compaction warning:** Within a single Phase 5 session, context compaction is invisible — you will not know it happened. The per-module protocol (Steps 2a through 2g) is designed to be run unconditionally for every module precisely because compaction cannot be detected. If you find yourself thinking "I already know these rules, I can skip the re-reads," that is the post-compaction failure mode this protocol prevents.
