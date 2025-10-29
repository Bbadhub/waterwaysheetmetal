# Water Ways Sheet Metal - CSS Pattern Guide
**Created:** 2025-10-28
**Pattern:** Pattern-CONTEXT-002
**Purpose:** Ensure all service pages use correct CSS classes and structure

---

## CSS Files (3 Required for Service Pages)
```html
<link rel="stylesheet" href="../css/variables.css">
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/conversion-enhancements.css">
```

**Note:** Some working pages (like roofing-gutters.html, flashing.html) only use 2:
```html
<link rel="stylesheet" href="../css/variables.css">
<link rel="stylesheet" href="../css/style.css">
```

For conversion-focused service pages (chimney-caps.html), include all 3.

**Fonts:**
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

---

## Page Structure Pattern

### 1. Hero Section
```html
<section class="page-hero">
  <div class="container">
    <h1 class="page-title">Problem-Focused Headline</h1>
    <p class="page-subtitle">Solution-focused subtitle with benefits</p>
  </div>
</section>
```

### 2. Standard Section
```html
<section class="section-padding">
  <div class="container-narrow">
    <h2 class="section-title">Section Headline</h2>
    <p class="lead">Lead paragraph with larger text</p>
    <!-- Content -->
  </div>
</section>
```

### 3. Light Background Section
```html
<section class="section-padding bg-light">
  <div class="container">
    <h2 class="section-title centered">Centered Headline</h2>
    <p class="section-intro centered">Centered intro text</p>
    <!-- Content -->
  </div>
</section>
```

### 4. Dark Background Section (for CTAs)
```html
<section class="section-padding bg-dark">
  <div class="container">
    <h2 class="section-title centered">Final CTA Headline</h2>
    <p class="section-intro centered">CTA description</p>
    <!-- CTA buttons -->
  </div>
</section>
```

---

## Layout Containers

### Container Types
- `.container` - Max-width: 1280px (default for most content)
- `.container-narrow` - Max-width: 800px (for text-heavy sections)

### Grid Classes
- `.benefits-grid` - 2-4 column grid for benefit cards
- `.materials-grid` - Grid for material/product cards
- `.styles-grid` - Grid for style options
- `.services-grid` - Grid for service cards
- `.projects-grid` - Grid for portfolio/project items
- `.testimonials-grid` - Grid for testimonial cards
- `.process-grid` - Grid for process steps

---

## Component Classes

### Cards
```html
<div class="benefit-item">
  <h3>Benefit Title</h3>
  <p>Benefit description</p>
</div>

<article class="material-card">
  <h3 class="material-title">Title</h3>
  <p>Content</p>
</article>

<article class="service-card">
  <!-- Service content -->
</article>

<article class="project-card">
  <!-- Project content -->
</article>

<blockquote class="testimonial-card">
  <!-- Testimonial content -->
</blockquote>
```

### Text Utilities
- `.lead` - Larger intro paragraph
- `.centered` - Center-align text
- `.section-title` - Section heading style
- `.section-intro` - Section intro paragraph

### Background Utilities
- `.bg-light` - Light gray background
- `.bg-dark` - Dark background with white text
- `.section-padding` - Consistent top/bottom padding

---

## Button Classes
```html
<a href="#" class="btn btn-primary">Primary CTA</a>
<a href="#" class="btn btn-secondary">Secondary CTA</a>
<a href="#" class="btn btn-tertiary">Tertiary/Link</a>
```

---

## Common Mistakes to AVOID

❌ **DON'T USE:**
- `.hero` (use `.page-hero`)
- `.section` (use `.section-padding`)
- `.two-column-grid` (not in CSS)
- `.service-cta-group` (not in CSS)
- Full-width hero images (use constrained layouts)
- Made-up class names not in style.css

✅ **DO USE:**
- Existing CSS classes from style.css
- `.container` or `.container-narrow` for all content
- `.section-padding` for vertical spacing
- Grid classes that exist: `.benefits-grid`, `.services-grid`, etc.
- Images within proper containers (not full-screen)

---

## Header/Footer Structure

### Header (use exactly as shown)
```html
<header class="header">
  <div class="container header-container">
    <!-- Logo, nav, mobile menu -->
  </div>
</header>
```

### Footer (use exactly as shown)
```html
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <!-- 4 footer columns -->
    </div>
    <div class="footer-bottom">
      <!-- Copyright -->
    </div>
  </div>
</footer>
```

### Script
```html
<script src="../js/script.js"></script>
```
(NOT `main.js`)

---

## Image Best Practices

### Use `<picture>` for optimized images
```html
<picture>
  <source srcset="../images-optimized/folder/size/image.webp" type="image/webp">
  <source srcset="../images-optimized/folder/size/image.jpg" type="image/jpeg">
  <img src="../images-optimized/folder/size/image.jpg"
       alt="Descriptive alt text"
       loading="lazy"
       width="1200"
       height="900">
</picture>
```

### Image Sizes
- **Hero:** 1920px (hero folder)
- **Featured:** 1200px (featured folder)
- **Thumbnail:** 600px (thumbnail folder)

### Lazy Loading
- Hero images: `loading="eager"`
- All other images: `loading="lazy"`

---

## Conversion Elements (from conversion-enhancements.css)

### Phone in Header
```html
<a href="tel:+14799573794" class="nav-phone">📞 (479) 957-3794</a>
```

### Problem Callout
```html
<div class="service-problem">⚠️ Problem statement</div>
```

### Solution Highlight
```html
<div class="service-solution">
  <strong>Our Solution:</strong> Solution description
</div>
```

### Testimonial with Rating
```html
<blockquote class="testimonial-card">
  <div class="testimonial-rating">⭐⭐⭐⭐⭐</div>
  <p class="testimonial-quote">Quote text</p>
  <footer class="testimonial-author">
    <strong>Name</strong>
    <span class="testimonial-location">Location</span>
    <span class="testimonial-result">✓ Result achieved</span>
  </footer>
</blockquote>
```

---

## Content Strategy (ACT 1-4)

### ACT 1: The Problem (page-hero + first section)
- Problem-focused headline
- Pain points and costs
- Emotional appeal

### ACT 2: The Solution (bg-light section)
- Custom copper/material benefits
- What makes it different
- Lifetime value proposition

### ACT 3: The Proof (multiple sections)
- Testimonials with results
- Photo galleries
- Case studies
- Benefits grid

### ACT 4: The Invitation (bg-dark final CTA)
- Clear call to action
- Guarantee badges
- Urgency elements
- Trust signals

---

## Checklist for New Service Pages

- [ ] CSS files: variables.css, style.css, conversion-enhancements.css
- [ ] Fonts: Playfair Display + Inter
- [ ] Header structure matches homepage exactly
- [ ] `.page-hero` for hero section
- [ ] `.section-padding` for all sections
- [ ] `.container` or `.container-narrow` for all content
- [ ] Use existing grid classes (benefits-grid, services-grid, etc.)
- [ ] Images in `<picture>` elements with WebP + JPEG
- [ ] Images properly sized (not full-screen)
- [ ] Footer structure matches homepage exactly
- [ ] Script tag: `script.js` (not main.js)
- [ ] 8-10 CTAs at strategic decision points
- [ ] ACT 1-4 story structure
- [ ] Problem-focused copy (not feature-focused)

---

**Last Updated:** 2025-10-28
**Status:** Active pattern guide for all service page development
