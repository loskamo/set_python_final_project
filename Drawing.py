import matplotlib.pyplot as plt

def plotPrices(prices):
    plt.figure(figsize=(8, 5))

    plt.plot(prices, marker='o', linestyle='-', label='Prices')

    plt.title('Price Trend')
    plt.xlabel('Time (Index)')
    plt.ylabel('Price')
    plt.grid(True, linestyle='-', alpha=0.7)
    plt.legend()
    plt.tight_layout()

    plt.show()

def plotTwoSeries(series1, series2, labels=('Series 1', 'Series 2')):
    plt.figure(figsize=(10, 6))

    plt.plot(series1, label=f'Normalized {labels[0]}')
    plt.plot(series2, label=f'Normalized {labels[1]}')

    plt.title('Normalized Comparison of Two Series')
    plt.xlabel('Time (Index)')
    plt.ylabel('Normalized Value (0 to 1)')
    plt.legend()
    plt.grid(True, linestyle='-', alpha=0.7)
    plt.tight_layout()

    plt.show()

def plotManyPrices(data_dict):
    plt.figure(figsize=(12, 8))
    
    for label, series in data_dict.items():
        plt.plot(series, label=label)

    plt.title('Time Series Comparison')
    plt.xlabel('Time (Index)')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True, linestyle='-', alpha=0.7)
    plt.tight_layout()

    plt.show()

