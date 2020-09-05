# This program is designed to take a set of stock tickers and return share prices to make an even split across all of them
# Requires yfinance to be installed, ** add when back on own computer.

import time
import yfinance as yf
from datetime import date, timedelta
import calendar

today = date.today()

Stock_Num = input("How many stocks total would you like to split evenly?\n")
print("Great, well split " + Stock_Num + " Stock(s)!\n")
time.sleep(1)
Cash = input("Now how much money are you investing?\n")
time.sleep(1)
ticker = input("Perfect!, now we just need the tickers for your stocks!\n Please use all caps (EX: DPZ or AC.TO)\n")


tickerData = yf.Ticker(ticker)

# In case of needing historical data
# tickerDf = tickerData.history(period='1d', start=yesterday, end=today)

price = tickerData.get_info()
print(price['previousClose'])
