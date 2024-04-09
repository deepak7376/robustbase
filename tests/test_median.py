from typing import Optional, Union

import numpy as np
import pytest

from robustbase.utils.median import median

X_EMPTY = []
X_ODD_N = [5.5, 3.2, -10.0, -2.1, 8.4]
X_EVEN_N = [5.5, 3.2, -10.0, -2.1, 8.4, 0.0]


@pytest.mark.parametrize("as_array", [False, True])
@pytest.mark.parametrize(
    "comb",
    [
        (X_EMPTY, False, False, None),
        (X_EMPTY, True, False, None),
        (X_EMPTY, False, True, None),
        (X_EMPTY, True, True, None),
        (X_ODD_N, False, False, 3.2),
        (X_ODD_N, True, False, 3.2),
        (X_ODD_N, False, True, 3.2),
        (X_ODD_N, True, True, 3.2),
        (X_EVEN_N, False, False, 1.6),
        (X_EVEN_N, True, False, 0.0),
        (X_EVEN_N, False, True, 3.2),
        (X_EVEN_N, True, True, 0.0),
    ],
)
def test_median(
    comb: tuple[Union[list, np.ndarray], bool, bool, Optional[float]],
    as_array: bool,
):
    x, low, high, expected = comb
    if as_array:
        x = np.array(x)

    # for empty samples, an error should be raised
    if expected is None:
        with pytest.raises(ValueError):
            median(x, low=low, high=high)

        return

    # otherwise, the expected median should be returned
    assert median(x, low=low, high=high) == expected
