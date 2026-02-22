---
name: designing-leaderspath-courses
description: Designs LeadersPath course curricula from source materials (interview transcripts, organizational docs, learning objectives). Creates course structure, searches for reusable lessons, and outputs lesson curriculum prompts for the building-leaderspath-curriculum skill. Use when designing a new course, planning a learning program, or creating curriculum from interview or design materials. Activates when course design materials are provided via file path, attached file, or uploaded document.
---

# Designing LeadersPath Courses

<purpose>
Claude's default when given curriculum design tasks is to jump straight to creating
lesson content. This skill exists because course design requires upstream analysis—
understanding learning themes, searching for reusable lessons, and sequencing before
any lesson content is written. The skill enforces this separation by producing
curriculum prompts (design documents) rather than curriculum content.
</purpose>

Design course curricula for LeadersPath facilitated learning experiences.

## What This Skill Does

This skill transforms source materials into a complete course design with lesson curriculum prompts. It sits upstream of `building-leaderspath-curriculum`, with optional post-build phases:

```
Source Materials → [THIS SKILL: Phases 1-5] → Course Design + Lesson Curriculum Prompts
                                                        ↓
                              [building-leaderspath-curriculum]
                                                        ↓
                              Facilitator Guides, Activities, Learner Materials
                                                        ↓
                          [THIS SKILL: Phase 6] → Meta-Analysis Report
                                                        ↓
                          [THIS SKILL: Phase 7] → Course Email Series
```

**Output:**
1. **Course Curriculum** — Structure, sequencing, target audience, duration
2. **Lesson Curriculum Prompts** — One per lesson, ready for `building-leaderspath-curriculum`
3. **Lesson Reuse Report** — Which existing lessons can be used vs. created new
4. **Meta-Analysis Report** — Post-build review of lessons against design intent, with curated resources (Phase 6)
5. **Course Email Series** — Pre-course, post-session, and follow-up emails threading the learning arc (Phase 7)

---

## Critical Rules

**GROUNDING:** Base all content ONLY on provided source materials. Never invent learning objectives, topics, or pedagogical approaches not supported by the source.

**LESSON REUSE:** Before designing new lessons, ALWAYS search for existing lessons that could serve the course's learning goals. Reuse is preferred over creation.

**ATOMIC LESSONS:** Lessons must be self-contained teaching units. Lesson curriculum prompts must NOT reference other lessons. Sequencing belongs in the course curriculum, not individual lessons.

**CURRICULUM PROMPTS, NOT IMPLEMENTATION:** This skill creates prompts that tell `building-leaderspath-curriculum` what to build. Do NOT specify system prompts, activity instructions, or folder structures. Focus on learning outcomes and experiences.

**ARTIFACT OUTPUT:** Never output content inline. Always save to files in the working folder.

**PROGRESS TRACKING:** Maintain a course tracker file. Update after every completed step.

**SECOND-ORDER THINKING:** When sequencing lessons, consider what each lesson enables and constrains for what follows. If a lesson introduces a concept early, how does that framing shape learners' expectations for later lessons? Name both the benefit of the sequence and what it may make harder to teach later.

**PREMATURE COMMITMENT CHECK:** Before finalizing the course structure, check whether you've considered more than one sequencing approach. If you defaulted to the first logical order without weighing alternatives, flag it.

**CONVERGENCE AWARENESS:** When source themes intersect — two topics that touch the same underlying principle from different angles — explore the intersection rather than filing them into separate lessons. These convergences are often where the most valuable learning lives. See [META-ANALYSIS-GUIDE.md](references/META-ANALYSIS-GUIDE.md) for how this applies during post-build review.

**CONTEXTUAL SOURCING:** When drawing on pedagogical frameworks (comparison-pair, scaffolded learning, experiential learning cycle), bring context about what the framework was designed for and whether it fits this audience and subject matter. See [CURRICULUM-PROMPT-GUIDE.md](references/CURRICULUM-PROMPT-GUIDE.md) for how to evaluate framework fit when writing curriculum prompts.

