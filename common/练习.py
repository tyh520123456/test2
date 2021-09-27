#!/usr/bin/env python
# encoding: utf-8
import jsonpath
d={"key1":{"key2":{"key3":"python"}}}

print(jsonpath.jsonpath(d,'$..key3')[0])
