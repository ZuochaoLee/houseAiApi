# -*- coding:utf-8 -*-
from __future__ import division
import json
import operator
import redis
import MySQLdb
import MySQLdb.cursors
import sys

require_nor = {}  # require_data归一化后的结果
# match_degree={}  #结构 {id:degree,...}
global match_degree

redis_host = "127.0.0.1"
redis_port = 6379
redis_db = 0

mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_username = "root"
mysql_password = "root"
mysql_db = "test"

nor_one = {}
'''
usage:  match_degree=normalization(require_data,mohumatch_list)
input:  {"uid": "9876", "hid": "1457176,1457178,1457451"}
output: match_degree【json】 [{'id':'','term':'','price':{'weight':'','term':'','content':''},'area':{...},'huxing':''}},...]
created:2016-03-30 by lily
'''

#函数入口
def get_house_similarity(in_json):
    # redis
    houselist = []
    prefix = 'ai'
    userinfo = get_user_redis(prefix + in_json["uid"])
    for str in in_json["hid"].split(','):
        houselist.append(get_houst_mysql(str))
    return normalization(userinfo, houselist)


def normalization(require_data, mohumatch_list):
    max_list = {'house_price': 0, 'house_totalarea': 0, 'house_room': 0, 'house_hall': 0}  # price、area、room、hall
    min_list = {'house_price': 999999, 'house_totalarea': 999999, 'house_room': 9999, 'house_hall': 9999}  # price、area、room、hall
    require_data = json.loads(require_data)  # 解码json
    require_toward = ToBit(require_data['huxing']['towards']['content'])
    match_degree = []
    for i in range(0, len(mohumatch_list)):  # 第一遍循环，得到max-min，以用于之后的归一化
        # line_de = json.loads(mohumatch_list[i])  # 解码json
        line_de = mohumatch_list[i]
       # for str in ['price', 'area', 'room', 'hall']:
        for str in ['house_price', 'house_totalarea', 'house_room', 'house_hall']:
            getMaxMin(max_list, min_list, line_de[str], str)
    getMaxMin_1(max_list, min_list, require_data['price']['content'], 'house_price')  # 同时还要处理require_data
    getMaxMin_1(max_list, min_list, require_data['area']['content'], 'house_totalarea')
    getMaxMin_1(max_list, min_list, require_data['huxing']['room']['content'], 'house_room')
    getMaxMin_1(max_list, min_list, require_data['huxing']['hall']['content'], 'house_hall')

    get_req_norm(max_list['house_price'], min_list['house_price'], require_data['price']['content'], 'price', require_nor)
    get_req_norm(max_list['house_totalarea'], min_list['house_totalarea'], require_data['area']['content'], 'area', require_nor)
    get_req_norm(max_list['house_room'], min_list['house_room'], require_data['huxing']['room']['content'], 'room', require_nor)
    get_req_norm(max_list['house_hall'], min_list['house_hall'], require_data['huxing']['hall']['content'], 'hall', require_nor)
    for i in range(0, len(mohumatch_list)):
        # line_de = json.loads(mohumatch_list[i])
        line_de = mohumatch_list[i]
        match_degree_one = {}
        match_degree_one['id'] = line_de['id']
        match_degree_one['huxing'] = {}
        match_degree_one['huxing']['term'] = 0
        match_degree_one['huxing']['weight'] = int(require_data['huxing']['room']['weight']) + int(
            require_data['huxing']['hall']['weight']) + int(require_data['huxing']['towards']['weight'])
        match_degree_one['huxing']['content'] = {}
        match_degree_one['huxing']['content']['room'] = line_de['house_room']
        match_degree_one['huxing']['content']['hall'] = line_de['house_hall']


        match_degree_one['huxing']['term'] += handleTowards(require_toward, ToBit(line_de['house_toward'])) * int(
            require_data['huxing']['towards']['weight'])
        getNormalization(max_list, min_list, line_de)
        for str in ['price', 'area']:
            match_degree_one[str] = {}
            match_degree_one[str]['term'] = 0
            match_degree_one[str]['weight'] = require_data[str]['weight']
            if(str=='area'):
                match_degree_one[str]['content'] = line_de["house_totalarea"]
            else:
                match_degree_one[str]['content'] = line_de["house_"+str]


        match_degree_one['price']['term'] += (1 - getDistance('house_price')) * int(require_data['price']['weight'])
        match_degree_one['area']['term'] += (1 - getDistance('house_totalarea')) * int(require_data['area']['weight'])
        match_degree_one['huxing']['term'] += (1 - getDistance('house_room')) * int(require_data['huxing']['room']['weight'])
        match_degree_one['huxing']['term'] += (1 - getDistance('house_hall')) * int(require_data['huxing']['hall']['weight'])


        match_degree_one['term'] = match_degree_one['huxing']['term'] + match_degree_one['price']['term'] + match_degree_one['area']['term']
        match_degree.append(match_degree_one)
        # match_degree.append(json.dumps(match_degree_one))
    match_degree = sorted(match_degree, key=operator.itemgetter('term'), reverse=True)
    # for i in range()
    for i in range(0, len(match_degree)):
        match_degree[i] = json.dumps(match_degree[i])
    return match_degree

