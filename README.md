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
* Sn scale estimator
* Median Absolute Deviation(MAD)
* Interquartile Range (IQR)

```python
from robustbase import Qn, Sn, mad, iqr
import numpy as np
  
data = np.random.rand(10)
print(Qn(data))
print(Sn(data))
print(mad(data))
print(iqr(data))
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