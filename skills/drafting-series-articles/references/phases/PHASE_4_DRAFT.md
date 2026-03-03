# Phase 4: Draft

> **CRITICAL RULES — Read these first:**
> - **Read the project CLAUDE.md FIRST.** Find the drafting bootstrap section. Load every Context file it specifies, in the order it specifies. These are your behavioral standards, prose standards, ethical framework, content methodology, and voice profile. **Do not proceed without them.** The skill declares a dependency on these modules — if they are not loaded, the guardrails below have nothing to reference.
> - Read the article plan (`Drafts/article-[N]-plan.md`) before starting. It contains orientation, comprehension findings, and the structural plan from previous sessions. The structural plan is the primary input for drafting — it tells you what each section DOES, not just what it's about.
> - Re-read the voice profile NOW. You are adopting a role — writing as this person, not about them.
> - Re-read [references/ARCHITECTURE.md](../ARCHITECTURE.md) NOW — Evidence Reasoning, Writing From a Voice Profile, and Narrative Construction sections.
> - Re-read research documents for each section before writing that section. Do not write from memory.
> - Do not load any file from an `Archive/` directory.
>
> **GUARDRAILS THAT SURVIVE ROLE ADOPTION — these apply to every sentence, including calibration:**
> - **F0 Process Gate 1 (Source Before Statement):** Before writing any claim or narrative detail, locate its source in the research documents. If you cannot locate it, you cannot write it — your output for that detail is nothing. This applies to narrative details (days of the week, settings, feelings, sequences of events) exactly as it applies to empirical claims. The per-section protocol enforces this through step 4 (identify available narrative material) — that inventory is exhaustive. Do not add to it during generation.
> - **F0 Process Gate 2 (Mark the Move):** The reader must be able to tell whether they're receiving a sourced finding, an extension of sourced material, or original analysis — from the language itself.
> - **Natural prose standards:** Apply your loaded prose standards throughout.
> - Role adoption means writing *as* the person. It does not mean relaxing the process gates. The gates are upstream sequence requirements — complete them before generating, not prohibitions to remember during generating.

---

## What This Phase Does

Write the article using the structural plan from Comprehend — structural question, article movement, per-section necessity and structural roles. The voice profile determines how sentences are built, how evidence lands, and how the reader is addressed. The structural plan determines what each section DOES — what it changes in the reader's understanding and why it's necessary.

**This is the highest-risk phase.** Voice profile fidelity and evidence curation degrade with context consumption. The mandatory session break before this phase exists to ensure these instructions are fresh.

---

## Before You Start

1. **Read the project CLAUDE.md** — find the drafting bootstrap section. It specifies Context files and their loading order. **Load every file it lists, in the order it lists them.** These include behavioral standards, prose standards, ethical framework, content methodology, and voice profile. The loading order is project-specific — follow it exactly.
2. **Read `Drafts/article-[N]-plan.md`** — review orientation (story, arc, thread, section structure), comprehension findings (what the evidence earns, connections, narrative), and the **structural plan** (structural question, article movement, per-section argument structures). The per-section argument structures are the primary input for drafting — each section has a reader entry point, an argument statement, a numbered argument sequence showing how the section builds its claim move by move, and a closing handoff. Draft from these sequences.
3. **Read [references/ARCHITECTURE.md](../ARCHITECTURE.md)** — the full file.
4. **Re-read the audience document** — for this specific article's position in the series build.
5. **Complete the Voice Calibration** below before writing any article prose.

---

## Loading GATE

**REQUIRED before Voice Calibration.** Write to the process log:
- "Context library loaded from project CLAUDE.md: [list each module loaded, in order]."
- "Article plan read: [filename]."
- "ARCHITECTURE.md read: yes."
- "Audience document read: [filename]."

---

<phase_calibration>
## Voice Calibration

**REQUIRED before drafting begins.** The voice profile is a role adoption document. It describes a person — not a style. Do not scan it for features to reproduce. Read it for the person.

### Step 1: Adopt the role

Re-read the voice profile. Do not look for key features — look for a role. Answer these questions in the process log:

- **Who is this person?** What is their relationship to the subject matter? Where does their authority come from — what have they built, managed, lived through?
- **How do they think?** When they encounter a new problem, what do they do first? When they disagree, how does the disagreement arrive?
- **What do they care about?** Not the topic of this article — what matters to them as a person working in this space?
- **What context applies?** Given the audience document, which of the voice profile's contextual adaptations fits this article's reader?

### Step 2: Confirm the role is active

Read the Orient section of the article plan — specifically the story question and the emotional arc. Then state, in 1–2 sentences, how this person would approach telling this story to this audience. Not what they'd say — how they'd approach it. What mode would they lead with? What would they care about getting right?

This is a comprehension check, not a writing exercise. Do not draft article content here.

**GATE:** Write to the process log:
- "Role: [1–2 sentences — who this person is and where their authority comes from]"
- "Approach: [1–2 sentences — how this person would tell this story to this audience]"
- "Contextual adaptation: [which adaptation from the voice profile applies]"
- "Leading mode: [conclusion-first / working-through]"
</phase_calibration>

---

<phase_drafting>
## Drafting Process

