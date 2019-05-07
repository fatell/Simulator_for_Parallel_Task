# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 20:22
# @Author  : weichenchen
# @Site    : 
# @File    : testmain.py
# @Software: PyCharm
from taskSetsGenerator import *
if __name__ == '__main__':
    # tasksets = tasksets_generator2(6, 4)
    # print "任务生成完毕！"
    # max_tardiness_list = []
    # for i in range(NUM_OF_TASKSETS):
    #     period_list = []
    #     execution_cost = 0
    #     for task in tasksets[i]:
    #         period_list.append(task.period)
    #         execution_cost = execution_cost +task.cost
    #     least_common_mutiple = lcmAll(period_list)
    #     time = 10 * least_common_mutiple
    #     average_execution_cost = 1.0 * execution_cost / len(tasksets[i])
    #     result, finish_job, m1, m2 = gedf_scheduler(tasksets[i], CORENUM, time)
    #     print "第",i,"测试组最大tardiness：",finish_job[-1].tardiness
    #     max_tardiness = finish_job[-1].tardiness
    #     max_normalized_tardiness = 1.0 * max_tardiness / average_execution_cost
    #     max_tardiness_list.append(max_normalized_tardiness)
    #     # for item in finish_job:
    #     #     print item.ID,":",item.tardiness
    #     # print "m1:",m1,"m2",m2
    # for item in max_tardiness_list:
    #     print item
    tasksets = tasksets_generator2(4, 2)
    print "任务生成完毕！"
    average_execution_cost_list = []
    for i in range(NUM_OF_TASKSETS):
        period_list = []
        execution_cost = 0
        for task in tasksets[i]:
            period_list.append(task.period)
            execution_cost = execution_cost + task.cost
        least_common_mutiple = lcmAll(period_list)
        time = 10 * least_common_mutiple
        average_execution_cost = 1.0 * execution_cost / len(tasksets[i])
        average_execution_cost_list.append(average_execution_cost)
    print average_execution_cost_list
