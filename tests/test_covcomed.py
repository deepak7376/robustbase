import numpy as np
import pytest
from robustbase.stats.covComed import covComed, CovComedResult  

def test_covcomed_basic():
    np.random.seed(42)
    X = np.random.rand(100, 3)
    result = covComed(X)
    
    assert isinstance(result, CovComedResult), "Result should be of type CovComedResult"
    assert result.cov.shape == (3, 3), "Covariance matrix should be 3x3"
    assert result.center.shape == (3,), "Center should be a 3-element vector"
    assert len(result.weights) == 100, "Weights should have 100 elements"

def test_covcomed_reweight():
    np.random.seed(42)
    X = np.random.rand(100, 3)
    result = covComed(X, reweight=True)
    
    assert isinstance(result, CovComedResult), "Result should be of type CovComedResult"
    assert result.cov.shape == (3, 3), "Covariance matrix should be 3x3"
    assert result.center.shape == (3,), "Center should be a 3-element vector"
    assert len(result.weights) == 100, "Weights should have 100 elements"
    assert np.any(result.weights == 0), "There should be some zero weights when reweighting"

def test_covcomed_custom_control():
    np.random.seed(42)
    X = np.random.rand(100, 3)
    control = {'tolSolve': 1e-5, 'trace': True, 'wgtFUN': '01.original'}
    result = covComed(X, n_iter=1, control=control)
    
    assert isinstance(result, CovComedResult), "Result should be of type CovComedResult"
    assert result.cov.shape == (3, 3), "Covariance matrix should be 3x3"
    assert result.center.shape == (3,), "Center should be a 3-element vector"
    assert len(result.weights) == 100, "Weights should have 100 elements"

# def test_covcomed_no_iterations():
#     np.random.seed(42)
#     X = np.random.rand(100, 3)
#     result = covComed(X, n_iter=0)
    
#     assert isinstance(result, CovComedResult), "Result should be of type CovComedResult"
#     assert result.cov.shape == (3, 3), "Covariance matrix should be 3x3"
#     assert result.center.shape == (3,), "Center should be a 3-element vector"
#     assert len(result.weights) == 100, "Weights should have 100 elements"

def test_covcomed_invalid_wgtfun():
    np.random.seed(42)
    X = np.random.rand(100, 3)
    with pytest.raises(ValueError, match="Only '01.original' wgtFUN is implemented"):
        covComed(X, wgt_fun="invalid")

# # Example with specific data
# def test_covcomed_specific_data():
#     # Using the same example as in the description
#     hbk_x = np.array([
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9],
#         # Add more rows if needed for testing
#     ])
#     with pytest.raises(LinAlgError, match="Covariance matrix is singular"):
#         result = covComed(hbk_x)

if __name__ == "__main__":
    pytest.main()
