#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ex16.py
# @Author: Superhan
# @Date  : 2017/12/25
# @Desc  : created by Superhan
# @license : Copyright(C), Superhan 
# @Contact : chenchaohan@live.com 
# @Software : via PyCharm

from sys import argv
script, filename=argv
print "we're going to erase %r ." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")

print "Opening the file..."
target =open(filename,"w")

print "Truncating the file. GOodbye!"
target.truncate() # 清空文件

print "Now i am going to ask yu for three lines."

line1 =raw_input("line1:")
line2=raw_input("line2:")
line3=raw_input("line3:")

print "I'm going to write these to the file ."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally ,we close it "
target.close()