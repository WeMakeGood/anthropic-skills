# LeadersPath Data Schema

This document defines the data model and field requirements for LeadersPath content, aligned with the WordPress plugin schema (v0.3.0).

## Terminology

| Curriculum Term | WordPress Post Type | REST Endpoint | Description |
|-----------------|---------------------|---------------|-------------|
| Course | `leaderspath_course` | `/courses` | Container grouping lessons into a program |
| Lesson | `leaderspath_lesson` | `/lessons` | Teaching unit with objectives and activities |
| Activity | `leaderspath_activity` | `/activities` | Individual hands-on learning exercise |
| Context File | `leaderspath_context` | `/context-files` | Reference material for AI chatbots |
| Skill | `leaderspath_skill` | `/skills` | Agent skill package (ZIP with SKILL.md) |

---

## Entity Overview

```
Course (program container)
└── Lessons (ordered sequence)
    ├── Learning Objectives (lesson-level)
    ├── Facilitator Guide
    ├── Learner Overview
    ├── Q&A Chatbot (optional)
    └── Activities (ordered sequence)
        ├── Activity Sandbox Configuration
        ├── Activity Instructions
        └── Context Files (relationship)
```

---

## Course Fields

### Core Content

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | Text | Yes | Course title |
| `post_content` | Text | Yes | Course description |
| `course_lessons` | Relationship | Yes | Ordered sequence of Lessons |

---

## Lesson Fields

### Core Content

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | Text | Yes | Lesson title |
| `post_content` | Text | Yes | Lesson description |
| `lesson_objectives` | Repeater | Yes | Learning objectives (what learners achieve) |
| `lesson_facilitator_guide` | WYSIWYG | Yes | Complete facilitator guide content |
| `lesson_learner_overview` | WYSIWYG | Yes | Learner-facing overview |
| `lesson_activities` | Relationship | Yes | Ordered sequence of Activities |

### Metadata

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `lesson_difficulty` | Select | Yes | beginner/intermediate/advanced | Target skill level |
| `lesson_total_duration` | Text | Yes | — | Total time (e.g., "90 minutes") |
| `lesson_access_roles` | Checkbox | No | WordPress roles | Who can access |

### Lesson Q&A Chatbot (Optional)

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `lesson_chatbot_enabled` | Boolean | Yes | false | Enable Q&A bot |
| `lesson_chatbot_model` | Select | No | sonnet | Claude model |
| `lesson_chatbot_system_prompt` | Textarea | No | — | Custom Q&A prompt |
| `lesson_chatbot_context_files` | Relationship | No | — | Reference materials |
| `lesson_chatbot_max_tokens` | Number | No | 4096 | Response length limit |
| `lesson_chatbot_temperature` | Number | No | 0.7 | Response randomness |

**Key distinction:**
- **Activity Sandbox** = Demonstrates specific AI behavior (might be sycophantic, limited, roleplay)
- **Lesson Q&A Bot** = Always helpful, accurate, grounded in lesson content

---

## Activity Fields (WordPress: `leaderspath_activity`)

### Core Content

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | Text | Yes | Activity title |
| `post_content` | Text | Yes | Activity instructions ("Try this, notice that") |

### Metadata

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `activity_duration` | Number | Yes | 1-480 minutes | Estimated completion time |
| `activity_prerequisites` | Relationship | No | Other Activities | Required prior Activities |
| `activity_references` | Repeater | No | — | Supporting reference links |

### Activity Sandbox Configuration

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `chatbot_enabled` | Boolean | Yes | true | — | Enable AI sandbox |
| `chatbot_model` | Select | Yes | sonnet | sonnet/haiku/opus-4.5 | Model selection |
| `chatbot_allow_model_switch` | Boolean | No | false | — | Allow learner to switch models |
| `chatbot_system_prompt` | Textarea | Yes | — | — | **The sandbox configuration** |
| `chatbot_context_files` | Relationship | No | — | Max 20 | Context files to load |
| `chatbot_skills` | Relationship | No | — | Max 20 | Skills to enable |
| `chatbot_max_tokens` | Number | No | 4096 | 256-16384 | Response length limit |
| `chatbot_temperature` | Number | No | 0.7 | 0-1 | Response randomness |

