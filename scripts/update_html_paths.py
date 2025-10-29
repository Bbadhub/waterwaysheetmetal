#!/usr/bin/env python3
"""
Update HTML files with new canonical image paths after deduplication
Uses IMAGE_REFACTOR_MAPPING.json to replace old paths with new paths
"""

import json
import os
import re
from pathlib import Path

def load_mapping(mapping_file):
    """Load the rename mapping from JSON"""
    with open(mapping_file, 'r') as f:
        data = json.load(f)
    return data['rename_map']

def update_html_file(html_path, rename_map, images_dir):
    """Update image paths in a single HTML file"""

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    replacements_made = []

    # Process each old_path -> new_path mapping
    for old_path, new_path in rename_map.items():
        # Convert Windows backslashes to forward slashes for HTML
        old_path_html = old_path.replace('\\', '/')
        new_path_html = new_path.replace('\\', '/')

        # Pattern 1: Direct image references in images/ directory
        # Example: images/downloads/p7210424.jpg -> images/architectural/custom-metalwork-1.jpg
        pattern1 = re.escape(f"images/{old_path_html}")
        replacement1 = f"images/{new_path_html}"

        if re.search(pattern1, content):
            content = re.sub(pattern1, replacement1, content)
            replacements_made.append(f"  {old_path_html} -> {new_path_html}")

        # Pattern 2: Optimized image references
        # Example: images-optimized/downloads/hero/p7210424.jpg -> images-optimized/architectural/hero/custom-metalwork-1.jpg
        old_dir = os.path.dirname(old_path_html)
        old_file = os.path.basename(old_path_html)
        new_dir = os.path.dirname(new_path_html)
        new_file = os.path.basename(new_path_html)

        # For optimized paths, preserve /hero/, /featured/ subdirs
        for subdir in ['hero', 'featured', 'gallery', '']:
            if subdir:
                pattern_opt = re.escape(f"images-optimized/{old_dir}/{subdir}/{old_file}")
                replacement_opt = f"images-optimized/{new_dir}/{subdir}/{new_file}"
            else:
                pattern_opt = re.escape(f"images-optimized/{old_dir}/{old_file}")
                replacement_opt = f"images-optimized/{new_dir}/{new_file}"

            if re.search(pattern_opt, content):
                content = re.sub(pattern_opt, replacement_opt, content)
                replacements_made.append(f"  [optimized] {pattern_opt} -> {replacement_opt}")

        # Pattern 3: Also handle .webp extensions for optimized images
        old_file_base = os.path.splitext(old_file)[0]
        new_file_base = os.path.splitext(new_file)[0]

        for subdir in ['hero', 'featured', 'gallery', '']:
            if subdir:
                pattern_webp = re.escape(f"images-optimized/{old_dir}/{subdir}/{old_file_base}.webp")
                replacement_webp = f"images-optimized/{new_dir}/{subdir}/{new_file_base}.webp"
            else:
                pattern_webp = re.escape(f"images-optimized/{old_dir}/{old_file_base}.webp")
                replacement_webp = f"images-optimized/{new_dir}/{new_file_base}.webp"

            if re.search(pattern_webp, content):
                content = re.sub(pattern_webp, replacement_webp, content)
                replacements_made.append(f"  [webp] {pattern_webp} -> {replacement_webp}")

    # Only write if changes were made
    if content != original_content:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return replacements_made

    return []

def main():
    project_root = Path(__file__).parent.parent
    mapping_file = project_root / 'IMAGE_REFACTOR_MAPPING.json'
    images_dir = project_root / 'images'

    print("=" * 80)
    print("UPDATING HTML FILES WITH NEW IMAGE PATHS")
    print("=" * 80)
    print()

    # Load mapping
    print("Loading mapping file...")
    rename_map = load_mapping(mapping_file)
    print(f"  Found {len(rename_map)} path mappings")
    print()

    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk(project_root):
        # Skip certain directories
        if any(skip in root for skip in ['images', 'scripts', 'node_modules', '.git']):
            continue

        for filename in files:
            if filename.endswith('.html'):
                html_files.append(os.path.join(root, filename))

    print(f"Found {len(html_files)} HTML files to process")
    print()

    # Process each HTML file
    total_replacements = 0
    files_updated = 0

    for html_path in html_files:
        rel_path = os.path.relpath(html_path, project_root)
        replacements = update_html_file(html_path, rename_map, images_dir)

        if replacements:
            files_updated += 1
            total_replacements += len(replacements)
            print(f"{rel_path}")
            for r in replacements:
                print(r)
            print()

    # Summary
    print("=" * 80)
    print("UPDATE COMPLETE")
    print("=" * 80)
    print(f"Files processed: {len(html_files)}")
    print(f"Files updated: {files_updated}")
    print(f"Total replacements: {total_replacements}")
    print()
    print("Next steps:")
    print("1. Delete old images-optimized/ directory")
    print("2. Run optimize_images.py to regenerate optimized versions")
    print("3. Test website to verify all images load correctly")

if __name__ == '__main__':
    main()
