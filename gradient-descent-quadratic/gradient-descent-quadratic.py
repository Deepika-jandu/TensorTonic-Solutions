def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    x = float(x0)
    for i in range(steps):
        dv_f = float(2*a*x + b)
        x = float(x - (dv_f * lr))
    return x
    # Write code here
    pass