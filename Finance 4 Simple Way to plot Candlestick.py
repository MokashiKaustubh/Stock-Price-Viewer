import matplotlib.pyplot as plt
from plotly import graph_objects as go
import pandas_datareader as pdr
import pandas as pd
from matplotlib import style
import datetime as dt
import tensorflow as tf
from tensorflow import keras

style.use('ggplot')

start = dt.datetime(2015, 1, 1)
end = dt.datetime(2019, 10, 25)

# print(df1.head(), df2.head())   # to check
# df = pdr.DataReader('TSLA', 'yahoo', start, end)
# df2 same for apple...
# then
# convert to csv
# df.to_csv(filename)
# df2.to_csv('AAPL.csv')


df = pd.read_csv('TSLA.csv')              # here we command the library to read from this variable
df2 = pd.read_csv('AAPL.csv')


fig = go.Figure(data=[go.Candlestick(x=df2['Date'], open=df2['Open'], high=df2['High'], low=df2['Low'], close=df2['Close'])])

fig1 = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])

fig.update_layout(title='Apple Stock')
fig1.update_layout(title='Tesla Stock')
fig.show()
fig1.show()



