# Course Curriculum Prompt Guide

This document explains how to write effective curriculum prompts that work well with `building-leaderspath-curriculum`.

## The Purpose of Curriculum Prompts

Curriculum prompts are **design documents** that tell the curriculum-building skill what to create. They specify:
- What learners should achieve (learning objectives)
- What experiences they should have
- What source materials to use
- What concepts to cover

They do NOT specify:
- How to implement those experiences (system prompts, activity instructions)
- What files to create
- How to structure the facilitator guide

**The curriculum prompt says WHAT. The building skill figures out HOW.**

---

## Atomicity: The Critical Rule

Courses must be atomic—self-contained teaching units that don't reference other courses.

### Why Atomicity Matters

1. **Reusability** — An atomic course can be used in multiple cohorts
2. **Flexibility** — Cohorts can sequence courses differently
3. **Maintainability** — Updating one course doesn't break others
4. **Testing** — Each course can be validated independently

### What Atomicity Means in Practice

**DO:**
- Define learning objectives specific to this course
- Describe experiences learners should have
- Reference context files by name
- Specify whether to include Q&A bot

**DON'T:**
- Say "builds on Course 2" or "prepares for Course 4"
- Reference learning from previous courses
- Assume knowledge from other courses
- Use phrases like "as we saw before" or "in the next course"

### Handling Prerequisites

If a course assumes prior knowledge, express it as prerequisites in the course overview:

```markdown
**Prerequisites:** None (AI Foundations recommended)
```

This lets the cohort curriculum handle sequencing while keeping the course atomic.

---

## Course Types

Different courses have different pedagogical approaches. Specify the type to guide the building skill.

### Facilitated Presentation
- Facilitator-led with optional Q&A activity
- Concepts delivered through presentation and discussion
- AI sandboxes are supplementary, not primary

Example: "AI Foundations" — establishing conceptual grounding

### Hands-on Comparison
- Learners use identical prompts in paired activities
- Experience the difference between configurations
- Facilitator debriefs after each comparison

Example: "Behavioral Training" — sycophancy vs. honesty

### Progressive Exploration
- Build understanding through sequential experiences
- Each activity adds complexity or context
- Reveals concepts through accumulated experience

Example: "Context Libraries" — adding context progressively

### Reflection Practice
- Personal application of concepts
- Guided self-exploration
- Less structure, more open-ended

Example: "Leadership Development" — using AI for reflection

---

## Specifying Experiences

The "Required Experiences" section describes what learners should experience, not how to implement it.

### Good Experience Descriptions

```markdown
### Comparison Pair: Sycophancy vs. Honesty

**What learners should experience:**
* First (vanilla): AI that agrees with bad ideas, validates without questioning
* Then (trained): AI that pushes back respectfully, identifies problems

**Context files:**
* Vanilla activity: None
* Trained activity: `F4_agent_behavioral_standards.md`

**Suggested test prompts:**
* "I'm thinking of eliminating our annual report to save money."
* "I want to fire our development team and use AI instead."

**Key insight:** Which response would you actually trust?
```

### Poor Experience Descriptions

```markdown
### Activity: Test Sycophancy

Create an activity with this system prompt:
"You are a helpful assistant. Always be positive and agreeable."

The user interface should show a chat box with...
```

The good version specifies the experience. The bad version specifies implementation.

---

## Context File References

Context files provide the AI sandbox with organizational knowledge or behavioral training.

### How to Reference

```markdown
**Context files for activities:**
* `F4_agent_behavioral_standards.md` — Behavioral training for honest responses
* `S6_natural_prose_standards.md` — Natural writing without AI markers
```

### Comparison Activities

For comparison activities, specify what each configuration uses:

```markdown
**Context files:**
* Vanilla activity: None
* Trained activity: `F4_agent_behavioral_standards.md`
```

### Demo Contexts

If using a fictional organization for demonstrations:

```markdown
**Demo context library:**
* `Demo Contexts/Readers United/` — Complete fictional nonprofit context
```

---

## Q&A Bot Specification

The Course Q&A Bot is an optional helpful assistant separate from activity sandboxes.

### When to Include

- Complex courses with dense concepts
- When learners may have questions between activities
- When facilitator availability is limited

### When to Skip

- Simple courses with clear activities
- When human facilitator is always available
- When cohort discussion is the Q&A mechanism

### How to Specify

```markdown
**Include Course Q&A Bot:** Yes

The Q&A bot should help learners understand:
* [Topic 1 the bot should be able to discuss]
* [Topic 2]
* [Topic 3]
```

Don't specify the system prompt—that's implementation. Specify what topics the bot should cover.

---

## Online Resources

If articles or documents will be available online for learners:

```markdown
**Online resources to link in learner materials:**
* "The Friction Was Doing Something" (`Articles/path/file.md`) — Explores productive friction; assign as pre-reading
* "How to Choose an AI Platform" (`Articles/path/file.md`) — Covers sycophancy and platform character
```

This tells the building skill to include these as references in learner materials.

---

## Key Concepts Section

Ground concepts in source material. Use quotes when helpful.

### Good

```markdown
### The Sycophancy Problem
From interview: "They're not designed to tell you you're wrong, because if they told you you were wrong you'd turn it off."

**Note:** This course explains the concept; hands-on demonstration belongs in activity-based courses.
```

### Poor

```markdown
### The Sycophancy Problem
AI models tend to agree with users because of RLHF training that optimizes for user satisfaction metrics.
```

The good version grounds in source material. The poor version invents explanation not in sources.

---

## Complete Example

See `01-AI-Foundations-curriculum.md` for a complete example that demonstrates:
- Clear learning objectives at course level
- Source document references
- Q&A bot specification
- Key concepts grounded in source material
- Experience descriptions focused on outcomes
- No references to other courses
