#!/usr/bin/env python3
"""
Kaggle Dataset Downloader - Dogs vs Cats
========================================
Downloads and extracts images to D: drive with minimal storage usage.

Setup Required:
1. Go to https://www.kaggle.com/settings/account
2. Click "Create New API Token" - this downloads kaggle.json
3. Place kaggle.json in your user home .kaggle folder
4. Run this script
"""

import os
import json
from pathlib import Path

def setup_kaggle_api():
    """Check if Kaggle API is configured"""
    kaggle_config = Path.home() / '.kaggle' / 'kaggle.json'
    
    if not kaggle_config.exists():
        print("\n⚠️  Kaggle API NOT configured yet!")
        print("\n📋 Setup Instructions:")
        print("=" * 60)
        print("1. Go to: https://www.kaggle.com/settings/account")
        print("2. Scroll down and click 'Create New API Token'")
        print("3. This downloads 'kaggle.json'")
        print("4. Move kaggle.json to your home .kaggle folder")
        print("5. Run this script again")
        print("=" * 60)
        return False
    
    print("✅ Kaggle API configured!")
    return True

def download_dataset():
    """Download Dogs vs Cats dataset"""
    if not setup_kaggle_api():
        return
    
    try:
        import kaggle
        
        dataset_name = 'dogs-vs-cats/data'
        output_dir = r'd:\dog_cats classifier\dataset'
        
        # Create dataset folder
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"\n📥 Downloading Dogs vs Cats dataset...")
        print(f"📂 Destination: {output_dir}")
        print("⏳ This may take several minutes (700MB+ dataset)...\n")
        
        # Download dataset
        kaggle.api.dataset_download_files(
            dataset_name, 
            path=output_dir, 
            unzip=True
        )
        
        print("\n✅ Download complete!")
        print(f"📁 Images saved to: {output_dir}")
        
    except Exception as e:
        print("\n❌ Download failed: {e}")
        print("\n💡 Troubleshooting:")
        print("   - Verify kaggle.json is in your home .kaggle folder")
        print("   - Check internet connection")
        print("   - Make sure D: drive has enough space (800MB+)")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🐱🐶 Kaggle Dogs vs Cats Dataset Downloader")
    print("="*60)
    download_dataset()
    print("\n" + "="*60)
