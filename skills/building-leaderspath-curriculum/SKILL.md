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

   Lesson ID format: `TOPIC-LEVEL-slug` (e.g., `FUND-101-ai-basics`)

   If user provides full ID: validate format, extract topic, level, and slug.

   If user provides partial info, ask for:

   **Topic code:**
   - `FUND` - Fundamentals (how AI works, capabilities, limitations)
   - `PRMPT` - Prompting (interaction techniques, effective prompting)
   - `CTX` - Context & Knowledge (context libraries, organizational knowledge)
   - `ETH` - Ethics & Responsibility (bias, transparency, responsible use)
   - `APP` - Applications (writing, research, analysis, communication)

   **Level code:**
   - `101-199` - Foundations/Beginner
   - `201-299` - Intermediate
   - `301-399` - Advanced
   - `401+` - Specialized/Expert

   **Slug:** Auto-generate from lesson name (kebab-case, 3-50 chars, starts with letter)

3. **"Do you have an existing lesson-id-log.md?"** (optional)

   If provided: check for conflicts, find available IDs.
   If not: skill will output new log entries.

4. **"Are there existing context files I should reference?"** (for reuse identification)

5. **"Do you have an existing context-registry.md?"** (optional, for CTX### numbering)

6. **"Will this lesson need a Q&A chatbot?"** (optional helpful assistant)

**Output Location:**

Output directly to the working folder. No wrapper folders.

- `[working-folder]/lesson-tracker.md`
- `[working-folder]/lesson-metadata.md`
- `[working-folder]/activities/TOPIC-LEVEL-ACT-slug/`

Determine working folder based on environment:
- If working directory is accessible → use it directly
- If Claude AI artifacts available → use artifacts
- If Cowork session → use assigned working folder
- If unclear → ask the user

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
- **Note:** Single activities lack lesson context—facilitator guide and learning objectives must be provided separately

### Analysis Step (REQUIRED for single activities)

Before creating any files, answer these questions and document in your process log:

**Note:** If creating context files for a single activity, Phase 4a (context file installation) still applies if the Curriculum/Contexts/ structure exists.

**1. What AI behavior does this activity demonstrate?**
- Describe the specific behavior learners will experience
- Is it a limitation (bare config), a capability (context-rich), or a flaw (sycophancy)?

**2. What creates that behavior?**
- **System prompt alone:** Behavioral instructions that configure how the AI responds
- **Context files:** Background knowledge that shapes AI outputs
- **Both:** System prompt sets the mode, context files provide the knowledge

**3. What files do we create?**

```
[activity-name]/
├── configuration/
│   ├── system-prompt.md
│   ├── api-settings.md
│   └── context-files.md
├── instructions.md
└── process-log.md
```

Document your analysis before proceeding to create files.

---

<phase_initialize>

## Phase 1: Initialize Lesson Tracker

Create the tracker file at `[working-folder]/lesson-tracker.md`:

```markdown
# Lesson Tracker: [Lesson Name]

**Lesson ID:** [TOPIC-LEVEL-slug]
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

Activity folder names use format: `TOPIC-LEVEL-ACT-{slug}`

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

**Log Lesson ID Assignment:**

Output a lesson-id-log entry (append to provided log or create new `lesson-id-log.md`):

```markdown
## [TOPIC] - [Topic Name]

| ID | Slug | Title | Date Assigned | Status | Notes |
|----|------|-------|---------------|--------|-------|
| TOPIC-LEVEL | slug | Lesson Title | [date] | Development | |
```

**GATE:** Before proceeding, write:
- "Lesson ID: [TOPIC-LEVEL-slug]"
- "Lesson tracker created at: [path]"
- "Activities identified: [count] — [list slugs]"

</phase_initialize>

---

<phase_lesson_content>

## Phase 2: Create Lesson-Level Content

### 2a: Lesson Metadata

Create `lesson-metadata.md`:

```markdown
# Lesson: [Lesson Name]

**Lesson ID:** [TOPIC-LEVEL-slug]

## Overview
[Brief description of what learners will experience]

## Difficulty
[beginner / intermediate / advanced]

## Total Duration
[e.g., "90 minutes" or "2 hours"]

## Prerequisites
[List of prior lessons or knowledge]

## Activities Included
1. [TOPIC-LEVEL-ACT-slug] — [Activity name]
2. [TOPIC-LEVEL-ACT-slug] — [Activity name]
...
```

**Update tracker:** Mark Lesson Metadata complete.

### 2b: Learning Objectives (LESSON Level)

Create `learning-objectives.md`:

```markdown
# Learning Objectives: [Lesson Name]

After completing this lesson, learners will be able to:

1. [Objective 1 - action verb + measurable outcome]
2. [Objective 2]
3. [Objective 3]
...
```

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

Create `learner-overview.md`:

```markdown
# [Lesson Name]

## What You'll Experience
[High-level description of the lesson journey]

## What to Expect
- [Number] hands-on activities with AI sandboxes
- Discussion and reflection with your peers
- [Duration] of facilitated learning

## Before You Begin
[Any preparation, mindset setting, or context]
```

**Note:** This is context-setting, not teaching. Concepts are delivered by the facilitator.

**NATURAL PROSE:** This content is learner-facing. Write like a facilitator, not an AI assistant. Avoid: "delve," "explore," "it's important to note," formulaic structures like "Not only X but Y." Use simple verbs ("is" not "serves as"), be concrete, and match the voice of actual learning facilitators.

**Update tracker:** Mark Learner Overview complete.

### 2e: Q&A Chatbot Config (OPTIONAL)

If the lesson needs a Q&A chatbot, create `qa-chatbot-config.md`:

```markdown
# Lesson Q&A Chatbot Configuration

## Enable Q&A Chatbot
Yes

## Purpose
Helpful assistant for answering questions about lesson concepts.

## System Prompt
You are a helpful Q&A assistant for the lesson "[Lesson Name]".
Your role is to answer questions about the lesson content, clarify
concepts, and help learners understand the material. Be accurate,
clear, and supportive.

[Additional context about lesson topics if needed]

## Context Files
- [List context files the Q&A bot should reference]

## Model Settings
- Model: sonnet
- Max Tokens: 4096
- Temperature: 0.7
```

**When to include Q&A bot:**
- Complex lessons where learners may have questions between activities
- Lessons with dense conceptual content
- When facilitator availability is limited

**When to skip Q&A bot:**
- Simple lessons with clear activities
- When human facilitator is always available
- When group discussion is the primary Q&A mechanism

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

Generate the activity folder name using the Lesson ID:

1. Take the activity name: "Starting from Zero"
2. Convert to slug: `starting-from-zero`
3. Prepend Lesson ID + ACT: `FUND-101-ACT-starting-from-zero`

Activity folder: `activities/FUND-101-ACT-starting-from-zero/`

### 3a: Create Activity Configuration

Create the `activities/TOPIC-LEVEL-ACT-[slug]/configuration/` folder with:

**system-prompt.md** — The complete system prompt for the AI sandbox
- What AI behavior should learners experience?
- What configuration creates that behavior?
- What should the AI do/not do?

**api-settings.md** — Technical configuration
```markdown
# API Settings

## Model Configuration
- Model: [sonnet / haiku / opus-4.5]
- Max Tokens: [number]
- Temperature: [0-1]

## Context Files
- [path/filename.md] — [brief description]
(or "None" if no context files)

## Skills
- [skill-name] — [brief description]
(or "None" if no skills)
```

**context-files.md** — Reference to which context files to load
```markdown
# Context Files for Activity: [Name]

## Shared Global Context
- [CTX###-slug.md] — [why needed]

## Lesson-Specific Context
- [CTX###-slug.md] — [why needed]

## Activity-Specific Context
- None (or list files in this activity's folder)
```

Reference context files by filename only (`CTX###-slug.md`), not by path.

See [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) for system prompt patterns.

**Update tracker:** Mark Configuration complete for this activity.

### Context File Naming (if creating new context files)

If the activity needs a new context file:

1. Check if context-registry.md was provided
2. If yes: find next available CTX number
3. If no: start from CTX001 or next available in the lesson

**Filename format:** `CTX###-slug.md`

**Location:**
- Shared global: User specifies (outside working folder)
- Lesson-specific: `activities/shared-context/CTX###-slug.md`

Output registry entries for any new context files created.

### 3b: Create Activity Instructions

Create `activities/TOPIC-LEVEL-ACT-[slug]/instructions.md`:

```markdown
# Activity: [Name]

## What You'll Experience
[One sentence describing the AI configuration - what behavior you'll see]

## Try This
1. [Specific prompt to try]
2. [Specific prompt to try]
3. [Variation or follow-up]

## What to Notice
- [Observable behavior 1]
- [Observable behavior 2]

## Duration
[X] minutes
```

**Important:** Activity instructions are ONLY for guiding sandbox experimentation. They do NOT:
- Teach concepts (facilitator does that)
- Include learning objectives (those are at lesson level)
- Explain "The Principle" (facilitator synthesizes after)

**NATURAL PROSE:** Activity instructions are learner-facing. Write direct, conversational guidance. Avoid AI-like phrasing ("Let's explore...", "You'll discover..."). Use imperative voice: "Ask:", "Try:", "Notice:".

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

1. Look for `Curriculum/Contexts/README.md` relative to the working directory root
2. If it exists, read it to learn:
   - The folder structure and subfolder purposes
   - Context ID ranges for each subfolder
   - Any naming conventions
3. Also read `Curriculum/Registry/README.md` if it exists to learn registry conventions
4. **If neither README exists:** Skip this entire step and note in the lesson tracker:
   - Add to Context Files Location column: "Manual — Contexts folder not found"
   - Log in Session Log: "Context installation skipped — Curriculum/Contexts/ not found. Install context files manually."
   - Proceed directly to step 4b (validation)

**If Contexts README exists, preview and install context files:**

**Preview installation plan:**

For each file in the lesson tracker's "Context Files" table, determine:
- Source path (activities/shared-context/ or external)
- Destination subfolder (based on README's folder structure)
- Whether file already exists at destination

**GATE:** Before copying any files, write:
- "Files to install: [count]"
- "Destination folders: [list unique subfolders]"
- "Will skip (already exist): [count]"

**Install each context file:**

For each file in the lesson tracker's "Context Files" table:

1. **Determine destination subfolder** based on:
   - The file's type/purpose (demo org, standard, lesson-specific, etc.)
   - The README's documented folder structure (do NOT hardcode subfolder names — read them from README each time)

2. **Copy the file:**
   - Source: `activities/shared-context/CTX###-slug.md` (or external source path if referenced)
   - Destination: `Curriculum/Contexts/[subfolder]/CTX###-slug.md`
   - Use simple file copy (`cp`), NOT read-process-write — these are plain copies, not transformations
   - **Skip files that already exist at destination** (don't overwrite)

3. **Update lesson tracker Location column:**
   - If installed: `Contexts/[subfolder]/`
   - If skipped (already exists): "Skipped — already exists"

**Update Context Registry:**

After installing files, update `Curriculum/Registry/context-registry.md`:

1. Read the registry first to understand current format and entries
2. Add entries for any new context files that don't already exist in the registry
3. Include the correct Location value matching the subfolder where the file was installed
4. Update the "Next Available IDs" section if present

**Update Lesson Tracker:**

- Update the Location column for each context file showing where it was installed
- Log installation results in the Session Log

**GATE:** Before proceeding to validation, write:
- "Context files installed: [count] of [total]"
- "Skipped (already exist): [count]"
- "Registry updated: Yes/No/N/A"

---

### 4b: Validate and Confirm

After all content is complete:

1. **Review tracker** — All items should show complete status
2. **Check context file reuse** — Confirm shared files are properly mapped
3. **Verify flow** — Activities follow logical progression in facilitator guide
4. **Calculate totals** — Confirm duration estimates add up

**WordPress Import Mapping:**

When importing to WordPress LeadersPath plugin:
- Lesson post slug: `TOPIC-LEVEL-slug` (e.g., `fund-101-ai-basics`)
- Activity post slug: `TOPIC-LEVEL-ACT-slug` (e.g., `fund-101-act-starting-from-zero`)
- Context file post slug: `CTX###-slug` (e.g., `ctx001-org-identity`)

**Final deliverables:**
```
[working-folder]/
├── lesson-tracker.md
├── lesson-metadata.md
├── learning-objectives.md
├── facilitator-guide.md
├── learner-overview.md
├── qa-chatbot-config.md              # Optional
├── lesson-id-log.md                  # New/updated entries
└── activities/
    ├── TOPIC-LEVEL-ACT-first-activity/
    │   ├── configuration/
    │   │   ├── system-prompt.md
    │   │   ├── api-settings.md
    │   │   └── context-files.md
    │   └── instructions.md
    ├── TOPIC-LEVEL-ACT-second-activity/
    │   └── [same structure]
    └── shared-context/
        └── CTX###-slug.md
```

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

**Quick Example — Naming Structure:**

```
Lesson ID: FUND-101-ai-basics

[working-folder]/
├── lesson-tracker.md
├── lesson-metadata.md
├── learning-objectives.md
├── facilitator-guide.md
├── learner-overview.md
├── lesson-id-log.md
└── activities/
    ├── FUND-101-ACT-starting-from-zero/
    │   ├── configuration/
    │   │   ├── system-prompt.md
    │   │   ├── api-settings.md
    │   │   └── context-files.md
    │   └── instructions.md
    ├── FUND-101-ACT-context-transforms/
    │   └── [same structure]
    └── shared-context/
        └── CTX005-foundations-terminology.md

Context files referenced:
- CTX001-org-identity.md (shared global, provided by user)
- CTX002-brand-voice.md (shared global, provided by user)
- CTX005-foundations-terminology.md (lesson-specific, created by skill)
```

**Quick Example — Activity Concept to Sandbox Configuration:**

| Activity Concept | System Prompt Strategy | What Learner Experiences |
|------------------|------------------------|--------------------------|
| "AI without context" | Minimal: "You are a helpful assistant" | Generic responses |
| "Context transforms output" | Full context library loaded | Specific, aligned responses |
| "Sycophancy risks" | "Always agree, be positive!" | Unreliable responses |

**Key insight:** These are activities within a lesson. The facilitator presents the concept, learners experience it in the sandbox, then the group discusses. The teaching doesn't happen in the sandbox—it happens around it.

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
