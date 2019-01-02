import numpy as np
import scipy.linalg as lina
a = np.array([[2,1,-5,1],[1,-3,0,-6],[0,2,1,1],[1,4,-7,6]])
b = np.array([8,9,-5,0])
x = lina.solve(a,b)
print("方程的解:",x)