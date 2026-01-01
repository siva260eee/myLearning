# Machine Learning Fundamentals - Exercises

## Exercise 1: Linear Regression ⭐
**Goal**: Build a salary prediction model

Create a linear regression model that predicts salary based on years of experience.

**Data**:
```python
years = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
salaries = [40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000]
```

**Tasks**:
1. Split into train/test sets (80/20)
2. Train a Linear Regression model
3. Calculate R² score
4. Predict salary for 12 years of experience
5. Visualize the results

---

## Exercise 2: Classification ⭐⭐
**Goal**: Build a customer churn predictor

Predict whether a customer will leave based on their behavior.

**Data**:
```python
# Features: [age, monthly_spend, support_calls, tenure_months]
customers = [
    [25, 50, 5, 2], [35, 100, 2, 12], [45, 80, 3, 24],
    [28, 40, 8, 1], [52, 120, 1, 36], [30, 60, 4, 6],
    [40, 90, 2, 18], [33, 45, 6, 3], [48, 110, 1, 30],
    [27, 35, 9, 1]
]
churned = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]  # 1=Churned, 0=Stayed
```

**Tasks**:
1. Use Logistic Regression
2. Calculate accuracy, precision, and recall
3. Create a confusion matrix
4. Predict for a new customer: [31, 55, 5, 4]

---

## Exercise 3: Multi-Class Classification ⭐⭐
**Goal**: Classify handwritten digits

Use the digits dataset from sklearn.

**Tasks**:
1. Load `sklearn.datasets.load_digits()`
2. Try 3 different algorithms:
   - KNN
   - Decision Tree
   - Random Forest
3. Compare their accuracies
4. Use cross-validation (5-fold)
5. Which model performs best?

---

## Exercise 4: Data Preprocessing ⭐⭐
**Goal**: Clean and prepare messy data

**Data**:
```python
data = {
    'age': [25, np.nan, 35, 40, 28, np.nan, 45],
    'income': [50000, 60000, np.nan, 80000, 55000, 70000, np.nan],
    'education': ['BS', 'MS', 'HS', 'PhD', 'BS', 'MS', 'HS'],
    'purchased': [1, 1, 0, 1, 0, 1, 0]
}
```

**Tasks**:
1. Handle missing values (use mean imputation)
2. Encode 'education' (one-hot encoding)
3. Scale 'age' and 'income' (standardization)
4. Split into X and y
5. Train a model and evaluate

---

## Exercise 5: Feature Engineering ⭐⭐⭐
**Goal**: Create better features

You're predicting house prices with:
```python
data = {
    'length': [50, 60, 70, 80, 90],
    'width': [30, 35, 40, 45, 50],
    'bedrooms': [2, 3, 3, 4, 4],
    'age_years': [10, 5, 15, 2, 20],
    'price': [200000, 280000, 300000, 420000, 350000]
}
```

**Tasks**:
1. Create engineered features:
   - Total area (length × width)
   - Price per square foot
   - Age category (new: <5, medium: 5-15, old: >15)
   - Room density (bedrooms / area)
2. Train model with original features
3. Train model with engineered features
4. Compare R² scores
5. Which features are most important?

---

## Exercise 6: Model Comparison ⭐⭐⭐
**Goal**: Find the best model

Use the Iris dataset and compare:
- Logistic Regression
- KNN (try k=3, 5, 7)
- Decision Tree
- Random Forest
- SVM

**Tasks**:
1. Use same train/test split for all
2. Calculate accuracy for each
3. Use cross-validation
4. Create a comparison table
5. Recommend the best model

---

## Exercise 7: Overfitting Detection ⭐⭐⭐
**Goal**: Understand overfitting

Create a polynomial regression model with different degrees.

**Tasks**:
1. Generate noisy data: y = 2x + noise
2. Try polynomial degrees: 1, 3, 5, 10, 15
3. Calculate train and test errors
4. Plot learning curves
5. Identify where overfitting starts
6. What's the optimal degree?

---

## Exercise 8: Real Dataset Challenge ⭐⭐⭐⭐
**Goal**: Complete ML pipeline

Download the Titanic dataset from Kaggle or sklearn.

**Tasks**:
1. Exploratory Data Analysis (EDA)
   - Check for missing values
   - Visualize distributions
   - Find correlations
2. Data Preprocessing
   - Handle missing values
   - Encode categorical variables
   - Feature scaling
3. Feature Engineering
   - Create family_size
   - Extract titles from names
   - Create age_group
4. Model Building
   - Try multiple algorithms
   - Use cross-validation
   - Tune hyperparameters
5. Evaluation
   - Confusion matrix
   - ROC curve
   - Feature importance
6. Final prediction accuracy > 75%

---

## Exercise 9: Custom ML Pipeline ⭐⭐⭐⭐
**Goal**: Build a reusable ML pipeline

Create a class that handles the entire ML workflow.

**Requirements**:
```python
class MLPipeline:
    def __init__(self, model_type):
        # Initialize with model choice
        pass
    
    def load_data(self, X, y):
        # Load and validate data
        pass
    
    def preprocess(self):
        # Handle missing values, encoding, scaling
        pass
    
    def split_data(self, test_size=0.2):
        # Train/test split
        pass
    
    def train(self):
        # Train the model
        pass
    
    def evaluate(self):
        # Return metrics
        pass
    
    def predict(self, X_new):
        # Make predictions
        pass
```

**Tasks**:
1. Implement all methods
2. Support multiple models (LR, KNN, RF)
3. Test with iris dataset
4. Add cross-validation option
5. Save/load trained models

---

## Exercise 10: Ensemble Learning ⭐⭐⭐⭐⭐
**Goal**: Build a custom ensemble

Create an ensemble that combines:
- Logistic Regression
- Random Forest
- SVM

**Tasks**:
1. Train all three models
2. Use voting classifier
3. Try both hard and soft voting
4. Compare with individual models
5. Implement custom weighted ensemble
6. Which approach works best?

---

## Solutions

Create your solutions in `my_solutions.py`. Use this template:

```python
"""
ML Fundamentals - My Solutions
================================
"""

# Exercise 1: Linear Regression
def exercise_1():
    # Your code here
    pass

# Exercise 2: Classification
def exercise_2():
    # Your code here
    pass

# ... continue for all exercises
```

---

## Bonus Challenges 🚀

### Challenge 1: Feature Selection
Research and implement 3 feature selection techniques:
- Correlation-based
- Recursive Feature Elimination
- Feature importance from tree models

### Challenge 2: Hyperparameter Tuning
Use GridSearchCV to find optimal hyperparameters for:
- Random Forest (n_estimators, max_depth)
- SVM (C, kernel, gamma)

### Challenge 3: Imbalanced Data
Create a dataset with 90% class 0 and 10% class 1.
Handle it using:
- SMOTE
- Class weights
- Different evaluation metrics

---

## Tips for Success 💡

1. **Start Simple**: Begin with basic models before complex ones
2. **Visualize**: Always plot your data and results
3. **Validate**: Use cross-validation to avoid overfitting
4. **Document**: Comment your code and reasoning
5. **Experiment**: Try different approaches and parameters
6. **Compare**: Always have a baseline to compare against

## Next Steps

After completing these exercises:
1. Move to `02_Deep_Learning`
2. Work on Kaggle competitions
3. Build a project from scratch
4. Document your learning journey
