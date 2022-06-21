import time
import unittest
#定义测试套件
from HTMLTestRunner import HTMLTestRunner

# suite=unittest.TestLoader().discover("./test_case", pattern='test*.py')
suite=unittest.TestLoader().discover("./test_case", pattern='test*.py')
#定义测试报告文件的路径及名称
filename="./report/html_report_{}.html".format(time.strftime("%Y%m%d%H%M%S"))

with open(filename,'wb') as f:
    #实例化HTMLTestRunner
    runner=HTMLTestRunner(stream=f,title="web自动化测试",description="win10-chrome-v20")
    runner.run(suite)

