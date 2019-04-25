# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 21:01
# @Author  : weichenchen
# @Site    : 
# @File    : test1.py
# @Software: PyCharm

from scheduler import *
from datetime import datetime
import os
'''
U = 1.25+1.25+1.25+1=4.75
'''
# if __name__ == '__main__':
#     num_of_task_set = 5
#     num_of_bounded = 0
#     for i in range(num_of_task_set):
#         sum = i
#         str1 = "/Users/weichenchen/Desktop/Experiment1/"
#         str1 = str1 + datetime.now().strftime("%Y%m%d_%H%M%S") + "/"
#         task0 = ParallelTask(0, 5, 0.5, 1, 5, 25, 20, 20, 1, str1)
#         task1 = ParallelTask(1, 4, 0.8, 1, 5, 25, 20, 20, 1, str1)
#         task2 = ParallelTask(2, 5, 0.5, 1, 5, 25, 20, 20, 1, str1)
#         task3 = ParallelTask(3, 5, 0.5, 1, 5, 10, 10, 10, 1, str1)
#         # task0.matrix = [[0, 1, 1, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
#         # task0.pa = [1, 1, 2, 2, 1]
#         # task1.matrix = [[0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
#         # task1.pa = [2, 1, 1, 1]
#         # task2.pa = [5]
#         taskset = [task0, task1, task2, task3]
#         for task in taskset:
#             task.print_DAG()
#         # test_gedf_scheduler(taskset,3,10)
#         corenum = 5
#         time = 200
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

# 轻任务
if __name__ == '__main__':

    num_of_task_set = 100
    num_of_bounded = 0
    for i in range(num_of_task_set):
        sum = i
        str1 = "/Users/weichenchen/Desktop/ExperimentLow5.0/"
        str1 = str1 + datetime.now().strftime("%Y%m%d_%H%M%S") + "/"
        taskset = []
        for j in range(48):
            task = ParallelTask(j, 4, 0.5, 1, 5, 10, 100, 100, 1, str1)
            taskset.append(task)
        for task in taskset:
            task.print_DAG()
        corenum = 5
        time = 120
        result, finish_job, m1, m2 = gedf_scheduler(taskset, corenum, time)
        tardiness0 = finish_job[-1].tardiness
        tardiness1 = finish_job[0].tardiness
        f = open(str1 + 'result.txt', 'w+')
        for i in range(len(taskset)):
            temp = ""
            temp = temp + "task" + str(i) + ": " + str(taskset[i].size) + " nodes. " + "cost of " + str(
                taskset[i].pa) + ", period of " + str(taskset[i].period) + ".\n"
            f.write(temp)
        f.write("\n")
        first = "         "
        for i in range(corenum):
            first = first + "core" + str(i) + "   "
        f.write(first)
        f.write("\n")
        for i in range(len(result)):
            strNum = ""
            strNum = "第" + str(i).zfill(5) + "秒:"
            for j in range(corenum):
                strNum = strNum + result[i][j] + "  "

            f.write(strNum)
            f.write("\n")
        f.close()

        if m1 == m2:
            num_of_bounded = num_of_bounded + 1
        print "bound住的次数和运行的总次数为：", num_of_bounded, sum + 1


