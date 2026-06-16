#!/usr/bin/env python3
"""
Optimized Image Downloader - Dogs vs Cats
=========================================
Downloads compressed images directly to D: drive
No Kaggle API needed - uses public sources
Reduces storage by downloading thumbnails
"""

import os
import requests
from pathlib import Path

def create_dataset_folder():
    """Create dataset folder structure"""
    base_dir = r"d:\dog_cats classifier\dataset"
    os.makedirs(base_dir, exist_ok=True)
    return base_dir

def download_images_optimized():
    """Download a sample of dog and cat images with compression"""
    
    base_dir = create_dataset_folder()
    
    # Sample URLs for small, compressed images
    cat_urls = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/400px-Cat03.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/2010-kodak-cat.jpg/400px-2010-kodak-cat.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Saltriokithodes.jpg/400px-Saltriokithodes.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Golde33443.jpg/400px-Golde33443.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Tabby_cat_close_up.jpg/400px-Tabby_cat_close_up.jpg",
    ]
    
    dog_urls = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/YellowLabradorLooking_new.jpg/400px-YellowLabradorLooking_new.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Labrador_on_Quantock_%282175262184%29.jpg/400px-Labrador_on_Quantock_%282175262184%29.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Collage_of_Nine_Dogs.jpg/400px-Collage_of_Nine_Dogs.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/German_Shepherd_-_DSC_4701.JPG/400px-German_Shepherd_-_DSC_4701.JPG",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Puppy_grayscale.jpg/400px-Puppy_grayscale.jpg",
    ]
    
    print("\n" + "="*60)
    print("Downloading optimized images to D: drive")
    print("="*60 + "\n")
    
    # Download cat images
    print("[1/2] Downloading cat images...")
    for idx, url in enumerate(cat_urls, 1):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                filepath = os.path.join(base_dir, f"cat.{idx:02d}.jpg")
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                size_kb = len(response.content) / 1024
                print(f"   ✅ cat.{idx:02d}.jpg ({size_kb:.1f} KB)")
        except Exception as e:
            print(f"   ⚠️  Failed to download: {url[:50]}... ({e})")
    
    # Download dog images
    print("\n[2/2] Downloading dog images...")
    for idx, url in enumerate(dog_urls, 1):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                filepath = os.path.join(base_dir, f"dog.{idx:02d}.jpg")
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                size_kb = len(response.content) / 1024
                print(f"   ✅ dog.{idx:02d}.jpg ({size_kb:.1f} KB)")
        except Exception as e:
            print(f"   ⚠️  Failed to download: {url[:50]}... ({e})")
    
    # Summary
    image_count = len([f for f in os.listdir(base_dir) if f.endswith('.jpg')])
    total_size = sum(os.path.getsize(os.path.join(base_dir, f)) for f in os.listdir(base_dir) if f.endswith('.jpg')) / (1024*1024)
    
    print("\n" + "="*60)
    print(f"✅ Download complete!")
    print(f"📁 Images: {image_count}")
    print(f"💾 Total size: {total_size:.1f} MB")
    print(f"📂 Location: {base_dir}")
    print("="*60)
    print("\n✨ Next step: Run 'python svm_classifier.py'\n")

if __name__ == "__main__":
    try:
        download_images_optimized()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Make sure you have internet connection and D: drive has space")