---

## Context File Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | Text | Yes | File identifier |
| `post_content` | Markdown | Yes | Full context content |
| `context_description` | Textarea | No | Purpose and usage notes |
| `context_file_type` | Select | No | Content category |
| `context_version` | Text | No | Version tracking (semver) |

**Context file types:**
- Instructions
- Knowledge Base
- Guidelines
- Reference
- Other

---

## Skill Fields

Skills are uploaded as ZIP packages containing a `SKILL.md` file.

| Field | Type | Source | Description |
|-------|------|--------|-------------|
| `skill_name` | Text | Extracted | Skill identifier |
| `skill_description` | Textarea | Extracted | What the skill does |
| `skill_version` | Text | Manual | Version number |
| `skill_package` | File | Upload | ZIP file |

---

## System Prompt Assembly

When an Activity sandbox chat session starts, the system prompt is built from:

1. **`chatbot_system_prompt`** — The custom sandbox configuration
2. **Context files** — Full content of all related context files, each with a header
3. **Skill descriptions** — Title and description of each enabled skill

**Assembly format:**
```
[chatbot_system_prompt content]

--- Reference Materials ---

### [Context File 1 Title]
[Context File 1 content]

### [Context File 2 Title]
[Context File 2 content]

--- Available Skills ---

### [Skill 1 Name]
[Skill 1 description]
```

**Important:** Activity instructions (`post_content`) appear on the Activity page for the learner to read. They are NOT included in the AI system prompt.

---

## WordPress Mapping Reference

When curriculum is imported to WordPress:

### Course Post (`leaderspath_course`)

| Curriculum Output | Plugin Field |
|-------------------|--------------|
| Course name | `post_title` |
| Course description | `post_content` |
| Lessons | `course_lessons` (relationship) |

### Lesson Post (`leaderspath_lesson`)

| Curriculum Output | Plugin Field |
|-------------------|--------------|
| Lesson name | `post_title` |
| Lesson description (from lesson-metadata.md) | `post_content` |
| Learning objectives | `lesson_objectives` (repeater) |
| facilitator-guide.md content | `lesson_facilitator_guide` |
| learner-overview.md content | `lesson_learner_overview` |
| Activities | `lesson_activities` (relationship) |
| Difficulty level | `lesson_difficulty` |
| Duration text | `lesson_total_duration` |
| Q&A enabled | `lesson_chatbot_enabled` |
| Q&A settings | `lesson_chatbot_*` fields |

### Activity Post (`leaderspath_activity`)

| Curriculum Output | Plugin Field |
|-------------------|--------------|
| Activity name | `post_title` |
| instructions.md content | `post_content` |
| Duration in minutes | `activity_duration` |
| Prerequisites | `activity_prerequisites` |
| References | `activity_references` |
| Model | `chatbot_model` |
| Allow model switch | `chatbot_allow_model_switch` |
| system-prompt.md content | `chatbot_system_prompt` |
| Context file references | `chatbot_context_files` |
| Skill references | `chatbot_skills` |
| Max tokens | `chatbot_max_tokens` |
| Temperature | `chatbot_temperature` |

### Context File Post (`leaderspath_context`)

| Curriculum Output | Plugin Field |
|-------------------|--------------|
| Context file name | `post_title` |
| Full content | `post_content` |
| File type | `context_file_type` |

---

## Naming System

See [NAMING-SYSTEM.md](NAMING-SYSTEM.md) for complete naming conventions.

