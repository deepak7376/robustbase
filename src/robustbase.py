import statistics
import math
import numpy as np


#Author: Deepak Yadav
#E-mail: dky.united@gmail.com

def mad(data):
    """
    Median absolute deviation (MAD), Gaussian efficiency 37%
    
    """
    if (len(data)==0):
        return None
    elif len(data)==1:
        return 0
    amd=[]                             #absolute median deviation
    median=statistics.median(data)
    for x in data:
        amd.append(abs(x-median))
    return 1.4826*statistics.median(amd)


def Sn(data):
    """
    Sn scale estimator , Gaussian efficiency 58%
    """

    if (len(data)==0):
        return None
    elif len(data)==1:
        return 0
    med=[]
    for i in data:
        diff=[]
        for j in data:
            diff.append(abs(i-j))
        med.append(statistics.median(diff))
    return(1.1926*(statistics.median(med)))


def iqr(data):
    """
    Interquartile range
    """

    if len(data)==0:
        return None
    elif len(data)==1:
        return 0
    q75,q25=np.percentile(data,[75,25])
    return (q75,q25)

def Qn(data):
    """
    Qn scale estimator, Gaussian effieciency 82%
    """

    if (len(data)==0):
        return None
    elif len(data)==1:
        return 0
    diff = []
    h=0
    k=0
    for i in range(0,len(data)):
        for j in range(0,len(data)):
            if i<j:
                diff.append(abs(data[i]-data[j]))

    diff.sort()
    h=int(math.floor(len(data)/2)+1)   #h=[n/2]+1
    k=int(h*(h-1)/2)                    #k=h(h-1)/2
    return 2.219144465985076*diff[k-1]


if __name__ == '__main__':

    data = np.random.randn(10)
    #a = robustbase()
    y = 10 + Qn([1,2,3])
    print(y)

