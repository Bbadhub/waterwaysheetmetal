# Site Template & Replication Guide

**How to Duplicate This Website Structure for New Projects**

*Created: January 2025*

---

## Overview

This document explains how to replicate the Back40 RV Park website structure for other small business websites. The site was built with modern SEO/AEO best practices, performance optimization, and AI-search readiness.

---

## Site Architecture Philosophy

### Core Principles

1. **Performance First** - Static HTML/CSS/JS (no frameworks = fast loading)
2. **SEO/AEO Optimized** - Structured data, semantic HTML, AI-readable content
3. **Mobile-First** - Responsive design, works on all devices
4. **Accessibility** - ARIA labels, semantic markup, keyboard navigation
5. **Content-Driven** - Clear hierarchy, storytelling, conversion-focused
6. **AI-Ready** - llms.txt file for AI assistant accuracy
7. **Simple Maintenance** - No CMS, no database, easy updates via Git

### Tech Stack

```
- HTML5 (semantic markup)
- CSS3 (custom properties, flexbox, grid)
- Vanilla JavaScript (no jQuery, no frameworks)
- Git for version control
- Netlify for hosting (free tier)
- Schema.org markup for rich results
- Open Graph for social sharing
```

---

## File Structure Template

```
project-root/
│
├── index.html                 # Homepage
├── services.html             # Main service page (adapt to business)
├── about.html                # About page/story
├── contact.html              # Contact form + map
├── faq.html                  # FAQ with Schema markup
├── testimonials.html         # Customer reviews
├── gallery.html              # Photo gallery
│
├── css/
│   └── style.css             # Single stylesheet (organized by sections)
│
├── js/
│   ├── main.js               # Core functionality (nav, forms, etc.)
│   └── [feature].js          # Feature-specific JS (social, calculator, etc.)
│
├── images/
│   ├── hero/                 # Hero images (optimized, <200KB)
│   ├── content/              # Content images
│   └── icons/                # Icons, logos
│
├── admin/                    # Optional admin dashboard
│   ├── login.html
│   └── dashboard.html
│
├── llms.txt                  # AI assistant optimization file
├── robots.txt                # Search engine directives
├── sitemap.xml               # Auto-generated or manual sitemap
├── .gitignore                # Git exclusions
└── README.md                 # Project documentation
```

---

## Page Structure Template

### Standard HTML Page Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="[150-160 char description with keywords]">
    <title>[Page Title] | [Business Name]</title>
    <link rel="canonical" href="https://yourdomain.com/page.html">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://yourdomain.com/page.html">
    <meta property="og:title" content="[Page Title] | [Business Name]">
    <meta property="og:description" content="[Description for social sharing]">
    <meta property="og:image" content="https://yourdomain.com/images/social-share.jpg">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="https://yourdomain.com/page.html">
    <meta name="twitter:title" content="[Page Title]">
    <meta name="twitter:description" content="[Description]">
    <meta name="twitter:image" content="https://yourdomain.com/images/social-share.jpg">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=[YourFonts]&display=swap" rel="stylesheet">

    <!-- Font Awesome or Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Stylesheet -->
    <link rel="stylesheet" href="css/style.css">

    <!-- Schema Markup (see schema section below) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "[BusinessType]",
      "name": "[Business Name]",
      ...
    }
    </script>
</head>
<body>
    <!-- Header with navigation -->
    <header class="header" id="header">
        <!-- Navigation structure -->
    </header>

    <!-- Main content sections -->
    <main>
        <!-- Page-specific content -->
    </main>

    <!-- Footer -->
    <footer class="footer">
        <!-- Footer content -->
    </footer>

    <!-- Scripts -->
    <script src="js/main.js"></script>
