import numpy as np
from numpy.linalg import *
A = np.array([[1,2,3],[1,2,3],[2,1,2]])
print(det(A))
a = np.mat(A)
print(a.T)
print(a.I)