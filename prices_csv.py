#!/usr/bin/env python3
# File: prices_csv.py
# Creates CSV with timestamp of current prices using Binance API

from binance.client import Client
import csv, datetime, os

client = Client("", "") #doesn't need keys

symbols = ['BTCUSDT','ADABTC','ADAUSDT','ETHBTC','ETHUSDT','XMRBTC','XMRUSDT',
        'DOGEBTC','DOGEUSDT']
prices = {} #init dictionary

for ticker in symbols:
    avg_price = client.get_avg_price(symbol=ticker)
    prices[ticker] = avg_price['price'] #appends ticker and price

#makes csv with prices of interest
def create_file(filename):
    with open(filename, "w") as file:
        for ticker in prices:
            file.write(f"{ticker},{prices[ticker]},\n") #per row
    print('Output:', filename) #verbose

today = datetime.datetime.now() #get date
formatted = today.strftime("%Y-%m-%d") #format date yyyy-mm-dd
utime = today.strftime("%s") #unix time

cwd = os.getcwd()
if not os.path.isdir('reports'): os.mkdir('reports') #create reports dir 
create_file(f'{cwd}/reports/{utime}-prices.csv') #make csv with unix timestamp
