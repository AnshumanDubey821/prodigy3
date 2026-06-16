# 🧠 Prodigy InfoTech – Machine Learning Internship
## 📌 Task-03: Image Classification using Support Vector Machine (SVM)

**Objective**: Build a binary image classifier to distinguish between cats and dogs using Support Vector Machines.

---

## 📝 Task Description

This project implements an **SVM-based image classification system** that automatically identifies whether a given image contains a **cat** or a **dog**. The model is trained on labeled image datasets from Kaggle and uses machine learning techniques to provide accurate binary classifications.

---

## 🔍 Goal

Develop an accurate binary classification model using **Support Vector Machine (SVM)** that can predict whether an image contains a cat or a dog, demonstrating proper machine learning pipeline implementation including data preprocessing, model training, and performance evaluation.

---

## 🛠️ Technologies & Libraries

- **Python 3.10+** – Primary programming language
- **NumPy** – Numerical computing and array operations
- **OpenCV (cv2)** – Image processing and grayscale conversion
- **Scikit-learn** – SVM classifier and evaluation metrics
- **Matplotlib** – Data visualization and output plotting

---

## 📂 Project Structure

```
PRODIGY_ML_03/
├── svm_classifier.py              # Main SVM classifier script
├── svm_classifier.ipynb           # Interactive Jupyter notebook
├── dataset/                       # Training dataset folder
│   ├── cat.*.jpg                  # Cat images (label: 0)
│   └── dog.*.jpg                  # Dog images (label: 1)
├── output/                        # Model outputs & visualizations
│   └── svm_visualization.png      # Prediction results visualization
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## 📊 Dataset Details

- **Source**: [Kaggle - Dogs vs Cats Competition Dataset](https://www.kaggle.com/c/dogs-vs-cats/data)
- **Image Format**: JPG images processed in grayscale
- **Naming Convention**: Filenames must contain 'cat' or 'dog' (case-insensitive)
- **Image Dimensions**: Automatically resized to 64×64 pixels
- **Label Encoding**: 
  - **0** = Cat
  - **1** = Dog
- **Recommended Size**: 100+ images per class for optimal performance

---

## 🔄 Implementation Workflow

1. **Image Loading & Grayscaling** – Read all images from dataset folder in grayscale format
2. **Image Resizing** – Resize all images to 64×64 pixels for uniform dimensions
3. **Feature Extraction** – Flatten 2D image arrays into 1D feature vectors (4096 features)
4. **Data Labeling** – Assign binary labels based on filename (0=Cat, 1=Dog)
5. **Data Splitting** – Divide dataset into 80% training and 20% testing sets
6. **SVM Model Training** – Train linear kernel SVM classifier on training data
7. **Model Evaluation** – Calculate accuracy and generate classification report
8. **Visualization** – Create visualization showing predictions on test samples

---

## 📸 Output & Visualization

The model generates a detailed visualization showing:
- **10 random test samples** from the test dataset
- **True class labels** from ground truth data
- **Model predictions** for each sample
- **Grayscale image representation** of each sample

**Output Location**: `output/svm_visualization.png`

---

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Navigate to project directory**
   ```bash
   cd PRODIGY_ML_03
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the dataset**
   ```bash
   mkdir dataset
   # Place cat images (filename should contain 'cat') in dataset/
   # Place dog images (filename should contain 'dog') in dataset/
   ```

4. **Run the SVM classifier**
   ```bash
   python svm_classifier.py
   ```

### Expected Output
- Console displays:
  - Number of images loaded and their distribution
  - Training and testing sample counts
  - Overall accuracy percentage
  - Detailed classification report (precision, recall, F1-score)
  
- File output:
  - `output/svm_visualization.png` – Visualization of predictions
  - Plot displayed showing 10 sample predictions with true vs predicted labels

---

## 📈 Key Features

✅ **Automatic Image Preprocessing** – Handles grayscale conversion and resizing  
✅ **Binary Classification with SVM** – Uses linear kernel for fast classification  
✅ **Train/Test Split** – 80/20 split for proper model validation  
✅ **Detailed Performance Metrics** – Accuracy, precision, recall, and F1-score  
✅ **Visual Output** – Prediction visualization with confidence indicators  
✅ **Scalable Pipeline** – Easily handles variable image sizes and datasets  

---

## 📚 Learning Outcomes

This implementation demonstrates proficiency in:
- ✅ Image preprocessing and feature extraction
- ✅ Binary classification using Support Vector Machines
- ✅ Train/test data splitting for model validation
- ✅ Performance metrics evaluation
- ✅ Data visualization with Matplotlib
- ✅ Python machine learning pipeline development

---

## 📖 References

- **Kaggle Dataset**: https://www.kaggle.com/c/dogs-vs-cats/data
- **Scikit-learn SVM**: https://scikit-learn.org/stable/modules/svm.html
- **OpenCV Documentation**: https://opencv.org/

---

## 👨‍💻 Author

**Shashank Gupta**  
Task-03: Support Vector Machine Image Classifier

---

## 📄 License

This project is part of the Prodigy InfoTech Machine Learning Internship program and is provided for educational purposes.
