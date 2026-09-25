import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    x = np.asarray(x, dtype = float)
    y = np.asarray(y, dtype = float)
    # Write code here
    d = sum((x - y) ** 2)
    n = np.sqrt(d)
    return n
    pass