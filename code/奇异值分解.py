import numpy as np
A = np.mat([[1,3,5,0],[2,4,6,0]])
u,sigma,v = np.linalg.svd(A)
print("u=",u)
print("sigma=",sigma)
print("v=",v)