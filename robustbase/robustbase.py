import statistics
import math
import numpy as np


#Author Deepak Yadav
#E-mail: dky.united@gmail.com
#This method is based on Rousseeuw and Croux

class robustbase():

    def __init__(self, data):
        self.data = data

    # Median absolute deviation (MAD), Gaussian efficiency 37%
    def mad(self):
        if (len(self.data)==0):
            return None
        elif len(self.data)==1:
            return 0
        amd=[]                             #absolute median deviation
        median=statistics.median(self.data)
        for x in self.data:
            amd.append(abs(x-median))
        return 1.4826*statistics.median(amd)

    # Sn scale estimator , Gaussian efficiency 58%
    def Sn(self):

        if (len(self.data)==0):
            return None
        elif len(self.data)==1:
            return 0
        med=[]
        for i in self.data:
            diff=[]
            for j in self.data:
                diff.append(abs(i-j))
            med.append(statistics.median(diff))
        return(1.1926*(statistics.median(med)))

    # Standard deviation, non-robust method
    def sd(self):

        if len(self.data)==0:
            return None
        elif len(self.data)==1:
            return 0
        return (statistics.stdev(self.data))

    # Interquartile range
    def iqr(self):

        if len(self.data)==0:
            return None
        elif len(self.data)==1:
            return 0
        q75,q25=np.percentile(self.data,[75,25])
        return (q75,q25)

    # Qn scale estimator, Gaussian effieciency 82%
    def Qn(self):

        if (len(self.data)==0):
            return None
        elif len(self.data)==1:
            return 0
        diff = []
        h=0
        k=0
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if i<j:
                    diff.append(abs(self.data[i]-self.data[j]))

        diff.sort()
        h=int(math.floor(len(self.data)/2)+1)   #h=[n/2]+1
        k=int(h*(h-1)/2)                    #k=h(h-1)/2
        return 2.2219*diff[k-1]


if __name__ == '__main__':

    data = np.random.randn(10)
    a = robustbase(data).iqr()
    y = 10 + a[0]
    print(y)