**Quick reference:**
- **Course ID:** `CRS###-slug` (e.g., `CRS001-ethical-ai-nonprofit-leaders`)
- **Lesson ID:** `LSN###-slug` (e.g., `LSN001-skills-framework`)
- **Activity ID:** `ACT###-slug` (e.g., `ACT001-meeting-report-vanilla`)
- **Context File:** `CTX###-slug.md` (e.g., `CTX004-agent-behavioral-standards.md`)

---

## Output File Formats

When creating curriculum content, output in these formats:

### Folder Structure

```
Curriculum/Lessons/LSN###-slug/
├── lesson-tracker.md
├── lesson-metadata.md
├── learning-objectives.md
├── facilitator-guide.md
├── learner-overview.md
├── qa-chatbot-config.md              # Optional
└── activities/
    ├── ACT###-first-activity/
    │   ├── configuration/
    │   │   ├── system-prompt.md
    │   │   ├── api-settings.md
    │   │   └── context-files.md
    │   └── instructions.md
    ├── ACT###-second-activity/
    │   └── [same structure]
    └── shared-context/
        └── CTX###-slug.md
```

Registry files updated separately in `Curriculum/Registry/` (lesson-registry.yaml, context-registry.yaml).

### Lesson Metadata (`lesson-metadata.md`)

```markdown
# Lesson: [Title]

**Lesson ID:** [LSN###-slug]

## Overview
[Brief description of what learners will experience]

## Difficulty
[beginner / intermediate / advanced]

## Total Duration
[e.g., "90 minutes" or "2 hours"]

## Prerequisites
[List of prior lessons or knowledge]

## Activities Included
1. [ACT###-slug] — [Activity name]
2. [ACT###-slug] — [Activity name]
...
```

### Learning Objectives (`learning-objectives.md`)

```markdown
# Learning Objectives: [Lesson Name]

After completing this lesson, learners will be able to:

1. [Objective 1 - action verb + measurable outcome]
2. [Objective 2]
3. [Objective 3]
...
```

### Facilitator Guide (`facilitator-guide.md`)

See [CONTENT-GUIDES.md](CONTENT-GUIDES.md) for the complete structure.

### Learner Overview (`learner-overview.md`)

```markdown
# [Lesson Name]

## What You'll Experience
[High-level description of the lesson journey]

## What to Expect
- [Number] hands-on activities with AI sandboxes
- Discussion and reflection with your course peers
- [Duration] of facilitated learning

## Before You Begin
[Any preparation, mindset setting, or context]
```

### Q&A Chatbot Config (`qa-chatbot-config.md`)

```markdown
# Lesson Q&A Chatbot Configuration

## Enable Q&A Chatbot
Yes / No

## Purpose
[Why this lesson has a Q&A bot]

## System Prompt
[Complete system prompt for Q&A assistant]

## Context Files
- [List context files to load]

## Model Settings
- Model: [sonnet / haiku / opus-4.5]
- Max Tokens: [number]
- Temperature: [0-1]
```

### Activity Configuration (`configuration/`)

**system-prompt.md:**
```markdown
[The complete system prompt content, ready to paste into chatbot_system_prompt field]
```

**api-settings.md:**
```markdown
# API Settings

## Model Configuration
- Model: [sonnet / haiku / opus-4.5]
- Max Tokens: [number]
- Temperature: [0-1]
- Allow Model Switch: [yes / no]

## Context Files
- [path/filename.md] — [brief description]
(or "None")

## Skills
- [skill-name] — [brief description]
(or "None")
```

**context-files.md:**
```markdown
# Context Files for Activity: [Name]

## Lesson-Level Context
- [shared-context/filename.md] — [why needed]

## Activity-Specific Context
- None (or list files)
```

### Activity Instructions (`instructions.md`)

```markdown
# Activity: [Name]

## What You'll Experience
[One sentence describing the AI configuration]

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

### Context File (`CTX###-slug.md`)

```markdown
# [Title]

[Full markdown content following context library patterns]
```
