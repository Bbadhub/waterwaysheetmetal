# Water Ways Sheet Metal - Page Building Skill
**Version:** 1.0
**Created:** 2025-10-29
**Purpose:** Consistent, quality page construction following established patterns

---

## Overview

This skill documents the proven patterns for building Water Ways Sheet Metal website pages. Use this to ensure all pages maintain quality, consistency, and proper structure.

---

## CSS Structure (CRITICAL)

### Only 3 CSS Files Exist:
```html
<link rel="stylesheet" href="../css/variables.css">
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/conversion-enhancements.css">
```

**NEVER reference:** reset.css, typography.css, layout.css, components.css (these don't exist)

### Correct Path Adjustments:
- **Root pages** (index.html, about.html, etc.): `href="css/style.css"`
- **Service pages** (services/*.html): `href="../css/style.css"`
- **Subpages** (services/chimney-caps/*.html): `href="../../css/style.css"`

---

## HTML Structure Template

### Standard Page Template:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="[SEO description 150-160 chars]">
  <meta name="keywords" content="[relevant keywords]">

  <meta property="og:title" content="[Page Title]">
  <meta property="og:description" content="[Social description]">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://waterwayssheetmetal.com/[page-path]">

  <title>[Page Title] | Water Ways Sheet Metal</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="[ADJUST PATH]/css/variables.css">
  <link rel="stylesheet" href="[ADJUST PATH]/css/style.css">
  <link rel="stylesheet" href="[ADJUST PATH]/css/conversion-enhancements.css">

  <link rel="icon" type="image/png" href="[ADJUST PATH]/images/logo/favicon.png">
</head>
<body>
  <a href="#main-content" class="skip-nav">Skip to main content</a>

  [HEADER - Copy from existing page, adjust paths]

  <main id="main-content">
    [PAGE CONTENT]
  </main>

  [FOOTER - Copy from existing page, adjust paths]

  <script src="[ADJUST PATH]/js/script.js"></script>
</body>
</html>
```

---

## Hero Section Pattern

### Split Layout Hero (55/45 split):
```html
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <!-- Hero Content (55%) -->
      <div class="hero-content">
        <div class="hero-eyebrow">[Category/Specialty]</div>
        <h1 class="hero-title">[Emotional Problem-Focused Headline]</h1>
        <p class="hero-subtitle">[2-3 sentences explaining the problem and solution]</p>

        <div class="hero-value-props">
          <div class="value-prop">
            <svg class="value-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span>[Benefit statement]</span>
          </div>
          <!-- 2-3 more value props -->
        </div>

        <div class="hero-cta">
          <a href="[ADJUST PATH]/contact.html#quote-form" class="btn btn-primary btn-lg">Request a Quote</a>
          <a href="tel:+14799573794" class="btn btn-secondary btn-lg">Call (479) 957-3794</a>
        </div>
      </div>

      <!-- Hero Image (45%) -->
      <div class="hero-image">
        <picture>
          <source srcset="[ADJUST PATH]/images-optimized/[category]/hero/[image].webp" type="image/webp">
          <source srcset="[ADJUST PATH]/images-optimized/[category]/hero/[image].jpg" type="image/jpeg">
          <img src="[ADJUST PATH]/images-optimized/[category]/hero/[image].jpg" alt="[Descriptive alt text]" loading="eager" width="1920" height="1440">
        </picture>
        <div class="hero-image-badge">
          <span class="badge-text">[Badge Text]</span>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Content Section Patterns

### Service Cards Grid (2-column):
```html
<section class="section-padding [bg-light]">
  <div class="container">
    <h2 class="section-title [centered]">[Section Title]</h2>
    <p class="section-intro [centered]">[1-2 sentence introduction]</p>

    <div class="services-grid">
      <article class="service-card">
        <div class="service-image">
          <picture>
            <source srcset="[ADJUST PATH]/images-optimized/[category]/hero/[image].webp" type="image/webp">
            <source srcset="[ADJUST PATH]/images-optimized/[category]/hero/[image].jpg" type="image/jpeg">
            <img src="[ADJUST PATH]/images-optimized/[category]/hero/[image].jpg" alt="[Alt text]" loading="lazy" width="1920" height="1440">
          </picture>
        </div>
        <div class="service-content">
          <h3 class="service-title">[Card Title]</h3>
          <p>[Content paragraph]</p>
        </div>
      </article>

      <!-- More cards -->
    </div>
  </div>
</section>
```

### Problem → Solution Pattern:
```html
<section class="section-padding">
  <div class="container">
    <div class="problem-solution">
      <div class="problem-box">
        <h3 class="problem-title">The Problem</h3>
        <p>[Describe customer pain point emotionally]</p>
      </div>

      <div class="solution-box">
        <h3 class="solution-title">Our Solution</h3>
        <p>[Explain how Water Ways solves this]</p>
      </div>
    </div>
  </div>
</section>
```

---

## Image Usage Rules

### Image Size Guidelines:
- **Hero images:** Use `hero/` directory (1920x1440) - for split hero sections
- **Content cards:** Use `hero/` directory for better quality on service cards
- **Thumbnails:** Use `featured/` directory (1200x800) only if many small images needed
- **Always use WebP + JPEG fallback** with `<picture>` elements

### Picture Element Pattern:
```html
<picture>
  <source srcset="[path]/[image].webp" type="image/webp">
  <source srcset="[path]/[image].jpg" type="image/jpeg">
  <img src="[path]/[image].jpg" alt="[Descriptive alt text]" loading="lazy" width="1920" height="1440">
</picture>
```

### Image Directory Structure:
```
images-optimized/
├── chimney-caps/
│   ├── hero/         (1920x1440 - USE FOR HEROES & CARDS)
│   ├── featured/     (1200x800 - rarely needed)
│   └── thumbnail/    (600x400 - gallery only)
├── flashing/
├── roofing/
├── architectural/
├── interior/
├── homepage-showcase/
└── branding/
```

---

## Navigation Structure

### Header Navigation (copy and adjust paths):
```html
<header class="header">
  <div class="container header-container">
    <a href="[ADJUST PATH]/index.html" class="logo">
      <img src="[ADJUST PATH]/images/logo/Waterways-Logo-Header-Transparent.png" alt="Water Ways Sheet Metal Logo" width="200" height="60">
    </a>

    <nav class="nav-primary" aria-label="Primary navigation">
      <ul class="nav-menu">
        <li><a href="[ADJUST PATH]/index.html" class="nav-link">Home</a></li>
        <li class="nav-dropdown">
          <button class="nav-link dropdown-toggle" aria-expanded="false" aria-haspopup="true">
            Services <span class="dropdown-icon">▼</span>
          </button>
          <ul class="dropdown-menu">
            <li><a href="[ADJUST PATH]/services/chimney-caps.html">Chimney Caps & Tops</a></li>
            <li><a href="[ADJUST PATH]/services/flashing.html">Flashing & Weatherproofing</a></li>
            <li><a href="[ADJUST PATH]/services/roofing-gutters.html">Roofing & Gutters</a></li>
            <li><a href="[ADJUST PATH]/services/custom-metalwork.html">Custom Architectural Metalwork</a></li>
          </ul>
        </li>
        <li><a href="[ADJUST PATH]/portfolio.html" class="nav-link">Portfolio</a></li>
        <li><a href="[ADJUST PATH]/about.html" class="nav-link">About</a></li>
        <li><a href="[ADJUST PATH]/faq.html" class="nav-link">FAQ</a></li>
        <li><a href="[ADJUST PATH]/contact.html" class="nav-link">Contact</a></li>
      </ul>
      <a href="[ADJUST PATH]/contact.html#quote-form" class="btn btn-primary">Get a Quote →</a>
    </nav>

    <!-- Mobile hamburger menu -->
  </div>
</header>
```

---

## Content Writing Guidelines

### Headlines:
- **Focus on SOLUTIONS to customer problems**, not product features
- Use positive, benefit-driven language
- Lead with how we solve their problem
- Examples:
  - ✅ "Protect Your Home from Water Damage with Custom Copper Solutions"
  - ✅ "End Chimney Leaks Permanently with Precision-Crafted Caps"
  - ❌ "We Make Chimney Caps"
  - ❌ "Your Chimney Has Problems"

### Body Copy - SOLUTION-BASED APPROACH:
- **Start with the solution benefit** (what customer gets)
- Briefly acknowledge the problem (1 sentence max)
- **Focus 80% on the solution** and how it works
- Explain specific benefits with concrete outcomes
- Use positive, confident language
- End sections with clear, action-oriented CTAs

### Solution-Based Copy Structure:
```
1. SOLUTION BENEFIT (headline)
2. Brief problem context (1 sentence if needed)
3. HOW WE SOLVE IT (detailed explanation)
4. SPECIFIC BENEFITS (what customer experiences)
5. PROOF/VALIDATION (why this solution works)
6. CLEAR CTA (how to get this solution)
```

### Examples of Solution-Based Copy:

**❌ Problem-Focused (avoid):**
"Is your chimney leaking? Water damage can cost thousands in repairs. Cheap caps fail within years."

**✅ Solution-Focused (use this):**
"Our custom copper chimney caps provide lifetime protection with precision engineering. Each cap is crafted to your exact specifications, ensuring perfect fit and weather-tight seal. Premium 16oz copper develops a protective patina that actually strengthens over time—meaning your investment protects your home for generations."

### CTA Strategy - SOLUTION-ORIENTED:
- Primary CTA: **"Get Your Custom Solution"** or **"Protect Your Home Today"**
- Secondary CTA: **"Speak with a Craftsman: (479) 957-3794"**
- Make CTAs about **getting the solution**, not just requesting quotes
- Use action verbs: Protect, Secure, Eliminate, Ensure, Guarantee
- Examples:
  - ✅ "Protect Your Investment with Custom Copper"
  - ✅ "Eliminate Water Damage—Request Your Solution"
  - ✅ "Secure Lifetime Protection Today"
  - ❌ "Get a Quote"
  - ❌ "Contact Us"

### CTA Placement:
- Hero section: Focus on main benefit
- Mid-page CTAs: Context-specific to section topic
- Section endings: Reinforce solution benefit
- Final CTA: Strong, confident, benefit-driven
- Use throughout page—every major section should have path to conversion

---

## Quality Checklist

### Before Completing Page:
- [ ] All CSS paths correct (variables.css, style.css, conversion-enhancements.css)
- [ ] All navigation links have correct relative paths
- [ ] All images use hero/ directory for best quality
- [ ] All images have WebP + JPEG fallback
- [ ] All images have descriptive alt text
- [ ] Hero section uses split layout (55/45)
- [ ] Value props use checkmark SVG icons
- [ ] Multiple CTAs throughout page
- [ ] Section backgrounds alternate (white → bg-light → white)
- [ ] Mobile menu paths adjusted
- [ ] Footer paths adjusted
- [ ] Meta descriptions are 150-160 characters
- [ ] Page title follows pattern: "[Page Name] | Water Ways Sheet Metal"

---

## Common Mistakes to Avoid

### ❌ NEVER Do:
1. Reference non-existent CSS files (reset.css, typography.css, etc.)
2. Use `featured/` images when `hero/` available (hero = better quality)
3. Forget to adjust navigation paths for subdirectories
4. Use generic headlines ("Our Services", "About Us")
5. Skip WebP fallbacks
6. Use images without alt text
7. Forget loading="eager" on hero images
8. Mix up relative path depths (../ vs ../../)

### ✅ ALWAYS Do:
1. Verify image exists before referencing
2. Use hero/ images for service cards and heroes
3. Adjust ALL paths when changing directory depth
4. Use emotional, problem-focused copy
5. Include CTAs in every major section
6. Test all navigation links
7. Use descriptive alt text for images
8. Follow existing page patterns exactly

---

## Examples of Correct Implementation

### Example 1: Service Page Structure
See `services/chimney-caps.html` for reference:
- Hero with split layout
- Problem/solution pattern
- Service cards with hero images
- Portfolio showcase
- Multiple CTAs throughout
- Testimonials section
- Final CTA section

### Example 2: Portfolio Page Structure
See `portfolio.html` for reference:
- Hero introduction
- Card-based project grid
- Each project clickable
- Images using hero/ directory
- Clean, organized layout

---

## Building New Pages - Step by Step

### Step 1: Copy Template
1. Copy from existing page (same directory level if possible)
2. Adjust meta tags and title
3. Update page-specific content

### Step 2: Fix All Paths
1. Count directory depth (root=0, services/=1, services/subpage/=2)
2. Adjust CSS paths (0=css/, 1=../css/, 2=../../css/)
3. Adjust navigation links throughout
4. Adjust image paths
5. Adjust footer links

### Step 3: Add Content
1. Write hero section (problem-focused headline)
2. Add 2-4 content sections with service cards
3. Include problem/solution section if applicable
4. Add portfolio examples if relevant
5. Add testimonial section
6. End with strong CTA section

### Step 4: Add Images
1. Check which images exist in images-optimized/
2. Use hero/ directory for all service cards and heroes
3. Verify image filenames match exactly
4. Add WebP + JPEG sources
5. Write descriptive alt text

### Step 5: Quality Check
1. Run through checklist above
2. Test in browser
3. Check all links work
4. Verify images load
5. Test mobile menu

---

## Portfolio Project Page Pattern

For individual portfolio projects (like "Ohio Home", "Minnesota Project"):

```html
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-content">
        <div class="hero-eyebrow">Portfolio Project</div>
        <h1 class="hero-title">[Project Name]</h1>
        <p class="hero-subtitle">[Project description, location, unique aspects]</p>

        <div class="project-details">
          <div class="detail-item">
            <strong>Location:</strong> [City, State]
          </div>
          <div class="detail-item">
            <strong>Project Type:</strong> [Type]
          </div>
          <div class="detail-item">
            <strong>Materials:</strong> [Materials used]
          </div>
        </div>
      </div>

      <div class="hero-image">
        <picture>
          [Main project image]
        </picture>
      </div>
    </div>
  </div>
</section>

<section class="section-padding">
  <div class="container">
    <h2 class="section-title">Project Gallery</h2>
    <div class="projects-grid">
      [Multiple project images in grid]
    </div>
  </div>
</section>

[Customer testimonial if available]

[CTA section]
```

---

## Quick Reference: Path Adjustments

| Page Location | CSS Path | Image Path | Nav Link (to root) |
|--------------|----------|------------|-------------------|
| Root (index.html) | `css/` | `images-optimized/` | `index.html` |
| services/*.html | `../css/` | `../images-optimized/` | `../index.html` |
| services/subpage/*.html | `../../css/` | `../../images-optimized/` | `../../index.html` |

---

## Skill Usage

When building a new page:
1. Identify page type (service, portfolio project, subpage)
2. Choose appropriate template section
3. Follow step-by-step process
4. Run quality checklist
5. Verify all paths are correct for directory depth
6. Test in browser

**Remember:** Quality over speed. Better to build correctly once than fix mistakes later.
