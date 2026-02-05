---
name: designing-leaderspath-cohorts
description: Designs LeadersPath cohort curricula from source materials (interview transcripts, organizational docs, learning objectives). Creates cohort structure, searches for reusable courses, and outputs course curriculum prompts for the building-leaderspath-curriculum skill. Use when designing a new cohort, planning a learning program, or creating curriculum from interview or design materials. Activates when cohort design materials are provided via file path, attached file, or uploaded document.
---

# Designing LeadersPath Cohorts

<purpose>
Claude's default when given curriculum design tasks is to jump straight to creating
course content. This skill exists because cohort design requires upstream analysis—
understanding learning themes, searching for reusable courses, and sequencing before
any course content is written. The skill enforces this separation by producing
curriculum prompts (design documents) rather than curriculum content.
</purpose>

Design cohort curricula for LeadersPath facilitated learning experiences.

## What This Skill Does

This skill transforms source materials into a complete cohort design with course curriculum prompts. It sits upstream of `building-leaderspath-curriculum`:

```
Source Materials → [THIS SKILL] → Cohort Design + Course Curriculum Prompts
                                            ↓
                        [building-leaderspath-curriculum]
                                            ↓
                        Facilitator Guides, Activities, Learner Materials
```

**Output:**
1. **Cohort Curriculum** — Structure, sequencing, target audience, duration
2. **Course Curriculum Prompts** — One per course, ready for `building-leaderspath-curriculum`
3. **Course Reuse Report** — Which existing courses can be used vs. created new

---

## Critical Rules

**GROUNDING:** Base all content ONLY on provided source materials. Never invent learning objectives, topics, or pedagogical approaches not supported by the source.

**COURSE REUSE:** Before designing new courses, ALWAYS search for existing courses that could serve the cohort's learning goals. Reuse is preferred over creation.

**ATOMIC COURSES:** Courses must be self-contained teaching units. Course curriculum prompts must NOT reference other courses. Sequencing belongs in the cohort curriculum, not individual courses.

**CURRICULUM PROMPTS, NOT IMPLEMENTATION:** This skill creates prompts that tell `building-leaderspath-curriculum` what to build. Do NOT specify system prompts, activity instructions, or folder structures. Focus on learning outcomes and experiences.

**ARTIFACT OUTPUT:** Never output content inline. Always save to files in the working folder.

**PROGRESS TRACKING:** Maintain a cohort tracker file. Update after every completed step.

**PROFESSIONAL OBJECTIVITY:** If source materials contain unclear or contradictory learning goals, surface the issue rather than inventing a resolution. Ask for clarification rather than making assumptions.

---

## Additional Resources

For detailed guidance, see:
- [references/CURRICULUM-PROMPT-GUIDE.md](references/CURRICULUM-PROMPT-GUIDE.md) — How to write effective course curriculum prompts
- [references/COURSE-SEARCH-GUIDE.md](references/COURSE-SEARCH-GUIDE.md) — How to search for and evaluate existing courses
- [../building-leaderspath-curriculum/references/NAMING-SYSTEM.md](../building-leaderspath-curriculum/references/NAMING-SYSTEM.md) — Course ID, Activity ID, and Context File naming conventions

---

## Before Starting

**FIRST: Gather information from the user:**

1. **"Where are your source materials?"** (interview transcripts, design docs, organizational materials)
2. **"What is the cohort name?"** (used for tracker and curriculum files)
3. **"Who is the target audience?"** (nonprofit leaders, developers, executives, etc.)
4. **"What is the desired duration?"** (number of sessions, weeks, hours)
5. **"Are there existing courses I should check for reuse?"** (file paths or course library location)
6. **"Do you have an existing course-id-log.md?"** (optional)

   If provided:
   - Read to check existing Course IDs and avoid conflicts
   - Note which topic-level combinations are already used

   If not provided:
   - Skill will create a new log as part of output

**Topic and Level Code Reference** (for assigning Course IDs):

When assigning Course IDs in Phase 4, use these codes:

**Topic codes:**
- `FUND` - Fundamentals (how AI works, capabilities, limitations)
- `PRMPT` - Prompting (interaction techniques, effective prompting)
- `CTX` - Context & Knowledge (context libraries, organizational knowledge)
- `ETH` - Ethics & Responsibility (bias, transparency, responsible use)
- `APP` - Applications (writing, research, analysis, communication)

