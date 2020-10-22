import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.image as mpimg

x = [1,4,7,10,13,11,11,11,12,15,16,18,19,22]
y = [6,15,7,13,6,18,21,10,18,6,3,12,15,19]
points = np.array([(1,6),(4,15),(7,7),(10,13),(13,6),(12,18),(11,21),(11,10),(12,18),(15,6),(16,3),(18,12),(19,15),(22,19)])

# random values for x and y values
a = np.random.normal(0,10,20)
b = np.random.normal(0,10,20)

# calling the first hull with given points
plt.scatter(x, y)
hull1 = ConvexHull(points)
for simplex in hull1.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1])
plt.show()

# calling the second hull with random generated points
ab = np.hstack((a[:,np.newaxis],b[:,np.newaxis]))
hull2 = ConvexHull(ab)
plt.scatter(a,b)
plt.plot(a[hull2.vertices], b[hull2.vertices])
plt.show()
