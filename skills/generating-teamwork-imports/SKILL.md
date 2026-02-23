---
name: generating-teamwork-imports
description: Generates Teamwork.com import files (.xlsx) from project planning materials, transcripts, campaign overviews, and client dossiers. Use when creating project task lists for Teamwork, building project structures from planning documents, or converting project plans to Teamwork format. Activates when user says generate Teamwork import, create Teamwork project, build task list for Teamwork, or convert plan to Teamwork. Works with pasted text, attached files, or uploaded documents.
---

# Generating Teamwork Imports

<purpose>
LLMs default to creating plausible-looking project structures with hallucinated dates, times, and deliverables. This causes chaos—cluttered calendars full of AI-invented deadlines. This skill exists because Teamwork.com is used for time tracking and invoicing, so every task must be real, actionable, and grounded in source materials.
</purpose>

## Critical Rules

**GROUNDING:** Base ALL tasks, dates, times, and deliverables ONLY on provided source materials. If a date, time estimate, deliverable, or task name is not explicitly stated in the source, leave it empty rather than inventing a value. This applies especially to due dates, start dates, and time estimates — an empty field is honest; a plausible-looking date is a hallucination that clutters calendars and erodes trust.

**MINIMUM TIME THRESHOLD:** Subtasks must represent meaningful work chunks. Default minimum is 15 minutes unless the user specifies otherwise. Tasks like "send an email" are too granular—combine them into meaningful work units.

**AREA-BASED ORGANIZATION:** Task lists represent areas of concern (Editorial, Production, Marketing), NOT timeline phases. Do not create task lists organized as waterfall/Gantt stages.

**ASSIGNMENT CLARITY:** Tasks should be assigned to 1-2 people maximum. Do not mix assignments within a single task's subtasks—this confuses people trying to get work done.

**NO SINGLE SUBTASKS:** If a task would have only one subtask, don't create a subtask—just use the task. This prevents redundant nesting, NOT a requirement that every task must have subtasks. Tasks with no subtasks are valid and preferred when work doesn't naturally divide. Only create subtasks when the work genuinely splits into distinct pieces (e.g., "Research" has subtasks for different research activities, but "Write homepage copy" is just one task).

**DEPENDENCY ORDERING:** Within each task list, order tasks so dependencies come first. If Task B depends on Task A being complete, Task A must appear before Task B. This ensures logical workflow sequence in Teamwork.

**PROFESSIONAL OBJECTIVITY:** If source materials are incomplete, ambiguous, or contradictory, report this clearly rather than guessing. List specific gaps: "Source does not specify: [list missing items]. Please provide this information or confirm these should remain empty."

## Quick Start

1. User provides project planning materials
2. Skill identifies areas of concern and builds task hierarchy
3. Skill generates audit MD file for review
4. User approves structure
5. Skill runs Python script to generate Teamwork-compatible .xlsx file

## Workflow

Copy this checklist and track progress:

```
Progress:
- [ ] Phase 1: Gather inputs and configuration
- [ ] Phase 2: Analyze source materials
- [ ] Phase 3: Generate audit document
- [ ] Phase 4: User approval
- [ ] Phase 5: Generate Excel import file
- [ ] Phase 6: Optional template generation
```

<phase_gather>
### Phase 1: Gather Inputs

**REQUIRED inputs:**
- Project planning materials (transcripts, dossiers, campaign overviews, or structured plans)

**Configuration questions to ask:**

1. **Project name:** What should this project be called in Teamwork?

2. **Minimum time threshold:** What's the minimum meaningful task duration? (Default: 15 minutes)

3. **Team roles:** List the roles/people who will be assigned tasks with their **email addresses** (required for Teamwork import).
   - Example: "Editor: jane@company.com, Designer: bob@company.com"
   - If emails unavailable, use role classes: "Editor, Designer, Developer" (tasks will need manual email assignment in Teamwork after import)

4. **Template generation:** Would you like an anonymized template version for reuse?

**GATE:** Before proceeding, write:
- "Project name: [name]"
- "Minimum time threshold: [X] minutes"
- "Team roles: [list]"
- "Source materials received: [list files/content]"
</phase_gather>

<phase_analyze>
### Phase 2: Analyze Source Materials

Read all provided materials and identify:

