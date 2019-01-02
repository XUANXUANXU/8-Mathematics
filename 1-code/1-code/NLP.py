class NLP:
    #分词
    #严守一把手机关了
    #严守一/把/手机/关了
    dict_words = {}
    def __init__(self):  #初始化一个类
        self.load_dict()
    def __del__(self):
        self.dict_words.clear()
    def load_dict(self):
        #读取字典文件dict.txt 到dict_words
        file_dict = open("/home/xuan/桌面/8-数学基础/1-code/1-code/dict.txt",encoding="utf8")
        for line in file_dict:
            #print(line,end="")/
            line_list = line.split()
            self.dict_words[line_list[1]] = 1 #加载到内存
        file_dict.close()
    def segment(self,str):
        list_segment = [] #分词列表
        while len(str)>0:
            #严守一把手机关了
            #严守一把
            for i in range(len(str)):
                str2 = str[i:]
                if str2 in self.dict_words.keys():
                    #print(str2)
                    list_segment.append(str2)
                    str = str[0:len(str)-len(str2)]
                    #print(str)
                else:
                    if len(str2) == 1:
                        #list_segment.append(str2)
                        str = str[0:len(str) - len(str2)]
        return list_segment

# #本地调用
# nlp = NLP_1603C()  #类的实例
# str = input("输入")
# #nlp.load_dict()  not care
# list_segment = nlp.segment(str)
# str_segment = ""
# list_segment.reverse()
# for i in list_segment:
#     str_segment += i
#     str_segment += "/"
# print(str_segment)