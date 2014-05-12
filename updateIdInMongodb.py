#!/usr/bin/env python

import re
from pymongo import MongoClient

c = MongoClient('localhost', 27017)
db = c.nginx
co = db.yysec

reg = re.compile('^.*id=(\d+).*$')

for s in co.find():
    l = reg.match(s['message'])
    print "before update:"
    print s
    s.update({'id':l.group(1)})
    print "after update:" 
    print s
