# Building LeadersPath Curriculum

An Agent Skill for creating facilitated AI learning content for the LeadersPath platform.

## What This Skill Does

Transforms lesson designs into complete LeadersPath curriculum packages:

- **Facilitator guides** — The primary deliverable; complete teaching scripts with timing
- **Activity configurations** — System prompts that configure AI sandbox behavior
- **Activity instructions** — "Try this, notice that" guidance for sandbox experimentation
- **Context files** — Background knowledge (reusable across activities)
- **Lesson metadata** — Learning objectives, duration, prerequisites

## Quick Start

1. Invoke the skill with your curriculum materials
2. Provide lesson name and source documents
3. Review and approve lesson-level content (facilitator guide, objectives)
4. Skill produces all activity files with checkpoints for approval

### Example Prompt

```
Build a LeadersPath lesson called "The Sycophancy Problem"

Source: Two activities teaching learners to recognize sycophantic vs. objective AI.

Activity 1: "The Yes Machine" - AI configured to always agree
Activity 2: "The Professional Critic" - AI configured with anti-sycophancy guardrails

These are a comparison pair - use the same prompts in both activities.

Output to: ./my-lesson/
```

## What LeadersPath Is

LeadersPath is a **facilitated course learning experience**, not a self-paced platform. The system has three components:

1. **A group of learners** — Peers learning together
2. **A human facilitator** — Who teaches concepts and leads discussion
3. **AI sandboxes as activities** — For hands-on experimentation

**The AI sandbox is NOT the lesson—it's an activity within a facilitated learning experience.**

**Key concept:** The facilitator teaches; the AI sandbox demonstrates. Comparisons happen across activities within a lesson.

## Writing Better Prompts

The quality of curriculum output depends on the clarity of your input. See [references/CURRICULUM-DESIGNER-TIPS.md](references/CURRICULUM-DESIGNER-TIPS.md) for detailed guidance.

### Quick Tips

| Do This | Not This |
|---------|----------|
| "AI configured to always agree, avoid pushback" | "A sycophantic AI" |
| "Activities 1 & 2 are a comparison pair" | "Compare the two approaches" |
| "Roleplay: AI plays a client with red flags" | "A simulation activity" |
| "Use the same prompts across both activities" | "Let learners compare" |
| "Organizational context doc—extract principles" | "Here's a document" |

### Source Document Types

When providing source material, indicate what type:

- **Curriculum document** — Learning objectives, lesson outlines (used directly)
- **Organizational context** — Internal docs, frameworks (adapted/transformed)
- **Reference material** — Background reading (informs but not used directly)

## Output Structure

```
Curriculum/Lessons/LSN###-slug/
├── lesson-tracker.md          # Progress tracking, decisions log
├── lesson-metadata.md         # Lesson-level metadata
├── learning-objectives.md     # Lesson-level learning objectives
├── facilitator-guide.md       # PRIMARY DELIVERABLE
├── learner-overview.md        # Context for learners
├── qa-chatbot-config.md       # Optional Q&A assistant
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

All entities use sequential IDs: lessons are `LSN###-slug` (e.g., `LSN001-skills-framework`), activities are `ACT###-slug` (e.g., `ACT001-meeting-report-contextualized`), globally unique across all lessons. IDs are assigned from YAML registries in `Curriculum/Registry/`. See [references/NAMING-SYSTEM.md](references/NAMING-SYSTEM.md) for complete naming conventions.

## Activity Types

| Type | System Prompt | Context File | Example |
|------|---------------|--------------|---------|
| Bare/Limited | Minimal instructions | None | "AI without context" |
| Role-Constrained | Role definition | None | "Project planning assistant" |
| Context-Rich | Instructions + context reference | Yes | "AI with organizational knowledge" |
| Deliberately Flawed | Instructions creating problematic behavior | None | "Sycophantic AI" |
| Roleplay/Persona | Character definition | Usually none | "AI plays a prospective client" |

## Context File Decisions

The skill determines whether activities need context files based on:

| Behavior Source | Context File? |
|-----------------|---------------|
| **Instructions** (be agreeable, play a role) | No - system prompt only |
| **Knowledge** (organizational context, domain expertise) | Yes |
| **Guardrails** (anti-sycophancy rules, epistemic standards) | Yes |

Multiple activities can share context files. The skill tracks reuse opportunities.

## Context File Installation

After creating curriculum, the skill can automatically install context files to your shared Contexts library:

- Copies files from `activities/shared-context/` to `Curriculum/Contexts/` (flat directory — no subfolders)
- Updates `Curriculum/Registry/context-registry.yaml` with new entries
- Updates `Curriculum/Registry/lesson-registry.yaml` with lesson and activity entries
- Skips files that already exist (no overwrites)

This step is environment-dependent—if the Contexts folder doesn't exist, it gracefully skips and notes manual installation is needed.

## Files in This Skill

| File | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Main workflow and instructions |
| [references/LEADERSPATH-SCHEMA.md](references/LEADERSPATH-SCHEMA.md) | Data model, field requirements |
| [references/CONTENT-GUIDES.md](references/CONTENT-GUIDES.md) | Content creation patterns and examples |
| [references/ACTIVITY-TEMPLATE.md](references/ACTIVITY-TEMPLATE.md) | Template for activity configuration |
| [references/CURRICULUM-DESIGNER-TIPS.md](references/CURRICULUM-DESIGNER-TIPS.md) | Guidelines for curriculum designers |
| [references/NAMING-SYSTEM.md](references/NAMING-SYSTEM.md) | Lesson ID, Activity ID, and Context File naming |

## Platform Notes

LeadersPath provides learners with transparency—they can view the system prompt, context files, and skill configurations for each activity. This supports the pedagogical goal of teaching how AI configuration works.

## License

Part of the [Anthropic Skills Library](https://github.com/anthropics/anthropic-skills). See repository license.
