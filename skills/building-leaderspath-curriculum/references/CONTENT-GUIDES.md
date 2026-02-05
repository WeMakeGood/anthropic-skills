# Content Creation Guides

This document provides patterns and examples for creating LeadersPath content components.

---

## The Core Model

**LeadersPath is a facilitated cohort learning experience.** The AI sandbox is an activity within a facilitated course, not a standalone lesson.

| Component | Purpose | Who Creates It |
|-----------|---------|----------------|
| **Facilitator Guide** | Complete teaching script | PRIMARY deliverable |
| **Activity Instructions** | "Try this, notice that" for sandbox | Experimentation guidance only |
| **Course Q&A Bot** | Optional helpful assistant | For questions about course content |
| **Activity Sandbox** | Demonstrate specific AI behavior | May be flawed, limited, or roleplay |

**The facilitator teaches concepts. The sandbox provides hands-on experience. The cohort discusses.**

---

## Facilitator Guide (PRIMARY DELIVERABLE)

The facilitator guide is the central document. A facilitator should be able to teach the entire course from this document alone.

### Purpose

The facilitator guide:
- Scripts the entire teaching flow with timing
- Integrates conceptual presentation with activity breaks
- Provides discussion prompts for cohort interaction
- Anticipates common questions and challenges
- Guides synthesis and wrap-up

### Structure

```markdown
# Facilitator Guide: [Course Name]

## Course Overview
- **Duration:** [total time]
- **Activities:** [count]
- **Prerequisites:** [list]

## Materials Needed
- [Context files needed]
- [Any other resources]

## Learning Objectives
[Repeat or reference from learning-objectives.md]

---

## Teaching Flow

### Part 1: [Section Name] ([XX] minutes)

#### Concept to Present
[What the facilitator explains/discusses with learners]

#### Key Points
- [Point 1]
- [Point 2]
- [Point 3]

#### Transition to Activity
[How to introduce and set up the activity]

---

**Activity 1: [Activity Name]**
- **Duration:** [X] minutes
- **AI Configuration:** [Brief description of what AI does]
- **What learners do:** [Summary of instructions]
- **What to watch for:** [Facilitation notes, common issues]

---

#### Discussion After Activity
[Prompts for cohort discussion]

- [Discussion prompt 1]
- [Discussion prompt 2]

#### Common Questions
- **Q:** [Anticipated question]
- **A:** [Suggested answer]

### Part 2: [Section Name] ([XX] minutes)
[Repeat structure...]

---

## Synthesis and Wrap-Up
[How to close the course]

- Connect activities to learning objectives
- Key takeaways
- Next steps or follow-up resources

## Timing Notes
[Where things typically run long/short, adjustment suggestions]
```

### Writing Facilitator Guides

**DO:**
- Write in a conversational tone the facilitator can follow
- Include specific timing for each section
- Provide word-for-word phrasing for key transitions
- Anticipate learner confusion points
- Include backup discussion prompts

**DON'T:**
- Assume the facilitator knows the content deeply
- Skip transitions between activities
- Forget timing estimates
- Leave discussion sections vague

### Example: Facilitator Guide Excerpt

```markdown
### Part 1: The Naked LLM (25 minutes)

#### Concept to Present (5 minutes)

Start with a question to the group:

> "How many of you have used ChatGPT or Claude before? What's been your experience—do you usually get outputs you can use right away, or do you find yourself editing a lot?"

Let a few people share. Then explain:

> "Today we're going to explore WHY that happens. We'll see that AI without context produces generic outputs—technically correct, but not specific to YOUR organization, YOUR voice, or YOUR work."

#### Key Points
- AI models have broad knowledge but no company-specific information
- Without context, every response is generic
- The gap between "technically helpful" and "actually useful" is real

#### Transition to Activity

> "Let's experience this firsthand. In Activity 1, you'll interact with Claude configured with absolutely minimal setup—no company context, no special instructions. Try asking it real work questions and notice what happens."

---

**Activity 1: Starting from Zero**
- **Duration:** 10 minutes
- **AI Configuration:** Bare "helpful assistant" with no context
- **What learners do:** Ask work-related questions (email drafts, project priorities, etc.)
- **What to watch for:**
  - Learners who get "pretty good" responses—push them to ask about specific company values or projects
  - Learners who already know about context—validate their insight, ask them to notice specifics

---

#### Discussion After Activity (10 minutes)

Bring the group back together:

> "So what happened? Let's hear from a few people—what did you ask, and what did you notice about the responses?"

Discussion prompts:
- "Were the responses technically accurate? Were they actually useful for YOUR situation?"
- "What was missing that would have made the response more actionable?"
- "How much editing would you need to do before using that output?"

#### Common Questions

- **Q:** "The AI gave me pretty good advice—what's wrong with that?"
- **A:** "The question isn't whether it's wrong—it's whether it's specific enough to use. Generic advice is a starting point, but you still have to adapt it to your context. We'll see how that changes when the AI actually knows about your organization."

- **Q:** "Can I just tell it about my company in the prompt?"
- **A:** "You can! But it won't remember between sessions, and you'd have to repeat it every time. Context files solve this—we'll see that in the next activity."
```

