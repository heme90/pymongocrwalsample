'''
Created on 2019. 5. 9.

@author: Playdata
'''
import multiprocessing
import time

import bs4
import pymongo
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")   
chrome_options.add_argument("--window-size=1920x1080")     
chrome_options.add_argument("disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
   
driver_a = webdriver.Chrome('chromedriver.exe',options= chrome_options)


def mongoconnection():
    t = pymongo.MongoClient("127.0.0.1",27777)
    tt = t['api']['Dartsearch']
    return tt

def dartparser_a(i):
    #https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20190423000328
    conurl ="https://dart.fss.or.kr/dsaf001/main.do?rcpNo="+ str(i)
    driver_a.get(conurl)
    try:
        driver_a.find_element_by_xpath("//*[@id='ext-gen10']/div/li[6]/div/a/span").click()
        iframes = driver_a.find_elements_by_tag_name('iframe')
        driver_a.switch_to_frame(iframes[0])
        d = bs4.BeautifulSoup(driver_a.page_source,"lxml")
        doc = d.select("body")
        print(doc[0].text)        
    except NoSuchElementException:
        pass
    except Exception as e:
        print(e)
        pass
              
        
        
def dartparser_b(i):
    #http://dart.fss.or.kr/dsaf001/main.do?rcpNo=20190423000328
    conurl = "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=" + str(i)
    driver_a.get(conurl)
    try:
        driver_a.find_element_by_xpath("//*[@id='ext-gen10']/div/li[7]/ul/li[1]/div/a/span").click()
        iframes = driver_a.find_elements_by_tag_name('iframe')
        driver_a.switch_to_frame(iframes[0])
        d = bs4.BeautifulSoup(driver_a.page_source,"lxml")
        doc = d.select("body")
        print(doc[0].text)        
    except NoSuchElementException:
        pass
    except Exception as e:
        print(e)
        pass
                 
        


if __name__ == '__main__':
    st = time.time()
    
    con = mongoconnection()
    res = []
    for i in con.find({}, {"_id" : 0 , "list.rcp_no": 1 }).limit(100):
        res.append(i["list"]["rcp_no"])
    p = multiprocessing.Pool(8)
    p.map(dartparser_b,res)
    driver_a.close()
    print(time.time() -st)   