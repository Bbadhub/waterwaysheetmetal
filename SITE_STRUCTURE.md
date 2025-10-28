# Water Ways Sheet Metal - Site Structure & Navigation
# DESIGN-002 Deliverable
# Created: 2025-10-28
# Version: 1.0
# Pattern: Pattern-CONTEXT-002

---

## Overview

This document defines the complete site navigation structure, URL architecture, and breadcrumb strategy for waterwayssheetmetal.com. The structure balances user experience (easy navigation) with SEO requirements (semantic URLs, clear hierarchy).

**Total Pages:** 14 core pages + expandable portfolio
**Navigation Depth:** Maximum 3 clicks to any content
**URL Strategy:** Semantic, keyword-rich, hierarchical

---

## Primary Navigation (Header)

### Desktop Navigation Structure

```
┌─────────────────────────────────────────────────────────────┐
│  [Logo]  Home  Services ▼  Portfolio  About  FAQ  Contact  │
│                                            [Get a Quote →]   │
└─────────────────────────────────────────────────────────────┘
```

**Main Menu Items:**
1. **Home** - `/` or `/index.html`
2. **Services** (Dropdown) - 4 service pages
3. **Portfolio** - `/portfolio.html` or `/portfolio/`
4. **About** - `/about.html`
5. **FAQ** - `/faq.html`
6. **Contact** - `/contact.html`
7. **Get a Quote** (CTA Button) - `/contact.html#quote-form`

---

### Services Dropdown Menu

```
Services ▼
├── Chimney Caps & Tops
├── Flashing & Weatherproofing
├── Roofing & Gutters
└── Custom Architectural Metalwork
```

**Service Page URLs:**
```
/services/chimney-caps.html
/services/flashing.html
/services/roofing-gutters.html
/services/custom-metalwork.html
```

---

### Mobile Navigation

**Hamburger Menu (☰):**
```
☰ Menu
├── Home
├── Services >
│   ├── Chimney Caps & Tops
│   ├── Flashing & Weatherproofing
│   ├── Roofing & Gutters
│   └── Custom Architectural Metalwork
├── Portfolio
├── About
├── FAQ
├── Contact
└── [Get a Quote Button]
```

**Behavior:**
- Hamburger icon (☰) top-right on mobile
- Full-screen overlay menu
- Services expands/collapses in-place
- Close with X or tap outside

---

## Footer Navigation

### Four-Column Layout

```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│  Company    │  Services   │  Resources  │  Contact    │
├─────────────┼─────────────┼─────────────┼─────────────┤
│ About Us    │ All Services│ FAQs        │ (479) 957-  │
│ Our Process │ Chimney Caps│ Maintenance │  3794       │
│ Why Copper  │ Flashing    │ Care Tips   │             │
│ Testimonials│ Roofing     │ Blog        │ Ray@Water...│
│             │ Custom Work │ Portfolio   │             │
│             │             │             │ Watts, OK   │
│             │ Get Quote → │             │ 74964       │
├─────────────┴─────────────┴─────────────┴─────────────┤
│ © 2025 Water Ways Sheet Metal | Privacy Policy | Terms │
└─────────────────────────────────────────────────────────┘
```

### Footer Link Structure

**Company Column:**
- About Us → `/about.html`
- Our Process → `/about.html#process`
- Why Copper → `/about.html#why-copper`
- Testimonials → `/about.html#testimonials`

**Services Column:**
- All Services → `/services/` (overview page)
- Chimney Caps & Tops → `/services/chimney-caps.html`
- Flashing & Weatherproofing → `/services/flashing.html`
- Roofing & Gutters → `/services/roofing-gutters.html`
- Custom Architectural Metalwork → `/services/custom-metalwork.html`
- Get a Quote (CTA) → `/contact.html#quote-form`

**Resources Column:**
- FAQs → `/faq.html`
- Maintenance & Care Tips → `/resources/maintenance.html` (future)
- Blog/News → `/blog/` (future)
- Portfolio → `/portfolio.html`

**Contact Column:**
- Phone: (479) 957-3794 (clickable tel: link)
- Email: Ray@WaterwaysSheetMetal.com (clickable mailto: link)
- Address: Watts, OK 74964
- Map link (optional)

**Legal Links (bottom):**
- Privacy Policy → `/privacy.html`
- Terms of Service → `/terms.html`

---

## Complete URL Map

### Core Pages (14 pages)

```
Homepage:
/                                   (or /index.html)

Services (4 pages):
/services/chimney-caps.html
/services/flashing.html
/services/roofing-gutters.html
/services/custom-metalwork.html

Portfolio:
/portfolio.html                     (main gallery + featured projects)

About:
/about.html                         (single long-scroll page with anchors)

FAQ:
/faq.html                           (single page, expandable accordions)

Contact:
/contact.html                       (contact form, info, map)

Legal (2 pages):
/privacy.html
/terms.html
```

