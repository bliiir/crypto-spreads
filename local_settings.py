# Local Settings

import os

# Get key from env
key_nomics = os.environ["NOMICS_API_KEY"]
key_mysql = os.environ["MYSQL_PASSWORD"]

# Set nomics api keys
url_nomics = f"https://api.nomics.com/v1/prices?key={key_nomics}"
url_bitfinex = f"https://api.nomics.com/v1/exchange-markets/prices?key={key_nomics}&currency=USD&exchange=bitfinex"
url_poloniex = f"https://api.nomics.com/v1/exchange-markets/prices?key={key_nomics}&currency=USDT&exchange=poloniex"

instructions = """
Hi - welcome to my spread-bot. Below are the methods, paths and query parameters you can use

Methods: GET

Paths:

    ~/          Instructions
    ~/spread    List all assets by spread-percentage in descending order

Query parameters:

    assets      name of asset
                = * (all)
                = btc
                = ...

    order_by    what attribute to order by
                = id
                = price_nomics
                = price_bitfinex
                = price_poloniex
                = spread_usd
                = spread_percent
                = timestamp


    direction   Which direction to display the order in
                = asc
                = desc

Example:

    ~/spread?assets=*&order_by=spread_percent&direction=desc

    Displays all(*) assets by spread percentage in descending order

"""
