# Phase 3: Comprehend

> **CRITICAL RULES — Read these first:**
> - Re-read the article plan (`Drafts/article-[N]-plan.md`) before starting. It contains orientation decisions from the previous session.
> - Re-read primary research documents in this session, even if they were read before. Memory blurs; sources don't.
> - Do not load any file from an `Archive/` directory.
> - Apply the Source Before Statement gate to every empirical claim.
> - This phase exists because the agent's default is to load evidence and immediately plan deployment. Comprehension is the counter.

---

## What This Phase Does

The agent reads what it loaded and thinks about it — not to extract content parameters, but to understand what the evidence actually says and how the pieces connect. The outputs are the Comprehension Findings and the **Structural Plan** in the article plan. The structural plan maps comprehension findings into how the article works as a whole — what each section does, why it's necessary, and how the article moves the reader from one understanding to a different one.

---

## Before You Start

1. **Read `Drafts/article-[N]-plan.md`** — confirm orientation decisions. Review the story, emotional arc, single thread, and section structure.
2. **Read [references/ARCHITECTURE.md](../ARCHITECTURE.md)** — specifically the Evidence Reasoning and **Article Structure** sections. (ARCHITECTURE.md also contains a "Voice Profile and Writing Standards" section — those documents load in the Draft phase, not here.)
3. **Re-read the research index** (if provided in the manifest) — identify primary and supporting evidence documents for this article. If no index exists, use the article plan's loaded documents list.

---

<phase_comprehend_research>
## Step 1: Work Through the Research

Read the primary research documents not as sources to mine for citations but as arguments to understand.

For each primary document:
- What is it actually arguing (not just what data it contains)?
- What did the researchers find that surprised them?
- What surprises you?
- Where does it agree or create tension with other loaded documents?

**LOG:** For each primary document, write ONE sentence: the core finding or argument relevant to this article. Do not summarize the document — the agent re-reads the document each session. The log records your conclusion, not a restatement.

---

## Step 2: Find Connections the Outline Doesn't Name

The outline provides an argument arc. The research contains connections the outline hasn't identified — cross-domain parallels, findings that rhyme across different studies, evidence from one domain that illuminates another.

These connections are where the article's most original thinking will come from. The outline can't anticipate them because they emerge from reading, not from planning.

**Apply connection-finding from your behavioral standards:**
- What cross-domain parallels exist in the loaded research? Name at least two, even if they go unused.
- What would a different domain's evidence reveal about this article's central claim?
- What does acting on this article's thesis create that was not intended? What does it make harder? Who bears the cost?

**LOG:** Write each connection as two sentences: what connects, and why it matters for the article. No more than 2-3 sentences per connection.

---

## Step 3: Identify What the Evidence Earns

The outline may propose claims the evidence doesn't fully support. Name these gaps honestly. If the evidence earns a different claim than the one the outline proposes, say so.

**LOG:** Bullet list: what the evidence earns (claim → source) and what it doesn't (outline claim → what's missing). One line per item.

---

## Step 4: Find the Narrative in the Evidence

The evidence itself contains narrative — people who did things, institutions that changed, decisions that had consequences. Find the narrative that's already in the evidence, not a structure imposed on top of data points.

**LOG:** List each narrative element: person/event, source document, which section it serves. One line per element.
</phase_comprehend_research>

---

<phase_comprehend_structure>
## Step 5: Build the Structural Plan

Read [references/ARCHITECTURE.md](../ARCHITECTURE.md) — specifically the **Article Structure** section. Then build a structural plan that maps comprehension findings into how the article works as a whole. The structural plan is not a summary of what each section covers — it is a detailed blueprint of how each section builds its argument, move by move, so the drafting session can execute from it without re-deriving the logic.

**5a. Name the structural question.** One question that every section answers from a different angle. Not the thesis — the question that makes the reader need the thesis. Write it in one sentence.

**5b. Describe the article's movement.** In one phrase, describe the direction the reader moves: from what understanding to what different understanding? (e.g., "from conventional wisdom to new reality," "from specific experience to structural pattern.") If you can't describe the movement in one phrase, the sections are arranged by topic rather than building toward transformation. Return to the comprehension findings and restructure.

**5c. For each section, build the argument structure.** This is the most important output of the Comprehend phase. The drafting session reads this cold and writes from it. A table-level summary of what each section "does" is not sufficient — the draft session needs to see how the argument builds, step by step.

For each section, write:

**Reader entry point** — One sentence: what the reader knows, believes, or has just experienced from the previous section (or from their own work, for Section 1). This is where the section meets the reader.

**The argument this section makes** — One paragraph stating what the section argues — not what it covers or what information it contains, but the claim it builds and why that claim is necessary for the article's movement.

**Argument sequence** — Numbered steps showing how the section builds its claim. Each step has:
- A **bold move name** — what the step does (e.g., "Open with the claim itself," "Name what the convergence reveals")
- A paragraph of detail — what evidence or reasoning carries this move, what the reader encounters, what shifts
- An *italicized annotation* explaining why this move works structurally — why it's in this position, what it sets up, what would break without it

The argument sequence is the section's internal logic made visible. If a step can't explain why it's necessary in its position, it's arrangement, not structure. Each step should build on the previous one — the reader's understanding changes with each move, and the sequence traces that change.

