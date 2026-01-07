# Best Practices for Writing Skills

This document covers how to write effective skills that Claude can discover and use successfully. Read this before drafting any skill content.

## Core Principle: Be Concise

The context window is a shared resource. Your skill competes for tokens with conversation history, other skills, and the user's request.

**Default assumption:** Claude is already very smart.

Only add context Claude doesn't have:
- Domain-specific workflows and procedures
- Company or team conventions
- Specialized schemas, APIs, or data structures
- Knowledge that isn't in Claude's training data

**Challenge each piece of content:**
- "Does Claude really need this explanation?"
- "Can I assume Claude knows this?"
- "Does this paragraph justify its token cost?"

### Example: Concise vs Verbose

**Good (concise, ~50 tokens):**
```markdown
## Extract PDF Text

Use pdfplumber for text extraction:

```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
```

**Bad (verbose, ~150 tokens):**
```markdown
## Extract PDF Text

PDF (Portable Document Format) files are a common file format that contains
text, images, and other content. To extract text from a PDF, you'll need to
use a library. There are many libraries available for PDF processing, but we
recommend pdfplumber because it's easy to use and handles most cases well.
First, you'll need to install it using pip. Then you can use the code below...
```

The concise version assumes Claude knows what PDFs are and how pip works.

## Setting Freedom Levels

Match instruction specificity to the task's fragility and variability.

### High Freedom (Text Guidance)

Use when multiple approaches are valid and context determines the best path.

```markdown
## Code Review Process

1. Analyze the code structure and organization
2. Check for potential bugs or edge cases
3. Suggest improvements for readability
4. Verify adherence to project conventions
```

Claude decides how to apply these guidelines based on the specific code.

### Medium Freedom (Templates/Pseudocode)

Use when a preferred pattern exists but some variation is acceptable.

```markdown
## Generate Report

Use this template structure, customize as needed:

```python
def generate_report(data, format="markdown"):
    # Process and validate data
    # Generate output in specified format
    # Include summary statistics
```
```

### Low Freedom (Exact Scripts)

Use when operations are fragile, error-prone, or must follow an exact sequence.

```markdown
## Database Migration

Run exactly this command:

```bash
python scripts/migrate.py --verify --backup
```

Do not modify flags or add parameters.
```

### The Bridge Analogy

Think of Claude navigating a path:

- **Narrow bridge with cliffs:** Only one safe way forward. Provide exact instructions, specific scripts, explicit guardrails. Example: database migrations, financial calculations.

- **Open field:** Many paths lead to success. Give general direction and trust Claude to find the best route. Example: code reviews, content writing.

## Writing Effective Descriptions

The description is the most important part of your skill. It determines whether Claude discovers and uses the skill.

### Must Be Third Person

The description is injected into Claude's system prompt. Inconsistent voice causes discovery problems.

```yaml
# Good - third person
description: Extracts text from PDF files and converts to markdown.

# Bad - first person
description: I can help you extract text from PDF files.

# Bad - second person
description: You can use this to extract text from PDF files.
```

### Include What AND When

Describe both the capability and the trigger conditions:

```yaml
# Good - includes triggers
description: Extracts text and tables from PDF files, fills forms, merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.

# Bad - no trigger conditions
description: Processes PDF files.
```

### Include Keywords for Discovery

Think about what users will say when they need this skill:

```yaml
# Good - multiple keywords
description: Analyzes Excel spreadsheets, creates pivot tables, generates charts. Use when analyzing Excel files, spreadsheets, tabular data, .xlsx files, or CSV data.

# Bad - limited keywords
description: Works with Excel.
```

### Good vs Bad Descriptions

| Bad | Good |
|-----|------|
| Helps with documents | Extracts text from PDF files, fills form fields, merges multiple PDFs. Use when working with PDF documents. |
| Processes data | Analyzes CSV and Excel files, generates summary statistics, creates visualizations. Use for data analysis tasks. |
| Code helper | Reviews Python code for bugs, security issues, and style violations. Use when reviewing or improving Python code. |

## Content Patterns

### Quick Start Pattern

Lead with the most common use case:

```markdown
## Quick Start

Extract text from a PDF:

```python
import pdfplumber
with pdfplumber.open("doc.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## Advanced Usage

For form filling, see [FORMS.md](FORMS.md).
For batch processing, see [BATCH.md](BATCH.md).
```

