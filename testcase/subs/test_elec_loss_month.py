#-*- coding:utf8 -*-

import unittest
import requests
from public import *

class ElecLossMonth(unittest.TestCase):
    '''获取某个电站近六个月的输入电量输出电量和站损率'''
    def setUp(self):
        self.r = Sessionget.get_web().post("http://192.168.0.150:9522/mmop-web/main/selectCheckSubsByArea").json()
        self.verificationErrors = []
    def test_elec_loss_month(self):
        """获取某个电站近六个月的输入电量输出电量和站损率"""
        for i in self.r['msg']:
            for m in get_oracle.db_chk_count():
                for n in Sessionget().get_api()['items']:
                    if i['SUBS_NAME']==m[1].decode('utf8'):
                        if n['subs'] == m[0].decode('utf8'):
                            self.assertEqual(n['chk_count'], str(i['C']))
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
if __name__ =='__main__':
    unittest.main()
