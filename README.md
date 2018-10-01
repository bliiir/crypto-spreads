# Crypto-spread API

This script finds assets that are on both Bitfinex and Poloniex and the price spread between the two exchanges and offers the data up through a simple api using the [Nomics api](https://p.nomics.com/cryptocurrency-bitcoin-api/)

<img src="https://www.dropbox.com/s/67qmawnjd6mejuv/Screenshot%202018-10-01%2023.06.26.png?raw=1" alt="drawing" width="500"/>

## HTTP request and query method overview

### Paths

| Method | Path | Descriptions |
| :-- | :-- | :-- |
| `GET` | `~/` | Instructions on how to use the api |
| `GET` | `~/spread` | Displays all assets that are on both Bitfinex and Poloniex, sorted in descending order by spread percentage |


### Endpoints

#### Root

| | |
| :-- | :-- |
| **Method** | `GET` |
| **Endpoint** | `~/` |
| **Query parameters** | None |
| **Description** | Displays instructions on how to use the api |
| **Example** | `~/` |

##### Sample response

```
Methods: GET

Paths:

    ~/          Instructions
    ~/spread    List all assets by spread-percentage in descending order

Query parameters:

    assets      name of asset(s)
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


```

#### All assets

| | |
| :-- | :-- |
| **Method** | `GET` |
| **Endpoint** | `/spread` |
| **Query parameters** | `order_by`, `direction` - both optional |
| **Description** | Displays all assets that are on both Bitfinex and Poloniex, sorted in descending order by spread percentage |
| **Example** | `localhost:8000/spread?order_by=spread_percent&direction=desc` |

##### Sample response
```
[
    {
        "asset": "BAT",
        "price_nomics": 0.16992,
        "price_bitfinex": 0.16841,
        "price_poloniex": 0.172977,
        "spread_usd": 0.00456735,
        "spread_percent": 0.0268794,
        "timestamp": "2018-10-01 22:35:15.093823"
    },
    {
        "asset": "GNT",
        "price_nomics": 0.15337,
        "price_bitfinex": 0.15377,
        "price_poloniex": 0.151367,
        "spread_usd": 0.00240271,
        "spread_percent": 0.0156661,
        "timestamp": "2018-10-01 22:35:14.923219"
    },
...
```

#### Single assets

| | |
| :-- | :-- |
| **Method** | `GET` |
| **Endpoint** | `/spread` |
| **Query parameters** | `assets` - all optional |
| **Description** | Displays all assets that are on both Bitfinex and Poloniex, sorted in descending order by spread percentage |
| **Example** | `localhost:8000/spread?assets=btc` |

##### Sample response
```
[
    {
        "asset": "ETH",
        "price_nomics": 229.537,
        "price_bitfinex": 229.89,
        "price_poloniex": 229.919,
        "spread_usd": 0.0291488,
        "spread_percent": 0.00012699,
        "timestamp": "2018-10-01 22:42:31.199952"
    }
]
```


## External endpoints used

| USD markets | GET |
| :-- | :-- |
| Base | https://api.nomics.com/v1/prices?key={insert_key_here} |
| Bitfinex| https://api.nomics.com/v1/exchange-markets/prices?key={insert_key_here}&currency=USD&exchange=bitfinex |
| Poloniex | https://api.nomics.com/v1/exchange-markets/prices?key={insert_key_here}&currency=USDT&exchange=poloniex |



## Files

Deploy the inventory files below to your server:

| Filename | Description |
| :-- | :-- |
| README.md | This file |
| environment.py | The executable wisgi server |
| crypto_spread.py | The main logic for the spread server |



## Features

* [x] Get lists of assets from Bitfinex and Poloniex - two exchanges that offer margin trading
* [x] Normalize the data to enable cross-exchange comparison
* [x] Crop asset list to the ones they have in common
* [x] Store timestamped data in a MySQL database
* [x] Publish API with cross exchange assets with price in usd, spread in usd and spread in %


### Later

* [ ] Execute arbitrage orders


