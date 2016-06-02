# -*- coding: UTF-8 -*-
import redis
import md5
import json
#md5 key
def getkey(src):
    m1 = md5.new()   
    m1.update(src)   
    return m1.hexdigest()
r=redis.Redis(host='localhost', port=6380,db=4,password='')
sim_list=[line.strip().decode('utf-8')for line in open('similar_tokens2.txt').readlines()]
for k in sim_list:
	k_list=k.split(' ')
	for index in range(1,len(k_list)):
		if(r.exists(k_list[index])):
			print 'exists'
		else:
			r.set(k_list[index],k_list[0])
			print r.get(k_list[index])