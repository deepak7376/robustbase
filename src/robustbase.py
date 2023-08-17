import statistics
import math
import numpy as np


#Author: Deepak Yadav
#E-mail: dky.united@gmail.com

def bias_corr(n):
    # find out if the number of observations is even or odd
    even = bool((n + 1) % 2)                                         

    # find out if the number of observations is greater than 12
    magnitude_n = min(n, 13)

    # from that a key is generated
    n_key = (even, magnitude_n)

    # now the bias correction is calculated
    # for even n greater 12
    if n_key == (True, 13):

            corr_factor = 3.67561 + ((1.9654 + ((6.987 - (77 / n)) / n)) / n)
            corr_factor = 1 / ((corr_factor / n) + 1)

    # for odd n greater 12
    elif n_key == (False, 13):

            corr_factor = 1.60188 + ((- 2.1284 - (5.172 / n)) /n)
            corr_factor = 1 / ((corr_factor / n) + 1)

    # for n less or equal 12
    else:

            # the index of the list reaches from 0 to 10, while n reaches from 2 to 12, so 2 has to be subtracted
            corr_factor = [0.399356, 0.99365, 0.51321, 0.84401, 0.61220,
                                0.85877, 0.66993, 0.87344, 0.72014, 0.88906, 0.75743][n - 2]


    return corr_factor

def median(x, low=False, high=False):
    """
    Calculate the median of a given list of values.

    Parameters
    ----------
    x : list-like
        List of numeric values.
    low : bool, optional
        If True, calculate the 'lo-median' (for even sample size, take the smaller of the two middle values).
    high : bool, optional
        If True, calculate the 'hi-median' (for even sample size, take the larger of the two middle values).

    Returns
    -------
    median : float
        The calculated median based on the provided options.

    Notes
    -----
    The median is a measure of central tendency that represents the middle value in a sorted dataset.
    It is robust to outliers and is often used as an alternative to the mean.

    References
    ----------
    [1] https://docs.python.org/3/library/statistics.html#statistics.median
    """

    # Check if low flag is set
    if low == True:
        return statistics.median_low(x)

    # Check if high flag is set
    if high == True:
        return statistics.median_high(x)

    # Calculate the median using the default (high) method
    return statistics.median_high(x)


def mad(x, center=None, constant=1.4826, na=False, low=False, high=False):
    """
    Calculate the Median Absolute Deviation (MAD) for data x,  Gaussian efficiency 37%

    Parameters
    ----------
    x : array-like
        Numeric vector of observations.
    center : float or None, optional
        Center value to use for calculating the MAD. If None, the median of x is used.
    constant : float, optional
        Number by which the result is multiplied; the default achieves Gaussian efficiency.
    na : bool, optional
        Placeholder for NA handling (not used in this implementation).
    low : bool, optional
        If True, compute the 'lo-median'; take the smaller of the two middle values for even sample size.
    high : bool, optional
        If True, compute the 'hi-median'; take the larger of the two middle values for even sample size.

    Returns
    -------
    mad : float
        Median Absolute Deviation (MAD) calculated from the input data.

    Notes
    -----
    The MAD is a robust measure of the variability or dispersion of a dataset. It is defined as the median of the
    absolute deviations from the median of the data.

    References
    ----------
    [1] Leys, C., Ley, C., Klein, O., Bernard, P., & Licata, L. (2013). Detecting outliers: Do not use standard
    deviation around the mean, use absolute deviation around the median. Journal of Experimental Social Psychology, 49(4),
    764-766.

    """

    # Check for empty input
    if len(x) == 0:
        raise Exception("x should be non-empty !!!")

    # Check for single observation
    if len(x) == 1:
        return 0

    # Calculate the center if not provided
    center = median(x, low, high) if center is None else center

    # Calculate absolute deviations from the center
    amd = np.abs(x - center)

    # Calculate the MAD and return the result
    return round(constant * median(amd), 6)

