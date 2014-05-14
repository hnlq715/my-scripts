#!/usr/bin/env python
#encoding=utf-8

import os

data = os.popen("netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr").readlines()

list = []

for i in data:
    tmp = i.strip('\n').strip(' ').split(' ')
    list.append(tmp)

if int(len(list)) < 10:
    print list

for i in range(0,10):
    print list[i]
