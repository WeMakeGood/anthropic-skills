# Drafting Articles

Drafts research-grounded long-form articles using a multi-session workflow that survives context window limits. Works for both series articles and standalone pieces.

## When to Use

Use this skill when you need to:
- Draft an article from research documents
- Resume work on an in-progress article draft
- Write long-form content that requires deep comprehension of research evidence
- Draft a specific article within a multi-article series

## How to Invoke

Say things like:
- "Draft Article 3"
- "Draft an article from this research"
- "Let's work on the healthcare article"
- "Resume drafting where we left off"

## What You'll Need

- A **project manifest** (`project-manifest.md`) pointing to: voice profile, writing standards, audience document, research documents, and drafts directory. The manifest is produced by the `designing-article-series` skill, or can be created manually.
- If no manifest exists, the skill asks for the minimum: research files, voice profile path, audience description, and output directory.

## Related Skills

| Skill | Relationship |
|-------|-------------|
| **designing-article-series** | Produces the project manifest and series architecture this skill reads |
| **extracting-voice-profiles** | Produces voice profiles this skill loads at Draft time |
| **generating-writing-standards** | Produces writing standards modules this skill loads at Draft time |

## What You'll Get

Across multiple sessions, the skill produces:
- **Article plan** (`Drafts/article-[N]-plan.md`) — orientation, comprehension findings, structural plan, phase tracking
- **Draft** (`Drafts/[number]-[title]-draft-[date].md`) — the article with YAML metadata
- **Process log** (`Drafts/article-[N]-process-log.md`) — reasoning trace, editorial notes, self-corrections

## How It Works

The skill runs in four sessions:

| Session | What Happens |
|---------|-------------|
| A: Orient | Read manifest, load research, find the story, determine structure |
| B: Comprehend | Think through evidence, find connections, build structural plan |
| C: Draft | Load voice + writing standards, write the article section by section |
| D: Editorial + Quality | Multi-round revision, quality checks, presentation |

Each session produces durable artifacts that the next session reads cold. The boundary between Comprehend and Draft is mandatory — drafting needs voice profile and writing standards fresh in context.

**Key design decision:** Voice profile and writing standards load at Draft time (Session C), not at bootstrap. Orient and Comprehend are analytical phases that need context space for research, not for voice instructions.

## Tips

- The skill stops for user input after every phase — confirm or redirect before it proceeds
- Sessions A and B can combine if context permits; the break before C is mandatory
- The process log is a first-class deliverable, not a debugging artifact — review it alongside the draft
- Writing standards baselines are available in `references/baselines/` — specify `baseline:[name]` in the manifest
