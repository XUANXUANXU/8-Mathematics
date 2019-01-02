#课堂练习
#求中位数
#比如23,29,20,32,23,21,33,25

#list1 = [23,29,20,32,23,21,33,25 ]
list1 = [10,20,20,20,30 ]

'''
功能：取中位数
参数：list 列表
返回值：median 中位数
'''
def get_Median(list):
    # 步骤1、排序（从小到大）
    list.sort()
    median  = 0
    n = len(list)
    # 步骤2、如果偶数取中间两个数字的平均值，
    # 如果是奇数取中间的一个数，作为中位数
    if n%2 == 0:
        median = (list[n//2]+list[n//2-1])/2
    else:
        median = list[n//2]
    return median

print(get_Median(list1))