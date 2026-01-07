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

```bash
# Clone the repository
git clone git@github.com:WeMakeGood/anthropic-skills.git
cd anthropic-skills

# Create a new skill from template
./scripts/new-skill.sh my-skill-name

# Edit your skill
# ... modify skills/my-skill-name/SKILL.md ...

# Validate your skill
./scripts/validate-skill.sh skills/my-skill-name
```

## Repository Structure

```
anthropic-skills/
├── skills/              # Published skills
├── templates/           # Skill templates
├── scripts/             # Development tools
│   ├── new-skill.sh     # Create new skill from template
│   └── validate-skill.sh # Validate skill against spec
├── docs/                # Documentation
└── .claude/skills/      # Symlink for local testing
```

## Skill Format

Each skill is a folder with a `SKILL.md` file containing YAML frontmatter:

```yaml
---
name: skill-name
description: Brief description of what the skill does and when to use it.
---

# Skill Name

Instructions for the agent...
```

### Requirements

- **name**: Max 64 characters, lowercase letters/numbers/hyphens only
- **description**: Max 1024 characters, describes capability and trigger conditions
- **SKILL.md body**: Under 500 lines recommended (use additional files for more content)

## Contributing

We welcome contributions! Please see our [contribution guidelines](docs/CONTRIBUTING.md).

### Basic Process

1. Fork the repository
2. Create a skill: `./scripts/new-skill.sh your-skill-name`
3. Develop and test your skill
4. Validate: `./scripts/validate-skill.sh --all`
5. Submit a pull request

### Quality Guidelines

- Write concise instructions (agents are already smart)
- Include concrete examples, not abstract descriptions
- Use third person in descriptions
- Test with multiple Claude models
- Follow the [Agent Skills best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

## Resources

- [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Best Practices Guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Agent Skills Ecosystem](https://agentskills.io)
- [Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)

## License

MIT License - see [LICENSE](LICENSE) for details.
