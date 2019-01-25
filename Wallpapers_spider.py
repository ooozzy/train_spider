import requests
import re
import os
import datetime

class Wallpapers_spider:
    def get_pic_response(r):
        url = "https://alpha.wallhaven.cc/search"
        headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
        }
        params = {
        "categories": "111",
        "purity"  : "100",
        "topRange": "1d",
        "sorting" : "toplist",
        "order"  : "desc",
        "page"   : r
                }
        try:
            response = requests.get(url,headers=headers,params=params)
            if response.status_code == 200:
                results = re.findall("wallpaper/([0-9]*)/thumbTags", response.content.decode(), re.S)
                return results
        except requests.ConnectTimeout:
            return None

    def get_image(id,i):
        headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
        }
        url = "https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}.jpg".format(id)
        try:
            response = requests.get(url,headers=headers)
            if response.status_code == 200:
                with open("{}/{}.jpg".format(today,i), "ab") as f:
                    f.write(response.content)
                    print("保存成功")
        except requests.ConnectTimeout:
            print("请求超时")


    def run(self): #实现主要逻辑
        #1.获取图片编号
        for p in range(1,5):
            results = Wallpapers_spider.get_pic_response(p)
            for i in range(1,25):
                Wallpapers_spider.get_image(results[i-1],i)
        #2.将各个图片的url下载到本地

if __name__=='__main__':
    today = datetime.date.today()
    os.mkdir(str(today))
    spider = Wallpapers_spider()
    spider.run()