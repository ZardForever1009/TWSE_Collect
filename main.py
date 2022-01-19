# code that try to grab data from TWSE or yfinance API
# if Ok, analyze data and save it as well
# Creator: Eason Chen of National Cheng Kung University Electrical Engineering
from UserInterface import GetInput

UI = GetInput("00000000", "00000000")
UI.input_reminder()
UI.get_valid_date()
