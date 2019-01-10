import re
import requests
import time

url_vote = "http://h5.kepuchina.cn/voteapi/vote"
params= {
        "callback": "jQuery22405495586320480943_1547050152500",
        "cate_id": "1",
        "work_id": "6",
        "verify": "0fRmz.L8_Ifa8fmUr6WeVa19DfpSltP56Hv14qy_KmGft_RR8A1tJZSfYDPtMTwkMS1C4tlTNz5vhVD0GibFsDR0t.kTd.WGgOxE.gNK6IWz_fLvCo70uZHiU.j.7XoO1srgCc5_BEI.Pd6Y4.CdASlPVOzKZvi.hbpK8BHiFF5lizv6bLKJjg1YkgABJQi2-kABNe8YieASqTmEgnckpY04P-P9oiWyXMFS_qyJ91U5VqH8RFeycJcZMYAdlwerxA0t8rpu87ub8980va6ixGYwYry0cxJwGUq4fUKpvMrCkC6.cxTk.rIjsrfthWzGNNmjBDqliLgEeaoDHmWfXCXbYuWbBzYFclReBlgU4LfO1PiXGjJlyJ7FLQFtozjGjE4-LyvcWissPGiUqaeewcr.gQfbapNRhC-Hjrmji8UHrUBbF.qVJDcE.ZZxnVZLyi1HHpRYqsl2g0nn2E9IhopHyLdFz6W6F1PB4nlj2FZN2HO4bIGxflWz-lq3",
      }



#请求头信息
headers1 = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "DNT": "1",
            "Host": "h5.kepuchina.cn",
            "Referer": "http://zt.kepuchina.cn/20181225/vote.html?type=1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
            }

counts = 0
"""获取代理IP"""
with open("ip3.txt","r",encoding='utf-8') as f:  #打开ip配置文件
    lines = f.readlines()
for line in lines:
    ip = line.strip()
    proxies = {"http": "http://"+ip}
    print(proxies)
    time.sleep(1)
    for a in range(10):
        try:
            respond = requests.get(url=url_vote, headers=headers1, params=params, proxies=proxies, timeout=5)
            str_outcome = respond.content.decode()
            print(str_outcome)
            counts += 1
            print("已经刷票{}次".format(counts))
        except requests.exceptions.ConnectionError:
            print(ConnectionError)
            break
        except requests.exceptions.ReadTimeout:
            print("连接超时")
            break

input("代码运行完成，请按回车键结束")
