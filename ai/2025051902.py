from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# 연습용 데이터셋 로드
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data,
                                                    data.target,
                                                    random_state=42)


scaler = StandardScaler()
scaler.fit(X_train)              # 학습 데이터로 평균/표준편차 계산
X_train = scaler.transform(X_train)  # 학습 데이터 정규화
X_test = scaler.transform(X_test)    # 테스트 데이터도 같은 기준으로 정규화



# Estimator 인스턴스화 및 하이퍼 파라미터 설정
model = DecisionTreeClassifier(criterion='entropy')

model.fit(X_train, y_train)
y_pred = model.predict(X_test)


print("정확도:", accuracy_score(y_test, y_pred))
