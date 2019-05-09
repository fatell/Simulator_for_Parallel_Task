# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 18:56
# @Author  : weichenchen
# @Site    : 
# @File    : scheduler.py
# @Software: PyCharm

#from operator import itemgetter, attrgetter
from parallelTask  import *
from job  import *
from nodeInJob import *
from datetime import datetime
import  numpy as np
import math

'''
node_ToPolist_in_job：返回拓扑排序后的子任务序列，给定一个job，返回该job的子任务节点序列
子节点: 子节点ID cost 截止时间 释放时间 完成时间
'''
def node_ToPolist_in_job(job):
    size = job.size
    node_ToPolist = []
    prefixID = job.ID
    for i in job.topo_sort_list:
        ID = prefixID + "-" + str(i)
        cost = job.pa[i]
        ddl = job.deadline
        release_time = job.release_time
        node = NodeInJob(ID, cost, ddl, release_time)
        node_ToPolist.append(node)
    for i in node_ToPolist:
        print i.ID, i.cost, i.deadline, i.release_time
    return node_ToPolist
'''
pop_nodes_of_zero_in_degree: 返回入度为0的节点
'''
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

'''
delete_node_from_jobDAG: 从job_set中删除对应作业DAG的节点
    删除的节点是全局候选队列中执行时间变为0的节点，因此可能不止一个。
    删除这些节点后还要判断job_set中的作业是否有整个被删除了的，若有则删除这个作业
    
    返回：被删除的job，若没有整个被删除了的job，就返回空列表
'''
def delete_node_from_jobDAG(job_set, nodes):
    finish_job = [] # 存放完成的作业，也就是需要从job_set中删除的作业
    for node in nodes:
        temp = node.ID.split("-")
        ID = temp[0] + "-" + temp[1]

        job_ID = ID
        node_ID = int(temp[2])
        for job in job_set:
            if job.ID == job_ID:#确定是删除哪一个job中的节点
                for i in range(job.size):
                    job.matrix[node_ID][i] = 2 #将以该点为起点的边设为2 代表删除这条边
    #判断job_set中的作业是否有整个被删除了的，若有则删除这个作业
    for job in job_set:
        flag = True
        for i in range(job.size):
            for j in range(job.size):
                if job.matrix[i][j] != 2:
                    flag = False
        if flag:
            job_set.remove(job)
            finish_job.append(job)
    return finish_job


def bubble_sort(nodes):
    # 冒泡排序
    count = len(nodes)
    for i in range(0, count):
        for j in range(i + 1, count):
            if nodes[i].deadline > nodes[j].deadline:
                nodes[i], nodes[j] = nodes[j], nodes[i]
    return nodes

# 两个数的最大公约数
def gcd(a, b):
    r = a % b
    if r:
        return gcd(b, r)
    else:
        return b
#两个数的最小公倍数
def lcm(a, b):
    return a * b / gcd(a, b)
#一串数字的最小公倍数
def lcmAll(seq):
    return reduce(lcm, seq)


