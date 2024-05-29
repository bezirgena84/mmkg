import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

points = np.array([
    [7, 6],  
    [8, 4],  
    [3, -4], 
    [-3, 0],
    [-2, 3], 
    [2, 0],  
    [-6, -4] 
])

hull = ConvexHull(points)

plt.figure()
plt.plot(points[:,0], points[:,1], 'o')
for i, txt in enumerate(['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']):
    plt.annotate(txt, (points[i,0], points[i,1]), fontsize=12, ha='right')

for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

plt.fill(points[hull.vertices, 0], points[hull.vertices, 1], 'k', alpha=0.1)

plt.show()