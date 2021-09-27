#!/usr/bin/env python
# encoding: utf-8
# import random
import re
import os
# from pymysql.cursors import DictCursor


# from common.mysql import DB_mysql
from common.yaml import read_yaml
from common.sever import vivst
from config.config_path import test_yaml, test_Excle
from common.Excel import Excle


class Handler:
    # 读取yaml数据
    yaml=read_yaml(os.path.join(test_yaml,"config.yaml"))
    # 读取Excel的数据
    Excle=Excle(os.path.join(test_Excle,"test_cases.xlsx"))

    # @property
    # def username(self):
    #     return randow_user()
    # @property
    # def email(self):
    #     return randow_email()
    # @property
    # def name(self):
    #     return randow_name()
    # @property
    # def api_name(self):
    #     return randow_api_name()
    # @property
    # def case_name(self):
    #     return randow_case_name()
    @property
    def project_id(self):
        return project_id()

    @property
    def token(self):

        return login()
    def replace_data(self,data):
        pattern = r"#(.*?)#"
        while re.search(pattern, data):
            key = re.search(pattern, data).group(1)
            value = getattr(self, key, " ")
            data = re.sub(pattern, str(value), data, 1)
        return data
# def randow_user():
#     while True:
#         phone = "1" + random.choice(["3", "5", "7", "8"])
#         for x in range(9):
#             num = random.randint(0, 9)
#             phone = phone + str(num)
#         DB=My_sql()
#         res=DB.query("select*from auth_user where email='{}' ".format(phone) )
#         if  not res :
#             DB.close()
#             return phone
#         DB.close()
# def randow_email():
#     while True:
#         phone = "1" + random.choice(["3", "5", "7", "8"])
#         for x in range(9):
#             num = random.randint(0, 9)
#             phone = phone + str(num)
#         phone = phone + random.choice(["@qq.com", "@163.com"])
#         DB = My_sql()
#         res = DB.query("select*from auth_user where email='{}' ".format(phone))
#         if not res:
#             DB.close()
#             return phone
#         DB.close()
# def randow_name():
#         while True:
#             phone = "这是第"
#             for x in range(3):
#                 num = random.randint(0, 9)
#                 phone = phone + str(num)
#             DB = My_sql()
#             res = DB.query("select*from tb_projects where name='{}' ".format(phone))
#             if not res:
#                 DB.close()
#                 return phone+"个项目"
#             DB.close()


# def randow_api_name():
#     while True:
#         phone = "这是第"
#         for x in range(3):
#             num = random.randint(0, 9)
#             phone = phone + str(num)
#         DB = My_sql()
#         res = DB.query("select*from tb_interfaces where name='{}' ".format(phone))
#         if not res:
#             DB.close()
#             return phone + "个接口"
#         DB.close()
# def randow_case_name():
#     while True:
#         phone = "这是第"
#         for x in range(3):
#             num = random.randint(0, 9)
#             phone = phone + str(num)
#         DB = My_sql()
#         res = DB.query("select*from tb_testcases where name='{}' ".format(phone))
#         if not res:
#             DB.close()
#             return phone + "个用例"
#         DB.close()

# class My_sql(DB_mysql):
#     def __init__(self):
#         DB_config = Handler.yaml["mysql"]
#         super().__init__(
#                 host=DB_config["host"],
#                 port=DB_config["port"],
#                 user=DB_config["user"],
#                 password=DB_config["password"],
#                 charset=DB_config["charset"],
#                 database=DB_config["database"],
#                 cursorclass=DictCursor
#             )
def login():
    url=Handler.yaml["host"]["test_url"]+ "midauth/user/login/phone"
    data=Handler.yaml["user"]

    headers={"Content-Type":"application/json"}
    method="post"
    res=vivst(method=method,url=url,json=data,headers=headers).json()
    token=res["data"]["token"]
    return token
def project_id():
    url=Handler.yaml["host"]["test_url"]+ "/projects/"
    headers={"Content-Type":"application/json","Authorization":login()}
    method="post"
    data={
    "name": randow_name(),
     "leader": "可优",
     "tester": "某人",
    "programmer": "某人",
    "publish_app": "XXX应用",
    "desc": "xxxx描述"
 }
    res = vivst(method=method, url=url, json=data, headers=headers).json()
    return res["id"]

# def jiekou():
#     url=Handler.yaml["host"]["test_url"]+ "/interfaces/"
#     headers={"Content-Type":"application/json","Authorization":login()}
#     method="post"
#     data={
#     "name": randow_api_name(),
#     "tester": "某人",
#     "project_id": project_id(),
#     "desc": "xxxx描述"
#  }
#     res = vivst(method=method, url=url, json=data, headers=headers).json()
#     return {"pid":res["project_id"],"iid":res["id"]}
