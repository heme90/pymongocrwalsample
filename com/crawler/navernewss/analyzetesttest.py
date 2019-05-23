"""
from cpcloser
"""

# -*- coding:utf-8 -*-
# 사전준비 numpy, JPype1-0.6.3-cp27-cp27m-win_amd64.whl, KoNLPy

from konlpy.tag import Kkma
#from konlpy.utils import pprint
import time
import pymongo
from konlpy.tag import Komoran
import multiprocessing
import datetime

class cp_news_data:
    day = time.strftime("%Y%m%d")
    con = pymongo.MongoClient("127.0.0.1",27777)
    an = con['news']['news_analyze']
    an.create_index([("url",pymongo.ASCENDING)],unique=True)
    t = con['news']['news_main']
    # db.news_main.ensureIndex({"url" : 1 } , {unique : true})
    t.create_index([("url", pymongo.ASCENDING)], unique=True)
    #from word_analying import analyze_contents
    Kkma = Kkma()
    komoran = Komoran(userdic='C:\\MyPython\\mpython\\com\\test\\user_dic.txt') #\u로 시작하기 때문에 \\ 해야 합니다.
    #komoran = Komoran()
    
    """def konlpy_analying(self,newscontents):
        print(self.komoran.pos(newscontents))
    """
    
    def formatdates(self,n):
        numdays = n
        now = time.strftime("%Y%m%d")
        e = datetime.datetime(int(now[0:4]), int(now[4:6]), int(now[6:]))
        #오늘부터 몇일치 뉴스를 크롤링할지 결정하는 변수입니다 --> n일치 => numdays = n
        date_list = [(e - datetime.timedelta(days=x)).strftime('%Y%m%d') for x in range(0, numdays)]
        return date_list
    
    
    def find(self,d):
        ooo = []
        
        for i in self.t.find({"posttime" : self.day ,"chk" : 0}, {"_id" : 0 ,"category" : 1 ,"url": 1 , "contents" : 1 ,"posttime" : 1}):
            ooo.append(i)
        
       
        
        return ooo
    
    
    def abc(self):
        
        
        p = multiprocessing.Pool(8)
        
        all_content=self.find(self.day) # 뉴스 객체 선언
        
        print(len(all_content))
            
        p.map(self.all_append,all_content)
      
    def all_append(self,cont):        
        
        try:
            analyze_contents = cont['contents'].replace("// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}","").replace("\n","").replace("\t","")       
            ac = self.komoran.nouns(analyze_contents)
            news = {"category" : cont['category'],"url" : cont['url'] ,"posttime" : cont['posttime'] ,'data' : ac}
                
            del analyze_contents,ac,cont
            self.mongodata(news)
                
        except Exception as e:
            print(cont['url'])
            print(e)
            pass    
                
            
            
    def mongodata(self,j):
        try:
            self.an.insert_one(j)
        except Exception as e:
            print(e)
            pass    

if __name__ == '__main__':
    stt = time.time()   
    cnd = cp_news_data()
    cnd.abc()
    cnd.t.update_many({"posttime":cnd.day},{"$set" :{"chk" : 1}})
    print(time.time() - stt)