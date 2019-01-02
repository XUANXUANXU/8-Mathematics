list_x = [[150],[160],[170],[180],[190],[200],[210],[220],[230],[240]] #水泥用量
list_y = [56.9,58.3,61.6,64.6,68.1,73,74.1,77.4,80.2,82.5]#钢筋的强度
#预测水泥用量250,260的钢筋强度（86.4，89.7）
x1 = 250
x2 = 260
from sklearn import linear_model  #机器学习包里面的线性回归模型
#1、用sklearn包进行训练与预测
regr = linear_model.LinearRegression()  #类的实例化
#训练
regr.fit(list_x, list_y)  # train model训练模型
#预测
predict_outcome = regr.predict(300)
print("预测的钢筋强度为：",predict_outcome)
