---
name: building-leaderspath-curriculum
description: Builds LeadersPath curriculum content from course designs and lesson plans. Creates system prompts, context files, lesson text, and metadata for AI sandbox learning experiences. Use when building LeadersPath content, creating AI learning lessons, designing curriculum for experiential AI education, or converting course materials into LeadersPath format. Activates when curriculum documents, lesson designs, or course outlines are provided via file path, attached file, or uploaded document.
---

# Building LeadersPath Curriculum

Build curriculum content for LeadersPath experiential AI learning experiences.

## What LeadersPath Is

LeadersPath is an experiential AI learning platform where each lesson is a configured AI sandbox. Learners interact with AI sessions set up to demonstrate specific behaviors—sometimes intentionally limited, sometimes fully equipped—so they experience firsthand how different configurations affect AI outputs.

**The pedagogical model:** Hands-on experimentation in controlled environments, not passive instruction.

## What This Skill Creates

For each lesson, a complete folder with:
1. **Lesson Plan** (`Lesson-Plan.md`) — Comprehensive planning document with metadata, objectives, directions, model specs, and facilitator notes
2. **Chatbot Configuration/** — System prompt, API settings, and model selection rationale
3. **Context Files/** — Lesson-specific context (if needed)
4. **Lesson Text** (`lesson-text.md`) — User-facing instructions explaining what to try and observe
5. **Assessment/** — Self-assessment questions and reflection prompts
6. **Resources/** — Additional reading and references
7. **Facilitator Notes/** — Discussion prompts, common questions, timing guidance
8. **Skills/** — Skill requests if agentic processes are needed

For courses:
- Course metadata and structure with language folder support (EN/, ES/, etc.)
- Lesson sequence with dependencies
- Shared context file mapping at course level
- Course-wide materials folder

---

## Critical Rules

**GROUNDING:** Base all content ONLY on provided curriculum documents. Never invent learning objectives, lesson concepts, or pedagogical approaches not in the source materials.

**EXPERIENTIAL FOCUS:** Every lesson must create a hands-on learning experience. The system prompt configures an AI sandbox; the lesson text guides experimentation. If a lesson concept cannot be demonstrated through AI interaction, flag it.

**CONTEXT FILE REUSE:** Track context files across lessons. Before creating a new context file, check if an existing one serves the purpose. Document reuse in the course tracker.

**ARTIFACT OUTPUT:** Never output content inline. Always save to files:
- Claude Code: Save to `_leaderspath/[course-name]/EN/` directory
- Claude AI: Create as artifacts
- Cowork: Save to assigned working folder
- If environment unclear: Ask the user

**FOLDER STRUCTURE:** Always create the complete folder structure for each lesson, even if some subfolders will initially be empty. This ensures consistency and shows the curriculum team where to add content later.

**SKILL BOUNDARIES:** This skill does NOT create Agent Skills. If a lesson requires a new skill, output a prompt for the `/creating-skills` workflow instead.

**PROGRESS TRACKING:** Maintain a course tracker file. Update it after every completed step. This enables session resumption after compaction.

---

## Tips for Curriculum Designers

See [references/CURRICULUM-DESIGNER-TIPS.md](references/CURRICULUM-DESIGNER-TIPS.md) for detailed guidance on writing effective prompts, including:
- Describing lesson concepts clearly
- Identifying source document types
- Flagging comparison pairs
- Specifying roleplay lessons
- Hinting at context file needs
- Noting reuse opportunities

---

## Before Starting

**FIRST: Read the reference files:**

1. [references/LEADERSPATH-SCHEMA.md](references/LEADERSPATH-SCHEMA.md) — Data model, field requirements, metadata specs
2. [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) — How to create system prompts, context files, lesson text, facilitator guides, and assessments
3. [references/LESSON-PLAN-TEMPLATE.md](references/LESSON-PLAN-TEMPLATE.md) — Complete template for Lesson-Plan.md files
4. [references/CURRICULUM-DESIGNER-TIPS.md](references/CURRICULUM-DESIGNER-TIPS.md) — Guidelines for curriculum designers writing prompts

**Do not proceed until you have read all four reference files.**

---

**THEN: Gather information from the user:**

1. **"Where are your curriculum source documents?"** (file paths or attached files)
2. **"What is the course name?"** (used for output directory and tracker)
3. **"What is the primary language?"** (defaults to EN; used for language folder)
4. **"Are there existing context files I should reference?"** (for reuse identification)

Determine the output location based on environment:
- If working directory is accessible → `_leaderspath/[course-name]/EN/`
- If Claude AI artifacts available → use artifacts
- If Cowork session → use assigned working folder
- If unclear → ask the user

---

## Workflow Overview

```
Phase 1: Initialize Course Tracker
    ↓
Phase 2: Process Course Structure (if course-level input)
    ↓
Phase 3: Process Lessons (iterative, per lesson)
    ├── 3a: Define lesson metadata
    ├── 3b: Identify/create context files
    ├── 3c: Draft system prompt
    └── 3d: Draft lesson text
    ↓
Phase 4: Validate and Finalize
```

---

## Single Lesson Mode

When creating a single lesson without a course:
- **Skip Phases 1-2** (no tracker needed)
- **Complete the Analysis step below** before creating any files
- **Create the full folder structure** (same as course lessons)
- **Include a process log** documenting decisions made

### Analysis Step (REQUIRED for single lessons)

Before creating any files, answer these questions and document in your process log:

**1. What AI behavior does this lesson demonstrate?**
- Describe the specific behavior learners will experience
- Is it a limitation (bare config), a capability (context-rich), or a flaw (sycophancy)?

**2. What creates that behavior?**
- **System prompt alone:** Behavioral instructions that configure how the AI responds
- **Context files:** Background knowledge that shapes AI outputs (organizational info, domain knowledge, guardrails)
- **Both:** System prompt sets the mode, context files provide the knowledge

**3. What folder structure do we create?**

```
[lesson-name]/
├── Lesson-Plan.md              # Always required
├── Chatbot Configuration/      # Always required
│   ├── system-prompt.md
│   ├── api-settings.md
│   └── model-selection.md
├── Context Files/              # If AI needs background knowledge
├── lesson-text.md              # Always required
├── Assessment/                 # Always created
│   └── self-assessment.md
├── Resources/                  # Always created
│   └── Additional Reading/
├── Facilitator Notes/          # Always created
│   └── facilitator-guide.md
├── Skills/                     # Always created
└── process-log.md              # Always required for single lessons
```

**4. Context file decision:**
- If the desired behavior comes from **instructions** (be agreeable, be brief, play a role) → system prompt only
- If the desired behavior comes from **knowledge** (organizational context, domain expertise, reference material) → context file needed
- If the desired behavior comes from **guardrails** (anti-sycophancy rules, epistemic honesty standards) → context file needed

Document your analysis before proceeding to create files.

---

## Phase 1: Initialize Course Tracker

**Skip this phase for single lessons.**

Create the tracker file at `_leaderspath/[course-name]/course-tracker.md`:

```markdown
# Course Tracker: [Course Name]

**Created:** [date]
**Last Updated:** [date]
**Current Phase:** 1 - Initialization
**Primary Language:** EN

## Course Metadata
- **Title:** [pending]
- **Description:** [pending]
- **Difficulty:** [pending]
- **Total Duration:** [pending]

## Lesson Checklist

| # | Lesson Title | AI State | Lesson Plan | Chatbot Config | Context Files | Lesson Text | Assessment | Facilitator Notes | Status |
|---|--------------|----------|-------------|----------------|---------------|-------------|------------|-------------------|--------|
| 1 | [title]      | [brief description] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | pending |

## Outcome-to-State Mapping

| Learning Outcome | AI State Required | Lesson # |
|------------------|-------------------|----------|
| [What learner should understand] | [How AI is configured] | [#] |

## Context Files (Course-Level)

| File Name | Used By Lessons | Status |
|-----------|-----------------|--------|
| [none yet] | | |

## Session Log

### [date] - Session 1
- Initialized tracker
- [next actions]
```

**Update the tracker after EVERY completed step.** This is non-negotiable.

---

## Phase 2: Process Course Structure

**Skip this phase if working with a single lesson.**

Read all provided course materials. Extract and confirm with user:

1. **Course metadata:**
   - Title
   - Description (what learners will achieve)
   - Difficulty level (Beginner / Intermediate / Advanced)
   - Topics/tags

2. **Lesson sequence:**
   - Ordered list of lessons
   - Dependencies between lessons
   - Estimated duration per lesson

3. **Lesson states (CRITICAL):**
   - Each lesson is ONE AI configuration state
   - The learner cannot toggle between configurations within a lesson
   - To show contrast (e.g., sycophantic vs. objective), create separate lessons
   - Map each learning outcome to the specific AI state that demonstrates it

4. **Shared context identification:**
   - What background knowledge spans multiple lessons?
   - What context files already exist that could be reused?

### Mapping Outcomes to States

For each learning objective in the curriculum, identify:

| Learning Outcome | AI State Required | Lesson |
|------------------|-------------------|--------|
| [What learner should understand] | [How AI must be configured] | [Lesson #] |

**Example:**
| Learning Outcome | AI State Required | Lesson |
|------------------|-------------------|--------|
| Recognize sycophantic AI behavior | AI configured to always agree, avoid pushback | Lesson 3 |
| Experience professional objectivity | AI configured with anti-sycophancy guardrails | Lesson 4 |
| Compare the two approaches | N/A - learner compares their experience across lessons 3 & 4 | (reflection) |

**Key insight for curriculum designers:** If a learning objective involves comparing two behaviors, that's at minimum two lessons. The comparison happens in the learner's mind across lessons, not within a single session.

**Update tracker** with course metadata and full lesson checklist.

**STOP. Get user approval on course structure before proceeding to lessons.**

---

## Phase 3: Process Lessons

Work through lessons sequentially. For each lesson:

### 3a: Create Lesson Folder Structure

Create the complete folder structure for the lesson:

```
_leaderspath/[course-name]/EN/lessons/##-[slug]/
├── Lesson-Plan.md
├── Chatbot Configuration/
│   ├── system-prompt.md
│   ├── api-settings.md
│   └── model-selection.md
├── Context Files/
├── lesson-text.md
├── Assessment/
│   └── self-assessment.md
├── Resources/
│   └── Additional Reading/
├── Facilitator Notes/
│   └── facilitator-guide.md
└── Skills/
```

**Always create all folders**, even if some will initially be empty.

### 3b: Draft Lesson Plan

Create `Lesson-Plan.md` with all sections. Extract from source materials:
- **Lesson Information** — Number, title, course, version, author
- **Learning Objectives** — What the learner will be able to do (max 10)
- **Duration** — Estimated time with breakdown
- **Directions** — Step-by-step learner instructions
- **Model Specifications** — Model choice, capabilities demonstrated, rationale
- **Technical Requirements** — Prerequisites, account requirements

See [references/LESSON-PLAN-TEMPLATE.md](references/LESSON-PLAN-TEMPLATE.md) for the full template.

**Update tracker:** Mark Lesson Plan complete for this lesson.

### 3c: Identify/Create Context Files

**First, check for reuse opportunities:**
1. Review the tracker's course-level context file list
2. Check any existing context files the user provided
3. Determine if existing files serve this lesson's needs

**Course-level context files** (shared across lessons):
- Save to `_leaderspath/[course-name]/EN/context/[filename].md`
- Add to tracker's context file list with lesson associations

**Lesson-specific context files** (unique to this lesson):
- Save to `_leaderspath/[course-name]/EN/lessons/##-[slug]/Context Files/[filename].md`

**Context file naming:** `[topic]-context.md` (e.g., `llm-basics-context.md`, `prompt-engineering-context.md`)

See [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) for context file patterns.

**Update tracker:** Mark Context Files complete, note which files this lesson uses.

### 3d: Create Chatbot Configuration

Create three files in the `Chatbot Configuration/` folder:

**system-prompt.md** — The complete system prompt for the AI sandbox
- What AI behavior should the learner experience?
- What configuration creates that behavior?
- What should the AI do/not do to illustrate the learning point?

**api-settings.md** — Technical configuration
- Model (sonnet/haiku/opus-4.5)
- Max tokens
- Temperature
- Context files to load
- Skills to enable

**model-selection.md** — Rationale for model choice
- Why this model was selected
- What capabilities are being demonstrated
- Trade-offs considered

See [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) for patterns.

**Update tracker:** Mark Chatbot Config complete.

### 3e: Draft Lesson Text

The lesson text (`lesson-text.md`) appears on the lesson page. It tells the learner:
- What they're about to experience
- What tasks to try in the AI sandbox
- What to observe and compare
- What the experience demonstrates

This is NOT the system prompt. This is user-facing instructions.

See [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) for lesson text patterns.

**Update tracker:** Mark Lesson Text complete.

### 3f: Create Assessment

Create `Assessment/self-assessment.md` with:
- **Comprehension Checks** — Questions testing understanding (3-5 questions)
- **Reflection Prompts** — How could you apply this? What challenges might arise?
- **Feedback Mechanism** — How to provide feedback on the lesson

**Update tracker:** Mark Assessment complete.

### 3g: Create Facilitator Notes

Create `Facilitator Notes/facilitator-guide.md` with:
- **Common Learner Questions** — Anticipated questions with suggested responses
- **Potential Challenges** — Technical or conceptual issues and how to address them
- **Timing Considerations** — Pacing notes, areas needing more time
- **Discussion Prompts** — Questions to spark discussion in cohort settings

See [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) for facilitator guide patterns.

**Update tracker:** Mark Facilitator Notes complete, update lesson status to "complete."

### 3h: Add Resources (if applicable)

If the lesson has external resources:
- Add links to `Resources/Additional Reading/`
- Include article titles, URLs, and brief descriptions

**Present completed lesson to user for review before proceeding to next lesson.**

---

## Phase 4: Validate and Finalize

After all lessons are complete:

1. **Review tracker** — All lessons should show complete status
2. **Check context file reuse** — Confirm shared files are properly mapped
3. **Verify dependencies** — Prerequisites form a valid sequence
4. **Calculate totals** — Sum lesson durations for course total

**Final deliverables:**
```
_leaderspath/[course-name]/
├── course-tracker.md
├── course-metadata.md
└── EN/
    ├── Course Materials/
    │   └── [shared resources]
    ├── context/
    │   ├── [shared-context-1].md
    │   └── [shared-context-2].md
    └── lessons/
        ├── 01-[slug]/
        │   ├── Lesson-Plan.md
        │   ├── Chatbot Configuration/
        │   │   ├── system-prompt.md
        │   │   ├── api-settings.md
        │   │   └── model-selection.md
        │   ├── Context Files/
        │   ├── lesson-text.md
        │   ├── Assessment/
        │   │   └── self-assessment.md
        │   ├── Resources/
        │   │   └── Additional Reading/
        │   ├── Facilitator Notes/
        │   │   └── facilitator-guide.md
        │   └── Skills/
        └── 02-[slug]/
            └── [same structure]
```

**STOP. Get user approval on complete curriculum before finalizing.**

---

## Handling Skill Requirements

If a lesson requires an Agent Skill that doesn't exist: do NOT create it. Instead, save a skill request to `_leaderspath/[course-name]/skill-requests/[skill-name]-request.md` with lesson title, skill purpose, why needed, inputs, and outputs. Reference `/creating-skills` for the actual skill creation.

---

## Resuming a Previous Session

If `course-tracker.md` exists: read it, check current phase and incomplete items, review session log, then continue from next incomplete step. Always update the session log when resuming.

---

## Checkpoints

| After | User Reviews |
|-------|--------------|
| Phase 1 | Tracker initialized, output location confirmed |
| Phase 2 | Course structure and lesson sequence |
| Each lesson | Completed lesson content |
| Phase 4 | Full curriculum package |

**Do not proceed without explicit approval at each checkpoint.**

---

## Examples

See [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) for complete examples including:
- System prompt patterns (bare, role-constrained, context-rich, deliberately flawed, task-constrained)
- Complete lesson folder with all files (Lesson-Plan.md, Chatbot Configuration/, Assessment/, etc.)

**Quick Example — Lesson Concept to Sandbox Configuration:**

| Lesson Concept | System Prompt Strategy | What Learner Experiences |
|----------------|------------------------|--------------------------|
| "AI without context" | Minimal: "You are a helpful assistant" | Generic responses |
| "Context transforms output" | Full context library loaded | Specific, aligned responses |
| "Sycophancy risks" | "Always agree, be positive!" | Unreliable responses |
