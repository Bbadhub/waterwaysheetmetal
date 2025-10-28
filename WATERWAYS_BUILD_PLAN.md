# Water Ways Sheet Metal - Website Rebuild Implementation Plan

**Date:** 2025-10-25
**Project:** Phase 1 - Parent Company Site Rebuild
**Domain:** waterwayssheetmetal.com
**Timeline:** 4-6 weeks to launch

---

## Project Overview

**Objective:** Rebuild Water Ways Sheet Metal website as a modern, high-performing, SEO-optimized site that generates leads and showcases custom copper and sheet metal craftsmanship.

**Current State:**
- WordPress site (Travelify theme)
- Gallery-focused
- Limited SEO optimization
- Contact: (479) 957-3794 | Ray@WaterwaysSheetMetal.com

**New Site:**
- Static HTML/CSS/JS (fast, secure, no WordPress)
- SEO/AEO optimized
- Mobile-first responsive
- Lead generation focused
- Professional portfolio showcase

---

## Information Gathering Checklist

### Business Information Needed

**Contact & Location:**
- [ ] Full business address (street, city, state, zip)
- [ ] GPS coordinates (for Schema markup)
- [ ] Hours of operation
- [ ] Best phone number for customers
- [ ] Best email for customer inquiries
- [ ] Any other contact methods (fax, secondary phone)

**Business Details:**
- [ ] Year founded/established
- [ ] Legal business name (if different from "Water Ways Sheet Metal")
- [ ] Owner name(s) - Ray + others?
- [ ] Number of employees/team size
- [ ] Licenses/certifications
- [ ] Insurance information (for credibility)
- [ ] Trade association memberships (SMACNA, etc.)

**Service Area:**
- [ ] Primary service radius (miles from Siloam Springs)
- [ ] Cities/regions regularly served
- [ ] States served (AR, OK, MO, KS confirmed)
- [ ] Do you ship nationwide?
- [ ] Do you offer installation? (local only or broader)

**Products & Services:**
- [ ] Complete list of services offered
- [ ] Which are most profitable/desired?
- [ ] Any services you DON'T want to promote?
- [ ] Materials you work with (confirmed: copper, Rheinzink - others?)
- [ ] Typical project sizes (residential vs. commercial split)
- [ ] Custom capabilities vs. standard products

