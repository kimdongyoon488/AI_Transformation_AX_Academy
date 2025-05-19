import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지


print(sns.__version__)

print(sns.get_dataset_names())

#print(sns.load_dataset("iris"))


iris = sns.load_dataset("iris")      # 붓꽃 데이터
titanic = sns.load_dataset("titanic")  # 타이타닉호 데이터
tips = sns.load_dataset("tips")      # 팁 데이터
flights = sns.load_dataset("flights")  # 여객운송 데이터

#==================================-
#print(titanic)

#sns.countplot(x="class", data=titanic)
#plt.title("Titanic count/class")
#plt.show()


#==================================

#sns.countplot(x="day", data=tips)
#plt.title("요일별 팁을 준 횟수")
#plt.show()



#jointplot
#sns.jointplot(x="sepal_length", y="sepal_width", data=iris)
#plt.suptitle("꽃받침의 길이와 넓이의 Joint Plot", y=1.02)
#plt.show()



#jointplot - kde 옵션 적용
#sns.jointplot(x="sepal_length", y="sepal_width",
#              data=iris, kind="kde")
#plt.suptitle(
#    "꽃받침의 길이와 넓이의 Joint Plot과 Kernel Density Plot",
#    y=1.02
#)
#plt.show()



#sns.pairplot(iris, hue="species", markers=["o", "s", "D"])
#plt.title("Iris Pair Plot, Hue로 꽃의 종을 시각화")
#plt.show()



#heatmap
titanic_size = titanic.pivot_table(index="class",
                                   columns="sex",
                                   aggfunc="size")


print(titanic_size)

# sns.heatmap(titanic_size,
#            cmap=sns.light_palette("red", as_cmap=True),
#            annot=True,
#            fmt="d")
# plt.title("Heatmap")
# plt.show()

# sns.violinplot(x="class", y="age", data=titanic)
# plt.title("바이올린플롯: 좌석등급별 나이 분포")
# plt.show()




# flights_passengers = flights.pivot(index="month", columns="year", values="passengers")

# plt.title("연도, 월 별 승객수에 대한 Heatmap")

# sns.heatmap(flights_passengers,
#             annot=True, fmt="d", linewidths=1)

# plt.show()



#seaborn 스타일

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

sns.set_style("ticks")
sinplot()
plt.show()