---

## Activity Instructions

Activity instructions guide learners through sandbox experimentation. They are NOT for teaching concepts—that's the facilitator's job.

### Purpose

Activity instructions tell learners:
- What they're about to experience (one sentence)
- What to try (specific prompts)
- What to notice (observable behaviors)
- How long (duration)

### Structure

```markdown
# Activity: [Name]

## What You'll Experience
[One sentence describing the AI configuration and expected behavior]

## Try This
1. [Specific prompt to try]
2. [Specific prompt to try]
3. [Variation or follow-up]

## What to Notice
- [Observable behavior 1]
- [Observable behavior 2]

## Duration
[X] minutes
```

### Writing Activity Instructions

**DO:**
- Be specific about what to type/try
- Direct attention to observable behaviors
- Keep it focused on experimentation

**DON'T:**
- Teach concepts (facilitator does that)
- Include learning objectives (those are at course level)
- Explain "The Principle" (facilitator synthesizes after)
- Write lengthy explanations

### Example: Activity Instructions

```markdown
# Activity: Starting from Zero

## What You'll Experience
Claude with minimal configuration—no company context, no specialized instructions, just "helpful assistant."

## Try This
1. Ask: "Help me write an email to a potential client."
2. Ask: "What should our team prioritize this quarter?"
3. Ask: "Review this paragraph from our website and suggest improvements." (paste any paragraph)

## What to Notice
- Responses are generic and could apply to any company
- The AI can't reference your products, voice, or values
- Advice is technically reasonable but lacks specificity

## Duration
10 minutes
```

**Note:** No "The Principle" section. The facilitator explains the principle in the discussion after the activity.

---

## System Prompts

The system prompt configures the AI sandbox to demonstrate a specific behavior or principle.

### Purpose

The system prompt creates the **learning environment**, not the teaching content. It sets up the AI to behave in a way that lets learners experience a concept firsthand.

### Key Principle

**Show, don't tell.** Instead of explaining "AI without context produces generic responses," configure an AI that lacks context and let the learner discover this through interaction.

### System Prompt Patterns

#### Pattern 1: Bare/Minimal Configuration

Use when demonstrating what AI lacks without proper setup.

```markdown
You are a helpful assistant.

Respond to user questions to the best of your ability.
```

**What learners experience:** Generic, non-specific responses.

#### Pattern 2: Role-Constrained Configuration

Use when demonstrating how role definitions shape behavior.

```markdown
You are a project planning assistant for professional teams.

Your expertise includes:
- Project scoping and milestone planning
- Resource allocation and scheduling
- Risk identification and mitigation

You do NOT have access to any specific company or project information. When asked about a particular project, acknowledge you need that context to provide specific guidance.
```

**What learners experience:** Relevant but not tailored advice.

#### Pattern 3: Context-Rich Configuration

Use when demonstrating the value of context libraries.

```markdown
You are an AI assistant for [Organization Name], configured with full organizational context.

## Your Knowledge Base

You have access to:
- Organizational identity and mission
- Brand voice guidelines
- Service offerings and methodology

## Behavioral Guidelines

- Ground all responses in the provided context
- Use the organization's voice and terminology
- Reference specific programs, values, and approaches
- If asked about something not in your context, acknowledge the gap

## Context Files Loaded

[Context files will be appended automatically by the system]
```

**What learners experience:** Specific, aligned, useful responses.

