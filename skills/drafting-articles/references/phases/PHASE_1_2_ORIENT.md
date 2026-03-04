# Phase 1-2: Orient

> **CRITICAL RULES — Read these first:**
> - Read the project manifest (`project-manifest.md`) before anything else. It contains file paths for all project components. If no manifest exists, ask the user for: research files, voice profile path, writing standards preference, audience description, and output directory.
> - Do not load any file from an `Archive/` directory. Archived files are deprecated.
> - Apply the Source Before Statement gate to every empirical claim.
> - This phase produces a durable planning document. The next session reads it cold.
> - **Voice profile and writing standards are NOT loaded in this phase** (except a brief scan for generative mode). They load at Draft time to stay fresh in context.

---

## What This Phase Does

Read the project manifest, load research context (Phase 1), and establish the article's narrative positioning (Phase 2). The output is an article plan document that enables the next session to begin comprehension without re-loading everything.

---

<phase_bootstrap>
## Phase 1: Read Manifest and Load Research

**REQUIRED:** Read the project manifest first. If no manifest exists, gather the minimum from the user and note it in the article plan.

**Start the process log** — create `Drafts/article-[N]-process-log.md` with the article number, title, and date.

From the manifest, load in this order:

**1. Article context:**
- Series map (if series article) — locate the specific article section for thesis, argument arc, misconception to reframe, keyword targets, and series build position
- Article brief (if single article) — thesis, argument arc, research-to-load
- Audience document — who the reader is
- Core thesis/framework document (if provided) — the structural argument the article serves

**2. Research:**
- Research index (if provided) — read the evidence map to identify which research documents serve this article
- Load documents marked as **primary evidence** for this article's thesis elements
- Load **supporting evidence** documents relevant to the argument arc
- **Background context** documents: load only if comprehension identifies a specific need

**3. Voice profile — mode scan only:**
- Read the voice profile briefly to identify which generative modes are available and which might lead for this article. **Do not adopt the role.** Full role adoption happens in the Draft phase. Note the leading mode for Orient's section structure work.

**LOG:** Record what was loaded in compressed form — file names, primary/supporting designation, and any gaps. One line per document, or a grouped list. Target: under 15 lines for the entire loading record.

**GATE:** Write to the process log:
- "Article: [number and title]"
- "Manifest: [filepath, or 'none — setup gathered from user']"
- "Research documents loaded: [list by short name, noting primary vs. supporting]"
- "Article outline section reviewed: [yes/no]"
- "Keyword targets: [list primary and gap terms, or 'none provided']"
- "Voice profile scanned for mode selection: [leading mode]"

**STOP.** Present to the user:
- Which article is being drafted
- What was loaded (listed by name)
- Any loading gaps — documents referenced but not found
- Any ambiguities — if the article maps to more than one possibility

Do not proceed until the user confirms.
</phase_bootstrap>

---

<phase_orient>
## Phase 2: Orient

Orient establishes the article's narrative positioning — not its content parameters. The shift matters: Orient asks story questions, not fill-in-the-blank questions.

**Read [references/ARCHITECTURE.md](../ARCHITECTURE.md) now** — specifically the Narrative Construction and Reader Entry Points sections.

### Story Questions

Work through these in order. Each builds on the previous.

**The story question:** What happened — or what is happening — that this article makes visible? Not "what is the thesis" but "what's the story that earns the thesis?"

**The emotional arc:** Where is the reader at the beginning — emotionally, not informationally? What do they feel? What do they believe? Where are they at the end? What shifted?

**The single thread:** What is the one narrative thread connecting the evidence? One sentence. If the evidence doesn't connect along a single thread, the article will read as a data arrangement.

**From the audience document:** Re-read for this specific article. Where is the reader in the series build (if series)? What register applies? What does search behavior tell you about what they need?

**From keyword research (if available):** What did the reader search for? The opening must connect to search intent within the first two paragraphs.

**From the voice profile mode scan:** Which generative mode leads? Where does the article shift between modes? (This informs section structure but does not require full role adoption.)

### Section Structure

After the story is clear, determine section structure based on the story, the emotional arc, and the single thread — not based on the evidence loading order or the outline's sequence.

For each section, identify:
- Purpose (what it does for the argument)
- Key evidence (2–3 findings that carry the structural claim)
- Reader entry point ("The reader already knows from their own work that...")

### Connection Check

**Before committing to a structure:** Generate at least one alternative structure. Write both in the log. Name what each gains and what it loses. Choose — and log why.

**LOG:** This phase should produce substantial log entries — but substance means reasoning, not length. Write the story question work (including alternative framings and why one was chosen), the emotional arc, and the alternative structure tradeoffs. The reasoning is the value. Do not restate evidence or document summaries — those exist in the plan and the source files.

**Process log format for all phases:** The log is read by the agent in later sessions and by the user for review. Write for an LLM reader — compressed, structured, no restatement of source material. What belongs: reasoning, decisions, self-corrections, surprises, questions for the author. What doesn't belong: summaries of research documents, loading inventories that duplicate the plan, or second copies of plan content.

**GATE:** Write to the process log:
- "The story: [one paragraph]"
- "Emotional arc: reader starts [X], ends [Y]"
- "The single thread: [one sentence]"
- "Search entry point: [what they searched for]"
- "Generative mode: [from voice profile mode scan]"
- "Section structure: [list sections with brief description]"
- "Alternative structure considered: [what, why rejected]"
- "Additional research needed: [list, or 'none']"

### Create the Article Plan

Using the template at [templates/article-plan.md](../../templates/article-plan.md), create `Drafts/article-[N]-plan.md`. Populate the Bootstrap Summary and Orientation sections from the gate outputs above.

**STOP.** Present to the user:
- The story — what this article makes visible
- The emotional arc — where the reader starts and ends
- The single thread — one sentence
- The proposed section structure and the alternative considered, with tradeoffs
- Any places where the outline's argument arc doesn't match what the evidence supports
- Any additional research that would strengthen the article

This is the highest-value interaction point. The user can redirect the entire approach before any drafting begins. Ask whether this orientation is right, or whether they see a different story in the evidence.
</phase_orient>

---

## After This Phase

Update the article plan's phase status and set:
- **Current phase:** Phase 3 (Comprehend)
- **Next phase file:** `references/phases/PHASE_3_COMPREHEND.md`

**Tell the user:** "The article plan is saved at `Drafts/article-[N]-plan.md`. To continue, start a new session and say 'Resume drafting Article [N].' I'll read the plan and begin comprehension."

Sessions A and B may combine if context permits. If continuing in the same session, read [PHASE_3_COMPREHEND.md](PHASE_3_COMPREHEND.md) before proceeding.
