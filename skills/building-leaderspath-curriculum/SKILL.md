---
name: building-leaderspath-curriculum
description: Builds LeadersPath curriculum content from lesson designs. Creates facilitator guides, activity configurations, and learner materials for facilitated AI learning experiences. Use when building LeadersPath lessons, creating AI sandbox activities, designing curriculum for course-based AI education, or converting lesson materials into LeadersPath format. Activates when curriculum documents, lesson designs, or activity outlines are provided via file path, attached file, or uploaded document.
---

<purpose>
Curriculum designers default to lesson-centric thinking: each lesson teaches, the AI
delivers content, learners consume independently. LeadersPath inverts this. The facilitator
teaches; the AI sandbox demonstrates. This skill exists to enforce that inversion—producing
facilitator guides as the primary deliverable, with activities as hands-on experiments
rather than self-contained lessons.
</purpose>

# Building LeadersPath Curriculum

Build curriculum content for LeadersPath facilitated AI learning experiences.

## What LeadersPath Is

LeadersPath is a **facilitated course learning experience**, not a self-paced lesson platform. The system has three components:

1. **Learners in a course** — Peers learning together
2. **A human facilitator** — Who teaches concepts and leads discussion
3. **AI sandboxes as activities** — For hands-on experimentation

**The AI sandbox is NOT the lesson—it's an activity within a facilitated learning experience.**

**The pedagogical model:** Facilitator presents concepts → Learners experiment in AI sandboxes → Group discusses and reflects → Facilitator synthesizes.

## What This Skill Creates

For each **lesson** (the atomic teaching unit):

1. **Lesson Metadata** (`lesson-metadata.md`) — Title, description, difficulty, duration
2. **Learning Objectives** (`learning-objectives.md`) — What learners achieve (LESSON level, not per-activity)
3. **Facilitator Guide** (`facilitator-guide.md`) — **PRIMARY DELIVERABLE**: Complete teaching script with timing, activities, and discussion prompts
4. **Learner Overview** (`learner-overview.md`) — What learners will experience (context, not teaching)
5. **Q&A Chatbot Config** (`qa-chatbot-config.md`) — Optional helpful assistant for lesson content questions

For each **activity** (AI sandbox experiment within the lesson):

