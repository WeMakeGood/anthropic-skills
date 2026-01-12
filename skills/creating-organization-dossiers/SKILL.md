---
name: creating-organization-dossiers
description: Creates structured organizational dossiers following a 6-phase research workflow. Produces comprehensive profiles with executive summary, mission, leadership, financials, programs, partnerships, and strategic analysis sections. Use when user says create a dossier, build an org profile, generate an organization report, compile background on a company, or produce a prospect brief. Also triggers on client research, prospect research, due diligence report, partnership evaluation, or org analysis. Outputs to [org-name]-dossier.md file.
---

# Creating Organization Dossiers

Build comprehensive organizational profiles by systematically gathering and synthesizing public information.

## Before Starting

Gather requirements interactively:

1. **"What organization should I research?"**
   - Organization name (required)
   - Website URL (if known)
   - EIN for nonprofits (if known)

2. **"What's the purpose of this dossier?"**
   - Prospect research / client onboarding
   - Partnership evaluation
   - Grant application research
   - General background

3. **"Do you have any additional materials?"**
   - Existing documents about the organization
   - Previous correspondence
   - Specific areas of interest or concern

4. **Check for context files:**
   - Look for requester context (who is doing the research and why)
   - Look for organizational context about the requester
   - These inform the "alignment analysis" section

Store as:
- `ORG_NAME` - target organization name
- `ORG_URL` - website URL
- `ORG_EIN` - EIN (for nonprofits)
- `PURPOSE` - why this dossier is being created
- `REQUESTER_CONTEXT` - who is requesting and their goals

## Workflow

```
Dossier Progress:
- [ ] Phase 1: Gather requirements
- [ ] Phase 2: Collect website content
- [ ] Phase 3: Retrieve 990 data (if nonprofit)
- [ ] Phase 4: Process additional materials
- [ ] Phase 5: Synthesize findings
- [ ] Phase 6: Generate dossier
```

### Phase 1: Gather Requirements

Use the questions above. If user provides organization name without other details, search for:
- Official website
- Nonprofit status (check if they have 990 filings)
- Basic public information

### Phase 2: Collect Website Content

**If scripts are available (Claude Code):**

```bash
python3 <skill_dir>/scripts/scrape_website.py <ORG_URL> --output ./tmp/<org-name>
```

**If scripts are not available (Claude AI web):**

Use web_fetch or web_search to manually gather content from key pages:
- Homepage
- About / Our Story
- Team / Leadership
- Board of Directors
- Programs / Services / What We Do
- Impact / Outcomes / Annual Reports
- Partners / Funders
- Contact (for location, phone, email)

The scraper auto-discovers and extracts:
- About / Mission pages
- Team / Leadership
- Board / Governance
- Programs / Services
- Impact / Outcomes
- Partners / Funders

Review output in `./tmp/<org-name>/`:
- `scrape_manifest.json` - what was found
- `about.md`, `team.md`, etc. - extracted content

If scraper misses important pages (or if using web search), ask user for specific URLs.

### Phase 3: Retrieve 990 Data (Nonprofits)

**If scripts are available (Claude Code):**

```bash
python3 <skill_dir>/scripts/fetch_990.py "<ORG_NAME>" --output ./tmp/<org-name>
```

Or with known EIN:
```bash
python3 <skill_dir>/scripts/fetch_990.py --ein <EIN> --output ./tmp/<org-name>
```

**If scripts are not available (Claude AI web):**

Search for 990 data via:
- ProPublica Nonprofit Explorer: `https://projects.propublica.org/nonprofits/`
- Search: "[Organization Name] 990" or "[Organization Name] EIN"
- Fetch the ProPublica page directly for financial details

This retrieves from ProPublica Nonprofit Explorer:
- Recent 990 filings (up to 5 years)
- Revenue, expenses, assets
- Employee/volunteer counts
- PDF links to original filings

**If ProPublica returns no results:**
- Organization may not e-file
- Try GuideStar/Candid web search
- Ask user if they have 990 PDFs to provide

### Phase 4: Process Additional Materials

Read any user-provided materials:
- Previous meeting notes
- Correspondence
- Annual reports
- Press coverage
- Strategic plans

Extract relevant information for each dossier section.

### Phase 5: Synthesize Findings

Before writing, analyze:

**Organizational Understanding:**
- Core mission and theory of change
- Key programs and how they work
- Leadership structure and key decision-makers
- Financial health and sustainability
- Strategic direction

**If requester context exists, analyze:**
- Mission alignment
- Potential collaboration areas
- Shared values or approach
- Service/partnership fit

**Identify gaps:**
- What information is missing?
- What needs verification?
- What would be helpful to know?

### Phase 6: Generate Dossier

**Output file:** `<org-name>-dossier.md`

Use the template in [references/DOSSIER-TEMPLATE.md](references/DOSSIER-TEMPLATE.md).

Key sections:
1. Executive Summary
2. Organizational Overview (mission, vision, values)
3. Leadership & Governance
4. Programs & Services
5. Financial Profile
6. Partnerships & Collaborations
7. Digital Presence
8. Strategic Analysis (if requester context provided)
9. Information Gaps & Next Steps

## Output Requirements

**ALWAYS save the dossier to a file. Do not output inline in chat.**

1. Generate filename: `<org-name>-dossier.md`
2. Write the complete dossier to this file
3. After saving, confirm with brief summary of key findings

## Key Principles

**Be thorough but honest:**
- Note when information comes from organization's own claims vs. third-party sources
- Flag any discrepancies found between sources
- Clearly mark what's confirmed vs. inferred

**Respect the purpose:**
- Tailor depth to the stated purpose
- Prospect research needs different emphasis than general background
- Include alignment analysis only when requester context exists

**Note limitations:**
- 990 data lags 1-2 years behind current
- Website content may be outdated
- Always recommend verification for key decisions

## Example

**Input:**
```
Create a dossier on Community Bridges Foundation.
Website: https://communitybridges.org
Purpose: Evaluating as potential grantee
```

**Process:**
1. Scrape website content
2. Fetch 990 data
3. Synthesize findings
4. Generate dossier

**Output excerpt:**
```markdown
# Community Bridges Foundation - Organizational Dossier
*Generated: January 12, 2026*

## Executive Summary

Community Bridges Foundation is a 501(c)(3) serving the greater Metro area
since 2015. Annual revenue of ~$2.4M (2023), with 85% from foundation grants.
12 FTE staff plus 150+ volunteers. Strong focus on youth mentorship and
workforce development.

**Key Strengths:**
- Clear theory of change with documented outcomes
- Diverse board with relevant expertise
- Growing program reach (40% increase over 3 years)

**Areas to Explore:**
- Heavy reliance on foundation funding (sustainability risk)
- Recent executive transition (new ED in 2024)
- Limited digital presence relative to program scope

## Organizational Overview

### Mission
"Building pathways to opportunity for underserved youth through mentorship,
skill development, and community connection."

### Programs
1. **Youth Mentorship Network** - 1:1 mentoring for ages 14-18
2. **Career Pathways** - Workforce readiness and job placement
3. **Community Hub** - After-school programming and family support
...
```

## References

- [references/DOSSIER-TEMPLATE.md](references/DOSSIER-TEMPLATE.md) - Full dossier structure
- [references/DATA-SOURCES.md](references/DATA-SOURCES.md) - Additional research sources
