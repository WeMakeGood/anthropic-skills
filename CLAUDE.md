# Anthropic Skills Library

This repository contains a collection of reusable Agent Skills for Claude and other AI agents that support the Agent Skills standard.

## Repository Structure

```
anthropic-skills/
├── skills/              # Published skills (each skill is a folder with SKILL.md)
├── templates/           # Skill templates for creating new skills
├── scripts/             # Development tooling (validation, scaffolding)
├── docs/                # Documentation and guides
├── .claude/             # Claude Code configuration
│   └── skills/          # Symlink to skills/ for local testing
└── _prompts/            # Local prompts (not tracked in git)
```

## Skill Format

Each skill is a folder containing at minimum a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: skill-name
description: Brief description of what the skill does and when to use it.
---

# Skill Name

Instructions for Claude...
```

### Naming Conventions

- Skill folder names: lowercase with hyphens (e.g., `pdf-processing`)
- Skill names in frontmatter: match folder name exactly
- Use gerund form when possible (e.g., `processing-pdfs`, `analyzing-data`)

### Required Fields

- `name`: Max 64 chars, lowercase letters/numbers/hyphens only
- `description`: Max 1024 chars, describes what the skill does AND when to use it

## Development Workflow

### Creating a New Skill

```bash
# Generate a new skill from template
./scripts/new-skill.sh my-skill-name

# Or manually create
mkdir skills/my-skill-name
cp templates/SKILL.template.md skills/my-skill-name/SKILL.md
```

### Validating Skills

```bash
# Validate a single skill
./scripts/validate-skill.sh skills/my-skill-name

# Validate all skills
./scripts/validate-skill.sh --all
```

### Testing Skills Locally

The `.claude/skills/` directory symlinks to `skills/`, allowing Claude Code to discover and use skills from this repo during development.

## Contributing

1. Fork the repository
2. Create a new skill in `skills/your-skill-name/`
3. Ensure your skill passes validation
4. Submit a pull request

### Contribution Guidelines

- Keep SKILL.md under 500 lines; use additional files for detailed content
- Include concrete examples, not abstract descriptions
- Test with multiple Claude models (Haiku, Sonnet, Opus)
- Follow the naming conventions above
- No time-sensitive information in instructions

## Resources

- [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Agent Skills Ecosystem](https://agentskills.io)
