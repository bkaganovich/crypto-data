#!/usr/bin/env python3
# File: history.py
# Retrieves historical price from CoinGecko API

import sys
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

coin = sys.argv[1] #take coin id as first arg
to = sys.argv[2] #value in usd/btc as second arg
day = sys.argv[3] #take date (dd-mm-yyyy) as third arg

history = cg.get_coin_history_by_id(id=coin,date=day,localization='false') #retrieve data from cg
print((history['market_data']['current_price'][to])) #get converted value for specified date

