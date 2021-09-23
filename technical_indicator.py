import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import ie

import matplotlib.dates as mdates

ticker = 'NFLX'

# Already imported the NFLX close prices into the nflx dataframe table. Got the prices from IEX Finance

# Timeframe=1 year

# nflx

# Rolling means

rolling_mean_10 = nflx.close.rolling(10).mean()

rolling_mean_50 = nflx.close.rolling(50).mean()

nflx.plot(figsize=(10, 5), title='Simple Moving Average')

plt.plot(rolling_mean_10, label='10 Day SMA', color='red')

plt.plot(rolling_mean_50, label='50 Day SMA', color='orange')

plt.legend()

# EMA

EMA_10 = nflx.close.ewm(span=10, adjust=False).mean()

EMA_50 = nflx.close.ewm(span=50, adjust=False).mean()

nflx.plot(figsize=(10, 5), title='Exponential Moving Average')

plt.plot(EMA_10, label='10 Day EMA', color='red')

plt.plot(EMA_50, label='50 Day EMA', color='orange')

plt.legend()

# Bollinger Bands

rolling_mean_20 = nflx.close.rolling(20).mean()

upper_band = rolling_mean_20 + 2 * nflx.close.rolling(20).std()

lower_band = rolling_mean_20 - 2 * nflx.close.rolling(20).std()

nflx.plot(figsize=(10, 5), title='20 Day Rolling Bollinger Bands').fill_between(nflx.index, lower_band, upper_band,
                                                                                alpha=0.1)

plt.plot(upper_band, label='Upper Band', color='red')

plt.plot(lower_band, label='Lower Band', color='orange')

plt.legend()

plt.show()

# MACD

EMA_12 = nflx.close.ewm(span=12, adjust=False).mean()

EMA_26 = nflx.close.ewm(span=26, adjust=False).mean()

MACD = EMA_12 - EMA_26

SignalLine = MACD.ewm(span=9, adjust=False).mean()

nflx.plot(subplots=True, figsize=(10, 5), title='Moving Average Convergence Divergence')

plt.plot(EMA_12, label='12 Day EMA', color='red')

plt.plot(EMA_26, label='26 Day EMA', color='orange')

plt.legend()

plt.show()

MACD.plot(figsize=(10, 5), label='MACD', color='green', title='MACD vs Signal')

plt.plot(SignalLine, label='Signal Line', color='Purple')

plt.legend()

plt.show()

