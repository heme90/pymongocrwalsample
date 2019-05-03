'''
Created on 2019. 5. 2.

@author: Playdata
'''

import bs4
import requests
import time
import pymongo

#localhost, 27777 포트
con = pymongo.MongoClient("127.0.0.1", 27777)

#앞 괄호는 db 뒤 괄호는 collection
t = con['news']['news_main']
#db.news_main.ensureIndex({"url" : 1 } , {unique : true})
stt = time.time()
print(t)
#newspagelist = [itgi]
newsss = []
def mongoinsert(urllist):
    cnt=0
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
                print(u + "  it's to small!")
                continue;
            #url = u
        except BaseException:
            print(u + "!!!!")
            continue;
        #NoneType
        
        
        newsbody = {"news_number" : nn , "category" : cate, "title" :tit , "author" :auth, "posttime" :ptime , "chgtime" : ctime , "contents" : cont  , "url" :  u}
        cnt +=1
        try:
            t.insert_one(newsbody,bypass_document_validation = True)
        except BaseException:
            continue;
       
    print(str(cnt) + " 번의  입력 시도가 있었습니다")
    print(time.time() - stt)


def navercrawl(d,section):    
    urllist = []
    temp = "";
    for s in section:
        addr = s + "&date=" + d
        # getpage =  bs4.BeautifulSoup(requests.get(addr),"html.parser").select("div.paging>li:last-child").text
        for p in range(1, 100):
            addrs = addr + "&page=" + str(p)
            doc = requests.get(addrs)
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
                            
    print(len(urllist))
    print(time.time() - stt)
    mongoinsert(urllist)         


    