The draft follows the story, not the outline. The structural plan from Comprehend determines what each section does and why it's necessary. The article has a movement — a direction the reader travels — and each section advances that movement.

### Per-Section Protocol

For EACH section in the structure:

**1. Re-read the relevant research.** Identify which research documents inform this section (from the plan's evidence map). Read them now, even if read before.

**2. Review this section's argument structure.** Read the structural plan entry for this section: the argument it makes, the argument sequence (numbered steps with structural annotations), and the closing handoff. The argument sequence is the blueprint — it shows how the section builds its claim, move by move. Draft from the sequence, not from the topic.

**3. Use the reader entry point from the structural plan.** The plan specifies where the reader enters each section — what they know, believe, or have just experienced. Draft the section from that entry point.

**4. Select evidence.** The structural plan's argument sequence identifies which evidence carries each move. Those findings get prose treatment. Everything else: hyperlink only.

**5. Identify available narrative material.** Before writing, locate in the research documents any first-person accounts, specific experiences, described moments, or personal details that belong in this section. List them. These are the only narrative details available. If a sentence would require inventing a detail not in the research — a day of the week, a setting, a feeling, a sequence of events — that detail does not exist and cannot be written. This is F0 Process Gate 1 applied to narrative: locate the source before stating the claim. If you cannot locate it, you cannot state it.

**6. Write from the role.** Write as the person described in the voice profile — from inside their perspective, not about their topics. The narrative material from step 5 is your inventory. Do not add to it during generation. After writing each section, test: read the first and last paragraphs. Does this sound like the person, or like an AI writing about that person's field? Use Gates 2, 3, and 4 as diagnostic tests — if any gate fails, the role has slipped. Do not insert missing features. Return to the role and regenerate the section.

**7. Layer, don't linearize.** Recognition → evidence → understanding. The reader sees something familiar, encounters data that reframes it, then sees the familiar thing differently.

**8. Follow dense evidence with connection.** After presenting findings, connect them to the reader's experience. Evidence then recognition.

**9. Close with the closing handoff from the structural plan.** The handoff is the implicit question that makes the next section necessary. The transition is the question, not a bridge phrase.

**10. Check the frame.** Does the article's opening frame (person, event, question) remain present in this section? If it has disappeared, the article has shifted from story to report. Bring the frame back before moving to the next section.

### Opening — the role test

The opening section is where role adoption succeeds or fails. After writing the opening, test it before continuing:
- Read the opening paragraphs. Could any competent writer on this topic have written them? If yes, the role isn't active. Return to the voice profile, re-read the role (not the features), and regenerate.
- Use Gates 2, 3, and 4 as diagnostics — but the primary question is "does this sound like a specific person?" not "does this match a list?"

Connect to the reader's search intent within the first two paragraphs. Start with the interesting part.

### Closing

Close with a question that applies the article's frame to the reader's own situation. The question must genuinely require thought.

### Hyperlinking

Every sourced finding gets an inline hyperlink using URLs from the research base. Describe the finding, link the source.

---

## Output

Write the draft to: `Drafts/[article-number]-[short-title]-draft-[date].md`

Include a YAML header:

```yaml
---
article: [number]
title: [title]
series_position: [position in series]
keyword_targets: [list]
date: YYYY-MM-DD
---
```

---

## GATE

Write to the process log:
- "Draft written to: [filepath]"
- "Word count: [approximate]"
- "Structural question answered: [yes/no — does every section advance the structural question?]"
- "Article movement achieved: [yes/no — does the draft move the reader in the direction described in the structural plan?]"
- "Frame persistence: [yes/no — does the opening frame remain present throughout, or does it disappear?]"
- "Necessity test: [yes/no — could any section be removed without breaking comprehension of later sections?]"
- "Voice profile fidelity: [assessment — where did it hold, where did it slip?]"

**LOG:** Record drafting decisions in compressed form — one line per decision or self-correction. Focus on: where the story diverged from the plan, where evidence didn't fit, where the voice slipped and was corrected. Do not restate the structural plan or describe what each section covers — that's in the article plan. The log records what happened during drafting that the plan didn't anticipate.

---

## STOP

Present to the user:
- The draft filepath
- A brief assessment: whether the article moves as a whole (structural question, movement, frame persistence) or has slipped into section-by-section arrangement
- Any sections where evidence didn't support the intended claim
- Any places where the voice slipped and was corrected during drafting
- The closing question — does it work?

Ask the user to read the draft. The user may want to:
- **Confirm** — proceed to editorial cycle
- **Redirect** — change approach, restructure (returns to Orient or Comprehend)
- **Provide specific feedback** — incorporated into editorial cycle

Do not proceed until the user responds.
</phase_drafting>

---

## After This Phase

Update the article plan:
- Mark Phase 4 checkbox complete
- **Current phase:** Phase 5-6-7 (Editorial + Quality + Present)
- **Next phase file:** `references/phases/PHASE_5_6_7_EDITORIAL_QUALITY_PRESENT.md`

**Tell the user:** "The draft is saved. To continue with editorial revision, you can continue in this session or start a new one. Say 'Resume drafting Article [N]' to continue."

Sessions C and D may combine if context permits and the draft was not exceptionally long.
