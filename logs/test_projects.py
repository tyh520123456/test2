# import unittest
# import ddt
# import json
# from common.log的封装 import get_logger
# from common.接口请求的封装 import vivst
#
# from midd.Handler1 import Handler, My_sql
#
# #初始化一个loggin
# loggin=get_logger()
# #读取Excel数据
# cases=Handler.Excle.read_excle("test_projects")
#
#
#
# @ddt.ddt
# class MyTestCase(unittest.TestCase):
#     def setUp(self) -> None:
#         self.DB=My_sql()
#     def tearDown(self) -> None:
#         self.DB.close()
#     @ddt.data(*cases)
#     def test_projects(self,case_info):
#         case_info["data"] = Handler().replace_data(case_info["data"])
#         case_info["headers"]=Handler().replace_data(case_info["headers"])
#
#
#         # 预期结果
#         Expected_results = json.loads(case_info["Expected_results"])
#         # 执行用例之前的项目表长度
#         Before_Length = len(self.DB.query("select*from tb_projects "))
#
#         # 实际结果
#         method = case_info["method"]
#         url = Handler.yaml["host"]["test_url"] + case_info["url"]
#         data=json.loads(case_info["data"])
#         headers=json.loads(case_info["headers"])
#         res = vivst(method=method, url=url,json=data,headers=headers)
#
#         try:
#             if case_info["case_id"] in range(4):
#                 self.assertEqual(Expected_results["name"], res.json()["name"])
#             if case_info["case_id"] in range(4,6):
#                 self.assertEqual(Expected_results["leader"], res.json()["leader"])
#             if case_info["case_id"] in range(6,8):
#                 self.assertEqual(Expected_results["tester"], res.json()["tester"])
#             if case_info["case_id"] in range(8,10):
#                 self.assertEqual(Expected_results["programmer"], res.json()["programmer"])
#             if case_info["case_id"] in range(10,12):
#                 self.assertEqual(Expected_results["publish_app"], res.json()["publish_app"])
#             if case_info["case_id"] in range(12,14):
#                 self.assertEqual(Expected_results, str(res))
#             #数据库断言
#                 #新增项目成功后的项目表长度
#                 After_Length = len(self.DB.query("select*from tb_projects "))
#                 self.assertTrue(Before_Length+1==After_Length)
#
#             loggin.info("第{}测试用例通过".format(case_info["case_id"]))
#             Handler.Excle.write_excle(Form="test_projects", row=case_info["case_id"] + 1, column=9, data="pass")
#
#         except AssertionError as e:
#             loggin.error("第{}测试用例不通过:{}".format(case_info["case_id"], e))
#             Handler.Excle.write_excle(Form="test_projects", row=case_info["case_id"] + 1, column=9, data="fail")
#             raise e
#
#
# if __name__ == '__main__':
#     unittest.main()
