import re
import requests
import bs4

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

"""获取代理IP"""
url = "http://www.xicidaili.com/wt"
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Referer": "http://www.xicidaili.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
        }
r = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
data = soup.table.find_all("td")
ip_compile = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')  # 匹配IP
port_compile = re.compile(r'<td>(\d+)</td>')  # 匹配端口
ip = re.findall(ip_compile, str(data))  # 获取所有IP
port = re.findall(port_compile, str(data))  # 获取所有端口
ips = [":".join(i) for i in zip(ip, port)]  # 组合IP+端口，如：115.112.88.23:8080

#主函数

count = counts = 0
for i in range(len(ips)):
    proxies = {"http":"http://"+ips[i]}
    print(proxies)
    for a in range(10):
        try:
            respond = requests.get(url=url_vote, headers=headers1, params=params, proxies=proxies)
            str_outcome = respond.content.decode()
            print(str_outcome)
            counts += 1
            print("已经刷票成功{}次".format(counts))
        except requests.exceptions.ConnectionError:
            print(ConnectionError)
            if ip[i] in ips:
                ips.remove(ips[i])
            break


