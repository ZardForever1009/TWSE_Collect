from termcolor import colored
import os


# initialize get user input class

class GetInput:

    # start & end date format is 00000000 ,ex. 2021/10/8 ->20211008
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def input_reminder(self):
        os.system('color')
        print(colored("\n=====TWSE API Stock Data Collector=====\n", 'yellow', attrs=['bold']))
        print(colored("\n>> Date example: 2020/1/8", 'green', attrs=['bold']))
        print(colored(">> Date gap should be Monday to Friday\n", 'green', attrs=['bold']))
        os.system("pause")
        os.system("cls")

    # Get date input from user
    def get_valid_date(self):
        # start date
        import datetime
        input_check = True
        while input_check:
            start = input(">> Enter start date: ")
            # Check if input format is correct(date)
            start = start.replace("/", "-")
            try:
                datetime.datetime.strptime(start, "%Y-%m-%d")
            except ValueError:
                os.system('color')
                print(colored(">> Error: invalid date format\n", 'red'))
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
            elif datetime.datetime(start_year, start_month, start_day).weekday() != 0:
                os.system('color')
                print(colored(">> Error: not a Monday\n", 'red'))
            else:
                input_check = False
                from datetime import datetime
                self.start_date = str(datetime.strftime(start, '%Y%m%d'))
        # end date
        import datetime
        input_check = True
        while input_check:
            end = input(">> Enter end date: ")
            end = end.replace("/", "-")
            try:
                datetime.datetime.strptime(end, "%Y-%m-%d")
            except ValueError:
                os.system('color')
                print(colored(">> Error: invalid date format\n", 'red'))
                continue
            end = datetime.datetime.strptime(end, "%Y-%m-%d")
            end_year = end.year
            end_month = end.month
            end_day = end.day
            # Check if date is valid
            # Future date
            if datetime.datetime(end_year, end_month, end_day) > datetime.datetime.today():
                os.system('color')
                print(colored(">> Error: invalid future date\n", 'red'))
            elif datetime.datetime(end_year, end_month, end_day).weekday() != 4:
                os.system('color')
                print(colored(">> Error: not a Friday\n", 'red'))
            else:
                input_check = False
                from datetime import datetime
                self.end_date = str(datetime.strftime(end, '%Y%m%d'))
