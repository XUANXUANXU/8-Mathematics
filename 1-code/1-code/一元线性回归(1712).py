#用一元线性回归方程预测钢筋的抗压强度
list_x = [150,160,170,180,190,200,210,220,230,240] #水泥用量
list_y = [56.9,58.3,61.6,64.6,68.1,73,74.1,77.4,80.2,82.5]#钢筋的强度
#预测水泥用量250,260的钢筋强度（86.4，89.7）
n = len(list_x)
Segma_Xi_Yi = 0
Segma_Xi_2 = 0
for i in range(n):
    Segma_Xi_Yi += list_x[i]*list_y[i]
    Segma_Xi_2 += list_x[i]**2
X_bar = sum(list_x)/n
Y_bar = sum(list_y)/n
b = (Segma_Xi_Yi - n*X_bar*Y_bar)/(Segma_Xi_2-n*X_bar**2)
print(b)
a = Y_bar-b*X_bar
print(a)
#y = a+bx
x1 = 250
y1 = a+b*x1
print("当水泥用量为250时,钢筋的抗压强度为:",y1)
x2 = 260
y2 = a+b*x2
print("当水泥用量为260时,钢筋的抗压强度为:",y2)




