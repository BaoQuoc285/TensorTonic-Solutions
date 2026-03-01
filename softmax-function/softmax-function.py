import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.asarray(x, dtype=float)

    # Case 1: vector 1D
    if x.ndim == 1:
        x_shifted = x - np.max(x)   # tránh overflow
        exp_x = np.exp(x_shifted)
        return exp_x / np.sum(exp_x)

    # Case 2: matrix 2D (row-wise)
    elif x.ndim == 2:
        x_shifted = x - np.max(x, axis=1, keepdims=True)
        exp_x = np.exp(x_shifted)
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

    else:
        raise ValueError("Input must be 1D or 2D array")