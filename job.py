# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/31 16:18
# @Author  : weichenchen
# @Site    : 
# @File    : job.py
# @Software: PyCharm
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from copy import copy,deepcopy
import os
'''
Job类：task周期产生的作业
ID：x-y，x代表任务ID，属于哪一个任务；y代表该作业是该任务释放的第几个作业
size：DAG中节点个数，直接继承从属任务的size
release_time：该作业的释放时间
deadline：绝对截止时限
cost：总执行时间
matrix：以邻接矩阵形式表示的DAG图
pa：每个节点上的执行时间，例如有五个节点，执行时间分别为2，2，4，6，5，则pa就是[2,2,4,6,5]
critical_path_length：关键路径长度
topo_sort_list：拓扑排序结果
'''
class Job(object):
    def __init__(self, ParallelTask, t):
        self.ID = str(ParallelTask.ID) + '-' + str(t/ParallelTask.period)
        self.size = ParallelTask.size
        self.release_time = t
        self.deadline = t + ParallelTask.deadline
        self.relative_deadline = ParallelTask.deadline
        self.cost = ParallelTask.cost
        self.matrix = deepcopy(ParallelTask.matrix)
        self.pa = ParallelTask.pa
        self.critical_path_length = ParallelTask.critical_path_length
        self.topo_sort_list = ParallelTask.topo_sort_list
        self.str = ParallelTask.str
        self.finish_time = None
        self.tardiness = None
        self.response_time = None
        self.relative_tardiness = None
        self.relative_response_time = None

    #可视化任务生成DAG图
    def print_DAG(self):
        size=len(self.matrix)
        am=self.matrix
        Matrix = np.array(am)
        G = nx.from_numpy_matrix(Matrix, create_using=nx.DiGraph())
        nx.draw_networkx(G, pos=nx.circular_layout(G), nodesize=size, alpha=1)
        #S, pa = gen_node_load(size, 1, 10)
        #print pa
        #print "关键路径长度为：", calculate_critical_path_length(am, pa)
        #topo = topological_sort(am)
        #print "拓扑排序是：", topo

        path = self.str + "Job/"
        if (not os.path.exists(path)):
            os.makedirs(path)
        path = path + "Graph of " + str(self.ID) + "job"
        title = "Graph of " + str(self.ID) + "job"
        plt.title(title)
        plt.savefig(path + ".png", format="PNG")
        plt.cla()
        #plt.show()


