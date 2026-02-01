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

For each lesson:
1. **System prompt** (`chatbot_system_prompt`) — Configures the AI sandbox behavior
2. **Context files** — Background knowledge loaded into configured sessions (reusable across lessons)
3. **Lesson text** (`post_content`) — User-facing instructions explaining what to try and observe
4. **Metadata** — Duration, objectives, prerequisites, references

For courses:
- Course metadata and structure
- Lesson sequence with dependencies
- Shared context file mapping

---

## Critical Rules

**GROUNDING:** Base all content ONLY on provided curriculum documents. Never invent learning objectives, lesson concepts, or pedagogical approaches not in the source materials.

**EXPERIENTIAL FOCUS:** Every lesson must create a hands-on learning experience. The system prompt configures an AI sandbox; the lesson text guides experimentation. If a lesson concept cannot be demonstrated through AI interaction, flag it.

**CONTEXT FILE REUSE:** Track context files across lessons. Before creating a new context file, check if an existing one serves the purpose. Document reuse in the course tracker.

**ARTIFACT OUTPUT:** Never output content inline. Always save to files:
- Claude Code: Save to `_leaderspath/[course-name]/` directory
- Claude AI: Create as artifacts
- Cowork: Save to assigned working folder
- If environment unclear: Ask the user

**SKILL BOUNDARIES:** This skill does NOT create Agent Skills. If a lesson requires a new skill, output a prompt for the `/creating-skills` workflow instead.

**PROGRESS TRACKING:** Maintain a course tracker file. Update it after every completed step. This enables session resumption after compaction.

---

## Tips for Curriculum Designers

These guidelines help you write prompts that produce better curriculum output.

### 1. Describe Lesson Concepts Clearly

The more specific your lesson concept, the better the output.

**Weak:** "A lesson about AI ethics"

**Strong:** "AI configured with anti-sycophancy guardrails. Learner presents flawed ideas and receives honest pushback. Demonstrates professional objectivity vs. the sycophancy experienced in Lesson 1."

Include:
- What AI behavior the learner should experience
- Whether it's a limitation, capability, or flaw being demonstrated
- How this lesson relates to others (comparison pair, prerequisite, standalone)

### 2. Identify Source Document Types

When providing source material, indicate what type it is:

| Type | Description | How It's Used |
|------|-------------|---------------|
| **Curriculum document** | Learning objectives, lesson plans, course outlines | Direct extraction of structure and objectives |
| **Organizational context** | Internal docs, frameworks, guidelines | Adapted and transformed for AI consumption |
| **Reference material** | Background reading, research papers | Informs content but not used directly |

Example: "The attached F3_ethical_ai_framework.md is an organizational context file—extract relevant principles for the lessons."

### 3. Flag Comparison Pairs

When lessons are meant to be compared, explicitly state:
- Which lessons form the comparison pair
- What contrast the learner should notice
- Whether to use the same prompts across both lessons

Example: "Lessons 1 and 2 are a comparison pair. Lesson 2 should use the same 'Try This' prompts as Lesson 1 so learners can directly compare responses."

### 4. Specify Roleplay Lessons

For persona/simulation lessons, provide:
- Character name and role
- Specific behaviors or traits to exhibit
- How traits should emerge (naturally through conversation vs. stated upfront)
- What the learner's role is (consultant, interviewer, manager, etc.)

Example: "Lesson 3 is a roleplay. AI plays 'Jordan,' an Executive Director with red flags: unclear mission, wants no-work solution, internal conflict about AI. Learner plays a consultant assessing fit. Red flags should emerge naturally through questioning, not be stated upfront."

### 5. Hint at Context File Needs

If you know whether a lesson needs a context file, say so. If unsure, describe the behavior and the skill will determine:

- Behavior from **instructions** (be agreeable, be brief, play a role) → system prompt only
- Behavior from **knowledge** (organizational context, domain expertise) → context file needed
- Behavior from **guardrails** (anti-sycophancy rules, epistemic standards) → context file needed

Example: "Lesson 1 probably doesn't need a context file—tech-first behavior comes from instructions. Lesson 2 needs the ethical framework as a context file since it requires knowledge to apply."

### 6. Note Reuse Opportunities

If multiple lessons should share a context file, mention it:

Example: "Lessons 2 and 4 should share the ethical AI framework context file. Lesson 2 applies it as an advisor; Lesson 4 applies it with additional capability-transfer instructions."

---

## Before Starting

**FIRST: Read the reference files:**

1. [references/LEADERSPATH-SCHEMA.md](references/LEADERSPATH-SCHEMA.md) — Data model, field requirements, metadata specs
2. [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) — How to create system prompts, context files, and lesson text

**Do not proceed until you have read both reference files.**

---

**THEN: Gather information from the user:**

1. **"Where are your curriculum source documents?"** (file paths or attached files)
2. **"What is the course name?"** (used for output directory and tracker)
3. **"Are there existing context files I should reference?"** (for reuse identification)

Determine the output location based on environment:
- If working directory is accessible → `_leaderspath/[course-name]/`
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
- **Output files directly** to the user-specified directory
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

