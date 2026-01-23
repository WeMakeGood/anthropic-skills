# Validation Guide

## Phase-by-Phase Validation

### Phase 1: Index Validation

Before proceeding to synthesis:

- [ ] Source index created at `<OUTPUT_PATH>/source-index.md`
- [ ] All source files listed with type and status
- [ ] Each file classified correctly (strategy, operational, transcript, interview, notes, reference)
- [ ] Files needing synthesis marked as `needs-synthesis`
- [ ] Conflicts between documents identified
- [ ] Information gaps noted
- [ ] User approved the index

### Phase 2: Synthesis Validation

Before proceeding to proposal:

- [ ] Synthesis file created for each `needs-synthesis` source
- [ ] Each synthesis extracts facts, not verbatim quotes
- [ ] Exact names, dates, figures preserved from sources
- [ ] Ambiguous items flagged for clarification (not interpreted)
- [ ] Source index updated: status → `synthesized`, working source → synthesis path
- [ ] User approved ALL synthesis files

### Phase 3: Proposal Validation

Before proceeding to build:

- [ ] Proposal describes structure only (no pre-written content)
- [ ] Each module has: ID, name, purpose, source references, token estimate
- [ ] Agent-module mapping with token totals (target: 12,000-18,000 per agent)
- [ ] Conflicts listed with proposed resolutions
- [ ] Gaps classified (blocking/limiting/enhancing)
- [ ] Questions for user clearly stated
- [ ] User approved the proposal

---

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

---

## Source Verification Checklist (CRITICAL)

**Every [CONFIRMED] fact must pass this check:**

- [ ] Is this fact in one of the working sources listed in the source index?
- [ ] Can you point to where in that working source (original or synthesis)?
- [ ] Does the module use the EXACT names, dates, titles, and terms from the source?

**If ANY answer is NO:** Change to `[PROPOSED]` or remove the fact.

**Common hallucination patterns to check for:**
- Executive names or titles not in working sources
- Specific dates, founding years, or timelines not explicitly stated
- Legal entity details (LLC vs Inc, state of incorporation) not verified
- Locations, addresses, or geographic claims
- Revenue figures, headcounts, or metrics
- Partner or client names
- Certifications, credentials, or regulatory status

**Verification process:**
1. Read each [CONFIRMED] statement in the module
2. Consult source index to identify relevant working sources
3. Search working sources for supporting text
4. If not found: change marker to [PROPOSED] or remove
5. If found but details differ: use the SOURCE version, not what you wrote

---

## Cross-Reference Validation

Run: `python scripts/validate_library.py ./modules`

Check for:
- References to non-existent modules
- References to sections that don't exist
- Circular reference chains
- Orphaned modules (no agent loads them)

---

## Token Budget Validation

Run: `python scripts/count_tokens.py ./modules ./agents`

For each agent, verify:
- Total tokens under 20,000
- Target range: 12,000-18,000 tokens
- Foundation modules not over-weighted

If over budget:
1. Check for verbose explanations (trim)
2. Check for duplicated content (consolidate)
3. Consider splitting large modules
4. Review if agent needs all assigned modules

If under 10,000 tokens:
- Review if agent is missing useful context
- Only accept if agent's role is genuinely narrow

---

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

### Facts Not in Working Sources

**Symptom**: Module contains [CONFIRMED] facts not found in source index working sources
**Fix**: Either locate the working source and verify, or change to [PROPOSED]

---

## Final Validation Checklist

Before declaring complete:

- [ ] Source index status updated to `complete`
- [ ] All modules pass quality checklist
- [ ] **All [CONFIRMED] facts verified against working sources in source index**
- [ ] No broken cross-references
- [ ] No duplicated information
- [ ] All agents in target token range (12,000-18,000)
- [ ] All BLOCKING gaps resolved or user-approved
- [ ] High-stakes content properly marked and sourced
- [ ] Agent definitions include verification and objectivity guidance
- [ ] User approved final library

---

## Validation Report Template

```markdown
# Validation Report

**Date**: YYYY-MM-DD
**Library**: [Name]
**Source Index**: [path to source-index.md]

## Summary

- Total source files: [X]
- Synthesized sources: [X]
- Total modules: [X]
- Total agents: [X]
- Issues found: [X]
- **Source verification**: [PASSED/FAILED]
- Status: [PASS/NEEDS FIXES]

## Source Index Status

- [ ] All sources classified
- [ ] All syntheses approved
- [ ] Index status: [complete]

## Source Verification Audit

For each module, confirm [CONFIRMED] facts were verified against working sources:

| Module | [CONFIRMED] Count | Verified | Issues |
|--------|-------------------|----------|--------|
| F1 | [X] | Yes/No | [List any unverified claims] |

## Token Budgets

| Agent | Tokens | % of Limit | Status |
|-------|--------|------------|--------|
| [Agent] | [X] | [X]% | OK/OVER/UNDER |

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