def Sn(x, constant=1.1926, finite_corr=True):
    """
    Calculate the Sn scale estimator for data x, Gaussian efficiency 58%

    Parameters
    ----------
    x : list
        Numeric vector of observations.
    constant : float, optional
        Number by which the result is multiplied; the default achieves consistency for normally distributed data.
    finite_corr : bool, optional
        Logical indicating if the finite sample bias correction factor should be applied. Default to True unless constant is specified.

    Returns
    -------
    sn : float
        Sn scale estimator calculated from the input data.

    Notes
    -----
    The Sn scale estimator is used to estimate the scale of a dataset, which is a measure of its spread or variability.
    It is based on pairwise absolute differences between observations and their medians.

    References
    ----------
    [1] Rousseeuw, P. J., & Croux, C. (1993). Alternatives to the Median Absolute Deviation. Journal of the American
    Statistical Association, 88(424), 1273-1283.

    """

    # Get the number of observations
    n = len(x)

    # Check for empty input
    if n == 0:
        raise Exception("x should be non-empty !!!")

    # Check for single observation
    if n == 1:
        return 0

    # Convert input list to numpy array
    y = np.array(x)

    # Create a matrix of repeated observations and calculate absolute differences
    z = np.repeat(y, n).reshape(n, n)
    diff = np.abs(y - z)

    # Calculate medians of absolute differences and multiply by constant
    med = np.median(diff, axis=0)
    r = round(median(med) * constant, 6)

    # Apply finite correction if needed and return the Sn estimator
    if finite_corr:
        if n <= 9:
            correction = [.743, 1.851, .954, 1.351, .993, 1.198, 1.005, 1.131]
            correction = correction[n - 2]
        elif (n % 2) == 1:
            correction = n / (n - 0.9)
        else:
            correction = 1
        r = correction * r
    
    return r

def iqr(x):
    """
    Calculate the interquartile range (IQR) for data x.
    
    Parameters
    ----------
    x : array-like
        Numeric vector of observations.
    
    Returns
    -------
    iqr : tuple
        A tuple containing the 75th percentile (Q3) and 25th percentile (Q1) of the input data.
    
    Notes
    -----
    The interquartile range (IQR) is a measure of statistical dispersion, which is the difference between the 75th percentile
    (Q3) and the 25th percentile (Q1) of the dataset. It is often used to identify potential outliers in the data.
    
    References
    ----------
    [1] Tukey, J. W. (1977). Exploratory Data Analysis. Addison-Wesley.
    
    """
    
    # Check for empty input
    if len(x) == 0:
        raise Exception("x should be non-empty !!!")
    
    # Check for single observation
    if len(x) == 1:
        return 0
    
    # Calculate the 75th and 25th percentiles (Q3 and Q1)
    q75, q25 = np.percentile(x, [75, 25])
    
    # Return the IQR as a tuple
    return (q75, q25)

def Qn(x, constant = 2.21914, finite_corr=True):
    """
    Calculate the Qn scale estimator for data x, Gaussian efficiency 82%

    Parameters
    ----------
    x : array-like
        Numeric vector of observations.
    constant : float, optional
        Number by which the result is multiplied; the default achieves consistency for normally distributed data.
    finite_corr : bool, optional
        Logical indicating if the finite sample bias correction factor should be applied. Default to True.

    Returns
    -------
    qn : float
        Qn scale estimator calculated from the input data.

    Notes
    -----
    The Qn scale estimator is used to estimate the scale of a dataset, which is a measure of its spread or variability.
    It is based on pairwise absolute differences between observations.

    References
    ----------
    [1] Rousseeuw, P. J., & Croux, C. (1993). Alternatives to the Median Absolute Deviation. Journal of the American
    Statistical Association, 88(424), 1273-1283.

    """

    # Get the number of observations
    n = len(x)

    # Check for empty input
    if n == 0:
        raise Exception("x should be non-empty !!!")

    # Check for single observation
    if n == 1:
        return 0

    # Convert input to numpy array
    x = np.array(x)

    # Calculate pairwise absolute differences
    diffs = np.abs(np.subtract.outer(x, x))

    # Get the upper triangle of the differences and sort them
    diff_flat = diffs[np.triu_indices(n, k=1)]
    diff_flat.sort()

    # Calculate values for h and k
    h = int(np.floor(n / 2) + 1)
    k = int(h * (h - 1) / 2)

    # Apply finite correction if needed and return the Qn estimator
    return round(constant * diff_flat[k - 1] * bias_corr(n), 6) if finite_corr else round(constant * diff_flat[k - 1], 6)
