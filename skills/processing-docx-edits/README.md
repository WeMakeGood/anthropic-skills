# Processing DOCX Edits

Processes Word documents containing tracked changes and comments, synthesizes all edits, and produces clean final documents.

## What It Does

When you have a DOCX file that's been through review cycles with tracked changes and comments, this skill:

1. **Extracts** all tracked changes (insertions/deletions) and comments with their positions
2. **Analyzes** the full document to understand how changes relate to each other
3. **Synthesizes** edits into a clear summary, identifying conflicts or questions
4. **Presents** findings and waits for your approval before making changes
5. **Applies** approved edits and outputs a clean final document

## Use Cases

- Processing stakeholder feedback on documents
- Merging edits from multiple reviewers
- Resolving conflicting feedback
- Creating clean versions from marked-up drafts

## How to Use

### Claude Code

```
Process the edits in path/to/document.docx
```

### Claude.ai

Attach the DOCX file and say:
```
Process this document to integrate all tracked changes and comments
```

## What's Included

| File | Purpose |
|------|---------|
| `SKILL.md` | Main skill instructions |
| `scripts/extract_docx.py` | Extracts tracked changes, comments, and content from DOCX files |

## Output

- Final document saved to `./tmp/[original-name]-final.md`
- Summary of changes applied
- Any issues or decisions made during processing

## Requirements

- Python 3.x (uses standard library only: zipfile, xml.etree)
- No external packages required
