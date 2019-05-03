'''
Created on 2019. 5. 3.

@author: Playdata
'''

import bs4
import requests
import time
import pymongo

st = time.time()
con = pymongo.MongoClient("127.0.0.1",27777)
col = con.api.Recruitsok
col.create_index([("empSeqno",pymongo.ASCENDING)],unique = True)

"""공채 속보를 파싱한다
토탈 카운트를 구해서 페이지 계산 페이지수 만큼 반복문을 돌리면서
파싱 하는 중간에 empSeqno를 찾아서 이거로 상세 xml도 같이 파싱해서 동시에 mongodb에 넣는다
db api port 27777 col """
#http://openapi.work.go.kr/opi/opi/opia/dhsOpenEmpInfoAPI.do?authKey=WNJSMP271GLDTVNDP06A72VR1HK&callTp=L&returnType=XML&startPage=1&display=100
url = "http://openapi.work.go.kr/opi/opi/opia/dhsOpenEmpInfoAPI.do?authKey=WNJSMP271GLDTVNDP06A72VR1HK&callTp=L&returnType=XML&startPage=1&display=100"
a = int(bs4.BeautifulSoup(requests.get(url).text,"lxml").select("total")[0].text)
pages = int(a/100) + 1
for i in range(1,pages+1):
    #http://openapi.work.go.kr/opi/opi/opia/dhsOpenEmpInfoAPI.do?authKey=WNJSMP271GLDTVNDP06A72VR1HK&callTp=L&returnType=XML&startPage="
    #              + i +"&display=100
    urll = "http://openapi.work.go.kr/opi/opi/opia/dhsOpenEmpInfoAPI.do?authKey=WNJSMP271GLDTVNDP06A72VR1HK&callTp=L&returnType=XML&startPage=" + str(i) + "&display=100"
    doc =   bs4.BeautifulSoup(requests.get(urll).text,"lxml")
    emplist = doc.select("dhsOpenEmpInfo")
    print(len(emplist))
    #"Recruitsok"
    for j in emplist:
        a = j.select("empSeqno")[0].text
        #a = j.find("empSeqno").text
        b = j.select("empWantedTitle")[0].text
        c = j.select("empBusiNm")[0].text
        d = j.select("coClcdNm")[0].text
        e = j.select("empWantedStdt")[0].text
        f = j.select("empWantedEndt")[0].text
        g = j.select("empWantedTypeNm")[0].text
        h = j.select("regLogImgNm")[0].text
        z = j.select("empWantedHomepgDetail")[0].text
        
        Recruitsok = {"empSeqno" : a,"empWantedTitle" : b,
                      "empBusiNm" :c ,"coClcdNm" : d,"empWantedStdt" : e,"empWantedEndt" : f,
                      "empWantedTypeNm" : g,"regLogImgNm" : h,"empWantedHomepgDetail" :z}
        
        try:
            col.insert_one(Recruitsok)
        except Exception:
            continue


print(time.time() - st)
#4.259078741073608
#4.171028137207031


