import requests

import datetime
import time

def getCoins():
    listings_url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing'
    headers = {'Accepts': 'application/json'}
    parameters = {
        'start': '1',
        'limit': '1000',
        'sortBy': 'market_cap',
        'sortType': 'desc',
        'convert': 'USD',
        'marketCapRange': '1000000000~' # with capitalization 1B+
    }

    response = requests.get(listings_url, headers=headers, params=parameters)
    data = response.json()

    if response.status_code == 200:
        return [crypto['symbol'] for crypto in data['data']['cryptoCurrencyList']]
    else:
        print(f"Error {response.status_code}: {data['status']['error_message']}")
        return []

def getHistoricalData(symbol, N):
    base_url = 'https://api.binance.com/api/v3/klines'
    limit = 1000  # max records per request, binance limit
    interval = '1d'

    end_time = int(time.time() * 1000)
    start_time = end_time - N * 24 * 60 * 60 * 1000

    all_data = []
    while start_time < end_time:
        params = {
            'symbol': symbol,
            'interval': interval,
            'startTime': start_time,
            'limit': limit
        }
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code != 200:
            raise Exception(f"Error fetching data: {data}")

        if not data:
            break

        all_data.extend(data)

        start_time = data[-1][0] + 1  # get next 1000 elements

    # kline[2] - highest daily price, kline[3] - lowest daily price
    return [(float(kline[2]) + float(kline[3])) / 2 for kline in all_data]

def availableSymbols():
    base_url_info = 'https://api.binance.com/api/v3/exchangeInfo'

    response = requests.get(base_url_info)
    exchange_info = response.json()

    if response.status_code != 200:
        raise Exception(f"Error fetching exchange info: {exchange_info}")

    return {symbol['symbol'] for symbol in exchange_info['symbols']}
