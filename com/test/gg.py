'''
Created on 2019. 4. 29.

@author: Playdata
'''
import bs4
import requests


urllist = ["https://pypi.org/project/lxml/"]


      
cnt = 0
for u in urllist:
    newsdata = bs4.BeautifulSoup(requests.get(u).text, "html.parser")
    print(newsdata.select("meta"))
