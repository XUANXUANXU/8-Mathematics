#coding=utf8
import numpy as np
a = np.array([[1,2,3],
              [2,2,1],
              [3,4,3]])

A = np.mat(a)   #使用 mat 方法将 2 维数组转化为矩阵

print(A)
print(A.T)      #A.T 表示 A 矩阵的转置矩阵：
print(A.T.I)
print(A.I)      #A.I 表示 A 矩阵的逆矩阵：




