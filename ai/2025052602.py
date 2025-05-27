import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


iris = load_iris()
iris_data = iris.data
iris_data_pd = pd.DataFrame(iris_data, columns=iris.feature_names)


km = KMeans(n_clusters=2, random_state=20)
km.fit(iris_data_pd.iloc[:, 2:4])  # 꽃잎 길이, 너비만 사용
y_pred = km.predict(iris_data_pd.iloc[:, 2:4])

# y_pred = km.predict(iris_data_pd.iloc[:, 2:4])

# iris_data_pd.iloc[98, 2:4]

# km.cluster_centers_


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx**2 + dy**2)


n_cluster_list = [3, 4, 6, 12]

for i in n_cluster_list:
    km = KMeans(n_clusters=i, random_state=20)
    km.fit(iris_data_pd.iloc[:, 2:4])
    y_pred = km.predict(iris_data_pd.iloc[:, 2:4])
    
    plt.figure()
    plt.scatter(iris_data_pd.iloc[:, 2], iris_data_pd.iloc[:, 3], c=y_pred)
    plt.title(f"Clustering = {i}")
    plt.xlabel("petal length")
    plt.ylabel("petal width")
    plt.show()