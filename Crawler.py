from termcolor import colored
import os


# initialize class
class Crawler:
    # Constructor
    def __init__(self, title, stock_list, high_price, low_price, year, month, day):
        self.title = title
        self.stock_list = stock_list
        self.high_price = high_price
        self.low_price = low_price
        self.year = year
        self.month = month
        self.day = day

    def show_title(self):
        import os
        os.system('color')
        print(colored(self.title, 'yellow', attrs=['bold']))

    def run(self):
        os.system('color')
        print(colored("Reminder >> Date input example (2022-1-10)", 'red'))
        print(colored("         >> Date gap is five days by default", 'red'))
        print(colored("         >> Default timeout preventing blocked\n", 'red'))
        self.get_all_dates()
        self.get_all_data()
        print(colored("\n======TWSE Stock Collect Data Done======\n", 'yellow', attrs=['bold']))

    # Get date input from user
    def get_valid_start_date(self):
        import datetime
        input_check = True
        while input_check:
            date = input(">> Enter start date: ")
            # Check if input format is correct(date)
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                os.system('color')
                print(colored(">> Error: invalid date input format\n", 'red'))
                continue
            # Convert date
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            start_year = date.year
            start_month = date.month
            start_day = date.day
            # Check if date is valid
            # Future date
            if datetime.datetime(start_year, start_month, start_day) > datetime.datetime.today():
                os.system('color')
                print(colored(">> Error: invalid future date\n", 'red'))
            elif datetime.datetime(start_year, start_month, start_day).weekday() != 0:
                os.system('color')
                print(colored(">> Error: not a Monday input\n", 'red'))
            else:
                self.year.append(start_year)
                self.month.append(start_month)
                self.day.append(start_day)
                return date

    def get_all_dates(self):
        date = self.get_valid_start_date()
        from datetime import timedelta
        day = timedelta(days=1)
        counter = 0
        while counter < 4:
            date = date + day
            self.year.append(str(date.year))
            self.month.append(str(date.month))
            self.day.append(str(date.day))
            counter += 1

    def get_all_data(self):
        for company_id in self.stock_list:
            temp_high_price_for_comparison = []
            temp_low_price_for_comparison = []
            os.system('color')
            print(colored(("\n>> start getting " + company_id + " data"), 'yellow'))
            print(colored(">> Successfully connect to TWSE server", 'green'))
            for date_index in range(0, 5):
                temp_month = ""
                temp_day = ""
                if int(self.month[date_index]) <= 9:
                    temp_month = "0" + str(self.month[date_index])
                else:
                    temp_month = str(self.month[date_index])
                if int(self.day[date_index]) <= 9:
                    temp_day = "0" + str(self.day[date_index])
                else:
                    temp_day = str(self.day[date_index])
                date = str(self.year[date_index]) + str(temp_month) + str(temp_day)
                data = self.request_data_url(company_id, date)
                data = data["data"]
                print(colored((">> fetching day " + str(date_index + 1) + " data"), 'green'))
                for single_line_data in data:
                    os.system('color')
                    if single_line_data[0] == str(int(self.year[date_index]) - 1911) + "/" + str(temp_month) + "/" + str(temp_day):
                        temp_high_price_for_comparison.append(float(single_line_data[4]))
                        temp_low_price_for_comparison.append(float(single_line_data[5]))
                    else:
                        continue
                from time import sleep
                print(colored(">> 5 seconds timeout ...", 'cyan'))
                sleep(5)
                os.system('color')
            print(colored((">> complete getting " + company_id + " data"), 'yellow'))
            self.high_price.append(max(temp_high_price_for_comparison))
            self.low_price.append(min(temp_low_price_for_comparison))
            from time import sleep
            if company_id != self.stock_list[len(self.stock_list) - 1]:
                print(colored("\n>> 5 seconds timeout ...", 'cyan'))
                sleep(5)

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
        return data

    def print_data(self):
        print(colored("\n$$$===Final Price Result===$$$", 'yellow', attrs=['bold']))
        for index in range(0, len(self.stock_list)):
            print(colored(("\n>> " + self.stock_list[index]), 'red'))
            print(colored((">> High price: " + str(self.high_price[index])), 'green'))
            print(colored((">> Low price: " + str(self.low_price[index])), 'green'))
        print(colored("\n$$$===$-$-$-$----$-$-$-$===$$\n", 'yellow', attrs=['bold']))
        print(colored(">> All process are done !!!", 'green', attrs=['bold']))

    def write_data_to_file(self):
        if int(self.month[0]) <= 9:
            month = "0" + str(self.month[0])
        else:
            month = str(self.month[0])
        if int(self.day[0]) <= 9:
            day = "0" + str(self.day[0])
        else:
            day = str(self.day[0])
        date = str(self.year[0]) + str(month) + str(day)
        for index in range(0, len(self.stock_list)):
            import os
            from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
            path = "C:\\Users\\user\\Desktop\\Stock\\Data\\" + str(self.stock_list[index]) + ".csv"
            os.chmod(path, S_IWUSR | S_IREAD)  # This makes the file read/write for the owner
            with open(path, 'a') as file:
                file.write(date + "/" + str(self.high_price[index]) + "/" + str(self.low_price[index]) + "\n")
            file.close()
            filename = path
            os.chmod(filename, S_IREAD | S_IRGRP | S_IROTH)
