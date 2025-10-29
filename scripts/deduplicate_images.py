#!/usr/bin/env python3
"""
Deduplicate Images Script
Identifies truly unique images and organizes them by project/category
"""

import os
import hashlib
from pathlib import Path
from collections import defaultdict
import json

def get_file_hash(filepath):
    """Calculate MD5 hash of file"""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def find_duplicates(images_dir):
    """Find all duplicate images by comparing file hashes"""
    hash_to_files = defaultdict(list)

    # Walk through all image files
    for root, dirs, files in os.walk(images_dir):
        # Skip optimized directory
        if 'optimized' in root:
            continue
        if 'logo' in root:
            continue

        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                filepath = os.path.join(root, filename)
                try:
                    file_hash = get_file_hash(filepath)
                    file_size = os.path.getsize(filepath)
                    hash_to_files[file_hash].append({
                        'path': filepath,
                        'name': filename,
                        'size': file_size,
                        'dir': os.path.basename(os.path.dirname(filepath))
                    })
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

    return hash_to_files

def create_unique_inventory(hash_to_files):
    """Create inventory of truly unique images"""
    unique_images = []
    duplicate_groups = []

    for file_hash, files in hash_to_files.items():
        if len(files) == 1:
            # Truly unique
            unique_images.append(files[0])
        else:
            # Duplicates - pick best location and note others
            duplicate_groups.append({
                'hash': file_hash,
                'count': len(files),
                'files': files,
                'primary': files[0],  # We'll choose the best one
                'duplicates': files[1:]
            })

    return unique_images, duplicate_groups

def main():
    images_dir = Path(__file__).parent.parent / 'images'

    print("=" * 80)
    print("Water Ways Sheet Metal - Image Deduplication Analysis")
    print("=" * 80)
    print()

    # Find all duplicates
    print("Scanning for duplicate images...")
    hash_to_files = find_duplicates(images_dir)

    unique_images, duplicate_groups = create_unique_inventory(hash_to_files)

    # Print summary
    print(f"\nTotal unique image hashes: {len(hash_to_files)}")
    print(f"Truly unique images (1 copy): {len(unique_images)}")
    print(f"Duplicate image groups: {len(duplicate_groups)}")

    total_file_count = sum(len(files) for files in hash_to_files.values())
    print(f"Total image files: {total_file_count}")
    print(f"Duplicate files: {total_file_count - len(hash_to_files)}")

    # Show duplicate groups
    print("\n" + "=" * 80)
    print("DUPLICATE IMAGE GROUPS")
    print("=" * 80)

    for group in sorted(duplicate_groups, key=lambda x: x['count'], reverse=True):
        print(f"\n{group['count']} copies of {group['primary']['name']} ({group['primary']['size']:,} bytes):")
        for f in group['files']:
            rel_path = os.path.relpath(f['path'], images_dir)
            print(f"  - {rel_path}")

    # Save results to JSON
    output_file = images_dir.parent / 'IMAGE_DEDUPLICATION_ANALYSIS.json'
    results = {
        'summary': {
            'total_unique_hashes': len(hash_to_files),
            'unique_files': len(unique_images),
            'duplicate_groups': len(duplicate_groups),
            'total_files': total_file_count,
            'wasted_duplicates': total_file_count - len(hash_to_files)
        },
        'unique_images': unique_images,
        'duplicate_groups': duplicate_groups
    }

    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\n\nResults saved to: {output_file}")
    print("\nRECOMMENDATIONS:")
    print("1. Keep one copy of each duplicate in the most appropriate category directory")
    print("2. Delete all other copies to save space and reduce confusion")
    print("3. Update HTML references to use the canonical path for each image")

if __name__ == '__main__':
    main()
