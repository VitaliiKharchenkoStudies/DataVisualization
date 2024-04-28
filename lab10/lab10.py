import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA, TruncatedSVD, FactorAnalysis
from sklearn.manifold import TSNE, MDS
from sklearn.cluster import FeatureAgglomeration, KMeans
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.decomposition import KernelPCA

data = pd.read_csv("haberman.data", header=None)


def calculate_inertia_2D(method):
    transformed = method.fit_transform(data)
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(transformed)
    return kmeans.inertia_


def calculate_inertia_3D(method):
    transformed = method.fit_transform(data)
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(transformed)
    return kmeans.inertia_


# Список методів для пониження розмірності
methods_2D = [
    (PCA(n_components=2), "PCA"),
    (TruncatedSVD(n_components=2), "TruncatedSVD"),
    (FactorAnalysis(n_components=2), "Factor Analysis"),
    (TSNE(n_components=2, random_state=42), "t-SNE"),
    (MDS(n_components=2, random_state=42), "MDS"),
    (KernelPCA(n_components=2, kernel='linear'), "Kernel PCA"),
    (FeatureAgglomeration(n_clusters=2), "Feature Agglomeration")
]

methods_3D = [
    (PCA(n_components=3), "PCA"),
    (TruncatedSVD(n_components=3), "TruncatedSVD"),
    (FactorAnalysis(n_components=3), "Factor Analysis"),
    (TSNE(n_components=3, random_state=42), "t-SNE"),
    (MDS(n_components=3, random_state=42), "MDS"),
    (KernelPCA(n_components=3, kernel='linear'), "Kernel PCA"),
    (FeatureAgglomeration(n_clusters=3), "Feature Agglomeration")
]

print("Inertia for 2D:")
for method, name in methods_2D:
    inertia = calculate_inertia_2D(method)
    print(f"{name}: {inertia:.2f}")

print("Inertia for 3D:")
for method, name in methods_3D:
    inertia = calculate_inertia_3D(method)
    print(f"{name}: {inertia:.2f}")
