import numpy as np
def sobel_edges(image):
    """
    Apply the Sobel operator to detect edges.
    """
    image = np.array(image)
    H,W = image.shape
    # Write code here
    kx = np.array(
        [[-1,0,1],
         [-2,0,2],
         [-1,0,1]])
    ky = np.array([
        [-1,-2,-1],
        [0,0,0],
        [1,2,1]])
    Gx = np.zeros((H,W))
    Gy = np.zeros((H,W))
    padded_image = np.pad(image,pad_width = 1,mode = 'constant',constant_values = 0)
    for i in range(H):
        for j in range(W):
            tmp = padded_image[i:i+3,j:j+3]
            Gx[i,j] = np.sum(tmp*kx)
            Gy[i,j] = np.sum(tmp*ky)
    magnitude = np.sqrt(Gx**2 + Gy**2)
    return magnitude.tolist()
            
    
    