import requests
import re
import csv

domain = "https://www.dydytt.net/index2.htm"

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
resp = requests.get(domain, headers = headers, verify= False)
resp.encoding = "gb2312"


obj1 = re.compile(r"2022新片精品.*?<ul>(?P<ul>.*?)</ul>", re.S)
result1 = obj1.finditer(resp.text)
obj2 = re.compile(r"<a href='(?P<url>.*?)'" ,re.S)

urlList = []
for item in result1:
    ul = item.group("ul")
    result2 = obj2.finditer(ul)
    for it in result2:
        urlList.append("https://www.dydytt.net/" + it.group("url"))


"""
for href in urlList[1:]:
    hrefResp = requests.get(href, verify = False)
    hrefResp.encoding = "gb2312"
"""

f = open("dianyingtiantang.csv","w",encoding="utf-8")
csvwriter = csv.writer(f)
for url in urlList:
    print(url)
    csvwriter.writerow([url])
f.close()