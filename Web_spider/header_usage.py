import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
res=requests.get('http://bj.xiaozhu.com/',headers=headers)
# 通过使用try来防止异常导致代码修改后，爬虫重复运行的情况
try:
    print(res.text)
except ConnectionError:
    print('Refuse to connect!')