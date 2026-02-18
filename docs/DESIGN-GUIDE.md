# Skill Design Guide

This guide covers the thinking behind how skills in this library are designed. It's the "why" and "what" companion to [CONTRIBUTING.md](CONTRIBUTING.md), which covers the "how."

Read this before designing a new skill. It will help you make better decisions about scope, structure, and purpose.

---

## Start from the User Need

Every skill in this library starts from a question: **what does the user need to accomplish?**

The wrong starting point is "we have a prompt that does X" or "we use tool Y internally." Internal workflows and existing prompts are useful inputs, but they shouldn't dictate skill boundaries. A skill should be designed for general utility — not as a wrapper around a specific tool or process.

**Ask:** "What organizational problem does this solve?" If the answer is vague or internal-only, the skill isn't ready.

**Examples:**
- "Nonprofits need to document their impact" → case study writing skill
- "We need to process Word documents with track changes" → document processing skill
- "We have a WSForm prompt" → not a skill (too platform-specific)

---

## One Skill, One Purpose

Each skill does one thing well. It has clear boundaries — defined inputs, defined outputs, and a single coherent job.

A skill that synthesizes interviews should not also write the article. A skill that writes articles should not also do the research. Users can chain skills together for complex workflows, but each skill is independently useful and independently testable.

**Why this matters:**
- Focused skills are easier to test and validate
- Users understand what they'll get
- Skills can be improved without breaking adjacent functionality
- New combinations become possible without rebuilding

**The test:** Can you describe what the skill does in one sentence without using "and"? If not, it might be two skills.

---

## Design for Context

Skills in this library are designed to work with organizational context libraries — structured collections of organizational knowledge (voice guidelines, mission, audience profiles, terminology) that make AI output specific to an organization.

When designing a skill:
- **Identify what organizational knowledge would improve the output.** Voice guidelines? Mission and values? Audience profiles? These are the skill's context touchpoints.
- **Don't embed organizational knowledge in the skill.** The skill defines the process; the context library supplies the specifics.
- **Make the skill useful without context too.** Output will be more generic, but the skill should still produce a reasonable result. Context enhances — it shouldn't be a hard dependency.

The core equation: `Skill (universal process) + Context (organizational knowledge) = Personalized output`

---

## What Not to Build

The library stays focused by excluding certain categories:

### No Platform-Specific Skills

Skills that depend on a specific platform (a particular form builder, CRM, project management tool) are too narrow and change too frequently. Platform integrations are better handled as custom work for specific implementations.

**Exception:** If a platform is so widely used that the skill serves broad utility (e.g., generating import files for a common project management format), it may be appropriate. Use judgment.

### No Redundant Skills

Each user need should be served by one skill. If two skills overlap significantly in purpose, they should be combined or one should be retired. Before building a new skill, check whether an existing skill already covers the need — possibly under a different name or framing.

### No Speculative Skills

Don't build skills for hypothetical future needs. Build based on demonstrated demand — real users who need to accomplish real tasks. The extended tier of the library exists specifically for skills that wait for demand before being built.

---

## Skill Scope and Complexity

### Keep Instructions Concise

Claude is already intelligent. Skills should provide what the agent doesn't already know:
- Domain-specific workflows and decision points
- Organizational conventions and standards
- Quality criteria specific to this type of output
- Structural requirements for deliverables

Don't explain how to write well, how to organize information, or how to think through a problem. The agent already knows how to do those things. Focus on what makes *this specific process* different from general capability.

### Use Progressive Disclosure

For complex skills:
1. **SKILL.md** — The main workflow. Overview, common cases, the core process. Under 500 lines.
2. **references/** — Detailed reference material the skill can consult. Specifications, examples, domain knowledge.
3. **scripts/** — Deterministic operations that shouldn't be left to LLM judgment (validation, file generation, calculations).

The skill reads SKILL.md first and pulls in references as needed. Don't front-load everything — let the agent access detail when the workflow calls for it.

### Set Appropriate Freedom

Not every step needs the same level of prescription:
- **High freedom** — When multiple approaches work and the agent's judgment is reliable. Provide guidance, not scripts.
- **Low freedom** — When operations are fragile, order-dependent, or produce artifacts that must match a spec. Provide explicit steps or use scripts.

Most skills are a mix. Creative/analytical work benefits from high freedom. Structural/mechanical work benefits from low freedom.

---

## The LeadersPath Connection

Many skills in this library serve double duty: they're useful for daily organizational work *and* they create hands-on learning experiences in LeadersPath courses.

When designing a skill, consider:
- **Could this skill be used in a comparison activity?** (Same skill, with and without context, to demonstrate the value of organizational context)
- **Does this skill produce output that's immediately recognizable as better or worse?** (Skills that produce visibly different output with context make stronger teaching tools)
- **Is this skill accessible to non-technical users?** (LeadersPath participants range from executive directors to program staff)

You don't need to design for LeadersPath specifically — a well-designed skill naturally works as a teaching tool. But awareness of this connection helps inform design decisions.

---

## Quality Indicators

Before considering a skill complete:

**Does it solve a real problem?** Someone should be able to describe a concrete situation where this skill helps.

**Is the scope clear?** A user should know what they'll get — and what they won't get — before invoking the skill.

**Does it work without context?** The output should be reasonable (if generic) without a context library loaded.

**Does it improve with context?** The output should be noticeably better — more specific, more aligned, more useful — when organizational context is available.

**Are examples concrete?** Not "provide your input" but actual sample inputs and what the output looks like. Real examples, not placeholders.

**Has it been tested?** Validated with the repo's testing scripts, tested with at least one real context library, edge cases identified.

---

## Further Reading

- [CONTRIBUTING.md](CONTRIBUTING.md) — How to create, validate, and submit skills
- [creating-skills](../skills/creating-skills/) — The skill that guides skill creation, including the full specification and best practices
- [Agent Skills Specification](https://agentskills.io/specification) — The standard that skills conform to
