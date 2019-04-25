# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 21:59
# @Author  : weichenchen
# @Site    : 
# @File    : taskSetsGenerator.py
# @Software: PyCharm
from scheduler import *
NUM_OF_TASKSETS = 20  #1000
MIN_NUM_OF_NODES = 5#50 #每个任务中子节点个数范围
MAX_NUM_OF_NODES = 25#250
MIN_WCET_OF_NODE = 50#50 #每个子节点的WCET将从这个范围中随机选取
MAX_WCET_OF_NODE = 100#100
P = 0.01 #成边概率
ALPHA = 2 #用来控制任务集的轻重任务比例，1/alpha代表重任务在任务集的比例
'''
产生一次实验所需的并行任务集的集合：每次实验产生NUM_OF_TASKSETS个任务集合，每次实验相关参数是相同的，比如总利用率
应控制相等，也就是说每次实验产生NUM_OF_TASKSETS个任务集，每个任务集的总利用率都等于固定值
Usum:任务集需要达到的总利用率，一次实验产生NUM_OF_TASKSETS个任务集，每个任务集总利用率等于该值
ID, size, p, min, max, fixsum, period, deadine, option, str
'''
def tasksets_generator(Usum):
    tasksets = [] #用来存一次实验所需产生的NUM_OF_TASKSETS个任务集
    for i in range(NUM_OF_TASKSETS):
        taskset = [] #用来存一个该循环生成的任务集
        Us = 0 #统计任务集的当前利用率之和
        ID = 0 #在当前任务集合下生成任务的ID
        while(Us <= Usum): #任务集的总利用率达到要求之前一直生成任务并添加到任务集中
            n = random.randint(MIN_NUM_OF_NODES, MAX_NUM_OF_NODES)
            task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
            L = task.critical_path_length
            C = task.cost
            period = L + random.uniform(0, ALPHA * (C - L)) # 生成合规的周期
            period = round(period)
            u = 1.0 * C / period
            deadline = period
            task.period = period
            task.deadline = deadline
            taskset.append(task)
            Us = Us + u
            ID = ID + 1
        temp =  taskset[-1]
        util = temp.cost*1.0/temp.period
        Us = Us - util
        del taskset[-1]
        targetUtil = Usum - Us
        ID = len(taskset)
        print "1ID:",ID
        if targetUtil < 1:
            task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
            print "2ID:", ID
            cost = task.cost
            period = cost/targetUtil + 1
            deadline = period
            task.period = period
            task.deadline = deadline
            taskset.append(task)
            ID = ID + 1
            print "3ID:", ID
        else: #若剩余利用率大于1 则拆分为n个1，和一个小于1的任务
            num = int(targetUtil)
            remainUtil = targetUtil - num

            task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
            cost = task.cost
            period = 1.0*cost / remainUtil + 1
            deadline = period
            task.period = period
            task.deadline = deadline
            taskset.append(task)
            ID = ID + 1
            print "4ID,", ID, "num:", num
            for j in range(num):
                task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
                period = task.cost
                deadline = period
                task.period = period
                task.deadline = deadline
                taskset.append(task)
                ID = ID + 1
                j = j + 1
            print "5ID:", ID

        # while(Us < 0.99*Usum):
        #     n = random.randint(MIN_NUM_OF_NODES, MAX_NUM_OF_NODES)
        #     task1 = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, long_period, long_period, 0, "")
        #     taskset.append(task1)
        #     Us = Us + task1.cost*1.0/task1.period
        #     ID = ID + 1
        tasksets.append(taskset)
        i = i + 1
    return tasksets


def tasksets_generator1(Usum, m):
    tasksets = [] #用来存一次实验所需产生的NUM_OF_TASKSETS个任务集
    for i in range(NUM_OF_TASKSETS):
        taskset = [] #用来存一个该循环生成的任务集
        Us = 0 #统计任务集的当前利用率之和
        ID = 0 #在当前任务集合下生成任务的ID
        while(Us <= Usum): #任务集的总利用率达到要求之前一直生成任务并添加到任务集中
            n = random.randint(MIN_NUM_OF_NODES, MAX_NUM_OF_NODES)
            task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
            L = task.critical_path_length
            C = task.cost
            period = (L + C/(0.5*m))*(1+0.25*random.gammavariate(2,1)) # 生成合规的周期
            u = 1.0 * C / period
            deadline = period
            task.period = period
            task.deadline = deadline
            taskset.append(task)
            Us = Us + u
            ID = ID + 1
        temp =  taskset[-1]
        util = temp.cost*1.0/temp.period
        Us = Us - util
        del taskset[-1]
        targetUtil = Usum - Us
        ID = len(taskset)
        print "1ID:",ID
        if targetUtil < 1:
            task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
            print "2ID:", ID
            cost = task.cost
            period = cost/targetUtil + 1
            deadline = period
            task.period = period
            task.deadline = deadline
            taskset.append(task)
            ID = ID + 1
            print "3ID:", ID
        else: #若剩余利用率大于1 则拆分为n个1，和一个小于1的任务
            num = int(targetUtil)
            remainUtil = targetUtil - num

            task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
            cost = task.cost
            period = 1.0*cost / remainUtil + 1
            deadline = period
            task.period = period
            task.deadline = deadline
            taskset.append(task)
            ID = ID + 1
            print "4ID,", ID, "num:", num
            for j in range(num):
                task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
                period = task.cost
                deadline = period
                task.period = period
                task.deadline = deadline
                taskset.append(task)
                ID = ID + 1
                j = j + 1
            print "5ID:", ID

        # while(Us < 0.99*Usum):
        #     n = random.randint(MIN_NUM_OF_NODES, MAX_NUM_OF_NODES)
        #     task1 = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, long_period, long_period, 0, "")
        #     taskset.append(task1)
        #     Us = Us + task1.cost*1.0/task1.period
        #     ID = ID + 1
        tasksets.append(taskset)
        i = i + 1
    return tasksets

if __name__ == '__main__':
    tasksets = tasksets_generator(24)
    print len(tasksets)
    for i in range(NUM_OF_TASKSETS):
        Us = 0
        heavy = 0
        light = 0
        for task in tasksets[i]:
            #task.only_print_DAG()
            util = task.cost * 1.0 / task.period
            if util >= 1:
                heavy = heavy + 1
            else:
                light = light + 1
            Us = Us + util
        bilv = 1.0 * heavy / (heavy + light)
        print "第", i, "个taskset的总利用率是：", Us, "重占比：", bilv
        i = i + 1
