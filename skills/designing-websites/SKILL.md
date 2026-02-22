---
name: designing-websites
description: Designs website content strategy and generates all content assets before development. Creates calls-to-action, audience analysis, sitemaps, page content, form specs, and custom post type definitions. Use when planning a new website, creating website content strategy, building site architecture, or generating website copy. Triggers on website design, content strategy, sitemap creation, or website planning requests.
---

# Designing Websites

<purpose>
Website projects typically start with visuals and pages, leaving content strategy
as an afterthought. This produces beautiful sites with weak conversions. This skill
exists because content strategy must precede design—every page needs a purpose
before it needs a layout. The skill enforces CTA-first thinking by requiring
business goals before any structure decisions.
</purpose>

Guides website content strategy from business goals to complete content files. Flips traditional design: starts with CTAs, not visuals.

## Critical Rules

**GROUNDING:** Use ONLY information the user provides. Never invent company details, statistics, testimonials, or history.

**PROFESSIONAL OBJECTIVITY:** If the user's proposed CTAs are weak, their audience analysis is incomplete, or their sitemap has dead ends — say so directly. Challenge unclear business goals before proceeding. Your job is to produce an effective website, not to validate the user's initial ideas.

**SECOND-ORDER THINKING:** When defining CTAs and conversion paths, push past the first-order goal. If the primary CTA drives form submissions, what does that create downstream? What visitor needs does it leave unaddressed? If a sitemap funnels traffic one way, what does it make harder to find?

**CONVERGENCE AWARENESS:** When audience analysis reveals overlapping needs across segments, or when business goals intersect with user motivations, flag the intersection — it's often where the strongest content opportunities live.

**PREMATURE COMMITMENT CHECK:** Before finalizing the sitemap or CTA hierarchy, check whether you've considered more than one conversion strategy. If you defaulted to the first plausible structure, flag it.

**PLACEHOLDERS:** When information is needed but not provided, use `{{needs-input: description}}`. Never fill gaps with plausible-sounding content.

**NATURAL PROSE:** Write like a domain expert, not an AI assistant.

Banned vocabulary: pivotal, crucial, vital, testament to, underscores, highlights, vibrant, tapestry, delve, foster, garner, leverage, landscape (figurative), holistic, robust, synergy, cutting-edge, groundbreaking, nestled, showcases, boasts, elevate

Banned structures: "Not only X but Y," "serves as," "stands as," "-ing" phrases for empty analysis ("highlighting the importance," "showcasing their commitment"), vague attribution ("experts say," "industry leaders"), formulaic balance ("Despite challenges, [positive]")

Required: Use "is" not "serves as," repeat nouns rather than finding synonyms, be specific with numbers and names, match the voice of actual practitioners in the user's industry.

## Quick Start

```
Website Design Progress:
- [ ] Phase 1: Gather requirements
- [ ] Phase 2: Define CTAs
- [ ] Phase 3: Analyze audience
- [ ] Phase 4: Create sitemap
- [ ] Phase 5: Generate content
- [ ] Phase 6: Validate
```

## Process Overview

```
## Website Design Process

This skill guides you through creating a complete content strategy and all
content assets for your website. The process follows this order:

1. **Business Goals** - Define your primary calls-to-action first
2. **Audience Analysis** - Understand who visits and why
3. **Conversion Strategy** - Map how interest becomes action
4. **Sitemap** - Create a flow-based structure (no dead ends)
5. **Content Generation** - Produce all page/post content files
6. **Validation** - Verify completeness and consistency

**Important:** We start with business goals, not design or audience.
```

<phase_gather>
## Phase 1: Gather Requirements

Before writing any files, collect:

**Business Context**
- What does the organization do?
- What industry/sector?
- What makes them unique?

**Goals and CTAs**
- What is the PRIMARY action you want visitors to take?
- What is the secondary action?
- Any tertiary actions?

**Audience**
- Who are the primary users?
- How do they typically find you?
- Are there distinct user journeys?

**Technical Requirements**
- Custom post types needed?
- Forms required?
- E-commerce/donations?
- Integrations?

**Existing Content**
- Content to migrate?
- Brand guidelines?
- Tone of voice?

### Pre-Flight Checklist

**GATE:** Before proceeding to Phase 2, write:
- "Primary CTA: [specific action visitors should take]"
- "Secondary CTA: [specific action]"
- "Target audiences: [list with entry points]"
- "Technical requirements: [forms, CPTs, integrations needed]"

Do not proceed until you have written these statements. If the user cannot clearly articulate their primary CTA, help them define it before proceeding. A website without a clear primary action will underperform.
</phase_gather>

<phase_strategy>
## Phase 2-3: Strategy

Create `./tmp/<project-name>/` and generate strategy documents.

See [references/STRATEGY.md](references/STRATEGY.md) for:
- CTA definition format
- Audience analysis template
- Conversion strategy mapping

**Core philosophy:** Every piece of content converts interest + intent into action. No "informational only" pages.
</phase_strategy>

<phase_sitemap>
## Phase 4: Sitemap

Create flow-based sitemap with no dead ends.

See [references/SITEMAP-TEMPLATES.md](references/SITEMAP-TEMPLATES.md) for:
- Sitemap format and structure
- Template specifications
- Parent/child relationships

