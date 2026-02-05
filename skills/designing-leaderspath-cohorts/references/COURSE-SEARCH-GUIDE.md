# Course Search Guide

This document explains how to search for existing courses that can be reused in a new cohort.

## Why Reuse Matters

Creating courses is expensive—both in design time and in the curriculum-building process. Reusing well-designed courses:

1. **Saves time** — No need to redesign what already works
2. **Maintains quality** — Tested courses are proven effective
3. **Enables iteration** — Improvements benefit all cohorts using the course
4. **Reduces maintenance** — Fewer unique courses to maintain

**Default to reuse.** Only create new courses when existing ones don't fit.

---

## Where to Search

### Standard Locations

Look for course curriculum files in these patterns:
- `**/Courses/*-curriculum.md`
- `**/course-metadata.md`
- `**/*-curriculum.md`

### User-Specified Locations

Always ask: "Is there an existing course library I should search?"

Users may have courses in:
- Shared team folders
- Previous cohort designs
- Template libraries

---

## What to Look For

### In Course Curriculum Files

Extract:
1. **Course name and description**
2. **Learning objectives** — What learners achieve
3. **Target audience** — Who the course is for
4. **Prerequisites** — What prior knowledge is assumed
5. **Key concepts** — Topics covered
6. **Activities** — What experiences are included

### Matching Criteria

A course is a **good match** if:
- Learning objectives align with cohort goals
- Target audience is compatible
- Key concepts cover needed themes
- Difficulty level is appropriate

A course is a **partial match** if:
- Most objectives align but some gaps exist
- Audience is compatible but not identical
- Most concepts covered with minor gaps

A course **doesn't fit** if:
- Learning objectives don't align with cohort goals
- Target audience is incompatible
- Key concepts miss critical themes
- Difficulty level is wrong

---

## Search Process

### Step 1: List Available Courses

```bash
# Find all curriculum files
find . -name "*-curriculum.md" -type f
```

Or use the Glob tool:
```
pattern: "**/*-curriculum.md"
```

### Step 2: Read Each Course

For each file found:
1. Read the Course Overview section
2. Read the Learning Objectives section
3. Note the key concepts covered

### Step 3: Compare to Learning Themes

Map each course against the learning themes identified from source analysis:

| Learning Theme | Course A | Course B | Course C |
|----------------|----------|----------|----------|
| Theme 1 | ✓ covers | partial | — |
| Theme 2 | — | ✓ covers | — |
| Theme 3 | — | — | ✓ covers |
| Theme 4 | — | partial | partial |

### Step 4: Make Recommendations

Based on the mapping:
- **Reuse directly:** Course fully covers needed themes
- **Reuse with adaptation:** Course partially covers; may need supplemental content
- **Create new:** No existing course fits

---

## The Course Reuse Report

Document findings in `course-reuse-report.md`:

```markdown
# Course Reuse Report: [Cohort Name]

## Search Scope
- Searched: [locations searched]
- Courses found: [count]

## Existing Courses That Fit

| Course | File | Covers Themes | Recommendation |
|--------|------|---------------|----------------|
| AI Foundations | `01-AI-Foundations-curriculum.md` | 1, 2 | Reuse directly |
| Context Libraries | `03-Context-Libraries-curriculum.md` | 3 | Reuse with notes |

## Courses to Create New

| Course Needed | Themes Covered | Why Not Reusing |
|---------------|----------------|-----------------|
| Custom Ethics | 4, 5 | No existing course covers org-specific ethics |

## Gaps to Address

[Any themes that aren't fully covered by existing or planned courses]

## Recommendations

1. Reuse [Course A] as Session 1
2. Reuse [Course B] as Session 2
3. Create new [Course C] for Sessions 3-4
4. Note: Theme 5 needs supplemental content added to [Course B]
```

---

## Handling Partial Matches

When a course partially fits:

### Option 1: Reuse and Supplement
- Use the existing course as-is
- Add supplemental content in the cohort curriculum
- Facilitator bridges the gap

### Option 2: Create Variant
- Copy the course as a starting point
- Modify for the specific cohort
- Maintain both versions

### Option 3: Combine Courses
- Use portions of multiple courses
- Create new course that references existing materials
- Avoid duplication

**Prefer Option 1** when gaps are small. Only create variants when changes are substantial.

---

## When No Courses Exist

If no course library is available:
1. Document that no existing courses were searched
2. All courses will be new
3. Consider building a reusable course library as a secondary goal

Even when creating new courses, design them for future reuse:
- Keep them atomic (no course cross-references)
- Use generic examples where possible
- Document assumptions clearly
