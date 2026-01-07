---
name: generating-meeting-reports
description: Generates structured meeting reports from transcripts. Extracts attendees, topics, decisions, action items, and resources into a standardized executive summary format. Use when user says create meeting report, generate meeting minutes, summarize this meeting, turn transcript into report, or document this meeting. Activates when transcript content is present via pasted text, inline content, attached file, or uploaded document, even when accompanied by additional context files or reference materials.
---

# Generating Meeting Reports

Creates professional, actionable meeting reports from raw transcripts.

## Quick Start

Given a meeting transcript, generate a report:

1. Read the transcript
2. Extract meeting metadata, attendees, topics, decisions, and action items
3. Generate report following the structure in [references/REPORT-FORMAT.md](references/REPORT-FORMAT.md)
4. **Save the report to a file** (see Output Requirements below)

## Output Requirements

**ALWAYS save the report to a file. Do not output the report inline in chat.**

1. Generate a filename: `meeting-report-YYYY-MM-DD.md` (use the meeting date)
2. Write the complete report to this file
3. After saving, confirm to the user: "Report saved to `[filename]`" with a brief summary of key findings

If the meeting date is unknown, use the current date or ask the user.

## Workflow

```
Progress:
- [ ] Step 1: Analyze transcript
- [ ] Step 2: Extract structured data
- [ ] Step 3: Generate report
- [ ] Step 4: Review for completeness
```

### Step 1: Analyze Transcript

Identify from the transcript:
- Meeting date, time, and duration
- Meeting type/purpose
- Participants and their roles (infer from context if not explicit)
- Major discussion topics
- Decisions made
- Action items mentioned (look for "action item", "I'll do", "need to", etc.)
- Resources, tools, or documents referenced
- Follow-up items and open questions

### Step 2: Extract Structured Data

For each action item, capture:
- Specific task description
- Owner (who is responsible)
- Due date (if mentioned)
- Priority (if indicated)
- Dependencies (if any)

For each topic:
- Background/context
- Key points discussed
- Decisions made
- Implementation details

### Step 3: Generate Report

**ALWAYS use the exact format defined in [references/REPORT-FORMAT.md](references/REPORT-FORMAT.md).** Do not deviate from this structure.

Requirements:
- Executive summary: 2-3 paragraphs covering purpose, key decisions, and critical next steps
- All action items formatted as checkboxes with owner and details
- Resources section with any tools, links, or documents mentioned
- Notes section for follow-ups, open questions, and future considerations

**Write the report to a file, not inline.**

### Step 4: Review and Save

Before saving:
- All key information captured
- Action items are clear and assigned
- Professional tone maintained
- Format matches the template exactly

Then save to `meeting-report-YYYY-MM-DD.md` and confirm to the user.

## Handling Challenges

**Informal or fragmented transcripts:**
- Infer structure from conversational flow
- Group related discussions into coherent topics
- Extract implicit action items from commitments ("I'll look into that")

**Missing information:**
- Use "[Not specified]" for unknown dates/times
- Infer roles from context when not explicitly stated
- Note assumptions in the report if significant

**Multiple speakers with same name:**
- Distinguish by role if possible
- Note ambiguity if unavoidable

## Examples

### Input: Transcript Fragment

```
[Sarah Chen]
Okay so for the website redesign, I talked to the design team and they can start next week.

[Mike Torres]
Great. What's the timeline looking like?

[Sarah Chen]
They're saying 3 weeks for mockups. I'll send you the project brief by Friday.

[Mike Torres]
Perfect. Action item for me - I need to get the brand guidelines doc to Sarah before she briefs the team.
```

### Output: Extracted Report Section

**Discussion Topic:**
```markdown
### Website Redesign

- **Background/Context:** Planning phase for website redesign project
- **Key Points Discussed:**
  - Design team available to start next week
  - Timeline: 3 weeks for mockups
- **Decisions Made:** Proceed with design team engagement
- **Implementation Details:** Project brief to be shared Friday
```

**Action Items:**
```markdown
- [ ] Send project brief to Mike
   * Owner: Sarah Chen
   * Due: Friday
   * Priority: High

- [ ] Share brand guidelines doc with Sarah
   * Owner: Mike Torres
   * Due: Before Friday
   * Dependencies: Needed before design team briefing
```

## Resources

- [references/REPORT-FORMAT.md](references/REPORT-FORMAT.md) - Complete report template and structure
