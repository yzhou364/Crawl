from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)

#print(resp.read().decode("utf-8"))

with open("mybaidu.html", "w") as f:
    f.write(resp.read().decode("utf-8"))
f.close()

"""
1.服务器渲染：在服务器端直接把数据和html结合
2.客户端渲染：在客户端结合html和数据

"""