#-*- coding:utf8 -*-

import ConfigParser
import os
import logging
#获取config配置文件
def getConfig(section, key):
    config = ConfigParser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '\config.conf'
    config.read(path)
    return config.get(section, key)

if __name__=='__main__':
    print getConfig('SUBS','headers')