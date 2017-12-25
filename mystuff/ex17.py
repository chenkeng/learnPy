#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ex17.py
# @Author: Superhan
# @Date  : 2017/12/25
# @Desc  : created by Superhan
# @license : Copyright(C), Superhan 
# @Contact : chenchaohan@live.com 
# @Software : via PyCharm

from sys import argv
from os.path import exists

script, from_file,to_file=argv
print "Copying from %s to %s" % (from_file,to_file)

# we could do these two on one line too,how?

input =open(from_file)
indata=input.read()

print "the input file is %d bytes long " % len(indata)

print "does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."

raw_input()

output =open(to_file,'w')
output.write(indata)

print "Alright,all done."

output.close()
input.close()
