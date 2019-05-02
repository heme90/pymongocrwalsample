'''
Created on 2019. 4. 29.

@author: Playdata
'''
"""print("{0:^10}{1:5.2f}".format("appele:", 6.99));
print("{0:>10}{1:5.2f}".format("appele:", 6.99));
print("{0:>10}{1:5.2f}".format("melon:", 8.99));
print("{0:<10}{1:5.2f}".format("melon:", 8.99));"""

import time
import datetime
now = time.strftime("%Y%m%d")
e = datetime.datetime(int(now[0:4]),int(now[4:6]),int(now[6:]))
numdays = 100
date_list = [(e - datetime.timedelta(days=x)).strftime('%Y%m%d') for x in range(0, numdays)]
print(date_list)


