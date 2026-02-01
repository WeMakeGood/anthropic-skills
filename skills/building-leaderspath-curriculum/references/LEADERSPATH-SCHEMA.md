# LeadersPath Data Schema

This document defines the data model and field requirements for LeadersPath content.

## Entity Overview

```
Course
├── Lessons (ordered sequence)
│   ├── Context Files (relationship, max 20)
│   └── Skills (relationship, max 20)
└── Topics (taxonomy)
```

---

## Course Fields

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `title` | Text | Yes | — | Course title |
| `description` | Text | Yes | — | What learners will achieve |
| `course_lessons` | Relationship | Yes | Max 100 | Ordered lesson sequence |
| `course_difficulty` | Select | Yes | Beginner / Intermediate / Advanced | Target skill level |
| `course_total_duration` | Number | Auto | Minutes | Sum of lesson durations |
| `course_access_roles` | Checkbox | No | WordPress roles | Who can access |

---

## Lesson Fields

### Core Content

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `title` | Text | Yes | — | Lesson title |
| `post_content` | HTML/Text | Yes | — | User-facing lesson instructions (not sent to AI) |

### Metadata

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `lesson_duration` | Number | Yes | 1-480 minutes | Estimated completion time |
| `lesson_objectives` | Repeater | Yes | Max 10 items | Learning outcomes |
| `lesson_prerequisites` | Relationship | No | Other lessons | Required prior lessons |
| `lesson_references` | Repeater | No | — | External resources |

**Lesson References structure:**
- `title` (text) — Resource name
- `url` (URL) — Link to resource
- `description` (text) — Why it's relevant

### Chatbot Configuration

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `chatbot_enabled` | Boolean | Yes | true | — | Enable AI for this lesson |
| `chatbot_model` | Select | Yes | sonnet | sonnet / haiku / opus-4.5 | Default model |
| `chatbot_allow_model_switch` | Boolean | No | false | — | Let learners change models |
| `chatbot_system_prompt` | Textarea | Yes | — | — | **The sandbox configuration** |
| `chatbot_context_files` | Relationship | No | — | Max 20 | Context files to load |
| `chatbot_skills` | Relationship | No | — | Max 20 | Skills to enable |
| `chatbot_max_tokens` | Number | No | 4096 | 256-16384 | Response length limit |
| `chatbot_temperature` | Number | No | 0.7 | 0-1 | Response randomness |

---

## Context File Fields

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `title` | Text | Yes | — | File identifier |
| `post_content` | Markdown | Yes | — | Full context content |
| `context_description` | Textarea | No | — | Purpose and usage notes |
| `context_file_type` | Select | No | See below | Content category |
| `context_version` | Text | No | Semver format | Version tracking |

**Context file types:**
- System Prompt
- Knowledge Base
- Instructions
- Examples
- Other

**Context file categories (taxonomy):**
- Organization Profile
- Brand Guidelines
- Process Documentation
- Technical Specifications
- Example Content

---

## Skill Fields

Skills are uploaded as ZIP packages containing a `SKILL.md` file.

| Field | Type | Source | Description |
|-------|------|--------|-------------|
| `skill_name` | Text | Extracted from SKILL.md | Skill identifier |
| `skill_description` | Textarea | Extracted from SKILL.md | What the skill does |
| `skill_compatibility` | Text | Extracted from SKILL.md | Prerequisites |
| `skill_version` | Text | Manual | Version number |
| `skill_package` | File | Upload | ZIP file |

---

## System Prompt Assembly

When a chat session starts, the system prompt is built from:

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

**Important:** The lesson's `post_content` is NOT included in the system prompt. It appears only on the lesson page for the learner to read.

---

## Taxonomy: Topics

Both Courses and Lessons can have Topics assigned.

- Hierarchical (parent/child relationships allowed)
- Used for filtering and navigation
- Examples: "Prompt Engineering", "Context Libraries", "Ethical AI", "LLM Fundamentals"

---

## Output File Formats

When creating curriculum content, output in these formats:

### Course Metadata (`course-metadata.md`)

```markdown
# Course: [Title]

## Description
[What learners will achieve]

## Difficulty
[Beginner / Intermediate / Advanced]

## Duration
[Total minutes] (sum of all lesson durations)

## Topics
- [Topic 1]
- [Topic 2]

## Lessons
1. [Lesson 1 Title]
2. [Lesson 2 Title]
...
```

### Lesson Metadata (`lesson-metadata.md`)

```markdown
# Lesson: [Title]

## AI State
[Brief description of how the AI is configured for this lesson and what behavior it demonstrates]

## Duration
[X] minutes

## Objectives
1. [Objective 1]
2. [Objective 2]

## Prerequisites
- [Prerequisite lesson, if any]

## References
- [Title](URL) — [Description]

## Chatbot Configuration
- **Model:** [sonnet/haiku/opus-4.5]
- **Allow Model Switch:** [yes/no]
- **Max Tokens:** [number]
- **Temperature:** [0-1]
- **Context Files:** [list with paths, e.g., context/filename.md]
- **Skills:** [list, if any]
```

### System Prompt (`system-prompt.md`)

```markdown
[The complete system prompt content, ready to paste into chatbot_system_prompt field]
```

### Lesson Text (`lesson-text.md`)

```markdown
[The complete lesson content, ready to paste into post_content field]
```

### Context File (`[name]-context.md`)

```markdown
# [Title]

[Full markdown content following context library patterns]
```