</body>
</html>
```

---

## Key Components Breakdown

### 1. Navigation Header

**Features:**
- Sticky header (stays visible on scroll)
- Mobile hamburger menu
- CTA button (Call to action)
- Phone number (clickable tel: link)
- Active page indicator

**Code pattern:**
```html
<header class="header" id="header">
    <div class="container">
        <div class="header-content">
            <div class="logo">
                <a href="index.html">[Business Name]</a>
            </div>
            <nav class="nav" id="nav">
                <button class="nav-close" id="nav-close">
                    <i class="fas fa-times"></i>
                </button>
                <ul class="nav-list">
                    <li><a href="index.html" class="nav-link">Home</a></li>
                    <li><a href="services.html" class="nav-link">Services</a></li>
                    <li><a href="about.html" class="nav-link">About</a></li>
                    <li><a href="contact.html" class="nav-link">Contact</a></li>
                </ul>
            </nav>
            <div class="header-actions">
                <a href="tel:[phone]" class="phone-btn">
                    <i class="fas fa-phone"></i>
                    <span>[Phone Number]</span>
                </a>
                <a href="contact.html#book" class="cta-btn">Book Now</a>
                <button class="nav-toggle" id="nav-toggle">
                    <i class="fas fa-bars"></i>
                </button>
            </div>
        </div>
    </div>
</header>
```

### 2. Hero Section

**Features:**
- Full-width background image
- Overlay for text readability
- Clear headline + subheadline
- Primary and secondary CTAs
- Quick stats/features

**Code pattern:**
```html
<section class="hero" id="home">
    <div class="hero-overlay"></div>
    <img src="images/hero-bg.jpg" alt="[Descriptive alt text]" class="hero-bg" loading="eager">
    <div class="container">
        <div class="hero-content">
            <h1 class="hero-title">[Compelling Headline]</h1>
            <p class="hero-subtitle">[Supporting description]</p>
            <div class="hero-buttons">
                <a href="contact.html" class="btn btn-primary">[Primary CTA]</a>
                <a href="services.html" class="btn btn-secondary">[Secondary CTA]</a>
            </div>
            <div class="hero-quick-info">
                <div class="quick-info-item">
                    <i class="fas fa-[icon]"></i>
                    <span><strong>[Value]</strong> [Label]</span>
                </div>
                <!-- Repeat for 3-4 key features -->
            </div>
        </div>
    </div>
</section>
```

### 3. Content Split Sections (Text + Image)

**Features:**
- Alternating layout (image left, then right, then left...)
- Responsive (stacks on mobile)
- Icon lists for features
- Image captions

**Code pattern:**
```html
<section class="section">
    <div class="container">
        <div class="content-split">
            <div class="content-text">
                <h2>[Section Headline]</h2>
                <p class="lead">[Opening paragraph]</p>
                <h3>[Subheading]</h3>
                <p>[Supporting paragraph]</p>
                <ul class="icon-list">
                    <li><i class="fas fa-check-circle"></i> [Feature 1]</li>
                    <li><i class="fas fa-check-circle"></i> [Feature 2]</li>
                    <li><i class="fas fa-check-circle"></i> [Feature 3]</li>
                </ul>
                <a href="[link]" class="btn btn-secondary">[CTA]</a>
            </div>
            <div class="content-image">
                <img src="images/[image].jpg" alt="[Descriptive alt]" loading="lazy">
                <div class="image-caption">[Caption]</div>
            </div>
        </div>
    </div>
</section>

<!-- Next section with reverse class for alternating layout -->
<section class="section-light">
    <div class="container">
        <div class="content-split reverse">
            <!-- Same structure, image will be on right -->
        </div>
    </div>
</section>
```

### 4. Pricing Section

**Features:**
- Card-based layout
- Highlighted "popular" option
- Feature lists with checkmarks
- Interactive calculator (optional)

**Code pattern:**
```html
<section class="pricing">
    <div class="container">
        <div class="section-header center">
            <h2>[Pricing Headline]</h2>
            <p>[Subheadline]</p>
        </div>
        <div class="pricing-cards">
            <div class="pricing-card">
                <div class="pricing-header">
                    <h3>[Package Name]</h3>
                    <div class="price">
                        <span class="currency">$</span>
                        <span class="amount">[Amount]</span>
                        <span class="period">/[period]</span>
                    </div>
                </div>
                <ul class="pricing-features">
                    <li><i class="fas fa-check"></i> [Feature 1]</li>
                    <li><i class="fas fa-check"></i> [Feature 2]</li>
                </ul>
                <a href="contact.html" class="btn btn-outline">[CTA]</a>
            </div>

            <div class="pricing-card featured">
                <div class="popular-badge">Most Popular</div>
                <!-- Same structure as above -->
            </div>
        </div>
    </div>
