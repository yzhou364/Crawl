import requests
from bs4 import BeautifulSoup

domain = "https://www.dydytt.net/index2.htm"

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
resp = requests.get(domain, headers = headers, verify= False)
resp.encoding = "gb2312"

page = BeautifulSoup(resp.text, "html.parser")