**Total Core Pages:** 14

---

### Portfolio Expansion (Future)

**Option A: Single Page (Launch V1)**
```
/portfolio.html                     (All projects on one page)
```

**Option B: Individual Project Pages (V2)**
```
/portfolio.html                     (Grid overview)
/portfolio/minnesota-chimney-shroud.html
/portfolio/ohio-french-country-caps.html
/portfolio/north-carolina-custom-cap.html
/portfolio/mid-continent-tower-tulsa.html
```

**Recommendation:** Launch with Option A (single page), expand to Option B post-launch as portfolio grows.

---

### Future Pages (Backlog)

```
/resources/maintenance.html         (Care tips for copper)
/blog/                             (News, projects, updates)
/about/team.html                   (If team photos added)
/services/                         (Services overview page)
```

---

## URL Structure Guidelines

### URL Formatting Rules

**✅ DO:**
- Use lowercase only: `/services/chimney-caps.html`
- Use hyphens for spaces: `chimney-caps` not `chimney_caps` or `chimneycaps`
- Keep URLs short and descriptive: `/services/flashing.html`
- Include keywords: `chimney-caps` (SEO value)
- Use semantic names: `/about.html` not `/page2.html`

**❌ DON'T:**
- Use parameters: `/page.php?id=123`
- Use underscores: `/chimney_caps.html`
- Use mixed case: `/ChimneyCaps.html`
- Use numbers: `/service-1.html`
- Create deep nesting: `/services/residential/chimney/caps/custom.html`

---

### File Extension: .html

**Decision:** Use `.html` extensions (not extensionless or `.php`)

**Rationale:**
- Static HTML site (no server-side processing)
- Clear file type in browser
- Works on all hosting (no .htaccess rewriting needed)
- SEO-neutral (Google doesn't care)
- Simplicity for deployment

---

## Breadcrumb Strategy

### Pages with Breadcrumbs

**Service Pages:**
```
Home > Services > Chimney Caps & Tops
Home > Services > Flashing & Weatherproofing
Home > Services > Roofing & Gutters
Home > Services > Custom Architectural Metalwork
```

**Portfolio (if individual pages):**
```
Home > Portfolio > Minnesota Chimney Shroud
Home > Portfolio > Ohio French Country Caps
```

**Schema Markup:**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://waterwayssheetmetal.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Services",
      "item": "https://waterwayssheetmetal.com/services/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Chimney Caps & Tops",
      "item": "https://waterwayssheetmetal.com/services/chimney-caps.html"
    }
  ]
}
```

### Pages WITHOUT Breadcrumbs

- Homepage (top level)
- About (top level)
- FAQ (top level)
- Contact (top level)
- Privacy/Terms (utility pages)

---

## XML Sitemap Structure

### sitemap.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

  <!-- Homepage - Highest Priority -->
  <url>
    <loc>https://waterwayssheetmetal.com/</loc>
    <lastmod>2025-10-28</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>

  <!-- Services - High Priority -->
  <url>
    <loc>https://waterwayssheetmetal.com/services/chimney-caps.html</loc>
    <lastmod>2025-10-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://waterwayssheetmetal.com/services/flashing.html</loc>
    <lastmod>2025-10-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://waterwayssheetmetal.com/services/roofing-gutters.html</loc>
    <lastmod>2025-10-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://waterwayssheetmetal.com/services/custom-metalwork.html</loc>
    <lastmod>2025-10-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>

  <!-- Portfolio -->
  <url>
    <loc>https://waterwayssheetmetal.com/portfolio.html</loc>
    <lastmod>2025-10-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>

  <!-- About, FAQ, Contact -->
  <url>
    <loc>https://waterwayssheetmetal.com/about.html</loc>
    <lastmod>2025-10-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://waterwayssheetmetal.com/faq.html</loc>
    <lastmod>2025-10-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://waterwayssheetmetal.com/contact.html</loc>
    <lastmod>2025-10-28</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.7</priority>
  </url>

  <!-- Legal Pages -->
  <url>
    <loc>https://waterwayssheetmetal.com/privacy.html</loc>
    <lastmod>2025-10-28</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://waterwayssheetmetal.com/terms.html</loc>
    <lastmod>2025-10-28</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>

</urlset>
```

**Priority Guidelines:**
- Homepage: 1.0
- Service pages: 0.9 (primary conversion pages)
- Portfolio: 0.8 (important for lead generation)
- About/Contact: 0.7 (supporting pages)
- FAQ: 0.6 (helpful but not primary)
- Legal: 0.3 (required but low priority)

---

