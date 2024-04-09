import numpy as np

def Sn(x, constant=1.1926, finite_corr=True):
    """
    Sn scale estimator, Gaussian efficiency 58%

    Parameters:
    - x: list or array-like, numeric vector of observations.
    - constant: float, number by which the result is multiplied; the default achieves consistency for normally distributed data.
    - finite_corr: bool, logical indicating if the finite sample bias correction factor should be applied. Default to True unless constant is specified.

    Returns:
    - float: Sn scale estimator.
    """
    # Check if the input array has at least 2 observations
    n = len(x)
    if n < 2:
        raise ValueError("At least 2 observations are required.")

    # Calculate all pairwise absolute differences
    pairwise_diffs = np.abs(np.subtract.outer(x, x))

    # Calculate the medians of the pairwise absolute differences
    medians = np.median(pairwise_diffs, axis=0)

    # Calculate the Sn estimator
    sn = constant * np.median(medians)

    # Apply finite sample correction if specified
    if finite_corr:
        if n <= 9:
            correction = [0.743, 1.851, 0.954, 1.351, 0.993, 1.198, 1.005, 1.131]
            correction = correction[n - 2]
        elif n % 2 == 1:
            correction = n / (n - 0.9)
        else:
            correction = 1
        sn *= correction

    return sn
