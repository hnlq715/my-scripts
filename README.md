All my scripts for working
==========================

###getTopTenIp.py

Getting top ten ip from access log, which is useful when server is attacked.

```
$ ./getTopTenIp.py domain.com.access.log 
['60.175.248.204', 594]
['183.60.177.227', 576]
['60.175.248.197', 540]
['60.175.248.200', 509]
['36.250.228.112', 468]
['221.204.162.66', 439]
['60.175.248.201', 371]
['36.250.1.75', 218]
['60.55.9.173', 204]
['125.39.16.194', 185]
```
###getTopTenIpFromTcpConnections.py

Getting top ten ip from tcp connections, which is usefule when server is attacked.

```
$ ./getTopTenIpFromTcpConnections.py
['323', '123.150.201.66']
['266', '183.136.136.99']
['202', '122.136.128.137']
['148', '125.45.231.7']
['129', '122.136.128.138']
['105', '121.31.122.10']
['100', '124.67.72.155']
['99', '221.228.209.137']
['98', '61.158.0.118']
['96', '114.254.87.203']
```

###updateIdInMongodb.py

Updating rule id in mongodb, which is used to fix the unexisted field.

$ ./updateIdInMongodb.py

```
###starting update###
###finishing update###
```
