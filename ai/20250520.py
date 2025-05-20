from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


data = load_iris()

features= pd.DataFrame(data=data.data, columns=data.feature_names)
#print(features)

target = pd.DataFrame(data.target, columns=["species"])

#features 와 target을 병합
iris = pd.concat([features, target], axis=1)



#열 이름 수정
iris.rename({
    "sepal length (cm)": "sepal_length",
    "sepal width (cm)": "sepal_width",
    "petal length (cm)": "petal_length",
    "petal width (cm)": "petal_width"
}, axis=1, inplace=True)


#target 값 수정
iris["species"] = \
    iris.species.map(lambda x: data.target_names[x])

#iris.info()


# 결측값 분석(상관 관계)
#print(iris.drop("species", axis=1).corr())


# 집계 분석
#print(iris.groupby("species").size())


#(sepal/petal의 길이·너비) 데이터들을 boxplot을 사용하여 시각화
# def boxplot_iris(feature_names, dataset):
#     i = 1
#     plt.figure(figsize=(11,9))
#     for col in feature_names:
#         plt.subplot(2, 2, i)
#         plt.axis('on')
#         plt.tick_params(axis='both', left=True,
#                         top=False, right=False,
#                         bottom=True, labelleft=False,
#                         labeltop=False, labelright=False,
#                         labelbottom=False)
#         dataset[col].plot(kind='box', subplots=True,
#                           sharex=False, sharey=False)
#         plt.title(col)
#         i += 1
#     plt.show()

# boxplot_iris(iris.columns[:-1], iris)

# def histogram_iris(feature_names, dataset):
#     i = 1
#     plt.figure(figsize=(11,9))
#     for col in feature_names:
#         plt.subplot(2, 2, i)
#         plt.axis('on')
#         plt.tick_params(axis='both', left=True,
#                         top=False, right=False,
#                         bottom=True, labelleft=False,
#                         labeltop=False, labelright=False,
#                         labelbottom=False)
#         dataset[col].hist()
#         plt.title(col)
#         i += 1
#     plt.show()

# histogram_iris(iris.columns[:-1], iris)




# ========== 머신러닝 모델 ==============

X_train, X_test, y_train, y_test = \
    train_test_split(iris.iloc[:, :-1], iris.iloc[:, -1],
                     test_size=0.33, random_state=42)


model = DecisionTreeClassifier(
    criterion='gini',
    splitter='best',
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    min_weight_fraction_leaf=0.0,
    max_features=None,
    random_state=42,
    max_leaf_nodes=None,
    min_impurity_decrease=0.0,
    class_weight=None,
)


#학습
model.fit(X_train, y_train)

#성능 평가
print(model.score(X_test, y_test))




