#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ex18.py
# @Author: Superhan
# @Date  : 2017/12/25
# @Desc  : created by Superhan
# @license : Copyright(C), Superhan 
# @Contact : chenchaohan@live.com 
# @Software : via PyCharm

# this one  is like your scripts with argv
def print_two(*args):
    arg1,arg2=args
    print "arg1:%r,arg2:%r" %(arg1,arg2)

# ok ,that * args is actually pointless ,we can just do this
def print_two_again(arg1,arg2):
    print "arg1:%r,arg2:%r" %(arg1,arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1:%r" %arg1

# this one takes no arguments
def print_none():
    print "I got nothing ."

print_two("super","chen")
print_two_again("chen","chaohan")
print_one("first")
print_none()