import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
   
    # Write code here
    x = np.linalg.norm(a)
    y = np.linalg.norm(b)
    z = x * y
    if x == 0 or y == 0:
         return 0.0
    else:
        cos = float((np.dot(a, b))/z )
    return cos
    pass