# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 20:22
# @Author  : weichenchen
# @Site    : 
# @File    : testmain.py
# @Software: PyCharm

from taskSetsGenerator import *
def analyse_finish_job(finish_job, average_deadline):
    max_tardiness = finish_job[-1].tardiness
    finish_job.sort(key=lambda item: item.response_time)
    max_response_time = finish_job[-1].response_time

    sum_of_tardiness = 0
    sum_of_response_time = 0
    for job in finish_job:
        sum_of_tardiness = sum_of_tardiness + job.tardiness
        sum_of_response_time = sum_of_response_time + job.response_time
    average_of_tardiness = 1.0 * sum_of_tardiness / len(finish_job)
    average_of_response_time = 1.0 * sum_of_response_time / len(finish_job)
    max_normalized_tardiness = 1.0 * max_tardiness / average_deadline
    average_normalized_tardiness = 1.0 * average_of_tardiness / average_deadline
    max_normalized_response_time = 1.0 * max_response_time / average_deadline
    average_normalized_response_time = 1.0 * average_of_response_time / average_deadline

    analyse_result = [max_normalized_tardiness, average_normalized_tardiness, max_normalized_response_time,
                      average_normalized_response_time]
    return analyse_result


if __name__ == '__main__':
    tasksets = tasksets_generator2(4, 3)
    print "任务生成完毕！"
    analyse_list = []
    analyse_list_FS = []
    for i in range(NUM_OF_TASKSETS):
        period_list = []
        execution_cost = 0
        sum_of_deadline = 0
        for task in tasksets[i]:
            period_list.append(task.period)
            execution_cost = execution_cost + task.cost
            sum_of_deadline = sum_of_deadline + task.deadline
        least_common_mutiple = lcmAll(period_list)
        time = 5 * least_common_mutiple
        average_execution_cost = 1.0 * execution_cost / len(tasksets[i])
        average_deadline = 1.0 * sum_of_deadline / len(tasksets[i])

        result, finish_job, m1, m2 = gedf_scheduler(tasksets[i], CORENUM, time)

        analyse_result = analyse_finish_job(finish_job, average_deadline)
        high_result, low_result, FS_finish_job = gedf_scheduler_FS(tasksets[i], CORENUM, time)
        analyse_result_FS = analyse_finish_job(FS_finish_job, average_deadline)
        # 对finish_job进行数据处理分析，分别求归一化后的最大和平均tardiness，response_time
        # max_tardiness = finish_job[-1].tardiness
        # finish_job.sort(key=lambda item: item.response_time)
        # max_response_time = finish_job[-1].response_time
        #
        # sum_of_tardiness = 0
        # sum_of_response_time = 0
        # for job in finish_job:
        #     sum_of_tardiness = sum_of_tardiness + job.tardiness
        #     sum_of_response_time = sum_of_response_time + job.response_time
        # average_of_tardiness = 1.0 * sum_of_tardiness / len(finish_job)
        # average_of_response_time = 1.0 * sum_of_response_time / len(finish_job)
        # max_normalized_tardiness = 1.0 * max_tardiness / average_deadline
        # average_normalized_tardiness = 1.0 * average_of_tardiness / average_deadline
        # max_normalized_response_time = 1.0 * max_response_time / average_deadline
        # average_normalized_response_time = 1.0 * average_of_response_time / average_deadline
        #
        # analyse_result = [max_normalized_tardiness, average_normalized_tardiness, max_normalized_response_time, average_normalized_response_time]
        analyse_list.append(analyse_result)
        analyse_list_FS.append(analyse_result_FS)
        # for item in finish_job:
        #     print item.ID,":",item.tardiness
        # print "m1:",m1,"m2",m2
    print "GEDF!!!!:"
    for item in analyse_list:
        print item[0], item[1], item[2], item[3]
    print "FS!!!!!!:"
    for item in analyse_list_FS:
        print item[0], item[1], item[2], item[3]

