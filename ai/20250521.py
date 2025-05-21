from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scikitplot as skplt

#한글 깨짐 처리
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  

#붓꽃 정보 불러오기
data = load_iris()

#전체 150개 데이터 중 train = 100개 test = 50개
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.33, random_state=42
)

#결정 트리 모델
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
print("성능: " + str(model.score(X_test, y_test)))

# 예측 실행
y_pred = model.predict(X_test)


#Confusion Matrix 시각화
#모델이 예측한 값과 실제 정답이 어떻게 일치했는지를 표로 정리
skplt.metrics.plot_confusion_matrix(y_test, y_pred, figsize=(8,6))
plt.show()

#classification_report
classReport = classification_report(y_test, y_pred)
print('Classification Report :\n', classReport)




