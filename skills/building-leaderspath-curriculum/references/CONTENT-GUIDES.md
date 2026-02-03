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

## API Settings

The `api-settings.md` file documents the technical configuration for the lesson's AI sandbox.

### Purpose

Provide clear documentation of:
- Model selection and parameters
- Context files loaded
- Skills enabled
- Configuration rationale

### API Settings Structure

```markdown
# API Settings

## Model Configuration
- **Model:** [sonnet / haiku / opus-4.5]
- **Model String:** [claude-sonnet-4-5-20250929 / claude-haiku-4-5-20251001 / claude-opus-4-5-20251101]
- **Max Tokens:** [number, 256-16384]
- **Temperature:** [0-1]
- **Allow Model Switch:** [yes/no]

## Context Files
- [path/filename.md] — [brief description of what this context provides]

## Skills
- [skill-name] — [what this skill enables]

## Configuration Notes
[Any specific choices and their rationale]
```

### Writing API Settings

**DO:**
- Include the full model string for technical accuracy
- Explain why specific parameter values were chosen
- List all context files with brief descriptions
- Note any special configuration considerations

**DON'T:**
- Use default values without considering lesson needs
- Omit context files that are loaded
- Leave the Configuration Notes empty for non-standard settings

---

## Model Selection Rationale

The `model-selection.md` file explains why a particular model was chosen for the lesson.

### Purpose

Document the reasoning behind model choice so that:
- Curriculum team understands trade-offs
- Future updates can make informed decisions
- Learners understand what they're experiencing (via transparency principle)

### Model Selection Structure

```markdown
# Model Selection Rationale

## Why [Model Name]

[Explanation of why this specific model was chosen]

## Capabilities Demonstrated
- [Capability 1]
- [Capability 2]

## Trade-offs Considered
- [Trade-off 1]
- [Trade-off 2]

## Alternative Considerations
[Why other models were not chosen, if relevant]
```

### Model Guidelines

| Lesson Type | Recommended Model | Rationale |
|-------------|-------------------|-----------|
| Standard experiential | Sonnet | Good balance of quality and speed |
| Complex reasoning | Opus 4.5 | Best for nuanced, multi-step tasks |
| Quick demonstrations | Haiku | Fast responses for simple interactions |
| Roleplay/persona | Sonnet or Opus | Higher temperature benefits from quality |
| Task-constrained | Sonnet or Haiku | Consistent output, speed matters |

---

## Facilitator Guides

The `facilitator-guide.md` file provides support for cohort facilitators leading the lesson.

### Purpose

Help facilitators:
- Anticipate and address learner questions
- Handle technical or conceptual challenges
- Pace the lesson appropriately
- Spark meaningful discussion

### Facilitator Guide Structure

```markdown
# Facilitator Guide: [Lesson Title]

## Common Learner Questions

**Q: [Anticipated question]**
A: [Suggested response]

## Potential Challenges

### [Challenge Name]
**Issue:** [Description]
**Resolution:** [How to address]

## Timing Considerations

- **Introduction:** [Pacing notes]
- **Hands-on Practice:** [Where learners need more time]
- **Wrap-up:** [Timing notes]

## Discussion Prompts

- [Question to spark discussion]
- [Question to spark discussion]

## Tips for Live Facilitation

[Additional guidance]
```

### Writing Facilitator Guides

**DO:**
- Base questions on actual confusion points in the lesson concept
- Provide specific, actionable resolutions for challenges
- Include discussion prompts that connect to learner work
- Note where the lesson typically runs long or short

**DON'T:**
- Include generic questions unrelated to the lesson
- Provide vague resolutions ("just explain it better")
- Skip timing considerations
- Forget to address technical troubleshooting

### Common Question Patterns

| Lesson Type | Likely Questions |
|-------------|------------------|
| Bare/limited config | "Why can't it remember what I just said?" |
| Context-rich | "How do I create context files for my org?" |
| Deliberately flawed | "Is this how AI always works?" |
| Roleplay | "How realistic should I treat the character?" |
| Comparison (second lesson) | "Why is this so different from the last one?" |

---

## Self-Assessment

The `self-assessment.md` file provides learners with reflection opportunities.

### Purpose

Help learners:
- Check their understanding of key concepts
- Reflect on practical application
- Provide feedback to improve the lesson

### Self-Assessment Structure

