#!/usr/bin/env python
# encoding: utf-8
import unittest
from testcase import ddt
import json
from common.log import get_logger
from common.sever import vivst

from midd.Handler1 import Handler, login

#初始化一个loggin

loggin=get_logger('log4')

#读取Excel数据
cases=Handler.Excle.read_excle("test_my")

@ddt.ddt
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.token=login()
    @ddt.data(*cases)
    def test_projects(self,case_info):
        #  数据动态替换
        if "#token#"in case_info["url"]:
            case_info["url"] = case_info["url"].replace("#token#",self.token)
        if "#token#" in case_info["headers"]:
            case_info["headers"] = case_info["headers"].replace("#token#", self.token)

        #预期结果
        Expected_results = json.loads(case_info["Expected_results"])

        # 实际结果
        method = case_info["method"]

        url = Handler.yaml["host"]["test_url"] + case_info["url"]

        data=json.loads(case_info["data"])
        headers=json.loads(case_info["headers"])

        params = eval(case_info["params"])


        res = vivst(method=method, url=url,json=data,headers=headers,data=params).json()

        try:
            if case_info["case_id"] in range(3):
                self.assertEqual(Expected_results["msg"], res["msg"])
            if case_info["case_id"] in range(3,9):
                self.assertEqual(Expected_results["message"], res["message"])
                self.assertEqual(Expected_results["status"], res["status"])
            loggin.info("第{}条测试用例通过".format(case_info["case_id"]))
            Handler.Excle.write_excle(Form="test_my", row=case_info["case_id"] + 1, column=10, data="pass")

        except AssertionError as e:
            loggin.error("第{}条测试用例不通过:{}".format(case_info["case_id"], e))
            Handler.Excle.write_excle(Form="test_my", row=case_info["case_id"] + 1, column=10, data="fail")
            raise e


if __name__ == '__main__':
    unittest.main()
