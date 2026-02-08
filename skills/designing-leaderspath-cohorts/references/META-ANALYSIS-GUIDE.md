# Post-Build Meta-Analysis Guide

This guide provides detailed instructions for Phase 6 of the designing-leaderspath-cohorts workflow. Phase 6 runs AFTER all courses have been built by `building-leaderspath-curriculum`.

## Purpose

The meta-analysis reviews what was actually built against the original design intent. It surfaces insights from the building process, identifies gaps, and curates supplementary resources that feed into the cohort email series.

## Required Inputs

Before starting the meta-analysis, gather:

1. **Cohort design document** — The final cohort curriculum from Phase 3
2. **Source materials** — All interview syntheses, articles, and organizational docs used in design
3. **All curriculum prompts** — The course curriculum prompts from Phase 4
4. **All built course files:**
   - Facilitator guides
   - Activity configurations
   - Learner overviews
   - Q&A bot configs (if applicable)
5. **Tracking documents** — Cohort tracker and any session logs
6. **Context registry** — If demo contexts were used

## Meta-Analysis Structure

The meta-analysis report follows this structure:

### Section 1: Alignment — Do the Courses Meet the Cohort Design Intent?

**What to assess:**

- Did the built courses faithfully deliver the cohort design's vision?
- What aligned well between design and implementation?
- Where did courses diverge from the original design?
- Were divergences improvements or gaps?

**Document specific findings:**

| Design Element | Status | Notes |
|----------------|--------|-------|
| [Learning objective] | Aligned / Diverged / Missing | [Details] |

### Section 2: Insights from the Course Building Process

**What to surface:**

- What emerged during construction that wasn't in the original design?
- New frameworks or teaching approaches that developed
- Pacing or sequencing insights
- Meta-layers (e.g., Q&A bots that model the principles they teach)

**Key questions:**

- Did any distinctions become clearer through building? (e.g., behavioral training vs. context)
- Did course atomicity hold up?
- What teaching patterns proved effective?

### Section 3: Gap Analysis — What's Missing?

**Create a coverage matrix:**

| Source Topic | Covered In | Status | Notes |
|--------------|------------|--------|-------|
| [Topic from interview/design] | [Course ID] | Covered / Partial / Not covered | [Details] |

**Categories of gaps:**

1. **Interview topics not covered** — Themes from source materials that didn't make it into courses
2. **Design themes underrepresented** — Ideas mentioned in cohort design but not fully developed
3. **Missing connective tissue** — Between-session activities, cohort-level discussion arcs

**Recommendations format:**

For each gap, assess:
- Can it be addressed through supplementary materials? (Quick win)
- Does it need facilitator resources? (Medium effort)
- Does it require course revision? (Future iteration)

### Section 4: Supplementary Reading — External Articles

Curate articles from credible sources organized by cohort theme.

**Source priorities:**
1. Anthropic (research and blog)
2. Harvard Business Review
3. Stanford HAI
4. Pew Research
5. Brookings Institution
6. Stanford Social Innovation Review

**Curation criteria:**

| Criterion | Requirement |
|-----------|-------------|
| Audience | Accessible to non-technical leaders |
| Length | Under 15 minutes to read |
| Credibility | From established, reputable sources |
| Relevance | Directly connected to cohort themes |
| Angle | Adds perspective not covered in courses |

**Article entry format:**

```markdown
| # | Title | Source | Date | Description | Link |
|---|-------|--------|------|-------------|------|
| 1 | [Title] | [Source] | [Date] | [1-2 sentence description] | [Link] |
```

**Organize by theme:** Group articles under theme headings that match the cohort's major topics.

### Section 5: Supplementary Viewing — Video Resources

**IMPORTANT:** Use the `researching-youtube-channels` skill for video research. Do not attempt WebFetch for YouTube — it doesn't work reliably. The skill uses `yt-dlp` scripts to fetch channel metadata and filter by theme.

**Priority channels:**
- Anthropic official channel (@anthropic-ai)
- Channels relevant to the cohort's domain

**Video entry format:**

```markdown
| # | Title | Length | Date | Description | Themes |
|---|-------|--------|------|-------------|--------|
| 1 | [Title] | [X min] | [Date] | [Description] | [Relevant themes] |
```

**Viewing package format:**

Create suggested viewing packages per course:

```markdown
| Course | Required Viewing (Pre-Session) | Optional Deep Dive |
|--------|-------------------------------|-------------------|
| [Course ID] | [Video title] ([X min]) | [Longer video] ([X min]) |
```

### Section 6: Summary of Recommendations

Organize recommendations by priority:

**Priority 1: Quick Wins (Supplementary Materials)**
- Low effort, can be created immediately
- Examples: between-session activities, curated reading lists

**Priority 2: Facilitator Resources**
- Medium effort, improves delivery
- Examples: case study snippets, discussion arc guides

**Priority 3: Future Iteration Candidates**
- Higher effort, for next cohort version
- Examples: new activities, course revisions

## Output

Save the meta-analysis to:

```
[working-folder]/cohort-meta-analysis-[YYYY-MM-DD].md
```

Use the date the analysis is completed.

## Example Meta-Analysis Excerpt

```markdown
# Meta-Analysis: [Cohort Name]

**Date:** [Date]
**Scope:** Review of built courses against cohort design intent

## Section 1: Alignment

**Overall assessment:** [Strong / Adequate / Gaps identified]

### What Aligned Well

- The comparison-pair pedagogy survived intact across all hands-on courses
- Course atomicity holds — no course references another by name
- The philosophical foundation from source interviews appears in facilitator guides

### Where Courses Diverged

| Design Element | Divergence | Assessment |
|----------------|------------|------------|
| Activity count per course | Design listed 7; built courses have 3-7 | Correct call — conceptual content became facilitator-led |

## Section 3: Gap Analysis

| Source Topic | Status | Notes |
|--------------|--------|-------|
| Between-session homework | Not covered | Courses include reflection but no structured take-home work |
| Cohort-level discussion arc | Not covered | Discussion exists per-course but not mapped across weeks |

### Recommendations

**Quick Win:** Create between-session activities document
**Facilitator Resource:** Create cohort discussion arc guide
```

## Dependency Note

The meta-analysis must be completed before Phase 7 (Cohort Email Series). The curated resource lists (articles and videos) feed directly into the post-session emails.