1. **Areas of concern** — These become Task Lists
   - Group by domain/department, NOT by timeline
   - Examples: Editorial, Production, Marketing, Client Services, Technical

2. **Major work items** — These become Tasks
   - Should take meaningful time to complete
   - Can have subtasks assigned to same 1-2 people

3. **Individual work units** — These become Subtasks
   - Must meet minimum time threshold
   - Should be completable in a focused work session

4. **Dates and deadlines** — ONLY if explicitly stated in source
   - Do not infer or estimate dates
   - Leave empty if not specified

5. **Assignments** — Match to provided role list
   - If source specifies who does what, use that
   - If not, assign based on task type and role definitions

**Hierarchy rules:**
```
Project (provided by user)
└── Task List (area of concern)
    └── Task (major work item, 1-2 assignees)
        └── Subtask (individual work unit, same assignee as parent)
```

**GATE:** Before proceeding, write:
- "Areas of concern identified: [list]"
- "Total tasks identified: [count]"
- "Dates found in source: [list or 'none']"
</phase_analyze>

<phase_audit>
### Phase 3: Generate Audit Document

Create a markdown file for user review BEFORE generating the Excel file.

**Filename:** `[project-name]-teamwork-audit.md`

**Structure:**
```markdown
# [Project Name] - Teamwork Import Audit

## Configuration
- Minimum time threshold: [X] minutes
- Team roles: [list]

## Task Structure

### [Task List 1: Area Name]
Description: [from source or generated summary]

#### [Task 1.1: Task Name]
- Assignee: [role/person]
- Due date: [date or "Not specified"]
- Estimated time: [time or "Not specified"]
- Priority: [if specified]

##### Subtasks:
- [ ] [Subtask name] ([estimated time or "Not specified"])
- [ ] [Subtask name] ([estimated time or "Not specified"])

[Continue for all task lists, tasks, subtasks...]

## Validation Checklist
- [ ] All dates come from source materials
- [ ] All time estimates come from source materials
- [ ] No task lists organized by timeline
- [ ] All subtasks meet minimum time threshold
- [ ] Assignments limited to 1-2 people per task
- [ ] Task names derived from source content

## Source References
[List which source documents informed each section]
```

**GATE:** After generating, write:
- "Audit file saved to: [path]"
- "Total task lists: [count]"
- "Total tasks: [count]"
- "Total subtasks: [count]"
- "Awaiting user approval before generating Excel file"

**STOP.** Present the audit document to the user and wait for approval before proceeding.
</phase_audit>

<phase_approve>
### Phase 4: User Approval

Present the audit document and ask:

1. Does the task structure look correct?
2. Are there any missing areas of concern?
3. Should any tasks be reorganized?
4. Are the assignments appropriate?

Make requested changes and regenerate audit if needed.

**GATE:** User must explicitly approve before proceeding:
- "User approved structure: [yes/no]"
- "Changes requested: [list or 'none']"
</phase_approve>

<phase_generate>
### Phase 5: Generate Excel Import File

**REQUIRED:** Use the Python script to generate the Excel file. Do not attempt to write Excel/CSV directly.

**Note:** The script requires openpyxl. Install with: `pip install openpyxl`

```bash
python3 scripts/build_teamwork_xlsx.py [audit-file.md] --output [project-name]-teamwork-import.xlsx
```

The script:
- Parses the audit markdown file
- Handles Excel formatting correctly
- Generates proper column structure for Teamwork import
- Manages subtask relationships (dash prefix convention)

**Excel columns (Teamwork format):**
| Column | Description |
|--------|-------------|
| TASKLIST | Task list name (only on first row of list) |
| TASK | Task or subtask name (subtasks prefixed with `-`) |
| DESCRIPTION | Task list or task description |
| ASSIGN TO | **Email address** (must match Teamwork user) |
| START DATE | Start date (if specified) |
| DUE DATE | Due date (if specified) |
| PRIORITY | High, Medium, Low (if specified) |
| ESTIMATED TIME | Time estimate in Teamwork format (30m, 2hr) |
| TAGS | Comma-separated tags |
| STATUS | Active, Completed (default: Active) |

**GATE:** After generation, write:
- "Excel file saved to: [path]"
- "Ready for Teamwork import"
</phase_generate>

<phase_template>
### Phase 6: Optional Template Generation

If user requested a template version:

