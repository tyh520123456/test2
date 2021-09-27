# import unittest
# import ddt
# import json
# from common.log的封装 import get_logger
# from common.接口请求的封装 import vivst
#
# from midd.Handler1 import Handler, My_sql
# #初始化一个loggin
# loggin=get_logger()
# #读取Excel数据
# cases=Handler.Excle.read_excle("test_zhucejiaoyan")
#
# @ddt.ddt
# class MyTestCase(unittest.TestCase):
#     def setUp(self) -> None:
#         self.DB=My_sql()
#     def tearDown(self) -> None:
#         self.DB.close()
#     @ddt.data(*cases)
#     def test_zhucejiaoyan(self,case_info):
#         #数据动态替换
#         case_info["url"]=Handler().replace_data(case_info["url"])
#
#         #预期结果
#         Expected_results = json.loads(case_info["Expected_results"])
#
#         #实际结果
#         method=case_info["method"]
#         url=Handler.yaml["host"]["test_url"]+case_info["url"]
#         res=vivst(method=method,url=url).json()
#
#         #数据断言
#         self.assertEqual(Expected_results["count"],res["count"])
#
#         #数据库断言
#         try:
#             if case_info["title"]=="用户名存在":
#                 user=self.DB.query("select*from auth_user where username='{}'".format(res["username"]))
#                 self.assertTrue(user)
#             if case_info["title"]=="用户名不存在":
#                 user=self.DB.query("select*from auth_user where username='{}'".format(res["username"]))
#                 self.assertTrue(not user)
#             if case_info["title"]=="邮箱存在":
#                 email=self.DB.query("select*from auth_user where email='{}'".format(res["email"]))
#                 self.assertTrue(email)
#             if case_info["title"]=="邮箱不存在":
#                 email=self.DB.query("select*from auth_user where email='{}'".format(res["email"]))
#                 self.assertTrue(not email)
#             loggin.info("第{}测试用例通过".format(case_info["case_id"]))
#             Handler.Excle.write_excle(Form="test_zhucejiaoyan", row=case_info["case_id"] + 1, column=9, data="pass")
#         except AssertionError as e:
#             loggin.error("第{}测试用例不通过:{}".format(case_info["case_id"], e))
#             Handler.Excle.write_excle(Form="test_zhucejiaoyan", row=case_info["case_id"] + 1, column=9, data="fail")
#             raise e
#
#
#
#
#
# if __name__ == '__main__':
#     unittest.main()
