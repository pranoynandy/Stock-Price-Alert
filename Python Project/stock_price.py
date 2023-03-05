from whatsapp import alert
from yahoo_fin.stock_info import *
from datetime import datetime
import time

us_stocks = []
ind_stocks = []
result = {}

def info(stock):
    price = get_live_price(stock)
    change = round(get_quote_data(stock)["regularMarketChangePercent"],2)
    res = abs(change)

    if res>=3:
        result[stock] = change
    
    return 1

def start():
    my_stocks = []
    if datetime.now().hour >= 7 and datetime.now().hour <= 18:
        my_stocks = ind_stocks
    elif datetime.now().hour >= 19 or datetime.now().hour <= 4:
        my_stocks = us_stocks

    for stock in range(len(my_stocks)):
        info(my_stocks[stock])

if __name__ == "__main__":

    while True:
        with open('stocks.txt', 'r') as stk:
            current_list = None
            for line in stk:
                if line.startswith('US:'):
                    current_list = us_stocks
                elif line.startswith('INDIA:'):
                    current_list = ind_stocks
                else:
                    current_list.append(line.strip())

        print('Strating ...')
        start()

        if result == {}:
            print("No change!")
        else:
            print(result)
            alert(result)

        time.sleep(3600)