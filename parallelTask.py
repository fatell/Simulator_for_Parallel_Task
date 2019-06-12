# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 21:38
# @Author  : weichenchen
# @Site    : 
# @File    : parallelTask.py
# @Software: PyCharm
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

'''
ParallelTask：任务类，生成并行任务的DAG图，指定周期，DDL等
'''


class ParallelTask(object):
    # 节点个数 产生边的概率 节点payload的最小值 节点payload的最大值 任务总work值为某一固定值 周期 DDL 选项 保存的路径
    # 选项为1时产生总work值为固定值的任务，0时产生某一范围的子节点

    def __init__(self, ID, size, p, min, max, fixsum, period, deadine, option, str):
        self.ID = ID
        self.size = size
        self.p = p
        self.min = min
        self.max = max
        self.fixsum = fixsum
        self.period = period
        self.deadline = deadine
        self.option = option
        self.str = str
        self.cost = None
        self.matrix = [[0 for j in range(self.size)] for i in range(self.size)]
        self.pa = None
        self.critical_path_length = None
        self.topo_sort_list = None

        # 按照概率产生DAG图
        am = [[0 for j in range(self.size)] for i in range(self.size)]  # am为邻接矩阵
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if (random.random() < self.p):
                    am[i][j] = 1
                else:
                    am[i][j] = 0
        unconn_point = self.weak_conn_add(am)
        while (unconn_point != 0):
            target = unconn_point
            source = random.randint(0, target - 1)
            am[source][target] = 1
            unconn_point = self.weak_conn_add(am)
        am = self.adjust_matrix(am)
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] = am[i][j]

        # 计算拓扑排序 用来gedf
        n = self.size
        # 获取所有入度为0的结点
        q = []
        for j in range(n):
            flag = True
            for i in range(n):
                if am[i][j] == 1:
                    flag = False
                    break
            if flag:
                q.insert(0, j)

        topo = []  # 记录结果
        while len(q) > 0:
            # p出队，把从p出度的数据置为0
            p = q.pop()
            topo.append(p)
            for i in range(n):
                if am[p][i] == 1:
                    am[p][i] = 0  # 去掉连通
                    # 如果结点i的入度为0则入队结点i
                    in_degree_count = 0
                    for u in am:
                        if u[i] == 1:
                            in_degree_count += 1
                    if in_degree_count == 0:
                        q.insert(0, i)
        self.topo_sort_list = topo

        # 产生节点payload在范围(min, max)内
        if (option == 0):
            size = self.size
            min = self.min
            max = self.max
            pa = [0 for i in range(size)]
            S = 0
            for i in range(size):
                pa[i] = random.randint(min, max)
                S = S + pa[i]
            self.cost = S
            self.pa = pa

        # 产生总work为固定值的DAG
        if (option == 1):
            size = self.size
            fixSum = self.fixsum
            pa = [0 for i in range(size)]
            l = random.sample([i + 1 for i in range(fixSum - 1)], size - 1)
            l.insert(0, 0)
            l.append(fixSum)
            l.sort()
            for i in range(size):
                pa[i] = l[i + 1] - l[i]
            # print pa, sum(pa)
            self.cost = sum(pa)
            self.pa = pa

        # 计算关键路径长度
        size = len(am)
        source_node = []
        critical_path_length = 0
        stack = []
        dist = [0 for i in range(size)]
        for j in range(size):
            flag = True
            for i in range(size):
                if self.matrix[i][j] == 1:
                    flag = False
            if flag:
                source_node.append(j)
        # print source_node

        # print dist
        for i in range(len(source_node)):
            # print source_n  # print dist
            # print paode[i]
            stack.append(source_node[i])
            dist[source_node[i]] = pa[source_node[i]]

        while (len(stack) != 0):
            current = stack.pop(0)
            for i in range(size):
                if self.matrix[current][i] == 1:
                    temp = dist[current] + pa[i]
                    if temp > dist[i]:
                        dist[i] = temp
                        stack.append(i)
                        if temp > critical_path_length:
                            critical_path_length = temp
                            self.critical_path_length = critical_path_length
                            # print "少时诵诗书所所所所",critical_path_length

    # 调整DAG图，使其只有一个源节点和终结点
    @staticmethod
    def adjust_matrix(am):
        size = len(am)
        start = [True for i in range(size)]
        end = [True for i in range(size)]
        for i in range(size):
            for j in range(size):
                if (am[j][i] == 1):
                    start[i] = False
                if (am[i][j] == 1):
                    end[i] = False
        for i in range(size):
            if (start[i] == True):
                true_start = i
                start[i] = False
                break
        for i in range(size):
            if (start[i] == True):
                am[true_start][i] = 1
        for i in range(size - 1, -1, -1):
            if (end[i] == True):
                true_end = i
                end[i] = False
                break
        for i in range(size):
            if (end[i] == True):
                am[i][true_end] = 1
        return am

    # 找出不连通的节点
    # 若返回0说明全都连通 因为是从节点0开始深搜的，所以0必在连通里
    @staticmethod
    def weak_conn_add(am):
        if (am is None):
            print "null"
            return
        size = len(am)
        visited = [False for i in range(size)]
        # print visited
        stack = [0]
        while (len(stack) > 0):
            current = stack.pop()
            visited[current] = True
            for i in range(0, size):
                if (am[current][i] == 1 and visited[i] == False) or (am[i][current] == 1 and visited[i] == False):
                    stack.append(i)
        # print visited
        unconn_point = 0
        for i in range(0, size):
            if not visited[i]:
                unconn_point = i
        return unconn_point

    # 打印邻接矩阵
    def print_adjust_matrix(self):
        print self.matrix

    # 打印周期
    def print_period(self):
        print self.period

    # 打印任务节点个数
    def print_size(self):
        print self.size

    # 打印DDL
    def print_ddl(self):
        print self.deadline

    # 打印任务的WCET
    def print_WCET(self):
        print self.cost

    # 打印拓扑排序结果
    def print_topo_sort(self):
        print self.topo_sort_list

    # 打印任务各个节点的payload列表
    def print_payload_list(self):
        print self.pa

    # 打印关键路径长度
    def print_critical_path_length(self):
        print self.critical_path_length

    # 可视化任务生成DAG图
    def print_DAG(self):
        size = len(self.matrix)
        am = self.matrix
        Matrix = np.array(am)
        G = nx.from_numpy_matrix(Matrix, create_using=nx.DiGraph())
        nx.draw_networkx(G, pos=nx.circular_layout(G), nodesize=size, alpha=1)
        # S, pa = gen_node_load(size, 1, 10)
        # print pa
        # print "关键路径长度为：", calculate_critical_path_length(am, pa)
        # topo = topological_sort(am)
        # print "拓扑排序是：", topo
        path = self.str + "Task/"
        if (not os.path.exists(path)):
            os.makedirs(path)
        path = path + "Graph of " + str(self.ID) + "task"
        title = "Graph of " + str(self.ID) + "task"
        plt.title(title)
        plt.savefig(path + ".png", format="PNG")
        plt.cla()
        # plt.show()

    # 可视化任务生成DAG图
    def only_print_DAG(self):
        size = len(self.matrix)
        am = self.matrix
        Matrix = np.array(am)
        G = nx.from_numpy_matrix(Matrix, create_using=nx.DiGraph())
        nx.draw_networkx(G, pos=nx.circular_layout(G), nodesize=size, alpha=1)
        title = "Graph of " + str(self.ID) + "task"
        plt.title(title)
        plt.show()
        plt.cla()


if __name__ == '__main__':
    task = ParallelTask(0, 5, 0.5, 1, 10, 100, 10, 10, 1)
    print "matrix:"
    task.print_adjust_matrix()
    task.print_DAG()
    print "critical_path:"
    task.print_critical_path_length()
    print "ddl:"
    task.print_ddl()
    print "pa:"
    task.print_payload_list()
    print "period:"
    task.print_period()
    print "size:"
    task.print_size()
    print "topo_sort:"
    task.print_topo_sort()
    print "WCET:"
    task.print_WCET()
