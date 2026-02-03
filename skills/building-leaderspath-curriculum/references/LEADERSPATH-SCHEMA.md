# LeadersPath Data Schema

This document defines the data model and field requirements for LeadersPath content, aligned with the WordPress plugin schema.

## Terminology

**Important:** In the WordPress plugin, the post type is `leaderspath_lesson` for historical reasons, but the UI displays "Activity" throughout. When designing curriculum, use "Activity" terminology.

| Curriculum Term | WordPress Post Type | UI Label |
|-----------------|---------------------|----------|
| Course | `leaderspath_course` | Course |
| Activity | `leaderspath_lesson` | Activity |
| Context File | `leaderspath_context` | Context File |
| Skill | `leaderspath_skill` | Skill |

---

## Entity Overview

```
Course (teaching unit)
├── Learning Objectives (course-level)
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
| `course_objectives` | Repeater | Yes | Learning objectives (what learners achieve) |
| `course_facilitator_guide` | WYSIWYG | Yes | Complete facilitator guide content |
| `course_learner_overview` | WYSIWYG | Yes | Learner-facing overview |
| `course_lessons` | Relationship | Yes | Ordered sequence of Activities |

### Metadata

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `course_difficulty` | Select | Yes | beginner/intermediate/advanced | Target skill level |
| `course_total_duration` | Text | Yes | — | Total time (e.g., "90 minutes") |
| `course_access_roles` | Checkbox | No | WordPress roles | Who can access |

### Course Q&A Chatbot (Optional)

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `course_chatbot_enabled` | Boolean | Yes | false | Enable Q&A bot |
| `course_chatbot_model` | Select | No | sonnet | Claude model |
| `course_chatbot_system_prompt` | Textarea | No | — | Custom Q&A prompt |
| `course_chatbot_context_files` | Relationship | No | — | Reference materials |
| `course_chatbot_max_tokens` | Number | No | 4096 | Response length limit |
| `course_chatbot_temperature` | Number | No | 0.7 | Response randomness |

**Key distinction:**
- **Activity Sandbox** = Demonstrates specific AI behavior (might be sycophantic, limited, roleplay)
- **Course Q&A Bot** = Always helpful, accurate, grounded in course content

---

## Activity Fields (WordPress: `leaderspath_lesson`)

### Core Content

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | Text | Yes | Activity title |
| `post_content` | Text | Yes | Activity instructions ("Try this, notice that") |

**Note:** `lesson_objectives` has been **removed**. Learning objectives now live at Course level.

### Metadata

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `lesson_duration` | Number | Yes | 1-480 minutes | Estimated completion time |
| `lesson_prerequisites` | Relationship | No | Other Activities | Required prior Activities |

### Activity Sandbox Configuration

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `chatbot_enabled` | Boolean | Yes | true | — | Enable AI sandbox |
| `chatbot_model` | Select | Yes | sonnet | sonnet/haiku/opus-4.5 | Model selection |
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
| Course description (from course-metadata.md) | `post_content` |
| Learning objectives | `course_objectives` (repeater) |
| facilitator-guide.md content | `course_facilitator_guide` |
| learner-overview.md content | `course_learner_overview` |
| Activities | `course_lessons` (relationship) |
| Difficulty level | `course_difficulty` |
| Duration text | `course_total_duration` |
| Q&A enabled | `course_chatbot_enabled` |
| Q&A settings | `course_chatbot_*` fields |

### Activity Post (`leaderspath_lesson`, UI shows "Activity")

| Curriculum Output | Plugin Field |
|-------------------|--------------|
| Activity name | `post_title` |
| instructions.md content | `post_content` |
| Duration in minutes | `lesson_duration` |
| Model | `chatbot_model` |
| system-prompt.md content | `chatbot_system_prompt` |
| Context file references | `chatbot_context_files` |
| Max tokens | `chatbot_max_tokens` |
| Temperature | `chatbot_temperature` |

### Context File Post (`leaderspath_context`)

| Curriculum Output | Plugin Field |
|-------------------|--------------|
| Context file name | `post_title` |
| Full content | `post_content` |
| File type | `context_file_type` |

---

## Output File Formats

When creating curriculum content, output in these formats:

### Folder Structure

```
_leaderspath/[course-name]/
├── course-tracker.md
├── course-metadata.md
├── learning-objectives.md
├── facilitator-guide.md
├── learner-overview.md
├── qa-chatbot-config.md          # Optional
└── activities/
    ├── 01-[slug]/
    │   ├── configuration/
    │   │   ├── system-prompt.md
    │   │   ├── api-settings.md
    │   │   └── context-files.md
    │   └── instructions.md
    ├── 02-[slug]/
    │   └── [same structure]
    └── shared-context/
        └── [context-files].md
```

### Course Metadata (`course-metadata.md`)

```markdown
# Course: [Title]

## Overview
[Brief description of what learners will experience]

## Difficulty
[beginner / intermediate / advanced]

## Total Duration
[e.g., "90 minutes" or "2 hours"]

## Prerequisites
[List of prior courses or knowledge]

## Activities Included
1. [Activity 1 name]
2. [Activity 2 name]
...
```

### Learning Objectives (`learning-objectives.md`)

```markdown
# Learning Objectives: [Course Name]

After completing this course, learners will be able to:

1. [Objective 1 - action verb + measurable outcome]
2. [Objective 2]
3. [Objective 3]
...
```

### Facilitator Guide (`facilitator-guide.md`)

See [CONTENT-GUIDES.md](CONTENT-GUIDES.md) for the complete structure.

### Learner Overview (`learner-overview.md`)

```markdown
# [Course Name]

## What You'll Experience
[High-level description of the course journey]

## What to Expect
- [Number] hands-on activities with AI sandboxes
- Discussion and reflection with your cohort
- [Duration] of facilitated learning

## Before You Begin
[Any preparation, mindset setting, or context]
```

### Q&A Chatbot Config (`qa-chatbot-config.md`)

```markdown
# Course Q&A Chatbot Configuration

## Enable Q&A Chatbot
Yes / No

## Purpose
[Why this course has a Q&A bot]

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

## Course-Level Context
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

### Context File (`[name]-context.md`)

```markdown
# [Title]

[Full markdown content following context library patterns]
```
