# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 20:22
# @Author  : weichenchen
# @Site    : 
# @File    : testmain.py
# @Software: PyCharm

from taskSetsGenerator import *
'''
数据分析主函数
参数：finish_job
'''
def analyse_finish_job(finish_job, average_deadline):
    finish_job.sort(key=lambda item: item.relative_tardiness)
    max_normalized_tardiness = finish_job[-1].relative_tardiness
    finish_job.sort(key=lambda item: item.relative_response_time)
    max_normalized_response_time = finish_job[-1].relative_response_time
    sum_of_relative_tardiness = 0
    sum_of_relative_response_time = 0
    for job in finish_job:
        sum_of_relative_tardiness = sum_of_relative_tardiness + job.relative_tardiness
        sum_of_relative_response_time = sum_of_relative_response_time + job.relative_response_time
    average_normalized_tardiness = 1.0 * sum_of_relative_tardiness / len(finish_job)
    average_normalized_response_time = 1.0 * sum_of_relative_response_time / len(finish_job)
    analyse_result = [max_normalized_tardiness, average_normalized_tardiness, max_normalized_response_time,
                      average_normalized_response_time]

    return analyse_result


if __name__ == '__main__':
    tasksets = tasksets_generator(8)
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
        #least_common_mutiple = lcmAll(period_list)
        least_common_mutiple = return_max_period(period_list)
        time = 10 * least_common_mutiple
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
    # analyse_list里每一项都如下所示：
    # [max_normalized_tardiness, average_normalized_tardiness, max_normalized_response_time,
    #                       average_normalized_response_time]
    print "GEDF!!!!:"
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    for item in analyse_list:
        print item[0], item[1], item[2], item[3]
        sum1 = sum1 + item[0]
        sum2 = sum2 + item[1]
        sum3 = sum3 + item[2]
        sum4 = sum4 + item[3]
    average1 = 1.0 * sum1 / len(analyse_list)
    average2 = 1.0 * sum2 / len(analyse_list)
    average3 = 1.0 * sum3 / len(analyse_list)
    average4 = 1.0 * sum4 / len(analyse_list)

    print "平均max_normalized_tardiness, 平均average_normalized_tardiness," \
          "平均max_normalized_response_time,平均average_normalized_response_time:"
    print average1
    print average2
    print average3
    print average4

    print "FS!!!!!!:"
    sum5 = 0
    sum6 = 0
    sum7 = 0
    sum8 = 0
    for item in analyse_list_FS:
        print item[0], item[1], item[2], item[3]
        sum5 = sum5 + item[0]
        sum6 = sum6 + item[1]
        sum7 = sum7 + item[2]
        sum8 = sum8 + item[3]
    average5 = 1.0 * sum5 / len(analyse_list_FS)
    average6 = 1.0 * sum6 / len(analyse_list_FS)
    average7 = 1.0 * sum7 / len(analyse_list_FS)
    average8 = 1.0 * sum8 / len(analyse_list_FS)

    print "平均max_normalized_tardiness, 平均average_normalized_tardiness," \
          "平均max_normalized_response_time,平均average_normalized_response_time:"
    print average5
    print average6
    print average7
    print average8

