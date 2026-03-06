import numpy as np
def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    image = np.array(image)
    H,W = image.shape
    results = [0]*256

    for i in range(H):
        for j in range(W):
            intensity = image[i][j]
            results[intensity] += 1

    return results

    