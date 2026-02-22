# Tips for Curriculum Designers

These guidelines help you write prompts that produce better curriculum output.

---

## The Core Model

**LeadersPath is a facilitated course learning experience.** The AI sandbox is an activity within a facilitated lesson, not a standalone tutorial.

| Old Model (Avoid) | New Model (Use) |
|-------------------|-----------------|
| Activity = standalone unit with AI | Lesson = cohesive facilitated experience |
| Activity teaches through AI | Facilitator teaches; AI demonstrates |
| Objectives per activity | Objectives per lesson |
| Facilitator notes = secondary | Facilitator guide = primary deliverable |

---

## 1. Design Lessons as Cohesive Experiences

Think of a lesson as a single facilitated session, not a collection of independent activities.

**Include in your prompt:**
- What the facilitator will present (concepts, context)
- What learners will experience in activities (hands-on experimentation)
- How activities connect to each other
- What discussion happens between activities

**Example prompt:**

> "Create a 60-minute lesson on AI sycophancy. The facilitator introduces the concept of sycophancy, then learners experience it firsthand in Activity 1 (sycophantic AI). The facilitator debriefs, then learners experience Activity 2 (honest AI). Lesson closes with discussion comparing the two experiences."

---

## 2. Write Facilitator Guides as the Primary Deliverable

The facilitator guide is the central document—a facilitator should be able to teach the entire lesson from it alone.

**Include in your prompt:**
- Timing expectations for each section
- Discussion prompts after activities
- Common questions learners might ask
- How to transition between presentation and activities

**Example prompt:**

> "The facilitator guide should include word-for-word suggested phrasing for key transitions, especially the setup before each activity. Include 2-3 discussion prompts after each activity."

---

## 3. Create Focused Activity Instructions

Activity instructions guide sandbox experimentation only—they do NOT teach concepts.

**Activity instructions should:**
- Be one paragraph or less for "What You'll Experience"
- Have 3-5 specific prompts to try
- Note 2-3 observable behaviors
- Include duration

**Activity instructions should NOT:**
- Teach concepts (facilitator does that)
- Include learning objectives (those are at lesson level)
- Explain "The Principle" (facilitator synthesizes after)

**Example prompt:**

> "Activity 1 should guide learners to try 3 specific prompts that reveal sycophantic behavior. Don't explain WHY sycophancy is a problem—the facilitator will discuss that after."

---

## 4. Structure Comparison Activities Within a Lesson

When learners need to compare two AI behaviors, use sequential activities within the same lesson.

**Pattern:**
1. Facilitator introduces the concept
2. Activity 1: Experience behavior A
3. Facilitator guides brief reflection
4. Activity 2: Experience behavior B (use same prompts as Activity 1)
5. Facilitator leads comparison discussion

**Example prompt:**

> "Activities 1 and 2 are comparison activities. Activity 2 should use the exact same 'Try This' prompts as Activity 1 so learners can directly compare responses."

---

## 5. Decide When to Include a Lesson Q&A Bot

The Lesson Q&A Bot is optional and separate from Activity sandboxes.

**Include Q&A bot when:**
- Lesson has complex conceptual content
- Learners may have questions between activities
- Facilitator availability is limited
- Self-paced review is expected

**Skip Q&A bot when:**
- Simple lesson with clear activities
- Facilitator always available for questions
- Lesson is very short

**Important distinction:**
- **Activity Sandbox** = Demonstrates specific behavior (may be flawed)
- **Lesson Q&A Bot** = Always helpful assistant for questions

**Example prompt:**

> "This lesson does NOT need a Q&A bot—it's a 30-minute session with the facilitator present throughout."

---

## 6. Identify Source Document Types

When providing source material, indicate what type it is:

| Type | Description | How It's Used |
|------|-------------|---------------|
| **Curriculum document** | Learning objectives, lesson outlines | Direct extraction of structure |
| **Organizational context** | Internal docs, frameworks | Transformed for AI context files |
| **Reference material** | Background reading | Informs content, not used directly |

**Example prompt:**

> "The attached CTX007-ethical-ai-framework.md is an organizational context file—extract relevant principles for the activity configurations."

---