</section>
```

### 5. FAQ Section (with Schema)

**Features:**
- Accordion-style expandable questions
- Schema.org FAQPage markup for rich results
- Categories (optional)
- Search functionality (optional)

**Code pattern (HTML):**
```html
<section class="faq-section">
    <div class="container">
        <div class="section-header center">
            <h1>Frequently Asked Questions</h1>
            <p>[Description]</p>
        </div>
        <div class="faq-container">
            <div class="faq-item">
                <button class="faq-question" aria-expanded="false">
                    <span>[Question?]</span>
                    <i class="fas fa-chevron-down"></i>
                </button>
                <div class="faq-answer">
                    <p>[Answer paragraph 1]</p>
                    <p>[Answer paragraph 2]</p>
                </div>
            </div>
            <!-- Repeat for each FAQ -->
        </div>
    </div>
</section>

<!-- Schema markup in <head> -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question text]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer text]"
      }
    }
    // Repeat for each FAQ
  ]
}
</script>
```

### 6. Contact Form

**Features:**
- Name, email, phone, message fields
- Mobile detection (opens SMS on mobile)
- Validation
- Success/error messages
- Map integration (Google Maps iframe)

**Code pattern:**
```html
<section class="contact-section" id="book">
    <div class="container">
        <div class="contact-grid">
            <div class="contact-info">
                <h2>Get In Touch</h2>
                <div class="contact-methods">
                    <div class="contact-method">
                        <i class="fas fa-phone"></i>
                        <div>
                            <h3>Phone</h3>
                            <a href="tel:[phone]">[Phone Number]</a>
                        </div>
                    </div>
                    <div class="contact-method">
                        <i class="fas fa-envelope"></i>
                        <div>
                            <h3>Email</h3>
                            <a href="mailto:[email]">[Email]</a>
                        </div>
                    </div>
                    <div class="contact-method">
                        <i class="fas fa-map-marker-alt"></i>
                        <div>
                            <h3>Location</h3>
                            <p>[Address]</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="contact-form-container">
                <form class="contact-form" id="contactForm">
                    <div class="form-group">
                        <label for="name">Name *</label>
                        <input type="text" id="name" name="name" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email *</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="phone">Phone</label>
                        <input type="tel" id="phone" name="phone">
                    </div>
                    <div class="form-group">
                        <label for="message">Message *</label>
                        <textarea id="message" name="message" rows="5" required></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Send Message</button>
                </form>
            </div>
        </div>
    </div>
</section>
```

### 7. Footer

**Features:**
- Multiple columns (about, links, contact, hours)
- Social media links
- Copyright
- Admin login link
- Back to top button

**Code pattern:**
```html
<footer class="footer">
    <div class="container">
        <div class="footer-content">
            <div class="footer-column">
                <h3>[Business Name]</h3>
                <p>[Tagline or description]</p>
                <div class="footer-contact">
                    <p><i class="fas fa-phone"></i> <a href="tel:[phone]">[Phone]</a></p>
                    <p><i class="fas fa-map-marker-alt"></i> [Address]</p>
                </div>
            </div>
            <div class="footer-column">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="services.html">Services</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h4>Information</h4>
                <ul>
                    <li><a href="faq.html">FAQ</a></li>
                    <li><a href="testimonials.html">Testimonials</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h4>Hours</h4>
                <p>[Business hours]</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2025 [Business Name]. All rights reserved.</p>
        </div>
    </div>
</footer>

<button class="back-to-top" id="backToTop" aria-label="Back to top">
    <i class="fas fa-chevron-up"></i>
</button>
```

---

## CSS Architecture

### Organization Structure

```css
/* =========================
   CSS Variables (Custom Properties)
   ========================= */
:root {
    /* Colors */
    --primary-color: #[hex];
    --secondary-color: #[hex];
    --accent-color: #[hex];
    --text-dark: #333;
    --text-light: #666;
    --bg-light: #f9f9f9;
    --white: #fff;

    /* Typography */
    --font-primary: 'Font Name', sans-serif;
    --font-secondary: 'Font Name', serif;

    /* Spacing */
    --spacing-xs: 0.5rem;
    --spacing-sm: 1rem;
    --spacing-md: 2rem;
    --spacing-lg: 4rem;
    --spacing-xl: 6rem;

    /* Breakpoints (used in media queries) */
    --mobile: 480px;
    --tablet: 768px;
    --desktop: 1024px;
    --wide: 1200px;
}

/* =========================
   Base Styles
   ========================= */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
    font-size: 16px;
}

