---
name: creating-organization-dossiers
description: Creates structured organizational dossiers following a 6-phase research workflow. Produces comprehensive profiles with executive summary, mission, leadership, financials, programs, partnerships, and strategic analysis sections. Use when user says create a dossier, build an org profile, generate an organization report, compile background on a company, or produce a prospect brief. Also triggers on client research, prospect research, due diligence report, partnership evaluation, or org analysis.
---

# Creating Organization Dossiers

<purpose>
Claude's default research mode produces surface-level summaries that look comprehensive
but lack verification. Organizational dossiers require verified intelligence, not
plausible-sounding narratives. This skill exists to enforce source attribution for
every factual claim and explicit marking of inferences versus confirmed facts.
</purpose>

Build comprehensive organizational profiles by systematically gathering and synthesizing public information.

## Critical Rules

**SOURCE ATTRIBUTION:** Every factual claim MUST cite its source (website page, 990 filing, user-provided document). Never present inferences as facts.

**EPISTEMIC MARKERS:** Use these consistently throughout the dossier:
- `[Source: website/about]` — information from a specific source
- `[Source: 990 FY2023]` — information from tax filings
- `[Inferred]` — reasonable inference from available data
- `[Unverified]` — claimed by organization, not independently verified
- `[Outdated: YYYY]` — information that may no longer be current

**PROFESSIONAL OBJECTIVITY:** Report what you find, including concerns or red flags. If financials show declining revenue, leadership turnover is high, or public information is inconsistent — say so directly. The user needs accurate intelligence, not a favorable summary.

**NATURAL PROSE (for Executive Summary and narrative sections):** Write like a research analyst, not an AI assistant. Avoid: pivotal, crucial, vibrant, tapestry, delve, foster, leverage, "not only X but Y," "serves as." Use direct language: "Revenue is $2.4M" not "Revenue stands at $2.4M."

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

<phase_gather>
### Phase 1: Gather Requirements

Use the questions above. If user provides organization name without other details, search for:
- Official website
- Nonprofit status (check if they have 990 filings)
- Basic public information

**GATE (file/artifact):** Before proceeding, write:
- "Organization: [name]"
- "Purpose: [why this dossier is being created]"
- "Data collection plan: [scripts to run, sources to check]"

**GATE (inline):** Verify internally before proceeding. Do not output.
</phase_gather>

<phase_collect>
### Phase 2: Collect Website Content

**ALWAYS run the scraper script first.** It produces better, more complete results than web fetch.

```bash
python3 scripts/scrape_website.py <ORG_URL> --output ./tmp/<org-name>
```

The scraper:
- Discovers pages via sitemap.xml (preferred) or navigation crawling
- Extracts content from About, Team, Board, Programs, Impact, Partners pages
- Saves structured markdown files for analysis

Review output in `./tmp/<org-name>/`:
- `scrape_manifest.json` - what was found
- `homepage.md` - main page content
- `about.md`, `team.md`, etc. - categorized content

**Fallback (only if script fails):** Use web_fetch to manually gather content from key pages (Homepage, About, Team, Board, Programs, Impact, Partners, Contact).

If scraper misses important pages, ask user for specific URLs or use web_fetch for those specific pages.

**GATE (file/artifact):** Before proceeding, write:
- "Scraped pages: [list categories found]"
- "Missing categories: [what wasn't found or needs manual lookup]"

**GATE (inline):** Verify internally before proceeding. Do not output.
</phase_collect>

<phase_990>
### Phase 3: Retrieve 990 Data (Nonprofits)

**For U.S. nonprofits, ALWAYS run the 990 script:**

```bash
python3 scripts/fetch_990.py "<ORG_NAME>" --output ./tmp/<org-name>
```

Or with known EIN (more reliable):
```bash
python3 scripts/fetch_990.py --ein <EIN> --output ./tmp/<org-name>
```

The script retrieves from ProPublica Nonprofit Explorer API:
- Recent 990 filings (up to 5 years)
- Revenue, expenses, assets
- Employee/volunteer counts
- PDF links to original filings

**If script returns no results:** Organization may not e-file. Try web search for GuideStar/Candid or ask user for 990 PDFs.

**Skip this phase** for non-U.S. organizations or for-profit companies.

**GATE (file/artifact):** Before proceeding, write:
- "990 data available: [yes/no]"
- "Years covered: [list fiscal years]" or "Skipped: [reason]"

