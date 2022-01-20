from termcolor import colored
import os


# initialize class

class Crawler:
    # Constructor
    def __init__(self, title, stock_list, high_price, low_price, start_year, start_month, start_day, end_year, end_month, end_day):
        self.title = title
        self.stock_list = stock_list
        self.high_price = high_price
        self.low_price = low_price
        self.start_year = start_year
        self.start_month = start_month
        self.start_day = start_day
        self.end_year = end_year
        self.end_month = end_month
        self.end_day = end_day

    def show_title(self):
        import os
        os.system('color')
        print(colored(self.title, 'yellow', attrs=['bold']))

    def run(self):
        os.system('color')
        print(colored("Warning >> No foolproof design", 'red'))
        print(colored("        >> Be careful with date input\n", 'red'))

    def request_data_url(self, company_id, date):
        import urllib.request as req
        data_url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=" + str(date) + "&stockNo=" + str(company_id) + "&_="
        request = req.Request(data_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
        })
        # Decode data
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")
            # Parsing data (NOT using bs4 ,since bs4 is built for html format)
        import json
        data = json.loads(data)
        import os
        os.system('color')
        print(colored(">> Successfully connect to TWSE website server\n", 'yellow'))

    def printdata(self):
        print(colored("\n=====Final Result=====\n", 'yellow'))
        for index in len(self.stock_list):
            print(colored((">> " + self.stock_list[index]), 'red'))
            print(colored(("High price>> " + self.high_price[index]), 'green'))
            print(colored(("Low price>> " + self.low_price[index]), 'green'))
