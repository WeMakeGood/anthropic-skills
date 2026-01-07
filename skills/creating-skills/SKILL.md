---
name: creating-skills
description: Guides creation of new Agent Skills from prompts, context files, and requirements. Provides foundational knowledge about skill architecture, best practices, and testing procedures. Use when asked to create, build, develop, or convert content into an Agent Skill.
---

# Creating Skills

This skill guides you through creating well-structured Agent Skills from prompts, documentation, or requirements.

## Before You Begin

**You must read the reference documentation before creating any skill:**

1. Read [SPEC.md](SPEC.md) to understand:
   - What skills are and how they differ from prompts
   - The three loading levels (metadata, instructions, resources)
   - Progressive disclosure and why it matters
   - Structure requirements and field limits

2. Read [BEST-PRACTICES.md](BEST-PRACTICES.md) to understand:
   - How to write concise, effective content
   - Setting appropriate freedom levels
   - Writing discoverable descriptions
   - Content patterns and anti-patterns

## Workflow

Copy this checklist and track progress:

```
Skill Creation Progress:
- [ ] Phase 1: Gather requirements
- [ ] Phase 2: Read reference docs (SPEC.md, BEST-PRACTICES.md)
- [ ] Phase 3: Analyze source content
- [ ] Phase 4: Draft the skill
- [ ] Phase 5: Test and validate
- [ ] Phase 6: User review and finalize
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

### Phase 2: Read Reference Documentation

**This step is mandatory.** Do not skip it.

Read the full content of:
- [SPEC.md](SPEC.md) - Understanding skill architecture
- [BEST-PRACTICES.md](BEST-PRACTICES.md) - Writing effective content

Key points to internalize:
- Only add context you (Claude) don't already have
- Description must be third person with trigger conditions
- Keep SKILL.md under 500 lines; use referenced files for more
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
   - Needs detailed reference? → Add REFERENCE.md
   - Multiple domains? → Split by domain
   - Utility operations? → Add scripts/

### Phase 4: Draft the Skill

Create the skill directory:
```
skills/<skill-name>/
├── SKILL.md
└── (additional files as needed)
```

#### Write the Frontmatter

```yaml
---
name: skill-name
description: [Third person. What it does. When to use it. Include keywords.]
---
```

Description requirements:
- Third person ("Processes..." not "I process...")
- States what the skill does
- States when to use it (trigger conditions)
- Includes keywords users might say
- Under 1024 characters

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
[Links to reference files if needed]
```

Writing guidelines:
- Lead with Quick Start (most common case)
- Be concise - you're smart, skip obvious explanations
- Use appropriate freedom level (high/medium/low)
- Include concrete examples with real values
- Link to additional files for detailed content

### Phase 5: Test and Validate

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

### Phase 6: User Review and Finalize

Present the complete skill to the user:
- Show SKILL.md content
- Explain any additional files
- Note any trade-offs or decisions made

Get user approval before committing.

## File Reference

This skill includes:

| File | Purpose |
|------|---------|
| [SPEC.md](SPEC.md) | Agent Skills specification |
| [BEST-PRACTICES.md](BEST-PRACTICES.md) | Writing effective skills |
| [EXAMPLES.md](EXAMPLES.md) | Before/after conversion examples |
| [scripts/validate.py](scripts/validate.py) | Structure validation |
| [scripts/test-description.py](scripts/test-description.py) | Description quality testing |
| [scripts/test-examples.py](scripts/test-examples.py) | Example verification |
| [scripts/dry-run.py](scripts/dry-run.py) | Full loading simulation |

## Common Issues

**"Description too vague"**
→ Add specific trigger conditions: "Use when working with X" or "Use for Y tasks"

**"Examples are abstract"**
→ Replace `[placeholder]` with actual values. Show real input → real output.

**"SKILL.md too long"**
→ Move detailed content to REFERENCE.md or split by domain.

**"Skill doesn't trigger"**
→ Add more keywords to description that match how users phrase requests.

**"Referenced file not found"**
→ Check path is relative to skill directory, uses forward slashes.
