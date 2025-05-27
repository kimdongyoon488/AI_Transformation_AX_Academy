from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


iris = load_iris()
iris_data = iris.data
iris_data_pd = pd.DataFrame(iris_data, columns=iris.feature_names)

from sklearn.cluster import AgglomerativeClustering

linkage = ["complete", "average", "ward"]
for idx, i in enumerate(linkage):
    plt.figure()
    hier = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage=i)
    hier.fit(iris_data_pd.iloc[:,2:4])
    plt.scatter(iris_data_pd.iloc[:,2], iris_data_pd.iloc[:,3], c=hier.labels_)

    plt.title("Clustering: " + i)
    plt.xlabel("petal length")
    plt.ylabel("petal width")
    plt.show()

from scipy.cluster import hierarchy

hierar = hierarchy.linkage(iris_data_pd.iloc[:,2:4], 'complete')
plt.figure(figsize=(20,20))
dn = hierarchy.dendrogram(hierar)
plt.show()

hierar = hierarchy.linkage(iris_data_pd.iloc[:,2:4], 'single')
plt.figure(figsize=(20,20))
dn = hierarchy.dendrogram(hierar)
plt.show()