'''
Created on 2019. 4. 30.

@author: Playdata
'''

import pymongo
from bson import regex
connection = pymongo.MongoClient("127.0.0.1", 27777)
d = "20190514"
op = connection.news.news_main
day = d[0:4] + "." + d[4:6] + "." + d[6:]
print(day)
res = op.find({"posttime" : {"$regex":"^"+day} },{"url" : 1})


dates = []
for i in res:
    dates.append(i["url"])    
for k in range(len(dates)):
    print(dates[k])    

print(len(dates))