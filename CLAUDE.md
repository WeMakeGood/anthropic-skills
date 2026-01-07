# Anthropic Skills Library

Open-source collection of Agent Skills for Claude and AI agents supporting the Agent Skills standard.

## Repository Layout

- `skills/` - Published skills (each is a folder with SKILL.md)
- `templates/` - Skill scaffolding templates
- `docs/` - Human documentation
- `.claude/skills/` - Symlink to skills/ for local testing
- `_prompts/` - Local prompts to convert (not in git)

## Creating New Skills

**Use the `creating-skills` skill.** It provides:
- Complete specification of how skills work
- Best practices for writing effective skills
- Validation and testing scripts
- Step-by-step workflow

To create a new skill:

1. Invoke the creating-skills skill: "Help me create a new agent skill"
2. Follow the guided workflow
3. Provide your requirements and source content
4. Review and test the generated skill

The skill is located at `skills/creating-skills/` and includes:
- `SKILL.md` - Main workflow
- `references/SPEC.md` - What skills are, how they work
- `references/BEST-PRACTICES.md` - Writing guidelines
- `references/EXAMPLES.md` - Before/after conversion examples
- `scripts/` - Validation, testing, init, and packaging tools

## Quick Reference

### Skill Structure

Every skill requires a `SKILL.md` with YAML frontmatter:

```yaml
---
name: skill-name
description: What it does and when to use it. Third person. Include triggers.
---

# Skill Title

[Instructions...]
```

Standard directory layout:
```
skill-name/
├── SKILL.md           # Required - main instructions
├── references/        # Optional - additional documentation
└── scripts/           # Optional - utility scripts
```

**Field Requirements:**
- `name`: 1-64 chars, lowercase/numbers/hyphens, cannot start/end with hyphen, no consecutive hyphens
- `description`: 1-1024 chars, no angle brackets, third person, includes trigger conditions
- Body: Under 500 lines (split into references/ if larger)

### Scripts

Use the scripts in `skills/creating-skills/scripts/`:

```bash
# Initialize new skill
python3 skills/creating-skills/scripts/init_skill.py my-skill-name --path skills

# Validate structure
python3 skills/creating-skills/scripts/validate.py skills/your-skill

# Test description quality
python3 skills/creating-skills/scripts/test-description.py skills/your-skill "trigger phrase"

# Test examples
python3 skills/creating-skills/scripts/test-examples.py skills/your-skill

# Full simulation
python3 skills/creating-skills/scripts/dry-run.py skills/your-skill "test prompt"

# Package for distribution
python3 skills/creating-skills/scripts/package_skill.py skills/your-skill --output .
```

### Quality Checklist

Before committing:

- [ ] Name matches folder, lowercase/hyphens only, no consecutive hyphens
- [ ] Name doesn't start or end with hyphen
- [ ] Description is third person with trigger conditions
- [ ] Description contains no angle brackets
- [ ] SKILL.md under 500 lines (or properly split into references/)
- [ ] Concrete examples included (not placeholders)
- [ ] No time-sensitive information
- [ ] All validation scripts pass
- [ ] Tested locally via `.claude/skills/` symlink
