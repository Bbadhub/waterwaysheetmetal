#!/usr/bin/env python3
"""
Find images that might be the same but with different names
- One with original camera ID (IMG_xxxx, DCIM, P1234567, etc.)
- Another with descriptive name (ohio-french-caps, copper-roof, etc.)
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import hashlib

def get_file_hash(filepath):
    """Calculate MD5 hash of file"""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def is_camera_id_name(filename):
    """Check if filename looks like original camera ID"""
    patterns = [
        r'^IMG_\d+',           # IMG_1234
        r'^DSC_?\d+',          # DSC1234 or DSC_1234
        r'^DCIM\d+',           # DCIM100MEDIA...
        r'^P\d{7}',            # P1234567
        r'^\d{6}-r\d',         # 055217-r1-11a...
        r'^\d{7,}',            # Pure numbers 1234567
        r'^[A-Z]\d{7}',        # P7260047, P8120302
    ]

    base_name = Path(filename).stem
    for pattern in patterns:
        if re.match(pattern, base_name, re.IGNORECASE):
            return True
    return False

def is_descriptive_name(filename):
    """Check if filename is descriptive (not camera ID)"""
    base_name = Path(filename).stem.lower()

    # If it's a camera ID, it's not descriptive
    if is_camera_id_name(filename):
        return False

    # Descriptive names usually have dashes or underscores with meaningful words
    descriptive_words = [
        'copper', 'chimney', 'cap', 'flashing', 'roof', 'turret',
        'ohio', 'french', 'custom', 'minnesota', 'shroud',
        'bay', 'window', 'gutter', 'metalwork', 'architectural',
        'dormer', 'tower', 'natalie', 'ray'
    ]

    return any(word in base_name for word in descriptive_words)

def analyze_renamed_duplicates(images_dir):
    """Find potential renamed duplicates by size"""

    # Group by file size
    size_to_files = defaultdict(list)

    for root, dirs, files in os.walk(images_dir):
        if 'optimized' in root or 'logo' in root:
            continue

        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                filepath = os.path.join(root, filename)
                try:
                    file_size = os.path.getsize(filepath)
                    file_hash = get_file_hash(filepath)

                    file_info = {
                        'path': filepath,
                        'filename': filename,
                        'size': file_size,
                        'hash': file_hash,
                        'is_camera_id': is_camera_id_name(filename),
                        'is_descriptive': is_descriptive_name(filename)
                    }

                    size_to_files[file_size].append(file_info)

                except Exception as e:
                    print(f"Error: {e}")

    return size_to_files

def main():
    images_dir = Path(__file__).parent.parent / 'images'

    print("=" * 80)
    print("Finding Potentially Renamed Duplicates")
    print("Looking for: Same size + one camera ID + one descriptive name")
    print("=" * 80)
    print()

    size_to_files = analyze_renamed_duplicates(images_dir)

    # Find groups with same size that have both camera ID and descriptive names
    potential_renames = []

    for size, files in size_to_files.items():
        if len(files) < 2:
            continue

        # Check if this group has both camera ID and descriptive names
        camera_ids = [f for f in files if f['is_camera_id']]
        descriptive = [f for f in files if f['is_descriptive']]

        if camera_ids and descriptive:
            # Check if they're actually the same image (same hash)
            hashes = set(f['hash'] for f in files)

            if len(hashes) == 1:
                # Same hash - definitely renamed duplicates!
                status = "[CONFIRMED DUPLICATE]"
                potential_renames.append({
                    'size': size,
                    'files': files,
                    'confirmed': True
                })
            else:
                # Different hashes but same size - might be related images
                status = "[SAME SIZE, DIFFERENT IMAGES]"
                potential_renames.append({
                    'size': size,
                    'files': files,
                    'confirmed': False
                })

    # Sort by size (larger files first)
    potential_renames.sort(key=lambda x: x['size'], reverse=True)

    print(f"Found {len(potential_renames)} groups with potential renames\n")

    confirmed_count = sum(1 for r in potential_renames if r['confirmed'])
    print(f"Confirmed duplicates: {confirmed_count}")
    print(f"Same size, different images: {len(potential_renames) - confirmed_count}")
    print()

    print("=" * 80)
    print("CONFIRMED RENAMED DUPLICATES (Same Hash)")
    print("=" * 80)

    confirmed_duplicates = [r for r in potential_renames if r['confirmed']]

    for group in confirmed_duplicates:
        print(f"\nSize: {group['size']:,} bytes ({len(group['files'])} copies)")
        print(f"Hash: {group['files'][0]['hash'][:8]}")

        # Separate camera IDs and descriptive names
        camera_ids = [f for f in group['files'] if f['is_camera_id']]
        descriptive = [f for f in group['files'] if f['is_descriptive']]

        if camera_ids:
            print("  Camera ID names:")
            for f in camera_ids:
                rel_path = os.path.relpath(f['path'], images_dir)
                print(f"    - {rel_path}")

        if descriptive:
            print("  Descriptive names:")
            for f in descriptive:
                rel_path = os.path.relpath(f['path'], images_dir)
                print(f"    - {rel_path}")

    print("\n" + "=" * 80)
    print("SAME SIZE BUT DIFFERENT IMAGES")
    print("=" * 80)

    different_images = [r for r in potential_renames if not r['confirmed']]

    for group in different_images[:10]:  # Show first 10
        print(f"\nSize: {group['size']:,} bytes ({len(group['files'])} files, {len(set(f['hash'] for f in group['files']))} unique)")

        for f in group['files']:
            rel_path = os.path.relpath(f['path'], images_dir)
            id_type = "ID" if f['is_camera_id'] else "DESC"
            print(f"    [{id_type}] {f['hash'][:8]}  {rel_path}")

    # Summary
    total_confirmed_files = sum(len(r['files']) for r in confirmed_duplicates)
    total_unique_in_confirmed = len(confirmed_duplicates)
    wasted_files = total_confirmed_files - total_unique_in_confirmed

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Confirmed renamed duplicates: {total_unique_in_confirmed} unique images")
    print(f"Total duplicate files from renaming: {total_confirmed_files}")
    print(f"Unnecessary files: {wasted_files}")
    print(f"\nRecommendation: Keep descriptive names, delete camera ID versions")

if __name__ == '__main__':
    main()
