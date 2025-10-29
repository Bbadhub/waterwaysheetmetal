# Water Ways Sheet Metal - Image Reorganization Plan

**Date:** 2025-10-29
**Purpose:** Deduplicate and properly organize 102 truly unique images

---

## Current Problem

- **184 total image files** in images/ directory
- **Only 102 unique images** (82 are duplicates!)
- Images scattered across multiple directories with no clear organization
- Same image copied to downloads/, hero/, homepage-showcase/, category/ dirs

## Solution: Clean Project-Based Structure

```
images/
├── projects/
│   ├── bay-window-twf/          # 23 images - complete project sequence
│   ├── ohio-chimney-caps/        # 7 images - French caps project
│   ├── pinion-chimney-pots/      # 6 images - Pagoda pots project
│   ├── minnesota-shroud/         # 1 real image (33 corrupt placeholders deleted)
│   └── mid-continent-tower/      # Commercial project images
├── categories/
│   ├── chimney-caps/             # Generic cap shots (not project-specific)
│   ├── flashing/                 # Generic flashing examples
│   ├── roofing/                  # Generic roof work
│   ├── gutters/                  # 1 image - p4170196.jpg
│   ├── architectural/            # Custom metalwork, interior
│   └── branding/                 # Team photos (Ray, Natalie)
└── site/
    └── logo/                     # Waterways logo

```

---

## Deduplication Actions

### DELETE These Duplicate Directories:
- `downloads/` - All duplicates of images in other directories
- `hero/` - All duplicates
- `homepage-showcase/` - All duplicates

### KEEP One Copy in Best Location:

**Projects (keep in projects/ subdirs):**
1. Bay Window TWF → All 23 images stay in `flashing/bay-window-twf/`
2. Ohio Project → Move to `projects/ohio-chimney-caps/`
3. Pinion Pots → Move to `projects/pinion-chimney-pots/`
4. Minnesota Shroud → Keep 1 real image, delete 33 corrupt placeholders

**Categories (keep in categories/ subdirs):**
1. Chimney Caps → Keep unique caps in `categories/chimney-caps/`
2. Flashing → Keep in `categories/flashing/`
3. Roofing → Keep in `categories/roofing/`
4. Gutters → Keep 1 image in `categories/gutters/`
5. Architectural → Keep in `categories/architectural/`
6. Interior → Keep in `categories/interior/`

**Team/Branding:**
1. Keep in `categories/branding/` (Ray, Natalie photos)

---

## Step-by-Step Reorganization

### Phase 1: Delete Corrupt/Placeholder Images (33 files)
All the 35KB images in:
- `chimney-caps/minnesota-delivery/` (most)
- `chimney-caps/ohio-project/` (drone shots)
- `flashing/chimney-flashing/` (all corrupt)

### Phase 2: Consolidate Duplicate Groups

**Group 1: p7210424.jpg (6 copies → keep 1)**
- KEEP: `categories/architectural/p7210424.jpg`
- DELETE: architectural/mid-continent-tower.jpg, architectural/custom-metalwork-1.jpg
- DELETE: downloads/p7210424.jpg, hero/p7210424.jpg, homepage-showcase/p7210424.jpg

**Group 2: Custom caps (6 copies → keep each unique)**
Actually these might be different angles! Check if:
- `custom-cap-1.jpg` vs `img_2252.jpg` vs `minnesota-shroud.jpg` vs `nc-custom-cap.jpg`
Are truly the same image? Hash says YES - so keep best name.

**Group 3: Ohio French Caps (6 copies → keep 1)**
- KEEP: `categories/chimney-caps/ohio-french-caps.jpg`
- DELETE: chimney-caps/pa080064.jpg, downloads/pa080064.jpg, hero/copper-work-closeup.jpg, hero/pa080064.jpg, homepage-showcase/pa080064.jpg

**Group 4: Copper roof on turret (4 copies → keep 1)**
- KEEP: `categories/flashing/copper-roof-on-turret-1.png`
- DELETE: downloads/, hero/, homepage-showcase/ copies

**Group 5: p7080090 roofing (4 copies → keep 1)**
- KEEP: `categories/roofing/p7080090.jpg`
- DELETE: roofing/copper-roof-1.jpg (duplicate!), downloads/, homepage-showcase/ copies

**Group 6: pb190444 flashing (4 copies → keep 1)**
- KEEP: `categories/flashing/pb190444.jpg`
- DELETE: flashing/copper-flashing-1.jpg (duplicate!), downloads/, homepage-showcase/ copies

### Phase 3: Move Project Groups

**Bay Window TWF (23 images):**
- Already in good location: `flashing/bay-window-twf/`
- Rename parent to: `projects/bay-window-twf/`

**Ohio Chimney Caps:**
- Move IMG_1447-cropped.jpg through IMG_1457.jpg
- To: `projects/ohio-chimney-caps/`

**Pinion Chimney Pots:**
- Move IMG_0696-cropped.jpg through IMG_0843.jpg (5-6 images)
- To: `projects/pinion-chimney-pots/`

---

## Final Structure - 102 Unique Images

### Projects (organized by complete project sequences):
- `projects/bay-window-twf/` - 23 images
- `projects/ohio-chimney-caps/` - 4 images
- `projects/pinion-chimney-pots/` - 5 images
- `projects/minnesota-shroud/` - 1 image
- **Subtotal: ~33 project images**

### Categories (generic examples, not project-specific):
- `categories/chimney-caps/` - ~15 images
- `categories/flashing/` - ~10 images
- `categories/roofing/` - ~8 images
- `categories/gutters/` - 1 image
- `categories/architectural/` - ~10 images
- `categories/interior/` - ~6 images
- `categories/branding/` - 4 images (team photos)
- **Subtotal: ~54 category images**

### Site Assets:
- `site/logo/` - 1 image
- `site/reviews/` - 3 images (customer photos)
- **Subtotal: 4 images**

### Other:
- Miscellaneous - ~11 images
- **Subtotal: 11 images**

**TOTAL: 102 truly unique images**

---

## HTML Update Strategy

After reorganization, update all HTML files to use new canonical paths:

1. Search for old paths (downloads/, hero/, homepage-showcase/)
2. Replace with new category or project paths
3. Use consistent naming: `categories/{type}/hero/filename.ext`

---

## Implementation Commands

```bash
# 1. Backup current state
cp -r images/ images-backup-2025-10-29/

# 2. Delete corrupt images (35KB placeholders)
# ... specific delete commands

# 3. Create new structure
mkdir -p images/projects/{bay-window-twf,ohio-chimney-caps,pinion-chimney-pots,minnesota-shroud}
mkdir -p images/categories/{chimney-caps,flashing,roofing,gutters,architectural,interior,branding}
mkdir -p images/site/{logo,reviews}

# 4. Move files to correct locations
# ... specific move commands

# 5. Delete duplicate directories
rm -rf images/downloads/
rm -rf images/hero/
rm -rf images/homepage-showcase/

# 6. Re-run optimization script on clean structure
python scripts/optimize_images.py
```

---

## Benefits

1. **Clear organization** - Projects vs categories vs site assets
2. **No confusion** - Each unique image in one place
3. **Better maintenance** - Easy to find images for content
4. **Accurate inventory** - 102 unique images properly cataloged
5. **Smaller repo** - Delete 82 duplicate files

---

## Next Steps

1. Review this plan
2. Execute reorganization script
3. Update all HTML files with new paths
4. Delete old duplicate directories
5. Re-optimize images with clean structure
6. Create new accurate IMAGE_CATALOG.md
