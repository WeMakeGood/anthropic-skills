---
name: creating-skills
description: Guides creation of new Agent Skills from prompts, context files, and requirements. Provides foundational knowledge about skill architecture, best practices, and testing procedures. Use when asked to create, build, develop, or convert content into an Agent Skill.
---

# Creating Skills

This skill guides you through creating well-structured Agent Skills from prompts, documentation, or requirements.

## Critical Rules for All Skills

Every skill you create MUST include behavioral guardrails. These are non-negotiable.

**ANTI-HALLUCINATION:** Skills must ground Claude's responses in provided information. Include explicit instructions about:
- What sources Claude can use
- How to mark inferences vs confirmed facts
- When to acknowledge uncertainty
- Requirements to cite sources

**ANTI-SYCOPHANCY:** Skills must encourage honest, objective responses. Include explicit instructions about:
- When to challenge user assumptions
- How to surface problems or concerns
- Prioritizing accuracy over agreeability
- Reporting issues rather than sanitizing them

**INSTRUCTION ADHERENCE:** Skills must use strong, unambiguous language. Include:
- **REQUIRED/CRITICAL/STOP** markers for mandatory actions
- Explicit verification checkpoints
- Clear "do not proceed until X" gates
- Consequences of skipping steps

**NATURAL PROSE:** Skills producing external-facing content (marketing, website copy, case studies) must avoid AI-detectable writing patterns. Include explicit bans on AI vocabulary, formulaic structures, and promotional language (see BEST-PRACTICES.md).

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

## Critical Rules
[REQUIRED: Anti-hallucination, anti-sycophancy, and adherence rules specific to this skill]

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
- **ALWAYS include a Critical Rules section** with skill-specific behavioral guardrails
- Lead with Quick Start (most common case)
- Be concise - you're smart, skip obvious explanations
- Use appropriate freedom level (high/medium/low)
- Include concrete examples with real values
- Link to references/ files for detailed content
- **For skills producing reports/documents**: Add an Output Requirements section specifying file output vs inline (see BEST-PRACTICES.md)

#### Critical Rules Section (REQUIRED)

Every skill MUST have a Critical Rules section near the top. Include rules relevant to the skill:

**Anti-Hallucination Rules (always include for content-generating skills):**
```markdown
**GROUNDING:** Base all content ONLY on [source type]. Never invent [specific items].

**EPISTEMIC MARKERS:** Use "[Source: X]" for facts, "[Inferred]" for reasonable inferences, "[Unverified]" for claims you cannot confirm.
```

**Anti-Sycophancy Rules (always include for advisory/analytical skills):**
```markdown
**PROFESSIONAL OBJECTIVITY:** If you identify problems, concerns, or issues with [user's input/approach/content], report them directly. Do not omit negative findings to be agreeable.
```

**Instruction Adherence Rules (always include for multi-step workflows):**
```markdown
**REQUIRED/CRITICAL/STOP** — Use these markers for mandatory actions
**VERIFICATION** — "Before proceeding, verify X"
**CHECKPOINT** — "Do not proceed until user confirms"
```

### Phase 6: Test and Validate

Testing happens in two stages: **structural validation** (automated scripts) and **functional testing** (parallel session testing with real prompts).

#### Stage 1: Structural Validation

Run all validation scripts in sequence:

**1. Structure Validation**
```bash
python scripts/validate.py /path/to/new-skill
```
Fix any errors before proceeding.

**2. Description Quality**
```bash
python scripts/test-description.py /path/to/new-skill "expected trigger phrase"
```
Verify:
- Third-person voice
- Trigger conditions present
- Keywords match expected phrases

**3. Example Verification**
```bash
python scripts/test-examples.py /path/to/new-skill
```
Ensure:
- Examples section exists
- No placeholder patterns
- Concrete input/output pairs

**4. Full Simulation**
```bash
python scripts/dry-run.py /path/to/new-skill "test prompt"
```
Review:
- Token estimates are reasonable
- File references exist
- Trigger matching works

#### Stage 2: Functional Testing (Parallel Sessions)

Structural validation checks that the skill is well-formed. Functional testing checks that it **produces quality output**.

**The process:**

1. **Create test prompts** — Design 2-3 prompts that exercise the skill:
   - Simple case: The most common use case
   - Complex case: Edge cases, multiple inputs, or advanced features
   - Boundary case: Ambiguous inputs that test decision-making

2. **Run in parallel session** — Open a separate Claude session and run the skill with your test prompts. Keep the skill-building session open.

3. **Review output** — In the skill-building session, read and audit the output:
   - Did the skill follow the workflow correctly?
   - Is the output quality acceptable?
   - Were decisions documented appropriately?
   - What's missing or could be improved?

4. **Iterate** — Based on findings, update the skill and re-test:
   ```
   Test → Review → Fix → Re-test
   ```

5. **Document test results** — Note what was tested and what changes were made.

**Test prompt design tips:**

| Test Type | What It Validates | Example |
|-----------|-------------------|---------|
| Simple | Basic workflow executes correctly | Single input, happy path |
| Complex | Multi-step workflows, edge cases | Multiple inputs, dependencies |
| Boundary | Decision-making under ambiguity | Incomplete info, unclear requirements |

**What to look for during review:**

- Did the skill ask for clarification when needed?
- Did it follow checkpoints and get approval?
- Is the output format correct?
- Are decisions documented appropriately?
- Did it handle edge cases gracefully?
- What guidance would have prevented any issues?

See [references/BEST-PRACTICES.md](references/BEST-PRACTICES.md) for detailed functional testing methodology.

#### Validation Loop

```
1. Run structural validation scripts
2. Fix any errors
3. Run functional tests in parallel session
4. Review output in skill-building session
5. If issues found:
   - Update skill
   - Return to step 1
6. Only proceed when both stages pass
```

### Phase 7: Package and Finalize

Present the complete skill to the user:
- Show SKILL.md content
- Explain any additional files
- Note any trade-offs or decisions made

Get user approval, then package for distribution:

```bash
python scripts/package_skill.py /path/to/new-skill --output dist
```

This creates a zip file ready for:
- Upload to Claude.ai (Settings > Features > Skills)
- Distribution to other users
- Extraction to `~/.claude/skills/` for local use

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
