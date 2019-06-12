# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 10:00
# @Author  : weichenchen
# @Site    : 
# @File    : nodeInJob.py
# @Software: PyCharm
# 子节点ID cost 截止时间 释放时间 完成时间
'''
NodeInJob类：作业中的子节点类
ID：例如2-2-2代表二号任务的二号作业的二号节点
cost：节点上的执行时间
deadline：截止时间（不一定需要）
release_time：释放时间，同所属作业的释放时间相同
finish_time：该节点的完成时间
'''

from copy import copy, deepcopy


class NodeInJob(object):
    def __init__(self, ID, cost, deadline, t):
        self.ID = ID
        self.cost = deepcopy(cost)
        self.deadline = deadline
        self.release_time = t
        self.finish_time = None
