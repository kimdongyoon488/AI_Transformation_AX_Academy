import pandas as pd
print(pd.__version__)

data = [1,2,3,4]
index = ["A", "B" ,"C", "D"]
series1 = pd.Series(data=data, index=index)
print(series1)


data = {"colum1":[1,2,3,4], "colum2":["a","b","c","d"]}
dataFrame1 = pd.DataFrame(data, index=index)
print(dataFrame1)

