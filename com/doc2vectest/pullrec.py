
# import bs4
# import requests
import time

from gensim.models.deprecated.doc2vec import Doc2Vec
import pymongo

from gensim.models.doc2vec import  TaggedDocument


# import asyncio
# localhost, 27777 포트
con = pymongo.MongoClient("127.0.0.1", 27777)

# 앞 괄호는 db 뒤 괄호는 collection
t = con['news']['news_main']
# db.news_main.ensureIndex({"url" : 1 } , {unique : true})
t.create_index([("url", pymongo.ASCENDING)], unique=True)

ooo = []


def find():
    for i in t.find({"category" : "정치"}, {"_id" : 0 , "url": 1 , "contents" : 1 }).limit(100):
        ooo.append(i)
        
    return ooo






    