**Level codes:**
- `101-199` - Foundations/Beginner
- `201-299` - Intermediate
- `301-399` - Advanced
- `401+` - Specialized/Expert

If a course doesn't fit neatly, use the closest match or ask user.

**THEN: Identify working folder:**
- Look for a mounted/selected folder in the environment
- If Cowork: use assigned working folder
- If Claude Code: use current directory
- If unclear: ask the user

Output directly to the working folder. No wrapper folders.

---

## Workflow Overview

```
Phase 1: Initialize & Analyze Sources
    ├── Create cohort tracker
    ├── Read and analyze source materials
    └── Extract learning themes and objectives
    ↓
Phase 2: Search for Existing Courses
    ├── Search course library (if provided)
    ├── Match existing courses to learning objectives
    └── Create course reuse report
    ↓
Phase 3: Design Cohort Structure
    ├── Define audience and duration
    ├── Sequence courses (existing + new)
    └── Create cohort curriculum document
    ↓
Phase 4: Create Course Curriculum Prompts
    ├── For each NEW course needed
    └── Output atomic curriculum prompts
    ↓
Phase 5: Validate and Finalize
```

---

<phase_initialize>
## Phase 1: Initialize & Analyze Sources

### 1a: Create Cohort Tracker

Create `cohort-tracker.md` in the working folder:

```markdown
# Cohort Tracker: [Cohort Name]

**Created:** [date]
**Last Updated:** [date]
**Current Phase:** 1 - Initialization

## Source Materials
| File | Type | Status |
|------|------|--------|
| [filename] | [transcript/doc/notes] | [ ] analyzed |

## Learning Themes Identified
1. [Theme from analysis]
2. ...

## Course Plan
| Course ID | Course Name | Source | Status |
|-----------|-------------|--------|--------|
| TOPIC-LEVEL-slug | [name] | [existing/new] | [ ] |

## Session Log
### [date] - Session 1
- Initialized tracker
- [next actions]
```

### 1b: Analyze Source Materials

Read all source materials and extract:

1. **Learning themes** — Major topics that should be covered
2. **Key concepts** — Specific ideas, frameworks, or skills mentioned
3. **Target outcomes** — What learners should be able to do after
4. **Suggested activities** — Any hands-on experiences mentioned
5. **Quotes/examples** — Concrete material to reference in courses

Document findings in the tracker under "Learning Themes Identified."

**Update tracker:** Mark source materials as analyzed.

**GATE:** Before proceeding to Phase 2, write:
- "I have analyzed [N] source files: [list them]"
- "Learning themes identified: [list themes]"
</phase_initialize>

---

<phase_search>
## Phase 2: Search for Existing Courses

**REQUIRED:** Before creating new courses, search for existing ones.

### 2a: Search Course Library

If user provided a course library location:

1. List all course curriculum files (pattern: `*-curriculum.md`)
2. Read each course's learning objectives and description
3. Compare against identified learning themes

If no course library provided:
1. Ask user: "Is there an existing course library I should search?"
2. If no: proceed to Phase 3 (all courses will be new)

### 2b: Create Course Reuse Report

Create `[cohort-name]/course-reuse-report.md`:

```markdown
# Course Reuse Report: [Cohort Name]

## Existing Courses That Fit

| Course | File | Covers Themes | Gaps |
|--------|------|---------------|------|
| [name] | [path] | [themes 1, 3] | [missing X] |

## Courses to Create New

| Course | Themes Covered | Rationale |
|--------|----------------|-----------|
| [name] | [themes 2, 4] | [why not reusing] |

## Recommendations

[Summary of which courses to reuse, which to create, and any adaptations needed]
```

**Update tracker:** Add course plan with existing/new designations.

**GATE:** Before proceeding to Phase 3, write:
- "Courses to reuse: [list or 'none']"
- "Courses to create new: [list]"

**STOP.** Present course reuse report and get user approval before proceeding.
</phase_search>

---

<phase_design>
## Phase 3: Design Cohort Structure

### 3a: Create Cohort Curriculum

Create `cohort-curriculum.md` in the working folder:

