# import unittest
# import ddt
# import json
# from common.log的封装 import get_logger
# from common.接口请求的封装 import vivst
#
# from midd.Handler1 import Handler
# #初始化一个loggin
# loggin=get_logger()
# #读取Excel数据
# cases=Handler.Excle.read_excle("test_login")
#
#
# @ddt.ddt
# class MyTestCase(unittest.TestCase):
#     @ddt.data(*cases)
#     def test_login(self,case_info):
#         case_info["data"] = Handler().replace_data(case_info["data"])
#
#         # 预期结果
#         Expected_results = json.loads(case_info["Expected_results"])
#         # 实际结果
#         method = case_info["method"]
#         url = Handler.yaml["host"]["test_url"] + case_info["url"]
#         data=json.loads(case_info["data"])
#         headers=json.loads(case_info["headers"])
#         res = vivst(method=method, url=url,json=data,headers=headers).json()
#         try:
#             if case_info["case_id"] in range(3):
#                 self.assertEqual(Expected_results["username"], res["username"])
#             if case_info["case_id"] in range(3,5):
#                 self.assertEqual(Expected_results["password"], res["password"])
#             if case_info["case_id"] in range(5,7):
#                 self.assertEqual(Expected_results["non_field_errors"], res["non_field_errors"])
#             if case_info["case_id"] in range(7,8):
#                 self.assertEqual(str(Expected_results["username"]), str(res["username"]))
#             loggin.info("第{}测试用例通过".format(case_info["case_id"]))
#             Handler.Excle.write_excle(Form="test_login", row=case_info["case_id"] + 1, column=9, data="pass")
#
#         except AssertionError as e:
#             loggin.error("第{}测试用例不通过:{}".format(case_info["case_id"], e))
#             Handler.Excle.write_excle(Form="test_login", row=case_info["case_id"] + 1, column=9, data="fail")
#             raise e
#
#
# if __name__ == '__main__':
#     unittest.main()
