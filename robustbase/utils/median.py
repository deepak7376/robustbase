import numpy as np


def median(x, low=False, high=False):
    """
    Calculate the median of a list or array-like object.

    Parameters:
    - x: list or array-like, numeric vector of observations.
    - low: bool, if True, return the low median for even sample size. If ``True``, ``high`` is ignored.
    - high: bool, if True, return the high median for even sample size.

    Returns:
    - float: Median value.
    """

    n = len(x)
    if n == 0:
        raise ValueError("Empty list provided.")

    # for odd sample size, all three medians are the same
    if n % 2 == 1:
        return np.median(a=x)

    # for even sample sizes, the median is the average of the two middle values if
    # neither the low nor high median is requested
    if not (low or high):
        return np.median(a=x)

    # otherwise, either the low or the high median are found via introselect
    median_idx = n // 2
    if low:
        median_idx -= 1

    return np.partition(a=x, kth=median_idx)[median_idx]
