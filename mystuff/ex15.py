#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ex15.py
# @Author: Superhan
# @Date  : 2017/12/23
# @Desc  : created by Superhan
# @license : Copyright(C), Superhan 
# @Contact : chenchaohan@live.com 
# @Software : via PyCharm

from sys import argv
script , filename=argv
txt =open(filename)
print "here is your file %r :" % filename
print txt.read()

print "type the filename again:"

file_again= raw_input("> ")
txt_again=open(file_again)
print txt_again.read()



