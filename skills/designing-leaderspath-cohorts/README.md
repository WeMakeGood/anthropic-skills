# Designing LeadersPath Cohorts

An Agent Skill for designing cohort curricula from source materials, with optional post-build analysis and email series creation.

## What This Skill Does

Transforms source materials (interview transcripts, design docs, organizational materials) into:

**Phases 1-5 (Cohort Design):**
- **Cohort Curriculum** — Structure, sequencing, target audience, duration
- **Course Curriculum Prompts** — Design documents for building-leaderspath-curriculum
- **Course Reuse Report** — Which existing courses can be reused vs. created new

**Phases 6-7 (Post-Build, Optional):**
- **Meta-Analysis Report** — Review of built courses against design intent, with curated supplementary resources
- **Cohort Email Series** — Pre-cohort, post-session, and follow-up emails that thread courses into a learning arc

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
Source Materials → [THIS SKILL: Phases 1-5] → Course Curriculum Prompts
                                                        ↓
                              [building-leaderspath-curriculum]
                                                        ↓
                              Facilitator Guides, Activities, Learner Materials
                                                        ↓
                          [THIS SKILL: Phase 6] → Meta-Analysis Report
                                                        ↓
                          [THIS SKILL: Phase 7] → Cohort Email Series
```

Phases 1-5 sit upstream of `building-leaderspath-curriculum`, producing design documents (curriculum prompts) that tell the building skill what to create.

Phases 6-7 run after courses are built, analyzing the results and creating cohort-level communication assets.

## Output Structure

```
[working-folder]/
├── cohort-tracker.md          # Progress tracking, session log
├── cohort-curriculum.md       # Cohort structure and course sequence
├── course-reuse-report.md     # Analysis of existing vs. new courses
├── course-id-log.md           # New/updated Course ID entries
├── Courses/
│   ├── FUND-101-ai-basics-curriculum.md
│   ├── PRMPT-101-intro-prompting-curriculum.md
│   └── ...
│
│  (After courses are built by building-leaderspath-curriculum:)
│
├── cohort-meta-analysis-[date].md    # Phase 6: Post-build analysis
└── cohort-email-series.md            # Phase 7: Cohort communications
```

Course IDs use the format `TOPIC-LEVEL-slug` (e.g., `FUND-101-ai-basics`). See [building-leaderspath-curriculum/references/NAMING-SYSTEM.md](../building-leaderspath-curriculum/references/NAMING-SYSTEM.md) for complete naming conventions.

## Files in This Skill

| File | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Main workflow and instructions |
| [references/CURRICULUM-PROMPT-GUIDE.md](references/CURRICULUM-PROMPT-GUIDE.md) | How to write effective curriculum prompts |
| [references/COURSE-SEARCH-GUIDE.md](references/COURSE-SEARCH-GUIDE.md) | How to search for and evaluate existing courses |
| [references/META-ANALYSIS-GUIDE.md](references/META-ANALYSIS-GUIDE.md) | How to conduct post-build meta-analysis (Phase 6) |
| [references/EMAIL-SERIES-GUIDE.md](references/EMAIL-SERIES-GUIDE.md) | How to create the cohort email series (Phase 7) |

## License

Part of the [Anthropic Skills Library](https://github.com/anthropics/anthropic-skills). See repository license.
