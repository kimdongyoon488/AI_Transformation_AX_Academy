import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


counts = pd.read_csv("python/FremontBridge.csv", index_col="Date", parse_dates=True)
weather = pd.read_csv("python/BicycleWeather.csv", index_col="DATE", parse_dates=True)

print(counts.head)
weather.info()

daily = counts.resample("d").sum()
daily["Total"] = daily.sum(axis=1)
daily = daily[["Total"]]


print(daily)

days = ['M', 'T','W','T','F','Sat', 'Sun']

for i in range(7):
    daily[days[i]] = (daily.index.dayofweek == i).astype(float)
print(daily)

from pandas.tseries.holiday import USFederalHolidayCalendar
cal = USFederalHolidayCalendar()
holidays = cal.holidays("2012","2016")
daily = daily.join(pd.Series(1, index=holidays, name="holiday"))
print("===============")
#print(daily.index['2012'])
print("===============")
daily["holiday"].fillna(0, inplace=True)
print(daily)


