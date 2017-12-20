#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ex8.py
# @Author: Superhan
# @Date  : 2017/12/20
# @Desc  : created by Superhan
# @license : Copyright(C), Superhan 
# @Contact : chenchaohan@live.com 
# @Software : via PyCharm

formatter="%r %r %r %r"
print formatter %(1,2,3,4)
print formatter %("one","two",'three','four')
print formatter % (True, False, True, False) #  不明白此处如果是小些的  true false 就是报错
print formatter % (formatter,formatter,formatter,formatter)
print formatter %(
    "I had this thing .",
    "that you could type up right .",
    "but it did't sing .",
    "so i said goodnight."
)



