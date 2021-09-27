#!/usr/bin/env python
# encoding: utf-8
#
# from bs4 import BeautifulSoup
# import re
# # 打开测试报告html文件，读取报告内容
# from common.查询最新测试报告 import file_report
# from common.测试报告发送邮件 import send_mail
# from config.config_path import test_baogao
#
# baogao=file_report(test_baogao)
# with open(baogao,"r",encoding="utf-8") as e:
#     f=e.read()
# # 解析html，查找class属性text-center active
# soup = BeautifulSoup(f, "html.parser")
# status = soup.find_all(class_="text-center active")
# # 把内容转换成字符串
# str=str(status)
#
# # 通过正则匹配通过率
# pattern=re.compile("通过率：(.+)%")
# # 把通过率拿出来转换成浮点数进行判断
# result=float(pattern.findall(str)[0])
# # 当通过率小于100时发送邮件
# if result<100:
#     send_mail(baogao)
#     print("测试用例不通过发送邮件")
# # 当通过率等于100时不发送邮件
# else:
#     print("测试用例全部通过，不发送邮件")
