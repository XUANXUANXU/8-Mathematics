#调用
import NLP
nlp = NLP.NLP()

str = input("输入")
#nlp.load_dict()  not care
list_segment = nlp.segment(str)
str_segment = ""
list_segment.reverse()
for i in list_segment:
    str_segment += i
    str_segment += "/"
print(str_segment)