### Workflow Pattern with Checklist

For multi-step processes, provide a checklist Claude can track:

```markdown
## Document Processing Workflow

Copy this checklist and mark items as you complete them:

```
Progress:
- [ ] Step 1: Validate input file
- [ ] Step 2: Extract content
- [ ] Step 3: Transform to target format
- [ ] Step 4: Validate output
- [ ] Step 5: Save results
```

### Step 1: Validate Input
[Instructions...]

### Step 2: Extract Content
[Instructions...]
```

### Validation Loop Pattern

For quality-critical tasks, enforce validation:

```markdown
## Generating Output

1. Create the output file
2. Run validation: `python scripts/validate.py output.json`
3. If validation fails:
   - Review error messages
   - Fix issues in the output
   - Return to step 2
4. Only proceed when validation passes
5. Deliver the validated output
```

### Conditional Workflow Pattern

Guide Claude through decision points:

```markdown
## Document Modification

First, determine the task type:

**Creating new content?**
→ Use the creation workflow in [CREATE.md](CREATE.md)

**Editing existing content?**
→ Use the editing workflow below

## Editing Workflow
1. Load the existing document
2. Parse the structure
3. Apply modifications
4. Validate changes
5. Save the updated document
```

## Progressive Disclosure in Practice

### When to Split into Multiple Files

Split when SKILL.md exceeds 500 lines, or when content is only needed for specific subtasks:

```
my-skill/
├── SKILL.md           # Overview, quick start, common workflows
├── REFERENCE.md       # Detailed API documentation
├── ADVANCED.md        # Complex edge cases
└── scripts/
    └── validate.py    # Validation utility
```

### Organizing by Domain

For skills covering multiple domains, organize to minimize unnecessary loading:

```
data-analysis/
├── SKILL.md
└── schemas/
    ├── finance.md     # Revenue, billing schemas
    ├── sales.md       # Pipeline, opportunities
    └── product.md     # Usage metrics
```

When the user asks about sales data, Claude loads only `schemas/sales.md`.

### Table of Contents for Long Files

For reference files over 100 lines, add a TOC:

```markdown
# API Reference

## Contents
- Authentication
- Core Methods
- Error Handling
- Examples

## Authentication
[Content...]

## Core Methods
[Content...]
```

Claude can scan the TOC and jump to relevant sections.

## Anti-Patterns to Avoid

### Time-Sensitive Information

Don't include dates or version numbers that will become stale:

```markdown
# Bad
If using version 2.3 (released March 2024), use the new API.
After August 2025, the old endpoint will be deprecated.

# Good
Use the v2 API endpoint. See [LEGACY.md](LEGACY.md) for migration from v1.
```

### Windows-Style Paths

Always use forward slashes:

```markdown
# Bad
See templates\form.docx

# Good
See templates/form.docx
```

### Too Many Options

Don't overwhelm with choices:

```markdown
# Bad
You can use pypdf, pdfplumber, PyMuPDF, pdf2image, pdfminer, or camelot...

# Good
Use pdfplumber for text extraction:
[code example]

For scanned PDFs requiring OCR, use pdf2image with pytesseract instead.
```

### Vague Descriptions

Avoid generic language:

```markdown
# Bad
description: Helps with various tasks

# Good
description: Generates commit messages by analyzing git diffs. Use when committing code or reviewing staged changes.
```

### Abstract Examples

Use concrete input/output, not placeholders:

```markdown
# Bad
Input: [your data here]
Output: [processed result]

# Good
Input: {"name": "Alice", "age": 30}
Output: "Name: Alice\nAge: 30 years"
```

## Testing and Iteration

### Test Before Shipping

1. **Validate structure:** Run the validation script
2. **Test description:** Does it trigger for expected phrases?
3. **Test examples:** Are they concrete and runnable?
4. **Dry run:** Simulate the full loading flow

### Test with Multiple Models

Skills may behave differently across models:
- **Haiku:** Needs more explicit guidance
- **Sonnet:** Balanced performance
- **Opus:** May need less hand-holding

Write instructions that work across all models you'll use.

### Iterate Based on Usage

After deploying a skill:
1. Observe how Claude navigates it
2. Note where it struggles or misses content
3. Refine based on actual behavior, not assumptions
