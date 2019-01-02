import numpy as np
import math
list_X = [74,71,72,68,76,73,67,70,65,74]
list_y = [76,75,71,70,76,79,65,77,62,72]
#（１）
j_x = np.mean(list_X)
print("x的数学期望:",j_x)
j_y = np.mean(list_y)
print("y的数学期望:",j_y)

#（２）
x = np.var(list_X)
print("x的方差:",x)
y = np.var(list_y)
print("y的方差:",y)

#（３,4）
b_x = np.std(list_X)
print("x的标准差:",b_x)
b_y = np.std(list_y)
print("y的标准差:",b_y)

cov_XY = 0
list_XY = []
for i in range(len(list_X)):
    list_XY.append(list_X[i]*list_y[i])
EXY = np.mean(list_XY)
cov_XY = EXY - j_x*j_y
print("xy的协方差:",cov_XY)
R_XY = cov_XY/(math.sqrt(x)*math.sqrt(y))
print("xy的相关系数:",R_XY)
