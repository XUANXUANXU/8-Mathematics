import numpy as np
a = np.array([[2,1,-3],[1,2,-2],[-1,3,2]])

A = np.mat(a)   #使用 mat 方法将 2 维数组转化为矩阵

print(A)
# print(A.T)      #A.T 表示 A 矩阵的转置矩阵：
print(A.I)      #A.I 表示 A 矩阵的逆矩阵：
