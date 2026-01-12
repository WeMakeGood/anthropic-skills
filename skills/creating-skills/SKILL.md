---
name: creating-skills
description: Guides creation of new Agent Skills from prompts, context files, and requirements. Provides foundational knowledge about skill architecture, best practices, and testing procedures. Use when asked to create, build, develop, or convert content into an Agent Skill.
---

# Creating Skills

This skill guides you through creating well-structured Agent Skills from prompts, documentation, or requirements.

## Before You Begin

**You must read the reference documentation before creating any skill:**

1. Read [references/SPEC.md](references/SPEC.md) to understand:
   - What skills are and how they differ from prompts
   - The three loading levels (metadata, instructions, resources)
   - Progressive disclosure and why it matters
   - Structure requirements and field limits

2. Read [references/BEST-PRACTICES.md](references/BEST-PRACTICES.md) to understand:
   - How to write concise, effective content
   - Setting appropriate freedom levels
   - Writing discoverable descriptions
   - Content patterns and anti-patterns

## Workflow

Copy this checklist and track progress:

```
Skill Creation Progress:
- [ ] Phase 1: Gather requirements
- [ ] Phase 2: Read reference docs
- [ ] Phase 3: Analyze source content
- [ ] Phase 4: Initialize skill structure
- [ ] Phase 5: Draft the skill
- [ ] Phase 6: Test and validate
- [ ] Phase 7: Package and finalize
```

### Phase 1: Gather Requirements

Ask the user for:

1. **Purpose**: What capability should this skill provide?
2. **Target users**: Who will use this? (developers, writers, analysts, etc.)
3. **Inputs**: What will users provide? (files, data, requests)
4. **Outputs**: What should the skill produce?
5. **Context**: Any existing prompts, docs, or examples to convert?

Request any source materials:
- Existing prompts from `_prompts/` directory
- PDF documentation
- Text files with procedures
- Example inputs and outputs

Propose a skill name (lowercase, hyphens, gerund form preferred):
- `processing-pdfs` not `pdf-processor`
- `analyzing-data` not `data-analysis`
- `generating-reports` not `report-generator`

Name rules:
- 1-64 characters
- Lowercase letters, numbers, and hyphens only
- Cannot start or end with hyphen
- Cannot contain consecutive hyphens (`--`)

### Phase 2: Read Reference Documentation

**This step is mandatory.** Do not skip it.

Read the full content of:
- [references/SPEC.md](references/SPEC.md) - Understanding skill architecture
- [references/BEST-PRACTICES.md](references/BEST-PRACTICES.md) - Writing effective content

Key points to internalize:
- Only add context you (Claude) don't already have
- Description must be third person with trigger conditions
- Keep SKILL.md under 500 lines; use references/ folder for more
- Examples must be concrete, not abstract placeholders

### Phase 3: Analyze Source Content

If converting existing content (prompts, docs):

1. **Identify reusable patterns**
   - Workflows that apply across multiple uses
   - Domain-specific knowledge not in training data
   - Procedures with specific sequences

2. **Identify one-off content to remove**
   - Specific file names or paths
   - Dates or version numbers
   - Context specific to a single use case

3. **Determine structure**
   - Can it fit in under 500 lines? → Single SKILL.md
   - Needs detailed reference? → Add references/REFERENCE.md
   - Multiple domains? → Split into references/ files
   - Utility operations? → Add scripts/

### Phase 4: Initialize Skill Structure

Use the init script to create the standard directory structure:

```bash
python scripts/init_skill.py <skill-name> --path skills
```

This creates:
```
skills/<skill-name>/
├── SKILL.md           # Main instructions (template)
├── references/        # For additional documentation
│   └── REFERENCE.md   # Placeholder reference file
└── scripts/           # For utility scripts
```

### Phase 5: Draft the Skill

#### Write the Frontmatter

```yaml
---
name: skill-name
description: [Third person. What it does. When to use it. Include keywords.]
---
```

