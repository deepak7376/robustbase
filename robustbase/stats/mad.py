import numpy as np
from robustbase.utils.median import median


def mad(x, center=None, constant=1.4826, na=False, low=False, high=False):
    """
    Calculate the Median Absolute Deviation (MAD).

    Parameters:
    - x: list or array-like, numeric vector of observations.
    - center: float or None, value around which the MAD is computed. If None, median of x is used.
    - constant: float, scaling factor to make MAD consistent estimator of the standard deviation.
    - na: bool, if True, handle NA/NaN values in x. (Not implemented in this function)
    - low: bool, if True, compute the ‘lo-median’. (Not applicable in this function)
    - high: bool, if True, compute the ‘hi-median’. (Not applicable in this function)

    Returns:
    - float: MAD value.
    """
    x = np.asarray(x)
    if len(x) == 0:
        raise ValueError("Empty list provided.")
    if len(x) == 1:
        return 0.0

    center = median(x) if center is None else center
    amd = np.abs(x - center)
    
    return constant * median(amd)
