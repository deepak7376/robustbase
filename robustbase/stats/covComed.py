import numpy as np
from scipy.linalg import solve, LinAlgError
from scipy.spatial.distance import mahalanobis
from collections import namedtuple

CovComedResult = namedtuple('CovComedResult', ['cov', 'center', 'weights'])

def covComed(X, n_iter=2, reweight=False, tol_solve=1e-7, trace=False, wgt_fun="01.original", control=None):
    if control is None:
        control = {}

    # Default control values
    control_defaults = {
        'tolSolve': tol_solve,
        'trace': trace,
        'wgtFUN': wgt_fun
    }

    # Update control with any additional parameters provided
    control.update(control_defaults)

    # Initial center and covariance
    center = np.median(X, axis=0)
    cov = np.cov(X, rowvar=False)

    for i in range(n_iter):
        # Check if covariance matrix is singular
        if np.linalg.matrix_rank(cov) < cov.shape[0]:
            raise LinAlgError("Covariance matrix is singular. Cannot proceed with computations.")

        # Compute Mahalanobis distances
        inv_cov = solve(cov, np.eye(cov.shape[0]), assume_a='pos')
        dists = np.array([mahalanobis(x, center, inv_cov) for x in X])

        if control['trace']:
            print(f"Iteration {i}: center={center}, cov={cov}")

        # Compute weights
        if wgt_fun == "01.original":
            weights = (dists <= 1).astype(int)
        else:
            raise ValueError("Only '01.original' wgtFUN is implemented")

        # Update center and covariance with weights
        if np.sum(weights) == 0:
            break

        center = np.average(X, axis=0, weights=weights)
        cov = np.cov(X.T, aweights=weights)

    # Final reweighting step
    if reweight:
        if np.linalg.matrix_rank(cov) < cov.shape[0]:
            raise LinAlgError("Covariance matrix is singular. Cannot proceed with computations.")
        
        inv_cov = solve(cov, np.eye(cov.shape[0]), assume_a='pos')
        dists = np.array([mahalanobis(x, center, inv_cov) for x in X])
        if wgt_fun == "01.original":
            weights = (dists <= 1).astype(int)
        else:
            raise ValueError("Only '01.original' wgtFUN is implemented")

    return CovComedResult(cov, center, weights)

# Example usage
if __name__ == "__main__":
    # Example data matrix (with non-singular covariance matrix)
    X = np.random.rand(100, 3)  # 100 samples, 3 features

    try:
        result = covComed(X)
        print("Covariance Matrix:", result.cov)
        print("Center:", result.center)
        print("Weights:", result.weights)
    except LinAlgError as e:
        print("Error:", e)
