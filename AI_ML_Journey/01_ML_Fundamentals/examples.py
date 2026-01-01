"""
Machine Learning Fundamentals - Examples
==========================================
Run these examples to understand basic ML concepts
"""

# ============================================================================
# EXAMPLE 1: Simple Linear Regression
# ============================================================================
def example_linear_regression():
    """Predict house prices based on size"""
    from sklearn.linear_model import LinearRegression
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Sample data: house size (sq ft) and price (thousands)
    sizes = np.array([750, 800, 850, 900, 950, 1000, 1100, 1200, 1300]).reshape(-1, 1)
    prices = np.array([150, 160, 170, 180, 190, 200, 220, 240, 260])
    
    # Create and train model
    model = LinearRegression()
    model.fit(sizes, prices)
    
    # Make predictions
    new_size = np.array([[1150]])
    predicted_price = model.predict(new_size)
    
    print(f"Predicted price for 1150 sq ft: ${predicted_price[0]:.2f}k")
    print(f"Model equation: Price = {model.coef_[0]:.2f} * Size + {model.intercept_:.2f}")
    
    # Visualize
    plt.scatter(sizes, prices, color='blue', label='Actual')
    plt.plot(sizes, model.predict(sizes), color='red', label='Predicted')
    plt.xlabel('House Size (sq ft)')
    plt.ylabel('Price ($1000s)')
    plt.title('House Price Prediction')
    plt.legend()
    plt.show()


# ============================================================================
# EXAMPLE 2: Classification with Logistic Regression
# ============================================================================
def example_logistic_regression():
    """Classify emails as spam or not spam"""
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, confusion_matrix
    import numpy as np
    
    # Sample data: [word_count, special_char_count, has_link]
    X = np.array([
        [50, 2, 0], [100, 5, 1], [30, 1, 0], [200, 10, 1],
        [40, 3, 0], [150, 8, 1], [60, 2, 0], [180, 9, 1],
        [35, 1, 0], [120, 6, 1], [45, 2, 0], [160, 7, 1]
    ])
    y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])  # 0=Not Spam, 1=Spam
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"\nConfusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
    
    # Test new email
    new_email = np.array([[90, 5, 1]])
    prediction = model.predict(new_email)
    probability = model.predict_proba(new_email)
    
    print(f"\nNew email prediction: {'Spam' if prediction[0] == 1 else 'Not Spam'}")
    print(f"Confidence: {probability[0][prediction[0]] * 100:.2f}%")


# ============================================================================
# EXAMPLE 3: K-Nearest Neighbors (KNN)
# ============================================================================
def example_knn():
    """Classify iris flowers by species"""
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import classification_report
    
    # Load iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train KNN model
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    
    # Evaluate
    accuracy = knn.score(X_test, y_test)
    y_pred = knn.predict(X_test)
    
    print(f"KNN Accuracy: {accuracy * 100:.2f}%")
    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))


# ============================================================================
# EXAMPLE 4: Decision Tree
# ============================================================================
def example_decision_tree():
    """Decision tree for classification"""
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    
    # Load data
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train decision tree
    tree = DecisionTreeClassifier(max_depth=3, random_state=42)
    tree.fit(X_train, y_train)
    
    # Evaluate
    y_pred = tree.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Decision Tree Accuracy: {accuracy * 100:.2f}%")
    print(f"Feature Importances:")
    for name, importance in zip(iris.feature_names, tree.feature_importances_):
        print(f"  {name}: {importance:.4f}")


# ============================================================================
# EXAMPLE 5: Random Forest (Ensemble)
# ============================================================================
def example_random_forest():
    """Random Forest - multiple decision trees"""
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    
    # Load data
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train random forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    
    # Evaluate
    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Random Forest Accuracy: {accuracy * 100:.2f}%")
    print(f"\nNumber of trees: {rf.n_estimators}")


