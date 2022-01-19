from termcolor import colored
import os


class API:

    def __init__(self, start_date, end_date, title, stock_count):
        self.start_date = start_date
        self.end_date = end_date
        self.title = title
        self.stock_count = stock_count

    def show_title(self):
        import os
        os.system('color')
        print(colored(self.title, 'yellow', attrs=['bold']))

    # Get date input from user
    def get_valid_date(self):
        # for start date input
        import datetime
        input_check = True
        while input_check:
            start = input(">> Enter start date(ex. 2020-02-08): ")
            # Check if input format is correct(date)
            try:
                datetime.datetime.strptime(start, "%Y-%m-%d")
            except ValueError:
                os.system('color')
                print(colored(">> Error: invalid date input format\n", 'red'))
                continue
            # Convert date
            start = datetime.datetime.strptime(start, "%Y-%m-%d")
            start_year = start.year
            start_month = start.month
            start_day = start.day
            # Check if date is valid
            # Future date
            if datetime.datetime(start_year, start_month, start_day) > datetime.datetime.today():
                os.system('color')
                print(colored(">> Error: invalid future date\n", 'red'))
            # not a Monday
            elif datetime.datetime.weekday(start) != 0:
                os.system('color')
                print(colored(">> Error: not a Monday\n", 'red'))
            else:
                input_check = False
                from datetime import datetime
                self.start_date = str(start_year) + '-' + str(start_month) + '-' + str(start_day)
        # end date input
        import datetime
        input_check = True
        while input_check:
            end = input(">> Enter end date(ex. 2020-02-08): ")
            # Check if input format is correct(date)
            try:
                datetime.datetime.strptime(end, "%Y-%m-%d")
            except ValueError:
                os.system('color')
                print(colored(">> Error: invalid date input format\n", 'red'))
                continue
            # Convert date
            end = datetime.datetime.strptime(end, "%Y-%m-%d")
            end_year = end.year
            end_month = end.month
            end_day = end.day
            # Check if date is valid
            # Future date
            if datetime.datetime(end_year, end_month, end_day) > datetime.datetime.today():
                os.system('color')
                print(colored(">> Error: invalid future date\n", 'red'))
            # not a friday
            elif datetime.datetime.weekday(end) != 4:
                os.system('color')
                print(colored(">> Error: not a Friday\n", 'red'))
            elif (end - start).days != 4:
                os.system('color')
                print(colored(">> Error: date gap not a week\n", 'red'))
            else:
                input_check = False
                from datetime import datetime, timedelta
                end = end + timedelta(days=1)
                end_year = end.year
                end_month = end.month
                end_day = end.day
                self.end_date = str(end_year) + '-' + str(end_month) + '-' + str(end_day)

    # get full TWSE stock list
    def get_stock_info(self):
        import twstock
        i = 1
        stock_no = open("one.csv", "w")
        for code in range(0000, 10000):
            if str(code) in twstock.codes:
                print(str(code))
                i += 1
            else:
                continue
        stock_no.close()


    def get_stock_price(self):
        import twstock
        stock = twstock.Stock("1592")
        if stock.price==[]:
            print("fail")
        else:
            print(stock.price)

