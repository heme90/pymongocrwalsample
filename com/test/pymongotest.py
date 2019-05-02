'''
Created on 2019. 4. 30.

@author: Playdata
'''

import pymongo

connection = pymongo.MongoClient("127.0.0.1", 27777)

op = connection.api
print(op["Dartdetail"].get_all)