```markdown
# Self-Assessment: [Lesson Title]

## Comprehension Checks

1. [Question testing understanding of concept 1]
2. [Question testing understanding of concept 2]
3. [Question testing practical application]

## Reflection Prompts

- How could you apply this in your organization?
- What challenges might you encounter?
- What additional support or resources would you need?

## Feedback

We value your input! After completing this lesson:
- Share what worked well
- Identify what could be improved
- Ask questions or raise concerns

**Feedback Options:**
- LeadersPath community discussion forum
- Cohort session discussions
```

### Writing Comprehension Checks

**Good comprehension questions:**
- Ask about observable differences the learner experienced
- Connect to the lesson's learning objectives
- Can be answered based on the hands-on experience

**Bad comprehension questions:**
- Test memorization of definitions
- Ask about concepts not covered in the lesson
- Require external research to answer

**Example questions by lesson type:**

| Lesson Type | Example Questions |
|-------------|-------------------|
| Bare config | "What did you notice about the specificity of the AI's responses?" |
| Context-rich | "How did the AI's responses change compared to the unconfigured version?" |
| Sycophancy demo | "Did the AI push back on any of your ideas? Why or why not?" |
| Roleplay | "What techniques did the AI use to stay in character?" |

---

## Examples

### Complete Lesson Package

**Lesson: Starting from Zero**

**Folder structure:**
```
01-starting-from-zero/
├── Lesson-Plan.md
├── Chatbot Configuration/
│   ├── system-prompt.md
│   ├── api-settings.md
│   └── model-selection.md
├── Context Files/
├── lesson-text.md
├── Assessment/
│   └── self-assessment.md
├── Resources/
│   └── Additional Reading/
├── Facilitator Notes/
│   └── facilitator-guide.md
└── Skills/
```

**Lesson-Plan.md:**
```markdown
# Lesson Plan

## Lesson Information

* **Lesson Number:** 01
* **Lesson Title:** Starting from Zero
* **Course:** AI Foundations
* **Version:** 1.0
* **Last Updated:** 2026-01-15
* **Author:** LeadersPath Curriculum Team

---

## Learning Objectives

**By the end of this lesson, learners will be able to:**

1. Experience how an unconfigured LLM responds to work-related questions
2. Identify the limitations of generic AI responses
3. Recognize the gap that context and configuration fill

---

## Duration

**Estimated Time:** 20 minutes

**Breakdown:**
* Introduction: 3 min
* Main content: 5 min
* Hands-on practice: 10 min
* Wrap-up: 2 min

---

## Directions

### How to Proceed Through This Lesson

**Step 1: Read the Overview**
Read the lesson text to understand what you're about to experience.

**Step 2: Try the Suggested Prompts**
Enter each of the suggested prompts and observe the AI's responses.

**Step 3: Experiment Freely**
Try your own work-related questions to see how the AI responds.

**Step 4: Reflect**
Consider what's missing from the AI's responses and what would make them more useful.

---

## Model Specifications

### AI Models Used in This Lesson

**Primary Model:** Claude Sonnet

**Why This Model:**
Sonnet provides a good balance of capability and response speed for demonstrating baseline LLM behavior.

**Model Capabilities Demonstrated:**
* General knowledge and reasoning
* Natural language generation
* Task comprehension

### API Configuration

**Model String:** claude-sonnet-4-5-20250929
**Max Tokens:** 4096
**Temperature:** 0.7

---

## Chatbot Configuration

### Overview

This lesson uses a deliberately minimal chatbot configuration to demonstrate what AI lacks without proper setup.

### Configuration Files

**Location:** `Chatbot Configuration/` folder

**Files Included:**
* `system-prompt.md` - Minimal "helpful assistant" prompt
* `api-settings.md` - Standard parameters
* `model-selection.md` - Why Sonnet was chosen

### Transparency Principle

All configuration details are visible to learners. This allows them to understand exactly how limited the setup is.

---

## Context Files

### Purpose

This lesson deliberately uses NO context files to demonstrate baseline AI behavior.

### Files Included

None — this is intentional.

### Demonstration Approach

Learners experience the AI without any organizational context, observing the generic, non-specific nature of responses.

---

## Skills (Agentic Processes)

No agentic skills required for this lesson.

---

## Resources

### Additional Reading

**Location:** `Resources/Additional Reading/` folder

**External Resources:**
* [Anthropic Claude Documentation](https://docs.anthropic.com/) — Official model documentation

---

## Assessment and Feedback

### Comprehension Checks

**Location:** `Assessment/` folder

See `self-assessment.md` for comprehension questions and reflection prompts.

---

## Technical Requirements

### Prerequisites

**Prior Knowledge:**
* None (first lesson in course)

**Account Requirements:**
* LeadersPath learner account (logged in)

---

## Notes for Facilitators

**Location:** `Facilitator Notes/` folder

See `facilitator-guide.md` for discussion prompts, common questions, and timing considerations.

---

## Related Content

### Prerequisites
None (first lesson in course)

### Follow-Up Lessons
* Lesson 02 - Context Makes the Difference
```

