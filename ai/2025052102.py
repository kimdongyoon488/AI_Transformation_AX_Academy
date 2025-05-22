from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 데이터 불러오기
data = load_wine()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, random_state=42
)

# 모델 생성 및 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 모델 예측 및 평가
score = model.score(X_test, y_test)
print("정확도: ", score)


#계수/절편
coefficient = model.coef_
intercept = model.intercept_

print("계수 :\n", coefficient); print()
print("절편 :\n", intercept)


