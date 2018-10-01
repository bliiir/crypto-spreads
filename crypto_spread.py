import urllib.request, json, requests, datetime, mysql.connector as mc
from local_settings import *
from operator import itemgetter

def dispatch(environ):
    """Main function that executes all the sub functions and returns the result to the webserver which then returns it via the api

    Args:
        environ (OBJECT): The environment object passed from the make_server wisgi simple server. The environ object has the query, method and path from the HTTP request

    Returns:
        STRING: A json formatted string with the relevant data from the database to the webserver/api
    """

    query = environ['QUERY_STRING']
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']

    update() # [WORKS] Query the crypto endpoints and update the database

    bits = split_query(query) # [WORKS] Split the query into a dictionary
    # print(bits)
    sql_str = make_sql(bits[0], bits[1], bits[2]) # [WORKS] Assemble SQL from the bits dictionary
    # print(sql_str)
    db_read = exe_sql(method, path, sql_str) # [WORKS] Execute SQL
    # print(db_read)
    return db_read # Return the result of the database query
    # return "hello"


def split_query(query):
    """Split the query up into a key/value dictionary

    Args:
        query (STRING): The raw HTTP query from the users api request

    Returns:
        TUPLE: A tuple with the asset ticker (ie BTC), which column the user wants to order by and in which direction
    """

    try:
        _dict = {}
        parts = query.split('&')

        # Fill up the dictionary
        for part in parts:
            key = part.split('=')[0]
            value = part.split('=')[1]
            _dict[key] = value

        if "assets" in _dict.keys(): assets = _dict['assets']
        else: assets = "*"

        if "order_by" in _dict.keys(): order_by = _dict['order_by']
        else: order_by = 'spread_percent'

        if "direction" in _dict.keys(): direction = _dict['direction']
        else: direction = 'desc'

        return (assets, order_by, direction)

    except:
        return ("*", "spread_percent", "desc")


def make_sql(assets, order_by, direction):
    """Assemble an SQL statement as a string

    Args:
        assets (TYPE): Description
        order_by (TYPE): Description
        direction (TYPE): Description

    Returns:
        TYPE: Description
    """
    if assets == "*": sql_str = f"SELECT * FROM crypto_spread.assets ORDER BY {order_by} {direction}" # If the query is for all results, leave out the WHERE in the SELECT statement
    else: sql_str = f"SELECT * FROM crypto_spread.assets WHERE id='{assets}' ORDER BY {order_by} {direction};"
    return sql_str


# Execute SQL
def exe_sql(method, path, sql_str):

    labels = ['asset', 'price_nomics', 'price_bitfinex', 'price_poloniex', 'spread_usd', 'spread_percent', 'timestamp']

    if method == "GET":

        if path == "/spread":

            db = con() # Open a db connection
            cur = db.cursor() # Get a cursor

            try:
                observations = []

                cur.execute(sql_str, ())
                table = cur.fetchall()

                for row in table: # Loop through each row (tuple) in the query result
                    observation = {} # Reset the observation so it can take a new row
                    for column in range(len(row)): # Loop from 0 to the number of columns in the row
                        observation[labels[column]] = row[column] # Set dictionary key and value
                    observations.append(observation) # Add the observation to the list of observations dictionary

                return json.dumps(observations, indent=4) # Return the query result as a dictionary

            except Exception as exc:
                print(exc)
            finally:
                db.close()
        else: return instructions


    return "Your request is invalid. Please try a different URL"


###############################################################################


# Get data from the APIs
def fetch(url):
    prices = {}
    data = json.loads(requests.get(url).text)

    if "exchange" in url: # Extract prices from the exchange data
        for each in data:
            prices[each['base']] = float(each['price_quote'])

    else: # Extract prices from the nomics normalized data
        for each in data:
            prices[each['currency']] = float(each['price'])

    return(prices)



def write(ticker, p_nom, p_bit, p_pol, s_usd, s_per, ts):
    """Write data to database

    Args:
        ticker (TYPE): The crypto asset ticker - ie BTC
        p_nom (TYPE): The aggregate asset price from the Nomics api
        p_bit (TYPE): The asset price on Bitfinex via the Nomics api
        p_pol (TYPE): The asset price on Poloniex via the Nomics api
        s_usd (TYPE): The calculated USD spread between the Bitfinex and Poloniex price
        s_per (TYPE): The calculated percentage spread between the Bitfinex and Poloniex price using the aggregate nomics price as the denominator
        ts (TYPE): Timestamp - passed as a string to the database
    Returns:
        Nothing
    """

    db = con() # Open a db connection
    cur = db.cursor() # Get a cursor

    # Write the asset data to the database
    try:
        sql_str = "REPLACE INTO assets (id, price_nomics, price_bitfinex, price_poloniex, spread_usd, spread_percent, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cur.execute(sql_str, (ticker, p_nom, p_bit, p_pol, s_usd, s_per, ts))

        # sql_str = f"REPLACE INTO assets (id, price_nomics, price_bitfinex, price_poloniex, spread_usd, spread_percent, timestamp) VALUES ({ticker:s}, {p_nom:.8f}, {p_bit:.8f}, {p_pol:.8f}, {s_usd:.8f}, {s_per:.8f}, {ts:s})"

        # cur.execute(sql_str, ())
        db.commit()

    except Exception as exc: print(exc)
    finally: db.close()


def con():
    """Connect to the database

    Returns:
        OBJECT: Database connection object
    """
    db = mc.connect(
        host="localhost",
        user="root",
        password = key_mysql,
        database="crypto_spread")
    return(db)


def update():
    """Update the database with the current prices from assets on both the Bitfinex and Poloniex exchanges

    Args: None

    Returns: Nothing

    """
    p_nom = fetch(url_nomics)
    p_bit = fetch(url_bitfinex)
    p_pol = fetch(url_poloniex)

    # [WORKS] Make a list of tickers that are present on Bitfinex, Poloniex and Nomix
    common = list(set(p_bit.keys()).intersection(set(p_pol.keys()), set(p_nom.keys())))

    # Iterate through each ticker in the list of assets that are common to both exchanges and execute the write function
    for ticker in common:
        write(ticker, p_nom[ticker], p_bit[ticker], p_pol[ticker], abs(p_bit[ticker]-p_pol[ticker]), abs((p_bit[ticker]-p_pol[ticker])/p_nom[ticker]), datetime.datetime.now())




