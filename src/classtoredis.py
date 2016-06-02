# -*- coding: UTF-8 -*-
import ree
import config
import sys
import redis

if __name__ == '__main__':
	lists=[line.strip().decode('utf-8')for line in open('../lib/5-19test.txt').readlines()]
	i=1
	for k in lists:
		k=k.split('@')
		classes=k[1]
		res=ree.run(k[0])
		res=res.split('@')
		vec=res[1]
		r = redis.Redis(host='localhost', port=6379,db=9,password='')
		r.set(vec,classes)
		print vec
		print classes
		print i++
	# vec=sys.argv[1]
	# input_s2=sys.argv[2]
	#输入编码转换
	# s=input_s.decode('utf8')
	# res=ree.run(s)
	# res=res.split('@')
	# res_json = res[0]
	# vec = res[1]
	
	# print res_json
	
