import numpy as np


def median(x, low=False, high=False):
    """
    Calculate the median of a list or array-like object.

    Parameters:
    - x: list or array-like, numeric vector of observations.
    - low: bool, if True, return the low median for even sample size.
    - high: bool, if True, return the high median for even sample size.

    Returns:
    - float: Median value.
    """
    sorted_x = np.sort(x)
    n = len(sorted_x)
    if n == 0:
        raise ValueError("Empty list provided.")
    
    if n % 2 == 1:
        return sorted_x[n // 2]
    elif low:
        return sorted_x[n // 2 - 1]
    elif high:
        return sorted_x[n // 2]
    else:
        return (sorted_x[n // 2 - 1] + sorted_x[n // 2]) / 2