'''
gedf_scheduler：调度器函数
每到来一个时刻，都做以下步骤：
1：判断该时刻有没有周期来到，即是否需要释放新的作业。
2：更新job_set集合，有新释放的作业就加进去。
3：根据job_set集合更新全局候选队列nodes_to_be_sheduled，
   更新方法是将job_set集合中的每一个作业的入度为零的节点加入到全局候选队列，
   全局候选队列中的节点按照ddl排序，小的在前。
4：模拟执行：先判断全局候选队列中备选节点够不够一个核心上放一个，
   如果不够，就全选放在核心上执行，此时有核心空闲，如果够，就按照下面执行
   按照核心数m从全局候选队列中选取前m个节点执行（即cost-1操作），
   同时保存执行记录到result二维数组，行代表时刻，列代表核心
5：判断全局候选队列中是否有cost=0的节点：
   如果有，则从全局候选队列中删除该节点，同时删除job_set中对应的job图中的点，
   同时判断job_set中的作业是否有整个被删除了的，若有则删除这个作业
   再根据job_set集合更新全局候选队列nodes_to_be_sheduled，
   更新方法是将job_set集合中的每一个作业的入度为零的节点加入到全局候选队列，
   加入时需要去重，并按照ddl排序
'''
def gedf_scheduler(taskset, corenum, time):
    # for task in taskset:
    #     task.print_DAG()

    result = np.zeros([time + 1, corenum], dtype = "S10") # 结果数组，用来保存执行顺序
    t = 0
    tasknum = len(taskset)# 任务总个数
    period_set = []  # 周期列表 用来保存所有任务的周期 相同的周期也保存
    finish_job = []  # 存放执行完成的作业
    count1 = 0
    count2 = 0

    m1 = -1 # 用来保存最小公倍周期内完成的作业数
    m2 = -2 # 用来存放最小公倍周期内释放的作业数
            # 若这两个数相等则说明可以bound住
    for i in taskset:
        period_set.append(i.period)
    least_common_mutiple = lcmAll(period_set)# 最小公倍周期
    job_set = []
    nodes_to_be_sheduled = []
    while(t <= time): # 每到来一个时刻都和周期列表里的每一个周期进行对比，相等的就令该周期所属的任务释放一个新作业
        #step1&&step2：判断该时刻有没有周期来到，即是否需要释放新的作业。
        for i in range(tasknum):
            if t % period_set[i] == 0:
                # print "taskID",taskset[i].ID
                # print taskset[i].matrix
                count2 = count2 + 1
                temp = Job(taskset[i], t)
                # print temp.matrix
                # temp.print_DAG()
                # print temp.ID, temp.topo_sort_list, temp.pa, temp.deadline, temp.release_time
                # print "node topo list:"
                # node_ToPolist_in_job(temp)
                job_set.append(temp)
        #step3：根据job_set集合更新全局候选队列nodes_to_be_sheduled
        #       更新方法是将job_set集合中的每一个作业的入度为零的节点加入到全局候选队列
        #       全局候选队列中的节点按照ddl排序，小的在前。
        # for job in job_set:
        #     nodes = pop_nodes_of_zero_in_degree(job)
        #     nodes_to_be_sheduled.extend(nodes)
        #     sorted(nodes_to_be_sheduled, key = lambda node: node.deadline)

        nodes_list_before = []
        for job in job_set:
            nodes = pop_nodes_of_zero_in_degree(job)
            nodes_list_before.extend(nodes)
        for node in nodes_list_before:
            flag = True
            for i in nodes_to_be_sheduled:
                if node.ID == i.ID:
                    flag = False
            if not flag:
                continue
            else:
                nodes_to_be_sheduled.append(node)
        nodes_to_be_sheduled = sorted(nodes_to_be_sheduled, key=lambda node: node.deadline)
        #nodes_to_be_sheduled = bubble_sort(nodes_to_be_sheduled)
        # print t, "秒前备选节点信息："
        # print len(job_set), "待执行作业"
        # for node in nodes_to_be_sheduled:
        #     print node.ID, node.cost, node.deadline
        #step4：模拟执行：先判断全局候选队列中备选节点够不够一个核心上放一个，
        #       如果不够，就全选放在核心上执行，此时有核心空闲，如果够，就按照下面执行
        #       按照核心数m从全局候选队列中选取前m个节点执行（即cost-1操作），
        #       同时保存执行记录到result二维数组，行代表时刻，列代表核心
        nodes_num = len(nodes_to_be_sheduled)
        if nodes_num >= corenum:# 如果够一个核心一个
            for i in range(corenum):
                executionID = nodes_to_be_sheduled[i].ID
                result[t][i] = executionID
                nodes_to_be_sheduled[i].cost = nodes_to_be_sheduled[i].cost - 1
        else:# 如果不够一个核心一个
            for i in range(nodes_num):
                executionID = nodes_to_be_sheduled[i].ID
                result[t][i] = executionID
                nodes_to_be_sheduled[i].cost = nodes_to_be_sheduled[i].cost - 1
        #step5：判断全局候选队列中是否有cost=0的节点：如果有，则从全局候选队列中删除该节点，
        #       同时删除job_set中对应的job图中的点，同时判断job_set中的作业是否有整个被删除了的，
        #       若有则删除这个作业再根据job_set集合更新全局候选队列nodes_to_be_sheduled，
        #       更新方法是将job_set集合中的每一个作业的入度为零的节点加入到全局候选队列，加入时需要去重，并按照ddl排序

        # print t, "秒删除cost为0前备选节点信息："
        # print len(job_set), "待执行作业"
        # for node in nodes_to_be_sheduled:
        #     print node.ID, node.cost, node.deadline
        nodes_to_be_deleted = []
        for node in nodes_to_be_sheduled:
            if node.cost == 0:
                nodes_to_be_deleted.append(node)
                # print node.cost

        for node in nodes_to_be_deleted:
            nodes_to_be_sheduled.remove(node)
        # print t, "秒删除cost为0后备选节点信息："
        # print len(job_set), "待执行作业"
        # for node in nodes_to_be_sheduled:
        #     print node.ID, node.cost, node.deadline
        finish_job_this_second = delete_node_from_jobDAG(job_set, nodes_to_be_deleted)#删除操作 返回这一秒完成的job
        for job in finish_job_this_second:# 将完成时间保存下来
            job.finish_time = t
            deadline = job.deadline
            tardiness = t - deadline
            response_time = t - job.release_time
            job.response_time = response_time
            if tardiness <=0:
                job.tardiness = tardiness
            else:
                job.tardiness = tardiness
        finish_job.extend(finish_job_this_second)# 将这一秒完成的作业加入到finish_job里
        count1 = len(finish_job)
        #if t < least_common_mutiple:
        m1 = count1
        m2 = count2
        nodes_list = []
        for job in job_set:# 再次从job_set中获取入度为0的节点
            nodes = pop_nodes_of_zero_in_degree(job)
            nodes_list.extend(nodes)
        for node in nodes_list:# 加入到全局候选队列时需要去重复
            flag = True
            for i in nodes_to_be_sheduled:
                if node.ID == i.ID:
                    flag = False
            if not flag:
                continue
            else:
                nodes_to_be_sheduled.append(node)
        #sorted(nodes_to_be_sheduled, key=lambda node: node.deadline)
        nodes_to_be_sheduled = sorted(nodes_to_be_sheduled, key=lambda node: node.deadline)
        #nodes_to_be_sheduled = bubble_sort(nodes_to_be_sheduled)
        # print t, "秒后再次备选节点信息："
        # for node in nodes_to_be_sheduled:
        #     print node.ID, node.cost, node.deadline
        t = t + 1
    # print "job_num", len(job_set)
    # for i in job_set:
    #     print  "zero in-degree node of", i.ID, "job:",
    #     for j in (pop_nodes_of_zero_in_degree(i)):
    #         print j.ID
    #     i.print_DAG()
    #print result
    finish_job.sort(key=lambda item:item.tardiness)
    return result, finish_job, m1, m2

