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
    if low==True:
        return statistics.median_low(x)
    
    if high==True:
        return statistics.median_high(x)
    
    return statistics.median_high(x)

def mad(x, center = None, constant = 1.4826, na = False,
    low = False, high = False):
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
    """
    Sn scale estimator , Gaussian efficiency 58%
    """
    n = len(x)

    if n==0:
        raise Exception("x sholud be non-empty !!!")
    if n==1:
        return 0
    
    med=[]
    for i in x:
        diff=[]
        for j in x:
            diff.append(abs(i-j))
        med.append(median(diff))
    return round(bias_corr(n) * median(med) * constant, 6) if finite_corr==True else round(median(med) * constant, 6)


def iqr(x):
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
    """
    Qn scale estimator, Gaussian effieciency 82%
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


if __name__ == '__main__':

    x = [i for i in range(1,11)]
    #a = robustbase()
    # print(median(x, low=True))
    # print(mad(x,high=True))
    # print(iqr([1]))
    print(Sn(x))
    print(Sn(x, finite_corr=False))

    

