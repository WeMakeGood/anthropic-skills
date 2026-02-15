# Build State

<!--
This file tracks progress across sessions. Read this FIRST when resuming a build.
It tells you: what phase you're in, what's done, what's next, and what to read.
-->

**Library:** [Library Name]
**Source path:** [SOURCE_PATH]
**Output path:** [OUTPUT_PATH]
**Agents:** [list of target agents]
**Last updated:** YYYY-MM-DD

---

## Current Phase

**Phase:** [1 - Index | 2 - Synthesize | 3 - Analyze | 4 - Propose | 5 - Build | 6 - Agents | 7 - Validate]

**Read this phase file next:** `references/phases/[PHASE_FILE].md`

---

## Phase Completion Status

| Phase | Status | Notes |
|-------|--------|-------|
| 1 - Index | pending | |
| 2 - Synthesize | pending | |
| 3 - Analyze | pending | |
| 4 - Propose | pending | |
| 5 - Build | pending | |
| 6 - Agents | pending | |
| 7 - Validate | pending | |

Status values: `pending`, `in-progress`, `complete (pending approval)`, `complete`

---

## Module Build Checklist (Phase 5)

<!-- Populated after proposal approval. Track each module individually. -->

### Foundation
- [ ] F_agent_behavioral_standards — copied from templates
- [ ] S_natural_prose_standards — copied from templates
- [ ] F1_[name] — [status]

### Shared
- [ ] S1_[name] — [status]

### Specialized
- [ ] D1_[name] — [status]

### Addenda
- [ ] A1_[name] — [status]

---

## Agent Definition Checklist (Phase 6)

- [ ] [agent-name] — [status]

---

## User Decisions Log

<!-- Record decisions made during the build so they're not lost across sessions. -->

### Conflicts Resolved
- [Conflict]: [User's decision] (Phase [N])

### Gaps Accepted
- [Gap]: [User's decision — proceed without, or defer] (Phase [N])

### Scope Changes
- [Change]: [What was added/removed and why] (Phase [N])

---

## Session History

<!-- Optional: track when sessions start/end for debugging. -->

| Session | Date | Phases Covered | Notes |
|---------|------|----------------|-------|
| 1 | YYYY-MM-DD | 1-2 | |
