# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 19:39
# @Author  : weichenchen
# @Site    : 
# @File    : cpu.py
# @Software: PyCharm
'''
CPU类：CPU核心
ID：CPU核心的ID
flag：该核心是否空闲，0代表空闲，1代表被占用，不空闲
ExecutingNode：若flag为1，则此项为正在执行的节点，否则，此项为None
'''
class CPU(object):
    def __init__(self, ID):
        self.ID = ID
        self.flag = 0
        self.ExecutingNode = None
