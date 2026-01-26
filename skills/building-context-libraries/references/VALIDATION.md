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
- [ ] **Content is transformed, not transcribed** — no "they said X" patterns
- [ ] **No verbatim quotes** — facts stated directly, not attributed
- [ ] **No speech artifacts** — no filler words, false starts, or conversational fragments
- [ ] **Organized by topic** — not by speaker or document order
- [ ] Exact names, dates, figures preserved from sources
- [ ] Ambiguous items flagged for clarification (not interpreted)
- [ ] Source index updated: status → `synthesized`, working source → synthesis path
- [ ] **LLM agent test:** Would an agent find this synthesis useful and actionable?
- [ ] User approved ALL synthesis files

### Phase 2.5: Pre-Synthesis Evaluation

Before synthesizing each file marked `needs-synthesis`:

- [ ] Read the file first
- [ ] Evaluate whether it actually needs synthesis (messy/conversational) or is already clean
- [ ] If already clean: Update index to `ready`, skip synthesis
- [ ] If synthesis file already exists: Read it, update index to `synthesized`, skip re-synthesis

### Phase 3: Proposal Validation

Before proceeding to build:

- [ ] **NO CONTENT** — Proposal describes structure only, not organizational information
- [ ] **NO FABRICATION** — Every detail traces to a working source you actually read
- [ ] **NO COMPRESSION** — Token estimates reflect source richness, not arbitrary low targets
- [ ] Each module has: ID, name, purpose, source references, token estimate
- [ ] Agent-module mapping with token totals (maximum: 20,000 per agent)
- [ ] Conflicts listed with proposed resolutions
- [ ] Gaps classified (blocking/limiting/enhancing)
- [ ] Questions for user clearly stated
- [ ] User approved the proposal

**Red flags — STOP if you find yourself writing:**
- "The organization focuses on..." → That's content, not structure
- "Key services include..." → That's content
- "Their approach emphasizes..." → That's content
- Any specific organizational details not from sources → That's fabrication

---

## Module Quality Checklist

For each module:

- [ ] Has correct YAML frontmatter (module_id, name, tier, purpose, last_updated)
- [ ] Purpose clearly states what question it answers
- [ ] Scope defines what's included AND excluded
- [ ] No information duplicated from other modules
- [ ] All cross-references use explicit format
- [ ] `[PROPOSED]` used only for user-approved inferences (all other content is verified)
- [ ] High-stakes content marked with `[HIGH-STAKES]` and has source citations
- [ ] Agent instructions section included

---

## Source Verification Checklist (CRITICAL)

**All content must be verified. Every fact must pass this check:**

- [ ] Is this fact in one of the working sources listed in the source index?
- [ ] Can you point to where in that working source (original or synthesis)?
- [ ] Does the module use the EXACT names, dates, titles, and terms from the source?

**If ANY answer is NO:** Mark as `[PROPOSED]` or remove the fact.

**Common hallucination patterns to check for:**
- Executive names or titles not in working sources
- Specific dates, founding years, or timelines not explicitly stated
- Legal entity details (LLC vs Inc, state of incorporation) not verified
- Locations, addresses, or geographic claims
- Revenue figures, headcounts, or metrics
- Partner or client names
- Certifications, credentials, or regulatory status

**Verification process:**
1. Read each factual statement in the module
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
- Total tokens under 20,000 maximum
- Include all useful verified content (don't compress to hit a target)
- Foundation modules not over-weighted

If over budget:
1. Check for verbose explanations (trim)
2. Check for duplicated content (consolidate)
3. Consider splitting large modules
4. Review if agent needs all assigned modules

If agent seems thin:
- Review if agent is missing useful verified content from sources
- Check if sources contain more relevant information
- Only accept sparse context if sources genuinely lack content for this agent's role

---

## Common Issues

### Transcription Instead of Synthesis

**Symptom**: Content reads like the source — "John said X," verbatim quotes, conversational fragments, speech artifacts
**Fix**: Rewrite completely. Extract the *meaning* and state it directly. "X is true" not "John mentioned that X." Remove all filler words, false starts, and conversational structure.

**Wrong:**
```
The CEO mentioned that they "try to meet clients where they are" and emphasized
the importance of "quick wins" for new clients.
```

**Right:**
```
Client engagement adapts to maturity level:
- New clients: prioritize quick wins, minimize complexity
```

### Time Spans Instead of Dates

**Symptom**: Content includes relative time references like "25 years of experience," "over a decade," "for 15 years"
**Fix**: Convert to absolute dates. "25 years of experience" → "since 1999" (calculate from source document date). If source date unknown, flag for clarification.

### Duplicated Information

**Symptom**: Same fact appears in multiple modules
**Fix**: Keep in ONE module, add references in others

### Unverified Content

**Symptom**: Content that cannot be traced to a working source
**Fix**: Remove it, or mark with `[PROPOSED]` if user has approved including inferences

### Vague Cross-References

**Symptom**: "See other modules for details"
**Fix**: Specific reference: "See [Module Name] for [specific info]"

### Over-Explanation

**Symptom**: Explaining concepts Claude already knows
**Fix**: Remove general explanations, keep org-specific info only

### Missing Agent Instructions

**Symptom**: Module has content but no guidance on how to use it
**Fix**: Add "Agent Instructions" section with application guidance

### High-Stakes Content Without Source

**Symptom**: Legal, financial, or third-party claims without `[HIGH-STAKES]` marker
**Fix**: Add marker and ensure source citation exists

### Missing Verification Guidance

**Symptom**: Agent definition has no "Verification & Professional Objectivity" section
**Fix**: Add section with stakes-based verification behaviors and objectivity guidelines

### Facts Not in Working Sources

**Symptom**: Module contains facts not found in source index working sources
**Fix**: Either locate the working source and verify, or change to [PROPOSED]

---

## Final Validation Checklist

Before declaring complete:

- [ ] Source index status updated to `complete`
- [ ] All modules pass quality checklist
- [ ] **All facts verified against working sources in source index**
- [ ] No broken cross-references
- [ ] No duplicated information
- [ ] All agents under 20,000 token maximum
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

For each module, confirm all facts are verifiable in working sources:

| Module | Fact Count | Verified | Issues |
|--------|------------|----------|--------|
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

## Proposed Content Audit

- [ ] `[PROPOSED]` used only for user-approved inferences
- [ ] No unverified content without `[PROPOSED]` marker
- Issues: [List any unverified content]

## Stakes Classification Audit

- [ ] High-stakes content identified and marked
- [ ] High-stakes items have source citations
- [ ] Agent definitions include stakes-based verification guidance
- Issues: [List any high-stakes content without source]

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
