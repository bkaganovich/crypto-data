#!/usr/bin/env python3
# File: history.py
# Retrieves historical price from CoinGecko API

import sys
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

coin = sys.argv[1] #coin id as first arg
vs_currency = sys.argv[2] #vs_currency pair as second arg
day = sys.argv[3] #date (dd-mm-yyyy) as third arg

history = cg.get_coin_history_by_id(id=coin,date=day,localization='false') #retrieve data from cg
print((history['market_data']['current_price'][vs_currency])) #get converted value for specified date

