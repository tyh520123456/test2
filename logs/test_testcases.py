# # import unittest
# # import ddt
# # import json
# # from common.log的封装 import get_logger
# # from common.接口请求的封装 import vivst
# # from midd.Handler1 import Handler, My_sql, jiekou
# #
# # #初始化一个loggin
# # loggin=get_logger()
# # #读取Excel数据
# # cases=Handler.Excle.read_excle("test_testcases")
# #
# #
# @ddt.ddt
# class MyTestCase(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#        cls.interface=jiekou()
#     def setUp(self) -> None:
#         self.DB=My_sql()
#     def tearDown(self) -> None:
#         self.DB.close()
#     @ddt.data(*cases)
#     def test_testcases(self,case_info):
#         #数据动态替换
#         if "#pid#"in case_info["data"]:
#             case_info["data"] = case_info["data"].replace("#pid#",str(self.interface["pid"]))
#         if "#iid#" in case_info["data"]:
#             case_info["data"] = case_info["data"].replace("#iid#", str(self.interface["iid"]))
#
# #         case_info["data"] = Handler().replace_data(case_info["data"])
# #         case_info["headers"]=Handler().replace_data(case_info["headers"])
# #
# #
# #         # 预期结果
# #         Expected_results = json.loads(case_info["Expected_results"])
# #
# #         #创建接口成功之前的表长度
# #         Before_Length = len(self.DB.query("select*from tb_testcases "))
# #         # 实际结果
# #         method = case_info["method"]
# #         url = Handler.yaml["host"]["test_url"] + case_info["url"]
# #         data=json.loads(case_info["data"])
# #         headers=json.loads(case_info["headers"])
# #         res = vivst(method=method, url=url,json=data,headers=headers)
# #
# #         try:
# #             if case_info["case_id"] in range(4):
# #                 self.assertEqual(Expected_results["name"], res.json()["name"])
# #             if case_info["case_id"] in range(4, 10):
# #                 self.assertEqual(Expected_results["interface"], res.json()["interface"])
# #             if case_info["case_id"] in range(10, 12):
# #                 self.assertEqual(Expected_results["author"], res.json()["author"])
# #             if case_info["case_id"] in range(12, 14):
# #                 self.assertEqual(Expected_results, str(res))
# #             #数据库断言
# #                 # 创建接口成功之后的表长度
# #                 After_Length = len(self.DB.query("select*from tb_testcases "))
# #                 self.assertTrue(Before_Length+1==After_Length)
# #             loggin.info("第{}测试用例通过".format(case_info["case_id"]))
# #             Handler.Excle.write_excle(Form="test_testcases", row=case_info["case_id"] + 1, column=9, data="pass")
# #         except AssertionError as e:
# #             loggin.error("第{}测试用例不通过:{}".format(case_info["case_id"], e))
# #             Handler.Excle.write_excle(Form="test_testcases", row=case_info["case_id"] + 1, column=9, data="fail")
# #             raise e
# #
# #
# #
# #
# # if __name__ == '__main__':
# #     unittest.main()