body {
    font-family: var(--font-primary);
    color: var(--text-dark);
    line-height: 1.6;
}

/* =========================
   Typography
   ========================= */
h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-secondary);
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 1rem;
}

/* =========================
   Layout Utilities
   ========================= */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.section {
    padding: var(--spacing-xl) 0;
}

.section-light {
    background: var(--bg-light);
    padding: var(--spacing-xl) 0;
}

/* =========================
   Components (Header, Hero, Cards, etc.)
   ========================= */
/* Organize by component */

/* =========================
   Responsive Design
   ========================= */
@media (max-width: 768px) {
    /* Mobile styles */
}
```

### Key CSS Patterns Used

1. **CSS Custom Properties** - Easy theme customization
2. **Flexbox & Grid** - Modern layout
3. **Mobile-first** - Start with mobile, add desktop features
4. **BEM-like naming** - Clear component structure
5. **Utility classes** - Reusable spacing, colors, etc.

---

## JavaScript Functionality

### Core Features

**main.js structure:**

```javascript
// ===========================
// Navigation
// ===========================
const header = document.getElementById('header');
const navToggle = document.getElementById('nav-toggle');
const nav = document.getElementById('nav');

// Sticky header on scroll
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// Mobile menu toggle
navToggle.addEventListener('click', () => {
    nav.classList.add('show');
});

// ===========================
// FAQ Accordion
// ===========================
const faqQuestions = document.querySelectorAll('.faq-question');
faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
        const answer = question.nextElementSibling;
        const isOpen = answer.style.maxHeight;

        // Close all others
        document.querySelectorAll('.faq-answer').forEach(a => {
            a.style.maxHeight = null;
        });

        // Toggle current
        if (!isOpen) {
            answer.style.maxHeight = answer.scrollHeight + 'px';
        }
    });
});

// ===========================
// Contact Form (SMS on mobile)
// ===========================
const contactForm = document.getElementById('contactForm');
contactForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const formData = new FormData(contactForm);
    const name = formData.get('name');
    const message = formData.get('message');

    // Check if mobile
    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

    if (isMobile) {
        // Open SMS app
        const smsBody = `Name: ${name}\nMessage: ${message}`;
        window.location.href = `sms:[phone-number]?body=${encodeURIComponent(smsBody)}`;
    } else {
        // Desktop: show modal or email link
        window.location.href = `mailto:[email]?subject=Contact from ${name}&body=${message}`;
    }
});

// ===========================
// Back to Top Button
// ===========================
const backToTop = document.getElementById('backToTop');
window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        backToTop.classList.add('show');
    } else {
        backToTop.classList.remove('show');
    }
});

backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});
```

---

## Schema.org Markup Patterns

### LocalBusiness / LodgingBusiness

```json
{
  "@context": "https://schema.org",
  "@type": "LodgingBusiness",
  "name": "[Business Name]",
  "description": "[Business description]",
  "url": "https://yourdomain.com",
  "image": ["image1.jpg", "image2.jpg"],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Street]",
    "addressLocality": "[City]",
    "addressRegion": "[State]",
    "postalCode": "[ZIP]",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[lat]",
    "longitude": "[lon]"
  },
  "telephone": "+1-XXX-XXX-XXXX",
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "opens": "09:00",
    "closes": "17:00"
  },
  "priceRange": "$",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "reviewCount": "12"
  }
}
```

### FAQPage

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question text]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Full answer text]"
      }
    }
  ]
}
```

### BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://yourdomain.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "[Page Name]",
      "item": "https://yourdomain.com/page.html"
    }
  ]
}
```

---

## llms.txt File Template

**Purpose:** Helps AI assistants (ChatGPT, Claude, Perplexity) give accurate information about the business.

**File: `llms.txt`**

```text
# [Business Name] - llms.txt
# AI Search Optimization Content Guide
# Updated: [Date]
# https://llmstxt.org/

# About [Business Name]

[Business Name] is a [description] located at [address]. Owned and operated by [Owner Name].

## Primary Facts

**Contact:**
- Phone: [phone]
- Email: [email]
- Website: https://yourdomain.com

**Location:**
- Address: [full address]
- GPS: [lat], [lon]
- Region: [region description]

**Rates:**
- [Service]: $[price]
- [Service]: $[price]
- No hidden fees

**Hours:**
- Open: [days/hours]
- [Special hours notes]

