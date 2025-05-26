import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
from matplotlib import style

# 데이터 
X = np.array([[0, 0], [1, 1]])
y = [0, 1]

# 모델 생성 및 학습
LinearSVM = svm.LinearSVC()
LinearSVM.fit(X, y)

# 모델 파라미터 확인 (계수와 절편)
w = LinearSVM.coef_[0]     
b = LinearSVM.intercept_[0] 
slope = -w[0] / w[1]       

# 시각화 (결정 경계)
style.use("ggplot")
xx = np.linspace(0, 1.5)  
yy = slope * xx - b / w[1]  

# 시각화 그리기
plt.plot(xx, yy, 'k-', label="Hyperplane")  
plt.scatter(X[:, 0], X[:, 1], c=y)          
plt.legend()
plt.show()