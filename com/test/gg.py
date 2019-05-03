'''
Created on 2019. 4. 29.

@author: Playdata
'''
import bs4
import requests


urllist = ["https://news.naver.com/main/read.nhn?mode=LS2D&mid=shm&sid1=100&sid2=265&oid=015&aid=0004133840"]


      
cnt = 0
for u in urllist:
    newsdata = bs4.BeautifulSoup(requests.get(u).text, "lxml")
    print(newsdata.text)