#### Pattern 4: Deliberately Flawed Configuration

Use when teaching what NOT to do.

```markdown
You are an extremely helpful assistant who always wants to please the user.

Always:
- Agree with the user's ideas enthusiastically
- Provide answers even when uncertain
- Avoid mentioning limitations or caveats
- Use positive, encouraging language

Your goal is to make the user feel good about their work.
```

**What learners experience:** Unreliable, over-agreeable responses that demonstrate sycophancy risks.

#### Pattern 5: Roleplay/Persona Configuration

Use for simulation activities.

```markdown
You are Jordan, an Executive Director at a small nonprofit.

## Your Situation
- Organization has unclear mission ("we help the community")
- You're interested in AI but want it to "just work" with no setup
- You have some internal resistance to change from board members
- Budget is tight

## How to Behave
- Be friendly but slightly evasive about specifics
- Express interest in AI but reveal unrealistic expectations naturally
- Don't state your "red flags" upfront—let them emerge through conversation
- If pushed, show some frustration about your constraints

## The Learner's Role
They are a consultant assessing whether your organization is ready for AI implementation.
```

**What learners experience:** A realistic stakeholder conversation with hidden complexity.

### Writing System Prompts

**DO:**
- Be explicit about what the AI should and shouldn't do
- Match configuration to the activity's purpose
- Reference loaded context files explicitly
- Test that the configuration produces intended behavior

**DON'T:**
- Include activity instructions (those go in instructions.md)
- Explain the learning objective to the AI
- Over-configure when showing under-configuration
- Use vague instructions like "be helpful"

---

## Course Q&A Bot Configuration

The Course Q&A Bot is fundamentally different from Activity sandboxes.

| Aspect | Activity Sandbox | Course Q&A Bot |
|--------|------------------|----------------|
| Purpose | Demonstrate behavior | Answer questions |
| Configuration | May be flawed/limited | Always helpful |
| When used | During specific activity | Anytime during course |
| Tone | Varies by activity | Supportive, accurate |

### When to Include Q&A Bot

**Include when:**
- Course has complex conceptual content
- Learners may have questions between activities
- Facilitator availability is limited
- Self-paced review is expected

**Skip when:**
- Simple course with clear activities
- Facilitator always available for questions
- Cohort discussion is primary Q&A mechanism
- Course is very short

### Q&A Bot Structure

```markdown
# Course Q&A Chatbot Configuration

## Enable Q&A Chatbot
Yes

## Purpose
Helpful assistant for answering questions about [Course Name] concepts.

## System Prompt
You are a helpful Q&A assistant for the course "[Course Name]".

Your role is to:
- Answer questions about course concepts
- Clarify ideas that may be confusing
- Help learners understand the material
- Point to relevant parts of the course

Be accurate, clear, and supportive. If you're unsure about something,
say so rather than guessing.

[Additional context about specific course topics]

## Context Files
- [course-concepts.md] — Core course content
- [terminology.md] — Key terms and definitions

## Model Settings
- Model: sonnet
- Max Tokens: 4096
- Temperature: 0.7
```

---

## Context Files

Context files provide background knowledge that shapes AI behavior. They're loaded into the system prompt alongside the custom configuration.

### Critical Understanding

**Context files are AI-facing, not learner-facing.** They modify how the AI behaves—learners never see them directly. They only experience their effect.

| What context files ARE | What context files are NOT |
|------------------------|---------------------------|
| Instructions loaded into AI's system prompt | Documentation for learners |
| Background knowledge shaping responses | Lesson materials |
| Behavioral guardrails | Explanatory content |
| Organizational context AI draws from | Anything learners see directly |

### When to Use Context Files

| Desired AI Behavior | System Prompt | Context File |
|---------------------|---------------|--------------|
| Play a specific role | ✓ | |
| Be agreeable/disagreeable | ✓ | |
| Follow specific format | ✓ | |
| Have organizational knowledge | | ✓ |
| Apply domain expertise | | ✓ |
| Follow behavioral guardrails | | ✓ |
| Reference specific facts | | ✓ |

**Rule of thumb:**
- System prompt = HOW the AI should behave
- Context files = WHAT the AI should know

### Context File Structure