**What a completed step looks like** (showing shape, not content — your steps will be specific to the article's evidence and argument):

> 3. **Name the structural pattern across domains.** The reader has now seen three independent examples. This step names what they share — not as a thesis statement but as a pattern the reader can already see from the evidence. The specific finding from [research document] provides the language; the cross-domain connection from Step 2 provides the structure.
>
>    *This step earns the right to generalize because the reader has already encountered the specific cases. Placing the pattern-naming before the evidence would produce an assertion; placing it after lets the reader arrive at the pattern alongside the article.*

**Closing handoff** — The implicit question this section creates that the next section answers. Not a transition phrase — the question that makes the next section necessary. (The final section creates the closing question the reader carries away.)

**Necessity test** — State what the reader could NOT understand without this section. If the answer is "nothing — they'd just miss supporting evidence," the section doesn't earn its place. Propose cutting it or merging its evidence elsewhere.

**5d. Check the frame.** Does the opening frame (person, event, question) remain present throughout the article, or does it disappear when analysis begins? If it disappears, restructure so the frame persists. Write how the frame stays present in each section.

**LOG:** Write the structural question, the movement, and the per-section argument structures to the process log. (Compressed form — see log format below.)

**Quality check:** If any section's argument sequence has fewer than 3 steps, if any step's annotation can't explain why the move is necessary in that position, if the movement can't be described in one phrase, if the frame disappears — you have arrangement, not structure. Return to the comprehension findings and restructure before proceeding.

---

## Step 6: Update the Article Plan

Populate the **Comprehension Findings** section of `Drafts/article-[N]-plan.md`:

- What the Evidence Earns
- What the Evidence Doesn't Earn
- Connections Found (minimum three entries)
- Surprises
- The Narrative in the Evidence
- Gaps to Flag

Populate the **Structural Plan** section of `Drafts/article-[N]-plan.md`:

- Structural Question (one sentence)
- Article Movement (one phrase)
- Per-Section Argument Structure (for each section: reader entry point, argument paragraph, numbered argument sequence with move names, detail, and structural annotations, closing handoff, necessity test)
- Frame Persistence (how the opening frame stays present in each section)

**Quality check:** If the Connections Found section has fewer than three entries, if there are no surprises, if the narrative is just the outline restated — you have not done the work. Return to the research and read again. If any section fails the necessity test, restructure before proceeding.
</phase_comprehend_structure>

---

## Process Log Format

The process log is read by the agent in later sessions and by the user for review. Write for an LLM reader — compressed, structured, no restatement of source material.

**What belongs in the log:** Reasoning, decisions, self-corrections, connections discovered, surprises, questions for the author.

**What does NOT belong in the log:**
- **Restating what research documents argue.** The agent re-reads the documents each session. The log should note what the agent *concluded* from reading, not summarize what the document says. One sentence per document: the core finding relevant to this article, not a paragraph restating the document's argument.
- **Duplicating the article plan.** Comprehension findings and structural plan entries go in the article plan. The log records the *reasoning* that produced them — what was considered, what was rejected, what surprised — not a second copy of the plan content.
- **Loading inventories.** The Bootstrap loading record in the plan file already lists what was loaded. The log needs only: "Loaded [N] documents. Gaps: [list or none]."

**Target compression:** The full log for a 4-section article through Comprehend should be under 150 lines. If it's longer, the log is restating rather than reasoning.

---

## GATE

Write to the process log:
- "The evidence earns: [what claims the research supports]"
- "The evidence doesn't earn: [what the outline proposes that isn't supported]"
- "Connections found: [list]"
- "Surprises: [list]"
- "The narrative in the evidence: [where the story lives]"
- "Gaps to flag: [list]"
- "Structural question: [one sentence]"
- "Article movement: [one phrase]"
- "Per-section argument structures: [for each section — argument statement (one sentence), number of sequence steps, closing handoff (one sentence)]"

---

## STOP

Present to the user:
- What the evidence earns and doesn't — especially where outline claims aren't supported
- The most important connections found between documents or domains
- Surprises — findings that challenged the initial framing
- Where the narrative lives — specific people, events, decisions
- Gaps — what's missing, what would strengthen the argument
- **The structural plan** — the structural question, the article's movement, and for each section: the argument it makes, the sequence of moves that build the argument (with structural annotations), and the closing handoff to the next section

Ask: Do these connections and this reading match your understanding? Does the structural plan — the argument sequences, the movement between sections, the closing handoffs — match how you see the argument building? The drafting session will execute from these argument sequences, so they need to be right. Is there context you have that would change emphasis? Are the gaps acceptable, or do they need addressing before drafting?

Do not proceed until the user confirms or provides additional direction.

---

## After This Phase

Update the article plan:
- Mark Phase 3 checkbox complete
- **Current phase:** Phase 4 (Draft)
- **Next phase file:** `references/phases/PHASE_4_DRAFT.md`

**Tell the user:** "The article plan is updated with comprehension findings. **Start a new session before drafting** — the draft session needs a full context window for voice profile generation to work. Say 'Resume drafting Article [N]' to continue."

The boundary between comprehension and drafting is **mandatory**. Always start a new session before Phase 4.
