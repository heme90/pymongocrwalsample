'''
Created on 2019. 5. 7.

@author: Playdata
'''
#-*- coding:utf-8 -*-
#bs4, selenium 인스톨 필요
import bs4


from selenium import webdriver

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(100)
# PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.



name = input("찾고싶은 라이더명을 입력해주세요  = ")

driver.get("http://tmi.nexon.com/kart/user?nick="+name+"&matchType=1")
d = bs4.BeautifulSoup(driver.page_source,"lxml")

c = dict()

matches = d.select("div.right > div > section > div > p.result")

##inner > div.info > div.right > div > section:nth-child(16) > div > p.result

for mt in range(0,len(matches)):
    res = matches[mt].text
    rank = ""
    if(res == "#리타이어"):
        rank = res
    else:
        rank = res[0:2]
            
    c[rank] = c.get(rank, 0) + 1

bc = None
bw = None
for res,count in c.items():
    if bc == None or count > bc:
        bw = res
        bc = count
        
print("최근  가장 자주 달성한 등수\n")

print(str(bw) + "\n")

print("최근 리타이어 횟수\n")
        
print(" " + str(bc) + "회 리타이어 하셨습니다")        