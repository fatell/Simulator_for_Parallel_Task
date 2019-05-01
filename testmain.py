# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 20:22
# @Author  : weichenchen
# @Site    : 
# @File    : testmain.py
# @Software: PyCharm
from taskSetsGenerator import *
if __name__ == '__main__':
    tasksets = tasksets_generator2(16, 4)
    for i in range(NUM_OF_TASKSETS):
        period_list = []
        for task in tasksets[i]:
            period_list.append(task.period)
        least_common_mutiple = lcmAll(period_list)
        time = 10 * least_common_mutiple
        result, finish_job, m1, m2 = gedf_scheduler(tasksets[i], CORENUM, time)
        for item in finish_job:
            print item.ID,":",item.tardiness
        #print "m1:",m1,"m2",m2