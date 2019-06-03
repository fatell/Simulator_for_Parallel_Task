# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 15:38
# @Author  : weichenchen
# @Site    : 
# @File    : taskSetsAnalysis.py
# @Software: PyCharm

from taskSetsGenerator import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# from pandas import DataFrame
NUM_OF_TASKSETS = 300  #1000
CORENUM = 16
MIN_NUM_OF_NODES = 5#50 #每个任务中子节点个数范围
MAX_NUM_OF_NODES = 25#250
MIN_WCET_OF_NODE = 20#50 #每个子节点的WCET将从这个范围中随机选取
MAX_WCET_OF_NODE = 70#100
P = 0.6 #成边概率
ALPHA = 2 #用来控制任务集的轻重任务比例，1/alpha代表重任务在任务集的比例


if __name__ == '__main__':
    # ratio_base = 0.1
    # for i in range(10):
    #     ratio = 0.1 + ratio_base * i
    #     Utilization = CORENUM * ratio
    #     print ratio, Utilization
    dict = {"util": [],
            "WCET": [],
            "Deadline": [],
            "WCET_to_CriticalPathLength": [],
            "density": []}
    for i in range(CORENUM/2, CORENUM + 1, 1):
        print i
        # tasksets = tasksets_generator1(i, CORENUM)
        tasksets = tasksets_generator(i)
        for taskset in tasksets:
            for task in taskset:
                util = i
                WCET = task.cost
                Deadline = task.deadline
                CP = task.critical_path_length
                WCET_to_CriticalPathLength = 1.0 * WCET / CP
                density = 1.0 * WCET / Deadline
                # util_list = dict["util"]
                dict["util"].append(util)
                # WCET_list = dict["WCET"]
                dict["WCET"].append(WCET)
                # Deadline_list = dict["Deadline"]
                dict["Deadline"].append(Deadline)
                # n4_list = dict["WCET_to_CriticalPathLength"]
                dict["WCET_to_CriticalPathLength"].append(WCET_to_CriticalPathLength)
                # n5_list = dict["density"]
                dict["density"].append(density)
    #print max(dict["Deadline"]), min((dict["Deadline"]))
    #print dict["Deadline"]
    new_Deadline = []
    new_index = []
    for index, data in enumerate(dict["Deadline"]):
        if data > 0 and data < 6000:
            new_Deadline.append(data)
            new_index.append(index)

    new_Util = []

    for i in range(len(dict["util"])):
        if i in new_index:
            new_Util.append(dict["util"][i])


    new_dict = {"util":new_Util, "deadline":new_Deadline}

    plt.figure(figsize=(16, 10))
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.subplot(221)
    ax = sns.violinplot(x="util", y="WCET", data=dict, cut=0)
    # ax.set_title("Worst-case execution times")
    plt.xlabel(u"利用率", fontsize=18)
    plt.ylabel(u"最坏执行时间", fontsize=18)
    plt.subplot(222)
    ax = sns.violinplot(x="util", y="deadline", data=new_dict, cut=0)
    # ax.set_title("Deadline")
    plt.xlabel(u"利用率", fontsize=18)
    plt.ylabel(u"相对截止时间", fontsize=18)
    plt.subplot(223)
    ax = sns.violinplot(x="util", y="WCET_to_CriticalPathLength", data=dict, cut=0)
    # ax.set_title("Worst-case execution times to Critical Path Ratio")
    plt.xlabel(u"利用率", fontsize=18)
    plt.ylabel(u"最坏执行时间/关键路径长度", fontsize=18)
    plt.subplot(224)
    ax = sns.violinplot(x="util", y="density", data=dict, cut=0)
    # ax.set_title("Density")
    plt.xlabel(u"利用率", fontsize=18)
    plt.ylabel(u"密度", fontsize=18)

    plt.suptitle(u"DAG任务集静态属性分布（隐式截止时间，16核心，Ph = 0.50，Pl = 0.50)", fontsize=18)
    plt.savefig(u"/Users/weichenchen/Desktop/实时系统/实验结果/m16HLR23not.png", format="PNG")
    plt.show()




