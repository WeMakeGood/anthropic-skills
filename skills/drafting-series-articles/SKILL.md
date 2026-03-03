---
name: drafting-series-articles
description: Drafts research-grounded long-form articles within a series across multiple sessions. Bootstraps from project CLAUDE.md, loads voice profile and research, then drafts with comprehension, editorial revision, and quality gates. Use when drafting, writing, resuming, or working on an article for a series, or when the user says draft article, resume drafting, or references an article by number or title.
---

# Drafting Series Articles

<purpose>
Claude's default when drafting long-form content is to load evidence and fill in an outline —
producing competent prose organized by the plan rather than by the argument's own logic. This
skill counters that default through three mechanisms: a comprehension phase (think before
planning), a mandatory process log (track reasoning and self-corrections), and an iterative
editorial cycle (revise structurally, not just cosmetically).

The skill runs across multiple sessions because article drafting exceeds a single context
window. Loading research, reasoning through evidence, drafting, and revising all compete for
context. The session architecture ensures the critical instructions for each phase are fresh
when they matter — especially the voice profile and quality standards during drafting.
</purpose>

## Critical Rules

**CONTEXT LIBRARY DEPENDENCY:** This skill requires context library modules — behavioral standards, natural prose standards, ethical framework, content methodology, and voice profile. The project CLAUDE.md specifies which modules to load and in what order. **Sessions C (Draft) and D (Editorial) start cold** — the context library must be reloaded from the project CLAUDE.md's drafting bootstrap section at the start of each session. The phase instruction files enforce this through loading gates. If the modules are not loaded, the guardrails in this skill have nothing to reference.

**ARCHIVE EXCLUSION:** Never read, load, or reference any file from an `Archive/` directory. Archive directories contain deprecated documents. Loading archived material anchors the agent on previous output. This rule is absolute.

**SOURCING:** Every empirical claim must trace to a specific research document. Describe the finding and hyperlink to the source using URLs from the research base. Do not use academic author-name citation style.

**EPISTEMIC CALIBRATION:** Apply the epistemic calibration gate from your behavioral standards throughout — the reader must always be able to tell whether they're receiving a sourced finding, an extension of sourced material, or the article's original analysis, from the language itself.

**GENRE:** The audience document defines register. Before writing each section, select the 2–3 findings that carry the structural argument — those get prose treatment. Everything else is available for hyperlinking only.

**PROFESSIONAL CHALLENGE:** If evidence doesn't support the outline's claims, if a section structure doesn't serve the story, or if the user's direction contradicts what the research supports — name the problem and propose an alternative. The outline is a plan, not a mandate.

**PROSE ADDRESS:** Do not assign the reader an identity or position. Present structural analysis; let the reader locate themselves. Do not self-reference the article or reference the project's internal process using internal vocabulary.

**ANTI-SYCOPHANCY:** Do not tell the user the draft is good. Present the draft and name its weaknesses. The user decides what works.

---

## Project Structure Convention

This skill reads all project-specific details from the project's CLAUDE.md. The skill provides the drafting *process*; the project provides the *content, voice, and standards*.

**Required — the project CLAUDE.md must reference or contain:**

| Component | What it provides |
|-----------|-----------------|
| **Series outline / map** | Per-article thesis, argument arc, misconception, keyword targets, series build position |
| **Audience document** | Who the reader is, register/genre conventions, search behavior |
| **Thesis / framework document** | The structural argument the series serves |
| **Research index** | Evidence map organized by relevance to each article |
| **Research directory** | Actual research documents with source URLs |
| **Voice profile** | How the author writes — generative process gates |
| **Drafts directory** | Where drafts and process logs are saved |

**Optional:** Organizational identity, brand/communication guide, content methodology, keyword/SEO research.

The CLAUDE.md is the single source of truth. It names files and locations. This skill reads from it rather than maintaining its own file index.

---

## Quick Start

Tell the agent which article to work on — by number, title, or description. The agent will read the project CLAUDE.md, determine the current phase, and begin or resume.

Example triggers:
- "Draft Article 3"
- "Let's work on the healthcare article"
- "Resume drafting where we left off"

---

## Interaction Model

**GATE** — a self-check. The agent writes a commitment statement to the process log before proceeding. Gates do not require user input.

**STOP** — a user interaction point. The agent presents its work and waits for the user to respond before proceeding. The agent never proceeds past a STOP without user input.

