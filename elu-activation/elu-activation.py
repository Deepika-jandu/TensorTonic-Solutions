import math
import numpy as np

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    p = []
    for i in x:
        if i > 0:
            p.append(i)
        else:
            q = alpha * (np.exp(i) - 1)
            p.append(q)
    return p