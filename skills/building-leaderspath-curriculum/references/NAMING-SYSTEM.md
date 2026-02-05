# LeadersPath Curriculum Naming System

This document defines the naming conventions for LeadersPath courses, activities, and context files. These conventions ensure consistency, enable WordPress import, and support curriculum reuse across cohorts.

---

## Course ID Format

```
TOPIC-LEVEL-slug
```

**Examples:**
- `FUND-101-ai-basics`
- `PRMPT-201-advanced-techniques`
- `CTX-101-intro-to-context`
- `ETH-301-responsible-ai-leadership`

### Topic Codes

| Code | Topic | Description |
|------|-------|-------------|
| `FUND` | Fundamentals | How AI works, capabilities, limitations |
| `PRMPT` | Prompting | Interaction techniques, effective prompting |
| `CTX` | Context & Knowledge | Context libraries, organizational knowledge |
| `ETH` | Ethics & Responsibility | Bias, transparency, responsible use |
| `APP` | Applications | Writing, research, analysis, communication |

**Note:** These codes cover most curriculum needs. If a course doesn't fit neatly, use the closest match or ask the user which code applies.

### Level Codes

| Range | Level | Description |
|-------|-------|-------------|
| `101-199` | Foundations | Beginner, no prior knowledge assumed |
| `201-299` | Intermediate | Builds on foundational concepts |
| `301-399` | Advanced | Deep expertise, complex applications |
| `401+` | Specialized | Expert topics, niche applications |

### Slug Rules

- **Format:** kebab-case (lowercase, hyphens between words)
- **Length:** 3-50 characters
- **Start:** Must begin with a letter
- **Characters:** Letters, numbers, hyphens only
- **No consecutive hyphens**

**Good slugs:** `ai-basics`, `effective-prompting`, `context-transforms`
**Bad slugs:** `AI_Basics`, `1-intro`, `my--course`

---

## Activity ID Format

```
TOPIC-LEVEL-ACT-slug
```

**Examples:**
- `FUND-101-ACT-starting-from-zero`
- `FUND-101-ACT-context-transforms`
- `PRMPT-201-ACT-chain-of-thought`

### Construction

1. Start with the parent Course ID's topic and level: `FUND-101`
2. Add literal `ACT`: `FUND-101-ACT`
3. Add activity slug: `FUND-101-ACT-starting-from-zero`

### Activity Slug Rules

Same rules as course slugs:
- kebab-case, 3-50 characters, starts with letter
- Generated from activity name: "Starting from Zero" → `starting-from-zero`

### Global Uniqueness

The course ID prefix makes activities globally unique by construction. No separate registry is needed—just ensure no duplicate slugs within the same course.

---

## Context File ID Format

```
CTX###-slug.md
```

**Examples:**
- `CTX001-org-identity.md`
- `CTX002-brand-voice.md`
- `CTX015-foundations-terminology.md`

### Construction

1. Prefix: `CTX` (literal)
2. Number: Three digits, zero-padded (`001`, `002`, ... `999`)
3. Slug: kebab-case descriptor
4. Extension: `.md`

### Numbering

- Numbers are assigned sequentially from a registry
- If a registry is provided, find the next available number
- If no registry exists, start from `CTX001`

### Scope

Context files can be:
- **Shared globally:** Used across multiple courses (stored in a shared context library)
- **Course-specific:** Used only within one course (stored in `activities/shared-context/`)

Both use the same `CTX###-slug.md` format for consistency.

---

## Validation Rules

### Course ID Validation

```
Pattern: ^(FUND|PRMPT|CTX|ETH|APP)-[1-4][0-9]{2}-[a-z][a-z0-9-]{2,49}$
```

- Topic: One of FUND, PRMPT, CTX, ETH, APP (uppercase)
- Level: 101-499 (three digits)
- Slug: 3-50 characters, starts with letter, kebab-case
- Must be unique (check course-id-log if provided)

### Activity ID Validation

```
Pattern: ^(FUND|PRMPT|CTX|ETH|APP)-[1-4][0-9]{2}-ACT-[a-z][a-z0-9-]{2,49}$
```

- Topic-Level: Must match parent course
- ACT: Literal string (uppercase)
- Slug: 3-50 characters, starts with letter, kebab-case
- Must be unique within the course

### Context File ID Validation

```
Pattern: ^CTX[0-9]{3}-[a-z][a-z0-9-]{2,49}\.md$
```

- CTX: Literal prefix
- Number: 001-999 (three digits, zero-padded)
- Slug: 3-50 characters, starts with letter, kebab-case
- Must be sequential (check registry if provided)

---

## Log File Formats

### course-id-log.md

Tracks assigned Course IDs organized by topic.

