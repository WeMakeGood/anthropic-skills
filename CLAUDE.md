# Anthropic Skills Library

Open-source collection of Agent Skills for Claude and AI agents supporting the Agent Skills standard.

## Repository Layout

- `skills/` - Published skills (each is a folder with SKILL.md)
- `templates/` - Skill scaffolding templates
- `scripts/` - Validation and generation tools
- `docs/` - Human documentation
- `.claude/skills/` - Symlink to skills/ for local testing
- `_prompts/` - Local prompts to convert (not in git)

## Developing Skills

### Skill Specification

Every skill requires a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: skill-name
description: What it does and when to use it. Write in third person.
---
```

**Field Requirements:**
- `name`: Max 64 chars, lowercase letters/numbers/hyphens only, no reserved words (anthropic, claude)
- `description`: Max 1024 chars, non-empty, third person, include trigger conditions

### Writing Effective Skills

**Be concise.** Claude is already smart. Only add context Claude doesn't have:
- Domain-specific workflows and procedures
- Company/team conventions
- Specialized knowledge or schemas

**Set appropriate freedom:**
- High freedom (text guidance): When multiple approaches work
- Medium freedom (pseudocode/templates): When a preferred pattern exists
- Low freedom (exact scripts): When operations are fragile or must be exact

**Structure for progressive disclosure:**
1. SKILL.md body: Overview and common cases (under 500 lines)
2. Linked files: Detailed reference (REFERENCE.md, EXAMPLES.md, etc.)
3. Scripts: Deterministic operations Claude executes via bash

**Description triggers discovery.** The description is how Claude decides whether to use a skill. Include:
- What the skill does
- When to use it (trigger conditions, keywords)
- Key terms for matching

### Skill Content Patterns

**Quick start pattern** (example structure for a skill's SKILL.md):
```markdown
## Quick Start
[Most common use case with minimal code]

## Detailed Instructions
[Step-by-step for complex cases]

## Reference
See [REFERENCE.md](REFERENCE.md) for complete API details.
```

**Workflow pattern with checklist:**
```markdown
## Workflow

Copy and track progress:
- [ ] Step 1: Analyze input
- [ ] Step 2: Generate output
- [ ] Step 3: Validate result
- [ ] Step 4: Fix errors and repeat step 3
```

**Validation loop pattern** (for skills that include utility scripts):
```markdown
1. Generate output
2. Validate: `python scripts/validate.py output.json`
3. If errors, fix and return to step 2
4. Only proceed when validation passes
```
Note: The script path above is an example. Each skill defines its own scripts as needed.

### Converting Prompts to Skills

When converting a prompt from `_prompts/` to a skill:

1. **Identify the core capability** - What task does this enable?
2. **Extract reusable instructions** - Remove one-off context, keep procedural knowledge
3. **Write a discovery-friendly description** - Third person, includes trigger words
4. **Add concrete examples** - Input/output pairs, not abstract descriptions
5. **Structure for size** - If over 500 lines, split into linked files
6. **Remove time-sensitive content** - No dates, version numbers that will become stale

### File Organization

**Single-file skill** (most common):
```
skills/my-skill/
└── SKILL.md
```

**Multi-file skill** (when content exceeds 500 lines):
```
skills/my-skill/
├── SKILL.md           # Main instructions (under 500 lines)
├── REFERENCE.md       # Detailed API/schema reference (optional)
├── EXAMPLES.md        # Extended examples (optional)
└── scripts/           # Utility scripts (optional)
    └── *.py or *.sh
```

These are example filenames. Use names that describe your skill's content. Keep references one level deep from SKILL.md.

## Development Commands

```bash
# Create new skill from template
./scripts/new-skill.sh skill-name

# Validate a skill
./scripts/validate-skill.sh skills/skill-name

# Validate all skills
./scripts/validate-skill.sh --all
```

## Quality Checklist

Before committing a skill:

- [ ] Name matches folder, lowercase/hyphens only
- [ ] Description is third person with trigger conditions
- [ ] SKILL.md under 500 lines (or properly split)
- [ ] Concrete examples included
- [ ] No time-sensitive information
- [ ] Passes `./scripts/validate-skill.sh`
- [ ] Tested locally via `.claude/skills/` symlink
