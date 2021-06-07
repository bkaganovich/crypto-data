#!/usr/bin/env python3
# File: annual_report.py
# Retrieves prices, marketcap, volume, etc using CoinGecko API, creates yearly 
# report CSV

import sys
from datetime import datetime, timezone
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

tz=timezone.utc #UTC timezone

def unix_time(date):
    return int(date.timestamp()) #unix/epoch timestamp

def first_of(year):
    first = datetime(year, 1, 1, tzinfo=tz) #yyyy-01-01 00:00
    times = [str(first), unix_time(first)] 
    return times

def last_of(year):
    last = datetime(year, 12, 31, 23, 59, 59, tzinfo=tz) #yyyy-12-31 23:59
    times = [str(last), unix_time(last)]
    return times

def report(coin, vs_currency, year):
    #print(first_of(year), last_of(year), sep='\n') #dates
    
    history = cg.get_coin_market_chart_range_by_id(coin, vs_currency,
            first_of(year)[1], last_of(year)[1]) #cg api call

    print('dates', *history,sep=', ') #column titles
    data = {} #init

    for day in history['prices']:
        date = str(day[0])[:10] #timestamp
        data[date] = [day[1]] #init list with timestamps and prices
    for day in history['market_caps']:
        date = str(day[0])[:10] #timestamp
        data[date].append(day[1]) #append market caps
    for day in history['total_volumes']:
        date = str(day[0])[:10] #timestamp
        data[date].append(day[1]) #append volumes
    
    #don't want first entry from previous year
    for key in data:
        if str(datetime.fromtimestamp(int(key))).startswith(str(year-1), 0, 4):
            print(key)
            print(datetime.fromtimestamp(int(key)), data[key])

    filename = 'idk.csv'
    
    '''with open(filename, 'w') as archivo:
        for day in history['prices']:
            #date = history['prices'][day]
            #price = history['prices'][day]
            #market_cap = history['market_caps'][1]
            #total_vol = history['total_volumes'][1]
            #archivo.write(f'{date},{price},\n')'''
    
    '''print(*history['prices'], sep='\n')
    print(*history['market_caps'], sep='\n')
    print(*history['total_volumes'], sep='\n')
    #print(len(history['prices'])) #total entries
    '''

report('cardano', 'usd', int(sys.argv[1]))