1. Copy the audit document
2. Replace specific names with placeholders:
   - Client/project names → `[Client Name]`, `[Project Name]`
   - Specific dates → Remove entirely
   - Specific deliverables → Generalize to category
3. Save as `[project-type]-template.md`

This creates a reusable structure for similar future projects.
</phase_template>

## Examples

### Input: Book Campaign Planning Document

**Source excerpt:**
> "The book launch needs editorial review by the end of March. Sarah will handle copyediting. Design team (Mike) creates the cover. Marketing prepares social posts."

**Audit output:**
```markdown
### Editorial
Description: Editorial processes for book content

#### Copyediting Review
- Assignee: sarah@publisher.com
- Due date: [end of March - exact date from source]
- Estimated time: Not specified

(No subtasks - copyediting is one continuous activity)

### Design
Description: Visual and layout production

#### Cover Design
- Assignee: mike@publisher.com
- Due date: Not specified
- Estimated time: Not specified

(No subtasks - single deliverable)

### Marketing
Description: Promotional activities

#### Social Media Preparation
- Assignee: marketing@publisher.com
- Due date: Not specified
- Estimated time: Not specified

(No subtasks - source doesn't specify breakdown)

## Validation Checklist
- [x] All dates come from source materials (only "end of March" was specified)
- [x] All time estimates come from source materials (none specified)
- [x] No task lists organized by timeline (organized by area: Editorial, Design, Marketing)
- [x] All subtasks meet minimum time threshold (no subtasks created)
- [x] Assignments limited to 1-2 people per task
- [x] Task names derived from source content
- [x] No single subtasks
- [x] ASSIGN TO uses email addresses
- [x] Dependencies ordered correctly within each task list
```

Note: Only the March deadline appears because it was in the source. Other dates left empty. Tasks without natural subdivisions have no subtasks.

### Input: Project with Time Estimates

**Source excerpt:**
> "Website redesign: Research phase (2 hours), wireframes (4 hours), design mockups (8 hours). Developer implements over 2 weeks."

**Audit output:**
```markdown
### Design
#### Website Redesign - Design Phase
- Assignee: designer@company.com
- Estimated time: 14hr total

##### Subtasks:
- [ ] Research and competitive analysis (2hr)
- [ ] Wireframe creation (4hr)
- [ ] Design mockups (8hr)

### Development
#### Website Implementation
- Assignee: developer@company.com
- Due date: Not specified
- Estimated time: Not specified

(No subtasks - source says "implements" but doesn't break down the work)

Note: "2 weeks" is duration, not a time estimate. Left empty.

## Validation Checklist
- [x] All dates come from source materials (none specified)
- [x] All time estimates come from source materials (2hr, 4hr, 8hr for design)
- [x] No task lists organized by timeline (organized by area: Design, Development)
- [x] All subtasks meet minimum time threshold (smallest is 2hr)
- [x] Assignments limited to 1-2 people per task
- [x] Task names derived from source content
- [x] No single subtasks (Design has 3, Development has 0)
- [x] ASSIGN TO uses email addresses
- [x] Dependencies ordered correctly within each task list
```

<failed_attempts>
## What DOESN'T Work

- **Estimating dates:** "This should take about a week" is NOT a due date. Only explicit dates count.

- **Timeline-based task lists:** Creating lists like "Week 1", "Phase 1", "Sprint 1" mixes concerns and makes ongoing work hard to manage.

- **Granular subtasks:** "Send email" and "Update spreadsheet" are too small. Combine into "Complete administrative updates (30m)".

- **Direct CSV/Excel generation:** LLMs mess up quoting and formatting. Always use the script.

- **Mixed assignments:** A task where subtask 1 goes to Alice and subtask 2 goes to Bob creates confusion. Split into separate tasks.

- **Forced subtasks:** Do NOT artificially split single deliverables to create multiple subtasks. "Write homepage copy" should be one task, not "Draft homepage copy" + "Revise homepage copy." If a task is one piece of work, leave it as a task without subtasks.
</failed_attempts>

## File Reference

| File | Purpose |
|------|---------|
| [references/TEAMWORK-FORMAT.md](references/TEAMWORK-FORMAT.md) | Detailed Teamwork import format specification |
| [scripts/build_teamwork_xlsx.py](scripts/build_teamwork_xlsx.py) | Excel file generator |