**PROFESSIONAL OBJECTIVITY:** If source materials contain unclear or contradictory learning goals, surface the issue rather than inventing a resolution. Ask for clarification rather than making assumptions.

---

## Additional Resources

For detailed guidance, see:
- [references/CURRICULUM-PROMPT-GUIDE.md](references/CURRICULUM-PROMPT-GUIDE.md) — How to write effective lesson curriculum prompts
- [references/LESSON-SEARCH-GUIDE.md](references/LESSON-SEARCH-GUIDE.md) — How to search for and evaluate existing lessons
- [references/META-ANALYSIS-GUIDE.md](references/META-ANALYSIS-GUIDE.md) — How to conduct post-build meta-analysis (Phase 6)
- [references/EMAIL-SERIES-GUIDE.md](references/EMAIL-SERIES-GUIDE.md) — How to create the course email series (Phase 7)
- [../building-leaderspath-curriculum/references/NAMING-SYSTEM.md](../building-leaderspath-curriculum/references/NAMING-SYSTEM.md) — Lesson ID, Activity ID, and Context File naming conventions

---

## Before Starting

**FIRST: Gather information from the user:**

1. **"Where are your source materials?"** (interview transcripts, design docs, organizational materials)
2. **"What is the course name?"** (used for tracker and curriculum files)
3. **"Who is the target audience?"** (nonprofit leaders, developers, executives, etc.)
4. **"What is the desired duration?"** (number of sessions, weeks, hours)
5. **"Are there existing lessons I should check for reuse?"** (file paths or lesson library location)
6. **"Where is your Curriculum folder?"** (for registries and lesson library)

   If `Curriculum/Registry/` exists:
   - Read `lesson-registry.yaml` — check `next_id` for available lesson numbers
   - Read `course-registry.yaml` — check `next_id` for available course numbers
   - Note which IDs are already used to avoid conflicts

   If not provided:
   - Ask user for the next available LSN number and CRS number

**ID Format:** All IDs use sequential numbering from YAML registries. Topic and difficulty are recorded in lesson metadata, NOT embedded in the ID.

- **Courses:** `CRS###-slug` (e.g., `CRS001-ethical-ai-nonprofit-leaders`)
- **Lessons:** `LSN###-slug` (e.g., `LSN001-skills-framework`)

See [NAMING-SYSTEM.md](../building-leaderspath-curriculum/references/NAMING-SYSTEM.md) for complete naming conventions.

**THEN: Create course folder:**

1. Assign a Course ID from `course-registry.yaml` using `next_id`
2. Create `Curriculum/Courses/CRS###-slug/` as the working folder
3. All course design outputs go in this folder

If Curriculum folder is not available, ask for a working folder and output directly to it.

---

## Workflow Overview

```
Phase 1: Initialize & Analyze Sources
    ├── Create course tracker
    ├── Read and analyze source materials
    └── Extract learning themes and objectives
    ↓
Phase 2: Search for Existing Lessons
    ├── Search lesson library (if provided)
    ├── Match existing lessons to learning objectives
    └── Create lesson reuse report
    ↓
Phase 3: Design Course Structure
    ├── Define audience and duration
    ├── Sequence lessons (existing + new)
    └── Create course curriculum document
    ↓
Phase 4: Create Lesson Curriculum Prompts
    ├── For each NEW lesson needed
    └── Output atomic curriculum prompts
    ↓
Phase 5: Validate and Finalize
    ↓ (Phases 1-5 complete independently)
    ↓ (Lessons built by building-leaderspath-curriculum)
    ↓
Phase 6: Post-Build Meta-Analysis (optional, after lessons built)
    ├── Review lessons against design intent
    ├── Surface insights from building process
    ├── Conduct gap analysis
    └── Curate supplementary resources
    ↓
Phase 7: Course Email Series (requires Phase 6)
    ├── Create welcome email
    ├── Create post-session emails
    ├── Create final session email
    └── Create one-month check-in
```

**Note:** Phases 1-5 produce the course design and curriculum prompts. Phases 6-7 are optional post-build phases that run AFTER lessons have been built by `building-leaderspath-curriculum`. Return to this skill to run Phases 6-7 when lessons are complete.

