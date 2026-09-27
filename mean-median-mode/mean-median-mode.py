from collections import Counter
import numpy as np
from scipy import stats

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x = np.asarray(x, dtype = 'float')
    m = float(np.mean(x))
    n = float(np.median(x))
    o = float(stats.mode(x, keepdims=False).mode)
    return  {"mean": m, "median": n, "mode": o}
    # Write code here
    pass