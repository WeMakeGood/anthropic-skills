# Activity Template

This template defines the structure for Activity configuration and instructions. Activities are AI sandbox experiments within a facilitated lesson—they guide hands-on experimentation, not conceptual teaching.

---

## Activity Naming

Activity folders use the naming convention: `TOPIC-LEVEL-ACT-slug`

- **TOPIC-LEVEL:** Matches the parent lesson (e.g., `FUND-101`)
- **ACT:** Literal string indicating this is an activity
- **slug:** Kebab-case activity name (e.g., `starting-from-zero`)

**Example:** Lesson `FUND-101-ai-basics` with activity "Starting from Zero" → `FUND-101-ACT-starting-from-zero`

See [NAMING-SYSTEM.md](NAMING-SYSTEM.md) for complete naming conventions.

---

## Activity Folder Structure

```
activities/TOPIC-LEVEL-ACT-slug/
├── configuration/
│   ├── system-prompt.md      # AI sandbox configuration
│   ├── api-settings.md       # Model, tokens, temperature
│   └── context-files.md      # What context to load
└── instructions.md           # Learner-facing "try this" guidance
```

---

## Instructions Template (`instructions.md`)

```markdown
# Activity: [Activity Name]

## What You'll Experience
[One sentence describing the AI configuration and expected behavior]

## Try This
1. [Specific prompt to try]
2. [Specific prompt to try]
3. [Variation or follow-up]

## What to Notice
- [Observable behavior 1]
- [Observable behavior 2]
- [Observable behavior 3]

## Duration
[X] minutes
```

### Guidelines for Instructions

**DO:**
- Be specific about what to type/try
- Direct attention to observable behaviors
- Keep the "What You'll Experience" to one sentence
- Include 3-5 specific prompts to try

**DON'T:**
- Teach concepts (facilitator does that)
- Include learning objectives (those are at lesson level)
- Explain "The Principle" (facilitator synthesizes after)
- Write lengthy explanations or background

---

## Configuration Templates

### System Prompt (`configuration/system-prompt.md`)

```markdown
[Complete system prompt content]

[This is the exact text that configures the AI sandbox behavior.
It should be ready to paste into the chatbot_system_prompt field.]
```

**System prompt patterns:**
- **Bare/Minimal:** Just "helpful assistant" for baseline demos
- **Role-Constrained:** Specific role but no context
- **Context-Rich:** Full context library loaded
- **Deliberately Flawed:** Sycophantic or limited for contrast
- **Roleplay:** Character persona with hidden complexity

See [CONTENT-GUIDES.md](CONTENT-GUIDES.md) for detailed patterns and examples.

### API Settings (`configuration/api-settings.md`)

```markdown
# API Settings

## Model Configuration
- Model: [sonnet / haiku / opus-4.5]
- Max Tokens: [number, typically 4096]
- Temperature: [0-1, typically 0.7]

## Context Files
- [shared-context/filename.md] — [brief description]
- [Or "None" if no context files]

## Skills
- [skill-name] — [brief description]
- [Or "None" if no skills]
```

**Model selection guidance:**

| Activity Type | Recommended Model |
|---------------|-------------------|
| Standard experiential | Sonnet |
| Complex reasoning | Opus 4.5 |
| Quick demonstrations | Haiku |
| Roleplay/persona | Sonnet or Opus |

**Temperature guidance:**

| Activity Type | Temperature |
|---------------|-------------|
| Standard activities | 0.7 |
| Roleplay/persona | 0.7-0.9 |
| Task-constrained | 0.5-0.7 |

### Context Files Reference (`configuration/context-files.md`)

```markdown
# Context Files for Activity: [Activity Name]

## Course-Level Context
- [shared-context/filename.md] — [why this activity needs it]

## Activity-Specific Context
- [None, or list files unique to this activity]

## Notes
[Any special considerations about context loading]
```

---

## Example: Complete Activity

**Activity: Starting from Zero** (in lesson FUND-101-ai-basics)

**Folder structure:**
```
activities/FUND-101-ACT-starting-from-zero/
├── configuration/
│   ├── system-prompt.md
│   ├── api-settings.md
│   └── context-files.md
└── instructions.md
```

**instructions.md:**
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

**configuration/system-prompt.md:**
```markdown
You are a helpful AI assistant.

Respond to user questions to the best of your ability. Be friendly and informative.
```

**configuration/api-settings.md:**
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

**configuration/context-files.md:**
```markdown
# Context Files for Activity: Starting from Zero

## Course-Level Context
None

## Activity-Specific Context
None — this activity deliberately uses no context files to demonstrate baseline AI behavior.

## Notes
The absence of context files is intentional. This activity shows what AI produces without organizational knowledge.
```

---

## Key Reminders

1. **Activities are experiments, not lessons.** The facilitator teaches; the sandbox demonstrates.

2. **No learning objectives in activities.** Objectives live at lesson level.

3. **No "The Principle" section.** The facilitator synthesizes meaning after the activity.

4. **Keep instructions focused.** 50-100 words total is ideal.

5. **Test your configuration.** Make sure the AI actually behaves as intended before finalizing.