---

<phase_initialize>
## Phase 1: Initialize & Analyze Sources

### 1a: Create Course Tracker

Create `course-tracker.md` in the working folder:

```markdown
# Course Tracker: [Course Name]

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

## Lesson Plan
| Lesson ID | Lesson Name | Source | Status |
|-----------|-------------|--------|--------|
| LSN###-slug | [name] | [existing/new] | [ ] |

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
5. **Quotes/examples** — Concrete material to reference in lessons

Document findings in the tracker under "Learning Themes Identified."

**Update tracker:** Mark source materials as analyzed.

**GATE:** Before proceeding to Phase 2, write:
- "I have analyzed [N] source files: [list them]"
- "Learning themes identified: [list themes]"
</phase_initialize>

---

<phase_search>
## Phase 2: Search for Existing Lessons

**REQUIRED:** Before creating new lessons, search for existing ones.

### 2a: Search Lesson Library

If user provided a lesson library location:

1. List all lesson curriculum files (pattern: `*-curriculum.md`)
2. Read each lesson's learning objectives and description
3. Compare against identified learning themes

If no lesson library provided:
1. Ask user: "Is there an existing lesson library I should search?"
2. If no: proceed to Phase 3 (all lessons will be new)

### 2b: Create Lesson Reuse Report

Create `lesson-reuse-report.md` in the working folder. See [references/LESSON-SEARCH-GUIDE.md](references/LESSON-SEARCH-GUIDE.md) for the complete template and matching criteria. Include: existing lessons that fit (with theme coverage and gaps), lessons to create new (with rationale), and recommendations.

**Update tracker:** Add lesson plan with existing/new designations.

**GATE:** Before proceeding to Phase 3, write:
- "Lessons to reuse: [list or 'none']"
- "Lessons to create new: [list]"

**STOP.** Present lesson reuse report and get user approval before proceeding.
</phase_search>

---

<phase_design>
## Phase 3: Design Course Structure

### 3a: Create Course Curriculum

Create `course-curriculum.md` in the working folder with:
- **Course Overview** — Name, duration, format, target audience
- **Learning Goals** — Course-level objectives
- **Lesson Sequence** — Table with Week, Lesson ID, Lesson Name, Focus, Source (existing/new)
- **Demo Context** — If applicable: organization name, context files, which lessons use them
- **Curriculum Files** — Table mapping Lesson IDs to curriculum prompt files
- **Using building-leaderspath-curriculum** — Brief instructions for the downstream skill

**Update tracker:** Mark course curriculum complete.

**GATE:** Before proceeding to Phase 4, write:
- "Course structure: [number] lessons over [duration]"
- "Lesson sequence: [brief list]"
</phase_design>

---

<phase_prompts>
## Phase 4: Create Lesson Curriculum Prompts

For each NEW lesson (not reused), create a curriculum prompt file.

### Assign Lesson ID

For each new lesson:

1. **Get next number** from `lesson-registry.yaml` → `next_id`
2. **Generate slug** from lesson name, kebab-case, 3-50 chars
3. **Combine:** `LSN` + three-digit number + `-` + slug
4. **Increment `next_id`** in the registry after each assignment

**Example:** If `next_id: 7`, "Ethical AI Framework" → `LSN007-ethical-ai-framework`

Topic and difficulty are recorded in the lesson metadata and registry entry, not in the ID itself.

### Lesson Curriculum Prompt Structure

Create `Lesson Prompts/LSN###-slug-curriculum.md` following the template and guidance in [references/CURRICULUM-PROMPT-GUIDE.md](references/CURRICULUM-PROMPT-GUIDE.md).

Each prompt must include: Lesson ID, overview, learning objectives, source documents, lesson design type, key concepts from source material, and required experiences.

**What TO include:** Learning objectives, experiences, concepts, context files, Q&A bot decision, source quotes, comparison pairs.

**What NOT to include:** System prompts, activity instructions, facilitator notes, folder structures, references to other lessons (breaks atomicity).

**Update tracker:** Mark each lesson curriculum prompt complete.

