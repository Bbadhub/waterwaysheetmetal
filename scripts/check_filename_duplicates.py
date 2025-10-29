#!/usr/bin/env python3
"""
Check for images with same base filename but different extensions
These might be the same image in different formats
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

def get_base_name(filename):
    """Get filename without extension"""
    # Handle cases like 'image.jpg' and 'image-cropped.jpg'
    name = Path(filename).stem
    return name.lower()

def analyze_filename_duplicates(images_dir):
    """Find images with same base filename"""

    # Group by base filename
    basename_to_files = defaultdict(list)

    # Also track by hash
    hash_to_files = defaultdict(list)

    for root, dirs, files in os.walk(images_dir):
        # Skip optimized directory
        if 'optimized' in root or 'logo' in root:
            continue

        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                filepath = os.path.join(root, filename)
                try:
                    base_name = get_base_name(filename)
                    file_hash = get_file_hash(filepath)
                    file_size = os.path.getsize(filepath)

                    file_info = {
                        'path': filepath,
                        'filename': filename,
                        'size': file_size,
                        'hash': file_hash,
                        'ext': Path(filename).suffix.lower()
                    }

                    basename_to_files[base_name].append(file_info)
                    hash_to_files[file_hash].append(file_info)

                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

    return basename_to_files, hash_to_files

def main():
    images_dir = Path(__file__).parent.parent / 'images'

    print("=" * 80)
    print("Checking for Same-Name Different-Extension Duplicates")
    print("=" * 80)
    print()

    basename_to_files, hash_to_files = analyze_filename_duplicates(images_dir)

    # Find cases where same basename has multiple files
    same_name_groups = {name: files for name, files in basename_to_files.items()
                       if len(files) > 1}

    print(f"Total unique base filenames: {len(basename_to_files)}")
    print(f"Base names with multiple files: {len(same_name_groups)}")
    print()

    print("=" * 80)
    print("SAME BASENAME, MULTIPLE EXTENSIONS/LOCATIONS")
    print("=" * 80)
    print()

    # Categorize by whether they're actually the same image
    format_conversions = []
    truly_different = []

    for base_name, files in sorted(same_name_groups.items()):
        # Check if all files have same hash (just format conversions)
        unique_hashes = set(f['hash'] for f in files)

        print(f"\n{base_name} ({len(files)} files):")

        if len(unique_hashes) == 1:
            # All same hash - just format conversions
            print(f"  [OK] SAME IMAGE - format conversions/duplicates")
            format_conversions.append((base_name, files))
        else:
            # Different hashes - actually different images with same name!
            print(f"  [WARNING] DIFFERENT IMAGES with same base name!")
            truly_different.append((base_name, files))

        for f in files:
            rel_path = os.path.relpath(f['path'], images_dir)
            print(f"    {f['ext']:6} {f['size']:>10,} bytes  {f['hash'][:8]}  {rel_path}")

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"\nFormat conversions/duplicates: {len(format_conversions)} base names")
    print(f"Different images, same name: {len(truly_different)} base names")

    if truly_different:
        print("\n[WARNING] These base names refer to DIFFERENT images:")
        for base_name, files in truly_different:
            print(f"  - {base_name}: {len(files)} different images")
            for f in files:
                rel_path = os.path.relpath(f['path'], images_dir)
                print(f"      {rel_path}")

    # Calculate true unique images
    total_unique_hashes = len(hash_to_files)
    print(f"\n[OK] ACTUAL UNIQUE IMAGES (by hash): {total_unique_hashes}")

    # Save detailed results
    output = {
        'total_unique_base_names': len(basename_to_files),
        'base_names_with_multiple_files': len(same_name_groups),
        'format_conversions': len(format_conversions),
        'different_images_same_name': len(truly_different),
        'actual_unique_images': total_unique_hashes,
        'format_conversion_groups': [
            {
                'base_name': name,
                'files': files
            } for name, files in format_conversions
        ],
        'different_images_groups': [
            {
                'base_name': name,
                'files': files
            } for name, files in truly_different
        ]
    }

    output_file = images_dir.parent / 'FILENAME_DUPLICATE_ANALYSIS.json'
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\nDetailed results saved to: {output_file}")

if __name__ == '__main__':
    main()