Optional frontmatter fields:
- `license`: License terms (e.g., "MIT", "Apache-2.0")
- `compatibility`: Environment prerequisites (max 500 chars)
- `metadata`: Arbitrary key-value pairs
- `allowed-tools`: Pre-approved tools (experimental)

Description requirements:
- Third person ("Processes..." not "I process...")
- States what the skill does
- States when to use it (trigger conditions)
- Includes keywords users might say
- Covers content delivery variations (pasted, attached, uploaded, inline)
- Handles accompanying context files if relevant
- Under 1024 characters
- No angle brackets (< or >)

#### Write the Body

Structure for most skills:

```markdown
# Skill Title

## Quick Start
[Most common use case - get users productive fast]

## Instructions
[Core procedures and workflows]

## Examples
[Concrete input/output pairs - NOT placeholders]

## Additional Resources
[Links to files in references/ folder if needed]
```

Writing guidelines:
- Lead with Quick Start (most common case)
- Be concise - you're smart, skip obvious explanations
- Use appropriate freedom level (high/medium/low)
- Include concrete examples with real values
- Link to references/ files for detailed content
- **For skills producing reports/documents**: Add an Output Requirements section specifying file output vs inline (see BEST-PRACTICES.md)

### Phase 6: Test and Validate

Run all validation scripts in sequence:

#### 1. Structure Validation
```bash
python scripts/validate.py /path/to/new-skill
```
Fix any errors before proceeding.

#### 2. Description Quality
```bash
python scripts/test-description.py /path/to/new-skill "expected trigger phrase"
```
Verify:
- Third-person voice
- Trigger conditions present
- Keywords match expected phrases

#### 3. Example Verification
```bash
python scripts/test-examples.py /path/to/new-skill
```
Ensure:
- Examples section exists
- No placeholder patterns
- Concrete input/output pairs

#### 4. Full Simulation
```bash
python scripts/dry-run.py /path/to/new-skill "test prompt"
```
Review:
- Token estimates are reasonable
- File references exist
- Trigger matching works

#### Validation Loop

```
1. Run validation scripts
2. Review all output
3. If errors or warnings:
   - Fix the issues
   - Return to step 1
4. Only proceed when all tests pass
```

### Phase 7: Package and Finalize

Present the complete skill to the user:
- Show SKILL.md content
- Explain any additional files
- Note any trade-offs or decisions made

Get user approval, then package for distribution:

```bash
python scripts/package_skill.py /path/to/new-skill --output .
```

This creates a zip file ready for:
- Upload to Claude.ai
- Distribution to other users
- Archival

## File Reference

This skill includes:

| File | Purpose |
|------|---------|
| [references/SPEC.md](references/SPEC.md) | Agent Skills specification |
| [references/BEST-PRACTICES.md](references/BEST-PRACTICES.md) | Writing effective skills |
| [references/EXAMPLES.md](references/EXAMPLES.md) | Before/after conversion examples |
| [scripts/init_skill.py](scripts/init_skill.py) | Initialize new skill directory |
| [scripts/validate.py](scripts/validate.py) | Structure validation |
| [scripts/test-description.py](scripts/test-description.py) | Description quality testing |
| [scripts/test-examples.py](scripts/test-examples.py) | Example verification |
| [scripts/dry-run.py](scripts/dry-run.py) | Full loading simulation |
| [scripts/package_skill.py](scripts/package_skill.py) | Package skill for distribution |

## Common Issues

**"Description too vague"**
→ Add specific trigger conditions: "Use when working with X" or "Use for Y tasks"

**"Examples are abstract"**
→ Replace `[placeholder]` with actual values. Show real input → real output.

**"SKILL.md too long"**
→ Move detailed content to references/ folder or split by domain.

**"Skill doesn't trigger"**
→ Add more keywords to description that match how users phrase requests.

**"Referenced file not found"**
→ Check path is relative to skill directory, uses forward slashes.

**"Name validation failed"**
→ Ensure name is lowercase, uses hyphens (not underscores), doesn't start/end with hyphen.
