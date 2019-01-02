import numpy as np
A = np.mat([[1,1],[1,-1]])
print ("A\n", A)

b = np.array([1,2])
print ("b\n", b)

x = np.linalg.solve(A, b)
print("Solution", x)