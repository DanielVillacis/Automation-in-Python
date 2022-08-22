from tracemalloc import start
import requests
from datetime import datetime
import time

stock_input = input("Enter the stock you want to retrieve data: ")
start_date_input = input("Start date from (yyyy/mm/dd): ")
end_date_input = input("To (yyyy/mm/dd): ")

start_date = datetime.strptime(start_date_input, '%Y/%m/%d')
end_date = datetime.strptime(end_date_input, '%Y/%m/%d')

epoch_start = int(time.mktime(start_date.timetuple()))    # convert the input date to epoch time format, same as the web link
epoch_end = int(time.mktime(end_date.timetuple()))




url = f"https://query1.finance.yahoo.com/v7/finance/download/{stock_input}?period1={epoch_start}&period2={epoch_end}&interval=1d&events=history&includeAdjustedClose=true"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

content = requests.get(url, headers=headers).content

print(content)

with open('data.csv', 'wb') as file:
    file.write(content)
