#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:run_all_cases.py
# @time:2020/6/7 10:57 上午

import time,os
import unittest
import HTMLTestRunner
from utils import HTMLTestReportCN
from utils.config_utils import config

def get_testsuite():
    discover = unittest.defaultTestLoader.discover(start_dir='./testcases',
                                                   pattern='*_testcase.py',
                                                   top_level_dir='./testcases')
    all_suite = unittest.TestSuite()
    all_suite.addTest(discover)
    return all_suite

# 方式一
# now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
# html_report = os.path.join(config.report_path, 'result_%s.html'% now_time)
# file = open(html_report, 'wb')
# html_runner = HTMLTestRunner.HTMLTestRunner(stream=file,
#                                             title='API测试',
#                                             description='测试描述')
# html_runner.run(get_testsuite())

# 方式二
report_dir = HTMLTestReportCN.ReportDirectory(config.report_path)
report_dir.create_dir("API_TEST")
dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
fp = open(report_path, 'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                         title="API_TEST",
                                         description='测试描述',
                                         tester='cherry')
runner.run(get_testsuite())
fp.close()