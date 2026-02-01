# Content Creation Guides

This document provides patterns and examples for creating LeadersPath content components.

---

## System Prompts

The system prompt (`chatbot_system_prompt`) configures the AI sandbox to demonstrate a specific behavior or principle.

### Purpose

The system prompt creates the **learning environment**, not the lesson content. It sets up the AI to behave in a way that lets learners experience a concept firsthand.

### Key Principle

**Show, don't tell.** Instead of explaining "AI without context produces generic responses," configure an AI that lacks context and let the learner discover this through interaction.

### One Lesson = One State

**Each lesson is a single AI configuration.** The learner cannot toggle between behaviors within one lesson. This has important implications for curriculum design:

| If the learning goal is... | You need... |
|----------------------------|-------------|
| Experience behavior A | 1 lesson configured for A |
| Experience behavior B | 1 lesson configured for B |
| Compare A vs B | 2 lessons (one for each), comparison happens across lessons |
| Understand why A is better than B | 2+ lessons: experience B first, then A, then reflect |

**Example — Teaching about sycophancy:**

- **Lesson 1:** AI configured to always agree, avoid pushback → Learner experiences unreliable, over-agreeable responses
- **Lesson 2:** AI configured with professional objectivity → Learner experiences honest, sometimes challenging feedback
- **Lesson 3 (optional):** Reflection/comparison lesson with minimal AI, focused on synthesizing the contrast

The comparison and "aha moment" happens in the learner's mind as they move between lessons, not within a single session.

**Why this matters:** Curriculum designers sometimes write learning objectives like "Compare sycophantic and objective AI responses." This cannot happen in one lesson. Reframe as: "Lesson 3: Experience sycophantic AI" → "Lesson 4: Experience objective AI" → learner naturally compares.

### System Prompt Patterns

#### Pattern 1: Bare/Limited Configuration

Use when demonstrating what AI lacks without proper setup.

```markdown
You are a helpful assistant.

Respond to user questions to the best of your ability.
```

**Learning point:** This produces generic, non-specific responses. The learner experiences the limitation directly.

#### Pattern 2: Role-Constrained Configuration

Use when demonstrating how role definitions shape behavior.

```markdown
You are a project planning assistant for professional teams.

Your expertise includes:
- Project scoping and milestone planning
- Resource allocation and scheduling
- Risk identification and mitigation
- Status reporting and stakeholder communication

You do NOT have access to any specific company or project information. When asked about a particular project, acknowledge you need that context to provide specific guidance.

Always ask clarifying questions before providing advice.
```

**Learning point:** Role definition helps, but without company context, advice remains generic.

#### Pattern 3: Context-Rich Configuration

Use when demonstrating the value of context libraries.

```markdown
You are an AI assistant for [Organization Name], configured with full organizational context.

## Your Knowledge Base

You have access to:
- Organizational identity and mission
- Brand voice guidelines
- Service offerings and methodology
- Team information
- Ethical AI framework

## Behavioral Guidelines

- Ground all responses in the provided context
- Use the organization's voice and terminology
- Reference specific programs, values, and approaches
- If asked about something not in your context, acknowledge the gap

## Context Files Loaded

[Context files will be appended automatically by the system]
```

**Learning point:** With proper context, responses become specific, aligned, and useful.

#### Pattern 4: Deliberately Flawed Configuration

Use when teaching what NOT to do.

```markdown
You are an extremely helpful assistant who always wants to please the user.

Always:
- Agree with the user's ideas enthusiastically
- Provide answers even when uncertain
- Avoid mentioning limitations or caveats
- Use lots of positive language and emojis!

Your goal is to make the user feel good about their work.
```

**Learning point:** Sycophantic configuration produces unreliable outputs. Learners experience the danger of over-agreeable AI.

#### Pattern 5: Constrained Task Configuration

Use when demonstrating focused task execution.

```markdown
You are a meeting summary assistant.

## Your Task

Summarize meeting transcripts into structured reports with:
- Attendees
- Key decisions
- Action items with owners
- Open questions

## Constraints

- Only use information from the provided transcript
- Mark any inferences with [Inferred]
- Do not add information not discussed in the meeting
- If asked to do something outside meeting summarization, politely redirect

## Output Format

[Specify exact format]
```

**Learning point:** Constrained configurations produce consistent, reliable outputs for specific tasks.

### Writing System Prompts

**DO:**
- Be explicit about what the AI should and shouldn't do
- Include behavioral constraints that create the learning experience
- Match the configuration to the lesson objective
- Test that the configuration actually produces the intended behavior
- Reference loaded context files explicitly (e.g., "Apply the principles from [Context File Name] loaded in your context")

