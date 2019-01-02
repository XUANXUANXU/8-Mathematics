from sklearn.feature_extraction.text import TfidfVectorizer
import jieba
import jieba.analyse
import numpy as np
import re
"""
求并集
"""
def Union(lines):
    word_list = []
    class_flag = []
    for line in lines:
        index = line.find("######")
        line_split = line[0:index]
        class_falg_split = line[index + 6:]
        class_falg_split_dis = class_falg_split.strip()
        class_flag.append(class_falg_split_dis)
        keywords = jieba.analyse.extract_tags(line_split, topK=60, withWeight=False, allowPOS=())
        list_int = StrToInt(keywords)
        for word in list_int:
            if word not in word_list:
                word_list.append(word)
    return word_list,class_flag
"""
把字符串列表转成阿斯玛列表
"""
def StrToInt(list):
    str_to_int_list = []
    for str2 in list:
        str_dis_2 = ""
        for i in range(len(str2)):
            s_t_i = ord(str2[i])
            str_dis_2 = str_dis_2 + str(s_t_i)
        str_to_int_list.append(str_dis_2)
    return str_to_int_list
"""
统一所有list长度
"""
def UniformList(list,word_list):
    uniform_list = []
    for word in word_list:
        if word in list:
            uniform_list.append(1)
        else:
            uniform_list.append(0)
    return uniform_list
"""
判断结果是多少
"""
def Result(pred):
    if pred == "1":
        return "教育"
    if pred == "2":
        return "娱乐"
    if pred == "3":
        return "女士"
    if pred == "4":
        return "手机"
    if pred == "5":
        return "财经"
    if pred == "6":
        return "体育"
    if pred == "7":
        return "科技"
    if pred == "8":
        return "旅行"
"""
对文章进行非汉字处理，分词，转换为ASCII码，并返回
"""
def DisposeArticle(str_test):
    # 定义处理文章的正则表达式，把文章中所有非汉字的字母去掉（。，“”除外）
    reg_article = r'[a-zA-Z0-9<>/=:.#_&-()+##"（）]|\s'
    content_dispose = re.sub(reg_article, "", str_test)
    keywords2 = jieba.analyse.extract_tags(content_dispose, topK=20, withWeight=False, allowPOS=())
    st_to_list_test = StrToInt(keywords2)
    uni_list = UniformList(st_to_list_test, word_list)
    uni_list_list = []
    uni_list_list.append(uni_list)
    return uni_list_list

#1、读取语料库文件
file_read = open("beyes3.txt","r",encoding="UTF-8")
lines = file_read.readlines()  #读取所有行
#用于接收统一长度的list
list_list = []
#2、求并集、类别集
word_list, class_flag_list = Union(lines)
#3、遍历所有行，对每一行的关键字转化为ASCII码
for line in lines:
    index = line.find("######")
    line_split = line[0:index]
    class_falg_split = line[index:]
    class_falg_split_dis = class_falg_split.strip()
    #提取关键词
    keywords = jieba.analyse.extract_tags(line_split, topK=60, withWeight=False, allowPOS=())
    #把关键字列表转化为ASCII码列表
    str_list = StrToInt(keywords)
    """
    写入文件
    # file = open("txt2\\beyes_segment_ascii.txt", "a+", encoding="UTF-8")
    # for s in str_list:
    #     file.write(s)
    #     file.write("\t")
    # file.write(class_falg_split_dis)
    # file.write("\n")
    # file.close()
    """
    #把ASCII码列表与并集比较，统一list长度
    uniform_list = UniformList(str_list, word_list)
    #接收
    list_list.append(uniform_list)
#关闭
file_read.close()
"""
测试
"""
while(True):
    str_test = input("请输入要分类的文章:")
    uni_list_list = DisposeArticle(str_test)
    #把训练集转换为数组（二维）
    features_train = np.array(list_list)
    #把类别集转换为数组（二维）
    labels_train = np.array(class_flag_list)
    #引入高斯朴素贝叶斯
    from sklearn.naive_bayes import GaussianNB
    #实例化
    clf = GaussianNB()
    #训练数据 fit相当于train
    clf.fit(features_train, labels_train)
    #输出单个预测结果
    features_test = np.array(uni_list_list)
    pred = clf.predict(features_test)
    #print(pred[0])
    #print(type(pred[0]))
    print("预测的类别为:\t",pred)
    print("预测的类别为:\t",Result(pred[0]))


