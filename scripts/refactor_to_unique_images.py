#!/usr/bin/env python3
"""
Refactor Images to Truly Unique Set
- Identify all truly unique images by hash
- Pick best filename and location for each
- Delete all duplicates
- Create mapping file for HTML updates
"""

import os
import shutil
import hashlib
import json
from pathlib import Path
from collections import defaultdict
import re

def get_file_hash(filepath):
    """Calculate MD5 hash of file"""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def score_filename(filename):
    """Score filename - higher is better (more descriptive)"""
    score = 0
    base_name = Path(filename).stem.lower()

    # Prefer descriptive names
    descriptive_words = [
        'copper', 'chimney', 'cap', 'flashing', 'roof', 'turret',
        'ohio', 'french', 'custom', 'minnesota', 'shroud', 'bay',
        'window', 'gutter', 'metalwork', 'architectural', 'dormer',
        'tower', 'natalie', 'ray', 'installation', 'elegant', 'patina'
    ]

    for word in descriptive_words:
        if word in base_name:
            score += 10

    # Penalize camera IDs
    camera_patterns = [
        r'^img_\d+', r'^dsc_?\d+', r'^dcim\d+',
        r'^p\d{7}', r'^\d{6}-r\d', r'^[a-z]\d{7}'
    ]

    for pattern in camera_patterns:
        if re.match(pattern, base_name, re.IGNORECASE):
            score -= 50

    # Prefer shorter, cleaner names (not too long)
    if len(base_name) > 40:
        score -= 5
    elif 10 < len(base_name) < 30:
        score += 5

    # Prefer names with meaningful separators
    if '-' in base_name or '_' in base_name:
        score += 2

    return score

def score_directory(dirpath, images_dir):
    """Score directory - higher is better"""
    rel_path = os.path.relpath(dirpath, images_dir).lower()
    score = 0

    # Prefer organized category directories
    if 'branding' in rel_path:
        score += 30
    elif 'bay-window' in rel_path or 'ohio' in rel_path or 'pinion' in rel_path:
        score += 25  # Project directories
    elif 'chimney-caps' in rel_path or 'flashing' in rel_path or 'roofing' in rel_path:
        score += 20  # Category directories
    elif 'architectural' in rel_path or 'interior' in rel_path or 'gutters' in rel_path:
        score += 15

    # Penalize generic directories
    if 'downloads' in rel_path:
        score -= 100
    elif 'hero' in rel_path:
        score -= 80
    elif 'homepage-showcase' in rel_path:
        score -= 80

    return score

def is_corrupt_placeholder(filepath):
    """Check if file is a corrupt 35KB placeholder"""
    size = os.path.getsize(filepath)
    if size == 35525:  # The exact size of corrupt files
        try:
            from PIL import Image
            Image.open(filepath)
            return False
        except:
            return True
    return False

def choose_best_file(files, images_dir):
    """Choose the best file from duplicates"""
    valid_files = [f for f in files if not is_corrupt_placeholder(f['path'])]

    if not valid_files:
        return None

    # Score each file
    for f in valid_files:
        filename_score = score_filename(f['filename'])
        dir_score = score_directory(os.path.dirname(f['path']), images_dir)
        f['score'] = filename_score + dir_score

    # Return highest scoring file
    return max(valid_files, key=lambda x: x['score'])

def analyze_all_images(images_dir):
    """Analyze all images and group by hash"""
    hash_to_files = defaultdict(list)

    for root, dirs, files in os.walk(images_dir):
        if 'optimized' in root or 'logo' in root:
            continue

        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                filepath = os.path.join(root, filename)
                try:
                    file_hash = get_file_hash(filepath)
                    file_size = os.path.getsize(filepath)

                    file_info = {
                        'path': filepath,
                        'filename': filename,
                        'size': file_size,
                        'hash': file_hash,
                        'directory': os.path.dirname(filepath)
                    }

                    hash_to_files[file_hash].append(file_info)

                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

    return hash_to_files

