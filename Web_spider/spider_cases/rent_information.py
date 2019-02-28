import requests
import time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}


def judge_sex(class_name):
    """判断房东性别，通过图片右下角的性别图标"""
    if class_name == ['member_ico']:
        return '男'
    else:
        return '女'


def get_links(url):
    """对每个展示页提取各房源链接"""
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        href = link.get('href')
        get_info(href)


def get_info(url):
    """获取每个房源的具体信息"""
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    # body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4尝试
    titles = soup.select('div.pho_info > h4')
    addresses = soup.select('span.pr5')
    prices = soup.select('#pricePart > div.day_l > span')
    imgs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexes = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    for title, address, price, img, name, sex in zip(titles, addresses, prices, imgs, names, sexes):
        data = {
            'title': title.get_text().strip(),
            'address': address.get_text().strip(),
            'price': price.get_text(),
            'img': img.get('src'),
            'name': name.get_text(),
            'sex': judge_sex(sex.get('class'))
        }
        print(data)


if __name__ == '__main__':
    # 获取一定数量的展示页
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1, 11)]
    for single_url in urls:
        get_links(single_url)
        time.sleep(2)
