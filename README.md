[![Downloads](https://pepy.tech/badge/robustbase)](https://pepy.tech/project/robustbase)
[![Downloads](https://pepy.tech/badge/robustbase/month)](https://pepy.tech/project/robustbase/month)
[![Downloads](https://pepy.tech/badge/robustbase/week)](https://pepy.tech/project/robustbase/week)

# robustbase
> A Python Library to Calculate Robust Statistical Estimators.

## Installation

OS X, Windows & Linux:

```sh
pip install robustbase
```
## Usage Example

This package provides functions to calculate the following robust statistical estimators:

* **Qn Scale Estimator**
    * Computes the robust scale estimator Qn, an efficient alternative to the MAD. [Read More](https://rdrr.io/rforge/robustbase/man/Qn.html)

```python
from robustbase.stats import Qn

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# With bias correction
res = Qn(x)  # result: 3.196183

# Without bias correction
res = Qn(x, finite_corr=False)  # result: 4.43828

```

* **Sn Scale Estimator**
    * Computes the robust scale estimator Sn, an efficient alternative to the MAD. [Read More](https://rdrr.io/rforge/robustbase/man/Sn.html)

```python
from robustbase.stats import Sn

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# With bias correction
res = Sn(x)  # result: 3.5778

# Without bias correction
res = Sn(x, finite_corr=False)  # result: 3.5778

```

* **Median Absolute Deviation (MAD)**
    * Compute the MAD, a robust measure of the variability of a univariate sample of quantitative data. [Read More](https://en.wikipedia.org/wiki/Median_absolute_deviation)

```python
from robustbase.stats import mad

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = mad(x)

```
* **Interquartile Range (IQR)**
    * Compute the interquartile range, a measure of statistical dispersion, or spread. [Read More](https://en.wikipedia.org/wiki/Interquartile_range)

```python
from robustbase.stats import iqr

x = [1, 2, 3, 4, 5]
res = iqr(x)
```

* **Co-Median Location and Scatter "Covariance" Estimator**
    * Compute the multivariate "Comedian" covariance, a robust measure of multivariate location and scatter. Read More

```python
from robustbase.stats import covComed

# Example data matrix
X = np.random.rand(100, 3)

# Compute the Co-Median covariance estimator
result = covComed(X)

# Access the components of the result
print("Covariance Matrix:", result.cov)
print("Center:", result.center)
print("Weights:", result.weights)
```

## Development Setup

For local development setup:

```sh
git clone https://github.com/deepak7376/robustbase
cd robustbase
pip install -r requirements.txt -r requirements-dev.txt
```

## Recent Changes

### Version 3.0.0
- Changed the API's call
- Refactored the dir structure
- Updated README with usage examples for all functions.


## Contributing

1. Fork it ([https://github.com/deepak7376/robustbase/fork](https://github.com/deepak7376/robustbase/fork))
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## References
- [Qn Scale Estimator](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/qn_scale.htm)
- [Sn Scale Estimator](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/sn_scale.htm)
- [Median Absolute Deviation](https://www.statisticshowto.datasciencecentral.com/median-absolute-deviation/)
- [Interquartile Range](https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/interquartile-range/)
