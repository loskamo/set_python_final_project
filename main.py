import requests

def get_coins():
    listings_url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing'
    headers = {'Accepts': 'application/json'}
    parameters = {
        'start': '1',
        'limit': '1000',
        'sortBy': 'market_cap',
        'sortType': 'desc',
        'convert': 'USD',
        'cryptoType': 'coins',          # only native coins, not tokens
        'marketCapRange': '1000000000~' # with capitalization 1B+
    }

    response = requests.get(listings_url, headers=headers, params=parameters)
    data = response.json()
    
    if response.status_code == 200:
        crypto_list = data['data']['cryptoCurrencyList']
        return [crypto['symbol'] for crypto in crypto_list]
    else:
        print(f"Error {response.status_code}: {data['status']['error_message']}")
        return []

print(get_coins())