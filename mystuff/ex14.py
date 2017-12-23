#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ex14.py
# @Author: Superhan
# @Date  : 2017/12/23
# @Desc  : created by Superhan
# @license : Copyright(C), Superhan 
# @Contact : chenchaohan@live.com 
# @Software : via PyCharm

from sys import argv
script, user_name = argv
prompt="> "

print "Hi %s, I'm the %s script ." %(user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
print "%s" % likes

print "where do you live %s?" % user_name
lives = raw_input(prompt)
print "%s" % lives

print "what kind of computer do you have?"
computer = raw_input(prompt)
print "%s" % computer

print """  
Alright,so you said %r about liking me .
you live in $r . not sure where that is .
and you have a %r computer . nice .
""" % (likes, lives, computer)