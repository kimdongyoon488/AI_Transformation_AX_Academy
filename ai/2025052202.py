# 라이브러리 불러오기
from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from seaborn import lmplot
import matplotlib.pyplot as plt

dataset = load_breast_cancer()
train = pd.DataFrame(dataset.data, columns=dataset.feature_names)
target = pd.DataFrame(dataset.target, columns=["cancer"])
data = pd.concat([train, target], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    data[["mean radius"]], data[["cancer"]], random_state=42
)

# 모델 학습
model = LogisticRegression(solver="liblinear")
model.fit(X_train, y_train)

#예측 및  평가
pred = model.predict(X_test)
print("mean radius 기반 예측 정확도:", accuracy_score(y_test, pred))

# 로지스틱 회귀 시각화
lmplot(x="mean radius", y="cancer", data=data, logistic=True)
plt.show()

# 전체 데이터로 재학습 밎 재평가
X_train, X_test, y_train, y_test = train_test_split(
    data.loc[:, "mean radius"], data.loc[:, "cancer"], random_state=42
)
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print(f"전체 데이터로 예측한 결과: {score}")