import numpy as np
from math import sqrt

def normalize(series):
    series = np.log2(series)
    return (series - np.min(series)) / (np.max(series) - np.min(series))

def rmsd(data):
    N = len(data)
    growing_line = [i / (N-1) for i in range(N)]

    squared_differences = [(x - y) ** 2 for x, y in zip(growing_line, data)]
    mean_squared_difference = sum(squared_differences) / len(squared_differences)
    return sqrt(mean_squared_difference)
