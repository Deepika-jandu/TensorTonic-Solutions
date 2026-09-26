import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    p= []
    for i in x:
        if i >0:
            p.append(i)
        else:
            p.append(alpha * i)

    p = np.asarray(p, dtype = 'float')
    return p
    # Write code here
    pass