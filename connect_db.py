#!/usr/bin/env python
#coding=utf8

import pymysql.cursors
#连接到数据库
def conect(tup1):
    connection = pymysql.connect(host='10.10.2.19',
                                 user='ayu',
                                 password='yicai127',
                                 db='change_rate',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        sql1 = 'delete from normal'
        sql = 'insert into normal (currency,rate)values{}'.format(tup1)
        cursor.execute(sql1)
        cursor.execute(sql)
    connection.commit()
    connection.close()

def get_rate(currency1):
    connection = pymysql.connect(host='10.10.2.19',
                                 user='ayu',
                                 password='yicai127',
                                 db='change_rate',
                                 cursorclass =pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        sql = 'select rate from normal where currency=%s'
        cursor.execute(sql,currency1)
        rate = cursor.fetchall()[0]['rate']
    connection.close()
    return rate
#rate2 = get_rate('委内瑞拉博利瓦(VEF)')
#print(rate2)