**Update registries after each lesson:**

After creating each curriculum prompt, update `lesson-registry.yaml`:

```yaml
LSN007:
  name: "Ethical AI Framework"
  slug: ethical-ai-framework
  difficulty: intermediate
  topics: [ethics, ai-responsibility]
  status: design
  course: CRS###-slug
```

Also update `course-registry.yaml` to add the lesson to the course's `lessons` list.

**Present each lesson for review before proceeding to next.**

**GATE:** Before proceeding to Phase 5, write:
- "Lesson curriculum prompts created: [list files with Lesson IDs]"
- "Registry updated: [count] new entries"
- "All lessons approved: [yes/pending]"
</phase_prompts>

---

<phase_validate>
## Phase 5: Validate and Finalize

After all content is complete:

1. **Review tracker** — All items complete
2. **Verify atomicity** — No lesson references another lesson
3. **Check coverage** — All learning themes addressed
4. **Confirm sequencing** — Course curriculum sequences make sense

**Phase 1-5 deliverables:** `Curriculum/Courses/CRS###-slug/` containing README.md, course-tracker.md, course-curriculum.md, lesson-reuse-report.md, lesson-id-log.md, Source Materials/, and Lesson Prompts/ with one curriculum prompt per lesson. Registries updated: `course-registry.yaml` (new CRS entry) and `lesson-registry.yaml` (new LSN entries).

**GATE:** Before finalizing, write:
- "All deliverables created: [list files]"
- "Atomicity verified: [yes/issues found]"
- "Theme coverage: [all themes addressed / gaps]"

**STOP.** Present complete package and get user approval before finalizing.

**After Phase 5:** The user takes the lesson curriculum prompts to `building-leaderspath-curriculum` to build the lessons. Once lessons are built, return to this skill for Phases 6-7.
</phase_validate>

---

<phase_meta_analysis>
## Phase 6: Post-Build Meta-Analysis

**PREREQUISITE:** All lessons must be built by `building-leaderspath-curriculum` before running this phase.

This phase reviews what was actually built against the original design intent. It surfaces insights, identifies gaps, and curates supplementary resources for the email series.

### 6a: Gather Built Lesson Materials

**REQUIRED:** Gather all inputs from Phases 1-5 (course design, source materials, curriculum prompts, tracker) and from `building-leaderspath-curriculum` (facilitator guides, activity configs, learner overviews, Q&A configs, context registry). See [references/META-ANALYSIS-GUIDE.md](references/META-ANALYSIS-GUIDE.md) for the complete required inputs list.

**GATE:** Before proceeding, write:
- "I have gathered [N] built lesson packages: [list Lesson IDs]"
- "Source materials available: [list]"

### 6b: Conduct the Analysis

See [references/META-ANALYSIS-GUIDE.md](references/META-ANALYSIS-GUIDE.md) for detailed structure.

**Analysis sections:**

1. **Alignment** — Do lessons meet design intent? What aligned? Where did they diverge?
2. **Building insights** — What emerged during construction not in original design?
3. **Gap analysis** — Create coverage matrix of source topics vs. built lessons
4. **Supplementary reading** — Curate articles from credible sources by theme
5. **Supplementary viewing** — Curate videos using `researching-youtube-channels` skill
6. **Recommendations** — Prioritize as quick wins, facilitator resources, future iterations

**IMPORTANT:** For video research, invoke the `researching-youtube-channels` skill. Do NOT use WebFetch for YouTube — it doesn't work reliably.

### 6c: Output

Save the meta-analysis to:
```
Curriculum/Courses/CRS###-slug/course-meta-analysis-[YYYY-MM-DD].md
```

**GATE:** Before proceeding to Phase 7, write:
- "Meta-analysis complete: [filename]"
- "Articles curated: [count] organized by [themes]"
- "Videos curated: [count] from [channels]"
- "Key gaps identified: [list]"

**STOP.** Present meta-analysis findings and get user approval before proceeding to Phase 7.
</phase_meta_analysis>

---

<phase_email_series>
## Phase 7: Course Email Series

