import re
import urllib.request as request
import chardet
#爬取主页源代码
def spider(url):
    html_sourse = request.urlopen(url).read()
    codedetect = chardet.detect(html_sourse)
    if codedetect["encoding"] == "utf-8":
        decode_code = "utf-8"
    else:
        decode_code = "gbk"
    html_sourse = html_sourse.decode(decode_code, "ignore")
    return html_sourse
#通过正则表达式，抽取指定类别的URL
def getURL_CLASS(html):
    reg = r'<h3><a href=\"(http.*?.com)\">(.*?)</a>'
    re_url = re.compile(reg)
    url_list = re_url.findall(html)
    return url_list
"""
re.sub(pattern, repl, string, count=0)
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
"""
#根据url获取文章段落主体
def getArtical(url):
    reg = r'<p>(.*?)</p>'
    html = spider(url)
    article = re.compile(reg)
    article_list = article.findall(html)
    article_str = ""
    reg_article = r'[a-zA-Z0-9<>/=:.#_&-()+##"（）]|\s'
    for content in article_list:
        content_dispose = re.sub(reg_article,"",content)
        if len(content_dispose) >= 70:
            article_str += content_dispose
    # print(article_str)
    return article_str
#通过正则表达式，抽取指定的url
def getUrl(html,str):
    reg = r'<a href="(http://(sports|ent|money|auto+' \
          r'|tech|lady|house|travel|edu|mobile).*?.html)"'
    re_url = re.compile(reg)
    url_list = re_url.findall(html)
    url_set_dispose = set()
    for i in range(len(url_list)):
        if str in url_list[i][0] and "<" not in url_list[i][0] and len(url_list[i][0]) < 90:
            url_set_dispose.add(url_list[i][0])
    #把网址写入文件
    str_txt = "beyes_"
    str_txt += str
    str_txt += "_url.txt"
    file = open("txt2\\"+str_txt,"w+",encoding="UTF-8")
    for url in url_set_dispose:
        str_url = url
        str_url += "\n"
        file.write(str_url)
    file.close()
    return url_set_dispose

# html = spider("http://www.163.com")
# url_class_list = getURL_CLASS(html)
# url_list = []
# for line in url_class_list:
#     if line[1] != "新闻" and line[1] != "房产":
#         url_list.append(line[0])
#把类别的url写入文件
# file = open("url_list.txt","w+",encoding="UTF-8")
# for url in url_list:
#     str = url
#     str += "\n"
#     file.write(str)
# file.close()
#读取类别的url
# file = open("url_list.txt","r",encoding="UTF-8")
# urls_in_file = file.readlines()
# # http://auto.163.com
# reg = r'http://(.*?).163'
# for url in urls_in_file:
#     print(url)
#     reg_url = re.compile(reg)
#     url_str = reg_url.findall(url)
#     str = url_str[0]
#     print(str)
#     html = spider(url)
#     # print(html)
#     url_list_in_class = getUrl(html,str)
#     for url_li in url_list_in_class:
#         print(url_li)
"""
urls_in_txt: 27
urls_in_txt: 35
urls_in_txt: 56
urls_in_txt: 107
urls_in_txt: 182
urls_in_txt: 124
urls_in_txt: 82
urls_in_txt: 16
"""
list_read_file = ["beyes_edu_url.txt","beyes_ent_url.txt","beyes_lady_url.txt",
                  "beyes_mobile_url.txt","beyes_money_url.txt","beyes_sports_url.txt","beyes_tech_url.txt","beyes_travel_url.txt"]
# class_flag = 1
# for txt_file in list_read_file:
#     file = open("txt2\\"+txt_file,"r",encoding="UTF-8")
#     urls_in_txt = file.readlines()
#     file.close()
#     count = 1
#     write_article_in_txt = "beyes3.txt"
#     for url in urls_in_txt:
#         url_tripe = url.strip()
#         article = getArtical(url_tripe)
#         if article != "":
#             file_2 = open("txt2\\" + write_article_in_txt, "a+", encoding="UTF-8")
#             file_2.write(article)
#             file_2.write("######")
#             file_2.write(str(class_flag))
#             file_2.write("\n")
#             file_2.close()
#             print(txt_file,"_",count,len(article),"########:",article)
#             count = count + 1
#         if count > 12:
#             break
#     class_flag = class_flag + 1
#         # print(article)




