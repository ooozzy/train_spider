import requests
url = "http://api3.xiguadaili.com/ip/?tid=555553233386749&num=50000&delay=5"
respond = requests.get(url)
str = respond.content.decode()
with open("ip7.txt","w",encoding="utf-8") as f:
    f.write(str.strip("\n,\r"))
