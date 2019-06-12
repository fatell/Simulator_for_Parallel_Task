# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 10:56
# @Author  : weichenchen
# @Site    : 
# @File    : testlist.py
# @Software: PyCharm

from nodeInJob import *
from datetime import datetime
import os

'''
class NodeInJob(object):
    def __init__(self, ID, cost, deadline, t):
        self.ID = ID
        self.cost = cost
        self.deadline = deadline
        self.release_time = t
        self.finish_time = None
'''


def gcd(a, b):
    r = a % b
    if r:
        return gcd(b, r)
    else:
        return b


# print gcd(13, 6)

def lcm(a, b):
    return a * b / gcd(a, b)


# print lcm(12, 6)

def lcmAll(seq):
    return reduce(lcm, seq)


lis = [2, 2, 4, 5]
print lcmAll(lis)
