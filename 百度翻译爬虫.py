# coding=utf-8
import json
import requests
while 1:

        #获取语言类型
        str = input("请输入要翻译的文字：")
        url_lan = "https://fanyi.baidu.com/langdetect"
        headers = {
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
        }
        data_lan = {
                "query":str
        }
        response_lan = requests.post(url_lan,data=data_lan,headers=headers)
        response_stlan = response_lan.content.decode()
        response_strlan = json.loads(response_stlan)
        dict_lan = {"zh":"en","en":"zh"}

        #翻译语言
        url_tr = "https://fanyi.baidu.com/basetrans"
        data_tr ={
                "query": str,
                "from":response_strlan["lan"],
                "to":dict_lan[response_strlan["lan"]]
               }
        response_tr = requests.post(url_tr,data=data_tr,headers=headers)
        response_str = response_tr.content.decode()
        dic_outcome = json.loads(response_str)
        print("翻译的结果为：",dic_outcome['trans'][0]['dst'])
