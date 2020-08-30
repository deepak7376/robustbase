[![Downloads](https://pepy.tech/badge/robustbase)](https://pepy.tech/project/robustbase)
[![Downloads](https://pepy.tech/badge/robustbase/month)](https://pepy.tech/project/robustbase/month)
[![Downloads](https://pepy.tech/badge/robustbase/week)](https://pepy.tech/project/robustbase/week)
# robustbase
> A Python Library to Calculate Estimators.

## Installation

OS X , Windows & Linux:

```sh
pip install robustbase
```
## Usage example

This package is used to calculate the following statistical estimators.

* Qn scale estimator
    * Compute the robust scale estimator Qn, an efficient alternative to the MAD. [Read More.](https://rdrr.io/rforge/robustbase/man/Qn.html)
```python
Qn(x, constant = 2.21914, finite_corr=True)
```

```python
from robustbase import Qn
  
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# with bias correction
res = Qn(x, constant = 2.21914, finite_corr=True)  # ans = 3.196183

# Without bias correction
res = Qn(x, constant = 2.21914, finite_corr=False)  # ans = 4.43828

```

* Sn scale estimator
    * Compute the robust scale estimator Sn, an efficient alternative to the MAD.[Read More.](https://rdrr.io/rforge/robustbase/man/Sn.html)

```python
Sn(x, constant = 1.1926, finite_corr=True)

```

```python
from robustbase import Sn
  
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# with bias correction
# default finite_corr = True
res = Sn(x)  # ans = 3.5778 
# Note: This is not working properly as R Sn code works (Fix it)

# Without bias correction
res = Sn(x, finite_corr=False)  # ans = 3.5778

```

* Median Absolute Deviation(MAD)

```python
mad(x, center = None, constant = 1.4826, na = False,
    low = False, high = False)
```

```python
from robustbase import mad

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = mad(x)

```
* Interquartile Range (IQR)

```python
iqr(x)
```

```python
from robustbase import iqr

x = [1, 2, 3, 4. 5]
res = iqr(x)
```

## Development setup

For local development setup

```sh
git clone https://github.com/deepak7376/robustbase
cd robustbase
pip install -r requirements.txt
```

## Meta

Deepak Yadav – [@imdeepak_dky](https://twitter.com/imdeepak_dky) – dky.united@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/deepak7376/robustbase/blob/master/LICENSE](https://github.com/deepak7376)

## Contributing

1. Fork it (<https://github.com/deepak7376/robustbase/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## References
https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/qn_scale.htm
https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/sn_scale.htm
https://www.statisticshowto.datasciencecentral.com/median-absolute-deviation/
https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/interquartile-range/