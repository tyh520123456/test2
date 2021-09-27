#!/usr/bin/env python
# encoding: utf-8
import os
#获取跟目录
a=os.path.abspath(__file__)
b=os.path.dirname(a)
c=os.path.dirname(b)
#收集测试用例的路径
test_lujin=os.path.join(c,"testcase")
#存放测试报告的路径
test_baogao=os.path.join(c,"reports")
#测试数据的路径
test_Excle=os.path.join(c,"data")

#配置文件yaml的路径
test_yaml=os.path.join(c,"config")
#存放测试日志的路径
__test_log=os.path.join(c,"logs")
test_logs=os.path.join(__test_log,"test_log.txt")

