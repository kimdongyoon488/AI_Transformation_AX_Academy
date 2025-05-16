import seaborn as sns
import matplotlib.pyplot as plt
print(sns.__version__)


print(sns.get_dataset_names())

#print(sns.load_dataset("iris"))


titanic = sns.load_dataset("titanic")

print(titanic)

sns.countplot(x="class", data=titanic)
plt.title("Titanic count/class")
plt.show()


