list_x = [150,160,170,180,190,200,210,220,230,240] #水泥用量
list_y = [56.9,58.3,61.6,64.6,68.1,73,74.1,77.4,80.2,82.5]#钢筋的强度
#预测水泥用量250,260的钢筋强度（86.4，89.7）
x1 = 250
x2 = 260
#Y = a + bX
Xigema_xy = 0
X_bar = 0
Y_bar = 0
Xigema_X_2 = 0
n = len(list_x)
for i in range(len(list_x)):
    Xigema_xy += list_x[i]*list_y[i]
    X_bar += list_x[i]
    Y_bar += list_y[i]
    Xigema_X_2 += list_x[i]**2
X_bar /= len(list_x)
Y_bar /= len(list_y)

b = (Xigema_xy - n*X_bar*Y_bar)/(Xigema_X_2 - n*(X_bar**2))
print(b)
a = Y_bar - b*X_bar
print(a)
#Y = a + bX
y1 = a+b*x1
y2 = a+b*x2
print(x1,x2,'对应的水泥强度分别为：',y1,y2)