# Designing Websites Skill

A comprehensive skill for planning website content strategy and generating all content assets before development begins.

## Overview

This skill flips the traditional website design process: instead of starting with logos and visual design, it starts with **business goals, user intent, and calls-to-action**, then works backward to create all the content artifacts needed.

### What It Produces

A complete project folder containing:

- **Strategy documents** - CTAs, audience analysis, conversion strategy
- **Sitemap** - Flow-based structure with no dead ends
- **Template specs** - Requirements for each page template
- **Content files** - One markdown file per page/post
- **Form specs** - Complete form definitions
- **CPT/ACF specs** - Custom post type and field configurations
- **Validation reports** - Automated checks for completeness

## Quick Start

### For Claude Users

Simply ask Claude to help design a website:

```
Help me plan a website for [organization name]
```

Or invoke directly:

```
/designing-websites
```

### For Developers

The skill generates a project folder at `./tmp/<project-name>/` with this structure:

```
./tmp/<project-name>/
├── strategy/
│   ├── calls-to-action.md
│   ├── audience-analysis.md
│   └── conversion-strategy.md
├── sitemap.md
├── templates/
├── content/
│   ├── pages/
│   └── posts/
├── forms/
├── globals/
├── cpts/
└── _validation/
```

## The Process

### Phase 1: Gather Requirements

Before any files are created, the skill collects:

- Business context and unique value proposition
- Primary, secondary, and tertiary CTAs
- Target audience segments and entry points
- Technical requirements (forms, e-commerce, integrations)
- Existing content and brand guidelines

### Phase 2-3: Strategy

Creates documentation for:

- **Calls-to-Action** - What actions visitors should take, in priority order
- **Audience Analysis** - Who visits, how they arrive, what they need
- **Conversion Strategy** - How interest becomes action

### Phase 4: Sitemap

Builds a flow-based sitemap where:

- Every page has an exit path toward a CTA
- No dead ends exist
- Templates are assigned to each page
- Parent/child relationships are defined

### Phase 5: Content Generation

Produces one markdown file per page with:

- YAML frontmatter (title, slug, template, SEO, CTA assignment)
- Semantic markdown content
- Template syntax for non-text elements
- Placeholders for missing information (never fabricated)

### Phase 6: Validation

Runs automated scripts to verify:

- Project structure completeness
- Sitemap/content file synchronization
- CTA coverage (no orphaned pages)
- Link integrity
- Placeholder tracking

## Content Format

### Frontmatter

```yaml
---
title: Page Title
slug: /path/to/page
type: page
template: default
seo_description: Meta description (150-160 chars)
cta_primary: /contact
cta_text: Schedule a Consultation
---
```

### Template Syntax

For elements markdown can't represent:

```markdown
{{button: Schedule a Consultation | url=/contact | style=primary}}

{{image: Team photo in modern office setting}}

{{callout: info}}
Important information here.
{{/callout}}

{{form: contact-form}}
```

### Placeholder Patterns

The skill never fabricates information. Missing data uses:

```markdown
{{needs-input: Company founding year}}
{{placeholder: TEAM SIZE}} professionals
{{verify: Statistics should be confirmed}}
```

## Validation Scripts

All scripts work without external dependencies (no pip install required).

### Structure Validation

```bash
python3 scripts/validate_structure.py ./tmp/<project-name>
```

Checks required folders and files exist.

### Sitemap Validation

```bash
python3 scripts/validate_sitemap.py ./tmp/<project-name>
```

Cross-references sitemap entries with content files.

### Find Orphaned Pages

```bash
python3 scripts/find_orphans.py ./tmp/<project-name>
```

Finds pages without clear CTAs. Outputs `_validation/orphaned-pages.csv`.

### Find Missing Links

```bash
python3 scripts/find_missing_links.py ./tmp/<project-name>
```

Finds pending (`#`) and broken internal links. Outputs `_validation/missing-links.csv`.

### Find Placeholders

```bash
python3 scripts/find_placeholders.py ./tmp/<project-name>
```

Finds all content requiring user input. Outputs `_validation/placeholders.csv`.

### Generate Checklist

```bash
python3 scripts/generate_checklist.py ./tmp/<project-name>
```

Creates completion status report at `_validation/checklist.md`.

### Generate CPT Spec

```bash
python3 scripts/generate_cpt_spec.py ./tmp/<project-name>
```

Generates `cpts/spec.md` and `cpts/acf-export.json` from `cpts/source.yaml`.

## Best Practices

### For Content Strategists

1. **Start with CTAs, not pages** - Define what you want visitors to do before deciding what pages you need
2. **Map audience journeys** - Different visitors need different paths
3. **No dead ends** - Every page should lead somewhere useful
4. **Use placeholders** - Never invent statistics, quotes, or details

### For Developers

1. **Run validation after each phase** - Catch issues early
2. **Content is builder-agnostic** - Works with any CMS/page builder
3. **Template syntax is searchable** - Easy to find and replace
4. **CSV outputs integrate with project management** - Import into tracking tools

### For Project Managers

1. **Checklist shows true status** - Automated, not self-reported
2. **Placeholders track dependencies** - Know what's blocked on client input
3. **Sitemap defines scope** - Clear list of pages to produce

## Technical Context

This skill assumes:

- **CMS:** WordPress
- **Page Builder:** Divi (but content is builder-agnostic)
- **Custom Fields:** ACF Pro
- **Forms:** WS Form (primary), Gravity Forms (secondary)
- **E-commerce:** WooCommerce with Subscriptions/Memberships

Adjust these assumptions in the strategy phase if using different tools.

## File Reference

| File | Purpose |
|------|---------|
| `SKILL.md` | Main skill instructions for Claude |
| `references/STRATEGY.md` | Strategy phase templates |
| `references/SITEMAP-TEMPLATES.md` | Sitemap and template specs |
| `references/CONTENT-FORMAT.md` | Content file format and syntax |
| `references/FORMS-CPTS.md` | Form and CPT specifications |
| `scripts/validate_structure.py` | Check project structure |
| `scripts/validate_sitemap.py` | Cross-reference sitemap/content |
| `scripts/find_orphans.py` | Find pages without CTAs |
| `scripts/find_missing_links.py` | Find broken/pending links |
| `scripts/find_placeholders.py` | Find items needing input |
| `scripts/generate_checklist.py` | Generate status report |
| `scripts/generate_cpt_spec.py` | Generate CPT/ACF config |

## License

MIT
