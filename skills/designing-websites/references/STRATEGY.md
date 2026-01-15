# Strategy Phase Reference

This document covers the strategy artifacts produced during website design.

## Core Philosophy

**Interest + Intent → Action**

Every piece of content exists to convert user interest and intent into a specific action. There are no "informational only" pages:
- About/Team page → "Schedule a meeting with someone on our team"
- Annual report → Donations or email signup
- Blog posts → Primary or secondary CTA

## Strategy Documents

Create these files in `strategy/`:

### 1. calls-to-action.md

```yaml
---
primary_cta:
  action: "Schedule a consultation"
  url: /contact
  button_text: "Schedule Your Free Consultation"
secondary_cta:
  action: "Download resource guide"
  url: /resources/guide
  button_text: "Get the Free Guide"
tertiary_ctas:
  - action: "Subscribe to newsletter"
    url: /newsletter
  - action: "Follow on social"
    url: /connect
---

# Calls to Action

## Primary CTA
[Detailed description of the primary action and why it matters]

## Secondary CTA
[Description of secondary action and its role]

## Tertiary CTAs
[Supporting actions and when to use them]
```

### 2. audience-analysis.md

```yaml
---
audiences:
  - name: "Primary Audience Name"
    priority: 1
  - name: "Secondary Audience Name"
    priority: 2
---

# Audience Analysis

## Audience Segment: [Name]

### Demographics
- Who are they?
- What's their context?

### Entry Points
- How do they arrive? (direct, search, social, referral, email)
- What search terms bring them?

### Intent
- What are they looking for?
- What are their expectations?
- What problems are they trying to solve?

### Journey Mapping
- Entry → Discovery → Consideration → Action
- Obstacles to conversion
- Trust signals needed

## Audience Segment: [Name 2]
[Repeat structure for each segment]
```

### 3. conversion-strategy.md

```markdown
# Conversion Strategy

## Entry Point → CTA Mapping

| Entry Point | Primary Path | Secondary Path |
|-------------|--------------|----------------|
| Homepage | Services → Contact | Resources → Newsletter |
| Blog post | Related content → Services | Newsletter signup |
| Search landing | Direct to relevant service | Contact |

## Conversion Funnel

### Awareness Stage
- Content types
- CTAs appropriate at this stage

### Consideration Stage
- Content types
- Trust signals
- CTAs

### Decision Stage
- Final conversion points
- Friction reducers
```

## Workflow Order

**Always follow this sequence:**

1. **Define business goals first** (not audience)
   - What is the PRIMARY call-to-action?
   - What is the secondary CTA?
   - Any tertiary supporting actions?

2. **Analyze audience intent**
   - How do users arrive?
   - What are they looking for?
   - What are their expectations?
   - Map entry points to CTAs
   - Identify distinct user journeys

3. **Create conversion strategy**
   - Map how interest becomes action
   - Identify obstacles
   - Plan trust signals

## Pre-Flight Checklist

Before proceeding to sitemap, confirm:

- [ ] Clear primary CTA defined
- [ ] Secondary CTA defined
- [ ] Target audiences identified with entry points
- [ ] User journeys mapped for each audience
- [ ] Technical requirements noted (forms, integrations)
- [ ] Brand voice/tone understood (if provided)