## Navigation UX Considerations

### Active State Indicators

**Current Page Highlighting:**
```css
/* Active nav item */
.nav-link.active {
  color: var(--color-copper-primary);
  font-weight: var(--font-weight-semibold);
  border-bottom: 2px solid var(--color-copper-primary);
}
```

**Breadcrumb Current Page:**
```css
/* Last breadcrumb (current page) */
.breadcrumb-item:last-child {
  color: var(--color-gray-medium);
  pointer-events: none;
}
```

---

### Dropdown Behavior

**Desktop:**
- Hover to reveal dropdown
- Click "Services" to go to `/services/` overview (future)
- Dropdown persists while mouse over menu or dropdown
- 300ms delay before closing

**Mobile:**
- Tap to expand/collapse
- No hover states
- Tappable area minimum 44x44px

---

### Skip Navigation

**Accessibility:**
```html
<a href="#main-content" class="skip-nav">
  Skip to main content
</a>
```

**Behavior:**
- Hidden visually until keyboard focus
- Jumps to main content (bypasses header nav)
- WCAG 2.1 compliance

---

## SEO Considerations

### Internal Linking Strategy

**Homepage Links to:**
- All 4 service pages (primary navigation)
- Portfolio (featured projects section)
- About (company overview section)
- Contact (footer + CTA buttons)

**Service Pages Link to:**
- Homepage (breadcrumb)
- Other service pages (related services sidebar/footer)
- Portfolio (project examples using that service)
- Contact (CTA: "Request quote for [service]")

**Portfolio Links to:**
- Service pages (projects organized by service type)
- Individual project pages (future)
- Contact (CTA on each project: "Start your project")

**About Page Links to:**
- Services (from "Our Process" section)
- Portfolio (from "Our Work" section)
- Contact (CTA: "Work with us")

**FAQ Links to:**
- Service pages (service-specific questions)
- About (company questions)
- Contact (form questions)

---

### Anchor Links (On-Page Navigation)

**About Page:**
```
/about.html#story
/about.html#process
/about.html#why-copper
/about.html#team
/about.html#testimonials
```

**FAQ Page:**
```
/faq.html#general
/faq.html#materials
/faq.html#pricing
/faq.html#process
/faq.html#installation
/faq.html#maintenance
```

**Contact Page:**
```
/contact.html#quote-form
/contact.html#location
```

---

## Mobile Navigation Patterns

### Sticky Header (Optional)

**Behavior:**
- Header shrinks on scroll (60px → 50px)
- Logo scales down
- CTA button remains visible
- Hamburger menu always accessible

**Implementation:**
```css
.header {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  transition: var(--transition-all);
}

.header.scrolled {
  box-shadow: var(--shadow-md);
  padding: var(--space-sm) 0;
}
```

---

## URL Structure Summary

| Page Type | URL Pattern | Example |
|-----------|-------------|---------|
| Homepage | `/` | `/index.html` |
| Service | `/services/[keyword].html` | `/services/chimney-caps.html` |
| Portfolio | `/portfolio.html` | `/portfolio.html` |
| About | `/about.html` | `/about.html` |
| FAQ | `/faq.html` | `/faq.html` |
| Contact | `/contact.html` | `/contact.html` |
| Legal | `/[type].html` | `/privacy.html` |
| Future Blog | `/blog/[slug].html` | `/blog/copper-care-tips.html` |
| Future Project | `/portfolio/[slug].html` | `/portfolio/minnesota-project.html` |

---

## DESIGN-002 Deliverables ✅

- ✅ **Site Navigation Map**
  - Header navigation structure defined
  - Footer navigation structure defined
  - Mobile navigation pattern documented
  - Dropdown menus specified

- ✅ **URL Structure Defined**
  - 14 core pages mapped with semantic URLs
  - URL formatting guidelines established
  - Future expansion paths planned
  - `.html` extension decision documented

- ✅ **Breadcrumb Strategy**
  - Pages requiring breadcrumbs identified
  - Schema markup template created
  - Active state styling planned

- ✅ **Preliminary Sitemap**
  - sitemap.xml structure created
  - Priority levels assigned
  - Change frequency defined
  - Ready for implementation in DEV-001

---

## Next Steps (DEV-001)

With navigation structure complete, HTML development can proceed:

1. Create HTML templates with navigation
2. Implement breadcrumb markup
3. Build service page hierarchy
4. Generate sitemap.xml
5. Implement mobile hamburger menu (JavaScript)

**All navigation and URL decisions are now documented and ready for implementation.**

---

**Status:** DESIGN-002 Complete ✅
**Created:** 2025-10-28
**Version:** 1.0
**Pattern:** Pattern-CONTEXT-002
**Total Pages Defined:** 14 core + expandable portfolio
