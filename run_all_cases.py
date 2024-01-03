import unittestreport
import os

# #加载用例，生成测试报告
# from common import HTMLTestRunner
from config.config import local_config
import unittest
import time
def create_suite():
    suite=unittest.TestSuite()
    case_dir=local_config.dir_testcase
    dis=unittest.defaultTestLoader.discover(
        start_dir=case_dir,
        pattern='test_*.py',
        top_level_dir=None)
    suite.addTests(dis)
    return suite

cur_time=time.strftime("%Y%m%d-%H%M%S",time.localtime())
case=unittest.TestLoader().discover(os.path.join(local_config.dir_testcase))

runner=unittestreport.TestRunner(case,filename=cur_time+"report.html",
                 report_dir=".\\reports",
                 title='测试报告',
                 tester='wwh',
                 desc="项目测试生成的报告",
                 templates=2)

runner.run()
