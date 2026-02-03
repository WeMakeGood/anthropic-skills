# Tips for Curriculum Designers

These guidelines help you write prompts that produce better curriculum output.

---

## 1. Describe Lesson Concepts Clearly

The more specific your lesson concept, the better the output.

**Weak:** "A lesson about AI ethics"

**Strong:** "AI configured with anti-sycophancy guardrails. Learner presents flawed ideas and receives honest pushback. Demonstrates professional objectivity vs. the sycophancy experienced in Lesson 1."

Include:
- What AI behavior the learner should experience
- Whether it's a limitation, capability, or flaw being demonstrated
- How this lesson relates to others (comparison pair, prerequisite, standalone)

---

## 2. Identify Source Document Types

When providing source material, indicate what type it is:

| Type | Description | How It's Used |
|------|-------------|---------------|
| **Curriculum document** | Learning objectives, lesson plans, course outlines | Direct extraction of structure and objectives |
| **Organizational context** | Internal docs, frameworks, guidelines | Adapted and transformed for AI consumption |
| **Reference material** | Background reading, research papers | Informs content but not used directly |

Example: "The attached F3_ethical_ai_framework.md is an organizational context file—extract relevant principles for the lessons."

---

## 3. Flag Comparison Pairs

When lessons are meant to be compared, explicitly state:
- Which lessons form the comparison pair
- What contrast the learner should notice
- Whether to use the same prompts across both lessons

Example: "Lessons 1 and 2 are a comparison pair. Lesson 2 should use the same 'Try This' prompts as Lesson 1 so learners can directly compare responses."

---

## 4. Specify Roleplay Lessons

For persona/simulation lessons, provide:
- Character name and role
- Specific behaviors or traits to exhibit
- How traits should emerge (naturally through conversation vs. stated upfront)
- What the learner's role is (consultant, interviewer, manager, etc.)

Example: "Lesson 3 is a roleplay. AI plays 'Jordan,' an Executive Director with red flags: unclear mission, wants no-work solution, internal conflict about AI. Learner plays a consultant assessing fit. Red flags should emerge naturally through questioning, not be stated upfront."

---

## 5. Hint at Context File Needs

If you know whether a lesson needs a context file, say so. If unsure, describe the behavior and the skill will determine:

- Behavior from **instructions** (be agreeable, be brief, play a role) → system prompt only
- Behavior from **knowledge** (organizational context, domain expertise) → context file needed
- Behavior from **guardrails** (anti-sycophancy rules, epistemic standards) → context file needed

Example: "Lesson 1 probably doesn't need a context file—tech-first behavior comes from instructions. Lesson 2 needs the ethical framework as a context file since it requires knowledge to apply."

---

## 6. Note Reuse Opportunities

If multiple lessons should share a context file, mention it:

Example: "Lessons 2 and 4 should share the ethical AI framework context file. Lesson 2 applies it as an advisor; Lesson 4 applies it with additional capability-transfer instructions."

---

## Quick Reference

### Lesson Concept Checklist

Before submitting a lesson concept, ensure you've included:

- [ ] What AI behavior learners will experience
- [ ] Whether it's a limitation, capability, or flaw
- [ ] Relationship to other lessons (if any)
- [ ] Source document types identified
- [ ] Comparison pair flagged (if applicable)
- [ ] Roleplay details specified (if applicable)
- [ ] Context file hints provided
- [ ] Reuse opportunities noted

### Common Mistakes to Avoid

| Mistake | Better Approach |
|---------|-----------------|
| "Teach about context libraries" | "AI without context produces generic responses; learner asks work questions and sees the limitation" |
| "Show comparison of approaches" | "Lesson 1: sycophantic AI. Lesson 2: objective AI. Learner uses same prompts in both." |
| "Roleplay with a stakeholder" | "AI plays 'Jordan,' ED with unclear mission. Red flags emerge through questioning." |
| Vague source labeling | "File A is curriculum (extract objectives). File B is org context (transform for AI)." |
