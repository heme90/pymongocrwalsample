'''
Created on 2019. 4. 29.

@author: Playdata
'''
import bs4
import requests
import time
import datetime
import pymongo

con = pymongo.MongoClient("127.0.0.1", 27777)
t = con['test']['tec']

stt = time.time()
#db.tec.ensureIndex({url : 1},{unique : true})

itgi = ["https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=731"]

newspagelist = [itgi]
newsss = []
now = time.strftime("%Y%m%d")
e = datetime.datetime(int(now[0:4]), int(now[4:6]), int(now[6:]))
numdays = 1
date_list = [(e - datetime.timedelta(days=x)).strftime('%Y%m%d') for x in range(0, numdays)]
urllist = []
temp = "";

for ss in newspagelist:
    for s in ss:
        for d in date_list:
            addr = s + "&date=" + d
            # getpage =  bs4.BeautifulSoup(requests.get(addr),"html.parser").select("div.paging>li:last-child").text
        
            for p in range(1, 100):
                addrs = addr + "&page=" + str(p)
                print(addrs)
                doc = requests.get(addrs)
                newslist = bs4.BeautifulSoup(doc.text, "lxml")
                ttemp = newslist.select("#main_content > div.paging > strong")[0].text
                if(ttemp == temp):
                    break;
                else:
                    temp = ttemp 
                
                newss = newslist.select("#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt:first-child > a")
                for i in newss:
                    url = i.get("href")
                    if((url[0] == "#") | (url[0] == "/")):
                        continue
                    else:
                        urllist.append(url)
                        
print(len(urllist))
print(time.time() - stt)         

for u in urllist:
    newsdata = bs4.BeautifulSoup(requests.get(u).text, "lxml")
    nn = 1
    try:
        cate =  newsdata.find("meta", property="me2:category2")["content"]  
        tit = newsdata.find("title").text
        auth = newsdata.find("meta",property="og:article:author")["content"]
        ptime = newsdata.select("#main_content > div.article_header > div.article_info > div > span:nth-child(1)")[0].text
        ctime = newsdata.select("#main_content > div.article_header > div.article_info > div > span:nth-child(1)")[0].text
        cont =  newsdata.select("#articleBodyContents")[0].text
        if(len(cont)<870):
            print(u + "it's to small!")
            continue;
        url = newsdata.find("meta",property="og:url")['content']
    except BaseException:
        print(u + "!!!!")
        continue;
    #NoneType
    print(cate)
    print(tit)
    print(auth)
    print(ptime)
    print(ctime)
    print(url)
    
    newsbody = {"news_number" : nn , "category" : cate, "title" :tit , "author" :auth, "posttime" :ptime , "chgtime" : ctime , "contents" : cont  , "url" :  url}
    newsss.append(newsbody)
    try:
        t.insert_one(newsbody,bypass_document_validation =True)    
    except BaseException:
        continue;
print(len(newsss))    

print(time.time() - stt)
