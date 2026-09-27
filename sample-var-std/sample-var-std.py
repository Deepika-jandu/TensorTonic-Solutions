import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x = np.asarray(x, dtype = 'float')
    l = len(x)
    m = np.mean(x)
    p = l-1
    s_sq = float((1/p) * sum((x-m)**2))
    s = float(np.sqrt(s_sq))
    return {"variance": float(s_sq), "standard_deviation": float(s)}
    # Write code here
    pass