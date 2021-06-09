## Prerequisites
`pip install -r requirements.txt`

## Description
* **`./prices_csv.py`** retrieves current prices from Binance API and creates day CSV report with timestamp based on desired pairs set in `symbols` list
* **`./wallet_balance.py`** logs in to Binance API and retrieves wallet balances with keys set in `config.py`
* **`./history.py bitcoin usd dd-mm-yyyy`** retrieves historical daily price from CoinGecko API based on three specified arguments: `coin`,`vs_currency`,`day`
* **`./annual_report.py`** retrieves daily prices, market caps, volumes from CoinGecko API and creates bulk annual CSV reports based on desired variables set in `bulk_reports` function: `coins`,`vs_currencies`,`start_year`,`end_year`
* **`./annual_report.py bitcoin usd yyyy`** retrieves daily prices, market caps, volumes from CoinGecko API and creates single annual CSV report for coin pair based on three specified arguments: `coin`,`vs_currency`,`year`


