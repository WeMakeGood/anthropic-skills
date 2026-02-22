# Designing LeadersPath Courses

An Agent Skill for designing course curricula from source materials, with optional post-build analysis and email series creation.

## What This Skill Does

Transforms source materials (interview transcripts, design docs, organizational materials) into:

**Phases 1-5 (Course Design):**
- **Course Curriculum** — Structure, sequencing, target audience, duration
- **Lesson Curriculum Prompts** — Design documents for building-leaderspath-curriculum
- **Lesson Reuse Report** — Which existing lessons can be reused vs. created new

**Phases 6-7 (Post-Build, Optional):**
- **Meta-Analysis Report** — Review of built lessons against design intent, with curated supplementary resources
- **Course Email Series** — Pre-course, post-session, and follow-up emails that thread lessons into a learning arc

## Quick Start

1. Invoke the skill with your source materials
2. Provide course name, target audience, and duration
3. Review learning themes extracted from sources
4. Approve lesson reuse recommendations
5. Review lesson curriculum prompts as they're created

### Example Prompt

```
Design a LeadersPath course for nonprofit leaders

Source materials: interview-transcript.md, learning-goals.md
Course name: AI Foundations for Nonprofits
Target audience: Executive Directors and senior staff
Duration: 6 weeks (one session per week)
Lesson library: ./existing-lessons/
```

## Relationship to Other Skills

```
Source Materials → [THIS SKILL: Phases 1-5] → Lesson Curriculum Prompts
                                                        ↓
                              [building-leaderspath-curriculum]
                                                        ↓
                              Facilitator Guides, Activities, Learner Materials
                                                        ↓
                          [THIS SKILL: Phase 6] → Meta-Analysis Report
                                                        ↓
                          [THIS SKILL: Phase 7] → Course Email Series
```

Phases 1-5 sit upstream of `building-leaderspath-curriculum`, producing design documents (curriculum prompts) that tell the building skill what to create.

Phases 6-7 run after lessons are built, analyzing the results and creating course-level communication assets.

## Output Structure

```
Curriculum/Courses/CRS###-slug/
├── README.md                         # Course project overview
├── course-tracker.md                 # Progress tracking, session log
├── course-curriculum.md              # Course structure and lesson sequence
├── lesson-reuse-report.md            # Analysis of existing vs. new lessons
├── lesson-id-log.md                  # ID assignments made during design
├── Source Materials/                  # Inputs gathered before designing
│   └── [transcripts, syntheses, etc.]
├── Lesson Prompts/                   # One per lesson
│   ├── LSN###-slug-curriculum.md
│   └── ...
│
│  (After lessons are built by building-leaderspath-curriculum:)
│
├── course-meta-analysis-[date].md    # Phase 6: Post-build analysis
└── course-email-series.md            # Phase 7: Course communications
```

All entities use sequential IDs assigned from YAML registries in `Curriculum/Registry/`: courses are `CRS###-slug` (e.g., `CRS001-ethical-ai-nonprofit-leaders`), lessons are `LSN###-slug` (e.g., `LSN001-skills-framework`), activities are `ACT###-slug`. See [building-leaderspath-curriculum/references/NAMING-SYSTEM.md](../building-leaderspath-curriculum/references/NAMING-SYSTEM.md) for complete naming conventions.

## Files in This Skill

| File | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Main workflow and instructions |
| [references/CURRICULUM-PROMPT-GUIDE.md](references/CURRICULUM-PROMPT-GUIDE.md) | How to write effective curriculum prompts |
| [references/LESSON-SEARCH-GUIDE.md](references/LESSON-SEARCH-GUIDE.md) | How to search for and evaluate existing lessons |
| [references/META-ANALYSIS-GUIDE.md](references/META-ANALYSIS-GUIDE.md) | How to conduct post-build meta-analysis (Phase 6) |
| [references/EMAIL-SERIES-GUIDE.md](references/EMAIL-SERIES-GUIDE.md) | How to create the course email series (Phase 7) |

## License

Part of the [Anthropic Skills Library](https://github.com/anthropics/anthropic-skills). See repository license.
