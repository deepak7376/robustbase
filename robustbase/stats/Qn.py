import numpy as np

def Qn(x, constant=2.21914, finite_corr=True):
    """
    Qn scale estimator, Gaussian efficiency 82%

    Parameters:
    - x: list or array-like, numeric vector of observations.
    - constant: float, number by which the result is multiplied; the default achieves consistency for normally distributed data.
    - finite_corr: bool, logical indicating if the finite sample bias correction factor should be applied. Default to True unless constant is specified.

    Returns:
    - float: Qn scale estimator.
    """
    x = np.asarray(x)  # Convert input to NumPy array
    n = len(x)
    if n < 2:
        raise ValueError("At least 2 observations are required.")

    # Calculate all pairwise absolute differences using NumPy broadcasting
    diffs = np.abs(x[:, np.newaxis] - x)

    # Flatten the upper triangle of the absolute differences matrix and sort
    diffs_flat = np.triu(diffs).flatten()
    diffs_flat = diffs_flat[diffs_flat != 0]  # Remove zeros from the diagonal
    diffs_flat.sort()

    # Calculate the index for Qn estimation
    h = int(np.floor(n / 2) + 1)
    k = int(h * (h - 1) / 2)

    # Calculate the bias correction factor
    corr_factor = bias_corr(n)

    # Calculate the Qn estimator
    qn = constant * diffs_flat[k - 1] * corr_factor if finite_corr else constant * diffs_flat[k - 1]

    return qn

def bias_corr(n):
    """
    Bias correction factor for Qn estimator.

    Parameters:
    - n: int, number of observations.

    Returns:
    - float: Bias correction factor.
    """
    # Determine if the number of observations is even or odd
    even = (n % 2 == 0)

    # Determine the magnitude of n
    magnitude_n = min(n, 13)

    # Calculate the key for bias correction
    n_key = (even, magnitude_n)

    # Calculate the bias correction factor based on key
    if n_key == (True, 13):
        corr_factor = 3.67561 + ((1.9654 + ((6.987 - (77 / n)) / n)) / n)
        corr_factor = 1 / ((corr_factor / n) + 1)
    elif n_key == (False, 13):
        corr_factor = 1.60188 + ((- 2.1284 - (5.172 / n)) / n)
        corr_factor = 1 / ((corr_factor / n) + 1)
    else:
        corr_factor = np.array([0.399356, 0.99365, 0.51321, 0.84401, 0.61220,
                                0.85877, 0.66993, 0.87344, 0.72014, 0.88906, 0.75743])[n - 2]
    return corr_factor
