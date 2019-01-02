import numpy as np
#action 1...26
I = np.mat([[1,3,20],
            [9,15,14]])
#密钥
K = np.mat([[1,0,1],
            [3,2,7],
            [1,9,2]])
#信息加密C
C = I*K #矩阵相乘
print("加密后的信息为:")
print(C)
print("原信息为:")
print(C*K.I)  #原信息
print("逆矩阵为：")#逆矩阵
print(K.I)
