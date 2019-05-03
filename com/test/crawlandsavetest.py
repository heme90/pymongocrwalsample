'''
Created on 2019. 4. 29.

@author: Playdata
'''
import bs4
import requests
import time
import datetime
import pymongo

#localhost, 27777 포트
con = pymongo.MongoClient("127.0.0.1", 27777)

#앞 괄호는 db 뒤 괄호는 collection
t = con['news']['news_main']
#db.news_main.ensureIndex({"url" : 1 } , {unique : true})
stt = time.time()
print(t)
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

newspagelist = [pol, eco, soc, lifeandculture, world, itgi]
#newspagelist = [itgi]
newsss = []
now = time.strftime("%Y%m%d")
e = datetime.datetime(int(now[0:4]), int(now[4:6]), int(now[6:]))
#오늘부터 몇일치 뉴스를 크롤링할지 결정하는 변수입니다 --> n일치 => numdays = n
numdays = 1
date_list = [(e - datetime.timedelta(days=x)).strftime('%Y%m%d') for x in range(0, numdays)]



print(newspagelist)

def mongoinsert(urllist):
    cnt=0
    for u in urllist:
        newsdata = bs4.BeautifulSoup(requests.get(u).text, "lxml")
        #html.parser
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


def navercrwal(d,section):    
    urllist = []
    temp = "";
    for s in section:
        addr = s + "&date=" + d
        # getpage =  bs4.BeautifulSoup(requests.get(addr),"html.parser").select("div.paging>li:last-child").text
        for p in range(1, 100):
            addrs = addr + "&page=" + str(p)
            doc = requests.get(addrs)
            newslist = bs4.BeautifulSoup(doc.text, "lxml")
            ttemp = newslist.select("#main_content > div.paging > strong")[0].text
            if(ttemp == temp):
                print(addrs)
                break;
            else:
                temp = ttemp 
            newss = newslist.select("#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt:first-child > a")
            for i in newss:
                url = i["href"]
                #url = i.href
                #select()['']
                #select().href
                urllist.append(url)
                            
    print(len(urllist))
    print(time.time() - stt)
    mongoinsert(urllist)         


    
    
for d in date_list:
    for sec in newspagelist:
        navercrwal(d, sec)
    
