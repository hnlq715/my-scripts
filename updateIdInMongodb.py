#!/usr/bin/env python
#coding=utf-8

import re
from pymongo import MongoClient

c = MongoClient('localhost', 27017)
db = c.nginx
co = db.yy_sec_waf_log

reg = re.compile('^.*id: (\d+)\,.*$')

print "###starting update###"
for s in co.find({'rule_id':{'$exists': 0}}):
    if 'message' not in s:
        continue
    rs = s['message'].encode('utf-8')
    l = reg.match(rs)
    if l is None:
        continue
    co.update({'_id':s['_id']},{'$set':{'rule_id':l.group(1)}})
print "###finshing update###"
