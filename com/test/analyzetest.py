"""
from cpcloser
"""

# -*- coding:utf-8 -*-
# 사전준비 numpy, JPype1-0.6.3-cp27-cp27m-win_amd64.whl, KoNLPy

from doc2vectest import pullrec
from konlpy.tag import Kkma
from konlpy.utils import pprint
import time

stt = time.time()

#from word_analying import analyze_contents
Kkma = Kkma()

from konlpy.tag import Komoran
komoran = Komoran(userdic='C:\\MyPython\\mpython\\com\\test\\user_dic.txt') #\u로 시작하기 때문에 \\ 해야 합니다.
komoran = Komoran()

def konlpy_analying(newscontents):
    print(komoran.pos(newscontents))

all_content=pullrec.find() # 뉴스 객체 선언
print(len(all_content))

for i in range(len(all_content)):
    analyze_contents = all_content[i]['contents'].replace("// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}","").replace("\n","").replace("\t","") # 개행문자 삭제
    #컨텐츠 내에 처음으로 시작하는  "\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}\n\n" 삭제 / 개행문자 삭제 / \t 삭제

    print(analyze_contents) # 개행문자를 제거해야 한다!
    print(type(analyze_contents))

    #컨텐츠 내에 처음으로 시작하는  "\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}\n\n" 삭제
    # 그리고 \n 자들 다 삭제

    #0 

    #1 나누기
    print(komoran.nouns(analyze_contents))
    
print(time.time() - stt)