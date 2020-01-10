robustbase
===========
A Python Library to Calculate Estimators.
<"https://robustbase.readthedocs.io/en/latest/">
:Author: Deepak Yadav
:Version: 2.0
:Copyright: This document has been placed in the public domain.

.. contents::


Qn scale estimator
--------------
The median absolute deviation (MAD) and interquartile range are the two most commonly used robust alternatives to the standard deviation. The MAD in particular is a very robust scale estimator. However, the MAD has the following limitations:

- It does not have particularly high efficiency for data that is in fact normal (37%). In comparison, the median has 64% efficiency for normal data.
- The MAD statistic also has an implicit assumption of symmetry. That is, it measures the distance from a measure of central location (the median).

Rousseeuw and Croux proposed the Qn estimate of scale as an alternative to the MAD. It shares desirable robustness properties with MAD (50% breakdown point, bounded influence function). In addition, it has significantly better normal efficiency (82%) and it does not depend on symmetry.
`ReadMore <https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/qn_scale.htm>` _

Sn scale estimator
-------------------

Rousseeuw and Croux proposed the Sn estimate of scale as an alternative to the MAD. It shares desirable robustness properties with MAD (50% breakdown point, bounded influence function). In addition, it has significantly better normal efficiency (58%) and it does not depend on symmetry.

The Sn scale estimate is defined as:

Sn=cMediani{Medianj|xi−xj|}
That is, for each i we compute the median of {|xi - xj j = 1, ..., n}. The median of these n numbers is then the estimate of Sn. The constant c is determined to make Sn a consistent estimator. The value used is 1.1926 (this is the value needed to make Sn a consistent estimator for normal data).
'ReadMore <https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/sn_scale.htm>'_


Median Absolute Deviation(MAD)
------------------------------

The median absolute deviation(MAD) is a robust measure of how spread out a set of data is. The variance and standard deviation are also measures of spread, but they are more affected by extremely high or extremely low values and non normality. If your data is normal, the standard deviation is usually the best choice for assessing spread. However, if your data isn’t normal, the MAD is one statistic you can use instead.

The MAD is defined as:

MAD = median(|Yi – median(Yi|)

'ReadMore https://www.statisticshowto.datasciencecentral.com/median-absolute-deviation/'_


Interquartile Range (IQR)
-------------------------
The interquartile range is a measure of where the “middle fifty” is in a data set. Where a range is a measure of where the beginning and end are in a set, an interquartile range is a measure of where the bulk of the values lie. That’s why it’s preferred over many other measures of spread (i.e. the average or median) when reporting things like school performance or SAT scores.

The interquartile range formula is the first quartile subtracted from the third quartile:
IQR = Q3 – Q1.

'ReadMore https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/interquartile-range/"_


Installation
---------------
* Install from PyPI pacakage 'or'
 - pip install robustbase
 
* Clone the repo and run 
 - python3 setup.py install
 
How to Use
---------------
code:: 

  from robustbase.robustbase import Qn
  import numpy as np
  
  data = np.random.rand(10)
  print(Qn(data))
 
References
------------
soon...
