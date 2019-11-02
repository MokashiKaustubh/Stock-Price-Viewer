import pandas as pd
import pandas_datareader as pdr
import datetime as dt
from plotly import graph_objects as go

user_ticker = input('Input Ticker: ')
user_start = input('Please input start date in YY, MM, DD: ')
user_end = input('Please input end date in YY, MM, DD: ')


def stock_price_index(ticker, start, end):
    spi = pdr.DataReader(ticker, 'yahoo', start, end)
    spi.to_csv(f'{ticker}.csv')
    df = pd.read_csv(f'{ticker}.csv')
    fig1 = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
    fig1.update_layout(title=f'{ticker} Stock')
    fig1.show()


stock_price_index(user_ticker, user_start, user_end)

