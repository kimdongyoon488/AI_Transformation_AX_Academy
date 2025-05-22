# 데이터 불러오기 및 전처리
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score



dataset = load_iris()
data = pd.DataFrame(dataset.data, columns=dataset.feature_names)


X_train, X_test, y_train, y_test = train_test_split(
    data, dataset.target, random_state=42
)


X_train.plot(kind="box")
plt.title("X_train")
plt.show()

X_test.plot(kind="box")
plt.title("X_test")
plt.show()


mms = MinMaxScaler()
X_train_scaled = mms.fit_transform(X_train)
X_test_scaled = mms.transform(X_test)


model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)


pred = model.predict(X_test_scaled)
print("정확도:", accuracy_score(y_test, pred))