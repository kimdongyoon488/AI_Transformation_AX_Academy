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

sns.countplot(x="day", data=tips)
plt.title("요일별 팁을 준 횟수")
plt.show()



#다차원 데이터
sns.jointplot(x="sepal_length", y="sepal_width", data=iris)
plt.suptitle("꽃받침의 길이와 넓이의 Joint Plot", y=1.02)
plt.show()