#!/usr/bin/env python
# encoding: utf-8
import os

# 查询最新的测试报告邮件
from config.config_path import test_baogao


def file_report(test_baogao):
    # 列出所有的目录和文件
    lists = os.listdir(test_baogao)
    # # 重新按照时间排序
    lists.sort()

    #查找出最新的邮件并进行路径拼接
    file_report = os.path.join(test_baogao, lists[-1])
    #测试报告的路径
    return file_report


