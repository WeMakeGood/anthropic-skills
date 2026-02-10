# Lesson Search Guide

This document explains how to search for existing lessons that can be reused in a new course.

## Why Reuse Matters

Creating lessons is expensive—both in design time and in the curriculum-building process. Reusing well-designed lessons:

1. **Saves time** — No need to redesign what already works
2. **Maintains quality** — Tested lessons are proven effective
3. **Enables iteration** — Improvements benefit all courses using the lesson
4. **Reduces maintenance** — Fewer unique lessons to maintain

**Default to reuse.** Only create new lessons when existing ones don't fit.

---

## Where to Search

### Standard Locations

Look for lesson curriculum files in these patterns:
- `**/Lessons/*-curriculum.md`
- `**/lesson-metadata.md`
- `**/*-curriculum.md`

### User-Specified Locations

Always ask: "Is there an existing lesson library I should search?"

Users may have lessons in:
- Shared team folders
- Previous course designs
- Template libraries

---

## What to Look For

### In Lesson Curriculum Files

Extract:
1. **Lesson name and description**
2. **Learning objectives** — What learners achieve
3. **Target audience** — Who the lesson is for
4. **Prerequisites** — What prior knowledge is assumed
5. **Key concepts** — Topics covered
6. **Activities** — What experiences are included

### Matching Criteria

A lesson is a **good match** if:
- Learning objectives align with course goals
- Target audience is compatible
- Key concepts cover needed themes
- Difficulty level is appropriate

A lesson is a **partial match** if:
- Most objectives align but some gaps exist
- Audience is compatible but not identical
- Most concepts covered with minor gaps

A lesson **doesn't fit** if:
- Learning objectives don't align with course goals
- Target audience is incompatible
- Key concepts miss critical themes
- Difficulty level is wrong

---

## Search Process

### Step 1: List Available Lessons

```bash
# Find all curriculum files
find . -name "*-curriculum.md" -type f
```

Or use the Glob tool:
```
pattern: "**/*-curriculum.md"
```

### Step 2: Read Each Lesson

For each file found:
1. Read the Lesson Overview section
2. Read the Learning Objectives section
3. Note the key concepts covered

### Step 3: Compare to Learning Themes

Map each lesson against the learning themes identified from source analysis:

| Learning Theme | Lesson A | Lesson B | Lesson C |
|----------------|----------|----------|----------|
| Theme 1 | ✓ covers | partial | — |
| Theme 2 | — | ✓ covers | — |
| Theme 3 | — | — | ✓ covers |
| Theme 4 | — | partial | partial |

### Step 4: Make Recommendations

Based on the mapping:
- **Reuse directly:** Lesson fully covers needed themes
- **Reuse with adaptation:** Lesson partially covers; may need supplemental content
- **Create new:** No existing lesson fits

---

## The Lesson Reuse Report

Document findings in `lesson-reuse-report.md`:

```markdown
# Lesson Reuse Report: [Course Name]

## Search Scope
- Searched: [locations searched]
- Lessons found: [count]

## Existing Lessons That Fit

| Lesson | File | Covers Themes | Recommendation |
|--------|------|---------------|----------------|
| AI Foundations | `01-AI-Foundations-curriculum.md` | 1, 2 | Reuse directly |
| Context Libraries | `03-Context-Libraries-curriculum.md` | 3 | Reuse with notes |

## Lessons to Create New

| Lesson Needed | Themes Covered | Why Not Reusing |
|---------------|----------------|-----------------|
| Custom Ethics | 4, 5 | No existing lesson covers org-specific ethics |

## Gaps to Address

[Any themes that aren't fully covered by existing or planned lessons]

## Recommendations

1. Reuse [Lesson A] as Session 1
2. Reuse [Lesson B] as Session 2
3. Create new [Lesson C] for Sessions 3-4
4. Note: Theme 5 needs supplemental content added to [Lesson B]
```

---

## Handling Partial Matches

When a lesson partially fits:

### Option 1: Reuse and Supplement
- Use the existing lesson as-is
- Add supplemental content in the course curriculum
- Facilitator bridges the gap

### Option 2: Create Variant
- Copy the lesson as a starting point
- Modify for the specific course
- Maintain both versions

### Option 3: Combine Lessons
- Use portions of multiple lessons
- Create new lesson that references existing materials
- Avoid duplication

**Prefer Option 1** when gaps are small. Only create variants when changes are substantial.

---

## When No Lessons Exist

If no lesson library is available:
1. Document that no existing lessons were searched
2. All lessons will be new
3. Consider building a reusable lesson library as a secondary goal

Even when creating new lessons, design them for future reuse:
- Keep them atomic (no lesson cross-references)
- Use generic examples where possible
- Document assumptions clearly
