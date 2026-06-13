import numpy as np

def entropy_node(y):
    n = len(y)

    if n==0:
        return 0.0
    
    y = np.array(y)
    _, counts = np.unique(y, return_counts=True)

    h = 0
    
    for c in counts:
        p = c/n
        h -= p*np.log2(p)

    return h