**Chatbot Configuration/system-prompt.md:**
```markdown
You are a helpful AI assistant.

Respond to user questions to the best of your ability. Be friendly and informative.
```

**Chatbot Configuration/api-settings.md:**
```markdown
# API Settings

## Model Configuration
- **Model:** sonnet
- **Model String:** claude-sonnet-4-5-20250929
- **Max Tokens:** 4096
- **Temperature:** 0.7
- **Allow Model Switch:** no

## Context Files
None — this lesson deliberately omits context to demonstrate baseline behavior.

## Skills
None

## Configuration Notes
This minimal configuration is intentional. The lesson demonstrates what AI lacks without proper context and configuration.
```

**Chatbot Configuration/model-selection.md:**
```markdown
# Model Selection Rationale

## Why Sonnet

Sonnet provides the best balance of capability and response speed for this demonstration. It's capable enough to show what a modern LLM can do, while fast enough for responsive interaction.

## Capabilities Demonstrated
- General knowledge and reasoning
- Natural language generation
- Task comprehension without specific context

## Trade-offs Considered
- **Haiku:** Faster but might seem artificially limited; we want learners to see capable AI, just unconfigured AI
- **Opus 4.5:** More capable but slower; overkill for demonstrating baseline behavior

## Alternative Considerations
Haiku could work for this lesson, but Sonnet ensures learners see that the limitation is configuration, not capability.
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

**Assessment/self-assessment.md:**
```markdown
# Self-Assessment: Starting from Zero

## Comprehension Checks

1. What did you notice about the specificity of the AI's responses to your work questions?
2. When you asked about "your team" or "your company," how did the AI handle the lack of context?
3. How much editing would the AI's outputs need before you could use them in your actual work?

## Reflection Prompts

- How could you apply this understanding when evaluating AI tools for your organization?
- What specific information would the AI need to provide more useful responses?
- What challenges might arise if staff use unconfigured AI for organization-specific work?

## Feedback

We value your input! After completing this lesson:
- Share what worked well
- Identify what could be improved
- Ask questions or raise concerns

**Feedback Options:**
- LeadersPath community discussion forum
- Cohort session discussions
```

**Facilitator Notes/facilitator-guide.md:**
```markdown
# Facilitator Guide: Starting from Zero

## Common Learner Questions

**Q: Is this really the same AI that powers [impressive demo they've seen]?**
A: Yes! The difference is configuration. Those demos have extensive system prompts, context, and often curated examples. This lesson shows the baseline before any of that.

**Q: Why would anyone use AI without context?**
A: Many people do—and get frustrated by generic results. This lesson helps learners understand WHY their past AI experiences may have been disappointing.

**Q: Can I make it remember my company information during this session?**
A: You can tell it information in your prompts, but it won't persist. That's what context files solve in later lessons.

## Potential Challenges

### Learner Already Has AI Experience
**Issue:** Learners who use ChatGPT or similar tools may feel this is too basic.
**Resolution:** Acknowledge their experience and frame this as understanding the baseline. Ask: "How often do you get outputs you can use without editing?"

### Responses Seem Pretty Good
**Issue:** Sometimes the AI produces decent generic advice, which undercuts the lesson.
**Resolution:** Push for specificity: "Ask it about YOUR specific project or YOUR company's values. Notice how it can't actually reference those."

## Timing Considerations

- **Introduction:** Keep brief (2-3 min) — let the experience teach
- **Hands-on Practice:** This is the core — give learners 10+ minutes to explore
- **Wrap-up:** Important to solidify the insight before moving to next lesson

## Discussion Prompts

Use these to spark discussion in cohort settings:
- "What surprised you about the AI's responses?"
- "How is this different from what you expected?"
- "Where do you see this kind of generic AI advice in your current work?"

## Tips for Live Facilitation

- Resist the urge to over-explain upfront. The "aha" moment comes from experience.
- If learners ask "why is it doing that?" — turn it back: "What do you think is missing?"
- This lesson pairs well with Lesson 2 (Context Makes the Difference) — consider running them back-to-back for maximum contrast.
```