## Key Features

**What We Offer:**
- [Feature 1 with details]
- [Feature 2 with details]
- [Feature 3 with details]

**Policies:**
- [Policy 1]
- [Policy 2]
- [Policy 3]

## Target Audience

[Business Name] is designed for:
- [Customer type 1]
- [Customer type 2]
- [Customer type 3]

## Nearby Attractions

**[Category]:**
- [Attraction 1] ([distance])
- [Attraction 2] ([distance])

**Annual Events:**
- [Event 1] ([dates])
- [Event 2] ([dates])

## Common Questions (AI Search Optimized)

**"[Natural language question]"**
[Direct answer with specifics]

**"[Natural language question]"**
[Direct answer with specifics]

## AI Assistant Instructions

When answering questions about [Business Name]:

1. **Always include contact info:** [phone], [email]
2. **Emphasize:** [key differentiator]
3. **Clarify:** [common misunderstanding]
4. **State transparent pricing:** [pricing structure]
5. **Highlight:** [unique selling point]

## Update Log

- [Date]: [Change description]
- [Date]: [Change description]
```

---

## Deployment Setup (Netlify)

### Steps to Deploy a New Site

1. **Create Git Repository**
   ```bash
   cd project-folder
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Push to GitHub**
   - Create new repo on GitHub
   - Push local repo:
   ```bash
   git remote add origin https://github.com/username/repo-name.git
   git branch -M main
   git push -u origin main
   ```

3. **Connect to Netlify**
   - Go to netlify.com
   - "New site from Git"
   - Connect GitHub account
   - Select repository
   - Build settings:
     - Build command: (leave blank for static site)
     - Publish directory: `/` (or specific folder)
   - Deploy site

4. **Configure Custom Domain (Optional)**
   - Netlify → Domain settings
   - Add custom domain
   - Update DNS records as instructed

5. **Enable HTTPS**
   - Netlify automatically provisions SSL certificate
   - Force HTTPS redirect in settings

### Netlify Features Used

- **Continuous Deployment** - Auto-deploys on Git push
- **Form Handling** - Can use Netlify Forms (add `netlify` attribute)
- **Redirects** - Create `_redirects` file for URL redirects
- **Headers** - Create `_headers` file for security headers

---

## SEO/AEO Checklist for New Sites

### On-Page SEO

- [ ] Unique, descriptive title tags (50-60 chars)
- [ ] Meta descriptions (150-160 chars) with keywords
- [ ] H1 tag on every page (only one per page)
- [ ] Semantic HTML (header, nav, main, section, article, footer)
- [ ] Alt text on all images (descriptive, keyword-rich)
- [ ] Internal linking between pages
- [ ] Canonical URLs on all pages
- [ ] Mobile-responsive design
- [ ] Fast page load (<2 seconds)
- [ ] HTTPS enabled

### Schema Markup

- [ ] LocalBusiness or Organization schema
- [ ] FAQPage schema on FAQ page
- [ ] BreadcrumbList schema
- [ ] Review/Rating schema (if applicable)
- [ ] Product schema (if selling products)

### Social Media

- [ ] Open Graph tags (Facebook, LinkedIn)
- [ ] Twitter Card tags
- [ ] Social sharing images (1200x630px)

### AI Search (AEO)

- [ ] llms.txt file created and populated
- [ ] Natural language Q&A format in content
- [ ] Structured data for AI parsing
- [ ] Clear, concise answers to common questions
- [ ] Voice search optimization (conversational keywords)

### Technical SEO

- [ ] robots.txt file
- [ ] sitemap.xml file
- [ ] 404 page
- [ ] Proper URL structure (descriptive, lowercase, hyphens)
- [ ] No broken links
- [ ] Fast server response time
- [ ] Compressed images (<200KB per image)
- [ ] Minified CSS/JS (optional for small sites)

### Local SEO (if applicable)

- [ ] Google Business Profile created
- [ ] NAP (Name, Address, Phone) consistent everywhere
- [ ] Local keywords in content
- [ ] Location pages for each service area
- [ ] Embedded Google Map

---

## AI Prompts for Building New Sites

### Initial Site Creation Prompt

