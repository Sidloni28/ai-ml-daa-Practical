import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# 1. Load Dataset

df = pd.read_csv("emails.csv")

print("First 5 rows:")
print(df.head())

# 2. Separate Features & Target

# Drop Email No. column
df = df.drop(columns=["Email No."])

# Target column
y = df["Prediction"]

# Feature columns
X = df.drop(columns=["Prediction"])

print("\nFeature Shape:", X.shape)
print("Target Shape:", y.shape)

# 3. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 4. Feature Scaling (IMPORTANT for KNN & SVM)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. KNN Model

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred_knn = knn.predict(X_test)

# 6. SVM Model

svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

y_pred_svm = svm.predict(X_test)

# 7. Evaluation Function

def evaluate_model(y_test, y_pred, model_name):
    print(f"\n===== {model_name} Performance =====")
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print(f"Accuracy  : {acc:.4f}")
    print(f"Precision : {prec:.4f}")
    print(f"Recall    : {rec:.4f}")
    print(f"F1 Score  : {f1:.4f}")
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f"{model_name} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()
    
    return acc, prec, rec, f1

# Evaluate KNN
knn_metrics = evaluate_model(y_test, y_pred_knn, "KNN")

# Evaluate SVM
svm_metrics = evaluate_model(y_test, y_pred_svm, "SVM")

# 8. Model Comparison

comparison = pd.DataFrame({
    "Model": ["KNN", "SVM"],
    "Accuracy": [knn_metrics[0], svm_metrics[0]],
    "Precision": [knn_metrics[1], svm_metrics[1]],
    "Recall": [knn_metrics[2], svm_metrics[2]],
    "F1 Score": [knn_metrics[3], svm_metrics[3]]
})

print("\n===== Model Comparison =====")
print(comparison)

comparison.set_index("Model").plot(kind='bar', figsize=(8,6))
plt.ylim(0,1)
plt.title("KNN vs SVM Performance")
plt.ylabel("Score")
plt.show()
