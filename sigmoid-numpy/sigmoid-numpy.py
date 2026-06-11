import numpy as np

def sigmoid(x):
    x = np.array(x)
    sig = 1 / (1 + np.exp(-1*x))

    return sig