#coding=utf-8

import HTMLTestRunner
import unittest
import os,time
from testcase.subs.test_chk_count import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')
listaa='F:\\mmop_interface\\testcase'
def creatsuitel():
    testunit=unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(listaa,
                                                   pattern='test_*.py',
                                                   top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit
alltestnames = creatsuitel()
now = time.strftime('%Y-%m-%M-%H_%M_%S',time.localtime(time.time()))
filename = 'F:\\mmop_interface\\report\\'+now+'result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'北京关口大屏接口测试测试报告',
        description=u'用例执行情况：')
#执行测试用例
runner.run(alltestnames)
