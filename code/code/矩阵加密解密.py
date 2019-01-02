import numpy as np
info = np.array([[73,29,17],
                 [21,48,30],
                 [12,7,11]])
info_A = np.mat(info)
key = np.array([[1,2,3],
                [2,2,1],
                [3,4,3]])
key_A = np.mat(key)
after_A = info_A*key_A
print(after_A)
key1 = np.array([[1,2,3],
                [2,2,1],
                [3,4,3]])
key1_A = np.mat(key1)
print(after_A*key1_A.I)