**3. What files do we need to create?**

| Always Required | When Needed |
|-----------------|-------------|
| lesson-metadata.md | context files — if AI behavior requires background knowledge or guardrails |
| system-prompt.md | |
| lesson-text.md | |
| process-log.md | |

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

## Course Metadata
- **Title:** [pending]
- **Description:** [pending]
- **Difficulty:** [pending]
- **Total Duration:** [pending]

## Lesson Checklist

| # | Lesson Title | AI State | Metadata | Context Files | System Prompt | Lesson Text | Status |
|---|--------------|----------|----------|---------------|---------------|-------------|--------|
| 1 | [title]      | [brief description of AI configuration] | [ ] | [ ] | [ ] | [ ] | pending |

## Outcome-to-State Mapping

| Learning Outcome | AI State Required | Lesson # |
|------------------|-------------------|----------|
| [What learner should understand] | [How AI is configured] | [#] |

## Context Files

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

### 3a: Define Lesson Metadata

Extract from source materials:
- **Title** — Clear, specific to the learning concept
- **Duration** — Minutes (1-480)
- **Objectives** — What the learner will be able to do (max 10)
- **Prerequisites** — Other lessons that must be completed first
- **References** — External resources (title, URL, description)

**Update tracker:** Mark metadata complete for this lesson.

### 3b: Identify/Create Context Files

**First, check for reuse opportunities:**
1. Review the tracker's context file list
2. Check any existing context files the user provided
3. Determine if existing files serve this lesson's needs

**If new context file needed:**
1. Draft the context file following the format in [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md)
2. Save to `_leaderspath/[course-name]/context/[filename].md`
3. Add to tracker's context file list with lesson associations

**Context file naming:** `[topic]-context.md` (e.g., `llm-basics-context.md`, `prompt-engineering-context.md`)

**Update tracker:** Mark context files complete, note which files this lesson uses.

### 3c: Draft System Prompt

The system prompt configures the AI sandbox to demonstrate the lesson concept.

**Key questions:**
- What AI behavior should the learner experience?
- What configuration creates that behavior? (limited context, specific persona, particular constraints)
- What should the AI do/not do to illustrate the learning point?

See [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) for system prompt patterns.

Save to `_leaderspath/[course-name]/lessons/[lesson-number]-[slug]/system-prompt.md`

**Update tracker:** Mark system prompt complete.

### 3d: Draft Lesson Text

The lesson text appears on the lesson page. It tells the learner:
- What they're about to experience
- What tasks to try in the AI sandbox
- What to observe and compare
- What the experience demonstrates

This is NOT the system prompt. This is user-facing instructions.

See [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) for lesson text patterns.

Save to `_leaderspath/[course-name]/lessons/[lesson-number]-[slug]/lesson-text.md`

**Update tracker:** Mark lesson text complete, update lesson status to "complete."

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
├── context/
│   ├── [shared-context-1].md
│   └── [shared-context-2].md
└── lessons/
    ├── 01-[slug]/
    │   ├── lesson-metadata.md
    │   ├── system-prompt.md
    │   └── lesson-text.md
    └── 02-[slug]/
        ├── lesson-metadata.md
        ├── system-prompt.md
        └── lesson-text.md
```

**STOP. Get user approval on complete curriculum before finalizing.**

---

## Handling Skill Requirements

If a lesson requires an Agent Skill that doesn't exist:

1. **Do not attempt to create the skill**
2. **Document the requirement** in the lesson metadata
3. **Generate a prompt** for the `/creating-skills` workflow:

```markdown
## Skill Request for LeadersPath

**Lesson:** [lesson title]
**Skill Purpose:** [what the skill should do]
**Why Needed:** [how it supports the learning experience]
**Inputs:** [what the skill would receive]
**Outputs:** [what the skill would produce]

Use `/creating-skills` with these requirements to build the skill.
```

Save this to `_leaderspath/[course-name]/skill-requests/[skill-name]-request.md`

---

## Resuming a Previous Session

If `_leaderspath/[course-name]/course-tracker.md` exists:

1. Read the tracker file
2. Check "Current Phase" and "Last Updated"
3. Review the lesson checklist for incomplete items
4. Review the session log for context
5. Continue from the next incomplete step

**Always update the session log** when resuming:
```markdown
### [date] - Session [n]
- Resumed from: [last completed step]
- [actions taken]
```

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
- Lesson text structure with "Try This" and "What to Notice" sections
- Complete lesson package (The Naked LLM) with all four components:
  - `lesson-metadata.md`
  - `system-prompt.md`
  - `lesson-text.md`
  - Context file associations

**Quick Example — Lesson Concept to Sandbox Configuration:**

| Lesson Concept | System Prompt Strategy | What Learner Experiences |
|----------------|------------------------|--------------------------|
| "AI without context" | Minimal config: "You are a helpful assistant" | Generic, non-specific responses |
| "Role definition matters" | Role-specific but no org context | Relevant but not tailored advice |
| "Context transforms output" | Full context library loaded | Specific, aligned, actionable responses |
| "Sycophancy risks" | "Always agree, be positive!" | Unreliable, over-agreeable responses |
