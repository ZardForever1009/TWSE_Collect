# code that try to grab data from TWSE or yfinance API
# if Ok, analyze data and save it as well
# Creator: Eason Chen of National Cheng Kung University Electrical Engineering
from API import API

import yfinance as yf

msft = yf.Ticker("1101.TW")

# get historical market data
hist = msft.history(period="1mo")
print(round(hist, 2))

API = API("0000-00-00", "0000-00-00", "\n=====Yahoo Finance API Stock Data Collector=====\n")
API.show_title()
API.get_valid_date()

import yfinance as yf

tsmc = yf.Ticker("1101.TW")

# get stock info
print(round(tsmc.history(start=API.start_date, end=API.end_date), 2))