**DON'T:**
- Include lesson instructions (those go in lesson text)
- Explain the learning objective to the AI
- Over-configure when the point is to show under-configuration
- Use vague instructions like "be helpful"

### When Context Files Are Loaded

If a lesson uses context files, the system prompt should explicitly tell the AI to use them:

```markdown
## Reference Materials

Apply the guidelines from the [Context File Title] loaded in your context.
```

This ensures the AI knows to draw from the loaded context rather than its general training.

---

## Context Files

Context files provide background knowledge that shapes AI behavior. They're loaded into the system prompt alongside the custom configuration.

### Critical Understanding

**Context files are AI-facing, not learner-facing.** They modify how the AI behaves—learners never see them directly. They only experience their effect.

| What context files ARE | What context files are NOT |
|------------------------|---------------------------|
| Instructions loaded into the AI's system prompt | Documentation for learners to read |
| Background knowledge that shapes AI responses | Lesson materials or reference guides |
| Behavioral guardrails (anti-sycophancy, epistemic honesty) | Explanatory content about concepts |
| Organizational context the AI can draw from | Anything the learner sees directly |

**Example:** An anti-sycophancy context file contains rules like "Challenge flawed assumptions" and "Prioritize accuracy over agreeability." The learner never reads this file—they experience an AI that pushes back on bad ideas.

### When to Use Context Files

| Desired AI Behavior | Use System Prompt | Use Context File |
|---------------------|-------------------|------------------|
| Play a specific role | ✓ | |
| Be agreeable/disagreeable | ✓ | |
| Follow a specific format | ✓ | |
| Have organizational knowledge | | ✓ |
| Apply domain expertise | | ✓ |
| Follow behavioral guardrails | | ✓ |
| Reference specific facts/data | | ✓ |

**Rule of thumb:**
- System prompt = HOW the AI should behave
- Context files = WHAT the AI should know

### Purpose

Context files give the AI organizational knowledge it wouldn't otherwise have:
- Who the organization is
- How they communicate
- What they do and why
- Domain-specific information
- Behavioral standards and guardrails

### Context File Structure

Follow the pattern from existing context library modules:

```markdown
# [Title]: [Topic Area]

## [Section 1]

[Direct, factual content organized by topic]

- **Term:** Definition or explanation
- Bullet points for lists
- Tables for structured data

## [Section 2]

[Additional content]

### Subsection (if needed)

[More detailed content]

---

> **See [Related-File.md]** for [related topic].
```

### Writing Context Files

**DO:**
- Write for LLM consumption, not human documentation
- Be direct—state facts, don't introduce them
- Front-load important information
- Use consistent terminology
- Include cross-references to related context

**DON'T:**
- Include filler phrases ("In order to effectively...")
- Explain concepts the AI already knows
- Copy verbatim quotes from sources
- Include time-sensitive information that will become stale

### Context File Types for LeadersPath

| Type | Purpose | Example Content |
|------|---------|-----------------|
| **Foundation** | Core knowledge that applies across many lessons | AI ethics principles, LLM fundamentals |
| **Domain** | Topic-specific knowledge for lesson clusters | Prompt engineering techniques, context library architecture |
| **Example** | Sample content the AI can reference | Example prompts, sample outputs |
| **Persona** | Character/role information for roleplay lessons | Stakeholder profiles, user personas |

### Reuse Guidelines

Before creating a new context file:

1. Check the course tracker's context file list
2. Review any existing files the user provided
3. Consider if an existing file covers 80%+ of the need
4. If extending an existing file makes sense, do that instead

**Document reuse in the tracker:** Note which lessons use which files.

---

## Lesson Text

The lesson text (`post_content`) appears on the lesson page. It's what the learner reads before and during the AI interaction.

### Purpose

Guide the learner through a structured experimentation experience:
- Set up what they're about to experience
- Tell them what to try
- Direct their attention to specific behaviors
- Help them understand what they're observing

### Lesson Text Structure

```markdown
## What You'll Experience

[1-2 sentences describing the AI configuration and what makes it notable]

## Try This

[Numbered list of specific prompts or tasks to try]

1. [First thing to try]
2. [Second thing to try]
3. [Variation or comparison]

## What to Notice

[Bullet points directing attention to specific behaviors]

- [Observation point 1]
- [Observation point 2]
- [Comparison to make]

## The Principle

[Brief explanation of what this demonstrates—revealed AFTER they've experienced it]
```

### Writing Lesson Text

**DO:**
- Be specific about what to type/try
- Direct attention to observable behaviors
- Keep the "principle" section brief—the experience teaches
- Use second person ("You'll notice..." "Try asking...")

