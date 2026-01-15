# Sitemap and Templates Reference

## Sitemap Structure

Create `sitemap.md` in the project root with this structure:

```yaml
---
site_name: "Project Name"
base_url: https://example.org
last_updated: YYYY-MM-DD
---

# Sitemap

## Primary Navigation

### Home (/)
- **Template:** homepage
- **CTA:** Primary CTA prominent, secondary in hero
- **Children:** None

### About (/about/)
- **Template:** page
- **CTA:** Secondary (schedule meeting with team)
- **Children:**
  - Team (/about/team/) - archive template
  - Mission (/about/mission/)
  - History (/about/history/)

### Services (/services/)
- **Template:** archive
- **CTA:** Primary
- **Children:**
  - Service One (/services/service-one/)
  - Service Two (/services/service-two/)

### Resources (/resources/)
- **Template:** archive
- **CTA:** Secondary (download/subscribe)
- **Children:**
  - Blog (/resources/blog/) - posts archive
  - Guides (/resources/guides/)

### Contact (/contact/)
- **Template:** page
- **CTA:** Primary (this IS the conversion)
- **Form:** contact-form

## Utility Pages

### Search Results (/search/)
- **Template:** search

### 404 (/404/)
- **Template:** 404
- **CTA:** Return to homepage or primary CTA

### Thank You Pages
- /thank-you/contact/
- /thank-you/newsletter/
```

## Sitemap Rules

1. **No dead ends** - Every page connects to the conversion funnel
2. **Clear hierarchy** - Parent/child relationships defined
3. **Template assignment** - Every page has a template
4. **CTA assignment** - Every page has a designated CTA

## Template Specifications

Create template files in `templates/`:

### page.md (Default Page Template)

```yaml
---
template_name: page
used_by: General content pages
---

# Page Template

## Layout
- Header (global)
- Hero section (optional)
- Main content area
- Sidebar (optional, configurable)
- CTA section
- Footer (global)

## Required Elements
- H1 title
- Main content
- CTA block before footer

## Dynamic Content
- Breadcrumbs based on hierarchy
- Related content (optional)

## Mobile Considerations
- Single column layout
- CTA sticky or prominent
```

### archive.md (Archive Template)

```yaml
---
template_name: archive
used_by: Category listings, CPT archives
---

# Archive Template

## Layout
- Header (global)
- Archive title and description
- Filter/sort controls (if applicable)
- Item grid/list
- Pagination
- CTA section
- Footer (global)

## Item Display
- Featured image
- Title (linked)
- Excerpt
- Meta (date, category, etc.)

## Pagination
- Numbered pages
- Previous/Next
- Items per page: configurable
```

### single.md (Single Post Template)

```yaml
---
template_name: single
used_by: Blog posts, news items
---

# Single Post Template

## Layout
- Header (global)
- Featured image (full width or contained)
- Title and meta
- Content area
- Author bio (optional)
- Related posts
- CTA section
- Comments (if enabled)
- Footer (global)

## Meta Display
- Publication date
- Author
- Categories
- Reading time (optional)

## Content Elements
- Full post content
- Inline images
- Pull quotes
- Embedded media
```

### search.md (Search Results Template)

```yaml
---
template_name: search
used_by: Search results page
---

# Search Results Template

## Layout
- Header (global)
- Search form (pre-filled)
- Results count
- Results list
- Pagination
- No results state
- Footer (global)

## Result Display
- Title (linked)
- Excerpt with highlighted terms
- Content type indicator
- URL path

## No Results State
- Helpful message
- Alternative actions (browse categories, contact)
```

### 404.md (Error Template)

```yaml
---
template_name: 404
used_by: Page not found
---

# 404 Template

## Layout
- Header (global)
- Error message
- Helpful navigation
- Search form
- Footer (global)

## Content
- Friendly error message
- Links to:
  - Homepage
  - Main sections
  - Search
- Primary CTA (if appropriate)
```

### Custom Post Type Templates

For each CPT, create a template file:

```yaml
---
template_name: team-member
used_by: Team member single pages
cpt: team-member
---

# Team Member Template

## Layout
- Header (global)
- Photo (large)
- Name and title
- Bio content
- Contact info
- Related team members (optional)
- CTA (schedule meeting)
- Footer (global)

## Fields Displayed
- job_title (ACF)
- email (ACF)
- linkedin_url (ACF)
- bio (editor content)
```
