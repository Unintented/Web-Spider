import requests
import time
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
def get_info(url):

    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'lxml')
    # ranks_1=soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num > strong')
    # 首页前三首的序号使用了加粗，直接使用上一层次的标签获取具有普适性
    ranks_2=soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')
    songs_2=soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    times_2=soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
    for rank,song,time in zip(ranks_2,songs_2,times_2):
        data = {
            'rank': rank.get_text().strip(),
            'singer':song.get_text().split('-')[0],
            'song': song.get_text().split('-')[1],
            'time': time.get_text().strip()
        }
        print(data['rank']
              +'  song:'
              +data['song']
              +',  singer:'
              +data['singer']
              +',  time:'
              +data['time'])


if __name__=='__main__':
    urls=['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(number) for number in range(1,24)]
    for url in urls:
        get_info(url)
        # time.sleep(2)