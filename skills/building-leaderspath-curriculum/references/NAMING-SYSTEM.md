# LeadersPath Curriculum Naming System

Naming conventions for all LeadersPath curriculum entities. These ensure consistency across the file system, WordPress imports, YAML registries, and skill outputs.

---

## Unified ID Format

All entities use `PREFIX###-slug`:

| Entity | Prefix | Example |
|--------|--------|---------|
| Course | CRS | `CRS001-ethical-ai-nonprofit-leaders` |
| Lesson | LSN | `LSN001-skills-framework` |
| Activity | ACT | `ACT001-meeting-report-vanilla` |
| Context | CTX | `CTX004-agent-behavioral-standards` |

### Rules

- **Sequential numbering.** Use `next_id` from the registry YAML to get the next number.
- **Globally unique.** No two entities of the same type share a number.
- **Permanent.** Once assigned, an ID is never reassigned even if archived.
- **Three-digit, zero-padded.** `001`, `002`, ... `999`.

### Slug Rules

- kebab-case (lowercase, hyphens between words)
- 3-50 characters
- Must start with a letter
- Letters, numbers, hyphens only
- No consecutive hyphens

**Good slugs:** `ai-foundations`, `meeting-report-vanilla`, `ethical-ai-nonprofit-leaders`
**Bad slugs:** `AI_Basics`, `1-intro`, `my--lesson`

---

## Course IDs

```
CRS###-slug
```

**Examples:**
- `CRS001-ethical-ai-nonprofit-leaders`
- `CRS002-executive-ai-literacy`

Assigned from `course-registry.yaml`. A course selects and sequences lessons.

---

## Lesson IDs

```
LSN###-slug
```

**Examples:**
- `LSN001-skills-framework`
- `LSN002-ai-foundations`
- `LSN006-context-libraries`

Assigned from `lesson-registry.yaml`. Lessons are atomic and reusable across courses. Categorization (topic, difficulty) lives in lesson metadata and the registry, not in the ID.

---

## Activity IDs

```
ACT###-slug
```

**Examples:**
- `ACT001-meeting-report-vanilla`
- `ACT005-concept-explorer`
- `ACT020-adding-identity`

Activities are children of lessons. Their parent lesson is tracked in `lesson-registry.yaml`. Activity folders live inside `activities/` of their parent lesson.

**Globally unique numbering.** ACT### numbers are assigned sequentially across all lessons, not per-lesson.

---

## Context File IDs

```
CTX###-slug.md
```

**Examples:**
- `CTX004-agent-behavioral-standards.md`
- `CTX101-readers-united-identity.md`

Assigned from `context-registry.yaml`.

### Number Ranges

- CTX001-099: Real organizational contexts
- CTX101-199: Demo contexts for teaching
- CTX201+: Reserved

### Scope

- **Global:** Used across multiple lessons. Stored in `Curriculum/Contexts/`.
- **Lesson-specific:** Used only within one lesson. Stored in `activities/shared-context/`.

Both use the same `CTX###-slug.md` format.

---

## Validation Patterns

```
Course:   ^CRS[0-9]{3}-[a-z][a-z0-9-]{2,49}$
Lesson:   ^LSN[0-9]{3}-[a-z][a-z0-9-]{2,49}$
Activity: ^ACT[0-9]{3}-[a-z][a-z0-9-]{2,49}$
Context:  ^CTX[0-9]{3}-[a-z][a-z0-9-]{2,49}\.md$
```

---

## Registry Format

Registries are YAML files in `Curriculum/Registry/`:

- `course-registry.yaml` — CRS### IDs
- `lesson-registry.yaml` — LSN### IDs with child ACT### lists
- `context-registry.yaml` — CTX### IDs

Each registry has a `next_id` (or `next_real_id`/`next_demo_id` for contexts) counter. Increment after each assignment.

---

## WordPress Mapping

| Entity | WordPress Post Slug |
|--------|---------------------|
| Course | `crs001-ethical-ai-nonprofit-leaders` |
| Lesson | `lsn001-skills-framework` |
| Activity | `act001-meeting-report-vanilla` |
| Context | `ctx004-agent-behavioral-standards` |

All slugs are the ID lowercased. Globally unique by construction.

---

## Folder Structure

### Lesson Output (building-leaderspath-curriculum)

```
Curriculum/Lessons/LSN###-slug/
├── lesson-metadata.md
├── learning-objectives.md
├── facilitator-guide.md
├── learner-overview.md
├── lesson-tracker.md
├── qa-chatbot-config.md           # Optional
└── activities/
    ├── ACT###-slug/
    │   ├── instructions.md
    │   └── configuration/
    │       ├── system-prompt.md
    │       ├── api-settings.md
    │       └── context-files.md
    ├── ACT###-slug/
    │   └── [same structure]
    └── shared-context/
        └── CTX###-slug.md
```

### Course Output (designing-leaderspath-courses)

```
Curriculum/Courses/CRS###-slug/
├── course-curriculum.md
├── course-tracker.md
├── lesson-reuse-report.md
├── Source Materials/
└── Lesson Prompts/
    ├── LSN###-slug-curriculum.md
    └── ...
```

---

## Quick Reference

| Element | Format | Example |
|---------|--------|---------|
| Course ID | `CRS###-slug` | `CRS001-ethical-ai-nonprofit-leaders` |
| Lesson ID | `LSN###-slug` | `LSN001-skills-framework` |
| Activity ID | `ACT###-slug` | `ACT001-meeting-report-vanilla` |
| Context File | `CTX###-slug.md` | `CTX004-agent-behavioral-standards.md` |
| Lesson Folder | `Curriculum/Lessons/LSN###-slug/` | `Curriculum/Lessons/LSN001-skills-framework/` |
| Activity Folder | `activities/ACT###-slug/` | `activities/ACT001-meeting-report-vanilla/` |
| Curriculum Prompt | `LSN###-slug-curriculum.md` | `LSN001-skills-framework-curriculum.md` |
