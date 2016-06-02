# -*- coding: UTF-8 -*-
import config

#数字转换函数
def cn2dig(cn):
    lcn = list(cn)
    unit = 0 #当前的单位
    ldig = []#临时数组
    while lcn:
        cndig = lcn.pop()
        if config.CN_UNIT.has_key(cndig):
            unit = config.CN_UNIT.get(cndig)
            if unit==10000:
                ldig.append('w')    #标示万位
                unit = 1
            elif unit==100000000:
                ldig.append('y')    #标示亿位
                unit = 1
            elif unit==1000000000000:#标示兆位
                ldig.append('z')
                unit = 1
            continue
        else:
            dig = config.CN_NUM.get(cndig)
            if unit:
                dig = dig*unit
                unit = 0
            ldig.append(dig)
    if unit==10:    #处理10-19的数字
        ldig.append(10)
    ret = 0
    tmp = 0
    while ldig:
        x = ldig.pop()
        if x=='w':
            tmp *= 10000
            ret += tmp
            tmp=0
        elif x=='y':
            tmp *= 100000000
            ret += tmp
            tmp=0
        elif x=='z':
            tmp *= 1000000000000
            ret += tmp
            tmp=0
        else:
            tmp += x
    ret += tmp
    return ret
def toParam(dicts):
    result=''
    for key in dicts:
        result+=key+'='+dicts[key]+'&'
    return result
