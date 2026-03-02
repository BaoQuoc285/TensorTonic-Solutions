import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    n_col = len(A)
    n_row = len(A[0])
    new_array = np.zeros((n_row,n_col))
    for i in range(len(A)):
        for j in range(len(A[0])):
            new_array[j][i] = A[i][j]
    return new_array
    
