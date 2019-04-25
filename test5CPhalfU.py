# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 15:54
# @Author  : weichenchen
# @Site    : 
# @File    : test5CPhalfU.py
# @Software: PyCharm

from scheduler import *
from datetime import datetime
import os
'''
U = 0.7+0.7+0.7+0.9+0.9=3.9
不控制critical path 长度的时候，20次就出现一次不能bound，因此加上关键路径长度为0.5倍
的相对截止时间（隐式下等于周期）
'''
if __name__ == '__main__':

    num_of_task_set = 1000
    num_of_bounded = 0
    for i in range(num_of_task_set):
        sum = i
        str1 = "/Users/weichenchen/Desktop/Experiment5/"
        str1 = str1 + datetime.now().strftime("%Y%m%d_%H%M%S") + "/"
        num1 = 0
        num2 = 0
        taskset = []
        # 产生三个0.7的任务且cp<=0.5d
        while( num1 < 3):
            task = ParallelTask(0, 10, 0.5, 1, 5, 42, 60, 60, 1, str1)
            up_of_cp = task.deadline * 0.5

            if (task.critical_path_length <= up_of_cp):
                taskset.append(task)
                num1 = num1 + 1
        # 产生2个0.9的任务且cp<=0.5d
        while (num2 < 2):
            task = ParallelTask(4, 6, 0.5, 1, 5, 18, 20, 20, 1, str1)
            up_of_cp = task.deadline * 0.5

            if (task.critical_path_length <= up_of_cp):
                taskset.append(task)
                num2 = num2 + 1

        for j in range(len(taskset)):
            taskset[j].ID = j
        for j in range(len(taskset)):
            #print taskset[j].ID
            taskset[j].print_DAG()
        # test_gedf_scheduler(taskset,3,10)
        corenum = 5
        time = 150
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
