---
name: writing-case-studies
description: Guides users through creating comprehensive case studies from interview transcripts, notes, or outlines. Produces the case study plus all supporting assets (social posts, platform versions, metadata). Use when user says write a case study, create a case study, build a case study, develop a case study, case study from interview, or case study from transcript. Activates when source content is present via pasted text, attached file, or uploaded document, even when accompanied by context files or style guides.
---

# Writing Case Studies

Case studies are **teaching documents** that show readers how to solve problems. The subject is a running illustration, not the protagonist.

## The Fundamental Shift

**Wrong mindset:** "What happened in this project that we can report?"
**Right mindset:** "What techniques can we teach readers, using this project as proof?"

A case study is not a report of what happened. It's a teaching document that happens to use a real example.

## Before You Start

### 1. Confirm Output Directory

Ask: "Where should I save case study files? Default is `./tmp/` in your current directory."

**STOP. Wait for confirmation before proceeding.**

### 2. Read EVERY Provided File

You must read all files the user provides. No skipping. No assumptions.

- Context library → Read index AND every referenced module
- Style guide → Read completely
- Background files → Read each one
- Transcript → Read entirely

**If you skip files, you will hallucinate. You will miss critical context. You will write content that contradicts provided information.**

## Phase 1: Identify Reader Questions

**Do not start by analyzing what happened. Start by identifying what readers need to learn.**

Ask yourself:

1. Who will read this case study?
2. What problem keeps them up at night?
3. What questions do they have about solving that problem?
4. What techniques would help them if they knew about them?

Write 3-5 specific questions readers have. These become the backbone of the case study.

**Example questions (nonprofit leader reading about campaign management):**
- "How do I run a multi-channel campaign when I have a tiny team?"
- "What do I do when a campaign isn't working mid-stream?"
- "Can AI actually help, or is it just hype?"

**Ask the user:** "Here are the reader questions I identified: [list]. Are these the right questions? What's missing?"

## Phase 2: Extract Techniques from Source

Now read the source content looking for **techniques you can teach** that answer the reader questions.

For each reader question, find:
- **The technique** - What specific method/approach solves this?
- **The proof** - What evidence shows it works?
- **The quote** - What captures the insight?

### Teaching vs. Reporting

**Reporting (wrong):** "The team used a multi-phase approach and built assets in one week."

**Teaching (right):** "Break your campaign design into phases: planning, scheduling, then asset creation. Each phase feeds the next. Here's how one team applied this..."

The difference: Teaching tells readers **how to do it themselves**. Reporting just describes what someone else did.

### Critical Judgment Calls

**Before including ANY information, ask:**

1. **Does this teach a technique the reader can use?** If no, cut it.
2. **Would this embarrass the subject?** If yes, anonymize or cut it.
3. **Is this internal/operational?** Processing fees, platform migrations, org restructuring → cut it.
4. **Can the reader act on this?** If no, cut it.

### Protecting the Subject

The case study subject trusted you with their story. Do not:
- Expose financial difficulties
- Reveal organizational dysfunction
- Include metrics that make them look bad
- Name them if anonymity serves them better
- Include dollar amounts without permission (use percentages instead)

**Default to anonymization** ("a global environmental nonprofit") unless there's a clear reason to name them AND they benefit from being named.

## Phase 3: Plan the Structure

Structure the case study as a **teaching document with a through-line**.

### The Through-Line

Identify the reader's transformation:
- **From:** [Starting state - overwhelmed, stuck, skeptical]
- **To:** [Ending state - confident, equipped, enabled]

Each section should move the reader along this journey.

### The Pattern for Each Section

Each section teaches a technique, with the subject as illustration:

```
## [Technique as Header - what reader will learn]

[Speak directly to reader's problem - "You face X..."]

[Teach the technique - "Here's how to approach this..."]

[Illustrate with the example - "One team applied this by..."]

[Quote that captures the insight]
```

### What NOT to Do

Do not write:
- "The Challenge: [Subject] faced..."
- "Background: [Subject] is a..."
- "[Subject] needed to..."

The subject appears only as illustration after you've taught the technique.

### Full Structure

