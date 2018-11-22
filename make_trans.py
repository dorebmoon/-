#!/usr/bin/env python
#coding=utf-8

from connect_db import get_rate

def make(rmb):
    currency2 = str(input('输入币种--> '))
    rate2 = get_rate('{}'.format(currency2))
    print(rate2)

make(10)


