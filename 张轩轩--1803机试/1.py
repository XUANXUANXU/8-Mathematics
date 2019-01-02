import numpy as np
from numpy.linalg import *
A = np.mat([[3,1,-1,2],[-5,1,3,-4],[2,0,1,-1],[1,-5,3,-3]])
B = np.mat([[-2,-1,1,-2],[5,0,-3,4],[-2,0,0,1],[-1,5,-3,4]])
#（１）
print("A行列式的值:",det(A))
print("B行列式的值:",det(B))
#（２）
print("A的转置矩阵:",A.T)
print("B的转置矩阵:",B.T)
#（３）
print("A的逆矩阵:",A.I)
print("B的逆矩阵:",B.I)
#（４）
c1 = A+B
print("c1:",c1)
c2 = A*B
print("c2:",c2)
c3 = B*A
print("c3:",c3)