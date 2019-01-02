import numpy as np
from numpy.linalg import *
a = np.array([[1,2,-4],
             [-2,2,1],
             [-3,4,-2]])
a=np.mat(a)
print(a.T)
print(det(a))
