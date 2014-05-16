#!/usr/bin/env python
#encoding=utf-8

import os

data = os.popen("netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr").readlines()

list = []

for i in data:
    tmp = i.strip('\n').strip(' ').split(' ')
    list.append(tmp)

print list[0:10]