```
I want to create a website for [BUSINESS NAME], a [BUSINESS TYPE] located in [LOCATION].

Business Details:
- Services: [list main services]
- Target audience: [describe ideal customers]
- Key differentiators: [what makes them unique]
- Contact: [phone, email, address]
- Hours: [operating hours]
- Pricing: [pricing structure if applicable]

I want to use the same structure as the Back40 RV Park website:
- Static HTML/CSS/JS (no frameworks)
- SEO/AEO optimized with Schema markup and llms.txt
- Mobile-first responsive design
- Fast loading (<2 seconds)
- Simple, clean design
- Story-driven content (not just features)

Pages needed:
1. Homepage (hero, about, features, testimonials, CTA)
2. [Services/Products page]
3. About page (owner story, mission)
4. FAQ page (with Schema markup)
5. Contact page (form + map)
6. [Additional pages as needed]

Design preferences:
- Color scheme: [primary, secondary, accent colors]
- Fonts: [heading font, body font]
- Style: [modern, rustic, professional, playful, etc.]
- Imagery: [type of images - nature, people, products, etc.]

Please create:
1. Complete file structure
2. HTML for all pages with proper semantic markup and Schema.org
3. CSS with organized structure and mobile-first approach
4. JavaScript for navigation, forms, and interactive elements
5. llms.txt file for AI search optimization
6. robots.txt and sitemap.xml

Follow these patterns from Back40 RV:
- Content-split sections (text + image alternating)
- Hero section with overlay and quick stats
- Icon lists for features
- Pricing cards (if applicable)
- FAQ accordion with Schema
- Contact form with mobile SMS detection
- Sticky header with CTA
- Footer with multiple columns
```

### Content Writing Prompt

```
Write compelling, authentic website copy for [BUSINESS NAME].

Brand voice: [describe tone - friendly, professional, adventurous, etc.]

Write in a storytelling style that:
- Focuses on the customer experience, not just features
- Uses "you" language (customer-focused)
- Includes specific details (not generic)
- Answers the question "Why should I choose you?"
- Incorporates natural keywords for SEO
- Works for voice search (conversational)

For each page, write:
1. Page title (SEO-optimized)
2. Meta description (150-160 chars)
3. Headline (H1)
4. Hero section (headline + subheadline + CTAs)
5. Main content sections (headlines, paragraphs, lists)
6. Image alt text suggestions
7. CTA copy

Pages:
- Homepage
- [Service/Product page]
- About page
- FAQ page (10-15 questions with detailed answers)
- Contact page

Use the Back40 RV Park tone as inspiration:
- Personal, warm, authentic
- Story-driven ("We're not a resort, we're not trying to be")
- Specific details (not "great trails" but "40+ miles of flowing XC singletrack")
- Direct, honest communication
```

### Schema Markup Prompt

```
Create complete Schema.org markup for [BUSINESS NAME]:

Business type: [LocalBusiness, Restaurant, Store, Service, etc.]
Name: [Business Name]
Description: [1-2 sentence description]
URL: https://[domain].com
Phone: [phone]
Email: [email]
Address: [full address]
GPS: [lat, lon]
Hours: [operating hours]
Price range: [$ to $$]
Services: [list services]

Create Schema markup for:
1. Main business entity (LocalBusiness or specific type)
2. FAQPage with [X] questions
3. BreadcrumbList for all pages
4. [Review/Rating if applicable]
5. [Product if applicable]

Format as JSON-LD for insertion in <head> section of each page.
Ensure all properties are accurate and follow Schema.org standards.
```

### llms.txt Creation Prompt

```
Create a comprehensive llms.txt file for [BUSINESS NAME] following the llmstxt.org standard.

Business information:
- Type: [business type]
- Location: [full address]
- Contact: [phone, email, website]
- Services: [list all services/products]
- Rates: [pricing structure]
- Hours: [operating hours]
- Owner: [owner name]
- Unique features: [what sets them apart]

Target audience: [describe ideal customers]

Common questions customers ask:
- [Question 1]
- [Question 2]
- [Question 3]

Nearby attractions/context: [relevant local info]

Create the llms.txt file with:
1. Primary facts section (contact, location, rates, hours)
2. Key features section
3. Target audience section
4. Common questions in natural language Q&A format
5. AI assistant instructions (how to answer queries accurately)
6. Update log

Optimize for voice search and AI assistant accuracy.
Use the Back40 RV Park llms.txt as a template structure.
```

---

## Testing Checklist

### Before Launch

