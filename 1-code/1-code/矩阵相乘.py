import numpy as np
#action
A = np.mat([[1,3,20],
            [9,15,14]])
B = np.mat([[4,2,0],
           [-1,1,3],
           [2,0,2]])
C = A*B
print(A)
print('\n')
print(B)
print('\n')
print(C)
print('\n')
print(B.I)
print('\n')
print(C*B.I)