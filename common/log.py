#!/usr/bin/env python
# encoding: utf-8
import logging

from config.config_path import test_logs


def get_logger(name,setLevel="DEBUG",log_formatter="%(asctime)s--%(filename)s--%(lineno)d--%(levelname)s:%(msg)s",Handler=None,file=test_logs):
    # 初始化一个收集器
    logger=logging.getLogger(name)
    #设置级别
    logger.setLevel(setLevel)
    #设置日期格式
    formatter=logging.Formatter(log_formatter)
    #判断控制台输出还是文本输出日志
    if Handler:
        file_Handler=logging.FileHandler(file,encoding="utf-8")
        file_Handler.setLevel(setLevel)
        logger.addHandler(file_Handler)
        file_Handler.setFormatter(formatter)
    else:
        StreamHandler=logging.StreamHandler()
        StreamHandler.setLevel(setLevel)
        logger.addHandler(StreamHandler)
        StreamHandler.setFormatter(formatter)
    return logger
