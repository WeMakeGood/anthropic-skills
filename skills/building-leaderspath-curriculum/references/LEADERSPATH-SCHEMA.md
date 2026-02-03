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

### Folder Structure

```
_leaderspath/[course-name]/
├── course-tracker.md
├── course-metadata.md
└── EN/
    ├── Course Materials/
    │   └── [shared resources]
    ├── context/
    │   └── [shared-context-files].md
    └── lessons/
        └── ##-[slug]/
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

## Languages
- EN (primary)

## Lessons
1. [Lesson 1 Title]
2. [Lesson 2 Title]
...
```

### Lesson Plan (`Lesson-Plan.md`)

See [LESSON-PLAN-TEMPLATE.md](LESSON-PLAN-TEMPLATE.md) for the complete template.

The Lesson Plan replaces the previous `lesson-metadata.md` and includes:
- Lesson Information (number, title, course, version, author)
- Learning Objectives
- Duration with breakdown
- Directions (step-by-step learner instructions)
- Model Specifications (model choice, capabilities, rationale)
- Chatbot Configuration overview
- Context Files overview
- Skills overview
- Resources overview
- Assessment overview
- Notes for Facilitators
- Related Content
- Technical Requirements

### API Settings (`Chatbot Configuration/api-settings.md`)

```markdown
# API Settings

## Model Configuration
- **Model:** [sonnet / haiku / opus-4.5]
- **Model String:** [claude-sonnet-4-5-20250929 / claude-haiku-4-5-20251001 / claude-opus-4-5-20251101]
- **Max Tokens:** [number, 256-16384]
- **Temperature:** [0-1]
- **Allow Model Switch:** [yes/no]

## Context Files
- [context/filename.md] — [brief description]
- [Context Files/filename.md] — [brief description]

## Skills
- [skill-name] — [brief description]
```

### Model Selection (`Chatbot Configuration/model-selection.md`)

```markdown
# Model Selection Rationale

## Why [Model Name]

[Explanation of why this specific model was chosen for this lesson]

## Capabilities Demonstrated
- [Capability 1]
- [Capability 2]
- [Capability 3]

## Trade-offs Considered
- [Trade-off 1: e.g., "Sonnet provides faster responses than Opus while maintaining quality for this task"]
- [Trade-off 2]

## Alternative Considerations
[If applicable, why other models were not chosen]
```

### System Prompt (`Chatbot Configuration/system-prompt.md`)

```markdown
[The complete system prompt content, ready to paste into chatbot_system_prompt field]
```

### Lesson Text (`lesson-text.md`)

```markdown
[The complete lesson content, ready to paste into post_content field]
```

### Self-Assessment (`Assessment/self-assessment.md`)

```markdown
# Self-Assessment: [Lesson Title]

## Comprehension Checks

1. [Question testing understanding of concept 1]
2. [Question testing understanding of concept 2]
3. [Question testing practical application]

## Reflection Prompts

- How could you apply this in your organization?
- What challenges might you encounter?
- What additional support or resources would you need?

## Feedback

We value your input! After completing this lesson:
- Share what worked well
- Identify what could be improved
- Ask questions or raise concerns

**Feedback Options:**
- LeadersPath community discussion forum
- Cohort session discussions
```

### Facilitator Guide (`Facilitator Notes/facilitator-guide.md`)

```markdown
# Facilitator Guide: [Lesson Title]

## Common Learner Questions

**Q: [Anticipated question]**
A: [Suggested response]

**Q: [Anticipated question]**
A: [Suggested response]

## Potential Challenges

### [Challenge 1]
**Issue:** [Description of challenge]
**Resolution:** [How to address it]

### [Challenge 2]
**Issue:** [Description of challenge]
**Resolution:** [How to address it]

## Timing Considerations

- **Introduction:** [Notes about pacing]
- **Hands-on Practice:** [Areas where learners may need more time]
- **Wrap-up:** [Timing notes]

## Discussion Prompts

Use these to spark discussion in cohort settings:
- [Question 1]
- [Question 2]
- [Question 3]

## Tips for Live Facilitation

[Additional notes for facilitators leading this lesson in a cohort setting]
```

### Context File (`[name]-context.md`)

```markdown
# [Title]

[Full markdown content following context library patterns]
```
