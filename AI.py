import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model import ARIMA
import hvplot.pandas
import matplotlib.pyplot as plt
citIndex = 0
stream = open("cities.txt", encoding ='utf-8')
cities = [j for j in stream]
df = pd.read_csv('./csvs/Ханты-Мансийск' + '.csv', encoding = 'windows-1251', header = 0)
df.rename(columns = {"Год источника (местный)": "year", "Месяц источника (местный)" : "month", "День источника (местный)" : "day", "Срок источника ": "hour"}, inplace=True)
df.insert(91, column = 'datetime', value = pd.to_datetime(df[["year", "month", "day", "hour"]]))
df3 = df.iloc[150000:]
df3 = df3.interpolate(method='linear')
df3_train = df3.iloc[:16552]
words = ['Температура воздуха по сухому термометру', 'Относительная влажность воздуха', 'Средняя скорость ветра', 'Сумма осадков за период между сроками']
forecast = pd.DataFrame()
for i in range(4):
    model = ARIMA(df3_train[words[i]], order = (3, 1, 3))
    model_fit = model.fit()
    forecast.insert(i, column = words[i], value = model_fit.forecast(steps=44))
datetime = pd.date_range(start='2022-12-31 21:00:00', end = "2023-01-06 06:00:00", freq = '3h')
forecast.insert(4, column = 'datetime', value = datetime)
forecast.to_csv('./csvs/Предсказание_Ханты-Мансийск.csv', encoding = "windows-1251")
