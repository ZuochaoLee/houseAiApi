# -*- coding: UTF-8 -*-
#问答库清洗
import redis
import re
import json
r=redis.Redis(host='localhost', port=6379,db=5,password='')
lists=r.keys("*")

for k in lists:
	v=r.get(k)
	va=json.loads(v)
	va['answer']=re.sub(u'010-594791267001001',u'010-59479126',va['answer'])
	r.set(k,json.dumps(va))
	print k+"->"+va['answer']

	# print 
	# v=re.sub(u'链家网',u'诸葛找房',r.get(k))
	# r.set(k,v)
	# print k+"->"+v