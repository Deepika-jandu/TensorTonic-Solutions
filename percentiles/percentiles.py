import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Write code her
    n = len(x)
    x = np.sort(np.asarray(x, dtype=float))
    r = []
    for i in q:
        r.append((i/100) * (n-1))
    l= np.floor(r).astype(int)
    w = np.asarray(r) - l
    u = np.ceil(r).astype(int)
    p = (1-w) * x[l] + w * x[u]
    return p
    pass