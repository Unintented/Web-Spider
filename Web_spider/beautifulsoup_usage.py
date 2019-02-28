import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
res = requests.get('http://bj.xiaozhu.com/', headers=headers)
# 对返回的结果进行解析，按照标准缩进格式的结构输出，为结构化的数据
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
# page_list > ul > li:nth-of-type(1) > div.result_btm_con.lodgeunitname > div:nth-of-type(1) > span > i
prices = soup.select(
    "#page_list > ul > li > div.result_btm_con.lodgeunitname > div > span > i")
for price in prices:
    # 若不用get_text()得到的是标签
    print(price.get_text())