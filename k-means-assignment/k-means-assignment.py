import numpy as np
def k_means_assignment(points, centroids):
    points = np.array(points)
    centroids = np.array(centroids)
    
    outputs = np.zeros(len(points))
    j=0
    for p in points:
        best_dist = float('inf')
        best_idx = 0

        dist = np.zeros(len(centroids))
        for i in range(len(centroids)):
            dist[i] = (np.linalg.norm(p - centroids[i]))**2

        best_idx = np.argmin(dist)
        outputs[j] = best_idx
        j += 1

    return list(outputs)