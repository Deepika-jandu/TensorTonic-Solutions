import numpy as np

def r2_score(y_true: list, y_pred: list) -> float:
    """
    Returns the coefficient of determination as a Python float.
    """
    # Write code here
    y_pred = np.asarray(y_pred, dtype = 'float')
    y_true = np.asarray(y_true, dtype = 'float')
    m = np.mean(y_true)
    
    if np.all(y_true == y_true[0]):
        if np.all(y_true == y_pred):
            return 1.0
        else:
            return 0.0
            
    rs = sum((y_true - y_pred)**2)
    ts = sum((y_true - m) ** 2)
    r_sq = 1- (rs/ts)
    return float(r_sq)
            
    
    
    pass