**Pricing & Process:**
- [ ] Typical price ranges (we won't publish, but good to know)
- [ ] How do you prefer customers to contact? (phone, form, email)
- [ ] Do you offer free quotes/consultations?
- [ ] Typical turnaround time for quotes
- [ ] Typical project timeline (design to completion)
- [ ] Payment terms (deposit, final payment, etc.)
- [ ] Do you offer financing?

**Competitive Positioning:**
- [ ] What makes Water Ways different from competitors?
- [ ] Why should customers choose you over big box stores?
- [ ] Why copper over stainless steel? (your pitch)
- [ ] Any unique processes or technologies?
- [ ] Awards, recognition, notable projects?

### Content Assets Needed

**Images:**
- [ ] Download all existing images from current site (DONE - list created)
- [ ] High-resolution photos of recent projects (need 20-30 total)
- [ ] Shop/facility photos (exterior, interior, equipment)
- [ ] Team photos (Ray, craftsmen at work)
- [ ] Process photos (fabrication, welding, installation)
- [ ] Material close-ups (copper textures, patina stages)
- [ ] Logo (high-resolution, vector if possible)

**Project Portfolio:**
- [ ] 10-15 completed projects for portfolio page
- [ ] For each project need:
  - Project name/description
  - Location (city, state)
  - Date completed
  - Materials used
  - 3-5 photos minimum
  - Any challenges/special features
  - Client testimonial if available

**Testimonials:**
- [ ] 5-10 customer testimonials
- [ ] For each: quote, name, location, project type
- [ ] Permission to use on website
- [ ] Photos of customers or projects (optional)

**About/Story Content:**
- [ ] Company founding story
- [ ] Ray's background and expertise
- [ ] Why you started the business
- [ ] What drives your passion for copper/metalwork
- [ ] Any family business history
- [ ] Evolution of the business over time

### Legal & Technical

**Required:**
- [ ] Access to domain registrar (waterwayssheetmetal.com)
- [ ] Access to current hosting account
- [ ] Google Analytics account (or create new)
- [ ] Google Search Console access (or set up)
- [ ] Privacy policy requirements (state laws)
- [ ] Terms of service requirements

**Optional but Recommended:**
- [ ] Google Business Profile (claim/optimize)
- [ ] Bing Places for Business
- [ ] Any existing social media accounts to link

---

## Build Timeline & Phases

### Week 1: Planning & Content Gathering
**Tasks:**
- Gather all business information (checklist above)
- Download and organize all images from current site
- Collect new photos if needed
- Write/edit company story and about content
- Compile project portfolio details
- Gather testimonials

**Deliverables:**
- Content document with all copy
- Organized image folders
- Project portfolio spreadsheet

---

### Week 2: Design & Structure
**Tasks:**
- Finalize color scheme and typography
- Create mockups for homepage (optional but recommended)
- Write copy for all main pages
- Organize navigation structure
- Create wireframes for key pages

**Deliverables:**
- Design style guide
- All page copy written and approved
- Site structure finalized

---

### Week 3-4: Development
**Tasks:**
- Build HTML structure for all pages
- Write CSS (following design system from architecture doc)
- Implement JavaScript functionality
- Optimize all images
- Add Schema markup
- Create llms.txt file
- Mobile responsiveness testing

**Deliverables:**
- Functional website on staging server
- All pages coded and linked
- Mobile-responsive design

---

### Week 5: Testing & Refinement
**Tasks:**
- Cross-browser testing (Chrome, Firefox, Safari, Edge)
- Mobile device testing (iPhone, Android)
- Performance optimization (Lighthouse score >90)
- SEO validation (Schema, meta tags, titles)
- Contact form testing (desktop and mobile)
- Link checking (all internal/external links)
- Content proofreading
- Client review and feedback

**Deliverables:**
- Polished, tested website
- Performance report
- List of any final changes needed

---

### Week 6: Launch & Post-Launch
**Tasks:**
- Final client approval
- DNS/hosting setup (if changing)
- Site launch to live domain
- Submit sitemap to Google Search Console
- Submit sitemap to Bing Webmaster Tools
- Set up Google Analytics tracking
- Verify Google Business Profile
- Monitor for any issues
- Create redirect map (if URLs changing from WordPress)

**Deliverables:**
- Live website at waterwayssheetmetal.com
- Analytics tracking active
- Search engine submission complete

---

## Immediate Next Steps (This Week)

### Priority 1: Information Gathering
Create a simple document or form for Ray to fill out with:
1. **Business basics** (address, hours, team size, year founded)
2. **Service area** (specific cities/regions served)
3. **Key differentiators** (why choose Water Ways?)
4. **Image access** (can we download from current site or need new photos?)
5. **Project portfolio** (which projects to feature?)

### Priority 2: Download Existing Assets
- Download all images from waterwayssheetmetal.com/wp-content/gallery/
- Organize by category (chimney-caps, flashing, roofing, architectural, etc.)
- Optimize images (<200KB, WebP format)
- Create image inventory spreadsheet

### Priority 3: Content Framework
Start writing core pages based on what we already know:
- Homepage hero/intro text
- About page framework (fill in specifics later)
- Services pages structure
- FAQ questions (even if answers need refinement)

### Priority 4: Technical Setup
- Verify domain access/ownership
- Set up staging environment (GitHub repo + Netlify)
- Create project file structure locally

---

## Project File Structure Setup

```
waterways-site/
│
├── index.html
├── about.html
├── contact.html
├── portfolio.html
├── faq.html
├── testimonials.html
│
├── services/
│   ├── chimney-caps.html
│   ├── flashing.html
│   ├── roofing-gutters.html
│   └── custom-metalwork.html
│
├── portfolio/
│   ├── project-1.html
│   └── (individual project pages)
│
├── css/
│   └── style.css
│
├── js/
│   └── main.js
│
├── images/
│   ├── hero/
│   ├── services/
│   ├── portfolio/
│   ├── about/
│   ├── team/
│   └── icons/
│
├── llms.txt
├── robots.txt
├── sitemap.xml
└── README.md
```

---

## Design Decisions Needed

### Color Scheme (Proposed)
**Primary:**
- Copper: #B87333
- Dark Copper: #8B4513
- Charcoal: #333333
- White: #FFFFFF
- Light Gray: #F5F5F5

**Accent:**
- Patina Green: #469F9A
- Deep Blue: #1E3A5F

**Question for Ray:** Do these colors feel right for the Water Ways brand? Any preferences?

### Typography (Proposed)
- **Headlines:** Playfair Display (elegant serif)
- **Body:** Inter (clean, modern sans-serif)

**Question for Ray:** Any font preferences? Want more traditional/classic or more modern?

### Logo
**Question for Ray:**
- Do you have an existing logo?
- If yes, need high-resolution file (vector/SVG preferred, or high-res PNG)
- If no, should we create one? (Simple text logo or graphic element?)

---

## Content Writing Approach

### Voice & Tone Guidelines
**What we know about Water Ways:**
- "21st century technology meets centuries-old craftsmanship"
- Premium copper craftsmen
- Custom fabrication (not mass production)
- Family business feel (need to confirm)
- Professional but approachable
- Pride in workmanship

**Tone we'll use:**
- Expert but not arrogant
- Warm and personable
- Detail-oriented without overwhelming
- Educational (teach customers about copper benefits)
- Confident in quality
- Customer-focused ("your home," "you deserve")

### Sample Homepage Hero Copy (Draft)

**Option 1 (Heritage focus):**
```
Headline: Crafting Excellence in Copper & Sheet Metal Since [Year]
Subheadline: Where 21st century technology meets centuries-old craftsmanship
CTA: Get a Free Quote | View Our Work
```

**Option 2 (Benefit focus):**
```
Headline: Custom Copper & Sheet Metal That Lasts Generations
Subheadline: Protecting Northwest Arkansas homes with handcrafted quality since [Year]
CTA: Request a Consultation | See Our Portfolio
```

**Option 3 (Craft focus):**
```
Headline: Master Craftsmen. Modern Technology. Timeless Results.
Subheadline: Custom copper chimney caps, flashing, roofing, and architectural metalwork
CTA: Start Your Project | Call (479) 957-3794
```

**Question for Ray:** Which approach resonates most? Any specific message you want emphasized?

---

## Questions for Ray/Water Ways Team

### Critical (Need answers before we can proceed):
1. **Contact info:** Full address, hours of operation, preferred contact method?
2. **Service area:** Specific cities/regions you serve most?
3. **Images:** Can we use all images from current site? Need new photos?
4. **Logo:** Do you have an existing logo file?
5. **Installation:** Do you offer installation services or fabrication only?

### Important (Need for content quality):
6. **Company history:** Year founded? How did Water Ways start?
7. **Team:** Who's on the team? Ray + how many craftsmen?
8. **Certifications:** Any licenses, insurance, trade memberships?
9. **Turnaround:** Typical timeline from quote to completion?
10. **Projects:** Which 10-15 projects should we feature in portfolio?

### Nice to have (Can fill in later):
11. **Testimonials:** Do you have customer reviews we can use?
12. **Differentiators:** What makes you different from competitors?
13. **Materials:** Any materials besides copper/Rheinzink you want to highlight?
14. **Future products:** Any mention of wholesale/distribution program? (Sets up CopperCraft Caps later)

---

## Technical Decisions

### Hosting Approach
**Recommended:** Netlify (free tier)
- Auto-deploys from Git
- Free SSL certificate
- Fast CDN
- Custom domain support
- Form handling (if needed)

**Alternative:** Current WordPress hosting (if you want to keep existing)

**Question:** Do you want to keep current hosting or move to new platform?

### Form Handling
**Current plan:**
- Desktop: Opens email client (mailto:)
- Mobile: Opens SMS app with pre-filled message

**Alternative options:**
- Netlify Forms (simple, free tier available)
- FormSpree (third-party service)
- Email service integration (SendGrid, etc.)

**Question:** How do you prefer to receive customer inquiries?

### Analytics
**Recommended setup:**
- Google Analytics 4 (free, comprehensive)
- Google Search Console (SEO monitoring)
- Optional: Hotjar or similar (user behavior tracking)

**Question:** Do you currently use analytics? Want to track conversions/leads?

---

## Budget Considerations

### Free/Minimal Cost Approach:
- Static HTML/CSS/JS (no monthly CMS fees)
- Netlify hosting (free tier)
- Google Fonts (free)
- Font Awesome icons (free tier)
- DIY logo (text-based)
- **Total ongoing cost:** ~$10-15/year (just domain renewal)

### Professional Investment:
- Custom logo design: $300-1,000
- Professional photography: $500-1,500
- Premium fonts (optional): $0-100
- Premium icons (optional): $0-50
- **One-time investment:** $800-2,650

**Question:** Budget for professional design/photography or DIY approach?

---

## Success Metrics

### Launch Goals:
- [ ] Page load time <2 seconds
- [ ] Lighthouse Performance score >90
- [ ] Mobile-friendly (Google test passes)
- [ ] All Schema markup validates
- [ ] 10+ portfolio projects featured
- [ ] 5+ customer testimonials
- [ ] Contact form functional on all devices

### 30-Day Post-Launch:
- [ ] Indexed in Google (all main pages)
- [ ] Google Business Profile optimized
- [ ] 5+ organic search visitors/day
- [ ] 2+ contact form submissions/week (adjust based on seasonality)

### 90-Day Goals:
- [ ] Ranking on page 1 for "sheet metal fabrication Arkansas"
- [ ] Ranking on page 1 for "[city] custom copper work"
- [ ] 20+ organic visitors/day
- [ ] 10+ leads/month

---

## Next Actions for You (Brett)

**This week:**
1. **Schedule call/meeting with Ray** to go through information gathering checklist
2. **Download existing images** from current site (we have the list)
3. **Set up project repository** (GitHub + Netlify for staging)
4. **Create content gathering document** (Google Doc or similar) for Ray to fill out
5. **Confirm timeline** - is 4-6 weeks realistic for their needs?

**Questions to answer:**
- Who will write the copy? (AI-assisted with your input, or Ray writes it?)
- Who will take new photos if needed? (Professional photographer or DIY?)
- What's the approval process? (Ray reviews each page, or final review only?)
- Launch deadline? (Any specific date/season they want to go live?)

---

## What We Can Start Building Now (Without Additional Info)

Based on what we already know from the current site:

### Can Build Immediately:
1. **Homepage structure** (hero, services overview, process, CTA)
2. **Service pages structure** (chimney caps, flashing, roofing, custom work)
3. **Portfolio page layout** (grid structure, project cards)
4. **FAQ page** (common questions, need answers filled in)
5. **Contact page** (form, contact methods, map area)
6. **CSS framework** (colors, typography, components)
7. **JavaScript** (navigation, accordions, mobile menu)

### Need Client Input For:
1. **About page** (company history, team bios)
2. **Specific service details** (pricing approach, turnaround times)
3. **Individual project pages** (which projects, descriptions)
4. **Testimonials** (customer reviews)
5. **Exact contact info** (hours, address, team names)
6. **Logo and branding** (if custom logo needed)

---

## Recommendation: Start Here

**Option A: Build skeleton, fill in later**
- Build complete site structure with placeholder content
- Ray reviews structure/flow
- Then we fill in real content
- **Pros:** See the full site quickly, easier to visualize
- **Cons:** More revisions later

**Option B: Page by page with real content**
- Get all homepage info first
- Build homepage completely
- Get approval, move to next page
- **Pros:** Each page is "done" when finished
- **Cons:** Slower initial progress

**Recommended:** **Hybrid approach**
1. Build homepage with real content (this week)
2. Build other pages with structure + partial content
3. Ray reviews everything
4. Fill in gaps and refine
5. Final approval and launch

---

**Ready to start? Let me know what information you can get from Ray this week, and we'll begin building!**
