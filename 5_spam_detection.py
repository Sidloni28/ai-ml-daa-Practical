import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# ---------------- LOAD DATA ----------------
df = pd.read_csv("emails.csv")

print(df.head())

# ---------------- FEATURES ----------------
# Last column is label (spam)
X = df.iloc[:, :-1]   # all columns except last
y = df.iloc[:, -1]    # last column

# ---------------- SPLIT ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# ---------------- KNN ----------------
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)

# ---------------- SVM ----------------
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)

# ---------------- RESULTS ----------------
print("\nKNN Accuracy:", accuracy_score(y_test, knn_pred))
print("SVM Accuracy:", accuracy_score(y_test, svm_pred))

print("\nSVM Classification Report:\n")
print(classification_report(y_test, svm_pred))