def getDistance(str):
    if(str!="house_totalarea"):
        if nor_one[str] <= require_nor[str.split("_")[1]][0]:
            return abs(nor_one[str] - require_nor[str.split("_")[1]][0])
        elif nor_one[str] >= require_nor[str.split("_")[1]][1]:
            return abs(nor_one[str] - require_nor[str.split("_")[1]][1])
        else:
            return 0
    else:
        if nor_one[str] <= require_nor["area"][0]:
            return abs(nor_one[str] - require_nor["area"][0])
        elif nor_one[str] >= require_nor["area"][1]:
            return abs(nor_one[str] - require_nor["area"][1])
        else:
            return 0
    return


## 通过mysql 获取房源属性

def get_user_redis(useid):
    # pool = redis.ConnectionPool(host="123.57.61.107", port=6379, db=0)
    # host = "123.57.61.107", port = 6379, db = 0
    r = redis.StrictRedis(host="123.57.61.107", port=6379, db=0)
    return r.get(useid)


def get_houst_mysql(houseid):
    try:
        conn = MySQLdb.connect(host="182.92.96.120", user="zhuge", passwd="zhuge1116", db="spider", charset="utf8")
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cursor.execute(
            """SELECT hsi.id, hsi.house_price,hs.house_totalarea,hs.house_room ,hs.house_hall,hsi.house_toward from house_sell hs left join house_sell_info hsi on hs.id=hsi.id where hs.id =%s and hsi.weight=0""",
            (houseid,))
        data = cursor.fetchall()
        cursor.close()

    except  MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return data[0]


def ToBit(x):  # 转化为四维二元变量(对应的十进制数- -)
    switcher = {
        1: 1, 2: 2, 3: 4, 4: 8, 5: 5, 6: 6, 7: 9, 8: 10, 9: 12, 10: 3, 11: 7, 12: 13, 13: 14, 14: 11, 15: 15
    }
    return switcher.get(int(x), 15)  # default=15(东南西北)



def get_req_norm(max, min, data, str, require_nor):
    if '-' in data:  # 处理区间
        index = data.index('-')  # 返回'-'字符位置
        mmin = division((int(data[:index]) - min), (max - min))  # normalization
        mmax = division((int(data[index + 1:]) - min), (max - min))
    else:
        mmin = mmax = division((int(data) - min), (max - min))
    require_nor[str] = [mmin, mmax]
    return


def getNormalization(max_list, min_list, line_de):  # 非区间当做区间的特殊情况
    for str in ['house_price', 'house_totalarea', 'house_room', 'house_hall']:
        nor_one[str] = division((int(line_de[str]) - min_list[str]), (max_list[str] - min_list[str]))
    return


def division(a, b):
    if b == 0:  # 处理分母为0的情况
        return 0
    else:
        return a / b
    return


def getMaxMin(max_list, min_list, str1, str):
    str1 = int(str1)  # 字符串转为int以比较大小
    if str1 > max_list[str]:
        max_list[str] = str1
    if str1 < min_list[str]:
        min_list[str] = str1
    return


def getMaxMin_1(max_list, min_list, str1, str):
    if '-' in str1:  # 处理区间
        index = str1.index('-')  # 返回'-'字符位置
        mmin = int(str1[:index])
        mmax = int(str1[index + 1:])
        if mmin < min_list[str]:
            min_list[str] = mmin
        if mmax > max_list[str]:
            max_list[str] = mmax
        return
    str1 = int(str1)
    if str1 > max_list[str]:
        max_list[str] = str1
    elif str1 < min_list[str]:
        min_list[str] = str1
    return


def handleTowards(x, y):
    return ToBitNum(x & y) / ToBitNum(x | y)


def ToBitNum(x):  # 对应的二进制数中bit1的个数
    switcher = {
        1: 1, 2: 1, 3: 2, 4: 1, 5: 2, 6: 2, 7: 3, 8: 1, 9: 2, 10: 2, 11: 3, 12: 2, 13: 3, 14: 3, 15: 4
    }
    return switcher.get(int(x), 15)


if __name__ == "__main__":
    #sql = {"uid": "9876", "hid": "1457176,1457178,1457451"}
    sql=sys.argv[1]
    print get_house_similarity(sql)

