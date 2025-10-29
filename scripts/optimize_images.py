#!/usr/bin/env python3
"""
Image Optimization Script for Water Ways Sheet Metal
Pattern-CONTEXT-002

Batch processes all images into 3 optimized versions:
- hero: 1920px width, 85% quality (for page headers)
- featured: 1200px width, 80% quality (for showcases)
- thumbnail: 600px width, 75% quality (for grids/galleries)

Creates both WebP and JPEG versions for fallback support.
Target: <150 KB average per image (from 395 KB average)
"""

import os
import sys
from pathlib import Path
from PIL import Image
import pillow_heif

# Register HEIF opener (for iPhone images if any)
pillow_heif.register_heif_opener()

# Configuration
SIZES = {
    'hero': {'width': 1920, 'quality_webp': 85, 'quality_jpeg': 85},
    'featured': {'width': 1200, 'quality_webp': 80, 'quality_jpeg': 80},
    'thumbnail': {'width': 600, 'quality_webp': 75, 'quality_jpeg': 75}
}

# Input/Output directories
SOURCE_DIR = Path(__file__).parent.parent / 'images'
OUTPUT_DIR = Path(__file__).parent.parent / 'images-optimized'

def get_optimized_path(source_path, size_name, format_ext):
    """
    Generate optimized image path maintaining directory structure.

    Example:
    images/chimney-caps/main/p7210424.jpg
    -> images-optimized/chimney-caps/main/hero/p7210424.webp
    -> images-optimized/chimney-caps/main/hero/p7210424.jpg
    """
    rel_path = source_path.relative_to(SOURCE_DIR)
    parent = rel_path.parent
    stem = rel_path.stem

    output_subdir = OUTPUT_DIR / parent / size_name
    output_subdir.mkdir(parents=True, exist_ok=True)

    return output_subdir / f"{stem}.{format_ext}"

def optimize_image(source_path, size_name, config):
    """
    Optimize single image to target size in both WebP and JPEG formats.
    Returns: (webp_path, jpeg_path, webp_size, jpeg_size)
    """
    try:
        # Open and convert to RGB (handles RGBA, grayscale, etc.)
        img = Image.open(source_path)
        if img.mode in ('RGBA', 'LA', 'P'):
            # Create white background for transparency
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize maintaining aspect ratio
        target_width = config['width']
        aspect_ratio = img.height / img.width
        target_height = int(target_width * aspect_ratio)

        # Only resize if image is larger than target
        if img.width > target_width:
            img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

        # Save WebP version
        webp_path = get_optimized_path(source_path, size_name, 'webp')
        img.save(webp_path, 'WebP', quality=config['quality_webp'], method=6)
        webp_size = webp_path.stat().st_size

        # Save JPEG version
        jpeg_path = get_optimized_path(source_path, size_name, 'jpg')
        img.save(jpeg_path, 'JPEG', quality=config['quality_jpeg'], optimize=True, progressive=True)
        jpeg_size = jpeg_path.stat().st_size

        return (webp_path, jpeg_path, webp_size, jpeg_size)

    except Exception as e:
        print(f"  ERROR processing {source_path.name}: {e}")
        return None

def format_size(bytes):
    """Format bytes as human-readable size"""
    for unit in ['B', 'KB', 'MB']:
        if bytes < 1024:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024
    return f"{bytes:.1f} GB"

def main():
    print("=" * 80)
    print("Water Ways Sheet Metal - Image Optimization")
    print("Pattern-CONTEXT-002")
    print("=" * 80)
    print()

    # Find all source images
    image_extensions = {'.jpg', '.jpeg', '.png', '.heic'}
    source_images = [
        p for p in SOURCE_DIR.rglob('*')
        if p.is_file() and p.suffix.lower() in image_extensions
    ]

    print(f"Found {len(source_images)} images to optimize")
    print(f"Source directory: {SOURCE_DIR}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Statistics
    total_source_size = 0
    total_optimized_size = 0
    success_count = 0
    error_count = 0

    # Process each image
    for i, source_path in enumerate(source_images, 1):
        source_size = source_path.stat().st_size
        total_source_size += source_size

        rel_path = source_path.relative_to(SOURCE_DIR)
        print(f"[{i}/{len(source_images)}] {rel_path}")
        print(f"  Source: {format_size(source_size)}")

        # Process all 3 sizes
        image_optimized_size = 0
        for size_name, config in SIZES.items():
            result = optimize_image(source_path, size_name, config)
            if result:
                webp_path, jpeg_path, webp_size, jpeg_size = result
                image_optimized_size += webp_size + jpeg_size
                print(f"  OK {size_name}: WebP {format_size(webp_size)}, JPEG {format_size(jpeg_size)}")
            else:
                error_count += 1

        if image_optimized_size > 0:
            total_optimized_size += image_optimized_size
            success_count += 1
            savings = ((source_size - (image_optimized_size / 6)) / source_size) * 100
            print(f"  Stats: Avg per version: {format_size(image_optimized_size / 6)} (saved {savings:.1f}%)")

        print()

    # Final statistics
    print("=" * 80)
    print("OPTIMIZATION COMPLETE")
    print("=" * 80)
    print(f"Images processed: {success_count}/{len(source_images)}")
    print(f"Errors: {error_count}")
    print()
    print(f"Total source size: {format_size(total_source_size)}")
    print(f"Total optimized size: {format_size(total_optimized_size)}")
    print(f"Average source size: {format_size(total_source_size / len(source_images))}")
    print(f"Average optimized size per version: {format_size(total_optimized_size / (success_count * 6))}")
    print()

    total_savings = total_source_size * success_count - total_optimized_size
    savings_percent = (total_savings / (total_source_size * success_count)) * 100
    print(f"Total savings: {format_size(total_savings)} ({savings_percent:.1f}%)")
    print()

    # Calculate files created
    files_created = success_count * 6  # 3 sizes × 2 formats
    print(f"Files created: {files_created} ({success_count} images × 3 sizes × 2 formats)")
    print()

    return 0 if error_count == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
