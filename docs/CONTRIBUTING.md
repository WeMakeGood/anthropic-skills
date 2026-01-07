# Contributing to Anthropic Skills Library

Thank you for your interest in contributing to the Anthropic Skills Library! This guide will help you get started.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone git@github.com:YOUR-USERNAME/anthropic-skills.git
   cd anthropic-skills
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b add-my-skill
   ```

## Creating a New Skill

### Option 1: Use the Creating-Skills Skill (Recommended)

The easiest way to create a skill is to use the `creating-skills` skill:

1. Open the repository in Claude Code
2. Ask: "Help me create a new agent skill"
3. Follow the guided workflow
4. The skill will read the spec, best practices, and guide you through creation

### Option 2: Create Manually

```bash
# Create skill directory
mkdir skills/your-skill-name

# Copy template
cp templates/SKILL.template.md skills/your-skill-name/SKILL.md

# Edit the skill
# ... modify skills/your-skill-name/SKILL.md ...
```

### Writing Your Skill

**Frontmatter Requirements:**
- `name`: Must match folder name, max 64 chars, lowercase/numbers/hyphens only
- `description`: Max 1024 chars, third person, include trigger conditions

**Content Guidelines:**
- Keep SKILL.md under 500 lines
- Write concise instructions (Claude is already smart)
- Include concrete examples, not abstract descriptions
- Use additional files for detailed reference content

### Validate Your Skill

Use the validation scripts in `skills/creating-skills/scripts/`:

```bash
# Structure validation
python3 skills/creating-skills/scripts/validate.py skills/your-skill-name

# Description quality
python3 skills/creating-skills/scripts/test-description.py skills/your-skill-name "expected trigger phrase"

# Example verification
python3 skills/creating-skills/scripts/test-examples.py skills/your-skill-name

# Full simulation
python3 skills/creating-skills/scripts/dry-run.py skills/your-skill-name "test prompt"
```

Fix any errors before submitting.

### Test Locally

The `.claude/skills/` symlink allows you to test skills with Claude Code:

1. Open the repository in your editor with Claude Code
2. Invoke your skill by describing a task that matches its description
3. Verify Claude discovers and uses the skill correctly
4. Test with different prompts and edge cases

### Submit a Pull Request

1. Commit your changes:
   ```bash
   git add skills/your-skill-name
   git commit -m "Add your-skill-name skill"
   ```
2. Push to your fork:
   ```bash
   git push origin add-my-skill
   ```
3. Open a Pull Request on GitHub

## Quality Checklist

Before submitting, ensure your skill:

- [ ] Passes all validation scripts
- [ ] Has a clear, specific description in third person
- [ ] Includes trigger conditions in description
- [ ] Includes concrete examples (not placeholders)
- [ ] Is under 500 lines (or uses additional files appropriately)
- [ ] Uses consistent terminology throughout
- [ ] Contains no time-sensitive information
- [ ] Has been tested with Claude Code

## Skill Writing Best Practices

For detailed guidance, see:
- `skills/creating-skills/SPEC.md` - How skills work
- `skills/creating-skills/BEST-PRACTICES.md` - Writing guidelines
- `skills/creating-skills/EXAMPLES.md` - Conversion examples

### Key Principles

**Be Concise**
Claude is already intelligent. Only include context it doesn't have:
- Domain-specific workflows
- Company/team conventions
- Specialized procedures

**Use Progressive Disclosure**
For complex skills, structure as:
1. Main SKILL.md with overview and common cases
2. Linked files for detailed reference (REFERENCE.md, EXAMPLES.md)
3. Scripts for deterministic operations

**Set Appropriate Freedom**
- **High freedom**: General guidance when multiple approaches work
- **Low freedom**: Specific scripts when operations are fragile

**Include Feedback Loops**
For quality-critical tasks, add validation steps in your skill's workflow.

## Code of Conduct

- Be respectful and constructive in discussions
- Focus on improving the library for everyone
- Credit original sources when adapting existing work
- Report security concerns privately to maintainers

## Questions?

Open an issue on GitHub for:
- Questions about skill design
- Feature requests
- Bug reports
- General discussion

Thank you for contributing!
