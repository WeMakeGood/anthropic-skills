# Lesson Plan Template

This template defines the structure for `Lesson-Plan.md` files. Fill all sections based on the curriculum source documents.

---

## Template

```markdown
# Lesson Plan

## Lesson Information

* **Lesson Number:** [##]
* **Lesson Title:** [Descriptive title]
* **Course:** [Parent course name]
* **Version:** [1.0]
* **Last Updated:** [YYYY-MM-DD]
* **Author:** [Name or "LeadersPath Curriculum Team"]

---

## Learning Objectives

**By the end of this lesson, learners will be able to:**

1. [Specific, measurable objective]
2. [Specific, measurable objective]
3. [Specific, measurable objective]

---

## Duration

**Estimated Time:** [## minutes]

**Breakdown:**
* Introduction: [## min]
* Main content: [## min]
* Hands-on practice: [## min]
* Wrap-up: [## min]

---

## Directions

### How to Proceed Through This Lesson

**Step 1: [First Step]**

[Clear instructions for what learner should do]

**Step 2: [Second Step]**

[Clear instructions]

**Step 3: [Hands-On Practice]**

[Instructions for interactive component]

**Step 4: [Reflection]**

[Prompts for learner to consider what they've learned]

---

## Model Specifications

### AI Models Used in This Lesson

**Primary Model:** Claude [Opus 4.5 / Sonnet / Haiku]

**Why This Model:**
[Brief explanation of why this specific model was chosen for this lesson]

**Model Capabilities Demonstrated:**
* [Capability 1]
* [Capability 2]
* [Capability 3]

### API Configuration

**Model String:** [claude-opus-4-5-20251101 / claude-sonnet-4-5-20250929 / claude-haiku-4-5-20251001]
**Max Tokens:** [####]
**Temperature:** [0.0 - 1.0]

**Configuration Notes:**
[Any specific configuration choices and rationale]

---

## Chatbot Configuration

### Overview

This lesson uses a [type: minimal / role-constrained / context-rich / deliberately flawed] chatbot configuration to demonstrate [concept/capability].

### Configuration Files

**Location:** `Chatbot Configuration/` folder

**Files Included:**
* `system-prompt.md` - [Brief description]
* `api-settings.md` - API endpoint and parameter configuration
* `model-selection.md` - Why this model was chosen

### Transparency Principle

All configuration details are visible to learners. This allows them to:
* Understand exactly how the chatbot is configured
* Replicate the setup in their own implementation
* Learn best practices for prompt engineering
* See the impact of different model choices

---

## Context Files

### Purpose

[Describe what context the AI has access to, or explicitly state "None" if this lesson deliberately omits context]

### Files Included

**Course-Level Context (shared):**
* [context/filename.md] — [Purpose]

**Lesson-Specific Context:**
* [Context Files/filename.md] — [Purpose]

Or: "None — this lesson deliberately omits context to demonstrate [behavior]."

### Demonstration Approach

[Describe how the presence or absence of context creates the learning experience]

### Learner Access

[Note whether learners can view/download context files per transparency principle]

---

## Skills (Agentic Processes)

### Overview

[Does this lesson use agentic skills? If not, state: "No agentic skills required for this lesson."]

### Skills Included

**Location:** `Skills/` folder

* [skill-name] — [Description]

### Transparency and Copyability

Per LeadersPath's transparency principle:
* All skill definitions are visible to learners
* Implementation details are documented
* Learners can copy and adapt skills for their own use

---

## Resources

### Additional Reading

**Location:** `Resources/Additional Reading/` folder

**Articles and Guides:**
* [Title] — [Brief description]

**External Resources:**
* [Title](URL) — [Brief description]

---

## Assessment and Feedback

### Comprehension Checks

**Location:** `Assessment/` folder

See `self-assessment.md` for:
* Comprehension questions
* Reflection prompts
* Feedback mechanism

---

## Technical Requirements

### Prerequisites

**Prior Knowledge:**
* [Required prior lessons]
* [Technical skills needed]

**Account Requirements:**
* LeadersPath learner account (logged in)
* [Any other platform access needed]

---

## Notes for Facilitators

**Location:** `Facilitator Notes/` folder

See `facilitator-guide.md` for:
* Common learner questions with suggested responses
* Potential challenges and resolutions
* Timing considerations
* Discussion prompts for cohort settings

---

## Related Content

### Prerequisites
* Lesson [##] - [Title]

### Follow-Up Lessons
* Lesson [##] - [Title]

### Related Courses
* [Course name that explores related topics]
```

---

## Section Guidelines

### Lesson Information

- **Lesson Number:** Use two digits (01, 02, etc.) for consistent sorting
- **Version:** Start at 1.0; increment for significant updates
- **Author:** Use individual name for drafts, "LeadersPath Curriculum Team" for finalized content

### Learning Objectives

Write objectives as **observable, demonstrable outcomes**.

**Good:**
- "Identify the difference between AI responses with and without context"
- "Configure a system prompt that constrains AI behavior"
- "Recognize sycophantic AI patterns and their risks"

**Bad:**
- "Understand context libraries" (not observable)
- "Learn about prompt engineering" (too vague)
- "Appreciate the importance of ethical AI" (not demonstrable)

### Duration

Base estimates on:
- Reading lesson text: ~2-3 minutes
- Each suggested interaction: ~3-5 minutes
- Reflection/comparison: ~2-3 minutes

**Typical ranges:**
- Simple demonstration: 15-20 minutes
- Standard experiential lesson: 20-30 minutes
- Complex multi-part lesson: 30-45 minutes

### Directions

Write step-by-step instructions that guide learners through the experience:
1. What to read first
2. What to try in the sandbox
3. What to observe
4. What to reflect on

Use second person ("Read the overview," "Try this prompt," "Notice how...").

### Model Specifications

See CONTENT-GUIDES.md for model selection guidelines.

| Lesson Type | Recommended Model | Temperature |
|-------------|-------------------|-------------|
| Standard experiential | Sonnet | 0.7 |
| Complex reasoning | Opus 4.5 | 0.7 |
| Quick demonstrations | Haiku | 0.7 |
| Roleplay/persona | Sonnet or Opus | 0.7-0.9 |
| Task-constrained | Sonnet or Haiku | 0.5-0.7 |

### Chatbot Configuration

Identify the configuration type:
- **Minimal:** Bare "helpful assistant" with no context
- **Role-constrained:** Defined role but no org context
- **Context-rich:** Full context library loaded
- **Deliberately flawed:** Configured to demonstrate bad patterns (sycophancy, etc.)
- **Task-constrained:** Focused on specific task with guardrails

### Context Files

Distinguish between:
- **Course-level context** (in `EN/context/`) — Shared across multiple lessons
- **Lesson-specific context** (in lesson's `Context Files/`) — Unique to this lesson

If no context files: Explicitly state this is intentional and explain why.

### Prerequisites

Only mark prerequisites when:
- The lesson builds directly on concepts from another lesson
- The AI configuration assumes knowledge from a prior experience
- Doing lessons out of order would create confusion

**Don't over-prerequisite:** If lessons are related but can stand alone, don't force sequencing.

---

## Curriculum Design Principles

This template follows LeadersPath's pedagogical principles:

* **Show, don't tell** — Experiential learning through hands-on practice
* **Transparency** — All implementation details visible to learners
* **Community learning** — Questions and discussion valued
* **No vendor pitching** — Teaching over selling
* **Technical translation** — Making AI accessible to nonprofit leaders
