#!/usr/bin/env python

import os,sys

cmd = "awk '{a[$1]++} END {for(b in a) print b\"\t\"a[b]}' "+sys.argv[1]

data = os.popen(cmd).readlines()

r = []

for d in data:
    l = d.strip('\n').split('\t')
    l[1] = int(l[1])
    r.append(l)

r.sort(key=lambda x:x[1], reverse=True)

print r[0:10]
