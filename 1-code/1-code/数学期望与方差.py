#编程实例1: python编写函数E(X),D(X)
#求一组数据 1,2,3的数学期望与方差
def get_EX(list):
    sum = 0
    for i in list:
        sum += i
    ex = sum/len(list)
    return ex
def get_EX_square(list):
    sum = 0
    for i in list:
        sum += i**2
    ex = sum/len(list)
    return ex

#公式法
def get_DX(list):
    return get_EX_square(list)-get_EX(list)**2
#定义法
# def get_DX(list):
#     lists = []
#     for i in list:
#         lists.append((i-(sum(list)/len(list)))**2)
#     dx = sum(lists)/len(lists)
#     return dx

list2 = [1,2,3]
print(get_EX(list2)) #2
print(get_DX(list2)) #0.6667

