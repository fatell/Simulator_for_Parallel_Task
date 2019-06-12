# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 20:44
# @Author  : weichenchen
# @Site    : 
# @File    : test0.py
# @Software: PyCharm

from scheduler import *
from datetime import datetime
import os

'''
U = 1.25+0.5+0.8+0.6+0.6+1.25=5.0  [[0]]
'''
if __name__ == '__main__':
    str1 = " "
    task = ParallelTask(0, 1, 0.5, 1, 5, 10, 100, 100, 1, str1)
    print task.matrix, task.cost
    task.matrix = [[0]]
    print task.matrix, task.cost

# 轻任务
# if __name__ == '__main__':
#
#     num_of_task_set = 10
#     num_of_bounded = 0
#     for i in range(num_of_task_set):
#         sum = i
#         str1 = "/Users/weichenchen/Desktop/ExperimentLow5.0/"
#         str1 = str1 + datetime.now().strftime("%Y%m%d_%H%M%S") + "/"
#         taskset = []
#         for j in range(50):
#             task = ParallelTask(j, 4, 0.5, 1, 5, 10, 100, 100, 1, str1)
#             taskset.append(task)
#         for task in taskset:
#             task.print_DAG()
#         corenum = 5
#         time = 120
#         result, finish_job, m1, m2 = gedf_scheduler(taskset, corenum, time)
#         tardiness0 = finish_job[-1].tardiness
#         tardiness1 = finish_job[0].tardiness
#         f = open(str1 + 'result.txt', 'w+')
#         for i in range(len(taskset)):
#             temp = ""
#             temp = temp + "task" + str(i) + ": " + str(taskset[i].size) + " nodes. " + "cost of " + str(
#                 taskset[i].pa) + ", period of " + str(taskset[i].period) + ".\n"
#             f.write(temp)
#         f.write("\n")
#         first = "         "
#         for i in range(corenum):
#             first = first + "core" + str(i) + "   "
#         f.write(first)
#         f.write("\n")
#         for i in range(len(result)):
#             strNum = ""
#             strNum = "第" + str(i).zfill(5) + "秒:"
#             for j in range(corenum):
#                 strNum = strNum + result[i][j] + "  "
#
#             f.write(strNum)
#             f.write("\n")
#         f.close()
#
#         if m1 == m2:
#             num_of_bounded = num_of_bounded + 1
#         print "bound住的次数和运行的总次数为：", num_of_bounded, sum + 1
#
#
