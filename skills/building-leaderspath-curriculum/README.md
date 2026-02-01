# Building LeadersPath Curriculum

An Agent Skill for creating experiential AI learning content for the LeadersPath platform.

## What This Skill Does

Transforms course designs and lesson plans into complete LeadersPath curriculum packages:

- **System prompts** that configure AI sandbox behavior
- **Context files** that provide background knowledge (reusable across lessons)
- **Lesson text** that guides learner experimentation
- **Metadata** for course and lesson configuration

## Quick Start

1. Invoke the skill with your curriculum materials
2. Provide course name and source documents
3. Review and approve course structure
4. Skill produces all lesson files

### Example Prompt

```
Build a LeadersPath course called "The Sycophancy Problem"

Source: Two lessons teaching learners to recognize sycophantic vs. objective AI.

Lesson 1: "The Yes Machine" - AI configured to always agree
Lesson 2: "The Professional Critic" - AI configured with anti-sycophancy guardrails

These are a comparison pair - use the same prompts in both lessons.

Output to: ./my-course/
```

## What LeadersPath Is

LeadersPath is an experiential AI learning platform where each lesson is a configured AI sandbox. Learners interact with AI sessions set up to demonstrate specific behaviors—sometimes intentionally limited, sometimes fully equipped—to experience firsthand how configuration affects AI outputs.

**Key concept:** One lesson = one AI state. Learners can't toggle between configurations within a lesson. Comparisons happen across lessons.

## Writing Better Prompts

The quality of curriculum output depends on the clarity of your input. See the "Tips for Curriculum Designers" section in [SKILL.md](SKILL.md) for detailed guidance.

### Quick Tips

| Do This | Not This |
|---------|----------|
| "AI configured to always agree, avoid pushback" | "A sycophantic AI" |
| "Lessons 1 & 2 are a comparison pair" | "Compare the two approaches" |
| "Roleplay: AI plays a client with red flags" | "A simulation lesson" |
| "Use the same prompts across both lessons" | "Let learners compare" |
| "Organizational context doc—extract principles" | "Here's a document" |

### Source Document Types

When providing source material, indicate what type:

- **Curriculum document** — Learning objectives, lesson plans (used directly)
- **Organizational context** — Internal docs, frameworks (adapted/transformed)
- **Reference material** — Background reading (informs but not used directly)

## Output Structure

```
_leaderspath/[course-name]/
├── course-tracker.md          # Progress tracking, decisions log
├── course-metadata.md         # Course-level metadata
├── context/                   # Shared context files
│   └── [topic]-context.md
└── lessons/
    ├── 01-[slug]/
    │   ├── lesson-metadata.md
    │   ├── system-prompt.md
    │   └── lesson-text.md
    └── 02-[slug]/
        └── ...
```

## Lesson Types

| Type | System Prompt | Context File | Example |
|------|---------------|--------------|---------|
| Bare/Limited | Minimal instructions | None | "AI without context" |
| Role-Constrained | Role definition | None | "Project planning assistant" |
| Context-Rich | Instructions + context reference | Yes | "AI with organizational knowledge" |
| Deliberately Flawed | Instructions creating problematic behavior | None | "Sycophantic AI" |
| Roleplay/Persona | Character definition | Usually none | "AI plays a prospective client" |
| Capability-Transfer | Teaching instructions + context | Yes | "AI that explains its reasoning" |

## Context File Decisions

The skill determines whether lessons need context files based on:

| Behavior Source | Context File? |
|-----------------|---------------|
| **Instructions** (be agreeable, play a role) | No - system prompt only |
| **Knowledge** (organizational context, domain expertise) | Yes |
| **Guardrails** (anti-sycophancy rules, epistemic standards) | Yes |

Multiple lessons can share context files. The skill tracks reuse opportunities.

## Files in This Skill

| File | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Main workflow and instructions |
| [references/LEADERSPATH-SCHEMA.md](references/LEADERSPATH-SCHEMA.md) | Data model, field requirements |
| [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) | Content creation patterns and examples |

## Platform Notes

LeadersPath provides learners with transparency—they can view the system prompt, context files, and skill configurations for each lesson. This supports the pedagogical goal of teaching how AI configuration works.

## License

Part of the [Anthropic Skills Library](https://github.com/anthropics/anthropic-skills). See repository license.
