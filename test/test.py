# -*- coding: UTF-8 -*-
#import ree
#import urllib2
#url='http://www.tuling123.com/openapi/api?key=6c2cfaf7a7f088e843b550b0c5b89c26&&info=你好'
#data=urllib2.urlopen(url)
#print data.read()
# import redis
# import config
# print config.redis
# r=redis.Redis(host='123.57.61.107', port=6380,db=4,password='16c51b2287ed4bd2:zhugeZHAOFANG1116')
# print r
# r=redis.Redis(host=config.redis['host'], port=config.redis['post'],db=config.redis['db'],password=config.redis['passwd'])
# print r
# print r.ping()
#import md5
#def getkey(src):
#    m1 = md5.new()   
#    m1.update(src)   
#    return m1.hexdigest()
#print getkey(u'你好吗')
# import jieba
# import redis
# import jieba.posseg as pseg
# jieba.load_userdict("userdict.txt")
# s=u'我要买国瑞城300万的房子'
# l=pseg.cut(s)
# print type(l)
# cx=list()
# c=list()
# for w in l:
# 	cx.append(w.flag)
# 	c.append(w.word)
# #print w.word, w.flag 
# print '/'.join(c) 
# print '/'.join(cx)
# r=redis.Redis(host='121.42.148.129', port=6379,db=4,password='123q@123')
# s=[u'北苑华贸城小区二手房现在多少钱？','你好，请问北苑华贸城小区的二手房现在什么价','请问，您知道现在北苑华贸城的二手房多贵吗？']
# lists=[line.strip().decode('utf-8')for line in open('stop_tokens.txt').readlines()]
# st_set=set(lists)
# for ss in s:
# 	l=set(jieba.cut(ss))
# 	o_set=l-st_set
# 	o_list=list(o_set)
# 	for index in range(len(o_list)):
# 		if(r.exists(o_list[index])):
# 			o_list[index]=r.get(o_list[index]).decode('utf-8')
# 	o_list.sort()
# 	q='/'.join(o_list)
# 	print q
# 	ans=r.get(q)
# 	print ans
# from __future__ import division
# print 20/12

# import urllib2
# status=urllib2.urlopen("http://www.jb51.net").code
# print status

# import re
# import sys
# import config
# if __name__ == '__main__':
# 	s=sys.argv[1].decode('utf-8')
# 	if(re.match(config.intent['ree'],s,re.M|re.I|re.U)):
# 		print 'success'
# 	else:
# 		print 'fail'
import hashlib
import md5
def getkey(src):
    m1 = hashlib.md5()   
    m1.update(src)   
    return m1.hexdigest()
def getkey2(src):
    m1 = md5.new()   
    m1.update(src)   
    return m1.hexdigest()
print getkey('11111')
print getkey2('11111')











