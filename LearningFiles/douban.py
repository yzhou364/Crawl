### 获取页面源代码
import requests
import re
import csv
url = "https://movie.douban.com/top250"

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
resp = requests.get(url, headers= headers)

page_content = resp.text
### 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">'
                            r'(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                            r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                            r'.*?<span>(?P<num>.*?)人评价</span>', re.S)
### 开始匹配
result = obj.finditer(page_content)

f = open("douban.csv","w",encoding="utf-8")
csvwriter = csv.writer(f)
csvwriter.writerow(["Name","Year","Rating","Rate numbers"])
for item in result:
    dic = item.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()
print("Finished!")