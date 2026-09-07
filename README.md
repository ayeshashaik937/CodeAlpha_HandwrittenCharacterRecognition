# Handwritten Character Recognition Using CNN

## 📌 Project Overview

This project implements a Handwritten Character Recognition system using a Convolutional Neural Network (CNN).

The model is trained on the MNIST handwritten digit dataset and recognizes handwritten digits from 0 to 9.

This project was developed as part of the CodeAlpha Machine Learning Internship – Task 3: Handwritten Character Recognition.

## 🎯 Objective

The objective of this project is to develop a deep learning model that can recognize handwritten digits from images using image preprocessing and a Convolutional Neural Network.

## 💡 Problem Statement

Handwritten digit recognition is a computer vision and machine learning problem in which a system identifies the numerical digit represented by a handwritten image.

The goal is to build a CNN model that can learn patterns from handwritten digit images and accurately predict digits from 0 to 9.

## ✨ Features

- MNIST handwritten digit dataset
- Image preprocessing and normalization
- Exploratory Data Analysis
- Convolutional Neural Network (CNN)
- Model training with validation
- Test dataset evaluation
- Accuracy and loss visualization
- Confusion matrix
- Classification report
- Precision, recall and F1-score
- Individual digit prediction
- Custom handwritten image prediction
- Error analysis
- Trained model saved in Keras format

## 📊 Dataset

The project uses the MNIST handwritten digit dataset.

- Training images: 60,000
- Testing images: 10,000
- Image dimensions: 28 × 28 pixels
- Image type: Grayscale
- Number of classes: 10
- Classes: Digits 0–9

The MNIST dataset is loaded using TensorFlow/Keras.

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab
- GitHub

## 🔄 Project Workflow

MNIST Dataset → Data Exploration → Data Preprocessing → Normalization → CNN Model → Model Training → Evaluation → Prediction → Error Analysis → Model Saving

## 🧹 Data Preprocessing

The MNIST images contain grayscale pixel values ranging from 0 to 255.

The pixel values were normalized to a range between 0 and 1.

The images were also reshaped to include the grayscale channel required by the CNN.

Before preprocessing: (60000, 28, 28)

After preprocessing: (60000, 28, 28, 1)

Normalization helps the neural network train efficiently, while the additional channel dimension represents the grayscale image.

## 🧠 CNN Architecture

The CNN used in this project contains:

- Input: 28 × 28 × 1
- Conv2D: 32 filters, 3 × 3, ReLU
- MaxPooling2D: 2 × 2
- Conv2D: 64 filters, 3 × 3, ReLU
- MaxPooling2D: 2 × 2
- Flatten
- Dense: 128 neurons, ReLU
- Dropout: 0.5
- Output: 10 neurons, Softmax

Total trainable parameters: 225,034

CNN is suitable for image recognition because convolutional layers can learn important visual patterns such as edges, shapes, and digit structures.

## ⚙️ Model Training

The CNN was trained using:

- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy
- Evaluation Metric: Accuracy
- Batch Size: 128
- Epochs: 10
- Validation: Used during training

## 📈 Model Evaluation

The trained model was evaluated using the MNIST test dataset.

### Test Results

- Test Loss: 0.0218
- Test Accuracy: 99.32%
- Macro Precision: 99.32%
- Macro Recall: 99.31%
- Macro F1-Score: 99.31%
- Weighted Precision: 99.32%
- Weighted Recall: 99.32%
- Weighted F1-Score: 99.32%

These are the actual results obtained during model evaluation.

## 📊 Classification Report

| Digit | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| 0 | 99.39% | 99.69% | 99.54% |
| 1 | 99.65% | 99.56% | 99.60% |
| 2 | 99.04% | 99.71% | 99.37% |
| 3 | 98.92% | 99.60% | 99.26% |
| 4 | 99.49% | 99.69% | 99.59% |
| 5 | 98.99% | 98.77% | 98.88% |
| 6 | 99.58% | 99.06% | 99.32% |
| 7 | 99.41% | 98.74% | 99.07% |
| 8 | 99.59% | 99.28% | 99.43% |
| 9 | 99.11% | 99.01% | 99.06% |

## 🔍 Confusion Matrix

A confusion matrix was generated to analyze correct and incorrect predictions for each digit class.

It helps identify which handwritten digits are sometimes confused with one another.

## 🧪 Prediction System

The trained CNN can predict handwritten digits from input images.

The prediction system provides:

- Input image
- Predicted digit
- Prediction confidence

The model was also tested with a custom handwritten digit image.

## ❌ Error Analysis

The project includes an error analysis section that displays incorrectly classified test images with their actual and predicted labels.

Misclassifications can occur when handwritten digits have similar shapes or unusual writing styles.

## 💾 Saved Model

The trained CNN model is saved as:

handwritten_character_recognition.keras

The saved model can be loaded later without retraining.

## 🚀 How to Run

### Google Colab

1. Open the .ipynb notebook using Google Colab.
2. Run the cells in order.
3. The MNIST dataset will be downloaded automatically.
4. Perform preprocessing.
5. Build and train the CNN.
6. Evaluate the model.
7. Test handwritten digit predictions.

### Local Environment

Install the required dependencies using requirements.txt.

Then open the handwritten_character_recognition.ipynb notebook and run the cells in order.

## 📁 Project Structure

CodeAlpha_HandwrittenCharacterRecognition/
│
├── README.md
├── handwritten_character_recognition.ipynb
├── handwritten_character_recognition.keras
├── requirements.txt
├── images/
│   └── sample_results.png
└── src/
    └── prediction.py

## 🔮 Future Improvements

- Extend the project to handwritten alphabets using the EMNIST dataset.
- Improve preprocessing for real-world handwritten images.
- Build a graphical user interface.
- Develop a web-based digit recognition application.
- Experiment with different CNN architectures.
- Deploy the trained model as an online application.

## 🏁 Conclusion

This project demonstrates how Convolutional Neural Networks can be used for handwritten digit recognition.

Using the MNIST dataset, the CNN successfully learned visual patterns from handwritten digits and achieved a test accuracy of 99.32%.

The project demonstrates data preprocessing, exploratory data analysis, CNN architecture, model training, evaluation, classification metrics, confusion matrix, prediction, error analysis, and model saving.

## 👩‍💻 Internship

CodeAlpha Machine Learning Internship

Task 3: Handwritten Character Recognition

## 📚 References

- MNIST Handwritten Digit Dataset
- TensorFlow Documentation
- Keras Documentation
- Scikit-learn Documentation
- NumPy Documentation
- Matplotlib Documentation

## ⭐ Acknowledgement

This project was developed as part of the CodeAlpha Machine Learning Internship to gain practical experience in deep learning, computer vision, and image classification.