Every phase ends with a GATE followed by a STOP. Without stops, the agent runs all phases in a single pass, producing a draft built on unchecked assumptions.

---

## Session Architecture

The drafting process runs across multiple sessions. Each phase has a dedicated instruction file in `references/phases/`.

| Session | Phases | Instruction File | Description |
|---------|--------|------------------|-------------|
| A | Bootstrap + Orient | [PHASE_1_2_BOOTSTRAP_ORIENT.md](references/phases/PHASE_1_2_BOOTSTRAP_ORIENT.md) | Load context, find the story |
| B | Comprehend | [PHASE_3_COMPREHEND.md](references/phases/PHASE_3_COMPREHEND.md) | Think through the evidence |
| C | Draft | [PHASE_4_DRAFT.md](references/phases/PHASE_4_DRAFT.md) | Write the article |
| D | Editorial + Quality + Present | [PHASE_5_6_7_EDITORIAL_QUALITY_PRESENT.md](references/phases/PHASE_5_6_7_EDITORIAL_QUALITY_PRESENT.md) | Revise, check, deliver |

**Before starting any phase:** Read the phase instruction file. It contains all procedures and gates for that phase.

### Session Groupings

| Session | Phases | Why Together |
|---------|--------|-------------|
| A | Bootstrap + Orient | Both are read-heavy; Orient needs loaded context fresh |
| B | Comprehend | Deepest analytical work; needs full window focused on research |
| **MANDATORY BREAK** | | **Always start a new session before Session C** |
| C | Draft | Writing needs voice profile and quality standards fresh in context |
| D | Editorial + Quality + Present | All revision-focused, operating on the draft artifact |

Sessions A and B may combine if context permits. **The boundary between B and C is mandatory** — the draft session needs a full context window for the voice profile's generative process gates to work.

---

## Starting a New Article

1. **Read the project CLAUDE.md** — it contains loading order and file references.
2. **Read the Phase 1-2 instruction file:** [references/phases/PHASE_1_2_BOOTSTRAP_ORIENT.md](references/phases/PHASE_1_2_BOOTSTRAP_ORIENT.md)
3. **Begin Phase 1.**

## Resuming a Draft

If `Drafts/article-[N]-plan.md` exists:

1. **Read `article-[N]-plan.md`** — it tells you the current phase and what's done.
2. **Read the phase instruction file** for the current phase.
3. **If a phase checkbox is marked but the next phase hasn't started,** confirm with the user: "It looks like [phase] was completed. Ready to begin [next phase]?"
4. **Continue from where work left off.**

---

## The Process Log

A running document the agent writes throughout every phase, saved to `Drafts/article-[N]-process-log.md`. Started at the beginning of Phase 1, updated continuously.

**What goes in:** Reasoning, surprises, connections discovered, self-corrections, editorial notes, questions for the author.

**What it's for:** The log serves the agent's own process. During editorial revision, the agent rereads its log to see patterns in its own mistakes. The log is also a first-class output — presented to the author alongside the draft.

---

## Reference Files

| File | Purpose |
|------|---------|
| [references/ARCHITECTURE.md](references/ARCHITECTURE.md) | Evidence reasoning, voice generation, narrative construction |
| [references/phases/PHASE_1_2_BOOTSTRAP_ORIENT.md](references/phases/PHASE_1_2_BOOTSTRAP_ORIENT.md) | Bootstrap + Orient instructions |
| [references/phases/PHASE_3_COMPREHEND.md](references/phases/PHASE_3_COMPREHEND.md) | Comprehend instructions |
| [references/phases/PHASE_4_DRAFT.md](references/phases/PHASE_4_DRAFT.md) | Draft instructions |
| [references/phases/PHASE_5_6_7_EDITORIAL_QUALITY_PRESENT.md](references/phases/PHASE_5_6_7_EDITORIAL_QUALITY_PRESENT.md) | Editorial + Quality + Present instructions |
| [templates/article-plan.md](templates/article-plan.md) | Article planning document template |

---

<failed_attempts>
## What DOESN'T Work

- **Running all phases in one context window.** Context compaction silently degrades voice profile instructions, quality standards, and evidence curation rules. The draft reverts to default LLM prose. The session architecture exists to prevent this.

