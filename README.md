- [x] Figure out how to avoid putting my keys on Github

### Get asset lists from Bitfinex and Poloniex

| USD markets | GET |
| :-- | :-- |
| Base | https://api.nomics.com/v1/prices?key=98615f635e271c3f55947d25807a0fd5 |
| Bitfinex| https://api.nomics.com/v1/exchange-markets/prices?key=98615f635e271c3f55947d25807a0fd5&currency=USD&exchange=bitfinex |
| Poloniex | https://api.nomics.com/v1/exchange-markets/prices?key=98615f635e271c3f55947d25807a0fd5&currency=USDT&exchange=poloniex |

### Find out what assets Poloniex and Bitfinex have in common

1. Extract the tickers from the json objects as two lists
2. Use `set()` and `intersection()` to find common elements
3. Create a new list of objects containing the following attributes for the assets that both exchanges have in common sorted by biggest spread:

## Set up WISGI server

### Enpoints

| All assets| |
|:--|:--|
| Method | `GET` |
| Endpoint | `http://localhost:8000/spreads` |
| Query parameters | `?sort=ascending`, `?sort=descending` |
| Description | |
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
        "spread_avg_24h_usd": 2.1000,
        "spread_avg_24h_percentage": 0.0224
    },
    "eth": {
        "price_avg": 6000.00,
        "price_bitfinex": 6000.00,
        "price_poloniex": 6001.00,
        "spread_usd": 1.0000,
        "spread_percentage": 0.0167,
        "spread_avg_24h_usd": 2.1000,
        "spread_avg_24h_percentage": 0.0224
    }
}
```


| All assets| |
|:--|:--|
| Method | `GET` |
| Endpoint | `http://localhost:8000/spreads` |
| Query parameters | `?sort=ascending`, `?sort=descending` |


| Single asset | `http://localhost:8000/btc` |


## APIs

### Bitfinex


### Poloniex






## DUMP


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


