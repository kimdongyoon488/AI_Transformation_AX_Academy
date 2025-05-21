from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

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

#타이타닉 정보 불러오기
data2 = sns.load_dataset("titanic")
print(data2)

# features= pd.DataFrame(data=data.data, columns=data.feature_names)
# #print(features)

# target = pd.DataFrame(data.target, columns=["species"])

# #features 와 target을 병합
# iris = pd.concat([features, target], axis=1)



# #열 이름 수정
# iris.rename({
#     "sepal length (cm)": "sepal_length",
#     "sepal width (cm)": "sepal_width",
#     "petal length (cm)": "petal_length",
#     "petal width (cm)": "petal_width"
# }, axis=1, inplace=True)


# #target 값 수정
# iris["species"] = \
#     iris.species.map(lambda x: data.target_names[x])

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


# X_train, X_test, y_train, y_test = \
#     train_test_split(iris.iloc[:, :-1], iris.iloc[:, -1],
#                      test_size=0.33, random_state=42)

#학습 데이터 줄여서 틀릴 확률 높이기
#이유 : 모델이 틀릴 확률을 높여서 헷갈리는 부분이 어딘지 파악하기 위해
# X_train, X_test, y_train, y_test = \
#      train_test_split(iris.iloc[:, :-1], iris.iloc[:, -1],
#                       test_size=0.67, random_state=42)

#전체 150개 데이터 중 train = 100개 test = 50개
# X_train, X_test, y_train, y_test = train_test_split(
#     data.data, data.target, test_size=0.33, random_state=42
# )

#전체 150개 데이터 중 train = 50개 test = 100개
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.67, random_state=42
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

# 예측 실패한 샘플들 추출
wrong_idx = (y_pred != y_test) 
X_wrong = X_test[wrong_idx]
y_wrong = y_test[wrong_idx]

# 틀린 샘플을 DataFrame으로 변환 (시각화용)
wrong_df = pd.DataFrame(X_wrong, columns=iris.columns[:-1])
wrong_df["species"] = y_wrong  # 실제 품종

#pairplot으로 틀린 샘플 위치 확인
sns.pairplot(wrong_df, hue="species", diag_kind="hist")
plt.suptitle("예측 실패", y=1.02)
plt.show()


#틀린 데이터가 하나 뿐이고 성능이 좋은 상황이라 모델이 어떤 데이터들을
# 헷갈려 하는지 파악하기가 힘듬 


#("모델이 어떤 위치에서, 왜 틀렸는가?"를 분석하는
#오류 원인 분석(모델 약점 파악) 과제.
 
# 과제>iris 데이터 : (sepal length, sepal width, petal length, petal width)
#              =        5.0             3.7            7.3            2.1
# -> 품종 맞추기 : 안 맞았을 경우 pair plot을 놓고 여집합 위치에서 데이터를 10개 뽑아서 테스트하고
#    실제 정확도를 체크해 본다.


print("==============")

sample = np.array([5.0, 3.7, 7.3, 2.1]).reshape(1, -1)

is_in_test = np.any(np.all(X_test == sample, axis=1))

print("sample 데이터는 X_test에 포함되어 있는지 여부:", is_in_test)

print("==============")



