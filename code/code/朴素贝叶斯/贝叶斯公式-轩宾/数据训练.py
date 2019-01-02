import xlrd#要提取xlsx的模块
from sklearn.naive_bayes import GaussianNB
import numpy as np
import random #获取随机数据
file = xlrd.open_workbook(r'/home/coodi/桌面/数据计算/贝叶斯公式/iris.xlsx')#获取xlsx格式的路径
data = file.sheet_by_name('iris')
dict = [] #列表中放的是xlsx的数据
label_list = []
for line in range(data.nrows):
    data1 =data.row_values(line) #获取xlsl里面的每条数据
    data2 = data1[0:4] #获取数值
    dict.append(data2)
    data3 = data1[-1] #获取分类
    label_list.append(data3)
    for i in range(len(label_list)): #将分类数据转为1 2 3
        if label_list[i] == 'Iris-setosa':
            label_list[i] = 1
        elif label_list[i] == 'Iris-versicolor':
            label_list[i] = 2
        elif label_list[i] == 'Iris-virginica':
            label_list[i] = 3
dict1 = [] #获取30%数据为预测
Indexes = [] #索引
label_list1 = [] #获取30%分类为预测
dict2 = [] #获取70%数据为样本
dict3 = [] #获取70%数据为分类
while len(dict1) <= 44:
    rd = random.randint(0,len(dict)-1) #获取150条数据随机的一条
    if dict[rd] not in dict1:
        dict1.append(dict[rd])
    if rd not in Indexes:
        Indexes.append(rd)
for m in range(0,len(dict)):
    if m not in Indexes:
        dict2.append(dict[m])
for n in range(0,len(label_list)):
    if n not in Indexes:
        dict3.append(label_list[n])

for One in Indexes:
    label_list1.append(label_list[One])

features_train = np.array(dict2) #样本数
labels_train = np.array(dict3) #分类数
nb = GaussianNB()
nb.fit(features_train,labels_train) #训练iris
features_test = np.array(dict1)
pred = nb.predict(features_test)  #预测后的结果

#判断预测后的数据与原30%分类预测的数进行比较
dict4 = []
for g in range(len(pred)):
    if pred[g] == label_list1[g]:
        dict4.append(pred[g])
rate = len(dict4)/len(label_list1)
print(rate)