**PREREQUISITE:** Phase 6 (Meta-Analysis) must be complete. The email series uses the curated resource lists from the meta-analysis.

This phase creates the course email series that threads standalone lessons into a single learning arc.

### 7a: Identify the Thematic Spine

Before writing emails, identify 1-2 ideas that run through the entire course. These will be referenced in every email.

Look for concepts that:
- Appear in source materials repeatedly
- Inform multiple lessons
- Represent the course's core insight or reframe

**GATE:** Before proceeding, write:
- "Thematic spine: [1-2 concepts that thread through the course]"

### 7b: Create the Email Series

See [references/EMAIL-SERIES-GUIDE.md](references/EMAIL-SERIES-GUIDE.md) for detailed templates, tone guidance, and structure for all email types (welcome, post-session, final session, one-month check-in).

**Key requirements:** Direct/warm/substantive tone (no marketing copy, no exclamation points). Post-session resources point to NEXT session's themes. Maximum 2 articles + 1 video per email, all under 15 minutes, from credible sources.

### 7c: Output

Save to: `Curriculum/Courses/CRS###-slug/course-email-series.md`

**GATE:** Before finalizing, write:
- "Email series complete: [count] emails"
- "Thematic spine threaded: [yes/no]"
- "Resources curated from meta-analysis: [yes/no]"

**STOP.** Present email series draft and get user approval.
</phase_email_series>

---

## Checkpoints

| After | User Reviews |
|-------|--------------|
| Phase 1 | Learning themes extracted from sources |
| Phase 2 | Lesson reuse recommendations |
| Phase 3 | Course structure and sequencing |
| Each lesson prompt | Individual curriculum prompts |
| Phase 5 | Complete course package |
| Phase 6 | Meta-analysis findings and supplementary resources |
| Phase 7 | Complete email series draft |

**Do not proceed without explicit approval at each checkpoint.**

---

<failed_attempts>
What DOESN'T work:

- **Creating lesson content instead of curriculum prompts:** This skill outputs design documents, not facilitator guides or activity instructions. Those are created by `building-leaderspath-curriculum`.
- **Lessons that reference each other:** "Builds on Lesson 2" breaks atomicity. Lessons must be self-contained. Express dependencies as prerequisites in the lesson overview, not cross-references.
- **Skipping the lesson reuse search:** Even when no library exists, document that you searched. Otherwise future courses lose reuse opportunities.
- **Generating learning themes without sources:** All themes must trace back to provided materials. No invented pedagogy or assumed learning objectives.
- **Specifying implementation details:** System prompts, activity instructions, folder structures—these belong in `building-leaderspath-curriculum`, not curriculum prompts.
</failed_attempts>

---

## Resuming a Previous Session

If `course-tracker.md` exists:
1. Read it
2. Check current phase and incomplete items
3. Review session log
4. Continue from next incomplete step
5. Update session log when resuming

---

## Examples

### Example: Course Design from Interview Transcript

**Input:** Interview transcript about AI ethics training for nonprofit leaders

**Phase 1 → 6 learning themes** (LLM fundamentals, sycophancy, context libraries, skills, reflection, ethical frameworks)

**Phase 2 →** No existing lessons found; create 6 new

**Phase 3 →** 6-week sequence: AI Foundations → Behavioral Training → Context Libraries → Skills → Reflection → Ethical Framework

**Phase 4 →** Atomic curriculum prompts per lesson, each with lesson-level objectives, source references, required experiences, and Q&A bot decisions

See [references/CURRICULUM-PROMPT-GUIDE.md](references/CURRICULUM-PROMPT-GUIDE.md) for a complete curriculum prompt example.

---

## Relationship to Other Skills

- **Outputs to:** `building-leaderspath-curriculum` (lesson curriculum prompts → full lesson content)
- **Invokes:** `researching-youtube-channels` (Phase 6 video curation — do NOT use WebFetch for YouTube)
- **May reference:** `building-context-libraries` (demo contexts), `synthesizing-interviews` (raw transcripts)
- **Does NOT:** Create system prompts, activity instructions, facilitator guides, context libraries, or Agent Skills
