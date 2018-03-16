#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ex25.py.py
# @Author: Superhan
# @Date  : 2018/3/16
# @Desc  : created by Superhan
# @license : Copyright(C), Superhan 
# @Contact : chenchaohan@live.com 
# @Software : via PyCharm

def break_words(stuff):
    """ this funtion will break up words for us"""
    words = stuff.split(" ")
    return words

def sort_words(words):
    """sorts the words"""
    return sorted(words)

def print_first_word(words):
    """prints the first word after popping it off ."""
    word =words.pop(0)
    print word

def print_last_word(words):
    """prints the lost word after popping it off """
    word =words.pop(-1)
    print word


def sort_sentence(sentence):
    """takes in a full sentence and returns the sorted words"""
    words =break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints the first and last words of the sentence."""
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one."""
    words =sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

