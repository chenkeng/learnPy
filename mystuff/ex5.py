#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ex5.py
# @Author: Superhan
# @Date  : 2017/12/20
# @Desc  : created by Superhan
# @license : Copyright(C), Superhan 
# @Contact : chenchaohan@live.com 
# @Software : via PyCharm

my_name="superhan"
my_age=28 #not a lie
my_height=172 # cm
my_weight=70 # kg
my_eyes="black"
my_teeth="white"
my_hair="black"

print "Let's talk about %s." % my_name
print "He's %d cm tall ." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and % s hair." %(my_eyes,my_hair)
print "his teeth are usually %s depending on the tea ." % my_teeth

# this line is tricky ,try to get it exactly right
print "If I add %d ,%d, and % d I get %d." %(my_age,my_height,my_weight,my_age+my_height+my_weight)