import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    x_ = np.asarray(x, dtype = float)
    p_ = np.asarray(p, dtype = float)
    E_x = np.sum(x_ * p_)
    return E_x
    pass