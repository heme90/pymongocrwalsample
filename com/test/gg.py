'''
Created on 2019. 4. 29.

@author: Playdata
'''
import bs4
import requests


urllist = ["https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=003&aid=0009208266"]


      
cnt = 0
for u in urllist:
    newsdata = bs4.BeautifulSoup(requests.get(u).text, "lxml")
    #news number --> 시퀀스로 대체
    nn = 1
    try:
        cate =  newsdata.find("meta", property="me2:category2")["content"]  
        tit = newsdata.find("meta",property="og:title")["content"]
        auth = newsdata.find("meta",property="og:article:author")['content']
        ptime = newsdata.select("#main_content > div.article_header > div.article_info > div > span:nth-child(1)")[0].text
        ctime = newsdata.select("#main_content > div.article_header > div.article_info > div > span:nth-child(1)")[0].text
        cont =  newsdata.select("#articleBodyContents")[0].text
        if(len(cont)<300):
            print(u + "it's to small!")
            continue;
        url = newsdata.find("meta",property="og:url")['content']
    except BaseException:
        print(u + "!!!!")
        continue;
    #NoneType
    
    
    newsbody = {"news_number" : nn , "category" : cate, "title" :tit , "author" :auth, "posttime" :ptime , "chgtime" : ctime , "contents" : cont  , "url" :  url}
    cnt +=1
    print(newsbody)
   
