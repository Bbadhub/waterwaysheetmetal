# Water Ways Sheet Metal - Homepage Wireframe
# DESIGN-003 Deliverable
# Created: 2025-10-28
# Version: 1.0
# Pattern: Pattern-CONTEXT-002

---

## Overview

This document provides a detailed wireframe (structural blueprint) for the Water Ways Sheet Metal homepage (`/index.html`). The wireframe defines content hierarchy, section order, and layout patterns without detailed visual design.

**Goal:** Convert visitors into leads through clear value proposition, portfolio showcase, and strong CTAs
**Key Conversion Points:** "Get a Quote" buttons, phone number prominence, contact form
**Content Source:** CONTENT_COPY.md (Homepage section - 16,000+ words ready)

---

## Homepage Sections (Top to Bottom)

**Section Order:**
1. Header Navigation (sticky)
2. Hero Section (above fold)
3. About Preview (trust building)
4. Services Overview (4 cards)
5. Featured Projects Gallery
6. Why Choose Water Ways (3 columns)
7. Process Overview (4 steps)
8. Testimonials (3 customer quotes)
9. Final CTA Section
10. Footer Navigation

**Total Sections:** 10
**Estimated Page Length:** 4-5 screen heights (scroll depth)

---

## Section 1: Header Navigation

```
┌─────────────────────────────────────────────────────────────────┐
│  ┌────┐  Home  Services ▼  Portfolio  About  FAQ  Contact      │
│  │Logo│                                   [Get a Quote →]       │
│  └────┘                                                          │
└─────────────────────────────────────────────────────────────────┘
```

