# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 19:34
# @Author  : weichenchen
# @Site    : 
# @File    : testPopZeroInDegreeNode.py
# @Software: PyCharm
from parallelTask import *
from job import *
from nodeInJob import *
import numpy as np


def pop_nodes_of_zero_in_degree(job):
    n = job.size
    # 获取所有入度为0的结点
    matrix = job.matrix
    q = []
    for j in range(n):
        flag = True
        for i in range(n):
            if matrix[i][j] == 1:
                flag = False
                break
        if flag and matrix[j][j] != 2:
            ID = job.ID + "-" + str(j)
            cost = job.pa[j]
            ddl = job.deadline
            release_time = job.release_time
            node = NodeInJob(ID, cost, ddl, release_time)
            q.append(node)
    return q


# 测试数据
# task1 = ParallelTask(5, 0.1, 1, 10, 100, 10, 10, 1)
# task2 = ParallelTask(4, 0.8, 1, 10, 30, 5, 8, 1)
# task3 = ParallelTask(3, 0.7, 1, 10, 20, 4, 6, 1)
# ParallelTask(ID, size, p, min, max, fixsum, period, deadine, option)
if __name__ == '__main__':
    i = "1-10-0"
    m = i.split("-")

    print m
