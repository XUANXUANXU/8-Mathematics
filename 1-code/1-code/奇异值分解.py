import numpy as np
A = np.mat([[0,-1.6,0.6],
            [0,1.2,0.8],
            [0,0,0],
            [0,0,0]])
u,sigma,v = np.linalg.svd(A)
print("u=",u)
print("sigma=",sigma)
print("v=",v)