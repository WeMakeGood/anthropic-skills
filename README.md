# Anthropic Skills Library

An open-source collection of [Agent Skills](https://agentskills.io) for Claude and other AI agents that support the Agent Skills standard.

## What Are Agent Skills?

Agent Skills are modular capabilities that extend AI agent functionality. Each skill packages instructions, metadata, and optional resources (scripts, templates) that agents use automatically when relevant. Skills enable:

- **Specialization**: Tailor agent capabilities for domain-specific tasks
- **Reusability**: Create once, use automatically across conversations
- **Composability**: Combine skills to build complex workflows

## Quick Start

### Using Skills

Skills in this library can be used with:

- **Claude Code**: Copy skill folders to `~/.claude/skills/` or `.claude/skills/` in your project
- **Claude API**: Upload via the `/v1/skills` endpoints
- **Claude.ai**: Upload as zip files through Settings > Features
- **Claude Agent SDK**: Place in `.claude/skills/` directory

### Creating Skills

The easiest way to create a new skill is to use the `creating-skills` skill included in this repo:

1. Open this repository in Claude Code
2. Ask: "Help me create a new agent skill"
3. Follow the guided workflow

Or manually:

```bash
# Clone the repository
git clone git@github.com:WeMakeGood/anthropic-skills.git
cd anthropic-skills

# Create skill directory
mkdir skills/my-skill-name

# Copy template
cp templates/SKILL.template.md skills/my-skill-name/SKILL.md

# Edit your skill
# ... modify skills/my-skill-name/SKILL.md ...

# Validate
python3 skills/creating-skills/scripts/validate.py skills/my-skill-name
```

## Repository Structure

```
anthropic-skills/
├── skills/                    # Published skills
│   └── creating-skills/       # Skill for creating new skills
│       ├── SKILL.md           # Main workflow
│       ├── SPEC.md            # Agent Skills specification
│       ├── BEST-PRACTICES.md  # Writing guidelines
│       ├── EXAMPLES.md        # Conversion examples
│       └── scripts/           # Validation tools
├── templates/                 # Skill templates
├── docs/                      # Documentation
└── .claude/skills/            # Symlink for local testing
```

## Skill Format

Each skill is a folder with a `SKILL.md` file containing YAML frontmatter:

```yaml
---
name: skill-name
description: Brief description of what the skill does and when to use it. Third person.
---

# Skill Name

Instructions for the agent...
```

### Requirements

- **name**: Max 64 characters, lowercase letters/numbers/hyphens only
- **description**: Max 1024 characters, third person, includes trigger conditions
- **SKILL.md body**: Under 500 lines recommended (use additional files for more content)

## Contributing

We welcome contributions! Please see our [contribution guidelines](docs/CONTRIBUTING.md).

### Basic Process

1. Fork the repository
2. Use the `creating-skills` skill or create manually
3. Develop and test your skill
4. Validate: `python3 skills/creating-skills/scripts/validate.py skills/your-skill`
5. Submit a pull request

### Quality Guidelines

- Write concise instructions (agents are already smart)
- Include concrete examples, not abstract descriptions
- Use third person in descriptions
- Include trigger conditions in descriptions
- Test with the validation scripts

## Resources

- [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Best Practices Guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Agent Skills Ecosystem](https://agentskills.io)
- [Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)

## License

MIT License - see [LICENSE](LICENSE) for details.