**Layout:**
- **Desktop:** Horizontal navigation, logo left, CTA button right
- **Mobile:** Logo left, hamburger menu (☰) right
- **Background:** White with 1px bottom border (#E0E0E0)
- **Height:** 80px desktop, 60px mobile
- **Position:** Sticky (follows scroll)

**Elements:**
- Logo: Waterways-Logo-Header-Transparent.png (48KB, already downloaded)
- Navigation links: Charcoal text, copper hover
- CTA button: Copper background, white text

**Behavior:**
- Header shrinks slightly on scroll (sticky)
- Dropdown appears on Services hover
- CTA button always visible

---

## Section 2: Hero Section (Above Fold)

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│   ┌──────────────────────────────────┐  ┌────────────────┐   │
│   │                                  │  │                │   │
│   │  HEADLINE (H1 - Playfair 48px)  │  │   Hero Image   │   │
│   │  Master Craftsmen. Modern        │  │   (Copper      │   │
│   │  Technology. Timeless Results.   │  │    Work)       │   │
│   │                                  │  │                │   │
│   │  SUBHEADLINE (18px - Inter)     │  │   720x540px    │   │
│   │  Custom copper chimney caps,     │  │                │   │
│   │  flashing, and architectural     │  │                │   │
│   │  metalwork serving AR, OK, MO    │  │                │   │
│   │                                  │  └────────────────┘   │
│   │  [Get a Free Quote →]            │                        │
│   │  [View Our Work]  [(479) 957-..  │                        │
│   │                                  │                        │
│   └──────────────────────────────────┘                        │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

**Layout:**
- **Desktop:** 60/40 split (text left, image right)
- **Mobile:** Stack (text above, image below)
- **Background:** White
- **Padding:** 96px top/bottom (desktop), 64px (mobile)

**Content:**
- **H1 Headline:** "Master Craftsmen. Modern Technology. Timeless Results."
- **Subheadline:** "Custom copper chimney caps, flashing, roofing, and architectural metalwork serving Northwest Arkansas and beyond"
- **Primary CTA:** "Get a Free Quote" (copper button)
- **Secondary CTA:** "View Our Work" (outline button)
- **Phone Number:** (479) 957-3794 (clickable, prominent)

**Hero Image:**
- **Source:** `images/hero/pa080064.jpg` or `images/hero/copper-roof-on-turret-1.png`
- **Size:** 720x540px (4:3 aspect ratio)
- **Alt Text:** "Custom copper chimney cap with French curve patina on residential home"
- **Shadow:** --shadow-2xl for depth

**Stats Bar (Optional Below Hero):**
```
┌────────────┬────────────┬────────────┬────────────┐
│  20+ Years │ 100% Custom│ Nationwide │  Premium   │
│ Experience │ Fabrication│  Shipping  │  Materials │
└────────────┴────────────┴────────────┴────────────┘
```

---

## Section 3: About Preview

```
┌─────────────────────────────────────────────────────────────┐
│                       ABOUT WATER WAYS                      │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Headline (H2 - Playfair 40px)                      │   │
│  │  "21st Century Technology Meets Centuries-Old       │   │
│  │   Craftsmanship"                                    │   │
│  │                                                      │   │
│  │  Body Copy (2-3 paragraphs from CONTENT_COPY.md)    │   │
│  │  - Premier copper craftsmen                         │   │
│  │  - Protecting homes from water penetration          │   │
│  │  - Ray & Natalie Hines (husband/wife team)          │   │
│  │                                                      │   │
│  │  [Learn More About Us →]                            │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

**Layout:**
- **Desktop:** Centered column, max-width 720px
- **Mobile:** Full width with padding
- **Background:** Light gray (#F5F5F5)
- **Padding:** 64px top/bottom

**Content:**
- **H2:** "21st Century Technology Meets Centuries-Old Craftsmanship"
- **Body:** 2-3 paragraphs introducing company, owners, philosophy
- **CTA:** "Learn More About Us" (link to /about.html)

---

## Section 4: Services Overview (4 Cards)

```
┌───────────────────────────────────────────────────────────────┐
│                      OUR SERVICES                             │
│                                                               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│  │ [Icon]   │  │ [Icon]   │  │ [Icon]   │  │ [Icon]   │     │
│  │ Chimney  │  │ Flashing │  │ Roofing &│  │  Custom  │     │
│  │  Caps    │  │    &     │  │  Gutters │  │Metalwork │     │
│  │          │  │Weatherpr.│  │          │  │          │     │
│  │ Brief    │  │ Brief    │  │ Brief    │  │ Brief    │     │
│  │ descrip. │  │ descrip. │  │ descrip. │  │ descrip. │     │
│  │          │  │          │  │          │  │          │     │
│  │[Learn →] │  │[Learn →] │  │[Learn →] │  │[Learn →] │     │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘     │
└───────────────────────────────────────────────────────────────┘
```

**Layout:**
- **Desktop:** 4 cards in a row (25% width each)
- **Tablet:** 2x2 grid
- **Mobile:** Stack (1 column)
- **Background:** White
- **Padding:** 64px top/bottom

**Card Structure:**
- **Icon/Image:** Service-specific image or icon (64x64px)
- **Title:** Service name (H3, Inter semibold, 20px)
- **Description:** 2-3 sentences (from CONTENT_COPY.md)
- **CTA:** "Learn More →" (link to service page)
- **Hover:** Lift effect (translateY(-4px)) + shadow increase

**Services:**
1. **Chimney Caps & Tops** → `/services/chimney-caps.html`
2. **Flashing & Weatherproofing** → `/services/flashing.html`
3. **Roofing & Gutters** → `/services/roofing-gutters.html`
4. **Custom Architectural Metalwork** → `/services/custom-metalwork.html`

---

## Section 5: Featured Projects Gallery

```
┌─────────────────────────────────────────────────────────────┐
│                    FEATURED PROJECTS                        │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Image   │  │  Image   │  │  Image   │  │  Image   │   │
│  │          │  │          │  │          │  │          │   │
│  │ Minnesota│  │   Ohio   │  │N.Carolina│  │  Tulsa   │   │
│  │ Chimney  │  │  French  │  │  Custom  │  │Mid-Cont. │   │
│  │  Shroud  │  │ Country  │  │   Cap    │  │  Tower   │   │
│  │          │  │          │  │          │  │          │   │
│  │ [View]   │  │ [View]   │  │ [View]   │  │ [View]   │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                             │
│                   [View Full Portfolio →]                   │
└─────────────────────────────────────────────────────────────┘
```

**Layout:**
- **Desktop:** 4 cards in a row
- **Tablet:** 2x2 grid
- **Mobile:** 2x2 grid (smaller cards) or stack
- **Background:** Light gray (#F5F5F5)
- **Padding:** 64px top/bottom

**Card Structure:**
- **Image:** 400x300px (4:3 ratio)
- **Overlay:** Dark gradient on hover (shows title + location)
- **Title:** Project name
- **Location:** City, State
- **CTA:** "View Project" (hover state)

**Projects (4 featured from PORTFOLIO_PROJECTS.md):**
1. Minnesota Copper Chimney Shroud
2. Ohio French Country Chimney Caps
3. North Carolina Custom Chimney Cap
4. Mid-Continent Tower, Tulsa (commercial)

**Gallery CTA:** "View Full Portfolio" → `/portfolio.html`

---

## Section 6: Why Choose Water Ways (3 Columns)

```
┌───────────────────────────────────────────────────────────────┐
│               WHY CHOOSE WATER WAYS?                          │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │  Premium     │  │   Custom     │  │   Expert     │       │
│  │  Materials   │  │  Fabrication │  │  Craftsmen   │       │
│  │              │  │              │  │              │       │
│  │ • Copper     │  │ • 100% Custom│  │ • 20+ Years  │       │
│  │ • Rheinzink  │  │ • No Pre-Fab │  │ • Ray &      │       │
│  │ • Premium    │  │ • Design     │  │   Natalie    │       │
│  │   Finishes   │  │   Assist     │  │ • Commercial │       │
│  │              │  │ • Progress   │  │   Experience │       │
│  │              │  │   Photos     │  │              │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
└───────────────────────────────────────────────────────────────┘
```

**Layout:**
- **Desktop:** 3 columns (33% width each)
- **Mobile:** Stack (1 column)
- **Background:** White
- **Padding:** 64px top/bottom

**Column Structure:**
- **Icon:** Material/craftsman icon (optional)
- **Headline:** Benefit (H3, Inter semibold)
- **Bullet Points:** 4-5 specific details
- **From:** CONTENT_COPY.md "Why Choose Water Ways" section

**Three Pillars:**
1. **Premium Materials:** Copper, Rheinzink, quality focus
2. **Custom Fabrication:** 100% custom-built, no pre-fab, design assistance
3. **Expert Craftsmen:** 20+ years experience, commercial projects, apprenticeship

---

## Section 7: Process Overview (4 Steps)

```
┌──────────────────────────────────────────────────────────────┐
│                     OUR PROCESS                              │
│                                                              │
│  ╔═══════╗      ╔═══════╗      ╔═══════╗      ╔═══════╗    │
│  ║   1   ║  →   ║   2   ║  →   ║   3   ║  →   ║   4   ║    │
│  ║Consult║      ║ Design║      ║Fabric-║      ║Install║    │
│  ║       ║      ║       ║      ║ ation ║      ║       ║    │
│  ╚═══════╝      ╚═══════╝      ╚═══════╝      ╚═══════╝    │
│                                                              │
│  Brief description under each step                           │
│                                                              │
│                  [Start Your Project →]                      │
└──────────────────────────────────────────────────────────────┘
```

**Layout:**
- **Desktop:** Horizontal timeline (4 steps with arrows)
- **Mobile:** Vertical timeline (stack)
- **Background:** Light gray (#F5F5F5)
- **Padding:** 64px top/bottom

**Four Steps:**
1. **Consultation:** "Share your project vision, measurements, and timeline"
2. **Design:** "We create custom designs and provide progress photos"
3. **Fabrication:** "Expert craftsmanship using premium materials"
4. **Delivery/Install:** "Careful packaging and shipping or local installation"

**CTA:** "Start Your Project" → `/contact.html`

---

## Section 8: Testimonials (3 Customer Quotes)

```
┌─────────────────────────────────────────────────────────────┐
│              WHAT OUR CUSTOMERS SAY                         │
│                                                             │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────┐ │
│  │ "We are 100%...  │  │ "We are very...  │  │ "We have │ │
│  │                  │  │                  │  │ the best │ │
│  │ — Paul M.        │  │ — Tom Z.         │  │ chimney  │ │
│  │   Minnesota      │  │   Ohio           │  │ cap..."  │ │
│  │ ★★★★★            │  │ ★★★★★            │  │          │ │
│  └──────────────────┘  └──────────────────┘  │ — Sarah  │ │
│                                               │   NC     │ │
│                                               │ ★★★★★    │ │
│                                               └──────────┘ │
└─────────────────────────────────────────────────────────────┘
```

**Layout:**
- **Desktop:** 3 cards in a row
- **Mobile:** Stack or 1 card carousel
- **Background:** White
- **Padding:** 64px top/bottom

**Card Structure:**
- **Quote:** Customer testimonial (2-3 sentences)
- **Attribution:** Name, Location
- **Rating:** 5 stars (visual)
- **Project Type:** Optional subtitle

**Testimonials (from PORTFOLIO_PROJECTS.md):**
1. Paul M., Minnesota - "We are 100% convinced we made the right decision"
2. Tom Z., Ohio - "We are very glad we chose Waterways. They are a fantastic company!"
3. Sarah P., North Carolina - "We have the best-looking chimney cap in town!"

---

## Section 9: Final CTA Section

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│              READY TO START YOUR PROJECT?                   │
│                                                             │
│     Get a free quote from our expert craftsmen today        │
│                                                             │
│              [Get a Free Quote →]                           │
│           or call (479) 957-3794                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Layout:**
- **Full Width:** Edge-to-edge
- **Background:** Copper gradient or dark charcoal
- **Text Color:** White
- **Padding:** 80px top/bottom

**Content:**
- **Headline:** "Ready to Start Your Project?" (H2, white)
- **Subheadline:** "Get a free quote from our expert craftsmen today"
- **Primary CTA:** "Get a Free Quote" button (white with copper text, or gold)
- **Secondary:** "or call (479) 957-3794" (clickable phone)

---

## Section 10: Footer Navigation

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
│ © 2025 Water Ways Sheet Metal | Privacy | Terms        │
└─────────────────────────────────────────────────────────┘
```

**Layout:**
- **Desktop:** 4 columns
- **Tablet:** 2x2 grid
- **Mobile:** Stack (accordions optional)
- **Background:** Dark charcoal (#333)
- **Text Color:** White/light gray
- **Padding:** 48px top/bottom

**Detailed structure:** See SITE_STRUCTURE.md (Footer Navigation section)

---

## Responsive Breakpoints

### Desktop (1024px+)
- Multi-column layouts (4 columns for services, 3 for why choose)
- Hero: Side-by-side text/image
- All sections at full width up to 1280px max

### Tablet (640px - 1023px)
- 2-column layouts (services, projects)
- Hero: May remain side-by-side or stack
- Footer: 2x2 grid

### Mobile (< 640px)
- Single column stack
- Hero: Text above, image below
- Cards: Full width, stacked
- Touch-friendly buttons (44px minimum)

---

## Performance Optimization

### Above-the-Fold Priority
**Critical Resources (load first):**
- Header navigation
- Hero section (text + image)
- CSS (inline critical CSS)

**Defer:**
- Below-fold images (lazy load)
- Testimonials (lazy load)
- Footer content

### Image Optimization
- **Hero image:** WebP format, <200KB, 720x540px
- **Service cards:** Icons or small images, <50KB each
- **Project gallery:** Lazy load, WebP, 400x300px thumbnails
- **Total page weight target:** <2MB

---

## Accessibility Considerations

### Keyboard Navigation
- All interactive elements tab-accessible
- Skip nav link to main content
- Focus states visible (copper outline)

### Screen Readers
- Semantic HTML (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`)
- Alt text for all images
- ARIA labels for icon-only buttons
- Heading hierarchy (H1 → H2 → H3)

### Color Contrast
- All text meets WCAG AA standards
- CTA buttons have 4.5:1+ contrast
- Focus indicators have 3:1+ contrast

---

## Content Sources (CONTENT_COPY.md)

All copy for this wireframe exists in CONTENT_COPY.md:

- **Hero:** Homepage Hero section
- **About Preview:** Homepage About Preview section
- **Services:** Homepage Services Overview (4 cards)
- **Featured Projects:** PORTFOLIO_PROJECTS.md (4 projects)
- **Why Choose:** Homepage Why Choose Water Ways section
- **Process:** Homepage Our Process section
- **Testimonials:** EXTRACTED_SITE_CONTENT.md (3 testimonials)
- **Final CTA:** Homepage Final CTA section

**Total Homepage Word Count:** ~1,200-1,500 words (readable, not overwhelming)

---

## DESIGN-003 Deliverables ✅

- ✅ **Homepage Structure Defined**
  - 10 sections from header to footer
  - Content hierarchy established
  - Section order optimized for conversion

- ✅ **Layout Patterns Documented**
  - Desktop, tablet, mobile breakpoints
  - Grid systems (4-column, 3-column, 2-column, 1-column)
  - Responsive stacking order

- ✅ **Content Mapping Complete**
  - All content sourced from CONTENT_COPY.md
  - Images sourced from downloads (18 images available)
  - CTAs strategically placed (5 conversion points)

- ✅ **Visual Hierarchy Established**
  - H1 → H2 → H3 progression
  - Emphasis on hero, services, portfolio, testimonials
  - Clear conversion path (multiple CTAs)

---

## Next Steps (DEV-001)

With wireframe complete, HTML development can proceed:

1. Create semantic HTML structure for homepage
2. Implement responsive grid layouts
3. Add images from `images/` folders
4. Insert copy from CONTENT_COPY.md
5. Build navigation from SITE_STRUCTURE.md
6. Apply styles from DESIGN_SYSTEM.md

**Homepage is ready for HTML/CSS implementation.**

---

**Status:** DESIGN-003 Complete ✅
**Created:** 2025-10-28
**Version:** 1.0
**Pattern:** Pattern-CONTEXT-002
**Sections:** 10 (Header → Footer)
**Conversion Points:** 5 CTAs strategically placed
