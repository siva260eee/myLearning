"""
Test your ML setup - Your first ML model!
==========================================
"""

# Import libraries
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("🚀 Testing your AI/ML setup...\n")

# Load data
print("📊 Loading wine dataset...")
wine = load_wine()
print(f"   Features: {wine.feature_names[:3]}... (total: {len(wine.feature_names)})")
print(f"   Classes: {wine.target_names.tolist()}")
print(f"   Samples: {len(wine.data)}\n")

# Split data
print("✂️  Splitting data (80% train, 20% test)...")
X_train, X_test, y_train, y_test = train_test_split(
    wine.data, wine.target, test_size=0.2, random_state=42
)
print(f"   Training samples: {len(X_train)}")
print(f"   Testing samples: {len(X_test)}\n")

# Train model
print("🧠 Training Random Forest model...")
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
print("   ✅ Training complete!\n")

# Make predictions
print("🎯 Making predictions...")
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"   Accuracy: {accuracy:.1%}\n")

# Feature importance
print("📈 Most important features:")
importances = model.feature_importances_
for idx in importances.argsort()[-3:][::-1]:
    print(f"   - {wine.feature_names[idx]}: {importances[idx]:.3f}")

print("\n" + "="*50)
print("🎉 SUCCESS! Your ML environment is ready!")
print("="*50)
print("\n👉 Next step: Go to AI_ML_Journey/START_HERE.md")
