#coding=utf8
import random
import time
#课堂练习
#编写随机点名程序
#1.读取"1712.txt"　放到list_student
list_student  = []
file_student = open("1712.txt",encoding="utf8")
for line in file_student:
    line = line.strip()
    if len(line)>0:
        list_student.append(line)
file_student.close()
# print(len(list_student))
# print(list_student)
while(1):
    input("请输入任意键开始")
    for i in range(5,0,-1):
        print(i)
        #time.sleep(1)
    print("恭喜:\t", "\033[1;32;44m", random.choice(list_student), " \033[0m", "\t同学!")
