from NetworkRequests import getCoins, availableSymbols, getHistoricalData
from DataUtils import rmsd, normalize

def getSymbols():
    coins = getCoins()
    print(f"Found {len(coins)} coins with capitalization 1B+")
    return [coin+"USDT" for coin in coins]

def getPrices(symbols, N):
    available_symbols = availableSymbols()
    filtered_symbols = list(set(symbols) & set(available_symbols))
    print(f"Only {len(filtered_symbols)} of {len(symbols)} symbols are availiable on Binance")

    print("Getting prices from Binance...")
    prices = {symbol: getHistoricalData(symbol, N) for symbol in filtered_symbols}
    print("Prices received.")

    filtered_prices = {symbol: normalize(price) for symbol, price in prices.items() if len(price) >= N}
    print(f"There are {len(filtered_prices)} symbols with enough data")

    return filtered_prices

def rmsdFiltered(prices, threshold):
    return {symbol: price for symbol, price in prices.items() if rmsd(price) < threshold}