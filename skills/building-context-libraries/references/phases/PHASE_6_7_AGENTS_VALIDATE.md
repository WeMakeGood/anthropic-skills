# Phase 6-7: Create Agent Definitions & Validate

> **CRITICAL RULES — Read these first, even if you read nothing else:**
> - NEVER invent details. Agent definitions reference modules — they don't contain organizational facts.
> - NEVER duplicate guardrail content. Standard guardrail modules handle anti-hallucination and prose quality.
> - All agents MUST load F_agent_behavioral_standards. External-facing agents MUST also load S_natural_prose_standards.
> - Every fact in every module must trace to a working source. If you can't verify it, remove it.
> - Update build-state.md before ending the session.

---

## Phase 6: Create Agent Definitions

### What This Phase Does

Create a definition file for each agent in the approved proposal. Agent definitions specify which modules to load, the agent's role, and any domain-specific behavioral guidance.

### Before You Start

1. **Read `<OUTPUT_PATH>/build-state.md`** — confirm Phase 5 is complete.
2. **Read `<OUTPUT_PATH>/proposal.md`** — agent-module mapping is your blueprint.
3. **Review completed modules** in `<OUTPUT_PATH>/modules/` — verify they exist and are complete.
4. **Review completed addenda** in `<OUTPUT_PATH>/addenda/` — verify they exist and are complete.

### Create Agent Definition Files

For each agent, create `<OUTPUT_PATH>/agents/[agent-name].md`:

```markdown
---
agent_name: [Name]
agent_domain: [domain]
purpose: "[What this agent does]"
modules:
  foundation:
    - F1_[name]
    - F_agent_behavioral_standards
  shared:
    - S1_[name]
    - S_natural_prose_standards  # if external-facing
  specialized:
    - D1_[name]
addenda:  # optional — only if this agent consults reference data
  - addendum_name: "[what data]"
estimated_tokens: [total]
last_updated: YYYY-MM-DD
---

# [Agent Name]

## Role

[2-3 sentences: what this agent does — focused on actions and decisions, not knowledge]

## Responsibilities

1. [Primary responsibility — what the agent produces or decides]
2. [Secondary responsibility]
3. [Additional responsibility]

## Knowledge Sources

| Area | Module | Why Needed |
|------|--------|------------|
| [Area] | [Module ID] | [What decisions this enables] |

## Reference Addenda (Optional)

If this agent consults reference data (pricing, biographical details, service catalogs), list the addenda here. Addenda are loaded on demand when modules direct the agent to consult them — they do not count against the module token budget.

| Addendum | When Consulted |
|----------|----------------|
| [addenda/name.md] | [What triggers the agent to load this — e.g., "When building proposals that include pricing"] |

## Guidelines

**Do:**
- [Behavioral instruction]
- [Approach to follow]

**Don't:**
- [Anti-pattern to avoid]
- [Common mistake]

## Domain-Specific Guidance (Optional)

Only add guidance here that extends beyond the standard guardrail modules:

- **Additional verification:** [e.g., "Always verify partner names against F1"]
- **Escalation:** [e.g., "Flag pricing questions for human review"]
- **Domain constraints:** [e.g., "Never provide legal advice"]

## Token Budget

- Foundation: [X] tokens
- Shared: [X] tokens
- Specialized: [X] tokens
- **Total: [X] tokens** ([X]% of per-agent limit)
- Addenda: not counted (loaded on demand)
```

### Required Module Assignments

| Agent Type | F_agent_behavioral_standards | S_natural_prose_standards |
|------------|------------------------------|---------------------------|
| Marketing/communications | Required | Required |
| Content creation | Required | Required |
| Internal documentation | Required | Skip |
| Research/analysis | Required | Skip (unless published) |

### Do NOT