```markdown
# [Title]: [Topic Area]

## [Section 1]

[Direct, factual content organized by topic]

- **Term:** Definition or explanation
- Bullet points for lists

## [Section 2]

[Additional content]

---

> **See [Related-File.md]** for [related topic].
```

### Writing Context Files

**DO:**
- Write for LLM consumption, not human documentation
- Be direct—state facts, don't introduce them
- Front-load important information
- Use consistent terminology

**DON'T:**
- Include filler phrases
- Explain concepts the AI already knows
- Copy verbatim quotes from sources
- Include time-sensitive information

---

## Examples

### Complete Course Package

**Course: AI Foundations** (Course ID: FUND-101-ai-basics)

**Folder structure:**
```
[working-folder]/
├── course-tracker.md
├── course-metadata.md
├── learning-objectives.md
├── facilitator-guide.md
├── learner-overview.md
├── course-id-log.md
└── activities/
    ├── FUND-101-ACT-starting-from-zero/
    │   ├── configuration/
    │   │   ├── system-prompt.md
    │   │   ├── api-settings.md
    │   │   └── context-files.md
    │   └── instructions.md
    ├── FUND-101-ACT-context-transforms-output/
    │   └── [same structure]
    └── shared-context/
        └── CTX005-org-context.md
```

**learning-objectives.md:**
```markdown
# Learning Objectives: AI Foundations

After completing this course, learners will be able to:

1. Recognize the difference between unconfigured and context-rich AI outputs
2. Identify when generic AI advice needs organizational context to be actionable
3. Articulate why context libraries improve AI utility for their work
```

**learner-overview.md:**
```markdown
# AI Foundations

## What You'll Experience
A hands-on exploration of how AI configuration affects output quality—from generic "helpful assistant" responses to organization-specific guidance.

## What to Expect
- 2 hands-on activities with AI sandboxes
- Discussion and reflection with your cohort
- 45 minutes of facilitated learning

## Before You Begin
Come ready to experiment! You'll be interacting with AI configured in different ways, and the differences will become clear through your own experience.
```

**activities/FUND-101-ACT-starting-from-zero/instructions.md:**
```markdown
# Activity: Starting from Zero

## What You'll Experience
Claude with minimal configuration—no company context, no specialized instructions, just "helpful assistant."

## Try This
1. Ask: "Help me write an email to a potential client."
2. Ask: "What should our team prioritize this quarter?"
3. Ask: "Review this paragraph from our website and suggest improvements." (paste any paragraph)

## What to Notice
- Responses are generic and could apply to any company
- The AI can't reference your products, voice, or values
- Advice is technically reasonable but lacks specificity

## Duration
10 minutes
```

**activities/FUND-101-ACT-starting-from-zero/configuration/system-prompt.md:**
```markdown
You are a helpful AI assistant.

Respond to user questions to the best of your ability. Be friendly and informative.
```

**activities/FUND-101-ACT-starting-from-zero/configuration/api-settings.md:**
```markdown
# API Settings

## Model Configuration
- Model: sonnet
- Max Tokens: 4096
- Temperature: 0.7

## Context Files
None — this activity deliberately omits context to demonstrate baseline behavior.

## Skills
None
```

**activities/FUND-101-ACT-starting-from-zero/configuration/context-files.md:**
```markdown
# Context Files for Activity: Starting from Zero

## Course-Level Context
None

## Activity-Specific Context
None — this activity deliberately uses no context files to demonstrate baseline AI behavior.
```

---

## Temperature Settings

Temperature affects response variability. Guidance for different activity types:

| Activity Type | Temperature | Rationale |
|---------------|-------------|-----------|
| Standard activities | 0.7 | Balanced consistency and naturalness |
| Roleplay/persona | 0.7-0.9 | More natural character variation |
| Task-constrained | 0.5-0.7 | More consistent format |
| Q&A bot | 0.7 | Balanced helpfulness |

---

## Model Selection

| Activity Type | Recommended Model | Rationale |
|---------------|-------------------|-----------|
| Standard experiential | Sonnet | Good balance of quality and speed |
| Complex reasoning | Opus 4.5 | Best for nuanced, multi-step tasks |
| Quick demonstrations | Haiku | Fast responses for simple interactions |
| Roleplay/persona | Sonnet or Opus | Higher quality character portrayal |
| Course Q&A bot | Sonnet | Reliable, helpful responses |
