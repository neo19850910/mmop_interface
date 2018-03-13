#-*- coding:utf8 -*-

import unittest
from public import Sessionget
class chk_count(unittest.TestCase):
    def setUp(self):
        self.r = Sessionget.get_web().post("http://192.168.0.150:9522/mmop-web/main/selectCheckSubsByArea")

    def test_chk_count(self):
        '''获取所有厂站当年检验次数'''
        print self.r.json()['msg'][0]['AREA_NAME'],self.r.json()['msg'][0]['AREA_ID'],self.r.json()['msg'][0]['SUBS_NAME'], self.r.json()

    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()
