# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 21:14
# @Author  : weichenchen
# @Site    : 
# @File    : testGeneratotAndScheduler.py
# @Software: PyCharm

from scheduler import *
from datetime import datetime
from taskSetsGenerator import *
if __name__ == '__main__':
    #tasksets = tasksets_generator(5)
    tasksets = tasksets_generator2(24, 4)
    num_of_task_set = len(tasksets)
    num_of_bounded = 0
    for i in range(num_of_task_set):
        str1 = "/Users/weichenchen/Desktop/result/"
        str1 = str1 + datetime.now().strftime("%Y%m%d_%H%M%S") + "/"
        taskset = tasksets[i]
        corenum = 8
        time = 100
        result, finish_job, m1, m2 = gedf_scheduler(taskset, corenum, time)
        path = str1
        if (not os.path.exists(path)):
            os.makedirs(path)
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