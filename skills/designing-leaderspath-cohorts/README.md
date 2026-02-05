# Designing LeadersPath Cohorts

An Agent Skill for designing cohort curricula from source materials.

## What This Skill Does

Transforms source materials (interview transcripts, design docs, organizational materials) into:

- **Cohort Curriculum** — Structure, sequencing, target audience, duration
- **Course Curriculum Prompts** — Design documents for building-leaderspath-curriculum
- **Course Reuse Report** — Which existing courses can be reused vs. created new

## Quick Start

1. Invoke the skill with your source materials
2. Provide cohort name, target audience, and duration
3. Review learning themes extracted from sources
4. Approve course reuse recommendations
5. Review course curriculum prompts as they're created

### Example Prompt

```
Design a LeadersPath cohort for nonprofit leaders

Source materials: interview-transcript.md, learning-goals.md
Cohort name: AI Foundations for Nonprofits
Target audience: Executive Directors and senior staff
Duration: 6 weeks (one session per week)
Course library: ./existing-courses/
```

## Relationship to Other Skills

```
Source Materials → [THIS SKILL] → Course Curriculum Prompts
                                          ↓
                      [building-leaderspath-curriculum]
                                          ↓
                      Facilitator Guides, Activities, Learner Materials
```

This skill sits upstream of `building-leaderspath-curriculum`. It produces design documents (curriculum prompts) that tell the building skill what to create.

## Output Structure

```
[working-folder]/
├── cohort-tracker.md          # Progress tracking, session log
├── cohort-curriculum.md       # Cohort structure and course sequence
├── course-reuse-report.md     # Analysis of existing vs. new courses
├── course-id-log.md           # New/updated Course ID entries
└── Courses/
    ├── FUND-101-ai-basics-curriculum.md
    ├── PRMPT-101-intro-prompting-curriculum.md
    └── ...
```

Course IDs use the format `TOPIC-LEVEL-slug` (e.g., `FUND-101-ai-basics`). See [building-leaderspath-curriculum/references/NAMING-SYSTEM.md](../building-leaderspath-curriculum/references/NAMING-SYSTEM.md) for complete naming conventions.

## Files in This Skill

| File | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Main workflow and instructions |
| [references/CURRICULUM-PROMPT-GUIDE.md](references/CURRICULUM-PROMPT-GUIDE.md) | How to write effective curriculum prompts |
| [references/COURSE-SEARCH-GUIDE.md](references/COURSE-SEARCH-GUIDE.md) | How to search for and evaluate existing courses |

## License

Part of the [Anthropic Skills Library](https://github.com/anthropics/anthropic-skills). See repository license.
