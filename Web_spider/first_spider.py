import requests
res=requests.get('http://bj.xiaozhu.com/')
# 返回结果为<Response [200]>，说明请求网址成功
print(res)
print(res.text)