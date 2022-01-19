# code that try to grab data from TWSE or yfinance API or twstock API
# if Ok, analyze data and save it as well
# Creator: Eason Chen of National Cheng Kung University Electrical Engineering
from API import API

API = API("0000-00-00", "0000-00-00", "\n=====Yahoo Finance API Stock Data Collector=====\n", 0)
API.show_title()
# API.get_valid_date()
API.get_stock_info()
API.get_stock_price()

