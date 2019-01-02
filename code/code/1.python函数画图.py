import numpy as np
import matplotlib.pyplot as plt
#endpoint=False 不包括－５，５　　
x = np.linspace(-5.0,5.0,300,endpoint=False)
y=x**2+2*x+1
#gca = get current axis 得到当前的轴
ax = plt.gca()
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.plot(x,y,color='red')
plt.show()