- **Feature-matching the voice profile instead of adopting the role.** The voice profile describes a person, not a style. The agent's default is to scan for features (short sentences, action verbs, dry humor) and reproduce them — which produces prose that performs style traits without inhabiting the person. The fix is not better feature-matching. It is understanding who the person is and writing as them. The gates are diagnostic tests that confirm the role is active, not checklists to execute.

- **Dropping guardrails during role adoption.** When told to "write as this person," the agent fabricates narrative details (days of the week, settings, feelings) to make the voice feel lived-in. Restating the guardrail as a prohibition ("do not fabricate") doesn't fix this — prohibitions don't interrupt narrative generation. The fix is the per-section protocol's narrative inventory step: before writing, list the narrative details that exist in the research documents. That inventory is exhaustive. During generation, write from the inventory, not from imagination. This is F0 Process Gate 1 (locate before stating) applied as an upstream sequence requirement rather than a named failure mode to monitor.

- **Treating editorial as text editing rather than voice-checked structural revision.** The editorial phase's default failure is to find surface-level issues (word swaps, link fixes, reference corrections) while leaving the voice and argument structure unexamined. Every editorial round must start with a voice fidelity check against the actual voice profile document — not against a memory of what the draft should sound like.

- **Treating the outline as a template to fill.** The draft must feel like someone thinking through the evidence. If a section feels like it's executing the outline rather than reasoning through the evidence, the drafting mode has slipped.

- **Drafting sections as adjacent containers rather than parts of a single structure.** The agent's default is to treat each section as a self-contained unit organized by topic — producing sections that feel distinct without a common through-line. The fix is the structural plan from Comprehend: before drafting, build per-section argument sequences — not summaries of what each section covers, but numbered steps showing how each section builds its claim, with structural annotations explaining why each move is necessary in its position. The structural plan is the primary input for drafting. If it reads as a table of topics, the draft will read as a sequence of topic sections.

- **Producing table-level structural plans instead of argument sequences.** When asked to build a structural plan, the agent's default is a high-level summary: what each section covers, why it's necessary, what findings it uses. This produces a plan that describes the article but doesn't enable drafting. The fix is the per-section argument structure: reader entry point, argument statement, numbered argument sequence (each step with a bold move name, a detail paragraph, and an italicized structural annotation), and closing handoff. The structural plan must be detailed enough that a different session can draft from it without re-deriving the argument logic.

- **Delivering conclusions before the evidence earns them.** The reader arrives at the conclusion through the evidence. The thesis sentence from the outline is where the article *arrives*, not where it starts.

- **Skipping comprehension.** Loading documents and immediately planning sections produces an article organized by what was loaded, not by what it means.

- **Single-pass drafting.** The initial draft is never the best version. The editorial cycle is where the argument actually gets built.

- **Loading archived drafts.** Loading a previous draft anchors the agent on that draft's structure and phrasing. Draft from the research, the outline, and the voice profile — never from a previous draft.

- **Skipping context library loading in cold-start sessions.** Sessions C and D start without the context library in memory. The agent's default is to jump to the task (drafting or editing) without loading the behavioral standards, prose standards, and voice profile that the guardrails reference. The result: guardrails fire but have nothing to enforce against — "apply your loaded prose standards" means nothing if no prose standards are loaded. The project CLAUDE.md specifies the loading order. Follow it.

- **Skipping STOPs.** The agent's default is to execute all phases without stopping. This produces a draft built on unchecked assumptions the user can only reject or accept wholesale. In autonomous execution environments (Claude Code with broad tool permissions), nothing forces a pause at STOP points — the agent has momentum and continues. The user must monitor and interrupt, or run with per-tool approval that naturally creates interaction points.

- **Softening the evidence.** "Approximately," "many," "significant" soften specificity into generality. Use the actual numbers from the research.

- **Embedding all evidence instead of curating.** Select 2–3 findings per section that carry the structural argument. Hyperlink the rest. Curation is pacing.

- **Verbose process logs that consume context window.** The agent's default is to restate research document contents in the process log (paragraph-length summaries of what each document argues), duplicate the article plan's loading record, and write comprehension findings to both the log and the plan. The result: a 400+ line log that wastes context tokens in later sessions. The fix: the log records reasoning, decisions, and self-corrections — not summaries of source material. One sentence per document (the core finding relevant to this article), one-line loading records, no duplication of plan content. The log exists for what the plan doesn't capture: the process of getting there.
</failed_attempts>
