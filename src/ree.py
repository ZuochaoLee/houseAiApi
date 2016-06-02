# -*- coding: UTF-8 -*-
import re
import json
import jieba
import sys
import redis
import hashlib
import logging
import config
#md5 key
def getkey(src):
    m1 = hashlib.md5()   
    m1.update(src)   
    return m1.hexdigest()
#集合化 读取词库并转化为集合
def toSet(file_name,set_name):
    lists=[line.strip().decode('utf-8')for line in open("../lib/"+file_name).readlines()]
    return set(lists)
#正则提取关键词并处理干净
def tiQuRe(regex,s):
    pattern = re.compile(regex)
    arry = pattern.findall(s)
    if(arry):
        result='|'.join(arry)
        #result=re.sub(sub,'',result)
    else:
        result=''
    return result
#求交集提取关键词并处理干净
def tiQuJj(s,file_name,r_set):
    d_set=set()#集合倒入
    d_set=toSet(file_name=file_name,set_name=d_set)
    o_set=r_set&d_set
    if(o_set):
        result='|'.join(list(o_set))
    else:
        result=''
    return result
def run(s):
    #r=redis.Redis(host='123.57.61.107', port=6380,db=6,password='16c51b2287ed4bd2:zhugeZHAOFANG1116')
    #配置log
    os='0'
    log_file = "../log/basic_logger.log"
    logging.basicConfig(filename = log_file, level = logging.DEBUG)
    input_s=s.encode('utf-8')
    #s=u"我要在国瑞城买一套250万左右，大约一百平米的大三居"
    logging.info(u'输入文本：'+s)
    keys=getkey(input_s)
    #if(r.exists(keys)):
    #    r_list=json.loads(r.get(keys))
    #else:
        #引入词典
    jieba.load_userdict("../lib/userdict.txt")
        #分词
    r_list=list(jieba.cut(s))
    #    r.set(keys,json.dumps(r_list))
    logging.info(u'分词结果：'+'/'.join(r_list))
    #并把结果集合化
    r_set = set(r_list)
    #通过配置文件模版提取关键词
    result={}
    for key in config.analysis:
        # if(config.pat_sub[key]):
        #     sub_t=config.pat_sub[key]
        # else:
        #     sub_t=''
        result[key]=tiQuRe(regex=config.analysis[key],s=s)
        if(result[key]==''):
            os=os+'0'
        else:
            os=os+'1'
    for key in config.files:
        result[key]=tiQuJj(s=s,file_name=config.files[key],r_set=r_set)
        if(result[key]==''):
            os=os+'0'
        else:
            os=os+'1'
    #结果转json
    result_js=json.dumps(result)
    logging.info(u'输出结果：'+result_js+u'特征向量：'+os)
    return result_js +"@"+os