```markdown
# Cohort Curriculum: [Cohort Name]

## Cohort Overview

**Cohort Name:** [Name]
**Duration:** [X weeks / sessions]
**Format:** Live facilitated sessions with AI sandbox activities
**Target Audience:** [Description]

---

## Learning Goals

After completing this cohort, learners will be able to:

1. [Goal 1]
2. [Goal 2]
...

---

## Course Sequence

| Week | Course ID | Course Name | Focus | Source |
|------|-----------|-------------|-------|--------|
| 1 | FUND-101-ai-basics | AI Foundations | Conceptual grounding | new |
| 2 | PRMPT-101-intro-prompting | Introduction to Prompting | Prompting basics | new |
...

---

## Demo Context (if applicable)

**Organization:** [Name]
**Context files:** [list CTX###-slug.md files]
**Used in:** [which courses]

---

## Curriculum Files

| Course ID | File |
|-----------|------|
| FUND-101-ai-basics | `Courses/FUND-101-ai-basics-curriculum.md` |
...

---

## Using building-leaderspath-curriculum

1. Invoke the skill
2. Provide the course curriculum file and Course ID
3. Provide any referenced context files
4. The skill creates facilitator guides, activities, learner materials

Work course-by-course for best results.
```

**Update tracker:** Mark cohort curriculum complete.

**GATE:** Before proceeding to Phase 4, write:
- "Cohort structure: [number] courses over [duration]"
- "Course sequence: [brief list]"
</phase_design>

---

<phase_prompts>
## Phase 4: Create Course Curriculum Prompts

For each NEW course (not reused), create a curriculum prompt file.

### Assign Course ID

For each new course:

1. **Select Topic Code:** FUND, PRMPT, CTX, ETH, or APP (closest match)
2. **Select Level:** 101-199 (beginner), 201-299 (intermediate), 301-399 (advanced), 401+ (specialized)
3. **Generate Slug:** From course name, kebab-case, 3-50 chars

**Example:** "AI Foundations" for beginners → `FUND-101-ai-foundations`

If course-id-log.md was provided, check for conflicts before assigning.

### Course Curriculum Prompt Template

Create `Courses/TOPIC-LEVEL-slug-curriculum.md`:

```markdown
# Course: [Course Name] — Curriculum Prompt

**Course ID:** [TOPIC-LEVEL-slug]

## Course Overview

**Course Name:** [Name]
**Difficulty:** [Beginner / Intermediate / Advanced]
**Prerequisites:** [None / Other courses recommended]
**Estimated Duration:** [X minutes]

**Description:** [What learners will experience and why it matters]

---

## Course Learning Objectives

After completing this course, learners will be able to:

1. [Objective 1 — action verb + measurable outcome]
2. [Objective 2]
...

---

## Source Documents

**Primary curriculum source:**
* [filename.md] — [brief description]

**Context files for activities (if applicable):**
* [filename.md] — [what it provides]

**Online resources to link (if applicable):**
* "[Article Title]" ([path]) — [brief description]

---

## Course Design

**Course type:** [Facilitated presentation / Hands-on comparison / Discussion-based / etc.]

[Brief description of pedagogical approach]

**Include Course Q&A Bot:** [Yes / No]

[If yes, describe what the Q&A bot should help with]

---

## Key Concepts from Source Material

### [Concept 1]
[Explanation grounded in source material]

### [Concept 2]
[Explanation grounded in source material]

---

## Required Experiences

### [Experience/Activity Name]

**What learners should experience:**
* [Observable outcome 1]
* [Observable outcome 2]

**Context files:** [List or "None"]

**[Any suggested prompts or approaches]**

---

[Repeat for each major experience/activity]
```

### What TO Include

* Learning objectives (course level)
* What experiences learners should have
* What concepts should be covered
* Which context files to use
* Whether to include Q&A bot (and what it covers)
* Key quotes or concepts from source material
* Suggested comparison pairs (if applicable)

### What NOT to Include

* System prompts (skill generates those)
* Activity instructions (skill generates those)
* Facilitator notes (skill generates those)
* Folder structures (skill decides those)
* References to other courses (breaks atomicity)

**Update tracker:** Mark each course curriculum prompt complete.

**Log Course ID assignments:**

After creating each curriculum prompt, output a course-id-log entry (append to provided log or create new `course-id-log.md`):

```markdown
## [TOPIC] - [Topic Name]

| ID | Slug | Title | Date Assigned | Status | Notes |
|----|------|-------|---------------|--------|-------|
| TOPIC-LEVEL | slug | Course Title | [date] | Design | Part of [Cohort Name] |
```

**Present each course for review before proceeding to next.**

**GATE:** Before proceeding to Phase 5, write:
- "Course curriculum prompts created: [list files with Course IDs]"
- "Course IDs logged: [count]"
- "All courses approved: [yes/pending]"
</phase_prompts>

