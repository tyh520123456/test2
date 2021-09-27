#!/usr/bin/env python
# encoding: utf-8
import yaml
#定义一个读取yaml的函数
def read_yaml(file):
    with open(file, "r", encoding="utf-8") as  f:
        conf = yaml.load(f, Loader=yaml.SafeLoader)
        return conf
#定义一个写人yaml的函数
def write_yaml(file,data):
    with open(file,"w",encoding="utf-8") as f:
        yaml.dump(data,f)