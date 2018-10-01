## Requirements
* Use two apis
* Store data in MySQL database
* Deploy own api for interacting with the data


## Project plan
1. Get list of assets and prices from Bitfinex and Poloniex
2. Normalize the data to enable cross-exchange comparison
3. Find out what assets Poloniex and Bitfinex have in common
4. Store the timestamped data in a MySQL database
5. Publish API to get cross exchange assets with price in usd, spread in usd and spread in %


## Functionality needed

### Now
* [ ] Get prices
* [ ] Normalize data
* [ ] Store data
* [ ] Get


Own API methods


Get:
Post:

1d average spread
1w average spread
1m average spread



### Later
* [ ] Execute order






## 1. Get asset lists from Bitfinex and Poloniex

| USD markets | GET |
| :-- | :-- |
| Base | https://api.nomics.com/v1/prices?key={insert_key_here} |
| Bitfinex| https://api.nomics.com/v1/exchange-markets/prices?key={insert_key_here}&currency=USD&exchange=bitfinex |
| Poloniex | https://api.nomics.com/v1/exchange-markets/prices?key={insert_key_here}&currency=USDT&exchange=poloniex |


## 2. Normalise the data to enable comparison

## 3. Find out what assets Poloniex and Bitfinex have in common

1. Extract the tickers from the json objects as two lists
2. Use `set()` and `intersection()` to find common elements
3. Create a new list of objects containing the following attributes for the assets that both exchanges have in common sorted by biggest spread:


## 4. Store the timestamped data in a SQL database

## 5. Publish API

### Set up WISGI server

### Enpoints

| spreads| |
|:--|:--|
| Method | `GET` |
| Endpoint | `http://localhost:8000/spreads` |
| Query parameters | `?sort=ascending`, `?sort=descending` |
| Description | Get spreads for all cross-exchange assets |
| Example | `http://localhost:8000/spreads?sort=ascending`|

#### Sample response

```json
{
    "btc": {
        "price_avg": 6000.00,
        "price_bitfinex": 6000.00,
        "price_poloniex": 6001.00,
        "spread_usd": 1.0000,
        "spread_percentage": 0.0167,
        "spread_avg_01d_usd": 2.1000,
        "spread_avg_01d_percentage": 0.0224,
        "spread_avg_07d_usd": 2.1000,
        "spread_avg_07d_percentage": 0.0224,
        "spread_avg_30d_usd": 2.1000,
        "spread_avg_30d_percentage": 0.0224
    },
    "eth": {
        "price_avg": 6000.00,
        "price_bitfinex": 6000.00,
        "price_poloniex": 6001.00,
        "spread_usd": 1.0000,
        "spread_percentage": 0.0167,
        "spread_avg_1d_usd": 2.1000,
        "spread_avg_1d_percentage": 0.0224
    }
}
```






## DUMP


## APIs

### Bitfinex


### Poloniex





Get asset code from user
Respond with current price, USD spread and % spread on Bitfinex and Poloniex

If no asset code, list all assets that are on both platforms ranked by spread




1. Get all assets/USD from Coinmarketcap
2. Convert the response to an object
3. https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5000&convert=USD&sort=percent_change_24h





Ideas

Arbitrage / Spread

Get 24hr price changes in price from nomics
Search
Get biggest 24 hr price movement from nomics
Search



https://api.nomics.com/v1
https://coinmarketcap.com/api/

https://api.coinmarketcap.com/v2/ticker/?limit=10&sort=rank


https://pro-api.coinmarketcap.com
https://pro.coinmarketcap.com/api/v1#section/Authentication
https://pro-api.coinmarketcap.com/v1/exchange/listings/latest



Rank assets by percent_change_24h
Make a list of the 100 assets with most movement
Get prices from Bitfinex
Get prices from Poloniex

Check prices for each of the pairs in the list against Bitfinex and Poloniex
Calculate the spread in USD
Calculate the spread in %


