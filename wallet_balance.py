#!/usr/bin/env python3
# File: wallet_balance.py
# Logins in and retrieves wallet data from Binance using keys

from binance.client import Client
import config #keys

client = Client(config.api_key,config.api_secret) #login
info = client.get_account()
bal = info['balances'] #load wallet balances

#print coins with non-null wallet balance
def ready_wallets():
    for asset in bal:
        if float(asset['free']) > 0: 
            print(asset)

ready_wallets()
