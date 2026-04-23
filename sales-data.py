import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# 1. Load Dataset

df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# 2. Select Relevant Numerical Features

# We select important numerical columns for clustering
X = df[['SALES', 'QUANTITYORDERED', 'PRICEEACH']]

print("\nSelected Features Shape:", X.shape)

# 3. Feature Scaling

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Elbow Method (To Find Optimal K)

inertia = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot Elbow Graph
plt.figure(figsize=(8,5))
plt.plot(K_range, inertia, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.show()

# 5. Apply K-Means (Choose Optimal K)

optimal_k = 3   # Change based on elbow graph

kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
clusters_kmeans = kmeans.fit_predict(X_scaled)

df['KMeans_Cluster'] = clusters_kmeans

print("\nK-Means Cluster Counts:")
print(df['KMeans_Cluster'].value_counts())

# 6. Visualize K-Means Clusters

plt.figure(figsize=(8,6))
sns.scatterplot(
    x=df['SALES'],
    y=df['QUANTITYORDERED'],
    hue=df['KMeans_Cluster'],
    palette='Set1'
)
plt.title("K-Means Clustering")
plt.show()

# 7. Hierarchical Clustering

linked = linkage(X_scaled, method='ward')

plt.figure(figsize=(10,6))
dendrogram(linked)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()

# Apply Agglomerative Clustering
hc = AgglomerativeClustering(n_clusters=optimal_k, linkage='ward')
clusters_hc = hc.fit_predict(X_scaled)

df['Hierarchical_Cluster'] = clusters_hc

print("\nHierarchical Cluster Counts:")
print(df['Hierarchical_Cluster'].value_counts())

# 8. Visualize Hierarchical Clusters

plt.figure(figsize=(8,6))
sns.scatterplot(
    x=df['SALES'],
    y=df['QUANTITYORDERED'],
    hue=df['Hierarchical_Cluster'],
    palette='Set2'
)
plt.title("Hierarchical Clustering")
plt.show()