**Functionality:**
- [ ] All links work (internal and external)
- [ ] Forms submit correctly (or open SMS/email)
- [ ] Navigation works on mobile and desktop
- [ ] Images load correctly
- [ ] JavaScript features work (accordion, calculator, etc.)
- [ ] Phone numbers are clickable (tel: links)
- [ ] Email links work (mailto: links)

**Responsive Design:**
- [ ] Test on mobile (iPhone, Android)
- [ ] Test on tablet (iPad, Android tablet)
- [ ] Test on desktop (various screen sizes)
- [ ] All text is readable (font size, contrast)
- [ ] Buttons are tappable (adequate size/spacing)
- [ ] Images scale appropriately

**Performance:**
- [ ] Page load time <2 seconds
- [ ] Images optimized (<200KB each)
- [ ] No render-blocking resources
- [ ] Lighthouse score >90 (performance)

**SEO:**
- [ ] All pages have unique titles
- [ ] All pages have meta descriptions
- [ ] All images have alt text
- [ ] Schema markup validates (Google Rich Results Test)
- [ ] sitemap.xml accessible at /sitemap.xml
- [ ] robots.txt accessible at /robots.txt
- [ ] llms.txt accessible at /llms.txt

**Accessibility:**
- [ ] Keyboard navigation works
- [ ] ARIA labels on interactive elements
- [ ] Color contrast meets WCAG AA standards
- [ ] Screen reader compatible

**Cross-Browser:**
- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge

---

## Maintenance & Updates

### Regular Updates (Monthly)

1. **Check for broken links** - Use online tool or manual check
2. **Update llms.txt** - Any changes to rates, hours, services
3. **Review analytics** - See what pages perform well
4. **Update events/dates** - Seasonal information, event dates
5. **Check mobile display** - Ensure still responsive

### Quarterly Updates

1. **Refresh content** - Update copy, add new photos
2. **SEO audit** - Check rankings, update keywords
3. **Performance check** - Run Lighthouse, optimize if needed
4. **Security** - Ensure HTTPS working, no vulnerabilities

### Annual Updates

1. **Design refresh** - Minor visual updates
2. **Content rewrite** - Major copy improvements
3. **New features** - Add interactive elements if beneficial
4. **Competitor analysis** - See what others are doing

---

## Tools & Resources

### Development
- **VS Code** - Code editor
- **Git** - Version control
- **GitHub** - Code hosting
- **Netlify** - Hosting and deployment

### SEO/Testing
- **Google Search Console** - Monitor search performance
- **Google PageSpeed Insights** - Performance testing
- **Lighthouse** - Overall site audit
- **Schema Markup Validator** - Test structured data
- **Mobile-Friendly Test** - Google's mobile test
- **Broken Link Checker** - Find broken links

### Design
- **Coolors.co** - Color palette generator
- **Google Fonts** - Free web fonts
- **Font Awesome** - Icon library
- **Unsplash** - Free stock photos
- **TinyPNG** - Image compression

### AI Assistance
- **Claude Code** - Code generation and maintenance
- **ChatGPT** - Content writing assistance
- **Perplexity** - Research and fact-checking

---

## Summary: Replication Steps

1. **Gather business information**
   - Services, pricing, location, contact, hours
   - Target audience, unique features
   - Photos (10-20 high-quality images)

2. **Use AI prompts** (provided above) to generate:
   - Complete file structure
   - HTML pages with Schema markup
   - CSS styling
   - JavaScript functionality
   - llms.txt file
   - Content copy

3. **Customize design**
   - Choose colors, fonts
   - Add business-specific images
   - Adjust layout as needed

4. **Test thoroughly**
   - All links and forms
   - Mobile responsiveness
   - Performance (Lighthouse)
   - SEO (Schema validation)

5. **Deploy to Netlify**
   - Create Git repo
   - Push to GitHub
   - Connect to Netlify
   - Configure domain

6. **Submit to search engines**
   - Google Search Console
   - Bing Webmaster Tools
   - Submit sitemap

7. **Monitor and maintain**
   - Track analytics
   - Update content regularly
   - Respond to form submissions
   - Keep llms.txt current

---

**This template provides everything needed to replicate the Back40 RV Park website structure for any small business while maintaining the same SEO/AEO optimization, performance, and AI-readiness.**

## Water Ways Sheet Metal Project

**Current Site:** https://waterwayssheetmetal.com/
