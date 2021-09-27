#!/usr/bin/env python
# encoding: utf-8
import requests

from common.log import get_logger

def vivst(method, url, **kwargs):
   try:
      res = requests.request(method, url, **kwargs)
      return res
   except requests.exceptions.InvalidSchema as e:
      get_logger().error("输入的参数类型不对{}".format(e))
# url="https://health.sina.cn/patient/v3/community/pagePersonalCommunity"
# params={"pageNum":1,"pageSize":20}
# headers={"Content-Tpye":"application/x-www-form-urlencoded","token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mjg2NjIwNTI4NDIsInBheWxvYWQiOiJcIjEzMTg5NzcwOTcwXCIifQ.Mul_q29TfXz9XK5rL9UOzBbuDbxxyz04wIuQ5NLp-Jw"}
# res=vivst(url=url,data=params,headers=headers,method="post")
# print(res.json())