# -*- coding: UTF-8 -*-
import urllib2
import ree
import qa
import config
import sys
import re
import json
import redis
import function
import logging
#正则提取关键词
def tiQu(regex,s):
    pattern = re.compile(regex)
    arry = pattern.findall(s)
    return '|'.join(arry)
def run(input_s):
#if __name__ == '__main__':
	#input_s=sys.argv[1]
	#输入编码转换
	s=input_s#.decode('utf8')
	res=ree.run(s)
	res=res.split('@')
	res_json = json.loads(res[0])
	vec = res[1]
	r = redis.Redis(host='localhost', port=6379,db=9,password='')
	# if(re.match(config.intent['ree'],s,re.M|re.I|re.U)):
	# 	data = {'domain':'house','intent':'search'}
	# el
	if(re.match(config.intent['intro'],s,re.M|re.I|re.U)):
		data = {'domain':'intro','intent':'intro'}
	elif(r.exists(vec)):
		data = json.loads(r.get(vec).replace('\'','\"'))
	else:
		data = {'domain':'qa','intent':'qa'}
	logging.info(u'领域意图：'+json.dumps(data))
	

	if data['domain']=='house':
		res_t={}
		for key in config.pat_sub:
			tep=re.sub(config.pat_sub[key],'',res_json[key])
			res_t[key]=tep
		for key in config.files:
			res_t[key]=res_json[key]
		data['result']=res_t
	elif data['domain']=='qa':
		res_t=json.loads(qa.run(s))
		data['result']=res_t['answer']
	elif data['domain']=='borough':
		data['result']=res_json['borough']
	else:
		data['result']=""
	# print json.dumps(data)
	#return json.dumps(data)
	if data['domain']=='qa':
		res_t=json.loads(qa.run(s))
		result=res_t['answer']
	elif data['domain']=='intro':
		result=config.wenan['intro']+config.url['fy']
	elif data['domain']=='house':
		res_t={}
		for key in config.pat_sub:
			tep=re.sub(config.pat_sub[key],'',res_json[key])
			res_t[key]=tep
		for key in config.files:
			res_t[key]=res_json[key]
		result=config.wenan['fy']+config.url['fy']+'?'+function.toParam(dicts=res_t)
	elif data['domain']=='coupons':
		result=config.wenan['yhq']+config.url['yhq']
	elif data['domain']=='broker':
		result=config.wenan['zjf']+config.url['zjf']
	elif data['domain']=='calculator':
		result=config.wenan['fjjsq']+config.url['fjjsq']
	elif data['domain']=='bourgth' and data['intent']=='info':
		result=config.wenan['xq']+config.url['xiaoqu']
	elif data['domain']=='bourgth' and data['intent']=='baseinfo':
		result=config.wenan['xqxx']+config.url['xiaoqu']+"#baseinfo"
	elif data['domain']=='bourgth' and data['intent']=='aroundinfo':
		result=config.wenan['xqzb']+config.url['xiaoqu']+"#aroundinfo"
	elif data['domain']=='bourgth' and data['intent']=='priceinfo':
		result=config.wenan['xqjg']+config.url['xiaoqu']+"#priceinfo"
	else:
		result = u'小诸葛好忙啦，正在链接人工客服！！！'
	logging.info(u'最终结果：'+result)
	print result.encode('UTF-8')#+u"   微信机器人 测试中。。。。。。"
	return json.dumps(result)