```
# [Title that speaks to reader pain]

## [Technique 1 - addresses first reader question]
[Reader's problem → Technique → Illustration from example → Quote]

## [Technique 2 - addresses second reader question]
[Reader's problem → Technique → Illustration from example → Quote]

## [Technique 3 - addresses third reader question]
[Reader's problem → Technique → Illustration from example → Quote]

## What This Produces
[Results - proof the techniques work]

## Get Started
[Concrete next steps - specific tools, resources, actions]
```

### Planning Questions

Before finalizing the plan, verify:
- Does every section teach a specific technique?
- Does every section open with the reader's problem?
- Does the subject appear only as illustration (not protagonist)?
- Is there a clear through-line (reader transformation)?
- Does "Get Started" give readers something new and actionable?

**STOP. Get approval before drafting.**

## Phase 4: Write the Draft

### Rule 1: Teach, Don't Report

Every section must teach something the reader can do. If you're just describing what happened, rewrite.

**Test:** Could the reader implement this technique based on what you wrote?

### Rule 2: Follow the Approved Plan

The plan was approved. Execute it. Do not:
- Invent a different structure
- Add sections not in the plan
- Skip sections that are in the plan
- Change the techniques you committed to teaching

### Rule 3: Quotes Are Verbatim

**Never alter quotes.** This is an integrity issue.

- Copy quotes exactly from source material
- Use [...] for omissions
- If you must paraphrase, clearly mark it: "The team lead explained that..." (not in quotation marks)
- Attribute quotes to named speakers when possible

### Rule 4: Follow Provided Style Guidelines

If the user provided a context library with writing guidelines—**follow them exactly.** Your instincts about "good writing" do not override explicit instructions.

Watch for:
- Banned words or phrases
- Voice and tone requirements
- Attribution requirements
- Confidentiality rules (e.g., no dollar amounts)

### Rule 5: Substantive Paragraphs

Case studies are documentation, not social media content.

- No single-sentence paragraphs for dramatic effect
- Each paragraph should contain multiple related points
- Information density over style
- Professional tone, not punchy engagement-bait

### What to NEVER Include

- Platform migrations, tool changes
- Processing fees, administrative costs
- Attribution tracking implementation
- Organizational politics or restructuring
- Metrics that don't prove the techniques work
- Details that could embarrass the subject
- Generic advice readers could figure out themselves

### The "Get Started" Section

This section must give readers something **new and actionable**—not platitudes.

**Bad:** "Start by defining your goals and understanding your audience."
**Good:** "Download the context-library skill and run it on your organization's strategic plan. Upload the output to a Claude Project."

Reference specific tools, resources, or techniques by name.

## Phase 5: Review

Present the draft summary and ask:

1. Does each section teach a technique (not just report what happened)?
2. Is the subject protected?
3. Does "Get Started" give readers something new?
4. Would you share this with the audience?

**Make edits until approved.**

## Phase 6: Generate Assets

Only after draft approval.

**Create in the output directory:**

`versions/`
- `blog-post.md` - Full version
- `linkedin-article.md` - Condensed
- `email-version.md` - 200-300 word teaser

`social/`
- `linkedin-posts.md` - 3 posts (one per technique taught)
- `twitter-posts.md` - 3-5 posts
- `pull-quotes.md` - 3-5 quotes with attribution

`metadata.md` - Audience, keywords, imagery

`index.md` - Summary and file list

## Quick Reference: The Questions

**Phase 1 - Reader Questions:**
- Who reads this?
- What problem do they have?
- What techniques would help them?

**Phase 2 - Extraction Filters:**
- Does this teach a technique the reader can use?
- Would this embarrass the subject?
- Is this internal/operational?
- Can the reader act on this?

**Phase 3 - Structure Check:**
- Does every section teach a specific technique?
- Does every section open with the reader's problem?
- Is there a through-line (reader transformation)?
- Does the subject appear only as illustration?

**Phase 4 - Drafting Rules:**
- Am I teaching or just reporting?
- Are quotes verbatim and attributed?
- Am I following provided style guidelines?
- Does "Get Started" give something new and actionable?

**Phase 5 - Final Check:**
- Would you share this with the target audience?
- Does this teach readers something they didn't know?