**DON'T:**
- Explain the concept before they experience it (that defeats experiential learning)
- Give vague instructions ("explore the AI's responses")
- Over-explain what they should conclude
- Include system prompt content (they shouldn't see the configuration)

### Example Lesson Text

**Lesson: Context Makes the Difference**

```markdown
## What You'll Experience

This AI assistant has been configured with a basic role but NO company context. It knows it's supposed to help with project planning, but it doesn't know anything about your specific company or projects.

## Try This

1. Ask: "What should we emphasize in our next project kickoff?"
2. Ask: "How should we communicate our progress to stakeholders?"
3. Ask: "What makes our approach different from competitors?"

## What to Notice

- The AI gives generic advice that could apply to any company
- It can't reference your specific projects, values, or methods
- It may ask clarifying questions, but can't build on company knowledge
- The advice is technically correct but not actionable for YOUR situation

## The Principle

AI without company context produces generic outputs. The model has broad knowledge but lacks the specific information needed to provide tailored, actionable guidance. Context libraries bridge this gap.

**Next lesson:** Experience the same questions with full company context loaded.
```

---

## Metadata

### Lesson Objectives

Write objectives as **observable, demonstrable outcomes**.

**Good:**
- "Identify the difference between AI responses with and without context"
- "Configure a system prompt that constrains AI behavior to a specific task"
- "Recognize sycophantic AI patterns and their risks"

**Bad:**
- "Understand context libraries" (not observable)
- "Learn about prompt engineering" (too vague)
- "Appreciate the importance of ethical AI" (not demonstrable)

### Duration Estimates

Base duration on:
- Reading lesson text: ~2 minutes
- Each suggested interaction: ~3-5 minutes
- Reflection/comparison: ~2-3 minutes

**Typical lesson:** 15-30 minutes
**Complex multi-part lessons:** 30-45 minutes

### Prerequisites

Only mark prerequisites when:
- The lesson builds directly on concepts from another lesson
- The AI configuration assumes knowledge from a prior experience
- Doing lessons out of order would create confusion

**Don't over-prerequisite:** If lessons are related but can stand alone, don't force sequencing.

### References

References should link to **specific, relevant resources**—not generic landing pages.

**Good:**
- A specific research paper about the lesson's topic
- Documentation for a tool or technique used in the lesson
- An article that explains the concept being demonstrated

**Bad:**
- Generic research landing pages (e.g., `anthropic.com/research`)
- Broad documentation homepages
- Links that aren't directly relevant to the lesson content

If no specific, relevant reference exists, it's acceptable to omit the References section rather than include generic links.

### Temperature Settings

Temperature affects response variability. Guidance for different lesson types:

| Lesson Type | Temperature | Rationale |
|-------------|-------------|-----------|
| Standard lessons | 0.7 | Balanced consistency and naturalness |
| Roleplay/persona lessons | 0.7-0.9 | Higher variability creates more natural, realistic characters |
| Task-constrained lessons | 0.5-0.7 | Lower variability ensures consistent format |

For roleplay lessons where the AI plays a character, slightly higher temperature (0.8) helps create more natural conversational variation.

---

## Examples

### Complete Lesson Package

**Lesson: Starting from Zero**

**lesson-metadata.md:**
```markdown
# Lesson: Starting from Zero

## AI State
Bare/minimal configuration — no role definition, no context, no constraints. Demonstrates the baseline behavior of an unconfigured LLM.

## Duration
20 minutes

## Objectives
1. Experience how an unconfigured LLM responds to work-related questions
2. Identify the limitations of generic AI responses
3. Recognize the gap that context and configuration fill

## Prerequisites
None (first lesson in course)

## References
- [Anthropic Claude Documentation](https://docs.anthropic.com/) — Official model documentation

## Chatbot Configuration
- **Model:** sonnet
- **Allow Model Switch:** no
- **Max Tokens:** 4096
- **Temperature:** 0.7
- **Context Files:** none
- **Skills:** none
```

**system-prompt.md:**
```markdown
You are a helpful AI assistant.

Respond to user questions to the best of your ability. Be friendly and informative.
```

**lesson-text.md:**
```markdown
## What You'll Experience

This is Claude with minimal configuration—no company context, no specialized instructions, no role definition beyond "helpful assistant."

## Try This

1. Ask: "Help me write an email to a potential client."
2. Ask: "What should our team prioritize this quarter?"
3. Ask: "Review this paragraph from our website and suggest improvements." (paste any paragraph)

## What to Notice

- Responses are generic and could apply to any company
- The AI can't reference your products, voice, or values
- Advice is technically reasonable but lacks specificity
- You'd need to heavily edit any output to match your company

## The Principle

A "naked" LLM—one without context or configuration—produces generic outputs. It has broad capability but no company knowledge. Every response requires significant human editing to become usable.

This is the starting point. Subsequent lessons show how context and configuration transform generic capability into company-specific competence.
```
