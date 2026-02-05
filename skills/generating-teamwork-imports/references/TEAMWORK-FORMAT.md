# Teamwork.com Import Format Reference

This document details the Excel/CSV import format for Teamwork.com projects.

## File Format

Teamwork accepts both CSV and Excel (.xlsx) files. Excel is preferred for reliability.

## Column Specification

| Column | Required | Description | Valid Values |
|--------|----------|-------------|--------------|
| TASKLIST | No | Task list name | Text. Only include on first row of each list. |
| TASK | Yes | Task or subtask name | Text. Prefix with `-` for subtasks. |
| DESCRIPTION | No | Task list or task description | Text. Only on task list rows or tasks. |
| ASSIGN TO | No | Person assigned | **Email address required.** Must match existing Teamwork user. |
| START DATE | No | Task start date | YYYY-MM-DD format |
| DUE DATE | No | Task due date | YYYY-MM-DD format |
| PRIORITY | No | Task priority | High, Medium, Low |
| ESTIMATED TIME | No | Time estimate | Format: 30m, 1hr, 2hr 30m |
| TAGS | No | Task tags | Comma-separated |
| STATUS | No | Task status | Active, Completed |

## Hierarchy Structure

Teamwork uses a 4-level hierarchy:

```
Project (created in Teamwork, not in import)
└── Task List
    └── Task
        └── Subtask
```

### How Hierarchy is Represented

The import file is flat (rows), but hierarchy is inferred:

1. **Task List**: Row with TASKLIST column filled, TASK empty or contains list name
2. **Task**: Row with TASK column filled, no dash prefix
3. **Subtask**: Row with TASK column starting with `-` (dash)

### Example Structure

```
TASKLIST          | TASK                        | DESCRIPTION
------------------|-----------------------------|-----------------------
Editorial         |                             | Editorial processes
                  | Copyediting                 |
                  | -Initial review             |
                  | -Author revisions           |
                  | Proofreading                |
                  | -Final proofread            |
Design            |                             | Visual production
                  | Cover design                |
```

## Subtask Convention

Subtasks are indicated by prefixing the task name with a dash (`-`):

- `-Initial review` is a subtask of the preceding task
- Subtasks inherit the assignee from their parent task
- Subtasks cannot have their own subtasks (only 1 level deep)

## Time Estimate Formats

Teamwork accepts several formats:

| Input | Interpretation |
|-------|---------------|
| 30m | 30 minutes |
| 1hr | 1 hour |
| 2hr | 2 hours |
| 1hr 30m | 1.5 hours |
| 90m | 90 minutes |

## Date Formats

Use ISO format for reliability:

- Preferred: `2024-03-15` (YYYY-MM-DD)
- Also works: `03/15/2024` (MM/DD/YYYY)
- Avoid: `15/03/2024` (ambiguous)

## Priority Values

Only three values are valid:
- `High`
- `Medium` (or `Med`)
- `Low`

Case-insensitive.

## Assignment Rules

The ASSIGN TO field **requires an email address** that matches an existing Teamwork user:
- Use the user's email address (e.g., `jane@company.com`)
- Display names alone will NOT work for import
- If email doesn't match a Teamwork user, the task will be unassigned after import
- Leave blank if assignment should be done manually in Teamwork

## Import Notes

1. **First row is headers** — The import expects column headers in row 1
2. **Empty cells are ignored** — Leave cells blank for no value (not "N/A" or "None")
3. **UTF-8 encoding** — Save files with UTF-8 encoding for special characters
4. **Maximum 500 rows** — Large imports should be split into multiple files

## Common Import Errors

| Error | Cause | Fix |
|-------|-------|-----|
| "Invalid date format" | Date not recognized | Use YYYY-MM-DD |
| "User not found" | ASSIGN TO doesn't match | Use email address, not display name |
| "Invalid priority" | Priority value wrong | Use High, Medium, or Low |
| "Task list required" | First task has no list | Add task list row before tasks |

## Example: Complete Import File

```
TASKLIST,TASK,DESCRIPTION,ASSIGN TO,START DATE,DUE DATE,PRIORITY,ESTIMATED TIME,TAGS,STATUS
New Client Onboarding,,Welcome and initial setup.,,,,,,,
,Set up client project,,jane@company.com,2024-01-15,2024-01-18,High,30m,Setup,Active
,-Create project folder,,,,,,,Setup,Active
,-Add client brief,,,,,,,Setup,Active
,Send welcome materials,,jane@company.com,,2024-01-20,Medium,1hr,Communications,Active
Client Kick-off Meeting,,First meeting prep and follow-up.,,,,,,,
,Prepare meeting agenda,,bob@company.com,2024-01-22,2024-01-25,High,2hr,Meeting,Active
,-Draft agenda,,,,,,,Meeting,Active
,-Send to client for review,,,,,,,Meeting,Active
```
