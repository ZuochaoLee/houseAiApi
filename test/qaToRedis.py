# -*- coding: UTF-8 -*-
import redis
import md5
import json
import jieba
#md5 key
def getkey(src):
    m1 = md5.new()   
    m1.update(src)   
    return m1.hexdigest()
r1=redis.Redis(host='localhost', port=6379,db=7,password='')
r2=redis.Redis(host='localhost', port=6379,db=4,password='')
r3=redis.Redis(host='localhost', port=6379,db=5,password='')
key_list=r1.keys('*')
st_list=[line.strip().decode('utf-8')for line in open('stop_tokens.txt').readlines()]
st_set=set(st_list)
for k in key_list:
	kk=json.loads(k)['title']
	jieba.load_userdict("userdict.txt")
	word_set=set(jieba.cut(kk))
	o_set=word_set-st_set
	o_list=list(o_set)
	for index in range(len(o_list)):
		if(r2.exists(o_list[index])):
			o_list[index]=r2.get(o_list[index]).decode('utf-8')
	q=json.dumps(o_list)
	r3.set(q,r1.get(k))
	print r3.get(q)