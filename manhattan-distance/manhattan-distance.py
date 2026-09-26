import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    x = np.asarray(x, dtype='float')
    y = np.asarray(y, dtype='float')
    s = float(sum(abs(x - y)))
    return s
    # Write code here
    pass