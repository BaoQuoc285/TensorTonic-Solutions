import numpy as np

def color_to_grayscale(image):

    image = np.array(image)

    H, W, C = image.shape

    gray = np.zeros((H,W))

    for i in range(H):
        for j in range(W):

            R = image[i,j,0]
            G = image[i,j,1]
            B = image[i,j,2]

            gray[i,j] = 0.299*R + 0.587*G + 0.114*B

    return gray.tolist()