'''
Federated Scheduling:
将任务集划分为高利用率任务和低利用率任务，高利用率任务单独分配若干核心调度，
低利用率任务在一起共享剩下的核心，并且低利用率任务视为非并行任务进行调度
'''
def gedf_scheduler_FS(taskset, corenum, time):
    high_tasks = []
    low_tasks = []
    finish_job = []
    high_result = []
    for task in taskset:
        util = task.cost * 1.0 / task.period
        if util >= 1:
            high_tasks.append(task)
        else:
            low_tasks.append(task)
    cores_of_high = 0
    for task in high_tasks:
        temp_task_set = []
        L = task.critical_path_length
        C = task.cost
        D = task.deadline
        cores_num = int(math.ceil(1.0 * (C - L)/(D - L)))
        cores_of_high = cores_of_high +cores_num
        temp_task_set.append(task)
        tem_high_result, high_finish_job, high_m1, high_m2 = gedf_scheduler(temp_task_set, cores_num, time)
        high_result.append(tem_high_result)
        finish_job.extend(high_finish_job)
    cores_of_low = corenum - cores_of_high

    # 将低利用率任务转换为非并行任务
    for task in low_tasks:
        task.size = 1
        task.matrix = [[0]]
        task.critical_path_length = task.cost
    low_result, low_finish_job, low_m1, low_m2 = gedf_scheduler(low_tasks, cores_of_low, time)
    finish_job.extend(low_finish_job)
    finish_job.sort(key=lambda item: item.tardiness)
    return high_result, low_result, finish_job