# ============================================================================
# EXAMPLE 6: Data Preprocessing
# ============================================================================
def example_preprocessing():
    """Essential data preprocessing techniques"""
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import StandardScaler, LabelEncoder
    from sklearn.impute import SimpleImputer
    
    # Sample dataset with issues
    data = {
        'age': [25, 30, np.nan, 35, 40],
        'salary': [50000, 60000, 55000, np.nan, 70000],
        'city': ['NYC', 'LA', 'NYC', 'SF', 'LA'],
        'purchased': ['Yes', 'No', 'Yes', 'Yes', 'No']
    }
    df = pd.DataFrame(data)
    
    print("Original Data:")
    print(df)
    print("\n" + "="*50 + "\n")
    
    # 1. Handle missing values
    imputer = SimpleImputer(strategy='mean')
    df[['age', 'salary']] = imputer.fit_transform(df[['age', 'salary']])
    
    print("After handling missing values:")
    print(df)
    print("\n" + "="*50 + "\n")
    
    # 2. Encode categorical variables
    le = LabelEncoder()
    df['city_encoded'] = le.fit_transform(df['city'])
    df['purchased_encoded'] = le.fit_transform(df['purchased'])
    
    print("After encoding:")
    print(df[['city', 'city_encoded', 'purchased', 'purchased_encoded']])
    print("\n" + "="*50 + "\n")
    
    # 3. Feature scaling
    scaler = StandardScaler()
    df[['age_scaled', 'salary_scaled']] = scaler.fit_transform(df[['age', 'salary']])
    
    print("After scaling:")
    print(df[['age', 'age_scaled', 'salary', 'salary_scaled']])


# ============================================================================
# EXAMPLE 7: Model Evaluation and Cross-Validation
# ============================================================================
def example_cross_validation():
    """Understand cross-validation"""
    from sklearn.model_selection import cross_val_score, KFold
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.datasets import load_iris
    
    # Load data
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Create model
    model = DecisionTreeClassifier(random_state=42)
    
    # Perform 5-fold cross-validation
    cv_scores = cross_val_score(model, X, y, cv=5)
    
    print(f"Cross-validation scores: {cv_scores}")
    print(f"Mean accuracy: {cv_scores.mean():.4f}")
    print(f"Standard deviation: {cv_scores.std():.4f}")


# ============================================================================
# EXAMPLE 8: Feature Engineering
# ============================================================================
def example_feature_engineering():
    """Create new features from existing ones"""
    import pandas as pd
    import numpy as np
    
    # Sample data
    df = pd.DataFrame({
        'length': [10, 20, 30, 40],
        'width': [5, 10, 15, 20],
        'price': [100, 200, 300, 400]
    })
    
    print("Original features:")
    print(df)
    print("\n" + "="*50 + "\n")
    
    # Create new features
    df['area'] = df['length'] * df['width']
    df['aspect_ratio'] = df['length'] / df['width']
    df['price_per_area'] = df['price'] / df['area']
    df['log_price'] = np.log(df['price'])
    
    print("After feature engineering:")
    print(df)


# ============================================================================
# Main execution
# ============================================================================
if __name__ == "__main__":
    print("="*70)
    print("MACHINE LEARNING FUNDAMENTALS - EXAMPLES")
    print("="*70)
    
    examples = [
        ("Linear Regression", example_linear_regression),
        ("Logistic Regression", example_logistic_regression),
        ("K-Nearest Neighbors", example_knn),
        ("Decision Tree", example_decision_tree),
        ("Random Forest", example_random_forest),
        ("Data Preprocessing", example_preprocessing),
        ("Cross-Validation", example_cross_validation),
        ("Feature Engineering", example_feature_engineering)
    ]
    
    print("\nAvailable examples:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"{i}. {name}")
    
    choice = input("\nEnter example number (or 'all' to run all): ").strip()
    
    if choice.lower() == 'all':
        for name, func in examples:
            print(f"\n{'='*70}")
            print(f"Running: {name}")
            print('='*70)
            try:
                func()
            except Exception as e:
                print(f"Error: {e}")
    elif choice.isdigit() and 1 <= int(choice) <= len(examples):
        name, func = examples[int(choice) - 1]
        print(f"\n{'='*70}")
        print(f"Running: {name}")
        print('='*70)
        func()
    else:
        print("Invalid choice!")
