from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# 붓꽃 데이터셋 로드
iris = load_iris()
x, y = iris.data, iris.target

# 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 학습
model = GaussianNB()
model.fit(x_train, y_train)

# 예측
y_pred = model.predict(x_test)

# 정확도
print("정확도:", accuracy_score(y_test, y_pred))