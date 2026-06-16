#!/usr/bin/env python3
"""
Synthetic Dataset Generator
============================
Creates augmented variations of existing images
Increases dataset size without downloading
Low storage - only ~50MB total
"""

import cv2
import numpy as np
import os
from pathlib import Path

def augment_images():
    """Create variations of existing images through augmentation"""
    
    dataset_dir = r"d:\dog_cats classifier\dataset"
    images_dir = Path(dataset_dir)
    
    print("\n" + "="*60)
    print("Creating augmented dataset variations...")
    print("="*60 + "\n")
    
    # Get existing images
    existing_images = sorted([f for f in os.listdir(dataset_dir) if f.endswith('.jpg')])
    print(f"Found {len(existing_images)} original images")
    
    variations_count = 0
    
    for img_file in existing_images:
        img_path = os.path.join(dataset_dir, img_file)
        img = cv2.imread(img_path)
        
        if img is None:
            continue
        
        # Extract label and number
        label = "cat" if "cat" in img_file.lower() else "dog"
        base_name = img_file.split('.')[0]
        
        # Create variations
        augmentations = {
            "original": img,
            "flipped": cv2.flip(img, 1),  # Horizontal flip
            "rotated_15": rotate_image(img, 15),  # Rotate 15 degrees
            "rotated_minus_15": rotate_image(img, -15),
            "brightness_up": adjust_brightness(img, 1.3),
            "brightness_down": adjust_brightness(img, 0.7),
            "blur": cv2.GaussianBlur(img, (5, 5), 0),
            "noise": add_noise(img),
        }
        
        for aug_name, aug_img in augmentations.items():
            if aug_name != "original":  # Skip original, keep source
                new_name = f"{label}.aug_{base_name}_{aug_name}.jpg"
                output_path = os.path.join(dataset_dir, new_name)
                
                cv2.imwrite(output_path, aug_img)
                variations_count += 1
                print(f"   ✅ Created: {new_name}")
    
    # Summary
    final_count = len([f for f in os.listdir(dataset_dir) if f.endswith('.jpg')])
    total_size = sum(os.path.getsize(os.path.join(dataset_dir, f)) 
                     for f in os.listdir(dataset_dir) if f.endswith('.jpg')) / (1024*1024)
    
    print("\n" + "="*60)
    print(f"✅ Augmentation complete!")
    print(f"📊 Original images: {len(existing_images)}")
    print(f"📊 Variations created: {variations_count}")
    print(f"📊 Total images: {final_count}")
    print(f"💾 Total dataset size: {total_size:.1f} MB")
    print("="*60)
    print("\n✨ Next step: Run 'python svm_classifier.py'\n")

def rotate_image(img, angle):
    """Rotate image by specified angle"""
    h, w = img.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, matrix, (w, h))
    return rotated

def adjust_brightness(img, factor):
    """Adjust image brightness"""
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
    img_hsv[:, :, 2] = np.clip(img_hsv[:, :, 2] * factor, 0, 255)
    return cv2.cvtColor(img_hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

def add_noise(img, noise_factor=0.1):
    """Add small random noise to image"""
    noisy = img.astype(np.float32)
    noise = np.random.normal(0, noise_factor * 255, noisy.shape)
    noisy = np.clip(noisy + noise, 0, 255)
    return noisy.astype(np.uint8)

if __name__ == "__main__":
    try:
        augment_images()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
