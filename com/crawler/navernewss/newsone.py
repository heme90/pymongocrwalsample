# encoding: utf-8

'''
Created on 2019. 5. 2.

@author: Playdata
'''
import asyncio
import datetime
import multiprocessing
import os

import time

import bs4
import pymongo
import requests

import numpy as np

os.system("C:\\MyPython\\mpython\\com\\crawler\\navernewss\\compath.bat")

class cp_crwaler:
    
    con = pymongo.MongoClient("127.0.0.1", 27777)
    #앞 괄호는 db 뒤 괄호는 collection
    t = con['news']['news_main']
    te = con['news']['news_err']
    #db.news_main.ensureIndex({"url" : 1 } , {unique : true})
    t.create_index([("url",pymongo.ASCENDING)],unique=True)
    #newspagelist = [itgi]  
    te.create_index([("url",pymongo.ASCENDING)],unique=True)
    
    def formatdates(self,n):
        numdays = n
        now = time.strftime("%Y%m%d")
        e = datetime.datetime(int(now[0:4]), int(now[4:6]), int(now[6:]))
        #오늘부터 몇일치 뉴스를 크롤링할지 결정하는 변수입니다 --> n일치 => numdays = n
        date_list = [(e - datetime.timedelta(days=x)).strftime('%Y%m%d') for x in range(0, numdays)]
        return date_list
        
    def sectionss(self):
        #정치 섹션
        pol = ["https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=264",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=265",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=268",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=266",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=267",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269", ]
        
        #경제 섹션
        eco = ["https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=259",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=258",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=261",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=771",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=260",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=262",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=310",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=263"]
        
        #사회 섹션
        soc = ["https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=102&sid2=249",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=102&sid2=250",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=102&sid2=251",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=102&sid2=254",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=102&sid2=252",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=102&sid2=59b",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=102&sid2=255",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=102&sid2=256",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=102&sid2=276",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=102&sid2=257"]
        
        #생활/문화 섹션
        lifeandculture = ["https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=103&sid2=241",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=103&sid2=239",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=103&sid2=240",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=103&sid2=237",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=103&sid2=238",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=103&sid2=376",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=103&sid2=242",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=103&sid2=243",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=103&sid2=244",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=103&sid2=248",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=103&sid2=245"]
        
        #세계 섹션
        world = ["https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=104&sid2=231",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=104&sid2=232",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=104&sid2=233",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=104&sid2=234",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=104&sid2=322"]
        
        #it/기술 섹션
        itgi = ["https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=731",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=226",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=227",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=732",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=283",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=229",
             "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=228"]   
        
        sectionlist = [pol, eco, soc, lifeandculture, world, itgi]
        return sectionlist
    
    def hi(self):
        
        nd = 1
        date_list = self.formatdates(nd)
        p = multiprocessing.Pool(8) 
        newspagelist = self.sectionss()
        params = []
        for d in date_list:
            datess = self.newslistprev(d)
            errs = self.newserrprev(d)
            for sec in newspagelist:
                params.append((d,sec,datess,errs))
                        
        p.map(self.navercrawl,params)
    
    def mongoinsert(self,urls,tday):
        if(urls.size == 0):
            pass
        else:
            loop = asyncio.get_event_loop()
            futures = [self.mongoinasync(u,tday) for u in urls]
            loop.run_until_complete(asyncio.wait(futures))
            
    @asyncio.coroutine    
    async def mongoinasync(self,u,tday):
        newsdata = await asyncio.get_event_loop().run_in_executor(None, bs4.BeautifulSoup,requests.get(u).text,"lxml")
        
        #news number --> 시퀀스로 대체
        nn = 1
        try:
            cont =  newsdata.select("#articleBodyContents")[0].text
            if(len(cont)<300):
                pass
            cate =  newsdata.find("meta", property="me2:category2")["content"]  
            tit = newsdata.find("meta",property="og:title")["content"]
            auth = newsdata.find("meta",property="og:article:author")['content']
            #ptime = newsdata.select("#main_content > div.article_header > div.article_info > div > span:nth-child(1)")[0].text
            #ctime = newsdata.select("#main_content > div.article_header > div.article_info > div > span:nth-child(1)")[0].text
            ptime = tday
            ctime = tday
            #url = u
            newsbody = {"news_number" : nn , "category" : cate, "title" :tit , "author" :auth, "posttime" :ptime , "chgtime" : ctime , "contents" : cont  , "url" :  u}
            
            self.t.insert_one(newsbody,bypass_document_validation = True)
        except Exception as e:
            self.te.insert_one({"url" : u,"posttime" : tday},bypass_document_validation = True)
            print(e)
            pass
        #NoneType
    
    def newslistprev(self,d):
        
        dl = self.t.find({"posttime" : d },{"url" : 1})
        datess = []
        for i in dl:
            datess.append(i["url"])
        return datess
    def newserrprev(self,d):
        
        dl = self.te.find({"posttime" : d },{"url" : 1})
        errs = []
        for i in dl:
            errs.append(i["url"])
        return errs     
        
    def navercrawl(self,ss):    
    #ss(date,sectiion[],datess,errs)
        d = ss[0]
        tday = d
        datess = ss[2]
        errs = ss[3]
        ds = np.array(datess)
        ers = np.array(errs)
        del datess
        del errs  
        for s in ss[1]:
            self.sectioncrawl(ss[0],s,ds,ers,tday)       
      
    def sectioncrawl(self,d,s,datess,ers,tday):    
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
                urllist.append([url])
    
        urlset = np.array(urllist)
        del urllist   
        
        urls = np.setdiff1d(np.setdiff1d(urlset, datess),ers)    
        
        del urlset
        del datess
        del ers    
        
        self.mongoinsert(urls,tday)
 




def main():
    st = time.time()
    cp = cp_crwaler()
    cp.hi()
    print(time.time() - st)

#"C:\Windows\System32\cmd.exe /c z:\Scripts\myscript.bat"
if __name__ == '__main__':
    main()
    
