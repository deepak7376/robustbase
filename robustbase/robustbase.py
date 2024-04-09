import statistics
import math
import numpy as np
import warnings

def deprecated_function():
    warnings.warn("DeprecationWarning: Importing Qn, Sn, iqr, mad from robustbase is deprecated. Please use from robustbase.stats import Qn, Sn, mad, iqr instead.", DeprecationWarning)

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
    if low==True:
        return statistics.median_low(x)
    
    if high==True:
        return statistics.median_high(x)
    
    return statistics.median_high(x)

def mad(x, center = None, constant = 1.4826, na = False,
    low = False, high = False):
    warnings.warn("The 'mad' function is deprecated and will be removed in a future version. Please use from robustbase.stats import Qn, Sn, mad, iqr instead.", DeprecationWarning)
    """
    Median absolute deviation (MAD), Gaussian efficiency 37%
    
    """
    if len(x)== 0:
        raise Exception("x sholud be non-empty !!!")
    if len(x)==1:
        return 0
    # if low TRUE, compute the ‘lo-median’, i.e., for even sample size, 
    # do not average the two middle values, but take the smaller one.

    # if high TRUE, compute the ‘hi-median’, i.e., take the 
    # larger of the two middle values for even sample size.
    
    center = median(x, low, high) if center==None else center
    
    amd=[abs(i-center) for i in x]        
    
    return round(constant*median(amd), 6)


def Sn(x, constant = 1.1926, finite_corr=True):
    warnings.warn("The 'Sn' function is deprecated and will be removed in a future version. Please use from robustbase.stats import Qn, Sn, mad, iqr instead.", DeprecationWarning)
    
    """
    Sn scale estimator , Gaussian efficiency 58%

    Attributes
    ----------
    x : list
        numeric vector of observations.
    constant : float
        number by which the result is multiplied; the default achieves consisteny for normally distributed data.
    finite_corr : bool
        logical indicating if the finite sample bias correction factor should be applied. Default to TRUE unless constant is specified.
    """
    n = len(x)
    if n==0:
        raise Exception("x sholud be non-empty !!!")
    if n==1:
        return 0

    y = np.array([x,]*n)
    z = y.transpose()
    diff = abs(y-z)
    med = np.median(diff, axis=0)
    r = round(median(med) * constant, 6)

    if finite_corr==True :
        if n <=9 :
            correction = [.743, 1.851, .954, 1.351, .993, 1.198, 1.005, 1.131]
            correction = correction[n-2]
        elif (n % 2) == 1:
            correction = n/(n-.9)
        else : 
            correction = 1
        r= correction*r
    return r

def iqr(x):
    warnings.warn("The 'iqr' function is deprecated and will be removed in a future version. Please use from robustbase.stats import Qn, Sn, mad, iqr instead.", DeprecationWarning)
    """
    Interquartile range
    """

    if len(x)==0:
        raise Exception("x sholud be non-empty !!!")
    
    if len(x)==1:
        return 0
    
    q75,q25=np.percentile(x,[75,25])
    return (q75, q25)

def Qn(x, constant = 2.21914, finite_corr=True):
    warnings.warn("The 'Qn' function is deprecated and will be removed in a future version. Please use from robustbase.stats import Qn, Sn, mad, iqr instead.", DeprecationWarning)
    """
    Qn scale estimator, Gaussian effieciency 82%

    Attributes
    ----------
    x : list
        numeric vector of observations.
    constant : float
        number by which the result is multiplied; the default achieves consisteny for normally distributed data.
    finite_corr : bool
        logical indicating if the finite sample bias correction factor should be applied. Default to TRUE unless constant is specified.
    """
    n = len(x)

    if n==0:
        raise Exception("x sholud be non-empty !!!")
    if n==1:
        return 0

    diff = []
    h=0
    k=0
    for i in range(0,n):
        for j in range(i + 1,n):
            diff.append(abs(x[i]-x[j]))

    diff.sort()
    h=int(math.floor(n/2)+1)
    k=int(h*(h-1)/2)                  
    return round(constant*diff[k-1]*bias_corr(n), 6) if finite_corr==True else round(constant*diff[k-1], 6)

