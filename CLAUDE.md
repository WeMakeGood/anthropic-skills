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
- `SPEC.md` - What skills are, how they work
- `BEST-PRACTICES.md` - Writing guidelines
- `EXAMPLES.md` - Before/after conversion examples
- `scripts/` - Validation and testing tools

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

**Requirements:**
- `name`: Max 64 chars, lowercase/numbers/hyphens, no reserved words
- `description`: Max 1024 chars, third person, includes trigger conditions
- Body: Under 500 lines (split into files if larger)

### Validation

Use the scripts in `skills/creating-skills/scripts/`:

```bash
# Validate structure
python3 skills/creating-skills/scripts/validate.py skills/your-skill

# Test description quality
python3 skills/creating-skills/scripts/test-description.py skills/your-skill "trigger phrase"

# Test examples
python3 skills/creating-skills/scripts/test-examples.py skills/your-skill

# Full simulation
python3 skills/creating-skills/scripts/dry-run.py skills/your-skill "test prompt"
```

### Quality Checklist

Before committing:

- [ ] Name matches folder, lowercase/hyphens only
- [ ] Description is third person with trigger conditions
- [ ] SKILL.md under 500 lines (or properly split)
- [ ] Concrete examples included (not placeholders)
- [ ] No time-sensitive information
- [ ] All validation scripts pass
- [ ] Tested locally via `.claude/skills/` symlink
