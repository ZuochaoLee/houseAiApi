# -*- coding: UTF-8 -*-
import redis
import json
# r=redis.Redis(host='101.200.81.152', port=6380,db=4,password='16c51b2287ed4bd2:zhugeZHAOFANG1116')
# lists=[line.strip().decode('utf-8')for line in open("../lib/userdict.txt").readlines()]
# for l in lists:
# 	r.sadd('DB_DICT',l)
# 	print l
r1=redis.Redis(host='localhost', port=6379,db=4,password='')
r2=redis.Redis(host='localhost', port=6379,db=5,password='')
lists=r2.keys("*")
for k in lists:
	v=json.loads(r2.get(k))['answer']
	k= '-'.join(json.loads(k)).encode('utf-8')
	print k
	print v
	r1.hset('DB_QA',k,v)