```markdown
# Course ID Log

Tracks Course ID assignments to avoid conflicts and find available IDs.

---

## FUND - Fundamentals

| ID | Slug | Title | Date Assigned | Status | Notes |
|----|------|-------|---------------|--------|-------|
| FUND-101 | ai-basics | AI Foundations | 2026-02-05 | Published | First LeadersPath course |
| FUND-102 | capabilities-limits | AI Capabilities & Limitations | 2026-02-10 | Development | |

## PRMPT - Prompting

| ID | Slug | Title | Date Assigned | Status | Notes |
|----|------|-------|---------------|--------|-------|
| PRMPT-101 | intro-prompting | Introduction to Prompting | 2026-02-12 | Development | |

## CTX - Context & Knowledge

| ID | Slug | Title | Date Assigned | Status | Notes |
|----|------|-------|---------------|--------|-------|

## ETH - Ethics & Responsibility

| ID | Slug | Title | Date Assigned | Status | Notes |
|----|------|-------|---------------|--------|-------|

## APP - Applications

| ID | Slug | Title | Date Assigned | Status | Notes |
|----|------|-------|---------------|--------|-------|
```

**Status values:** `Design`, `Development`, `Review`, `Published`, `Archived`

### context-file-registry.md

Tracks assigned Context File IDs.

```markdown
# Context File Registry

Tracks CTX### assignments for sequential numbering.

---

## Registry

| ID | Slug | Description | Scope | Location | Date Created |
|----|------|-------------|-------|----------|--------------|
| CTX001 | org-identity | Organization identity and mission | Global | Context Library | 2026-02-05 |
| CTX002 | brand-voice | Brand voice guidelines | Global | Context Library | 2026-02-05 |
| CTX003 | behavioral-standards | AI behavioral training | Global | Context Library | 2026-02-06 |
| CTX004 | prose-standards | Natural prose guidelines | Global | Context Library | 2026-02-06 |
| CTX005 | foundations-terminology | Course-specific terms | Course | FUND-101 | 2026-02-07 |

---

## Next Available ID

CTX006
```

**Scope values:** `Global` (shared library), `Course` (course-specific)

---

## WordPress Mapping

When importing to WordPress LeadersPath plugin:

| Curriculum Element | WordPress Post Slug |
|--------------------|---------------------|
| Course | `TOPIC-LEVEL-slug` (lowercase) |
| Activity | `TOPIC-LEVEL-ACT-slug` (lowercase) |
| Context File | `CTX###-slug` (lowercase) |

**Examples:**
- Course `FUND-101-ai-basics` → slug `fund-101-ai-basics`
- Activity `FUND-101-ACT-starting-from-zero` → slug `fund-101-act-starting-from-zero`
- Context file `CTX001-org-identity.md` → slug `ctx001-org-identity`

Activity slugs include the full course ID prefix, making them globally unique in WordPress without requiring a separate uniqueness check.

---

## Folder Structure

### Course Output (building-leaderspath-curriculum)

```
[working-folder]/
├── course-tracker.md
├── course-metadata.md
├── learning-objectives.md
├── facilitator-guide.md
├── learner-overview.md
├── qa-chatbot-config.md              # Optional
├── course-id-log.md                  # New/updated entries
└── activities/
    ├── TOPIC-LEVEL-ACT-first-activity/
    │   ├── configuration/
    │   │   ├── system-prompt.md
    │   │   ├── api-settings.md
    │   │   └── context-files.md
    │   └── instructions.md
    ├── TOPIC-LEVEL-ACT-second-activity/
    │   └── [same structure]
    └── shared-context/
        └── CTX###-slug.md            # Course-specific context
```

### Cohort Output (designing-leaderspath-cohorts)

```
[working-folder]/
├── cohort-tracker.md
├── cohort-curriculum.md
├── course-reuse-report.md
├── course-id-log.md                  # New/updated entries
└── Courses/
    ├── FUND-101-ai-basics-curriculum.md
    ├── PRMPT-201-effective-prompting-curriculum.md
    └── ...
```

---

## Quick Reference

| Element | Format | Example |
|---------|--------|---------|
| Course ID | `TOPIC-LEVEL-slug` | `FUND-101-ai-basics` |
| Activity ID | `TOPIC-LEVEL-ACT-slug` | `FUND-101-ACT-starting-from-zero` |
| Context File | `CTX###-slug.md` | `CTX001-org-identity.md` |
| Activity Folder | `activities/TOPIC-LEVEL-ACT-slug/` | `activities/FUND-101-ACT-starting-from-zero/` |
| Curriculum Prompt | `TOPIC-LEVEL-slug-curriculum.md` | `FUND-101-ai-basics-curriculum.md` |
