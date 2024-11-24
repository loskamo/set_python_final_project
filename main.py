from DataUtils import rmsd
from Drawing import plotManyPrices
from PriceProcessing import getSymbols, getPrices, rmsdFiltered

N = 365 * 4 + 1 # 4 years

symbols = getSymbols()
prices = getPrices(symbols, N)

filtered_prices = rmsdFiltered(prices, rmsd(prices['BTCUSDT']))
print(f"There's {len(filtered_prices.keys())} symbols more stable than BTC:")
print(list(filtered_prices.keys()))

plotManyPrices(filtered_prices)
