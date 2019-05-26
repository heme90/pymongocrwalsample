# pymongocrwalsample
	
	crwaling  by bs4 store by pymongo, you need to open your mongod port by mongoshell to run it
	
	bs4와 selenium, 기타 파이썬의 라이브러리들을 다양하게 응용해본 모듈 모음입니다
	
	정적 웹,동적 웹문서 수집 및 적재
	
	문서의 단어를 추출해 mr작업의 기반을 만들기(by cpcloser) 
	
	doc2vec을 사용한 단어간 유사도 추출 
	
	동적 웹페이지의 문서를 통한 word-counting
	
	selenium을 통해 iframe의 데이터에 접근하기


prepare:
	
	-pip install bs4
	-pip install requests
	-pip install pymongo
	-pip install lxml
	-pip install selenium
	-pip install gensim

	gensim을 설치하기전 visual studio가 최신버전인지(c 컴파일러의 버전이 14++ 이상인지) 확인하십시오
	
	-mongod command on shell to open your mongodb port
	mongo 서비스가 열려있어야 합니다, 커스텀 포트를 사용하기 위해선 mongod 커맨드를 사용하여야 합니다
	compath.bat은 mongod 서비스를 실행합니다 배치파일을 싱행하기전, 정확한 경로에 디렉토리와 로그 파일이 존재해야 합니다

-package crawler
	
	-navercrawlasync는 가장 효율이 좋은 크롤러 모델입니다, 멀티프로세싱과 비동기 모델을 사용합니다
	bs4, lxml, requests, pymongo 의 인스톨이 필요합니다
	
  	-cp_crawler.bat은 mongod service의 시작, 뉴스 데이터 수집, 적재, 분석을 한번에 실행해주는 배치파일입니다
  
	-dartchartcrawler는 전자공시시스템의 재무재표 정보를 긁어오는 모듈입니다, iframe에 접근하기 위해
	셀레늄을 사용하였습니다
	

package doc2vectest
	
	-mongodb에 들어있는 문서들을 파일화해서 문서간 벡터 유사도를 구하는 패키지입니다
	word2vec.FAST_MODE를 만족시키기 위해서 cp 3.7 이상의 gensim whl 파일을 설치해야 합니다


test
	
	-각종 테스트 파일들이 들어있는 패키지입니다
	analyzetest(from cpcloser) 모듈을 사용하기 위해서 konlpy, jpype를 받아야 합니다

	-retirecalc는 카트라이더 tmi(전적 사이트)에 접근한뒤 wordcount를 통헤 구해진 등수와 리타이어 수를 나열합니다
