# Machine Learning Fundamentals

## Overview
Machine Learning is a subset of AI that enables systems to learn and improve from experience without being explicitly programmed.

## Core Concepts

### 1. Types of Machine Learning

#### Supervised Learning
- **Definition**: Learning from labeled data
- **Use Cases**: Classification, Regression
- **Examples**: 
  - Spam detection (classification)
  - House price prediction (regression)
  - Image recognition

#### Unsupervised Learning
- **Definition**: Finding patterns in unlabeled data
- **Use Cases**: Clustering, Dimensionality Reduction
- **Examples**:
  - Customer segmentation
  - Anomaly detection
  - Recommendation systems

#### Reinforcement Learning
- **Definition**: Learning through trial and error with rewards
- **Use Cases**: Game playing, Robotics
- **Examples**:
  - Game AI (Chess, Go)
  - Self-driving cars
  - Trading bots

### 2. Key Algorithms

#### Linear Regression
```
y = mx + b
```
- Predicts continuous values
- Finds best-fit line through data
- Simple but powerful baseline

#### Logistic Regression
- Classification algorithm
- Outputs probability (0 to 1)
- Uses sigmoid function

#### Decision Trees
- Tree-like model of decisions
- Easy to interpret
- Prone to overfitting

#### Random Forest
- Ensemble of decision trees
- Reduces overfitting
- More accurate than single tree

#### K-Nearest Neighbors (KNN)
- Classifies based on nearest neighbors
- Simple but effective
- No training phase

#### Support Vector Machines (SVM)
- Finds optimal hyperplane
- Good for high-dimensional data
- Effective in classification

### 3. Essential Concepts

#### Features and Labels
- **Features (X)**: Input variables/attributes
- **Labels (y)**: Output variable/target

#### Training, Validation, Test Sets
- **Training (70%)**: Learn patterns
- **Validation (15%)**: Tune hyperparameters
- **Test (15%)**: Final evaluation

#### Overfitting vs Underfitting
- **Overfitting**: Model too complex, memorizes training data
- **Underfitting**: Model too simple, misses patterns
- **Goal**: Find the right balance

#### Bias-Variance Tradeoff
- **High Bias**: Underfitting, too simple
- **High Variance**: Overfitting, too complex
- **Goal**: Minimize both

### 4. Evaluation Metrics

#### Classification Metrics
- **Accuracy**: Correct predictions / Total predictions
- **Precision**: True Positives / (True Positives + False Positives)
- **Recall**: True Positives / (True Positives + False Negatives)
- **F1-Score**: Harmonic mean of Precision and Recall
- **Confusion Matrix**: Visual representation of predictions

#### Regression Metrics
- **MAE (Mean Absolute Error)**: Average absolute differences
- **MSE (Mean Squared Error)**: Average squared differences
- **RMSE (Root Mean Squared Error)**: Square root of MSE
- **R² Score**: Proportion of variance explained

### 5. Data Preprocessing

#### Data Cleaning
- Handle missing values
- Remove duplicates
- Fix inconsistencies

#### Feature Scaling
- **Normalization**: Scale to [0,1]
- **Standardization**: Mean=0, StdDev=1

#### Feature Engineering
- Create new features
- Combine existing features
- Domain knowledge application

#### Encoding Categorical Variables
- **One-Hot Encoding**: Binary columns for each category
- **Label Encoding**: Numeric labels for categories

## Libraries You'll Use

### NumPy
- Numerical computing
- Array operations
- Mathematical functions

### Pandas
- Data manipulation
- DataFrame operations
- CSV/Excel handling

### Scikit-learn
- ML algorithms
- Model evaluation
- Data preprocessing

### Matplotlib & Seaborn
- Data visualization
- Plotting graphs
- Statistical plots

## Next Steps

1. Install required libraries
2. Work through examples.py
3. Complete exercises
4. Build your first ML model
5. Move to Deep Learning

## Resources

- Scikit-learn Documentation
- Kaggle Datasets
- UCI Machine Learning Repository
- Google Colab for GPU computing