**GATE (inline):** Verify internally before proceeding. Do not output.
</phase_990>

<phase_materials>
### Phase 4: Process Additional Materials

Read any user-provided materials:
- Previous meeting notes
- Correspondence
- Annual reports
- Press coverage
- Strategic plans

Extract relevant information for each dossier section.

**GATE (file/artifact):** Before proceeding, write:
- "Additional materials processed: [list or 'none provided']"
- "Key information extracted: [brief summary]"

**GATE (inline):** Verify internally before proceeding. Do not output.
</phase_materials>

<phase_synthesize>
### Phase 5: Synthesize Findings

**GATE (file/artifact):** Before writing the dossier, list your sources:
- "Mission statement source: [page/document]"
- "Financial data source: [990 year or document]"
- "Leadership info source: [page/document]"
- "Program details source: [page/document]"

**GATE (inline):** Verify sources internally before proceeding. Do not output.

If any section lacks a source, note it here and address in Information Gaps.

**Organizational Understanding:**
- Core mission and theory of change — cite specific source
- Key programs and how they work — cite specific source
- Leadership structure and key decision-makers — cite specific source
- Financial health and sustainability — cite 990 data with fiscal year
- Strategic direction — cite source or mark as "[Inferred from available data]"

**If requester context exists, analyze:**
- Mission alignment
- Potential collaboration areas
- Shared values or approach
- Service/partnership fit

**CRITICAL — Identify and report:**
- **Gaps:** What information is missing? What needs verification?
- **Concerns:** Any red flags, inconsistencies, or issues found
- **Limitations:** Where is data outdated, self-reported, or unverifiable?

Do not omit concerns to make the dossier more favorable. The user needs accurate intelligence.
</phase_synthesize>

<phase_generate>
### Phase 6: Generate and Deliver Dossier

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

Deliver per the Output Rules above. If writing to file, use `<org-name>-dossier.md`.
</phase_generate>

## Output Rules

The user controls how the dossier is delivered by including a keyword in their request:

- **"as a file"** → Write to `<org-name>-dossier.md`. After saving, confirm with a brief summary of key findings.
- **"as an artifact"** → Create an artifact containing the complete dossier.
- **No keyword (default)** → Return the complete dossier inline in your response.

When delivering inline (the default), execute all workflow phases internally — do not output progress checklists, gate statements, or intermediate extraction notes. Return only the final dossier.

When delivering as a file or artifact, show the progress checklist and write gate statements visibly before proceeding through each phase.

## Key Principles

**Thorough and honest:**
- Cite sources for every factual claim
- Distinguish organization's own claims from third-party verification
- Flag discrepancies between sources — do not resolve them silently
- Mark inferences explicitly with "[Inferred]"

**Objective, not favorable:**
- Report concerns and red flags directly
- If financial trends are negative, say so
- If leadership appears unstable, note it
- If public information is sparse or inconsistent, flag this as a limitation
- The user's decision quality depends on accurate information, not positive framing

**Respect the purpose:**
- Tailor depth to the stated purpose
- Prospect research needs different emphasis than general background
- Include alignment analysis only when requester context exists

**Note limitations:**
- 990 data lags 1-2 years behind current — always note fiscal year
- Website content may be outdated — note if "last updated" dates are visible
- Self-reported information is not independently verified unless stated
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

<failed_attempts>
## What DOESN'T Work

- **Writing before running scripts:** Manual web fetch produces incomplete results. ALWAYS run scrape_website.py first.
- **Synthesizing without source verification:** Before writing any section, identify the exact source for each claim. "I'll verify later" means never.
- **Presenting inferences as facts:** If you deduce something from context (e.g., "likely a small team based on website"), mark it [Inferred]. Readers need to know what's verified vs reasoned.
- **Favorable framing of concerns:** If financials show declining revenue, say "Revenue declined 15% from $X to $Y." Don't soften it to "Revenue faced some headwinds."
- **Skipping the gaps section:** Every dossier has information gaps. Identifying what you DON'T know is as valuable as what you do know.
</failed_attempts>

## References

- [references/DOSSIER-TEMPLATE.md](references/DOSSIER-TEMPLATE.md) - Full dossier structure
- [references/DATA-SOURCES.md](references/DATA-SOURCES.md) - Additional research sources
