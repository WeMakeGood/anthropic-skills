# Forms and Custom Post Types Reference

## Form Specification Format

Create form files in `forms/`:

```yaml
---
form_name: contact-form
form_title: Contact Us
plugin: ws-form
multi_step: false
submit_button_text: Send Message
redirect_url: /thank-you/contact
---

# Contact Form

## Purpose
Brief description of form purpose and usage context.

## Fields

| Field | Type | Required | Validation | Notes |
|-------|------|----------|------------|-------|
| name | text | yes | min 2 chars | Full name |
| email | email | yes | valid email | For response |
| phone | tel | no | valid phone | Optional callback |
| message | textarea | yes | min 10 chars | Their inquiry |

## Conditional Logic
- If `inquiry_type` = "Partnership", show `organization_name` field
- If `inquiry_type` = "Volunteer", redirect to volunteer form

## On Submit

### Email Notifications

**To Admin:**
- Recipients: info@example.org
- Subject: New Contact: {{name}}
- Body:
  ```
  New inquiry received:

  Name: {{name}}
  Email: {{email}}
  Phone: {{phone}}

  Message:
  {{message}}
  ```

**To User:**
- Subject: Thank you for contacting us
- Body:
  ```
  Hi {{name}},

  Thank you for reaching out. We'll respond within 2 business days.

  - The Team
  ```

### Integrations
- Add to Mailchimp list: "General Inquiries"

## Success State
Redirect to: /thank-you/contact
```

## Multi-Step Form Example

```yaml
---
form_name: volunteer-application
form_title: Volunteer Application
plugin: ws-form
multi_step: true
submit_button_text: Submit Application
redirect_url: /thank-you/volunteer
---

# Volunteer Application

## Purpose
Collect volunteer information and availability.

## Step 1: Personal Information

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| first_name | text | yes | |
| last_name | text | yes | |
| email | email | yes | |
| phone | tel | yes | |

## Step 2: Background

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| experience | textarea | no | Relevant experience |
| skills | checkbox | no | Options: Admin, Events, Outreach |
| reference | text | no | Reference contact |

## Step 3: Availability

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| availability | checkbox | yes | Days available |
| hours_per_week | select | yes | 1-5, 5-10, 10+ |
| start_date | date | yes | When can you start |

## Conditional Logic
- If `skills` includes "Events", show `event_experience` field

## On Submit
[Email and integration specs...]
```

## Custom Post Types Specification

Create `cpts/spec.md`:

```markdown
# Custom Post Types and Fields Specification

## Custom Post Types

### Team Members
- **Slug:** team-member
- **Singular:** Team Member
- **Plural:** Team Members
- **Public:** Yes
- **Has Archive:** Yes (/team/)
- **Supports:** title, editor, thumbnail
- **Menu Icon:** dashicons-groups

### Programs
- **Slug:** program
- **Singular:** Program
- **Plural:** Programs
- **Public:** Yes
- **Has Archive:** Yes (/programs/)
- **Supports:** title, editor, thumbnail, excerpt
- **Menu Icon:** dashicons-portfolio

## Custom Taxonomies

### Department
- **Slug:** department
- **Applies to:** team-member
- **Hierarchical:** Yes
- **Terms:** Leadership, Operations, Programs, Development

### Program Type
- **Slug:** program-type
- **Applies to:** program
- **Hierarchical:** Yes
- **Terms:** Education, Outreach, Support Services

## ACF Field Groups

### Team Member Details
**Location:** team-member post type

| Field Name | Field Type | Required | Notes |
|------------|------------|----------|-------|
| job_title | text | yes | Role/position |
| email | email | no | Public contact |
| linkedin_url | url | no | Profile link |
| bio_short | textarea | yes | Archive cards (150 chars) |
| start_year | number | no | Year joined |

### Program Details
**Location:** program post type

| Field Name | Field Type | Required | Notes |
|------------|------------|----------|-------|
| program_status | select | yes | Active, Paused, Completed |
| impact_stat | text | no | e.g., "500 people served" |
| cta_override | link | no | Override default CTA |
| gallery | gallery | no | Program photos |
```

## ACF JSON Export

The skill generates `cpts/acf-export.json` for direct WordPress import:

```json
[
  {
    "key": "group_team_member_details",
    "title": "Team Member Details",
    "fields": [
      {
        "key": "field_job_title",
        "label": "Job Title",
        "name": "job_title",
        "type": "text",
        "required": 1
      },
      {
        "key": "field_email",
        "label": "Email",
        "name": "email",
        "type": "email",
        "required": 0
      }
    ],
    "location": [
      [
        {
          "param": "post_type",
          "operator": "==",
          "value": "team-member"
        }
      ]
    ]
  }
]
```

## Supported ACF Field Types

| Type | Usage |
|------|-------|
| text | Short text input |
| textarea | Multi-line text |
| number | Numeric values |
| email | Email addresses |
| url | URLs |
| password | Masked input |
| wysiwyg | Rich text editor |
| select | Dropdown options |
| checkbox | Multiple choices |
| radio | Single choice |
| true_false | Boolean toggle |
| link | URL with title/target |
| date_picker | Date selection |
| image | Single image |
| gallery | Multiple images |
| file | File upload |
| relationship | Post relationships |
| taxonomy | Taxonomy terms |
| user | User selection |
| repeater | Repeating field sets |
| group | Field grouping |

## WordPress/Technical Context

### CMS and Tools
- **CMS:** WordPress
- **Page Builder:** Divi (content is builder-agnostic markdown)
- **Custom Fields:** ACF Pro
- **Forms:** WS Form (primary), Gravity Forms (secondary)
- **E-commerce:** WooCommerce with Subscriptions/Memberships
