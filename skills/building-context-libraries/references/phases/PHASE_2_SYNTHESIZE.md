# Phase 2: Synthesize Complex Sources

> **CRITICAL RULES — Read these first, even if you read nothing else:**
> - NEVER synthesize a file with status `ready`. It's already clean — use it directly.
> - NEVER re-synthesize a file with status `synthesized`. Read the existing synthesis instead.
> - NEVER invent details. Every fact must come from the source file you're synthesizing.
> - NEVER copy quotes. Extract the *meaning* and state it directly.
> - Synthesis is for RAW DATA with speech artifacts. Structured documents are used directly.
> - Complete and update the index for EACH file before starting the next. No batching.

---

## What This Phase Does

Transform messy source material (transcripts, interviews, raw notes) into clean working documents that LLM agents can act on. Only files that genuinely need synthesis get synthesized.

## Before You Start

1. **Read `<OUTPUT_PATH>/source-index.md`** — this is your working checklist.
2. **Read `<OUTPUT_PATH>/build-state.md`** — check what's already done.
3. **Check for existing synthesis files** in `<OUTPUT_PATH>/synthesis/` — if they exist, read them instead of re-synthesizing.

---

## Source Classification: Three Categories

### Category A: MUST Synthesize

These files need synthesis — they contain raw, unprocessed content:

- Raw audio/video transcripts with speech artifacts (um, uh, you know)
- Unstructured notes with no headers or organization
- PDFs/CSVs/raw data that need conversion to structured markdown
- Interview transcripts in Q&A format with conversational speech

**How to identify:** Read the file. If it contains filler words, false starts, conversational rambling, verbatim quotes mixed with speech artifacts, or completely unstructured content — it needs synthesis.

### Category B: NEVER Synthesize

These files are already usable — do NOT synthesize them:

- Files with "synthesis" in the name (already processed)
- Clean structured documents with headers, lists, and organized sections
- Published articles, case studies, strategic documents
- Files the indexing script classified as `ready` (verify by reading)
- Operational documents with clear formatting

**How to identify:** Read the file. If it has clear structure, no speech artifacts, and an LLM agent could use it directly — mark it `ready` and move on.

### Category C: EVALUATE Then Decide

These files need human judgment:

- Files the indexing script classified as `needs-synthesis` but might be clean
- Notes that are partially structured
- Documents with some conversational elements but mostly organized content

**How to handle:**
1. Read the file
2. Check: Does this content need transformation for an LLM agent to use it?
3. If YES → synthesize (Category A treatment)
4. If NO → update status to `ready` in the index, note "reviewed — already clean"

---

## How to Synthesize (Only for Category A Files)

For each file that genuinely needs synthesis:

### 1. Read the source file

Re-read it even if you read it in Phase 1. Do not work from memory.

### 2. Create the synthesis file

Save to: `<OUTPUT_PATH>/synthesis/[filename]-synthesis.md`

```markdown
# Synthesis: [Original Filename]

**Source:** [path to original file]
**Generated:** YYYY-MM-DD
**Status:** draft

---

## [Topic Area]

[Clear prose stating facts extracted from the source.
Direct statements, not attributions. "X is true" not "John said X."]

## [Topic Area]

[Additional content organized by topic, not by speaker or chronology.]

---

## Flagged for Clarification

- [Ambiguous statement needing user input]
- [Unclear reference needing verification]

---
```

### 3. Update the source index immediately

- Change status from `needs-synthesis` to `synthesized`
- Add the synthesis path to the "Working Source" column
- Do NOT start the next file until this update is complete

### 4. Present to user for review

Show each synthesis to the user before moving on.

---

## What Synthesis IS and IS NOT

**Synthesis IS:**
- Extracting the *meaning* from messy source material
- Stating facts in clean, direct prose
- Organizing information by topic
- Creating content an LLM agent can act on
- Preserving exact names, dates, and figures from the source

**Synthesis is NOT:**
- Copying quotes with "they said X"
- Preserving conversational structure
- Including filler words, false starts, or rambling
- Transcription with light editing
- Summarizing (you're transforming, not compressing)

### Example — WRONG (transcription):
```
John mentioned that "we've always tried to, you know, meet clients where they are"
and emphasized that the team believes in "starting with quick wins."
```

### Example — RIGHT (synthesis):
```
Client Engagement Approach:
- Adapt to client's current state and capabilities
- Start with quick wins before complex implementations
- Avoid overwhelming clients with technical jargon
```

The first example is useless to an LLM agent. The second is actionable guidance.

---

## Synthesis Rules

- One synthesis per source file — do not combine multiple sources
- Extract facts, decisions, principles — never copy quotes
- Preserve exact names, dates, figures from the source
- Flag ambiguities — don't interpret them
- Organize by topic, not by speaker or document order
- **Test:** Would an LLM agent find this synthesis useful, or confusing?

---

## After All Syntheses Are Complete

1. Update source index: all synthesized files show status `synthesized` with working source paths
2. Update build-state.md: Phase 2 status → `complete (pending approval)`
3. Set next phase file → `references/phases/PHASE_3_ANALYZE.md`

## Gate: User Approval Required

Before requesting approval, write:
- "Synthesis complete: [N] files synthesized, [N] files already clean (skipped)"
- "All synthesis files saved to: [list paths]"
- "Source index updated with working source paths"

**STOP. Get user approval on ALL syntheses before proceeding.**

After approval, update build-state.md: Phase 2 status → `complete`.

---

## After This Phase

Read [PHASE_3_ANALYZE.md](PHASE_3_ANALYZE.md) to begin analysis.

**Session break point:** After Phase 2, the source index, syntheses, and build-state.md can be used to resume in a new session. A new session should read build-state.md first, then the next phase file.
