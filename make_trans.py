#!/usr/bin/env python
#coding=utf-8

from connect_db import get_rate

def make(currency1,currency2,amount):
#    currency2 = str(input('输入币种--> '))
    rate = get_rate(currency1,currency2)
    global result
    rate1 = rate[0]['rate']
    rate2 = rate[1]['rate']
    trans1 = float(amount) / float(rate1) #将源币种转换为人民币
    result = trans1 * rate2 #再将转换后的人民币转换为目标币种
    #print("{}人民币可以兑换{}{}".format(rmb,result,currency2))
    return result
#a=make('委内瑞拉博利瓦(VEF)','澳门元(MOP)',12)[0]
#b=make('委内瑞拉博利瓦(VEF)','澳门元(MOP)',12)[1]
#c=make('委内瑞拉博利瓦(VEF)','澳门元(MOP)',12)[2]
#print(a,b,c)

#make('太平洋法郎(XPF)',12)
