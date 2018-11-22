#!/usr/bin/env python
#coding=utf-8

import requests
import re
from bs4 import BeautifulSoup
from connect_db import conect

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
url = 'http://hl.anseo.cn/'
response = requests.get(url,headers=headers)
html = response.content.decode('utf8')
soup = BeautifulSoup(html,'lxml')
original=soup.find_all(name='ul')[0].text
partten = '.*?\d.\d+\s(.*?)\s.*?'
compiles = re.compile(partten,re.S)
currency = re.findall(compiles,original)
partten2 = '.*?(\d\.\d{4}).*?'
compiles2 = re.compile(partten2,re.S)
rate = re.findall(compiles2,original)
data = tuple(zip(currency,rate))
for tu in data:
    conect(tu)











