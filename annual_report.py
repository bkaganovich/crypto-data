#!/usr/bin/env python3
# File: annual_report.py
# Retrieves timestamp, price, marketcap, volume using CoinGecko API and
# creates annual report CSV for coin pair

import sys, os, datetime
from datetime import timezone, timedelta
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
tz = timezone.utc #UTC timezone

def unix_time(date):
    return int(date.timestamp()) #unix/epoch timestamp

def first_day_of(year):
    end_of_first = datetime.datetime(year, 1, 2, tzinfo=tz)
    end_of_first -= datetime.timedelta(microseconds=1) #yyyy-01-01 23:59
    times = [str(end_of_first), unix_time(end_of_first)]
    return times

def single_report(coin, vs_currency, year):
    history = cg.get_coin_market_chart_range_by_id(coin, vs_currency,
            first_day_of(year)[1], first_day_of(year+1)[1]) #get data from cg

    #create data list by daily timestamp, price, market cap, volume
    data = list(map(lambda x: (str(x[0][0])[:10], x[0][1], x[1][1], x[2][1]),
        zip(history['prices'], history['market_caps'],
            history['total_volumes'])))

    #init reports directory if not present
    cwd = os.getcwd()
    if not os.path.isdir('reports'): os.mkdir('reports') #init reports dir
    filename = f'{cwd}/reports/{year}-{coin}-{vs_currency}.csv' #csv file path

    with open(filename, 'w') as archivo:
        archivo.write(f'Date,Price,Market Capitalization,Total Volume,\n')
        for day in data:
            date = datetime.datetime.fromtimestamp(int(day[0]))
            price = day[1]
            market_cap = day[2]
            total_vol = day[3]
            archivo.write(f'{date},{price},{market_cap},{total_vol}\n')
    print('Output:', filename) #verbose

def bulk_reports(): #modify for desired reports
    coins = ['ethereum','cardano','monero'] #set desired coins
    pairs = ['usd','btc'] #set desired pairs
    this_year = int(datetime.datetime.now().strftime('%Y')) #this year
    start_year = 2021 #set start year range
    end_year = this_year #set end year range

    for year in range(start_year, end_year+1): #each year
        for coin in coins: #each coin
            for pair in pairs: #each pair
                single_report(coin, pair, year) #create report

if not len(sys.argv) > 1:
    bulk_reports() #bulk create all desired reports if no args provided
else:
    coin_id = sys.argv[1] #coin name (e.g., bitcoin)
    into = sys.argv[2] #vs_currency (e.g., usd)
    of_year = int(sys.argv[3]) #year for report (e.g., 2020)
    single_report(coin_id, into, of_year) #create single report by args
