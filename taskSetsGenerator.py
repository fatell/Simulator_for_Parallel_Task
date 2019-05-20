# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 21:59
# @Author  : weichenchen
# @Site    : 
# @File    : taskSetsGenerator.py
# @Software: PyCharm
from scheduler import *
NUM_OF_TASKSETS = 3  #1000
CORENUM = 16
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
'''
此种生成方法中周期period采用可以控制轻重比的方式
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
            period = int(round(period))
            period = roundup_pow_of_two(period)  # 将period设置为最靠近的2的幂指数 肯定是放大了的
                                                 # 因此可以保证至少是alpha倍
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
            period = int(cost/targetUtil + 1)
            period = roundup_pow_of_two(period)  # 将period设置为最靠近的2的幂指数 肯定是放大了的
                                                 # 因此可以保证至少是alpha倍
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
            period = int(1.0*cost / remainUtil + 1)
            period = roundup_pow_of_two(period)  # 将period设置为最靠近的2的幂指数 肯定是放大了的
            # 因此可以保证至少是alpha倍
            deadline = period
            task.period = period
            task.deadline = deadline
            taskset.append(task)
            ID = ID + 1
            print "4ID,", ID, "num:", num
            for j in range(num):
                task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
                period = task.cost
                period = roundup_pow_of_two(period)  # 将period设置为最靠近的2的幂指数 肯定是放大了的
                # 因此可以保证至少是alpha倍
                deadline = period
                task.period = period
                task.deadline = deadline
                taskset.append(task)
                ID = ID + 1
            print "5ID:", ID

        # while(Us < 0.99*Usum):
        #     n = random.randint(MIN_NUM_OF_NODES, MAX_NUM_OF_NODES)
        #     task1 = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, long_period, long_period, 0, "")
        #     taskset.append(task1)
        #     Us = Us + task1.cost*1.0/task1.period
        #     ID = ID + 1
        tasksets.append(taskset)
    return tasksets

'''
此种生成方式中周期period为采用gamma分布的方式
m：核心数
'''
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
            period = int((L + C/(0.5*m))*(1+0.25*random.gammavariate(2,1))) # 生成合规的周期
            period = roundup_pow_of_two(period)  # 将period设置为最靠近的2的幂指数 肯定是放大了的
            # 因此可以保证至少是alpha倍
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
        #print "1ID:",ID
        if targetUtil < 1:
            task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
            #print "2ID:", ID
            cost = task.cost
            period = int(cost/targetUtil + 1)
            period = roundup_pow_of_two(period)  # 将period设置为最靠近的2的幂指数 肯定是放大了的
            # 因此可以保证至少是alpha倍
            deadline = period
            task.period = period
            task.deadline = deadline
            taskset.append(task)
            ID = ID + 1
            #print "3ID:", ID
        else: #若剩余利用率大于1 则拆分为n个1，和一个小于1的任务
            num = int(targetUtil)
            remainUtil = targetUtil - num

            task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
            cost = task.cost
            period = int(1.0*cost / remainUtil + 1)
            period = roundup_pow_of_two(period)  # 将period设置为最靠近的2的幂指数 肯定是放大了的
            # 因此可以保证至少是alpha倍
            deadline = period
            task.period = period
            task.deadline = deadline
            taskset.append(task)
            ID = ID + 1
            #print "4ID,", ID, "num:", num
            for j in range(num):
                task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
                period = task.cost
                period = roundup_pow_of_two(period)  # 将period设置为最靠近的2的幂指数 肯定是放大了的
                # 因此可以保证至少是alpha倍
                deadline = period
                task.period = period
                task.deadline = deadline
                taskset.append(task)
                ID = ID + 1
            #print "5ID:", ID

        # while(Us < 0.99*Usum):
        #     n = random.randint(MIN_NUM_OF_NODES, MAX_NUM_OF_NODES)
        #     task1 = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, long_period, long_period, 0, "")
        #     taskset.append(task1)
        #     Us = Us + task1.cost*1.0/task1.period
        #     ID = ID + 1
        tasksets.append(taskset)
    return tasksets
'''
获取比num大的，最靠近num的2的次方的整数
'''
def roundup_pow_of_two(num):
    rval = 1
    while(rval < num):
        rval = rval * 2
    return rval

'''
此种生成方式控制任务集里周期同关键路径长度的比值关系
Usum:控制任务集总利用率为该值
alpha：周期和关键路径长度的倍数关系，即period >= alpha * L
'''
def tasksets_generator2(Usum, alpha):
    tasksets = [] # 用来存一次实验所需产生的NUM_OF_TASKSETS个任务集
    for i in range(NUM_OF_TASKSETS):
        print i
        taskset = [] # 用来存当前循环生成的任务集
        Us = 0 # 用来统计当前任务集的利用率之和 初始化为0
        ID = 0 # 当前任务集合下生成任务的ID
        while (Us <= Usum): # 任务集的总利用率达到要求之前一直生成任务并添加到任务集中
            n = random.randint(MIN_NUM_OF_NODES, MAX_NUM_OF_NODES) # 确定生成的并行任务中子任务个数
            task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
            # 生成方式设为0，即每个子节点的开销都从一个范围内随机选取
            # 一些参数并不需要 因此先随便指定 后面再进行修改 例如周期和截止时间
            L = task.critical_path_length # 返回该任务的关键路径长度
            C = task.cost # 返回WCET
            period = alpha * L # 设置周期为关键路径长度的alpha倍 事实上应该设为至少alpha倍
            period = roundup_pow_of_two(period) # 将period设置为最靠近的2的幂指数 肯定是放大了的
                                                # 因此可以保证至少是alpha倍
            u = 1.0 * C / period # 计算该任务的利用率
            deadline = period
            task.period = period
            task.deadline = deadline
            Us = Us + u
            ID = ID + 1
            taskset.append(task)
        print 1, taskset
        temp = taskset[-1] # 最后加入的那个任务导致总利用率超标 需要删掉
        temp_util = temp.cost * 1.0 / temp.period
        Us = Us -temp_util # 减去最后加入的那个任务的利用率
        del taskset[-1]
        #targetUtil = Usum - Us # 为了达标还所需的利用率
        ID = len(taskset)

        while(Us < Usum):
            targetUtil = Usum - Us
            task = ParallelTask(ID, n, P, MIN_WCET_OF_NODE, MAX_WCET_OF_NODE, 100, 100, 100, 0, "")
            cost = task.cost
            L = task.critical_path_length
            period = alpha * L
            targetPeriod = int(cost / targetUtil + 1) #根据剩余利用率反推出来所需的周期
            if(targetPeriod > period): # 如果所需要的周期大于计算得到周期 那正好可以使用前者
                period = targetPeriod
                period = roundup_pow_of_two(period)# 将period设置为最靠近的2的幂指数 肯定是放大了的
                                                   # 因此可以保证至少是alpha倍
                deadline = period
                task.period = period
                task.deadline = deadline
                taskset.append(task)
                #print ID,task
                break
            else: # targetPeriod <= alpha * L
                period = period
                period = roundup_pow_of_two(period)  # 将period设置为最靠近的2的幂指数 肯定是放大了的
                                                     # 因此可以保证至少是alpha倍
                deadline = period
                task.period = period
                task.deadline = deadline
                taskset.append(task)
                #print ID, task
            ID = ID + 1
            Us = Us + (cost / period)
        #print 2, taskset
        tasksets.append(taskset)
    return tasksets

if __name__ == '__main__':
    #tasksets = tasksets_generator(24)
    #tasksets = tasksets_generator1(24,32)
    tasksets = tasksets_generator2(6,4)
    print len(tasksets)
    for i in range(NUM_OF_TASKSETS):
        period_list = []
        Us = 0
        heavy = 0
        light = 0
        for task in tasksets[i]:
            #task.only_print_DAG()
            period_list.append(task.period)
            util = task.cost * 1.0 / task.period
            if util >= 1:
                heavy = heavy + 1
            else:
                light = light + 1
            Us = Us + util
        bilv = 1.0 * heavy / (heavy + light)
        least_common_mutiple = lcmAll(period_list)
        print "第", i, "个taskset的总利用率是：", Us, len(tasksets[i]),"个任务", "重占比：", bilv
        print "最小公倍周期是：", least_common_mutiple
