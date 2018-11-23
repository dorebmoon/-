#!/usr/bin/env python
#coding=utf-8

from connect_db import get_rate

def make(currency2,rmb):
#    currency2 = str(input('输入币种--> '))
    rate2 = get_rate('{}'.format(currency2))
    global result
    rmb = int(rmb)
    result = float(rate2) * rmb
    #print("{}人民币可以兑换{}{}".format(rmb,result,currency2))
    return result

#make('太平洋法郎(XPF)',12)
