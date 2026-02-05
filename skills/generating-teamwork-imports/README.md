# Generating Teamwork Imports

Generate Teamwork.com import files (.xlsx) from project planning materials, transcripts, and client dossiers.

## When to Use

Use this skill when you need to:
- Create a Teamwork.com project from planning documents
- Convert campaign overviews or project plans into importable task lists
- Build task structures from interview transcripts or client briefs

## How to Invoke

Say things like:
- "Generate a Teamwork import from this project plan"
- "Create a Teamwork project from this campaign overview"
- "Build task lists for Teamwork from this transcript"
- "Convert this plan to Teamwork format"

## What You'll Need

- Project planning materials (transcripts, dossiers, campaign overviews, or structured plans)
- Team members with **email addresses** (required for Teamwork assignment)
- Project name for Teamwork

## What You'll Get

1. **Audit document** (`[project-name]-teamwork-audit.md`) - Review the proposed task structure before generating the import file
2. **Excel import file** (`[project-name]-teamwork-import.xlsx`) - Ready to import into Teamwork.com
3. **Optional template** - Anonymized version for reuse on similar projects

## Example

**Input:** A campaign planning document describing editorial review, design work, and marketing activities with some deadlines.

**Output:** An Excel file with:
- Task lists organized by area of concern (Editorial, Design, Marketing)
- Tasks and subtasks derived from the source content
- Dates only where explicitly specified in the source
- Assignments using email addresses (required by Teamwork)

## Key Rules

This skill enforces several rules to produce clean, actionable task lists:

- **No hallucinated dates** - Only dates explicitly in your source appear in the import
- **No hallucinated time estimates** - "About a week" is not a time estimate
- **Area-based organization** - Task lists by department/function, not timeline phases
- **Email addresses required** - Teamwork needs emails, not names, for assignments
- **No forced subtasks** - Tasks without natural subdivisions stay as single tasks
- **Dependency ordering** - Tasks ordered so dependencies come before dependents

## Tips

- Run transcripts through the `synthesizing-interviews` skill first for better structure
- Provide team member emails upfront: "Designer: jane@company.com, Developer: bob@company.com"
- The skill will ask about your minimum time threshold for subtasks (default: 15 min)
- Review the audit document carefully before approving Excel generation