- Duplicate content from guardrail modules in agent definitions
- Include organizational facts in agent definitions (that's what modules are for)
- Create agents not in the approved proposal without user approval

---

## Phase 7: Validate

### What This Phase Does

Run validation scripts and perform manual checks to verify the complete library is correct, consistent, and ready for use.

### Step 1: Run Validation Scripts

```bash
# Check for broken cross-references and duplicated content
python3 <skill_dir>/scripts/validate_library.py <OUTPUT_PATH>/modules

# Check token budgets for each agent
python3 <skill_dir>/scripts/count_tokens.py <OUTPUT_PATH>/modules <OUTPUT_PATH>/agents
```

### Step 2: Source Verification Audit

For each module, verify all facts against working sources:

1. Read each factual statement in the module
2. Consult source index to identify relevant working sources
3. Search working sources for supporting text
4. If not found: mark `[PROPOSED]` or remove
5. If found but details differ: use the SOURCE version

**Common hallucination patterns to check for:**
- Executive names or titles not in working sources
- Specific dates, founding years, or timelines not explicitly stated
- Legal entity details (LLC vs Inc, state of incorporation)
- Locations, addresses, or geographic claims
- Revenue figures, headcounts, or metrics
- Partner or client names
- Credentials, certifications, or regulatory status

### Step 3: Cross-Reference Check

- All references to other modules point to modules that exist
- All references to specific sections point to sections that exist
- No circular reference chains
- No orphaned modules (every module is loaded by at least one agent)
- All module cross-references to addenda point to addenda that exist
- No orphaned addenda (every addendum is referenced by at least one module)

### Step 4: Content Quality Check

For each module, verify:
- [ ] **No verification logs remain.** `<!-- VERIFICATION LOG ... -->` blocks are build artifacts that must be removed before Phase 5 ends. If any are still present, delete them now. They waste tokens and can cause instruction conflicts.
- [ ] Content is metaprompting/context, not just copied facts
- [ ] No verbatim quotes from sources
- [ ] No speech artifacts or conversational structure
- [ ] Time spans converted to dates
- [ ] HIGH-STAKES content marked and sourced
- [ ] PROPOSED content marked where applicable
- [ ] Cross-references are specific, not vague
- [ ] Agent instructions section tells agents how to use the knowledge

### Step 4b: Addenda Quality Check

For each addendum, verify:
- [ ] **No verification logs remain.** Same as modules — delete any `<!-- VERIFICATION LOG ... -->` blocks.
- [ ] Contains data only — no behavioral instructions ("When X, do Y" belongs in modules)
- [ ] Has correct YAML frontmatter (addendum_id, addendum_name, purpose, referenced_by, update_frequency, last_updated)
- [ ] Every data point traces to a working source
- [ ] HIGH-STAKES content marked and sourced
- [ ] At least one module references this addendum
- [ ] Update frequency is specified and realistic

### Step 5: Token Budget Check

For each agent:
- Total module tokens under 10% of target model's context window (e.g., 20K for 200K-context models). Addenda are excluded — loaded on demand.
- No modules under 1,000 tokens (likely too thin)
- Include all useful verified content (don't compress to hit a target)

### Step 6: Update Build State

Update `<OUTPUT_PATH>/build-state.md`:
- Phase 6 status → `complete`
- Phase 7 status → `complete (pending approval)`
- Source index status → `complete`

### Gate: User Approval Required

Before requesting approval, write:
- "Validation complete"
- "Modules: [count] total ([count] foundation, [count] shared, [count] specialized)"
- "Addenda: [count] total"
- "Agents: [count] total"
- "Cross-reference issues: [count or 'none']"
- "Token budget status: [all agents under limit / issues found]"
- "Source verification: [passed / issues found]"
- "Content quality: [passed / issues found]"
- "Addenda quality: [passed / issues found]"

**STOP. Get user approval on final library.**

After approval, update build-state.md: all phases → `complete`, library status → `approved`.

---

## Session Handoff Validation

Before ending ANY session (not just the final one):

- [ ] `build-state.md` is updated with current phase and sub-step
- [ ] `build-state.md` points to the correct next phase instruction file
- [ ] All completed work is saved to disk (modules, agent definitions, etc.)
- [ ] Source index reflects current status of all files

This ensures a new session can resume by reading only `build-state.md`.
