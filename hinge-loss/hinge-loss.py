import numpy as np

def hinge_loss(y_true: list, y_score: list, margin: float = 1.0, reduction: str = "mean") -> float:
    """
    Returns the loss as a float.
    """
    s = np.asarray(y_score, dtype = 'float')
    t = np.asarray(y_true, dtype = 'float')
    l = np.maximum(0.0, margin - t * s)
    func = getattr(np, reduction)
    p = float(func(l))
    return p
     
    # Write code here
    pass