# 测试数据
# task1 = ParallelTask(5, 0.1, 1, 10, 100, 10, 10, 1)
# task2 = ParallelTask(4, 0.8, 1, 10, 30, 5, 8, 1)
# task3 = ParallelTask(3, 0.7, 1, 10, 20, 4, 6, 1)
# ParallelTask(ID, size, p, min, max, fixsum, period, deadine, option, str)
# taskset = [task1, task2, task3]
'''
U = 0.8+0.5+0.8+0.8+0.8+0.8=4.5
'''
# 重任务
# if __name__ == '__main__':
#     # num_of_task_set = 5
#     num_of_task_set = 1
#     num_of_bounded = 0
#     for i in range(num_of_task_set):
#         sum = i
#         str1 = "/Users/weichenchen/Desktop/Experiment/"
#         str1 = str1 + datetime.now().strftime("%Y%m%d_%H%M%S") + "/"
#         # task0 = ParallelTask(0, 5, 0.7, 1, 5, 20, 25, 25, 1, str1)
#         # task1 = ParallelTask(1, 5, 0.8, 1, 5, 10, 20, 20, 1, str1)
#         # task2 = ParallelTask(2, 5, 0.7, 1, 5, 20, 25, 25, 1, str1)
#         # task3 = ParallelTask(3, 5, 0.6, 1, 5, 20, 25, 25, 1, str1)
#         # task4 = ParallelTask(4, 5, 0.7, 1, 5, 20, 25, 25, 1, str1)
#         # task5 = ParallelTask(5, 5, 0.5, 1, 5, 20, 25, 25, 1, str1)
#         task0 = ParallelTask(0, 5, 0.7, 1, 5, 7, 10, 10, 1, str1)
#         task1 = ParallelTask(1, 4, 0.8, 1, 5, 5, 4, 4, 1, str1)
#         task2 = ParallelTask(2, 1, 0.7, 1, 5, 5, 8, 8, 1, str1)
#         task0.matrix = [[0, 1, 1, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
#         task0.pa = [1, 1, 2, 2, 1]
#         task1.matrix = [[0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
#         task1.pa = [2, 1, 1, 1]
#         task2.pa = [5]
#         # taskset = [task0, task1, task2, task3, task4, task5]
#         taskset = [task0, task1, task2]
#         for task in taskset:
#             task.print_DAG()
#         # test_gedf_scheduler(taskset,3,10)
#         corenum = 3
#         time = 100
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
#         if m1 == m2:
#             num_of_bounded = num_of_bounded + 1
#         print "bound住的次数和运行的总次数为：", num_of_bounded, sum + 1


# 轻任务
if __name__ == '__main__':

    num_of_task_set = 100
    num_of_bounded = 0
    for i in range(num_of_task_set):
        sum = i
        str1 = "/Users/weichenchen/Desktop/ExperimentLow4.5/"
        str1 = str1 + datetime.now().strftime("%Y%m%d_%H%M%S") + "/"
        taskset = []
        for j in range(45):
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


