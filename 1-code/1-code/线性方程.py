import numpy
import scipy.linalg as lina
#系数组成的数组（等号左边自变量的系数）
#系数行列式
a = numpy.array([[1,1,1,1],
                 [1,2,-1,4],
                 [2,-3,-1,-5],
                 [3,1,2,1]])
#等号右边的值
b= numpy.array([5,-2,-2,0])
#解方程组
x = lina.solve(a,b)
print(x)