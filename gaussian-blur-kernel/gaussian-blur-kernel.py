import numpy as np
def gaussian_kernel(size, sigma):
    """
    Generate a normalized 2D Gaussian blur kernel.
    """
    # Write code here
    a = np.zeros((size,size))
    offsets_array = []
    center = size//2
    sum = 0
    for i in range(size):
        for j in range(size):
            x = j - center
            y = i - center
            a[i][j] = np.exp(-(np.pow(x,2) + np.pow(y,2)) /(2*np.pow(sigma,2)))
            sum += a[i][j]
    norm = a / sum
    return norm.tolist()
    