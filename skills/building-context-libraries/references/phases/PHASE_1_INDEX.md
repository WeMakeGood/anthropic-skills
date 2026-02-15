# Phase 1: Create Source Index

> **CRITICAL RULES — Read these first, even if you read nothing else:**
> - NEVER invent details. Use exact names, dates, locations from sources.
> - NEVER fill gaps. Missing information is a gap to report, not a blank to fill.
> - NEVER skip source documents. Read every file in the source index.
> - Update the source index after reading EVERY file. Do not batch updates.
> - Do NOT proceed to Phase 2 until every file is marked read and user approves.

---

## What This Phase Does

Create the source manifest — a complete inventory of every file the agent must process. This becomes the working checklist for the entire build.

## Step 1: Run the Indexing Script

```bash
python3 <skill_dir>/scripts/create_source_index.py <SOURCE_PATH> <OUTPUT_PATH>
```

This creates `<OUTPUT_PATH>/source-index.md` with every source file listed, classified, and ready for processing.

## Step 2: Read Every File

Work through the source index in order. For each file:

1. **Read the file.**
2. **Update the index immediately:**
   - Mark the file `[x]` in the Reading Checklist
   - Add notes about what you found (key topics, quality, relevance)
   - If the classification seems wrong, update the Type/Status columns in the table
3. **Record issues as you find them:**
   - Conflicts between documents → add to "Conflicts Identified" section
   - Missing information → add to "Gaps Identified" section
   - Reclassifications needed → update the file's Type/Status in the table

**DO NOT:**
- Skip files because they seem unimportant
- Read files without updating the index
- Read multiple files before updating the index
- Proceed to Phase 2 until every file is marked read

## Step 3: Evaluate Synthesis Needs

As you read each file, refine the script's preliminary `needs-synthesis` classification:

| The file... | Correct status |
|-------------|----------------|
| Contains filler words, speech artifacts, conversational rambling, verbatim quotes | `needs-synthesis` |
| Is already clean, well-organized, directly usable by an LLM agent | Change to `ready` |
| Has "synthesis" in the filename (already processed) | Change to `ready` or `synthesized` |
| Is a structured document with headers, lists, organized sections | Change to `ready` |

The script classifies by file type heuristics. You classify by actual content quality.

## Step 4: Create Build State

After completing the index, create `<OUTPUT_PATH>/build-state.md` using the template from `references/TEMPLATES.md`. This file tracks progress across sessions.

Set:
- Current phase: `1 - Index`
- Phase 1 status: `complete (pending approval)`
- Next phase file: `references/phases/PHASE_2_SYNTHESIZE.md`

## Gate: User Approval Required

Before requesting approval, write:
- "Source index complete: [N] files catalogued"
- "Files needing synthesis: [list or 'none']"
- "Conflicts found: [list or 'none']"
- "Gaps found: [list or 'none']"

**STOP. Get user approval on completed source index before proceeding.**

After approval, update build-state.md: Phase 1 status → `complete`.

---

## After This Phase

Read [PHASE_2_SYNTHESIZE.md](PHASE_2_SYNTHESIZE.md) to begin synthesis.

The source index and build-state.md are your resumption points. If context is lost, reading these two files tells you exactly where you are and what to do next.
