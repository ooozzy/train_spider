import requests
import json
from lxml import etree

headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",'
            }
#获取响应
name = input("请输入要查看短评的电影：")
response_name = requests.get(url="https://movie.douban.com/j/subject_suggest?q="+name,headers=headers)
res_str = response_name.content.decode()
res = json.loads(res_str)
url_id = res[0]['id']
url = "https://movie.douban.com/subject/"+url_id+"/comments?start={}&limit=20&sort=new_score&status=P"
ret = "y"
num = 0
while ret=="y":
    response = requests.get(url = url.format(num),headers=headers)
    res_outcome = response.content.decode()

             #转换为类
    element = etree.HTML(res_outcome)
    str_list = element.xpath("//span[@class='short']/text()")
    for i in range(len(str_list)):
        print("*"*100+"\n")
        print(str_list[i])
        print("\n")
    ret = input("是否继续加载：[y/n]")
    num+=20

         #是否要保存

#with open("original.txt","a",encoding='utf-8') as f:
#    f.write(res_outcome)