---

<phase_validate>
## Phase 5: Validate and Finalize

After all content is complete:

1. **Review tracker** — All items complete
2. **Verify atomicity** — No course references another course
3. **Check coverage** — All learning themes addressed
4. **Confirm sequencing** — Cohort curriculum sequences make sense

**Final deliverables:**
```
[working-folder]/
├── cohort-tracker.md
├── cohort-curriculum.md
├── course-reuse-report.md
├── course-id-log.md              # New/updated entries
└── Courses/
    ├── FUND-101-ai-basics-curriculum.md
    ├── PRMPT-101-intro-prompting-curriculum.md
    └── ...
```

**GATE:** Before finalizing, write:
- "All deliverables created: [list files]"
- "Atomicity verified: [yes/issues found]"
- "Theme coverage: [all themes addressed / gaps]"

**STOP.** Present complete package and get user approval before finalizing.
</phase_validate>

---

## Checkpoints

| After | User Reviews |
|-------|--------------|
| Phase 1 | Learning themes extracted from sources |
| Phase 2 | Course reuse recommendations |
| Phase 3 | Cohort structure and sequencing |
| Each course prompt | Individual curriculum prompts |
| Phase 5 | Complete cohort package |

**Do not proceed without explicit approval at each checkpoint.**

---

<failed_attempts>
What DOESN'T work:

- **Creating course content instead of curriculum prompts:** This skill outputs design documents, not facilitator guides or activity instructions. Those are created by `building-leaderspath-curriculum`.
- **Courses that reference each other:** "Builds on Course 2" breaks atomicity. Courses must be self-contained. Express dependencies as prerequisites in the course overview, not cross-references.
- **Skipping the course reuse search:** Even when no library exists, document that you searched. Otherwise future cohorts lose reuse opportunities.
- **Generating learning themes without sources:** All themes must trace back to provided materials. No invented pedagogy or assumed learning objectives.
- **Specifying implementation details:** System prompts, activity instructions, folder structures—these belong in `building-leaderspath-curriculum`, not curriculum prompts.
</failed_attempts>

---

## Resuming a Previous Session

If `cohort-tracker.md` exists:
1. Read it
2. Check current phase and incomplete items
3. Review session log
4. Continue from next incomplete step
5. Update session log when resuming

---

## Examples

### Example: Cohort Design from Interview Transcript

**Input:** Interview transcript about AI ethics training for nonprofit leaders

**Phase 1 output (learning themes):**
- LLM fundamentals and misconceptions
- Sycophancy problem and honest AI
- Context libraries and organizational knowledge
- Skills and packaged processes
- Personal reflection and leadership
- Ethical frameworks for AI use

**Phase 2 output (course reuse report):**
```
Existing courses found: 0
Recommendation: Create 6 new courses
```

**Phase 3 output (cohort curriculum excerpt):**
```markdown
## Course Sequence

| Week | Course ID | Course Name | Focus | Source |
|------|-----------|-------------|-------|--------|
| 1 | FUND-101-ai-foundations | AI Foundations | Conceptual grounding | new |
| 2 | FUND-102-behavioral-training | Behavioral Training | Sycophancy, prose quality | new |
| 3 | CTX-101-context-libraries | Context Libraries | Organizational knowledge | new |
```

**Phase 4 output (course curriculum prompt excerpt):**
```markdown
# Course: AI Foundations — Curriculum Prompt

**Course ID:** FUND-101-ai-foundations

## Course Learning Objectives

After completing this course, learners will be able to:

1. Distinguish LLMs from other AI types
2. Explain the jazz ensemble metaphor for how LLMs work
3. Articulate the sycophancy problem

## Required Experiences

### Experience: Concept Explorer Q&A

**What learners should experience:**
* Conversational exploration of course concepts
* Answers grounded in course material

**Include Course Q&A Bot:** Yes
```

---

## Relationship to Other Skills

**This skill outputs prompts for:**
- `building-leaderspath-curriculum` — Takes course curriculum prompts, creates full course content

**This skill may reference:**
- `building-context-libraries` — If a demo context is needed
- `synthesizing-interviews` — If source is a raw transcript

**This skill does NOT:**
- Create system prompts, activity instructions, or facilitator guides (that's `building-leaderspath-curriculum`)
- Create context libraries (that's `building-context-libraries`)
- Create Agent Skills (that's `creating-skills`)