## 7. Hint at Context File Needs

If you know whether an activity needs context files, say so:

- Behavior from **instructions** (be agreeable, play a role) → system prompt only
- Behavior from **knowledge** (organizational context, domain expertise) → context file needed
- Behavior from **guardrails** (anti-sycophancy rules) → context file needed

**Example prompt:**

> "Activity 1 doesn't need context files—sycophantic behavior comes from instructions. Activity 2 needs the ethical framework as a context file since it requires applying those principles."

---

## 8. Specify Roleplay Activities

For persona/simulation activities, provide:
- Character name and role
- Specific behaviors or traits to exhibit
- How traits should emerge (naturally vs. stated upfront)
- What the learner's role is

**Example prompt:**

> "Activity 3 is a roleplay. AI plays 'Jordan,' an Executive Director with red flags: unclear mission, unrealistic AI expectations. Learner plays a consultant assessing fit. Red flags should emerge naturally through questioning, not be stated upfront."

---

## 9. Notice What Emerges During Building

The building process often reveals things the design didn't anticipate. These are valuable — don't absorb them silently.

**What to watch for:**

- **Distinctions that sharpen through implementation.** A curriculum prompt may describe a concept as one thing, but when you write the activity config and facilitator guide, the concept splits into two distinct ideas. The behavioral/context distinction — that HOW the AI responds (behavioral training) is a separate lever from WHAT it knows (context) — emerged during building, not design.

- **Activities that connect across lessons.** If you're building Activity 2 for one lesson and realize it touches the same principle as Activity 1 in a different lesson, note that in the lesson tracker. The designing-leaderspath-courses skill will use this during meta-analysis.

- **Implementation choices that shape the experience.** A system prompt that frames the AI as "a helpful assistant" produces a different learner experience than one that frames it as "an AI with no behavioral training." Both could satisfy the same curriculum prompt, but they teach subtly different things. When you make these choices, note what you chose and what the alternative would have produced.

- **Pacing surprises.** If a 60-minute lesson feels too dense or too thin once you've written the facilitator guide, that's an insight — not just a problem to solve.

**How to surface insights:**

Add an "Emergent Insights" entry to the lesson tracker after completing each lesson:

```markdown
## Emergent Insights: [Lesson ID]
- [What emerged, why it matters, and whether it affects other lessons]
```

These feed directly into the Phase 6 meta-analysis, where the course designer reviews what changed between design and implementation.

---

## Quick Reference Checklist

Before submitting a lesson design, ensure you've included:

**Lesson Level:**
- [ ] Lesson title and description
- [ ] Total duration
- [ ] Learning objectives (lesson-level, not per-activity)
- [ ] Facilitator guide expectations (timing, discussion prompts)
- [ ] Whether Q&A bot is needed

**Per Activity:**
- [ ] What AI behavior learners will experience
- [ ] Whether it's a limitation, capability, or flaw
- [ ] Context file hints (if applicable)
- [ ] Comparison pair flagged (if applicable)
- [ ] Roleplay details (if applicable)

---

## Common Mistakes to Avoid

| Mistake | Better Approach |
|---------|-----------------|
| "Activity 1 teaches about context" | "Activity 1 lets learners experience AI without context; facilitator explains why after" |
| "Include learning objectives in each activity" | "Learning objectives at lesson level only" |
| "The Principle section explains the takeaway" | "Facilitator synthesizes the principle in discussion after activity" |
| "Q&A bot in every activity" | "One Q&A bot at lesson level (if needed), separate from activity sandboxes" |
| "Activity should explain sycophancy" | "Activity demonstrates sycophancy; facilitator explains it" |

---

## Terminology Reference

| Old Term | New Term |
|----------|----------|
| Course (teaching unit) | Lesson |
| Cohort (program) | Course |
| Lesson (pre-2025) | Activity |
| Lesson Plan | Activity Configuration |
| Lesson Text | Activity Instructions |
| `lessons/` folder | `activities/` folder |
| "This lesson demonstrates..." | "This activity lets learners experience..." |
| Facilitator Notes (secondary) | Facilitator Guide (primary, lesson-level) |
| Lesson Objectives | Lesson Learning Objectives |
