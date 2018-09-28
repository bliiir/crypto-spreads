# Local Settings

import os

# Get key from env
key_nomics = os.environ["NOMICS_API_KEY"]

# Set nomics api keys
url_nomics = f"https://api.nomics.com/v1/prices?key={key_nomics}"
url_bitfinex = f"https://api.nomics.com/v1/exchange-markets/prices?key={key_nomics}&currency=USD&exchange=bitfinex"
url_poloniex = f"https://api.nomics.com/v1/exchange-markets/prices?key={key_nomics}&currency=USDT&exchange=poloniex"
