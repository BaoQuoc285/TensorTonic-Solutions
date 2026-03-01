import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """

    n_sample,n_feature = X.shape
    w= np.zeros(n_feature)
    b = 0.0
    for i in range(steps):
        z = X@w + b 
        
        predict = _sigmoid(z)

        delta_W = (X.T@(predict-y))/n_sample
        delta_b = np.mean(predict-y)
        w -= lr * delta_W
        b -= delta_b*lr
    return w,b

        
        
        
    