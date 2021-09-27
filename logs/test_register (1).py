# import json
# import unittest
# import ddt
#
# from common.log的封装 import get_logger
# from common.接口请求的封装 import vivst
#
# from midd.Handler1 import Handler, My_sql
# #初始化logger
# loggin=get_logger()
# #读取测试数据
# cases=Handler.Excle.read_excle("test_register")
# #获取测试环境的ip
# url=Handler.yaml["host"]["test_url"]
#
#
# @ddt.ddt
# class Test_register(unittest.TestCase):
#     def setUp(self) -> None:
#         self.DB=My_sql()
#     def tearDown(self) -> None:
#         self.DB.close()
#     @ddt.data(*cases)
#     def test_register(self,case_info):
#         #测试数据的替换
#         case_info["data"]=Handler().replace_data(case_info["data"])
#
#         #预期结果
#         Expected_results=json.loads(case_info["Expected_results"])
#
#
#         #执行用例之前的注册表长度
#         Before_Length=len(self.DB.query("select*from auth_user "))
#
#         #实际结果
#         data=json.loads(case_info["data"])
#         headers=json.loads(case_info["headers"])
#         test_url=url+ case_info["url"]
#         method=case_info["method"]
#         res=vivst(method=method,url=test_url,json=data,headers=headers)
#         #开始断言
#         try:
#             if case_info["case_id"] in range(5):
#                 self.assertEqual(Expected_results["username"], res.json()["username"])
#             if case_info["case_id"] in range(6,10):
#                 self.assertEqual(Expected_results["email"], res.json()["email"])
#             if case_info["case_id"] in range(10,14):
#                 self.assertEqual(Expected_results["password"], res.json()["password"])
#             if case_info["case_id"] in range(14,18):
#                 self.assertEqual(Expected_results["password_confirm"], res.json()["password_confirm"])
#             if case_info["case_id"] in range(18,19):
#                 self.assertEqual(Expected_results["non_field_errors"], res.json()["non_field_errors"])
#             if case_info["case_id"] in range(19,20):
#                 self.assertEqual(Expected_results, str(res))
#             #数据库断言
#             if case_info["title"]=="注册成功":
#                 #注册成功后的注册表长度
#                 After_Length = len(self.DB.query("select*from auth_user "))
#                 self.assertTrue(Before_Length+1==After_Length)
#             loggin.info("第{}测试用例通过".format(case_info["case_id"]))
#             Handler.Excle.write_excle(Form="test_register", row=case_info["case_id"] + 1, column=9, data="pass")
#
#         except AssertionError as e:
#             loggin.error("第{}测试用例不通过:{}".format(case_info["case_id"], e))
#             Handler.Excle.write_excle(Form="test_register", row=case_info["case_id"] + 1, column=9, data="fail")
#             raise e
#
#
# if __name__ == '__main__':
#     unittest.main()
