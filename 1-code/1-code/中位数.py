#课堂练习
#求中位数
#比如3,2,2,2,1,4
def get_Median(list):
    #排序(从小到大)
    list.sort()
    n = len(list)
    #取中位数,如果长度是奇数,取中间的数字
    if n%2 !=0:
        return list[int(n/2)]
    #如果是偶数,取中间两个数字的平均值
    else:
        return (list[int(n/2)-1]+list[int(n/2)])/2
list1 = [3,2,1]
print(get_Median(list1))