1. **Configuration/** — System prompt, API settings, context file references
2. **Instructions** (`instructions.md`) — "Try this, notice that" guidance (NOT conceptual teaching)

**Key distinction:**
- **Activity Sandbox** = Demonstrates specific AI behavior (might be sycophantic, limited, roleplay, etc.)
- **Lesson Q&A Bot** = Optional helpful assistant for answering questions about lesson content

---

## Critical Rules

**GROUNDING:** Base all content ONLY on provided curriculum documents. Never invent learning objectives, activity concepts, or pedagogical approaches not in the source materials.

**LESSON-FIRST:** The lesson is the teaching unit. Learning objectives live at lesson level, not per-activity. The facilitator guide is the central deliverable.

**ACTIVITIES ARE EXPERIMENTS:** Activities guide sandbox experimentation, not conceptual teaching. Concepts are delivered by the facilitator, not embedded in activity instructions.

**CONTEXT FILE REUSE:** Track context files across activities. Before creating a new context file, check if an existing one serves the purpose. Document reuse in the lesson tracker.

**ARTIFACT OUTPUT:** Never output content inline. Always save to files in the working folder. No wrapper folders like `_leaderspath/`—output directly to the assigned location.

**SKILL BOUNDARIES:** This skill does NOT create Agent Skills. If an activity requires a new skill, output a prompt for the `/creating-skills` workflow instead.

**PROGRESS TRACKING:** Maintain a lesson tracker file. Update it after every completed step. This enables session resumption after compaction.

**SECOND-ORDER THINKING:** When building facilitator guides and activity configs, consider what each implementation choice enables and constrains for the learner experience. If an activity's system prompt frames a concept one way, how does that shape what learners can discover? Name both sides. See [CURRICULUM-DESIGNER-TIPS.md](references/CURRICULUM-DESIGNER-TIPS.md) for detailed guidance.

**EMERGENT INSIGHTS:** The building process often reveals things that weren't in the original design — distinctions that become clearer through implementation, concepts that connect in unexpected ways, pacing that works differently than planned. Surface these explicitly rather than absorbing them silently. Note them in the lesson tracker for the meta-analysis phase.

**PROFESSIONAL OBJECTIVITY:** If curriculum source materials contain unclear or contradictory guidance, surface the issue rather than inventing a resolution. Ask for clarification rather than making assumptions.

---

## Tips for Curriculum Designers

See [references/CURRICULUM-DESIGNER-TIPS.md](references/CURRICULUM-DESIGNER-TIPS.md) for detailed guidance on writing effective prompts, including:
- Designing lessons as cohesive facilitated experiences
- Writing facilitator guides as the primary deliverable
- Creating focused activity instructions (not conceptual teaching)
- Structuring comparison activities within a lesson
- Deciding when to include a Lesson Q&A bot

---

## Before Starting

**FIRST: Read the reference files:**

1. [references/LEADERSPATH-SCHEMA.md](references/LEADERSPATH-SCHEMA.md) — Data model, field requirements, WordPress mapping
2. [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) — How to create facilitator guides, activity instructions, and Q&A configs
3. [references/ACTIVITY-TEMPLATE.md](references/ACTIVITY-TEMPLATE.md) — Template for activity configuration and instructions
4. [references/CURRICULUM-DESIGNER-TIPS.md](references/CURRICULUM-DESIGNER-TIPS.md) — Guidelines for curriculum designers
5. [references/NAMING-SYSTEM.md](references/NAMING-SYSTEM.md) — Lesson ID, Activity ID, and Context File naming conventions

**Do not proceed until you have read all five reference files.**

---

**THEN: Gather information from the user:**

1. **"Where are your curriculum source documents?"** (file paths or attached files)

2. **"What is the Lesson ID?"**

   Lesson ID format: `LSN###-slug` (e.g., `LSN001-skills-framework`)

   If user provides full ID: validate format against `LSN###-slug` pattern.

   If user provides partial info, construct the ID:
   - **Number:** Use `next_id` from `Curriculum/Registry/lesson-registry.yaml`
   - **Slug:** Auto-generate from lesson name (kebab-case, 3-50 chars, starts with letter)

   If no registry is available, ask the user for the next available LSN number.

3. **"Where is the Curriculum folder?"** (for registry and context file access)

   Look for `Curriculum/Registry/lesson-registry.yaml` relative to the working directory.
   If found: read it to get next available LSN### and ACT### IDs, check for conflicts.
   If not found: ask the user, or plan to output registry entries for manual addition.

4. **"Are there existing context files I should reference?"** (for reuse identification)

   Check `Curriculum/Contexts/` for existing CTX###-slug.md files (flat directory, no subfolders).
   Check `Curriculum/Registry/context-registry.yaml` for the full inventory and next available IDs.
   Note: context-registry.yaml has separate counters: `next_real_id` (CTX001-099) and `next_demo_id` (CTX101-199).

5. **"Will this lesson need a Q&A chatbot?"** (optional helpful assistant)

**Output Location:**

Output to the lesson folder: `Curriculum/Lessons/LSN###-slug/`

- `Curriculum/Lessons/LSN###-slug/lesson-tracker.md`
- `Curriculum/Lessons/LSN###-slug/lesson-metadata.md`
- `Curriculum/Lessons/LSN###-slug/activities/ACT###-slug/`

If the Curriculum folder structure is not present, ask the user where to output files.

---

## Workflow Overview

```
Phase 1: Initialize Lesson Tracker
    ↓
Phase 2: Create Lesson-Level Content
    ├── 2a: Lesson metadata
    ├── 2b: Learning objectives (LESSON level)
    ├── 2c: Facilitator guide (PRIMARY)
    ├── 2d: Learner overview
    └── 2e: Q&A chatbot config (if needed)
    ↓
Phase 3: Create Activities (iterative, per activity)
    ├── 3a: Activity configuration (system prompt, API settings)
    └── 3b: Activity instructions ("try this, notice that")
    ↓
Phase 4: Validate and Finalize
    ├── 4a: Install context files to library (if Contexts folder exists)
    └── 4b: Validate and confirm
```

---

## Single Activity Mode

When creating a single activity without a lesson:
- **Skip Phases 1-2** (no lesson-level content)
- **Complete the Analysis step below** before creating any files
- Phase 4a (context file installation) still applies if the Curriculum/Contexts/ structure exists

### Analysis Step (REQUIRED for single activities)

Before creating any files, document in your process log:

1. **What AI behavior does this activity demonstrate?** (limitation, capability, or flaw?)
2. **What creates that behavior?** (system prompt alone, context files, or both?)
3. **What files do we create?** (see [references/ACTIVITY-TEMPLATE.md](references/ACTIVITY-TEMPLATE.md) for folder structure)

---

<phase_initialize>

## Phase 1: Initialize Lesson Tracker

Create the tracker file at `[working-folder]/lesson-tracker.md`:

```markdown
# Lesson Tracker: [Lesson Name]

**Lesson ID:** [LSN###-slug]
**Created:** [date]
**Last Updated:** [date]
**Current Phase:** 1 - Initialization

## Lesson-Level Content

| Component | Status |
|-----------|--------|
| Lesson Metadata | [ ] |
| Learning Objectives | [ ] |
| Facilitator Guide | [ ] |
| Learner Overview | [ ] |
| Q&A Chatbot Config | [ ] or N/A |

## Activity Checklist

| Activity Slug | AI Behavior | Configuration | Instructions | Status |
|---------------|-------------|---------------|--------------|--------|
| [slug] | [brief description] | [ ] | [ ] | pending |

Activity folder names use format: `ACT###-{slug}`

## Context Files

| File ID | Description | Used By Activities | Status | Location |
|---------|-------------|-------------------|--------|----------|
| [CTX###-slug.md] | | | | |

## Session Log

### [date] - Session 1
- Initialized tracker
- [next actions]
```

**Update the tracker after EVERY completed step.** This is non-negotiable.

**Register Lesson and Activity IDs:**

If `Curriculum/Registry/lesson-registry.yaml` is accessible:
1. Read the registry to get `next_id`
2. Add the new lesson entry with its activity list
3. Increment `next_id`

If the registry is not accessible, output the entries that need to be added:

```yaml
LSN###:
  slug: [slug]
  name: [Lesson Title]
  status: development
  created: [date]
  activities: [ACT###, ACT###, ...]
```

**GATE:** Before proceeding, write:
- "Lesson ID: [LSN###-slug]"
- "Lesson tracker created at: [path]"
- "Activities identified: [count] — [list slugs]"

</phase_initialize>

---

<phase_lesson_content>

## Phase 2: Create Lesson-Level Content

### 2a: Lesson Metadata

Create `lesson-metadata.md` following the template in [references/LEADERSPATH-SCHEMA.md](references/LEADERSPATH-SCHEMA.md) (Output File Formats section).

**Update tracker:** Mark Lesson Metadata complete.

### 2b: Learning Objectives (LESSON Level)

Create `learning-objectives.md` following the template in [references/LEADERSPATH-SCHEMA.md](references/LEADERSPATH-SCHEMA.md) (Output File Formats section).

**Important:** Learning objectives are at LESSON level, not per-activity. Activities support these objectives through hands-on experimentation.

**Update tracker:** Mark Learning Objectives complete.

### 2c: Facilitator Guide (PRIMARY DELIVERABLE)

Create `facilitator-guide.md` — this is the central document a facilitator needs to teach the entire lesson.

See [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) for the complete facilitator guide structure and examples.

The facilitator guide should include:
- Lesson overview (duration, activities, prerequisites)
- Materials needed
- Learning objectives (repeated from learning-objectives.md)
- **Teaching flow** with timing for each section:
  - Concepts to present
  - Transitions to activities
  - Activity summaries (what learners do, what to watch for)
  - Discussion prompts after activities
  - Common questions and answers
- Synthesis and wrap-up guidance
- Timing notes (where things run long/short)

**A facilitator should be able to teach the entire lesson from this document alone.**

**Update tracker:** Mark Facilitator Guide complete.

### 2d: Learner Overview

Create `learner-overview.md` following the template in [references/LEADERSPATH-SCHEMA.md](references/LEADERSPATH-SCHEMA.md) (Output File Formats section).

**Note:** This is context-setting, not teaching. Concepts are delivered by the facilitator.

**NATURAL PROSE:** This content is learner-facing. Write from the voice of a learning facilitator speaking to their cohort — warm, direct, practical. When you catch yourself sounding like AI describing a learning experience rather than a facilitator setting one up, return to the facilitator's perspective. Revision backstop — these signal the voice has drifted: "delve," "explore," "it's important to note," "Not only X but Y," "serves as."

**Update tracker:** Mark Learner Overview complete.

### 2e: Q&A Chatbot Config (OPTIONAL)

If the lesson needs a Q&A chatbot, create `qa-chatbot-config.md` following the template in [references/LEADERSPATH-SCHEMA.md](references/LEADERSPATH-SCHEMA.md) (Output File Formats section). See [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) for Q&A bot configuration guidance and when to include/skip.

**Update tracker:** Mark Q&A Chatbot Config complete (or N/A).

**GATE:** Before proceeding to Phase 3, write:
- "Phase 2 complete. Files created: [list]"
- "User approval received: Yes"

**STOP.** Get user approval on lesson-level content before proceeding to activities.

</phase_lesson_content>

---

<phase_activities>

## Phase 3: Create Activities

Work through activities sequentially. For each activity:

### Activity Naming

Activity IDs are globally unique across all lessons (not per-lesson). See [references/NAMING-SYSTEM.md](references/NAMING-SYSTEM.md) for complete naming conventions. Get the next available ACT### from `lesson-registry.yaml`.

### 3a: Create Activity Configuration

Create the `activities/ACT###-[slug]/configuration/` folder with:

**system-prompt.md** — The complete system prompt for the AI sandbox
- What AI behavior should learners experience?
- What configuration creates that behavior?
- What should the AI do/not do?

**api-settings.md** and **context-files.md** — See [references/ACTIVITY-TEMPLATE.md](references/ACTIVITY-TEMPLATE.md) for templates. Reference context files by filename only (`CTX###-slug.md`), not by path.

See [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) for system prompt patterns.

**Update tracker:** Mark Configuration complete for this activity.

### Context File Naming (if creating new context files)

See [references/NAMING-SYSTEM.md](references/NAMING-SYSTEM.md) for complete context file naming conventions (ID ranges, scope, registry format). Get the next available CTX### from `context-registry.yaml` (`next_real_id` for CTX001-099, `next_demo_id` for CTX101-199). If registry is not accessible, ask the user for the next available CTX number.

Output registry entries for any new context files created, and update `context-registry.yaml` if accessible.

### 3b: Create Activity Instructions

Create `activities/ACT###-[slug]/instructions.md` following the template in [references/ACTIVITY-TEMPLATE.md](references/ACTIVITY-TEMPLATE.md).

**Important:** Activity instructions are ONLY for guiding sandbox experimentation. They do NOT:
- Teach concepts (facilitator does that)
- Include learning objectives (those are at lesson level)
- Explain "The Principle" (facilitator synthesizes after)

**NATURAL PROSE:** Activity instructions are learner-facing. Write from a facilitator's voice — direct, imperative, practical. "Ask:", "Try:", "Notice:" — not "Let's explore..." or "You'll discover...". When the voice drifts toward AI narration, return to the facilitator's perspective.

**Update tracker:** Mark Instructions complete, update activity status to "complete."

**Present completed activity to user for review before proceeding to next activity.**

**GATE (per activity):** Before proceeding to next activity, write:
- "Activity [N] complete: [name]"
- "Files created: configuration/, instructions.md"
- "User approval received: Yes"

</phase_activities>

---

<phase_finalize>

## Phase 4: Validate and Finalize

### 4a: Install Context Files to Library

This step installs context files created during curriculum development into the shared Contexts library. It is environment-dependent and gracefully skips if the library structure is not present.

**Check Prerequisites:**

1. Look for `Curriculum/Contexts/` directory relative to the working directory root
2. Also check for `Curriculum/Registry/context-registry.yaml`
3. **If neither exists:** Skip this entire step and note in the lesson tracker:
   - Add to Context Files Location column: "Manual — Contexts folder not found"
   - Log in Session Log: "Context installation skipped — Curriculum/Contexts/ not found. Install context files manually."
   - Proceed directly to step 4b (validation)

**If Contexts directory exists:**

**GATE:** Before copying any files, write:
- "Files to install: [count]"
- "Destination: Curriculum/Contexts/ (flat directory)"
- "Will skip (already exist): [count]"

For each file in the lesson tracker's "Context Files" table:
1. Copy from `activities/shared-context/CTX###-slug.md` to `Curriculum/Contexts/CTX###-slug.md` (flat — no subfolders). Use simple file copy (`cp`), NOT read-process-write. **Skip files that already exist** (don't overwrite).
2. Update lesson tracker Location column accordingly.

**Update registries:**
- `context-registry.yaml` — Add new entries, increment `next_real_id` or `next_demo_id`
- `lesson-registry.yaml` — Add lesson entry with activity list if not done in Phase 1

Update lesson tracker with installation results and log in Session Log.

**GATE:** Before proceeding to validation, write:
- "Context files installed: [count] of [total]"
- "Skipped (already exist): [count]"
- "Registries updated: Yes/No/N/A"

---

### 4b: Validate and Confirm

After all content is complete:

1. **Review tracker** — All items should show complete status
2. **Check context file reuse** — Confirm shared files are properly mapped
3. **Verify flow** — Activities follow logical progression in facilitator guide
4. **Calculate totals** — Confirm duration estimates add up

See [references/LEADERSPATH-SCHEMA.md](references/LEADERSPATH-SCHEMA.md) for the complete folder structure, WordPress import mapping, and field requirements.

**GATE:** Before declaring complete, write:
- "All activities complete: [count]"
- "All tracker items show complete status: Yes"
- "User approval received on full curriculum: Yes"

**STOP.** Get user approval on complete curriculum before finalizing.

</phase_finalize>

---

## Handling Skill Requirements

If an activity requires an Agent Skill that doesn't exist: do NOT create it. Instead, save a skill request to `skill-requests/[skill-name]-request.md` with activity name, skill purpose, why needed, inputs, and outputs. Reference `/creating-skills` for the actual skill creation.

---

## Resuming a Previous Session

If `lesson-tracker.md` exists: read it, check current phase and incomplete items, review session log, then continue from next incomplete step. Always update the session log when resuming.

---

## Checkpoints

| After | User Reviews |
|-------|--------------|
| Phase 1 | Tracker initialized, output location confirmed |
| Phase 2 | Lesson-level content (objectives, facilitator guide, learner overview) |
| Each activity | Completed activity configuration and instructions |
| Phase 4a | Context files installed to library (if applicable) |
| Phase 4b | Full curriculum package validated |

**Do not proceed without explicit approval at each checkpoint.**

---

## Examples

See [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) for complete examples including:
- Facilitator guide structure with teaching flow
- Activity instructions (focused on experimentation)
- System prompt patterns (bare, role-constrained, context-rich, deliberately flawed)
- Lesson Q&A bot configuration
- Complete lesson package with folder structure

See [references/NAMING-SYSTEM.md](references/NAMING-SYSTEM.md) for naming examples and folder structure conventions.

---

<failed_attempts>

## What Doesn't Work

- **Putting learning objectives in activities:** Objectives live at lesson level. Activities support objectives through experimentation, not through their own objectives. If you add objectives per activity, you're reverting to the old lesson-centric model.

- **Teaching concepts in activity instructions:** "The Principle" sections belong in the facilitator guide, not in activity instructions. Activities say "try this, notice that"—the facilitator synthesizes meaning afterward.

- **Creating Q&A bots for every lesson:** The Lesson Q&A Bot is optional. Simple lessons with present facilitators don't need one. Adding unnecessary Q&A bots creates maintenance burden and confuses the distinction between activity sandboxes (which demonstrate behavior) and Q&A bots (which are always helpful).

- **Bare system prompts that imply knowledge:** If the AI needs organizational knowledge (not just behavioral instructions), that knowledge must be in context files. A system prompt saying "You are an expert in our methodology" without a context file providing that methodology will produce hallucinated content.

- **Skipping the facilitator guide:** The facilitator guide is the primary deliverable, not an optional add-on. Without it, activities become disconnected experiments rather than a cohesive learning experience.

- **Designing activities as standalone lessons:** Each activity is part of a lesson flow. If an activity makes sense without the preceding facilitator presentation and subsequent discussion, it's probably over-teaching in the sandbox.

</failed_attempts>
