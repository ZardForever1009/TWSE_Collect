# code that try to grab data from TWSE or yfinance API or twstock API
# if Ok, analyze data and save it as well
# Creator: Eason Chen of National Cheng Kung University Electrical Engineering
from Crawler import Crawler

# stock list
stock_list = ["2408", "2436", "2449", "3035", "3583", "3532"]

TWSE = Crawler("\n=====TWSE Stock History Data Collector=====\n", stock_list, [], [], [], [], [])

TWSE.show_title()
TWSE.run()
TWSE.print_data()
TWSE.write_data_to_file()
