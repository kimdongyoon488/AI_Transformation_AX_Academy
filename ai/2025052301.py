
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import graphviz


from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



data = sns.load_dataset("titanic")

#중복/불필요한 열 제거
prep_data = data.drop(columns=["alive", "who", "adult_male", "class", "embark_town"])
prep_data.drop("deck", axis=1, inplace=True)

#결측치 제거 + 인덱스 재정렬
prep_data = prep_data.dropna().reset_index(drop=True)


# sex 열: (male=0, female=1)
le = LabelEncoder()
prep_data["sex"] = le.fit_transform(prep_data["sex"])

# embarked 열: OneHotEncoding
embarked_df = prep_data[["embarked"]]
ohe = OneHotEncoder()
embarked_ohe = ohe.fit_transform(embarked_df)
embarked_df = pd.DataFrame(embarked_ohe.toarray(), columns=ohe.categories_[0])

# 기존 embarked 열 삭제하고 원핫 인코딩된 열 추가
prep_data = pd.concat([prep_data, embarked_df], axis=1)
prep_data = prep_data.drop("embarked", axis=1)



# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    prep_data.iloc[:, 1:],  # feature (pclass ~ Q)
    prep_data.iloc[:, 0],   # label (survived)
    random_state=42
)

# 데이터셋 로드 및 DataFrame으로 변환
dataset = load_breast_cancer()
X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
y = pd.Series(dataset.target, name="target")

# 학습용/테스트용 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# 결정 트리 모델 생성 및 학습 (최대 깊이 2)
model = DecisionTreeClassifier(max_depth=2)
model.fit(X_train, y_train)

# 정확도 평가
score = model.score(X_test, y_test)
print("정확도:", score)

# 피처 중요도 시각화
plt.figure(figsize=(10, 6))
plt.barh(np.arange(X_train.shape[1]), model.feature_importances_, align="center")
plt.yticks(np.arange(X_train.shape[1]), X_train.columns)
plt.xlabel("Feature Importance")
plt.ylabel("Features")
plt.title("Feature Importances")
plt.tight_layout()
plt.show()

# 트리 구조 시각화 (plot_tree 방식)
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=X.columns, class_names=["악성", "양성"], filled=True, rounded=True)
plt.show()

# 8. 트리 구조를 graphviz로 시각화 (별도 이미지 생성)
dot_data = export_graphviz(
    model, out_file=None,
    feature_names=X.columns,
    class_names=["악성", "양성"],
    filled=True, rounded=True, special_characters=True
)
graph = graphviz.Source(dot_data)
graph.render("/mnt/data/decision_tree_visualization", format="png")