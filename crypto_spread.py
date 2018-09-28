from local_settings import *
import urllib.request
import json
import requests
from operator import itemgetter

def get_prices(url):
    prices = {}
    data = json.loads(requests.get(url).text)

    if "exchange" in url: # Extract prices from the exchange data
        for each in data:
            prices[each['base']] = float(each['price_quote'])

    else: # Extract prices from the nomics normalized data
        for each in data:
            prices[each['currency']] = float(each['price'])

    return(prices)

# Form simple normalized pricelists from Nomics, Bitfinex and Poloniex
prices_nomics = get_prices(url_nomics)
prices_bitfinex = get_prices(url_bitfinex)
prices_poloniex = get_prices(url_poloniex)


# Make a list of common tickers accross Bitfinex, Poloniex and Nomix in general
common = list(set(prices_bitfinex.keys()).intersection(set(prices_poloniex.keys()), set(prices_nomics.keys())))


assets = []
for ticker in common:
    asset = {}
    asset["ticker"] = ticker
    asset["price_bitfinex"] = prices_bitfinex[ticker]
    asset["price_poloniex"] = prices_poloniex[ticker]
    asset["price_avg"] = prices_nomics[ticker]
    asset["spread_usd"] = abs(prices_bitfinex[ticker]-prices_poloniex[ticker])
    asset["spread_%"] = abs((prices_bitfinex[ticker]-prices_poloniex[ticker])/prices_nomics[ticker]*100)
    assets.append(asset)

sort_criteria = "spread_%"
_reversed = True

assets = sorted(assets, key=itemgetter(sort_criteria), reverse=_reversed)

print(json.dumps(assets, indent=4))
