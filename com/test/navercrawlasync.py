'''
Created on 2019. 5. 2.

@author: Playdata
'''

import bs4
import requests
import pymongo
import asyncio


#localhost, 27777 포트
con = pymongo.MongoClient("127.0.0.1", 27777)

#앞 괄호는 db 뒤 괄호는 collection
t = con['news']['news_main']
#db.news_main.ensureIndex({"url" : 1 } , {unique : true})
t.create_index([("url",pymongo.ASCENDING)],unique=True)
print(t)
#newspagelist = [itgi]
newsss = []


def mongoinsert(urllist):
    loop = asyncio.get_event_loop()
    futures = [mongoinasync(u) for u in urllist]
    loop.run_until_complete(asyncio.wait(futures))
    """for u in urllist:
        mongoinasync(u)"""
       
        
@asyncio.coroutine    
async def mongoinasync(u):
    newsdata = await asyncio.get_event_loop().run_in_executor(None, bs4.BeautifulSoup,requests.get(u).text,"lxml")
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
            print(u + "  it's to small!")
            pass
        #url = u
        newsbody = {"news_number" : nn , "category" : cate, "title" :tit , "author" :auth, "posttime" :ptime , "chgtime" : ctime , "contents" : cont  , "url" :  u}
        
        t.insert_one(newsbody,bypass_document_validation = True)
        
    except Exception:
        print(u + "!!!!")
        pass
    #NoneType
    
def navercrawl(ss):    
#ss(date,sectiion[])
    for s in ss[1]:
        sectioncrawl(ss[0],s)
        
  
def sectioncrawl(d,s):    
    urllist = []
    temp = "";
    addr = s + "&date=" + d
    for p in range(1, 100):
        addrs = addr + "&page=" + str(p)
        #doc = await asyncio.get_event_loop().run_in_executor(None, requests.get,addrs)
        doc = requests.get(addrs)
        #newslist = await asyncio.get_event_loop().run_in_executor(None, bs4.BeautifulSoup,doc.text,"lxml")
        newslist = bs4.BeautifulSoup(doc.text, "lxml")
        #html.parser
        ttemp = newslist.select("#main_content > div.paging > strong")[0].text
        if(ttemp == temp):
            print(addrs)
            break;
        else:
            temp = ttemp 
        newss = newslist.select("#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt:first-child > a")
        for i in newss:
            url = i["href"]
            urllist.append(url)
    
    mongoinsert(urllist)

    

