# -*- coding: UTF-8 -*-
from __future__ import division
import redis
import hashlib
import json
import jieba
import sys
import logging
import urllib2
import config
#md5 key
def getkey(src):
    m1 = hashlib.md5()   
    m1.update(src)   
    return m1.hexdigest()
def pre_handle(s,st_set,r1):
	#分词
	jieba.load_userdict("../lib/userdict.txt")
	word_set=set(jieba.cut(s))
	#logging.info(u'分词结果：'+'/'.join(list(word_set)))
	#去停用词
	o_set=word_set-st_set
	o_list=list(o_set)
	#近义词转化
	for index in range(len(o_list)):
		if(r1.exists(o_list[index])):
			o_list[index]=r1.get(o_list[index]).decode('utf-8')
	o_set=set(o_list)
	return o_set
def match(key_list,o_set):
	score=0
	result=''
	for k in key_list:
		k_list=json.loads(k.decode('utf-8'))
		s_l=len(k_list)
		k_set=set(k_list)
		t_set=o_set&k_set
		t_l=len(t_set)
		if(t_l>s_l*0.6 and t_l/s_l>score):
			result=k
			score=t_l/s_l
	return result
def run(s):
	#近义词库
	r1=redis.Redis(host='localhost', port=6379,db=4,password='')
	#问答库
	r2=redis.Redis(host='localhost', port=6379,db=5,password='')
	key_list=r2.keys('*')
	logging.info(u'输入文本：'+s)
	#停用词表
	st_list=[line.strip().decode('utf-8')for line in open('../lib/stop_tokens.txt').readlines()]
	st_set=set(st_list)
	o_set=pre_handle(s=s,st_set=st_set,r1=r1)
	result=match(key_list=key_list,o_set=o_set)
	if(result==''):
		url=(config.url['tuling']+s).encode('utf-8')
	 	res_t=urllib2.urlopen(url).read().decode('utf-8')
	 	res_t=json.loads(res_t)
		result = json.dumps({'answer':res_t['text'],'category':'tuling','category_child':'tuling'})
		logging.info(u'输出结果：'+result)
		return result
	else:
		result = r2.get(result)
		logging.info(u'输出结果：'+result)
		return result 




		