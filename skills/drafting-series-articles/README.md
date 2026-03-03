# Drafting Series Articles

Drafts research-grounded long-form articles within a multi-article series, using a multi-session workflow that survives context window limits.

## When to Use

Use this skill when you need to:
- Draft a specific article within a research-backed series
- Resume work on an in-progress article draft
- Write long-form content that requires deep comprehension of research evidence

## How to Invoke

Say things like:
- "Draft Article 3"
- "Let's work on the healthcare article"
- "Resume drafting where we left off"

## What You'll Need

- A project CLAUDE.md referencing: series outline, audience document, thesis/framework document, research index, research documents, and voice profile
- Context library modules loaded (behavioral standards, natural prose standards)
- A `Drafts/` directory for output

## What You'll Get

Across multiple sessions, the skill produces:
- **Article plan** (`Drafts/article-[N]-plan.md`) — orientation, comprehension findings, phase tracking
- **Draft** (`Drafts/[number]-[title]-draft-[date].md`) — the article with YAML metadata
- **Process log** (`Drafts/article-[N]-process-log.md`) — reasoning trace, editorial notes, self-corrections

## How It Works

The skill runs in four sessions:

| Session | What Happens |
|---------|-------------|
| A: Bootstrap + Orient | Load context, find the story, determine structure |
| B: Comprehend | Think through evidence, find connections and narrative |
| C: Draft | Write the article section by section |
| D: Editorial + Quality | Multi-round revision, quality checks, presentation |

Each session produces durable artifacts that the next session reads cold. The boundary between Comprehend and Draft is mandatory — drafting needs voice profile instructions fresh in context.

## Tips

- The skill stops for user input after every phase — confirm or redirect before it proceeds
- Sessions A and B can combine if context permits; the break before C is mandatory
- The process log is a first-class deliverable, not a debugging artifact — review it alongside the draft
- If the skill is loaded without context library modules, it will note the dependency gap
