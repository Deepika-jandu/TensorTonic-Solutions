import numpy as np

def huber_loss(y_true: list, y_pred: list, delta: float = 1.0) -> float:
    """
    Returns the loss as a float.
    """
    l =[]
    s = np.asarray(y_true, dtype = 'float')
    t = np.asarray(y_pred, dtype = 'float')
    e = s - t
    for i in e:
        if abs(i) <= delta:
            l.append(0.5 * (i**2))

        else:
            l.append(delta*(abs(i) - 0.5 * delta))
    
    # Write code here
    l = np.asarray(l, float)
    return float(l.mean())
    pass