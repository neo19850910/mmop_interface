#-*- coding:utf8 -*-
import json
import requests

#-*- coding:utf8 -*-

import requests

class Sessionget:
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Referer':'http://192.168.0.150:9522/mmop-web/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    data = {'username':'SUPERADMIN','password':'SUPERADMIN'}
    url ='http://192.168.0.150:9522/mmop-web/login'
    @classmethod
    def get_web(cls):
        cls.session = requests.session()
        cls.session.post(cls.url, headers=cls.headers, data=cls.data)
        return cls.session

if __name__ =='__main__':
    print Sessionget.get_web()