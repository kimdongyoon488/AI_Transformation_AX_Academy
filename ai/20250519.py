import tensorflow.keras as kr;
import numpy as np
import matplotlib.pyplot as plt

# 학습용 데이터(문제지/정답지)를 준비
x_train = np.array([0, 1])
y_train = np.array([1, 3])
print(x_train);         print(y_train)

x_test = np.array([2, 3])
y_test = np.array([5, 7])
print(x_test);          print(y_test)

# 모델 준비(학습 주제: 학생)
model = kr.models.Sequential()
model.add(kr.layers.Dense(1, input_shape=(1,)))
print(type(model))
model.summary()

# 학습 전 모의고사 실시(사전 평가)
y_predict = model.predict(x_test)
print("예측값 :: ", y_predict.flatten());
print("정답    :: ", y_test)

# 수업준비(수업방식 지정)
model.compile('SGD', 'mse')

# 수업실시(반복학습 1000번)
history = model.fit(x_train, y_train, epochs=1000, verbose=1)

# 모의고사 실시(학습 후)
y_predict = model.predict(x_test)
print(y_predict.flatten());