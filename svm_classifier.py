#!/usr/bin/env python3
"""
PRODIGY INFOTECH - Machine Learning Internship
Task-03: Image Classification using Support Vector Machine (SVM)
================================================================

Objective: Build a binary classifier to distinguish between cats and dogs 
using Support Vector Machines.

Dataset: Kaggle - Dogs vs Cats Competition
Source: https://www.kaggle.com/c/dogs-vs-cats/data

Author: Shashank Gupta
Date: 2026
"""

import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import random

# Configuration
CONFIG = {
    'dataset_dir': 'dataset/',
    'output_dir': 'output/',
    'target_image_size': 64,
    'test_split': 0.2,
    'random_state': 42,
    'svm_kernel': 'linear'
}

def load_and_preprocess_images(directory, target_size):
    """
    Load images from directory and preprocess for classification.
    
    Args:
        directory: Path to folder containing images
        target_size: Target image dimension (square)
    
    Returns:
        Tuple of (feature_vectors, labels, filenames)
    """
    feature_vectors = []
    labels = []
    filenames = []
    
    print("[LOADING] Reading images from dataset folder...")
    
    try:
        image_files = os.listdir(directory)
        if not image_files:
            raise FileNotFoundError(f"No images found in {directory}")
        
        for idx, img_name in enumerate(image_files, 1):
            img_path = os.path.join(directory, img_name)
            
            # Read image in grayscale
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                print(f"   [SKIPPED] Invalid image: {img_name}")
                continue
            
            # Resize to target dimensions
            img_resized = cv2.resize(img, (target_size, target_size))
            
            # Flatten to 1D vector
            feature_vector = img_resized.flatten()
            feature_vectors.append(feature_vector)
            filenames.append(img_name)
            
            # Label assignment based on filename
            if 'cat' in img_name.lower():
                labels.append(0)  # Class 0: Cat
            elif 'dog' in img_name.lower():
                labels.append(1)  # Class 1: Dog
            else:
                print(f"   [WARNING] Unclear label: {img_name}")
    
    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
    
    return np.array(feature_vectors), np.array(labels), filenames

# ========== Load and Preprocess Dataset ==========
X, y, filenames = load_and_preprocess_images(CONFIG['dataset_dir'], CONFIG['target_image_size'])

if len(X) == 0:
    print("[ERROR] No images loaded. Exiting.")
    sys.exit(1)

print(f"[SUCCESS] Loaded {len(X)} images")
print(f"   - Feature vector shape: {X[0].shape}")
print(f"   - Class distribution: {np.bincount(y)}")

# ========== Data Splitting ==========
print("\n[SPLITTING] Dividing data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=CONFIG['test_split'], 
    random_state=CONFIG['random_state']
)
print(f"[SUCCESS] Training samples: {len(X_train)}, Testing samples: {len(X_test)}")

# ========== Train SVM Classifier ==========
print("\n[TRAINING] Training SVM classifier (this may take a moment)...")
classifier = SVC(kernel=CONFIG['svm_kernel'], C=1.0)
classifier.fit(X_train, y_train)
print("[SUCCESS] Model training completed!")

# ========== Model Evaluation ==========
print("\n[EVALUATING] Generating predictions on test set...")
y_predictions = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_predictions)

print("\n" + "="*60)
print("[RESULTS] CLASSIFICATION METRICS")
print("="*60)
print(f"Overall Accuracy: {accuracy:.2%}\n")
print("Detailed Metrics:")
print("-" * 60)
print(classification_report(y_test, y_predictions, target_names=['Cat', 'Dog']))
print("="*60)

# ========== Visualization & Output ==========
print("\n[VISUALIZING] Generating prediction visualization...")

# Create output directory if it doesn't exist
os.makedirs(CONFIG['output_dir'], exist_ok=True)

# Generate sample predictions visualization
fig = plt.figure(figsize=(15, 8))
fig.suptitle('SVM Classifier: Prediction Results (Cat vs Dog)', fontsize=16, fontweight='bold', y=0.98)

num_samples = min(10, len(X_test))

for i in range(num_samples):
    # Select random test sample
    sample_idx = random.randint(0, len(X_test) - 1)
    sample_image = X_test[sample_idx].reshape(CONFIG['target_image_size'], CONFIG['target_image_size'])
    true_class = y_test[sample_idx]
    pred_class = y_predictions[sample_idx]
    
    # Class labels
    class_names = ['Cat', 'Dog']
    true_label = class_names[true_class]
    pred_label = class_names[pred_class]
    
    # Determine correctness
    is_correct = (true_class == pred_class)
    border_color = 'green' if is_correct else 'red'
    result_marker = '✓' if is_correct else '✗'
    
    # Plot
    ax = plt.subplot(2, 5, i + 1)
    ax.imshow(sample_image, cmap='gray')
    
    title = f"{result_marker} True: {true_label}\nPred: {pred_label}"
    ax.set_title(title, fontsize=10, fontweight='bold', color=border_color)
    ax.axis('off')
    
    # Add border
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color(border_color)
        spine.set_linewidth(3)

plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save visualization
output_path = os.path.join(CONFIG['output_dir'], 'svm_visualization.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight')
print(f"[SUCCESS] Visualization saved to: {output_path}")

# Display plot
plt.show()

print("\n[COMPLETE] Classification finished! All outputs generated successfully.")

