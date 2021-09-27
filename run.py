#!/usr/bin/env python
# encoding: utf-8
import unittest
import os
from datetime import datetime

from HTMLTestRunnerNew import HTMLTestRunner
from config.config_path import test_lujin, test_baogao
from bs4 import BeautifulSoup
import re
# 打开测试报告html文件，读取报告内容
from common.baogao import file_report
from common.youjian import send_mail

# 初始化一个加载器，loader
loader=unittest.TestLoader()
# 使用loader收集所有的测试用例
suit=loader.discover(test_lujin)
# 测试报告路径的拼接
ts=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
reports_name="reports-{}.html".format(ts)
reports_file=os.path.join(test_baogao,reports_name)

# 生成html的测试报告
with open(reports_file,"wb") as f:
    runner=HTMLTestRunner(f,title="C端h5接口自动化测试",description="此次测试了31个接口",tester="唐阳辉")
    runner.run(suit)
# 获取最新测试报告路径
baogao=file_report(test_baogao)
# 读取测试报告内容
with open(baogao,"r",encoding="utf-8") as e:
    f=e.read()
# 关闭测试报告文件
e.close()
# 解析html，查找class属性text-center active
soup = BeautifulSoup(f, "html.parser")
status = soup.find_all(class_="text-center active")
# 把内容转换成字符串
str=str(status)

# 通过正则匹配通过率
pattern=re.compile("通过率：(.+)%")
# 把通过率拿出来转换成浮点数进行判断
result=float(pattern.findall(str)[0])
# 当通过率小于100时发送邮件
if result != 100:
    send_mail(baogao)
    print("测试用例不通过发送测试报告邮件")
# 当通过率等于100时不发送邮件
else:
    print("测试用例全部通过，不发送邮件")