Rules:
- Every page has an exit toward CTA
- Every page has assigned template
- Every page has assigned CTA

**GATE:** Before generating content, write:
- "Sitemap contains [N] pages"
- "All pages have assigned CTAs: [yes/no]"
- "No dead ends identified: [yes/no]"

Do not proceed until the sitemap is complete and validated.
</phase_sitemap>

<phase_content>
## Phase 5: Content Generation

Generate one markdown file per page/post.

See [references/CONTENT-FORMAT.md](references/CONTENT-FORMAT.md) for:
- Frontmatter fields
- Markdown conventions
- Template syntax for non-text elements
- Anti-hallucination patterns

See [references/FORMS-CPTS.md](references/FORMS-CPTS.md) for:
- Form specification format
- Custom post type definitions
- ACF field configuration

### Anti-Hallucination Rules

**Never invent:**
- Company details, history, statistics
- Contact information
- Pricing or financials
- Testimonials or quotes
- Partner/client names

**Use placeholders:**
```markdown
{{needs-input: Company founding year}}
{{placeholder: TEAM SIZE}} professionals
```

**REQUIRED:** Ask for missing information rather than proceeding with gaps. Do not generate content that requires facts you don't have.
</phase_content>

<phase_validation>
## Phase 6: Validation

Run validation scripts after each major phase:

```bash
# Structure validation
python3 scripts/validate_structure.py ./tmp/<project-name>

# Sitemap vs content sync
python3 scripts/validate_sitemap.py ./tmp/<project-name>

# Find pages without CTAs
python3 scripts/find_orphans.py ./tmp/<project-name>

# Find pending/broken links
python3 scripts/find_missing_links.py ./tmp/<project-name>

# Find placeholders needing input
python3 scripts/find_placeholders.py ./tmp/<project-name>

# Generate completion checklist
python3 scripts/generate_checklist.py ./tmp/<project-name>
```

For CPT/ACF generation from YAML:
```bash
python3 scripts/generate_cpt_spec.py ./tmp/<project-name>
```
</phase_validation>

## Output Structure

```
./tmp/<project-name>/
├── strategy/
│   ├── calls-to-action.md
│   ├── audience-analysis.md
│   └── conversion-strategy.md
├── sitemap.md
├── templates/
│   ├── page.md
│   ├── archive.md
│   ├── single.md
│   ├── search.md
│   └── 404.md
├── content/
│   ├── pages/
│   ├── posts/
│   └── <cpt-name>/
├── cpts/
│   ├── source.yaml
│   ├── spec.md
│   └── acf-export.json
├── forms/
│   └── <form-name>.md
├── globals/
│   ├── header.md
│   └── footer.md
└── _validation/
    ├── orphaned-pages.csv
    ├── missing-links.csv
    ├── placeholders.csv
    └── checklist.md
```

## Phase Transitions

When completing a phase, summarize and confirm:

```
## Phase Complete: Strategy

Documented:
- Primary CTA: [action]
- Secondary CTA: [action]
- [N] audience segments with journeys
- Entry point → conversion mapping

**Next:** Creating sitemap based on this strategy.

Ready to proceed?
```

## Example: Anti-Trafficking Nonprofit

**CTAs identified:**
- Primary: Help line for victims (crisis, prominent)
- Secondary: Volunteer sign-up
- Tertiary: Donations

**Two distinct journeys:**

1. **Victim seeking help**
   - Entry: Direct search, mobile, possibly in danger
   - Needs: Clear, fast access to hotline
   - Tone: Calm, reassuring

2. **Potential supporter**
   - Entry: Social share, news article
   - Needs: Impact stories, credibility
   - Tone: Inspiring, urgent but hopeful

**Sitemap accounts for both:**
- Homepage balances both journeys
- "Get Help" optimized for victims
- "Get Involved" for supporters
- All content drives to one of three CTAs

<failed_attempts>
What DOESN'T work:

- **Starting with pages:** "We need an About page" before "What do we want visitors to do?" leads to content without purpose.
- **Inventing details:** Creating plausible-sounding company history, statistics, or testimonials. These always ring false.
- **Dead-end pages:** Pages with no CTA become navigation dead ends. Every page must lead somewhere.
- **"Everyone" as audience:** If you can't name specific audience segments, the site can't speak to anyone effectively.
- **Skipping strategy:** Jumping to sitemap creation without CTA/audience work produces structure without strategy.
</failed_attempts>

## Reference Files

| File | Contents |
|------|----------|
| [STRATEGY.md](references/STRATEGY.md) | CTA, audience, conversion templates |
| [SITEMAP-TEMPLATES.md](references/SITEMAP-TEMPLATES.md) | Sitemap format, template specs |
| [CONTENT-FORMAT.md](references/CONTENT-FORMAT.md) | Content file format, markdown syntax |
| [FORMS-CPTS.md](references/FORMS-CPTS.md) | Form specs, CPT/ACF definitions |

## Technical Context

- **CMS:** WordPress
- **Page Builder:** Divi (content is builder-agnostic)
- **Custom Fields:** ACF Pro
- **Forms:** WS Form (primary), Gravity Forms (secondary)
- **E-commerce:** WooCommerce with Subscriptions/Memberships
