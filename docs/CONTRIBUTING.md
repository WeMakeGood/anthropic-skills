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

### Step 1: Generate from Template

```bash
./scripts/new-skill.sh your-skill-name
```

This creates `skills/your-skill-name/SKILL.md` with the basic structure.

### Step 2: Write Your Skill

Edit `SKILL.md` following these guidelines:

**Frontmatter Requirements:**
- `name`: Must match folder name, max 64 chars, lowercase/numbers/hyphens only
- `description`: Max 1024 chars, third person, include trigger conditions

**Content Guidelines:**
- Keep SKILL.md under 500 lines
- Write concise instructions (Claude is already smart)
- Include concrete examples, not abstract descriptions
- Use additional files for detailed reference content

### Step 3: Validate

```bash
./scripts/validate-skill.sh skills/your-skill-name
```

Fix any errors before submitting.

### Step 4: Test Locally

The `.claude/skills/` symlink allows you to test skills with Claude Code:

1. Open the repository in your editor with Claude Code
2. Invoke your skill by describing a task that matches its description
3. Verify Claude discovers and uses the skill correctly
4. Test with different prompts and edge cases

### Step 5: Submit a Pull Request

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

- [ ] Passes validation (`./scripts/validate-skill.sh`)
- [ ] Has a clear, specific description in third person
- [ ] Includes concrete examples
- [ ] Is under 500 lines (or uses additional files appropriately)
- [ ] Uses consistent terminology throughout
- [ ] Contains no time-sensitive information
- [ ] Has been tested with Claude

## Skill Writing Best Practices

### Be Concise
Claude is already intelligent. Only include context it doesn't have:
- Domain-specific workflows
- Company/team conventions
- Specialized procedures

### Use Progressive Disclosure
For complex skills, structure as:
1. Main SKILL.md with overview and common cases
2. Linked files for detailed reference (REFERENCE.md, EXAMPLES.md)
3. Scripts for deterministic operations

### Set Appropriate Freedom
- **High freedom**: General guidance when multiple approaches work
- **Low freedom**: Specific scripts when operations are fragile

### Include Feedback Loops
For quality-critical tasks, add validation steps:
```markdown
1. Generate output
2. Run validation: `./scripts/validate.py output.json`
3. If errors, fix and repeat step 2
4. Only proceed when validation passes
```

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
