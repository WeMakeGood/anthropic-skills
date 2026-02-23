# Content File Format Reference

## File Structure

Each content file uses YAML frontmatter plus semantic markdown:

```yaml
---
title: Page Title
slug: /parent/page-slug
type: page|post|<cpt-name>
template: default|archive|single|<template-name>
parent: /parent-slug
seo_title: SEO Title (if different)
seo_description: Meta description (150-160 chars)
excerpt: Short description for archives
featured_image: Description of ideal image
categories:
  - category-one
tags:
  - tag-one
custom_fields:
  field_name: value
cta_primary: /contact
cta_text: Schedule Your Free Consultation
---

# Page Title

[Content...]

## Take Action

{{button: CTA Text | url=/path | style=primary}}
```

## Frontmatter Fields

### Required Fields

| Field | Description |
|-------|-------------|
| title | Page/post title |
| slug | URL path |
| type | page, post, or CPT name |
| template | Template to use |
| cta_primary | Path to primary CTA page |
| cta_text | Button text for CTA |

### Optional Fields

| Field | Description |
|-------|-------------|
| parent | Parent page slug (for hierarchy) |
| seo_title | Override title for search |
| seo_description | Meta description |
| excerpt | Archive/preview text |
| featured_image | Description for production |
| categories | Taxonomy terms |
| tags | Tag terms |
| custom_fields | ACF field values |

## Markdown Conventions

### Use Native Markdown

Standard markdown for basic elements:

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text** and *italic text*

- Unordered list
- Another item

1. Ordered list
2. Second item

[Link text](/path/to/page)
[External link](https://example.com)

![Alt text](/path/to/image.jpg)

| Column 1 | Column 2 |
|----------|----------|
| Data | Data |
```

### Pending Internal Links

Use `#` for undetermined URLs:

```markdown
Learn more about [our programs](#) and [how to get involved](#).
```

For planned paths not yet created:

```markdown
Read about [our impact](/about/impact) and [annual reports](/resources/annual-reports).
```

## Template Syntax

Use double-curly-brace syntax for elements markdown cannot represent.

### Basic Syntax

```
{{type: content}}
{{type: content | attribute=value}}
```

### Multi-line Blocks

```
{{type: header}}
Content goes here.
Multiple lines supported.
{{/type}}
```

### Element Types

#### Buttons
```
{{button: Schedule a Consultation | url=/contact | style=primary}}
{{button: Learn More | url=/about}}
```

#### Images (Placeholders)
```
{{image: Team photo showing diverse group in modern office}}
{{image: Hero image of customer using product | alt=Customer testimonial}}
```

#### Videos
```
{{video: YouTube testimonial | source=youtube | placeholder=CEO explaining mission}}
```

#### Forms
```
{{form: contact-form}}
{{form: newsletter-signup | style=inline}}
```

#### Charts
```
{{chart: Bar chart of donation growth | type=bar | data=donations-by-year}}
```

#### Callouts
```
{{callout: info}}
Important information here.
{{/callout}}

{{callout: warning}}
Critical warning message.
{{/callout}}
```

#### Card Grids
```
{{card-grid: 3-column}}
{{card: Feature One | icon=heart}}
Description of first feature.
{{/card}}
{{card: Feature Two | icon=shield}}
Description of second feature.
{{/card}}
{{/card-grid}}
```

#### Accordions
```
{{accordion: FAQ Section}}
{{item: How do I donate?}}
Answer about donation process.
{{/item}}
{{item: Where does my money go?}}
Answer about fund allocation.
{{/item}}
{{/accordion}}
```

## Handling Missing Information

The following details must come from the user — do not generate them: company details (founding dates, history, statistics), contact information, pricing or financial figures, testimonials or quotes, partner/client names, legal claims or certifications.

### Placeholder Syntax

For missing information:

```markdown
{{needs-input: Company founding year and brief history}}

{{placeholder: COMPANY NAME}} has been serving {{placeholder: REGION}}
since {{placeholder: YEAR}}.
```

### Verification Blocks

For content requiring confirmation:

```markdown
{{verify: The following statistics should be confirmed}}
We've helped over {{placeholder: NUMBER}} families since {{placeholder: YEAR}}.
{{/verify}}
```

### Ask Before Proceeding

When details are needed:

```
To write the About page, I need:
- When was the organization founded?
- Key milestones or achievements?
- Specific statistics to highlight?

I can write around these if unavailable, but real details make it stronger.
```

## Example Content File

```yaml
---
title: Our Services
slug: /services
type: page
template: page
seo_title: Professional Services | Company Name
seo_description: Discover our comprehensive range of services designed to help you achieve your goals.
excerpt: Explore our full range of professional services.
featured_image: Professional team collaborating on client project
cta_primary: /contact
cta_text: Get Started Today
---

# Our Services

We provide comprehensive solutions tailored to your needs.

{{image: Team working with client in modern office setting}}

## Service Categories

{{card-grid: 3-column}}
{{card: Consulting | icon=lightbulb}}
Strategic guidance to help you make informed decisions.
{{/card}}
{{card: Implementation | icon=tools}}
Hands-on support to bring your vision to life.
{{/card}}
{{card: Support | icon=headset}}
Ongoing assistance to ensure continued success.
{{/card}}
{{/card-grid}}

## Why Choose Us

- Experienced team with proven track record
- Customized approach for every client
- Commitment to measurable results

{{callout: info}}
{{placeholder: UNIQUE VALUE PROPOSITION - what makes this company different}}
{{/callout}}

## Take Action

Ready to get started? Let's discuss how we can help.

{{button: Get Started Today | url=/contact | style=primary}}

Or [browse our case studies](#) to see our work in action.
```
