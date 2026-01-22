# Validation Guide

## Pre-Build Checklist

Before building modules:

- [ ] Read ALL source documents
- [ ] Created proposal with module structure
- [ ] Identified information gaps
- [ ] Got user approval on proposal

## Module Quality Checklist

For each module:

- [ ] Has correct YAML frontmatter (module_id, name, tier, purpose, confidence, last_updated)
- [ ] Purpose clearly states what question it answers
- [ ] Scope defines what's included AND excluded
- [ ] No information duplicated from other modules
- [ ] All cross-references use explicit format
- [ ] Confidence markers on all factual claims
- [ ] High-stakes content marked with `[HIGH-STAKES]` and has source citations
- [ ] Agent instructions section included

## Cross-Reference Validation

Run: `python scripts/validate_library.py ./library`

Check for:
- References to non-existent modules
- References to sections that don't exist
- Circular reference chains
- Orphaned modules (no agent loads them)

## Token Budget Validation

Run: `python scripts/count_tokens.py ./library ./agents`

For each agent, verify:
- Total tokens under 20,000
- At least 20% buffer remaining (under 16,000 preferred)
- Foundation modules not over-weighted

If over budget:
1. Check for verbose explanations (trim)
2. Check for duplicated content (consolidate)
3. Consider splitting large modules
4. Review if agent needs all assigned modules

## Common Issues

### Duplicated Information

**Symptom**: Same fact appears in multiple modules
**Fix**: Keep in ONE module, add references in others

### Missing Confidence Markers

**Symptom**: Facts without [CONFIRMED], [PROPOSED], or [HISTORICAL]
**Fix**: Add markers; if uncertain, mark [PROPOSED]

### Vague Cross-References

**Symptom**: "See other modules for details"
**Fix**: Specific reference: "See [Module Name] for [specific info]"

### Over-Explanation

**Symptom**: Explaining concepts Claude already knows
**Fix**: Remove general explanations, keep org-specific info only

### Missing Agent Instructions

**Symptom**: Module has content but no guidance on how to use it
**Fix**: Add "Agent Instructions" section with application guidance

### Unmarked High-Stakes Content

**Symptom**: Legal, financial, or third-party claims without `[HIGH-STAKES]` marker
**Fix**: Add marker and ensure source citation exists

### Missing Verification Guidance

**Symptom**: Agent definition has no "Verification & Professional Objectivity" section
**Fix**: Add section with stakes-based verification behaviors and objectivity guidelines

## Final Validation Checklist

Before declaring complete:

- [ ] All modules pass quality checklist
- [ ] No broken cross-references
- [ ] No duplicated information
- [ ] All agents under token budget
- [ ] All BLOCKING gaps resolved or user-approved
- [ ] High-stakes content properly marked and sourced
- [ ] Agent definitions include verification and objectivity guidance
- [ ] User approved final library

## Validation Report Template

```markdown
# Validation Report

**Date**: YYYY-MM-DD
**Library**: [Name]

## Summary

- Total modules: [X]
- Total agents: [X]
- Issues found: [X]
- Status: [PASS/NEEDS FIXES]

## Token Budgets

| Agent | Tokens | % of Limit | Status |
|-------|--------|------------|--------|
| [Agent] | [X] | [X]% | OK/OVER |

## Cross-Reference Check

- [ ] All references valid
- Issues: [List any]

## Duplication Check

- [ ] No duplicated content
- Issues: [List any]

## Confidence Audit

- [ ] All facts marked
- Unmarked items: [List any]

## Stakes Classification Audit

- [ ] High-stakes content identified and marked
- [ ] High-stakes items have source citations
- [ ] Agent definitions include stakes-based verification guidance
- Issues: [List any unmarked high-stakes content]

## Agent Objectivity Check

- [ ] Each agent has "Verification & Professional Objectivity" section
- [ ] Challenge/verify/flag behaviors defined
- [ ] Uncertainty handling specified
- Issues: [List any gaps]

## Gap Status

### Resolved
- [Gap]: [How resolved]

### Accepted (User Approved)
- [Gap]: [User decision]

### Outstanding
- [Gap]: [Status]

## Recommendation

[APPROVED FOR USE / NEEDS FIXES: list required changes]
```
