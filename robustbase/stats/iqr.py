import numpy as np

def iqr(x):
    """
    Interquartile range

    Parameters:
    - x: list or array-like, numeric vector of observations.

    Returns:
    - tuple: Interquartile range (Q3 - Q1).
    """
    q1, q3 = np.percentile(x, [25, 75])
    return (q3, q1)
