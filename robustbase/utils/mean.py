import numpy as np

def mean(x):
    """
    Calculate the mean of a list or array-like object.

    Parameters:
    - x: list or array-like, numeric vector of observations.

    Returns:
    - float: Mean value.
    """
    x = np.asarray(x)
    if len(x) == 0:
        raise ValueError("Empty list provided.")
    
    return np.mean(x)
