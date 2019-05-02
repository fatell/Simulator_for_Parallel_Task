# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 20:22
# @Author  : weichenchen
# @Site    : 
# @File    : testmain.py
# @Software: PyCharm
from taskSetsGenerator import *
if __name__ == '__main__':
    tasksets = tasksets_generator2(6, 4)
    max_tardiness_list = []
    for i in range(NUM_OF_TASKSETS):
        period_list = []
        for task in tasksets[i]:
            period_list.append(task.period)
        least_common_mutiple = lcmAll(period_list)
        time = 10 * least_common_mutiple
        result, finish_job, m1, m2 = gedf_scheduler(tasksets[i], CORENUM, time)
        print "第",i,"测试组最大tardiness：",finish_job[-1].tardiness
        max_tardiness_list.append(finish_job[-1].tardiness)
        # for item in finish_job:
        #     print item.ID,":",item.tardiness
        # print "m1:",m1,"m2",m2
    for item in max_tardiness_list:
        print item