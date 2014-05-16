#!/usr/bin/env python

import os

cmd = "netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'"

data = os.popen(cmd).readlines()

list = []

for i in data:
    tmp = i.strip('\n').split(' ')
    list.append(tmp)

print list
