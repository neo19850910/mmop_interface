#-*- coding:utf8 -*-

import unittest
import requests
from public import *

class Chking(unittest.TestCase):
    '''获取所有正在检验的厂站'''
    def setUp(self):
        self.verificationErrors = []
    def test_chking(self):
        """获取所有正在检验的厂站"""
        for i in get_oracle.db_chking():
            for m in i:
                for n in Sessionget().get_chking()['items']:
                    self.assertEqual(m,9)
    def tearDown(self):
        self.assertEqual([], self.verificationErrors,"test has bug!")
if __name__ =='__main__':
    unittest.main()