def main():
    images_dir = Path(__file__).parent.parent / 'images'
    backup_dir = Path(__file__).parent.parent / 'images-backup-before-refactor'

    print("=" * 80)
    print("WATER WAYS SHEET METAL - IMAGE REFACTORING")
    print("Deduplicating to truly unique set")
    print("=" * 80)
    print()

    # Safety check
    response = input("This will DELETE duplicate files. Continue? (yes/no): ")
    if response.lower() != 'yes':
        print("Aborted.")
        return

    # Backup first
    print("\n1. Creating backup...")
    if backup_dir.exists():
        print(f"   Backup already exists at: {backup_dir}")
    else:
        print(f"   Backing up to: {backup_dir}")
        try:
            # Custom copy function that skips problematic files
            def ignore_patterns(directory, files):
                ignore = []
                for f in files:
                    if 'optimized' in f or f in ['nul', 'con', 'prn', 'aux']:
                        ignore.append(f)
                return ignore

            shutil.copytree(images_dir, backup_dir, ignore=ignore_patterns)
            print("   [OK] Backup complete")
        except Exception as e:
            print(f"   WARNING: Backup had issues: {e}")
            print("   Continuing anyway...")

    # Analyze
    print("\n2. Analyzing all images...")
    hash_to_files = analyze_all_images(images_dir)

    total_files = sum(len(files) for files in hash_to_files.values())
    unique_images = len(hash_to_files)
    duplicate_files = total_files - unique_images

    print(f"   Total image files: {total_files}")
    print(f"   Unique images (by hash): {unique_images}")
    print(f"   Duplicate files to remove: {duplicate_files}")

    # Choose best files
    print("\n3. Selecting best version of each image...")

    kept_files = []
    deleted_files = []
    rename_map = {}  # old_path -> new_path for HTML updates

    for file_hash, files in hash_to_files.items():
        if len(files) == 1:
            # Only one copy - keep it
            kept_files.append(files[0])
            continue

        # Multiple copies - choose best
        best = choose_best_file(files, images_dir)

        if not best:
            print(f"   WARNING: No valid file found for hash {file_hash[:8]}")
            continue

        kept_files.append(best)

        # Mark others for deletion
        for f in files:
            if f['path'] != best['path']:
                deleted_files.append(f)
                # Map old path to new best path
                rename_map[f['path']] = best['path']

        # Show what we're keeping
        if len(files) > 1:
            print(f"\n   Hash {file_hash[:8]} ({len(files)} copies):")
            print(f"   [KEEP] {os.path.relpath(best['path'], images_dir)}")
            print(f"          (score: {best.get('score', 0)})")
            for f in files:
                if f['path'] != best['path']:
                    print(f"   [DEL]  {os.path.relpath(f['path'], images_dir)}")

    # Delete duplicates
    print(f"\n4. Deleting {len(deleted_files)} duplicate files...")

    for f in deleted_files:
        try:
            os.remove(f['path'])
            print(f"   Deleted: {os.path.relpath(f['path'], images_dir)}")
        except Exception as e:
            print(f"   ERROR deleting {f['path']}: {e}")

    # Save mapping file
    print("\n5. Creating mapping file for HTML updates...")

    mapping_output = {
        'summary': {
            'original_files': total_files,
            'unique_images': unique_images,
            'deleted_duplicates': len(deleted_files),
            'kept_files': len(kept_files)
        },
        'kept_files': [
            {
                'path': os.path.relpath(f['path'], images_dir),
                'filename': f['filename'],
                'size': f['size'],
                'hash': f['hash']
            }
            for f in kept_files
        ],
        'rename_map': {
            os.path.relpath(old, images_dir): os.path.relpath(new, images_dir)
            for old, new in rename_map.items()
        }
    }

    mapping_file = images_dir.parent / 'IMAGE_REFACTOR_MAPPING.json'
    with open(mapping_file, 'w') as f:
        json.dump(mapping_output, f, indent=2)

    print(f"   Saved to: {mapping_file}")

    # Summary
    print("\n" + "=" * 80)
    print("REFACTORING COMPLETE!")
    print("=" * 80)
    print(f"\n✓ Kept {len(kept_files)} truly unique images")
    print(f"✓ Deleted {len(deleted_files)} duplicate files")
    print(f"✓ Backup saved to: {backup_dir}")
    print(f"✓ Mapping file: {mapping_file}")
    print("\nNext steps:")
    print("1. Review IMAGE_REFACTOR_MAPPING.json")
    print("2. Update HTML files to use new image paths")
    print("3. Re-run optimization script on clean image set")
    print("4. Test website to ensure all images load correctly")

if __name__ == '__main__':
    main()
