#!/usr/bin/env python
# encoding: utf-8
import unittest
from testcase import ddt
import json
from common.log import get_logger
from common.sever import vivst
from midd.Handler1 import Handler

#初始化一个loggin
loggin=get_logger('log5')
#读取Excel数据
cases=Handler.Excle.read_excle("home_page")



@ddt.ddt
class MyTestCase(unittest.TestCase):

    @ddt.data(*cases)
    def test_follow(self,case_info):

        # 预期结果
        Expected_results = json.loads(case_info["Expected_results"])
        # 实际结果
        method = case_info["method"]
        url = Handler.yaml["host"]["test_url"] + case_info["url"]
        data=json.loads(case_info["data"])
        headers=json.loads(case_info["headers"])
        res = vivst(method=method, url=url,json=data,headers=headers).json()

        # 断言测试结果
        try:
            if case_info["case_id"] in range(10):
                self.assertEqual(Expected_results["message"],res["message"])
                self.assertEqual(Expected_results["status"],res["status"])
            if case_info["case_id"] in range(10,11):
                self.assertEqual(Expected_results["status"],res["status"])
            loggin.info("第{}条测试用例通过".format(case_info["case_id"]))
            Handler.Excle.write_excle(Form="home_page", row=case_info["case_id"] + 1, column=9, data="pass")
        except AssertionError as e:
            loggin.error("第{}条测试用例不通过:{}".format(case_info["case_id"], e))
            Handler.Excle.write_excle(Form="home_page", row=case_info["case_id"] + 1, column=9, data="fail")
            raise e




if __name__ == '__main__':
    unittest.main()
